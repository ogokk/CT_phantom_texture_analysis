% Concatenating all related Honeycomb groups

close all; clear all; clc;

% 1.horizontal', 2.vertical', 3.diagonal', 4.honeylarge', 5.honeymedium',
% 6.honeysmall', 7.sinusoidal', 8.square', 9.star4', 10.star8'

colors= {'red', 'green', 'blue', 'cyan', 'magenta'};
markers={'*', 'o', 'x', '.', '+'};
featureNames={'Energy', 'Contrast', 'Correlation', 'Variance'...
    'Homogeneity', 'Sum Average', 'Sum Variance', 'Sum Entropy'...
    'Entropy','D       ifference Variance', 'Difference Entropy', 'Correlation I'...
    'Correlation II', 'Maximal Correlation'};

numFigures=length(featureNames); 
numFeatures=length(featureNames); 

% for figNum = 1:numFigures
%     figure(figNum); % Create/select figure
%     title([textureNames(textureType) ' Figure ' num2str(figNum) featureNames(figNum)]); % Set title
%     hold on; % Keep the current figure active for multiple plots
% end

honeys = ["CCR_All_honey_1","CCR_All_honey_2","CCR_All_honey_3","CCR_All_honey_4"];

nExperiment=length(honeys);

featuresConcatenatedGLCM = [];

for k=1:nExperiment
    k
    file=honeys(k) + '.mat';

    load(file)

    glcm=glcm_stats_cell_array;
    
    [dummy nSlices]=size(glcm);

    % features
    % 1. Energy 2. Contrast ...
    for i = 1:length(glcm)
    sub_cells = glcm{i};
    
    for j = 1:length(sub_cells)
        featuresConcatenatedGLCM = [featuresConcatenatedGLCM; sub_cells{j}'];
    end
    end

    % Plot to different figures during each iteration
    % for k = 1:numFeatures
    %     figNum = k; % Select figure cyclically
    %     figure(figNum); % Switch to the selected figure
    %     plot(featuresConcatenatedGLCM(:,k), 'Color', colors{i}, 'Marker', markers{i}); hold on;
    %     legend('show'); % Update legend
    % end

% check NaNs if available
nanLocations = isnan(featuresConcatenatedGLCM);
featuresConcatenatedGLCM(nanLocations) = 0;
filename = honeys(k) + "_featuresConcatenatedGLCM.mat";
save(filename,"featuresConcatenatedGLCM")
end