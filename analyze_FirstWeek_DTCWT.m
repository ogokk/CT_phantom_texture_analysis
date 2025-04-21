% First scan date as a reference for follow-up assessment

close all; clear all; clc;

% 1.horizontal', 2.vertical', 3.diagonal', 4.honeylarge', 5.honeymedium',
% 6.honeysmall', 7.sinusoidal', 8.square', 9.star4', 10.horizontal_'
textureType=10;
textureNames={'horizontal', 'vertical', 'diagonal', 'honeylarge', 'honeymedium',...
    'honeysmall', 'sinusoidal', 'square', 'star4', 'star8'};

colors= {'red'};
markers={'*'};
featureNames={'Energy', 'Contrast', 'Correlation', 'Variance'...
    'Homogeneity', 'Sum Average', 'Sum Variance', 'Sum Entropy'...
    'Entropy','Difference Variance', 'Difference Entropy', 'Correlation I'...
    'Correlation II', 'Maximal Correlation'};

numFigures=length(featureNames); % number of Figures as the number of Features
numFeatures=length(featureNames); % number of Features

for k=1:numel(textureNames)
dates = 241016;

nExperiment=length(dates);


featuresConcatenatedDTCWT_FirstOriented  =[];
featuresConcatenatedDTCWT_SecondOriented =[];
featuresConcatenatedDTCWT_ThirdOriented  =[];
featuresConcatenatedDTCWT_FourthOriented =[];
featuresConcatenatedDTCWT_FifthOriented  =[];
featuresConcatenatedDTCWT_SixthOriented  =[];

featuresConcatenatedCOARSEDTCWT=[];


for i=1:nExperiment
    i
    file=['texturesAll' num2str(dates(i)) '.mat'];

    load(file)

    dtcwt=dtcwt_stats_cell_array{k};
    coarse_dtcwt= coarse_dtcwt_stats_cell_array{k};

    [dummy, nSlices]=size(dtcwt);
    [dummy1, nSlices1]=size(coarse_dtcwt);
    % features
    % 1. Energy 2. Contrast ...
    
    for j=1:nSlices
        featuresDTCWT(j,:)=dtcwt{1,j}; % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
    end

    for j=1:nSlices1
        featuresCOARSE_DTCWT(j,:)=(coarse_dtcwt{1,j});
    end
    
    k_th_orientation = 1; % 1 to 6 different orientation
    for t=1:nSlices
        First_Oriented_featuresDTCWT(t,:)=(featuresDTCWT{t,k_th_orientation}); % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
        Second_Oriented_featuresDTCWT(t,:)=(featuresDTCWT{t,k_th_orientation+1}); % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
        Third_Oriented_featuresDTCWT(t,:)=(featuresDTCWT{t,k_th_orientation+2}); % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
        Fourth_Oriented_featuresDTCWT(t,:)=(featuresDTCWT{t,k_th_orientation+3}); % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
        Fifth_Oriented_featuresDTCWT(t,:)=(featuresDTCWT{t,k_th_orientation+4}); % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
        Sixth_Oriented_featuresDTCWT(t,:)=(featuresDTCWT{t,k_th_orientation+5}); % featuresDTCWT dim --> nSlices x 14 (haralick feature dim)
    end


    featuresConcatenatedDTCWT_FirstOriented=[featuresConcatenatedDTCWT_FirstOriented; First_Oriented_featuresDTCWT];
    featuresConcatenatedDTCWT_SecondOriented=[featuresConcatenatedDTCWT_SecondOriented; Second_Oriented_featuresDTCWT];
    featuresConcatenatedDTCWT_ThirdOriented=[featuresConcatenatedDTCWT_ThirdOriented; Third_Oriented_featuresDTCWT];
    featuresConcatenatedDTCWT_FourthOriented=[featuresConcatenatedDTCWT_FourthOriented; Fourth_Oriented_featuresDTCWT];
    featuresConcatenatedDTCWT_FifthOriented=[featuresConcatenatedDTCWT_FifthOriented; Fifth_Oriented_featuresDTCWT];
    featuresConcatenatedDTCWT_SixthOriented=[featuresConcatenatedDTCWT_SixthOriented; Sixth_Oriented_featuresDTCWT];
    
    % disp(size(featuresCOARSE_DTCWT));
    % disp(size(featuresConcatanatedCOARSEDTCWT));

    featuresConcatenatedCOARSEDTCWT=[featuresConcatenatedCOARSEDTCWT; featuresCOARSE_DTCWT];

end

nanLocations = isnan(featuresConcatenatedDTCWT_FirstOriented);
featuresConcatenatedDTCWT_FirstOriented(nanLocations) = 0;
nanLocations = isnan(featuresConcatenatedDTCWT_SecondOriented);
featuresConcatenatedDTCWT_SecondOriented(nanLocations) = 0;
nanLocations = isnan(featuresConcatenatedDTCWT_ThirdOriented);
featuresConcatenatedDTCWT_ThirdOriented(nanLocations) = 0;
nanLocations = isnan(featuresConcatenatedDTCWT_FourthOriented);
featuresConcatenatedDTCWT_FourthOriented(nanLocations) = 0;
nanLocations = isnan(featuresConcatenatedDTCWT_FifthOriented);
featuresConcatenatedDTCWT_FifthOriented(nanLocations) = 0;
nanLocations = isnan(featuresConcatenatedDTCWT_SixthOriented);
featuresConcatenatedDTCWT_SixthOriented(nanLocations) = 0;
nanLocations = isnan(featuresConcatenatedCOARSEDTCWT);
featuresConcatenatedCOARSEDTCWT(nanLocations) = 0;

TobeSavedFileName1 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedCOARSEDTCWT.mat";
TobeSavedFileName2 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedDTCWT_FirstOriented.mat";
TobeSavedFileName3 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedDTCWT_SecondOriented.mat";
TobeSavedFileName4 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedDTCWT_ThirdOriented.mat";
TobeSavedFileName5 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedDTCWT_FourthOriented.mat";
TobeSavedFileName6 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedDTCWT_FifthOriented.mat";
TobeSavedFileName7 = "reference_Date_" + num2str(dates)+ "_" +textureNames(k) + "_" + "featuresConcatenatedDTCWT_SixthOriented.mat";


save(TobeSavedFileName1,"featuresConcatenatedCOARSEDTCWT")
save(TobeSavedFileName2,"featuresConcatenatedDTCWT_FirstOriented")
save(TobeSavedFileName3,"featuresConcatenatedDTCWT_SecondOriented")
save(TobeSavedFileName4,"featuresConcatenatedDTCWT_ThirdOriented")
save(TobeSavedFileName5,"featuresConcatenatedDTCWT_FourthOriented")
save(TobeSavedFileName6,"featuresConcatenatedDTCWT_FifthOriented")
save(TobeSavedFileName7,"featuresConcatenatedDTCWT_SixthOriented")
end
