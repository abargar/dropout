d3.json('testnet.json', function(data){
var model = data.model;
var layer_sizes = data.size;
var weights = data.weights;
console.log(layer_sizes);

margins = [5, 5, 5, 5];
w = 1200 - margins[0] - margins[2];
h = 600 - margins[1] - margins[3];
p = margins[3] + 10;
var svg = d3.select('body').append('svg:svg')
		  .attr('width', w)
		  .attr('height', h)
		  .append('svg:g')
		  .attr('transform', 'translate (' + margins[3] + ',' + margins[0] + ')');

var xDomain = d3.range(layer_sizes.length);

var xScale = d3.scale.ordinal()
                     .domain(xDomain)
                     .rangePoints([0+p, w-p]);
var yScales = layer_sizes.map(function(N, i){
	return d3.scale.ordinal()
		   .domain(d3.range(N))
		   .rangePoints([0+p, h-p]);
});
var indices = layer_sizes.map(function(N, x){
	return d3.range(N).map(function(d){
		return yScales[x](d);
	});
});

var layers  = svg.selectAll('g')
	.data(indices)
	.enter()
	.append('g')
	.attr('transform', function(d, x){ return 'translate (' + xScale(x) + ',' + margins[0] + ')'});

var nodes = layers.selectAll('circle')
				.data(function(y){
					return y;})
				.enter()
				.append('circle');

nodes.attr('cx', 0)
	.attr('cy', function(d,x){
		return d;
	})
	.attr('r', 5);

var linkData = weights.map(function(mat,k){
	return mat.map(function(d,i){
			return d.map(function(v, j){
				return [k, i, j, v];
			});
	});
});

linkData = [].concat.apply([], linkData);
linkData = [].concat.apply([], linkData);

var links = svg.selectAll('line')
			.data(linkData)
			.enter()
			.append('line');

links.style("stroke", "black")
     .attr("x1", function(d){return xScale(d[0]);})
     .attr("y1", function(d){return yScales[d[0]](d[1])+2;})
     .attr("x2", function(d){return xScale(d[0]+1);})
     .attr("y2", function(d){return yScales[d[0]+1](d[2])+2;})
     .style("stroke-opacity", function(d){return d[3];});

console.log('Showing model: ', model);
console.log('It lives!');

});
