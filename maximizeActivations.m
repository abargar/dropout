layer = 2;
weights =  csvread(sprintf('snapshots/hinton_dropout_2700_layer%d_weights.csv', layer));
numInputs = size(weights,1);
numOutputs = size(weights,2);
max_acts = zeros(numOutputs,1);

% tile = zeros([35 35]);

for i=1:1
    [max_acts(i), max_weights] = maximizeActivation(weights(:,i));
%     tile = reshape(max_weights, [28 28]);
    tile = [max_weights' zeros(1,25)];
    tile = reshape(tile, 35, 35);
    imshow(mat2gray(tile));
end
