function [ max_act, max_weights ] = maximizeActivation( weights )
%MAXIMIZEACTIVATION Summary of this function goes here
%   Detailed explanation goes here

numWeights = size(weights,1);
x = rand(numWeights,1);
lr = 0.2;
stop = 500;
max_act = sum(weights .* x)

% j = - sum(weights .* x);

for i=1:stop
%     old_max_act = max_act;
    h = weights .* x;
%     j = - log(1 + exp(h) );
    dj =  - weights ./ ( exp(-h) + 1);
    x = x - lr*dj;
    sum( weights .* x) - sum(h)
%     max_act - old_max_act
end
max_act = sum(weights .* x)
max_weights = x;
