% Calculation of Heatmap for the mat files 
% of a texture with a specific scan date
% using Concordance Correlation Coefficient (CCC)
clear all;close all;clc;
directory = uigetdir;
matFiles = dir(fullfile(directory, "*.mat"));
num_images = length(matFiles); 
similarity_matrix = zeros(num_images, num_images);
image_data = cell(1, num_images); 

for i = 1:num_images
    file_name = sprintf('%03d.mat', i);
    mat_data = load(fullfile(directory, file_name));
    var_name = sprintf('I_cropped_%03d', i);

    image_data{i} = mat_data.(var_name);
end

function ccc_score = calculateCCC(img1, img2)
    img1 = double(img1);
    img2 = double(img2);
    
    mean1 = mean(img1(:));
    mean2 = mean(img2(:));
    
    var1 = var(img1(:));
    var2 = var(img2(:));
    
    cov12 = cov(img1(:), img2(:));
    
    numerator = 2 * cov12(1,2);  
    denominator = var1 + var2 + (mean1 - mean2)^2;  
    ccc_score = numerator / denominator;
end

for i = 1:num_images
    for j = i:num_images
        ccc_value = calculateCCC(image_data{i}, image_data{j});
        
        similarity_matrix(i, j) = ccc_value;
        similarity_matrix(j, i) = ccc_value; 
    end
end

% Mean CCC for each slice (row-wise)
mean_ccc_scores = mean(similarity_matrix, 2);  

% Row-wise overall threshold in heatmap for CCC score (96%) to ensure 
% CCC score of each slice pair (i,j) > 0.9
threshold = 96;

selected_slices = find(100*mean_ccc_scores >= threshold);
eliminated_slices= find(100*mean_ccc_scores < threshold);

% disp(selected_slices);

if ~isempty(eliminated_slices)
    fprintf("Eliminated Slices: %d\n", eliminated_slices)
else
    fprintf("No Elimination..!\n")
end

% Heatmaps
filtered_similarity_matrix = similarity_matrix(selected_slices, selected_slices);
figure;
heatmap(similarity_matrix, 'Title', 'Similarity Heatmap (CCC) for Original Slices', 'XLabel', 'Image Index', 'YLabel', 'Image Index');
figure;
heatmap(filtered_similarity_matrix, 'Title', 'Similarity Heatmap (CCC) for Selected Slices', 'XLabel', 'Image Index', 'YLabel', 'Image Index');
