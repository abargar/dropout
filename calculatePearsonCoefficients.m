function [ r_s ] = calculatePearsonCoefficients( values, title )

num_nodes = size(values,2);
r_s = zeros(num_nodes);

for i = 1:num_nodes
    for j = 1:num_nodes
    x = values(:,i);
    y = values(:,j);
    n = size(x,1);

    r_num = n*sum(x .* y) - ( sum(x) * sum(y) );
    r_denom = sqrt( (n*sum(x.^2) - (sum(x)^2)) * (n*sum(y.^2) - sum(y)^2));

    r_s(i,j) = r_num / r_denom;
    r_s(j,i) = r_num / r_denom;
    
    end
end

fig = figure;
imagesc(r_s);
colorbar;
print(fig, sprintf('plots/%s', title), '-dpng');

save(sprintf('data/%s.mat', title), 'r_s');

end


