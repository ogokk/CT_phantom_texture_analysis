% Saving 'glcm_stats_cell_array','dtcwt_stats_cell_array' groups (1st,2nd,..6th) and
%'coarse_dtcwt_stats_cell_array'
%Combining them in a single mat file within each Honeycomb group.

clear all;close all;
clc

parent_folder = 'your_path/CCR_4_HONEYCOMB/';
ccr_phantoms = dir(parent_folder);
ccr_phantoms=ccr_phantoms(~ismember({ccr_phantoms.name},{'.','..'}));


% CCR_4_HONEYCOMB
% |
% --- CCR-2-001
% |    |
% |    --- Honeycomb_1
% |    |    |
% |    |    --- mat
% |    |         |
% |    |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
% |    |
% |    --- Honeycomb_2
% |    |    |
% |    |    --- mat
% |    |         |
% |    |         ---- 1.mat, 2.mat, 3.mat, ..., M.mat
% |    |
% |    --- Honeycomb_3
% |    |    |
% |    |    --- mat
% |    |         |
% |    |         ---- 1.mat, 2.mat, 3.mat, ..., P.mat
% |    |
% |    --- Honeycomb_4
% |         |
% |         --- mat
% |              |
% |              ---- 1.mat, 2.mat, 3.mat, ..., K.mat
% |
% --- CCR-2-002
% |    |
% |    --- Honeycomb_1
% |    |    |
% |    |    --- mat
% |    |         |
% |    |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
% |    |
% |    --- Honeycomb_2
% |    |    |
% |    |    --- mat
% |    |         |
% |    |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
% |    |
% |    --- Honeycomb_3
% |    |    |
% |    |    --- mat
% |    |         |
% |    |         ---- 1.mat, 2.mat, 3.mat, ..., L.mat
% |    |
% |    --- Honeycomb_4
% |         |
% |         --- mat
% |              |
% |              ---- 1.mat, 2.mat, 3.mat, ..., X.mat
% |
% ...
% |
% --- CCR-2-252
%      |
%      --- Honeycomb_1
%      |    |
%      |    --- mat
%      |         |
%      |         ---- 1.mat, 2.mat, 3.mat, ..., T.mat
%      |
%      --- Honeycomb_2
%      |    |
%      |    --- mat
%      |         |
%      |         ---- 1.mat, 2.mat, 3.mat, ..., F.mat
%      |
%      --- Honeycomb_3
%      |    |
%      |    --- mat
%      |         |
%      |         ---- 1.mat, 2.mat, 3.mat, ..., N.mat
%      |
%      --- Honeycomb_4
%           |
%           --- mat
%                |
%                ---- 1.mat, 2.mat, 3.mat, ..., H.mat



subfolders = {'Honeycomb_1', 'Honeycomb_2', 'Honeycomb_3', 'Honeycomb_4'};
% honeys_path(1)-->honey_1, honeys_path(2)-->honey_2, 
% honeys_path(3)-->honey_3, honeys_path(4)-->honey_4
all_texture_cell_array = cell(1, numel(subfolders));
dtcwt_stats_cell_array = cell(1, numel(subfolders));
glcm_stats_cell_array = cell(1, numel(subfolders));
coarse_dtcwt_stats_cell_array = cell(1, numel(subfolders));

for j = 1:numel(ccr_phantoms)
    subfolder_path = fullfile(parent_folder, ccr_phantoms(j).name);
    honeys_path = dir(subfolder_path);
    honeys_path=honeys_path(~ismember({honeys_path.name},{'.','..'}));
    mat_files1 = dir(fullfile(subfolder_path, honeys_path(4).name)); 
    mat_files1=mat_files1(~ismember({mat_files1.name},{'.','..'}));
    mat_files1_name = mat_files1(1).name; 
    mat_files1_folder = mat_files1(1).folder; 
    mat_files = fullfile(mat_files1_folder, mat_files1_name); 
    mat_files = dir(fullfile(mat_files, '*.mat'));  

    each_texture = cell(1, numel(mat_files));
    dtcwt_stats_cell = cell(1, numel(mat_files));
    glcm_stats_cell = cell(1, numel(mat_files));
    coarse_dtcwt_stats_cell = cell(1, numel(mat_files));

    for i = 1:numel(mat_files)
        mat_file_path = fullfile(mat_files(i).folder, mat_files(i).name);
        loaded_data = load(mat_file_path);
        each_texture{i} = loaded_data; 
        field_name = sprintf('I_cropped_%03d', i);
        current_data = loaded_data.(field_name); 
        % Image(Spatial) domain textural feature extraction over GLCM
        glcms = graycomatrix(current_data, Offset=[0 1]);
        haralick = haralickTextureFeatures(glcms, 1:14);  % Extract Haralick features

        glcm_stats_cell{1, i} = haralick;
        
        level = 1;  % Level of decomposition
        [a1, d1] = dualtree2(current_data, 'Level', level); 
        
        coarse_image = a1;
        haralick_coarse_dtcwt = haralickTextureFeatures(abs(coarse_image), 1:14); 


        haralick_dtcwt = cell(1, 6);  
        for k = 1:6  % for 6 oriented filters
            detail_image = d1{1,1}(:,:,k);
            % Space-Frequency domain textural feature extraction over
            % detailed images using 6 oriented filters
            detail_image_magnitude = abs(detail_image);
            haralick_dtcwt{k} = haralickTextureFeatures(detail_image_magnitude, 1:14);  
        end
        dtcwt_stats_cell{1, i} = haralick_dtcwt;
        coarse_dtcwt_stats_cell{1,i} = haralick_coarse_dtcwt;
    end
    glcm_stats_cell_array{1, j} = glcm_stats_cell; %contains 8 texture x (1xM,N,K..) slices x (14x1 haralick features)
    coarse_dtcwt_stats_cell_array{1, j} = coarse_dtcwt_stats_cell; %contains 8 texture x (1xM,N,K..) coarse x (14x1 haralick features)
    dtcwt_stats_cell_array{1, j} = dtcwt_stats_cell; %contains 8 texture x (1xM,N,K..) slices x (1x6 oriented images) x (14x1 haralick features)
    all_texture_cell_array{j} = each_texture;
end

[~, last_string_name_of_path, ~] = fileparts(mat_files1_folder);
TobeSavedFileName = "CCR_All_" +last_string_name_of_path +  ".mat";
save(TobeSavedFileName, 'glcm_stats_cell_array','dtcwt_stats_cell_array','coarse_dtcwt_stats_cell_array')