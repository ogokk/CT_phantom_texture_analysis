"""
Multi-violin plot analysis of all texture phantoms across all CT scans 
First date referenced for the follow-up assessment
Both GLCM and DTCWT methods are evaluated  using 
the custom 3D-printed phantom and CCR Honeycomb phantom dataset. 

"""

from scipy import io
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
#from glob import glob
import os
import numpy as np


# prefixes = ["vertical_", "horizontal_", "star4_", "star8_", "sinusoidal_",
#             "square_", "diagonal_", "honeysmall_", "honeymedium_", "honeylarge_",
#             "CCR_All_honey_1_", "CCR_All_honey_2_","CCR_All_honey_3_","CCR_All_honey_4_"]

prefixes = ["vertical_", "horizontal_", "star4_", "star8_", "sinusoidal_",
            "square_", "diagonal_", "honeysmall_", "honeymedium_", "honeylarge_"]



for prefix in prefixes:
    print(prefix)
    globals()[f'{prefix}featuresConcatenatedGLCM'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedGLCM.mat')['featuresConcatenatedGLCM']
    
    globals()[f'{prefix}featuresConcatenatedCOARSEDTCWT'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedCOARSEDTCWT.mat')['featuresConcatenatedCOARSEDTCWT']
    
    globals()[f'{prefix}featuresConcatenatedDTCWT_FirstOriented'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedDTCWT_FirstOriented.mat')['featuresConcatenatedDTCWT_FirstOriented']
    
    globals()[f'{prefix}featuresConcatenatedDTCWT_SecondOriented'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedDTCWT_SecondOriented.mat')['featuresConcatenatedDTCWT_SecondOriented']
    
    globals()[f'{prefix}featuresConcatenatedDTCWT_ThirdOriented'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedDTCWT_ThirdOriented.mat')['featuresConcatenatedDTCWT_ThirdOriented']
    
    globals()[f'{prefix}featuresConcatenatedDTCWT_FourthOriented'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedDTCWT_FourthOriented.mat')['featuresConcatenatedDTCWT_FourthOriented']
    
    globals()[f'{prefix}featuresConcatenatedDTCWT_FifthOriented'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedDTCWT_FifthOriented.mat')['featuresConcatenatedDTCWT_FifthOriented']
    
    globals()[f'{prefix}featuresConcatenatedDTCWT_SixthOriented'] = io.loadmat(f'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
        f'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/{prefix}featuresConcatenatedDTCWT_SixthOriented.mat')['featuresConcatenatedDTCWT_SixthOriented']

    # Check NaNs
    globals()[f'{prefix}featuresConcatenatedGLCM'][np.isnan(globals()[f'{prefix}featuresConcatenatedGLCM'])] = 0
    globals()[f'{prefix}featuresConcatenatedCOARSEDTCWT'][np.isnan(globals()[f'{prefix}featuresConcatenatedCOARSEDTCWT'])] = 0
    globals()[f'{prefix}featuresConcatenatedDTCWT_FirstOriented'][np.isnan(globals()[f'{prefix}featuresConcatenatedDTCWT_FirstOriented'])] = 0
    globals()[f'{prefix}featuresConcatenatedDTCWT_SecondOriented'][np.isnan(globals()[f'{prefix}featuresConcatenatedDTCWT_SecondOriented'])] = 0
    globals()[f'{prefix}featuresConcatenatedDTCWT_ThirdOriented'][np.isnan(globals()[f'{prefix}featuresConcatenatedDTCWT_ThirdOriented'])] = 0
    globals()[f'{prefix}featuresConcatenatedDTCWT_FourthOriented'][np.isnan(globals()[f'{prefix}featuresConcatenatedDTCWT_FourthOriented'])] = 0
    globals()[f'{prefix}featuresConcatenatedDTCWT_FifthOriented'][np.isnan(globals()[f'{prefix}featuresConcatenatedDTCWT_FifthOriented'])] = 0
    globals()[f'{prefix}featuresConcatenatedDTCWT_SixthOriented'][np.isnan(globals()[f'{prefix}featuresConcatenatedDTCWT_SixthOriented'])] = 0



# prefixes = ["vertical_", "horizontal_", "star4_", "star8_", "sinusoidal_",
#             "square_", "diagonal_", "honeysmall_", "honeymedium_", "honeylarge_"]
for phantom_idx,_ in enumerate(prefixes):
    prefix_texture = prefixes[phantom_idx]
    df_glcm = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedGLCM'])
    df_coarse = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedCOARSEDTCWT'])
    df_first = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedDTCWT_FirstOriented'])
    df_second = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedDTCWT_SecondOriented'])
    df_third = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedDTCWT_ThirdOriented'])
    df_fourth = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedDTCWT_FourthOriented'])
    df_fifth = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedDTCWT_FifthOriented'])
    df_sixth = pd.DataFrame(globals()[f'{prefix_texture}featuresConcatenatedDTCWT_SixthOriented'])
    
 
    
    
    
    # Horizontal reference first date for GLCM and COARSE DTCWT
    reference_Date_241016_horizontal_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_horizontal_featuresConcatenatedGLCM.mat')
    reference_Date_241016_horizontal_featuresConcatenatedGLCM = reference_Date_241016_horizontal_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_horizontal_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_horizontal_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_horizontal_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_horizontal_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    
    # Vertical reference first date for GLCM and COARSE DTCWT
    reference_Date_241016_vertical_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_vertical_featuresConcatenatedGLCM.mat')
    reference_Date_241016_vertical_featuresConcatenatedGLCM = reference_Date_241016_vertical_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_vertical_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_vertical_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_vertical_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_vertical_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    
    
    # Diagonal reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_diagonal_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_diagonal_featuresConcatenatedGLCM.mat')
    reference_Date_241016_diagonal_featuresConcatenatedGLCM = reference_Date_241016_diagonal_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_diagonal_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_diagonal_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_diagonal_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_diagonal_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    # HoneyLarge reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_honeylarge_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeylarge_featuresConcatenatedGLCM.mat')
    reference_Date_241016_honeylarge_featuresConcatenatedGLCM = reference_Date_241016_honeylarge_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_honeylarge_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeylarge_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_honeylarge_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_honeylarge_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    # HoneyMedium reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_honeymedium_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeymedium_featuresConcatenatedGLCM.mat')
    reference_Date_241016_honeymedium_featuresConcatenatedGLCM = reference_Date_241016_honeymedium_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_honeymedium_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeylarge_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_honeymedium_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_honeymedium_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    
    # HoneySmall reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_honeysmall_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeysmall_featuresConcatenatedGLCM.mat')
    reference_Date_241016_honeysmall_featuresConcatenatedGLCM = reference_Date_241016_honeysmall_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_honeysmall_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeysmall_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_honeysmall_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_honeysmall_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    # Sinusoidal reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_sinusoidal_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_sinusoidal_featuresConcatenatedGLCM.mat')
    reference_Date_241016_sinusoidal_featuresConcatenatedGLCM = reference_Date_241016_sinusoidal_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_sinusoidal_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_honeysmall_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_sinusoidal_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_sinusoidal_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    
    # Sqaure reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_square_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_square_featuresConcatenatedGLCM.mat')
    reference_Date_241016_square_featuresConcatenatedGLCM = reference_Date_241016_square_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_square_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_square_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_square_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_square_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    # Star4 reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_star4_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_star4_featuresConcatenatedGLCM.mat')
    reference_Date_241016_star4_featuresConcatenatedGLCM = reference_Date_241016_star4_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_star4_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_star4_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_star4_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_star4_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    # Star8 reference first date for GLCM and COARSE DTCWT
    
    reference_Date_241016_star8_featuresConcatenatedGLCM = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_star8_featuresConcatenatedGLCM.mat')
    reference_Date_241016_star8_featuresConcatenatedGLCM = reference_Date_241016_star8_featuresConcatenatedGLCM['featuresConcatenatedGLCM']
    
    reference_Date_241016_star8_featuresConcatenatedCOARSEDTCWT = io.loadmat(r'C:/Users/Bio İzmir/Desktop/Ozan_1001/1001'
                          r'/dtcwt_glcm_reproducible_features/AllFeaturesMatFiles/reference_Date_241016_star8_featuresConcatenatedCOARSEDTCWT.mat')
    reference_Date_241016_star8_featuresConcatenatedCOARSEDTCWT = reference_Date_241016_star8_featuresConcatenatedCOARSEDTCWT['featuresConcatenatedCOARSEDTCWT']
    
    
    
    # Reference digital phantoms check for NaNs
    # reference_featuresConcatenatedGLCM[np.isnan(reference_featuresConcatenatedGLCM)] = 0
    # reference_featuresConcatenatedCOARSEDTCWT[np.isnan(reference_featuresConcatenatedCOARSEDTCWT)] = 0
    # reference_featuresConcatenatedDTCWT_FirstOriented[np.isnan(reference_featuresConcatenatedDTCWT_FirstOriented)] = 0
    # reference_featuresConcatenatedDTCWT_SecondOriented[np.isnan(reference_featuresConcatenatedDTCWT_SecondOriented)] = 0
    # reference_featuresConcatenatedDTCWT_ThirdOriented[np.isnan(reference_featuresConcatenatedDTCWT_ThirdOriented)] = 0
    # reference_featuresConcatenatedDTCWT_FourthOriented[np.isnan(reference_featuresConcatenatedDTCWT_FourthOriented)] = 0
    # reference_featuresConcatenatedDTCWT_FifthOriented[np.isnan(reference_featuresConcatenatedDTCWT_FifthOriented)] = 0
    # reference_featuresConcatenatedDTCWT_SixthOriented[np.isnan(reference_featuresConcatenatedDTCWT_SixthOriented)] = 0
    
    
    # df_glcm_ref = pd.DataFrame(reference_featuresConcatenatedGLCM)
    # df_coarse_ref = pd.DataFrame(reference_featuresConcatenatedCOARSEDTCWT)
    # df_first_ref = pd.DataFrame(reference_featuresConcatenatedDTCWT_FirstOriented)
    # df_second_ref = pd.DataFrame(reference_featuresConcatenatedDTCWT_SecondOriented)
    # df_third_ref = pd.DataFrame(reference_featuresConcatenatedDTCWT_ThirdOriented)
    # df_fourth_ref = pd.DataFrame(reference_featuresConcatenatedDTCWT_FourthOriented)
    # df_fifth_ref = pd.DataFrame(reference_featuresConcatenatedDTCWT_FifthOriented)
    # df_sixth_ref = pd.DataFrame(reference_featuresConcatenatedDTCWT_SixthOriented)
    
    
    
    df_glcm_ref_horizontal_first_date = pd.DataFrame(reference_Date_241016_horizontal_featuresConcatenatedGLCM)
    df_coarse_ref_horizontal_first_date = pd.DataFrame(reference_Date_241016_horizontal_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_vertical_first_date = pd.DataFrame(reference_Date_241016_vertical_featuresConcatenatedGLCM)
    df_coarse_ref_vertical_first_date = pd.DataFrame(reference_Date_241016_vertical_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_diagonal_first_date = pd.DataFrame(reference_Date_241016_diagonal_featuresConcatenatedGLCM)
    df_coarse_ref_diagonal_first_date = pd.DataFrame(reference_Date_241016_diagonal_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_honeylarge_first_date = pd.DataFrame(reference_Date_241016_honeylarge_featuresConcatenatedGLCM)
    df_coarse_ref_honeylarge_first_date = pd.DataFrame(reference_Date_241016_honeylarge_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_honeymedium_first_date = pd.DataFrame(reference_Date_241016_honeymedium_featuresConcatenatedGLCM)
    df_coarse_ref_honeymedium_first_date = pd.DataFrame(reference_Date_241016_honeymedium_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_honeysmall_first_date = pd.DataFrame(reference_Date_241016_honeysmall_featuresConcatenatedGLCM)
    df_coarse_ref_honeysmall_first_date = pd.DataFrame(reference_Date_241016_honeysmall_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_sinusoidal_first_date = pd.DataFrame(reference_Date_241016_sinusoidal_featuresConcatenatedGLCM)
    df_coarse_ref_sinusoidal_first_date = pd.DataFrame(reference_Date_241016_sinusoidal_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_square_first_date = pd.DataFrame(reference_Date_241016_square_featuresConcatenatedGLCM)
    df_coarse_ref_square_first_date = pd.DataFrame(reference_Date_241016_square_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_star4_first_date = pd.DataFrame(reference_Date_241016_star4_featuresConcatenatedGLCM)
    df_coarse_ref_star4_first_date = pd.DataFrame(reference_Date_241016_star4_featuresConcatenatedCOARSEDTCWT)
    df_glcm_ref_star8_first_date = pd.DataFrame(reference_Date_241016_star8_featuresConcatenatedGLCM)
    df_coarse_ref_star8_first_date = pd.DataFrame(reference_Date_241016_star8_featuresConcatenatedCOARSEDTCWT)
 
    
    columns = [
        'Energy', 'Contrast', 'Correlation', 'Variance', 
        'Homogeneity', 'Sum Average', 'Sum Variance', 'Sum Entropy', 
        'Entropy', 'Difference Variance', 'Difference Entropy', 'Correlation I', 
        'Correlation II', 'Maximal Correlation'
    ]
    

    
    df_glcm_ref_horizontal_first_date.columns = columns
    df_coarse_ref_horizontal_first_date.columns = columns
    df_glcm_ref_vertical_first_date.columns = columns
    df_coarse_ref_vertical_first_date.columns = columns
    df_glcm_ref_diagonal_first_date.columns = columns
    df_coarse_ref_diagonal_first_date.columns = columns
    df_glcm_ref_honeylarge_first_date.columns = columns
    df_coarse_ref_honeylarge_first_date.columns = columns
    df_glcm_ref_honeymedium_first_date.columns = columns
    df_coarse_ref_honeymedium_first_date.columns = columns
    df_glcm_ref_honeysmall_first_date.columns = columns
    df_coarse_ref_honeysmall_first_date.columns = columns
    df_glcm_ref_sinusoidal_first_date.columns = columns
    df_coarse_ref_sinusoidal_first_date.columns = columns
    df_glcm_ref_square_first_date.columns = columns
    df_coarse_ref_square_first_date.columns = columns
    df_glcm_ref_star4_first_date.columns = columns
    df_coarse_ref_star4_first_date.columns = columns
    df_glcm_ref_star8_first_date.columns = columns
    df_coarse_ref_star8_first_date.columns = columns
    

    df_glcm.columns = columns
    df_coarse.columns = columns
    df_first.columns = columns
    df_second.columns = columns
    df_third.columns = columns
    df_fourth.columns = columns
    df_fifth.columns = columns
    df_sixth.columns = columns
    
    # Math for MinMaxScaler
    # X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    # X_scaled = X_std * (max - min) + min
    scaler = MinMaxScaler(feature_range=(0,1))
    
    df_glcm_normalized   = pd.DataFrame(scaler.fit_transform(df_glcm), columns=df_glcm.columns)
    df_coarse_normalized = pd.DataFrame(scaler.fit_transform(df_coarse), columns=df_coarse.columns)
    df_first_normalized  = pd.DataFrame(scaler.fit_transform(df_first), columns=df_first.columns)
    df_second_normalized  = pd.DataFrame(scaler.fit_transform(df_second), columns=df_second.columns)
    df_third_normalized  = pd.DataFrame(scaler.fit_transform(df_third), columns=df_third.columns)
    df_fourth_normalized  = pd.DataFrame(scaler.fit_transform(df_fourth), columns=df_fourth.columns)
    df_fifth_normalized  = pd.DataFrame(scaler.fit_transform(df_fifth), columns=df_fifth.columns)
    df_sixth_normalized  = pd.DataFrame(scaler.fit_transform(df_sixth), columns=df_sixth.columns)
    
    
    # ref order : diagonal, horizontal, sinusoidal, square, star4, star8, vertical
    ref_order = {
      "diagonal_": 0,
      "horizontal_": 1,
      "sinusoidal_": 2,
      "square_": 3,
      "star4_": 4,
      "star8_": 5,
      "vertical_": 6
    }
    

    
    df_glcm_ref_horizontal_first_date   = pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_horizontal_first_date)), columns=df_glcm_ref_horizontal_first_date.columns)
    df_coarse_ref_horizontal_first_date = pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_horizontal_first_date)), columns=df_coarse_ref_horizontal_first_date.columns)
    df_glcm_ref_vertical_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_vertical_first_date)), columns=df_glcm_ref_vertical_first_date.columns)
    df_coarse_ref_vertical_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_vertical_first_date)), columns=df_coarse_ref_vertical_first_date.columns)
    df_glcm_ref_diagonal_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_diagonal_first_date)), columns=df_glcm_ref_diagonal_first_date.columns)
    df_coarse_ref_diagonal_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_diagonal_first_date)), columns=df_coarse_ref_diagonal_first_date.columns)
    df_glcm_ref_honeylarge_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_honeylarge_first_date)), columns=df_glcm_ref_honeylarge_first_date.columns)
    df_coarse_ref_honeylarge_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_honeylarge_first_date)), columns=df_coarse_ref_honeylarge_first_date.columns)
    df_glcm_ref_honeymedium_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_honeymedium_first_date)), columns=df_glcm_ref_honeymedium_first_date.columns)
    df_coarse_ref_honeymedium_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_honeymedium_first_date)), columns=df_coarse_ref_honeymedium_first_date.columns)
    df_glcm_ref_honeysmall_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_honeysmall_first_date)), columns=df_glcm_ref_honeysmall_first_date.columns)
    df_coarse_ref_honeysmall_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_honeysmall_first_date)), columns=df_coarse_ref_honeysmall_first_date.columns)
    df_glcm_ref_sinusoidal_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_sinusoidal_first_date)), columns=df_glcm_ref_sinusoidal_first_date.columns)
    df_coarse_ref_sinusoidal_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_sinusoidal_first_date)), columns=df_coarse_ref_sinusoidal_first_date.columns)
    df_glcm_ref_square_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_square_first_date)), columns=df_glcm_ref_square_first_date.columns)
    df_coarse_ref_square_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_square_first_date)), columns=df_coarse_ref_square_first_date.columns)
    df_glcm_ref_star4_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_star4_first_date)), columns=df_glcm_ref_star4_first_date.columns)
    df_coarse_ref_star4_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_star4_first_date)), columns=df_coarse_ref_star4_first_date.columns)
    df_glcm_ref_star8_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_glcm_ref_star8_first_date)), columns=df_glcm_ref_star8_first_date.columns)
    df_coarse_ref_star8_first_date= pd.DataFrame(scaler.fit_transform(np.absolute(df_coarse_ref_star8_first_date)), columns=df_coarse_ref_star8_first_date.columns)
    
    
    df_glcm_ref_horizontal_first_date_median_vector = round(df_glcm_ref_horizontal_first_date.median().to_frame().T,3)
    df_coarse_ref_horizontal_first_date_median_vector = round(df_coarse_ref_horizontal_first_date.median().to_frame().T,3)
    df_glcm_ref_vertical_first_date_median_vector = round(df_glcm_ref_vertical_first_date.median().to_frame().T,3)
    df_coarse_ref_vertical_first_date_median_vector = round(df_coarse_ref_vertical_first_date.median().to_frame().T,3) 
    df_glcm_ref_diagonal_first_date_median_vector = round(df_glcm_ref_diagonal_first_date.median().to_frame().T,3) 
    df_coarse_ref_diagonal_first_date_median_vector = round(df_coarse_ref_diagonal_first_date.median().to_frame().T,3)  
    df_glcm_ref_honeylarge_first_date_median_vector = round(df_glcm_ref_honeylarge_first_date.median().to_frame().T,3) 
    df_coarse_ref_honeylarge_first_date_median_vector = round(df_coarse_ref_honeylarge_first_date.median().to_frame().T,3) 
    df_glcm_ref_honeymedium_first_date_median_vector = round(df_glcm_ref_honeymedium_first_date.median().to_frame().T,3) 
    df_coarse_ref_honeymedium_first_date_median_vector = round(df_coarse_ref_honeymedium_first_date.median().to_frame().T,3) 
    df_glcm_ref_honeysmall_first_date_median_vector = round(df_glcm_ref_honeysmall_first_date.median().to_frame().T,3) 
    df_coarse_ref_honeysmall_first_date_median_vector = round(df_coarse_ref_honeysmall_first_date.median().to_frame().T,3) 
    df_glcm_ref_sinusoidal_first_date_median_vector = round(df_glcm_ref_sinusoidal_first_date.median().to_frame().T,3) 
    df_coarse_ref_sinusoidal_first_date_median_vector = round(df_coarse_ref_sinusoidal_first_date.median().to_frame().T,3) 
    df_glcm_ref_square_first_date_median_vector = round(df_glcm_ref_square_first_date.median().to_frame().T,3) 
    df_coarse_ref_square_first_date_median_vector = round(df_coarse_ref_square_first_date.median().to_frame().T,3) 
    df_glcm_ref_star4_first_date_median_vector = round(df_glcm_ref_star4_first_date.median().to_frame().T,3) 
    df_coarse_ref_star4_first_date_median_vector = round(df_coarse_ref_star4_first_date.median().to_frame().T,3) 
    df_glcm_ref_star8_first_date_median_vector = round(df_glcm_ref_star8_first_date.median().to_frame().T,3) 
    df_coarse_ref_star8_first_date_median_vector = round(df_coarse_ref_star8_first_date.median().to_frame().T,3) 
    
    
    
    df_glcm_melted = df_glcm_normalized.melt(var_name='Feature', value_name='Value')
    df_glcm_melted['Methods'] = 'GLCM'
    
    df_coarse_melted = df_coarse_normalized.melt(var_name='Feature', value_name='Value')
    df_coarse_melted['Methods'] = 'Coarse DTCWT'
    
    
    df_first_melted = df_first_normalized.melt(var_name='Feature', value_name='Value')
    df_first_melted['Methods'] = 'First Oriented DTCWT'
    
    
    df_second_melted = df_second_normalized.melt(var_name='Feature', value_name='Value')
    df_second_melted['Methods'] = 'Second Oriented DTCWT'
    
    df_third_melted = df_third_normalized.melt(var_name='Feature', value_name='Value')
    df_third_melted['Methods'] = 'Third Oriented DTCWT'
    
    df_fourth_melted = df_fourth_normalized.melt(var_name='Feature', value_name='Value')
    df_fourth_melted['Methods'] = 'Fourth Oriented DTCWT'
    
    df_fifth_melted = df_fifth_normalized.melt(var_name='Feature', value_name='Value')
    df_fifth_melted['Methods'] = 'Fifth Oriented DTCWT'
    
    df_sixth_melted = df_sixth_normalized.melt(var_name='Feature', value_name='Value')
    df_sixth_melted['Methods'] = 'Sixth Oriented DTCWT'
    
    
    
    df_combined = pd.concat([df_glcm_melted, df_coarse_melted, df_first_melted, 
                             df_second_melted, df_third_melted,
                             df_fourth_melted,df_fifth_melted, df_sixth_melted], ignore_index=True)
    
    
    
    palette = {"GLCM": "pastel6", 
                'Coarse DTCWT': "terrain_r",
                'First Oriented DTCWT': "coolwarm", 
                'Second Oriented DTCWT': "flare",
                'Third Oriented DTCWT': "bright", 
                'Fourth Oriented DTCWT': "Set3",
                'Fifth Oriented DTCWT': "dark", 
                'Sixth Oriented DTCWT': "deep"}
    
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_xlabel("Feature Types", fontsize=14) 
    ax.set_ylabel("Normalized Feature Values", fontsize=14)  
    ax.set_title(f"Violin Plots of {prefix_texture[:-1].title()} Texture", fontsize=16)
    
    

    
    features = [
        "Energy", "Contrast", "Correlation", "Variance", "Homogeneity", 
        "Sum Average", "Sum Variance", "Sum Entropy", "Entropy", 
        "Difference Variance", "Difference Entropy", 
        "Correlation I", "Correlation II", "Maximal Correlation"
    ]
    
    for i, feature in enumerate(features):
        y_value = globals()[f"df_glcm_ref_{prefix_texture}first_date_median_vector"][feature].iloc[0]
        ax.plot(i, y_value, marker="*", color="r", markersize=20)
        plt.text(i + 0.1, y_value, str(y_value), color="r", fontsize=14)
        
    
    
    for i, feature in enumerate(features):
        y_value = globals()[f"df_coarse_ref_{prefix_texture}first_date_median_vector"][feature].iloc[0]
        ax.plot(i, y_value, marker="*", color="y", markersize=20)
        plt.text(i + 0.1, y_value, str(y_value), color="y", fontsize=14)
    
    ax.plot([], [], marker='*', color='r', label='GLCM Reference Values [1st Date for CT imaging]', linestyle='None', markersize=10)
    ax.plot([], [], marker='*', color='y', label='Coarse DTCWT Reference Values [1st Date for CT imaging]', linestyle='None', markersize=10)
    ax.legend()
    
    
    
    
    plt.xticks(rotation=15, fontsize=12)  
    
    # color palettes --> https://seaborn.pydata.org/tutorial/color_palettes.html
    rocket_cmap = sns.color_palette("flare", as_cmap=True)
    
    # Spaced colors from the colormap for DTCWT feature groups
    num_methods = 7  # coarse,1st,2nd,3rd,4th,5th,6th
    color_positions = np.linspace(0.2, 0.9, num_methods)
    dtcwt_colors = [rocket_cmap(pos) for pos in color_positions]
    
    methods = [
    "GLCM", 
    "Coarse DTCWT", 
    "First Oriented DTCWT", 
    "Second Oriented DTCWT", 
    "Third Oriented DTCWT", 
    "Fourth Oriented DTCWT", 
    "Fifth Oriented DTCWT", 
    "Sixth Oriented DTCWT"
     ]

    palette = {"GLCM": sns.color_palette("pastel6")[0]}
     
    dtcwt_methods = [method for method in methods if method != "GLCM"]
    
    for i, method in enumerate(dtcwt_methods):
        palette[method] = dtcwt_colors[i]  
    
    
    
    for method in methods:
        sns.violinplot(
            x="Feature", 
            y="Value", 
            hue="Methods",  
            data=df_combined[df_combined['Methods'] == method],
            palette=[palette[method]],
            split=False,
            ax=ax,
            density_norm="count",
            common_norm=True,
            saturation=5.75
        )
    
    for violin in ax.collections:
        violin.set_alpha(0.25)
        
    
    
    std_path = os.path.expanduser("~/Desktop/SD.txt")
    
    with open(std_path, "a") as file:
        file.write("\n----------------------****************************-------------------\n")
        file.write(f"\nStandard Deviations of Each Feature for {prefix_texture} \n\n")
        file.write("------------------------****************************-------------------\n")
        print(f"Standard Deviations of Each Feature for {prefix_texture} \n")
        print("----------------------****************************-------------------\n")
        for feature in features:
            glcm_values = df_combined[(df_combined["Methods"] == "GLCM") & (df_combined["Feature"] == feature)]["Value"]
            std_dev_glcm = glcm_values.std()
    
            dtcwt_values = df_combined[(df_combined["Methods"] != "GLCM") & (df_combined["Feature"] == feature)]["Value"]
            std_dev_dtcwt = dtcwt_values.std()
    
            print(f"Standard Deviation of {feature} values [GLCM]: {std_dev_glcm}")
            print(f"Standard Deviation of {feature} values [DTCWT group]: {std_dev_dtcwt}")

            file.write(f"Standard Deviation of {feature} values [GLCM]: {std_dev_glcm}\n")
            file.write(f"Standard Deviation of {feature} values [DTCWT group]: {std_dev_dtcwt}\n")
            file.write("-" * 50 + "\n")
    
    print("-" * 70)    
    print("-" * 70 + "\n\n")    

    os.chdir("C:/Users/Bio İzmir/Desktop/violinplots")
    plt.savefig(f"{prefix_texture[:-1]}_multi_violinplots.png", dpi=600)
    plt.show()

