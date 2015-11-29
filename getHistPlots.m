for class=0:9
    inputStr = 'hinton_dropout/%d/epoch=%d_average_over_100.csv';
    outputStr = 'hinton_dropout_class=%d_epoch=%d_layer=%d';
    epoch = 300;
    layer = 1;
    shape = [1200, 1200, 10];


    for epoch=300:300:1200
        input = sprintf(inputStr, class, epoch)
        layers = csvread(input);

        for i=1:2
            layers(i,:);
            [counts, centers] = hist(layers(i,1:shape(i)));
            fig = figure;
            bar(centers, counts);
            print(fig, sprintf(outputStr, class, epoch, i), '-dpng');
            close(fig);
        end
    end

    epoch = 2700;
    input = sprintf(inputStr, epoch);
    layers = csvread(input);

    for i=1:2
        layers(i,:);
        [counts, centers] = hist(layers(i,1:shape(i)));
        fig = figure;
        bar(centers, counts);
        print(fig, sprintf(outputStr, epoch, i), '-dpng');
        close(fig);
    end
end