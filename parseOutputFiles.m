backprop_outputs = zeros(2000, 1200);
dropout_outputs = zeros(2000, 1200);
layer = 0;
for class=0:9
    %     subplot(10,1,class+1); 
%     filename = sprintf('activations/%s/%d/2700_0.csv', net, class);
    rowHead = 200 * class + 1;
%     outputs = csvread(filename);
    backprop_outputs(rowHead:rowHead+199,:) = csvread(sprintf('activations/hinton_backprop/%d/2700_%d.csv', class, layer));
    dropout_outputs(rowHead:rowHead+199,:) = csvread(sprintf('activations/hinton_dropout/%d/2700_%d.csv', class, layer));
end

% csvwrite(sprintf('dropout_2700_layer%d_all_outputs.csv', layer), dropout_outputs);
% csvwrite(sprintf('backprop_2700_layer%d_all_outputs.csv', layer), backprop_outputs);
