net = 'hinton_backprop';

for layer=0:2

    dropout_weights = csvread(sprintf('snapshots/hinton_dropout_2700_layer%d_weights.csv', layer));
    backprop_weights = csvread(sprintf('snapshots/hinton_backprop_2700_layer%d_weights.csv', layer));
    
    min_val = min( min(dropout_weights(:)), min(backprop_weights(:)) );
    max_val = max( max(dropout_weights(:)), max(backprop_weights(:)) );
    clims = [min_val max_val];
    
    figure('Name', sprintf('Layer %d', layer));
    subplot(1,2,1);
    imagesc(dropout_weights, clims);
    colorbar;
    subplot(1,2,2);
    imagesc(backprop_weights, clims);
    colorbar;
    
    figure('Name', sprintf('Difference for Layer %d', layer));
    imagesc(abs(backprop_weights - dropout_weights));
    colorbar('SouthOutside');
end