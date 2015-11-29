function [ ] = drawOutputValues( outputs, net, lims, class, save )
%DRAWOUTPUTVALUES Summary of this function goes here
%   Detailed explanation goes here

fig = figure('Name', sprintf('outputs for %s - %s', net, class));
imagesc(outputs, [lims(1) lims(2)]);
colorbar;
if save
    print(fig, sprintf('plots/%s_%s_outputs', net, class), '-dpng');
end
end

