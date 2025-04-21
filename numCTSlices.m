% Finding the number of slices corresponding to  each texture and scan date

clear all; close all; clc;
rootFolder = 'phantom_slices';  % root folder path

% phantom_slices
% |
% --- textures
%     |
%     --- horizontal
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
%     |
%     --- vertical
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., M.mat
%     |
%     --- diagonal
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., K.mat
%     |
%     --- honeylarge
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., T.mat
%     |
%     --- honeymedium
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
%     |
%     --- honeysmall
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
%     |
%     --- sinusoidal
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., L.mat
%     |
%     --- square
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., P.mat
%     |
%     --- star4
%     |    |
%     |    --- mat
%     |         |
%     |         ---- 1.mat, 2.mat, 3.mat, ..., D.mat
%     |
%     --- star8
%          |
%          --- mat
%               |
%               ---- 1.mat, 2.mat, 3.mat, ..., X.mat


dateDirs = dir(rootFolder);
dateDirs = dateDirs(~ismember({dateDirs.name},{'.','..'}));

textures = {'horizontal', 'vertical', 'diagonal', 'honeylarge', ...
    'honeymedium', 'honeysmall', 'sinusoidal', 'square', 'star4', 'star8'};

textureCounts = struct();
for i = 1:length(textures)
    textureCounts.(textures{i}) = 0;  % Initialize counts for each texture
end

for i = 1:length(dateDirs)
    dateFolder = fullfile(rootFolder, dateDirs(i).name);
    
    textureFolder = fullfile(dateFolder, 'texture görüntüleri');
    if exist(textureFolder, 'dir')
        for j = 1:length(textures)
            textureFolderPath = fullfile(textureFolder, textures{j});
            
            if exist(textureFolderPath, 'dir')
                matFolder = fullfile(textureFolderPath, 'mat');  % 'mat' folder within the texture folder
                
                if exist(textureFolderPath, 'dir')
                    matFiles = dir(fullfile(matFolder, '*.mat'));
                    % matFiles = dir(fullfile(textureFolderPath, '*.mat'));

                    numSlices = length(matFiles);
                    fprintf('Date: %s, Texture: %s, Number of slices: %d\n', ...
                        dateDirs(i).name, textures{j}, numSlices);
                    
                    textureCounts.(textures{j}) = textureCounts.(textures{j}) + numSlices;
                end
            end
        end
    end
end

fprintf('\nTotal number of slices for each texture:\n');
for i = 1:length(textures)
    fprintf('Texture: %s, Total number of slices: %d\n', ...
        textures{i}, textureCounts.(textures{i}));
end
