# import statments
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


# main function
def main():
    # Manual inputs
    filename = 'left_eye_2.jpeg'

    # STEP 1
    # Convert from RGB to Grayscale Img using Normal Average
    # Note: Not ideal method to convert to grayscale - should use luminous factors
    original_img = np.array(Image.open(filename))
    grayScale_img_arr = np.mean(original_img, axis=2)
    gray_img = Image.fromarray(grayScale_img_arr.astype(np.uint8))
    grayScaleFilename = filename[:-5] + 'grayscale.jpeg'
    gray_img.save(grayScaleFilename)

    # STEP 2
    # For thresholding used 25x25 block size as given by paper
    # Constant for offset not provided by paper - assumed 0
    # Type of adaptive threshold not indicated - used mean thresholding (not gaussian)
    open_cv_img = cv2.imread(grayScaleFilename, 0)
    threshold_img_cv2 = cv2.adaptiveThreshold(open_cv_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 1)
    thresholdFilename = filename[:-5] + 'threshold.jpeg'
    threshold_img = Image.fromarray(threshold_img_cv2)
    threshold_img.save(thresholdFilename)

    # STEP 3
    # Resize Image to 1000x1000 pixels
    resized_img = threshold_img.resize((1000, 1000))
    resizedFileName = filename[:-5] + 'resized.jpeg'
    resized_img.save(resizedFileName)

    # STEP 4
    # Pixel Rescaling 0 to 1 by dividing each pixel by 255
    # Note: Not ideal normalization method as min/max are not 0-255 in each image
    # Ideal: https://stackoverflow.com/questions/62783984/how-to-normalize-pixel-values-in-an-image-and-save-it
    resized_img_np = np.asarray(resized_img)
    resized_img_np = resized_img_np.astype('float32')
    normalized_img = resized_img_np / 255
    normalized_img = Image.fromarray(normalized_img.astype(np.uint8))
    normalizedFilename = filename[:-5] + 'normalized.jpeg'
    normalized_img.save(normalizedFilename)


# Run main from here
if __name__ == '__main__':
    main()

