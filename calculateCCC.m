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