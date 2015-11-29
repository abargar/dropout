method = 'hinton_backprop';
for class=0
    layer = 1;
    inputStr = '%s/%d/epoch=%d_average_over_100.csv';
    outputStr = '%s_class=%d_layer=%d_evolution.mat';
    shape = [1200, 1200, 10];
    layerEvolves = [];
    testSum = 0;
    for epoch=2700
        epoch
        input = sprintf(inputStr, method, class, epoch);
        output = sprintf(outputStr, method, class, layer);
        layers = csvread(input);


        layerRep = [layers(1,:) zeros(1,25)];
        layerRep = reshape(layerRep, 35, 35);
        testSum = testSum + sum(layers(1,:));
        layerEvolves = cat(3, layerEvolves, layerRep);

    end
%     save(output, 'layerEvolves');
%     implay(layerEvolves);
end