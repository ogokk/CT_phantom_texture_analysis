% Saving 'glcm_stats_cell_array','dtcwt_stats_cell_array' groups (1st,2nd,..6th) and
% 'coarse_dtcwt_stats_cell_array'
% Combining them in a single mat file within 
% each custom designed 3D-printed phantom group.

clear all;close all;
clc


main_folder = ['C:\Users\Bio İzmir\Desktop\Ozan_1001\1001\' ...
    'dtcwt_glcm_reproducible_features\ccc_filtered_phantom_slices'];

% folders = dir(fullfile(main_folder, 'textures*'));
folders = dir(fullfile(main_folder));
folders = folders([folders.isdir] & ~ismember({folders.name}, {'.', '..'})); 


subfolders = {'horizontal', 'vertical', 'diagonal', 'honeylarge', ...
    'honeymedium', 'honeysmall', 'sinusoidal', 'square', 'star4', 'star8'};

all_texture_cell_array = cell(1, numel(subfolders));
dtcwt_stats_cell_array = cell(1, numel(subfolders));
glcm_stats_cell_array = cell(1, numel(subfolders));
coarse_dtcwt_stats_cell_array = cell(1, numel(subfolders));
for k = 1: numel(folders)
    parent_folder = fullfile(folders(k).folder,folders(k).name);
    saved_name = parent_folder;
    parent_folder = fullfile(parent_folder,"texture görüntüleri");
for j = 1:numel(subfolders)
    subfolder_path = fullfile(parent_folder, subfolders{j});
    subfolder_path = fullfile(subfolder_path, "mat");
    mat_files = dir(fullfile(subfolder_path, '*.mat'));  
    each_texture = cell(1, numel(mat_files));
    dtcwt_stats_cell = cell(1, numel(mat_files));
    glcm_stats_cell = cell(1, numel(mat_files));
    coarse_dtcwt_stats_cell = cell(1, numel(mat_files));

    for i = 1:numel(mat_files)
        mat_file_path = fullfile(subfolder_path, mat_files(i).name);
        [~, mat_name, ~] = fileparts(mat_file_path);
        loaded_data = load(mat_file_path);
        each_texture{i} = loaded_data; 
        field_name = sprintf('I_cropped_%03d', str2double(mat_name));
        current_data = loaded_data.(field_name); 
        % Image(Spatial) domain textural feature extraction over GLCM
        glcms = graycomatrix(current_data, Offset=[-1 -1]);
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

date = regexp(saved_name, '[^\\]+$', 'match', 'once');
TobeSavedFileName = date + "_Alltextures" + ".mat";
save(TobeSavedFileName, 'glcm_stats_cell_array','dtcwt_stats_cell_array','coarse_dtcwt_stats_cell_array')
end