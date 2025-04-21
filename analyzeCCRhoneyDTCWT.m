% Concatenating all related Honeycomb groups
close all; clear all; clc;


% CCR_All_honey_1,CCR_All_honey_2,CCR_All_honey_3,CCR_All_honey_4
honeys = ["CCR_All_honey_1","CCR_All_honey_2","CCR_All_honey_3","CCR_All_honey_4"];

nExperiment=length(honeys);


featuresConcatenatedDTCWT_FirstOriented  =[];
featuresConcatenatedDTCWT_SecondOriented =[];
featuresConcatenatedDTCWT_ThirdOriented  =[];
featuresConcatenatedDTCWT_FourthOriented =[];
featuresConcatenatedDTCWT_FifthOriented  =[];
featuresConcatenatedDTCWT_SixthOriented  =[];

featuresConcatenatedCOARSEDTCWT= [];


for k=1:nExperiment
    k
    file=honeys(k) + '.mat';

    load(file)

    dtcwt=dtcwt_stats_cell_array;
    coarse_dtcwt= coarse_dtcwt_stats_cell_array;

    [dummy, nSlices]=size(dtcwt);
    [dummy1, nSlices1]=size(coarse_dtcwt);
    % features
    % 1. Energy 2. Contrast ...
    
for i = 1:length(dtcwt)
    sub_cells_coarse = coarse_dtcwt{i};   
    sub_cells_dtcwt = dtcwt{i};           
    
    for j = 1:length(sub_cells_coarse)
        featuresConcatenatedCOARSEDTCWT = [featuresConcatenatedCOARSEDTCWT; sub_cells_coarse{j}'];
    end
    
    k_th_orientation = 1;  % 1 to 6 different orientations
    
    [nSlices, dummy] = size(sub_cells_dtcwt);
    
    for t = 1:nSlices
        if iscell(sub_cells_dtcwt{t, k_th_orientation})
            featuresConcatenatedDTCWT_FirstOriented = [featuresConcatenatedDTCWT_FirstOriented; double(cell2mat(sub_cells_dtcwt{t, k_th_orientation})')];
        else
            featuresConcatenatedDTCWT_FirstOriented = [featuresConcatenatedDTCWT_FirstOriented; double(sub_cells_dtcwt{t, k_th_orientation})'];
        end
        
        if iscell(sub_cells_dtcwt{t, k_th_orientation + 1})
            featuresConcatenatedDTCWT_SecondOriented = [featuresConcatenatedDTCWT_SecondOriented; double(cell2mat(sub_cells_dtcwt{t, k_th_orientation + 1})')];
        else
            featuresConcatenatedDTCWT_SecondOriented = [featuresConcatenatedDTCWT_SecondOriented; double(sub_cells_dtcwt{t, k_th_orientation + 1})'];
        end
        
        if iscell(sub_cells_dtcwt{t, k_th_orientation + 2})
            featuresConcatenatedDTCWT_ThirdOriented = [featuresConcatenatedDTCWT_ThirdOriented; double(cell2mat(sub_cells_dtcwt{t, k_th_orientation + 2})')];
        else
            featuresConcatenatedDTCWT_ThirdOriented = [featuresConcatenatedDTCWT_ThirdOriented; double(sub_cells_dtcwt{t, k_th_orientation + 2})'];
        end
        
        if iscell(sub_cells_dtcwt{t, k_th_orientation + 3})
            featuresConcatenatedDTCWT_FourthOriented = [featuresConcatenatedDTCWT_FourthOriented; double(cell2mat(sub_cells_dtcwt{t, k_th_orientation + 3})')];
        else
            featuresConcatenatedDTCWT_FourthOriented = [featuresConcatenatedDTCWT_FourthOriented; double(sub_cells_dtcwt{t, k_th_orientation + 3})'];
        end
        
        if iscell(sub_cells_dtcwt{t, k_th_orientation + 4})
            featuresConcatenatedDTCWT_FifthOriented = [featuresConcatenatedDTCWT_FifthOriented; double(cell2mat(sub_cells_dtcwt{t, k_th_orientation + 4})')];
        else
            featuresConcatenatedDTCWT_FifthOriented = [featuresConcatenatedDTCWT_FifthOriented; double(sub_cells_dtcwt{t, k_th_orientation + 4})'];
        end
        
        if iscell(sub_cells_dtcwt{t, k_th_orientation + 5})
            featuresConcatenatedDTCWT_SixthOriented = [featuresConcatenatedDTCWT_SixthOriented; double(cell2mat(sub_cells_dtcwt{t, k_th_orientation + 5})')];
        else
            featuresConcatenatedDTCWT_SixthOriented = [featuresConcatenatedDTCWT_SixthOriented; double(sub_cells_dtcwt{t, k_th_orientation + 5})'];
        end
    end
end


filename = honeys(k) + "_featuresConcatenatedCOARSEDTCWT.mat";
filename1 = honeys(k) + "_featuresConcatenatedDTCWT_FirstOriented.mat";
filename2 = honeys(k) + "_featuresConcatenatedDTCWT_SecondOriented.mat";
filename3 = honeys(k) + "_featuresConcatenatedDTCWT_ThirdOriented.mat";
filename4 = honeys(k) + "_featuresConcatenatedDTCWT_FourthOriented.mat";
filename5 = honeys(k) + "_featuresConcatenatedDTCWT_FifthOriented.mat";
filename6 = honeys(k) + "_featuresConcatenatedDTCWT_SixthOriented.mat";

save(filename,"featuresConcatenatedCOARSEDTCWT")
save(filename1,"featuresConcatenatedDTCWT_FirstOriented")
save(filename2,"featuresConcatenatedDTCWT_SecondOriented")
save(filename3,"featuresConcatenatedDTCWT_ThirdOriented")
save(filename4,"featuresConcatenatedDTCWT_FourthOriented")
save(filename5,"featuresConcatenatedDTCWT_FifthOriented")
save(filename6,"featuresConcatenatedDTCWT_SixthOriented")
end