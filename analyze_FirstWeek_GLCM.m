% First scan date as a reference for follow-up assessment

close all; clear all; clc;

% 1.horizontal', 2.vertical', 3.diagonal', 4.honeylarge', 5.honeymedium',
% 6.honeysmall', 7.sinusoidal', 8.square', 9.star4', 10.star8'
textureType=10;
textureNames={'horizontal', 'vertical', 'diagonal', 'honeylarge', 'honeymedium',...
    'honeysmall', 'sinusoidal', 'square', 'star4', 'star8'};

colors= {'red', 'green', 'blue', 'cyan', 'magenta'};
markers={'*', 'o', 'x', '.', '+'};
featureNames={'Energy', 'Contrast', 'Correlation', 'Variance'...
    'Homogeneity', 'Sum Average', 'Sum Variance', 'Sum Entropy'...
    'Entropy','Difference Variance', 'Difference Entropy', 'Correlation I'...
    'Correlation II', 'Maximal Correlation'};

numFigures=length(featureNames); % number of Figures as the number of Features
numFeatures=length(featureNames); % number of Features
for k=1:numel(textureNames)
for figNum = 1:numFigures
    figure(figNum); 
    title([textureNames(textureType) ' Figure ' num2str(figNum) featureNames(figNum)]); % Set title
    hold on; % Keep the current figure active for multiple plots
end

dates = [241016];

nExperiment=length(dates);

featuresConcatenatedGLCM=[];

for i=1:nExperiment
    i
    file=['texturesAll' num2str(dates(i)) '.mat'];

    load(file)

    glcm=glcm_stats_cell_array{k};

    [dummy nSlices]=size(glcm);

    % features
    % 1. Energy 2. Contrast ...
    for j=1:nSlices
        featuresGLCM(j,:)=(glcm{1,j}); % featuresGLCM dim --> nSlices x 14 (haralick feature dim)
    end

    featuresConcatenatedGLCM=[featuresConcatenatedGLCM; featuresGLCM];


    % Plot to different figures during each iteration
    % for k = 1:numFeatures
    %     figNum = k; % Select figure cyclically
    %     figure(figNum); % Switch to the selected figure
    %     plot(featuresGLCM(:,k), 'Color', colors{i}, 'Marker', markers{i}); hold on;
    %     legend('show'); % Update legend
    % end
end
% check NaNs if available
nanLocations = isnan(featuresConcatenatedGLCM);
featuresConcatenatedGLCM(nanLocations) = 0;
TobeSavedFileName = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedGLCM.mat";
save(TobeSavedFileName,"featuresConcatenatedGLCM")
end