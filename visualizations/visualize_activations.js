
document.getElementById("updateChart").addEventListener("click", function() {
    var epochNum = document.getElementById('epochNum').value;
    var layerNum = document.getElementById('layerNum').value - 1;

    console.log('epoch: ', epochNum, ' , layer: ', layerNum);

    // d3.select("svg").remove();

layers = []

d3.text('epoch=' + epochNum + '_average_over_100.csv', function(error, textString){
	//get data
	var data = d3.tsv.parseRows(textString)
	for(d in data){
		var row = data[d][0].split(', ');
		var layer = [];
		for(r in row){
			layer.push(parseFloat(row[r]));
		}

		layers.push(layer);
	}
	//console.log(layers);
	//set up container
	margins = [5, 15, 5, 5];
	w = 1200 - margins[0] - margins[2];
	h = 600 - margins[1] - margins[3];
	p = margins[3] + 10;
	var svg = d3.select('body').append('svg:svg')
			  .attr('width', w)
			  .attr('height', h)
			  .append('svg:g')
			  .attr('transform', 'translate (' + margins[0] + ',' + margins[3] + ')');

	//graph data as histogram
	var vizLayer = layers[layerNum];
	//console.log(vizLayer);
	var data = d3.layout.histogram()(vizLayer);
	var y = d3.scale.linear()
    .domain([0, d3.max(data, function(d) { return d.y; })])
    .range([h, 0]);
	var x = d3.scale.linear().domain([0,data.length]).range([50,w]);
	var xScale = d3.scale.linear().domain([0, d3.max(data, function(d){ return d.x;})]).range([0,w]);
	var xAxis = d3.svg.axis().scale(xScale).orient("top");
	var yAxis = d3.svg.axis().scale(y).orient("right");

	svg.append("g")
		.attr("class", "axis") 
		.attr("transform", "translate(5,0)")
    	.call(yAxis);



	var bar = svg.selectAll(".bar")
    .data(data)
    .enter().append("g")
    .attr("class", "bar")
    .attr("transform", function(d,i) { 
    	return "translate(" + x(i) + "," + y(d.y) + ")"; });

	bar.append("rect")
	    .attr("x", 1)
	    .attr("width", 
	    	w / data.length)
	    .attr("height", function(d) { 
	    	console.log(d.y);
	    	return h - y(d.y); });
	console.log(data);

	bar.append("text")
    .attr("dy", ".75em")
    .attr("y", 6)
    .attr("x", (w / data.length) / 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return d.x.toFixed(3); });

/*    svg.append("g")
    	.attr("class", "axis")
    	.attr("transform", "translate(5," + 575  + ")")
    	.call(xAxis);
*/
} );

}, false);