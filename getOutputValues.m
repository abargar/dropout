% backprop_outputs = csvread('backprop_2700_layer0_all_outputs.csv');
% backprop_activations = csvread('hinton_backprop_2700_layer0_weights.csv');
% dropout_outputs = csvread('dropout_2700_layer0_all_outputs.csv');
dropout_activations = csvread('snapshots/hinton_dropout_2700_layer2_weights.csv');
% 
% min_val = min(min(dropout_outputs(:)), min(backprop_outputs(:)));
% max_val = max(max(dropout_outputs(:)), max(backprop_outputs(:)));
% drawOutputValues(dropout_outputs, 'dropout', [min_val, max_val], 'all', true);
% drawOutputValues(backprop_outputs, 'backprop', [min_val, max_val], 'all', true);


% [nbo, boc] = hist(backprop_outputs(:), 50);
% [nmba, mbac] = hist(mean(backprop_activations,1), 50);
% [ndo, doc] = hist(dropout_outputs(:), 50);
% [nmda, mdac] = hist(mean(dropout_activations,1) * 0.5, 50);

% figure('Name', 'Backprop Outputs');
% bar(boc, nbo);
% figure('Name', 'Dropout Outputs');
% bar(doc, ndo);
% figure('Name', 'Backprop Activations');
% bar(bac, nba);
% figure('Name', 'Dropout Activations');
% bar(dac, nda);
% figure('Name', 'Mean Activations');
% bar(mbac, nmba);
% figure('Name', 'Mean Dropout Activations');
% bar(mdac, nmda);

% backprop_bool = backprop_outputs > 0;
% backprop_numactive = sum(backprop_bool,2);
% dropout_bool = dropout_outputs > 0;
% dropout_numactive = sum(dropout_bool,2);


thresholded_bp = zeros(2000, 10);
thresholded_dp = zeros(2000, 10);
threshold = 180;
% 
for class=0:9
    rowHead = 200 * class + 1;
    bp_out = backprop_outputs(rowHead:rowHead+199,:);
    dp_out = dropout_outputs(rowHead:rowHead+199,:);
    
    bp_bools = bp_out > 0;
    bp_actsum = sum(bp_bools,1);
    [nbp, bpc] = hist(bp_actsum, 50);
    dp_bools = dp_out > 0;
    dp_actsum = sum(dp_bools,1);
%     bp_inds = find(bp_actsum > threshold);
    dp_inds = find(dp_actsum > threshold)
    for i=1
        figure;
        imagesc(reshape(dropout_activations(:,dp_inds(i)), [35 35]));
    end
    
    thresholded_bp(rowHead:rowHead+199, bp_actsum > threshold) = bp_out(:, bp_actsum > threshold);
    thresholded_dp(rowHead:rowHead+199, dp_actsum > threshold) = dp_out(:, dp_actsum > threshold);
    
%     [ndp, dpc] = hist(dp_actsum, 50);
%     fig = figure('Name', sprintf('Num activations per node - Backprop Class %d', class));
%     bar(bpc, nbp);
%     print(fig, sprintf('plots/backprop_num_node_activations_class=%d', class), '-dpng');
%     close(fig);
%     figure('Name', sprintf('Num activations per node - Dropout Class %d', class));
%     bar(dpc, ndp);
%     print(fig, sprintf('plots/dropout_num_node_activations_class=%d', class), '-dpng');
%     close(fig);
%     save(sprintf('data/num_activations_class=%d.mat', class), 'bp_out', 'dp_out', 'bp_act', 'dp_act');
end

min_val = min(min(thresholded_dp(:)), min(thresholded_bp(:)));
max_val = max(max(thresholded_dp(:)), max(thresholded_bp(:)));

figure('Name', 'Thresholded Backprop');
imagesc(thresholded_bp, [min_val max_val]);
figure('Name', 'Thresholded Dropout');
imagesc(thresholded_dp, [min_val max_val]);