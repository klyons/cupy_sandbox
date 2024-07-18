import cupy as cp
import cv2
from scipy.ndimage import gaussian_filter

# Load image
img = cv2.imread('image.png', 0)
img = cp.asarray(img)  # Convert to CuPy array

# Apply Gaussian filter
sigma = 1  # Standard deviation for Gaussian kernel
img_filtered = gaussian_filter(img, sigma)

# Convert back to NumPy array for further processing with OpenCV
img_filtered = cp.asnumpy(img_filtered)

# Save the cleaned image
cv2.imwrite('cleaned_image.png', img_filtered)
