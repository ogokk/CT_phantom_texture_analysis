% Opening and accessing DICOM format slices using dicom23D
% Saving the files as .nft, .mat and .png file format 
% Automatically capturing the all slices through cropping the first slice

clear all;
clc;
[volume_image, slice_data, image_meta_data] = dicom23D();

%%
% CT slice sanity check
% imshow 1st slice of the corresponding texture phantom (i.e. diagonal, horizontal, etc..)
I = double((volume_image(:,:,619))); 
figure(34),imshow(I,[])
% Manuel cropping of the 1st slice
I_cropped = imcrop(I,[331.5 389.5 40 41]);  
figure, imshow(I_cropped, []);
  
%% 
% Create the subfolder where the PNG files will be saved.
png_folder = 'your_path/18.03.25_abdomen/texture görüntüleri/star8/png/';
if ~isfolder(png_folder)
    mkdir(png_folder);
end

% image_idx = 619;
% first_slice = imcrop(double((volume_image(:,:,image_idx))), [331.5 389.5 40 41]) - 1024;


% Total number of best-alinged or optimum slices corresponding to a texture.
% Optionally both obtaining total slices and Concordance Correlation Coefficient 
% (CCC)-checked slices for CT scan analysis.
% Automatically crop the all slices within the loop. 
optim_numSlices = 60;
for idx = 1:optim_numSlices 
    image_idx = 619 + (idx - 1);  % increasing image index
    I_cropped = imcrop(double((volume_image(:,:,image_idx))), [272 390 40 40]) - 1024; 
    
    % Accept slice if CCC score of (first_slice, I_cropped) >= 0.9.
    % ccc= calculateCCC(first_slice, I_cropped);
    % if ccc>= 0.9
    
    var_name = sprintf('I_cropped_%03d', idx);  
    
    % Dynamic variable assignment
    eval([var_name ' = I_cropped;']); 
    
    % Create the index name of .mat file 
    mat_filename = sprintf('your_path/18.03.25_abdomen/texture görüntüleri/star8/mat/%03d.mat', idx);
    
    % PNG filename for each slice to save
    png_filename = sprintf('%s%03d.png', png_folder, idx);
    
    % Save the .mat file
    save(mat_filename, var_name);
    
    % Preprocessing for saving the .png files
    I_cropped_normalized = uint8(255 * mat2gray(I_cropped));
    
    % Save the .png file
    imwrite(I_cropped_normalized, png_filename); 
 % end
end

%%
% Main folder path for saving .nft file
nft_main_folder_path = 'your_path/18.03.25_abdomen/texture görüntüleri';

% Finding all subfolders contained within the main folder
subfolder = dir(nft_main_folder_path);
subfolder = subfolder([subfolder.isdir]);
subfolder = subfolder(~ismember({subfolder.name}, {'.', '..'})); 

% Process each subfolder
for j = 1:length(subfolder)
    subfolder_name = subfolder(j).name;
    subfolder_path = fullfile(nft_main_folder_path, subfolder_name);
    
    % Find all .mat files in the subfolder
    matFiles = dir(fullfile(subfolder_path, '*.mat'));
    
    % Structure for all slices
    struct_all_slices = struct();

    % Load each slice and add to the structure
    for i = 1:length(matFiles)
        fileName = matFiles(i).name;
        fullFile_path = fullfile(subfolder_path, fileName);

        data = load(fullFile_path);

        [~, str_name, ~] = fileparts(fileName);
        str_name = matlab.lang.makeValidName(str_name);
        
        struct_all_slices.(str_name) = data;
    end

    % Create and save a file with the same name as the subfolder
    nftfileName = fullfile(subfolder_path, [subfolder_name, '.nft']);
    % Save a file in MATLAB v7.3 format, which supports files 
    % larger than 2 GB and is compatible with HDF5.
    save(nftfileName, '-struct', 'struct_all_slices', '-v7.3');

    disp(['The data in the subfolder has been saved to the file ', nftfileName, '.']);
end


