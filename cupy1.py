import numpy as np
from scipy.ndimage import gaussian_filter
from PIL import Image
import matplotlib.pyplot as plt

# Load image of our cat
img = Image.open('cat.jpg')
img = np.array(img)

# Apply Gaussian filter
sigma = 1  # Standard deviation for Gaussian kernel
img_filtered = gaussian_filter(img, sigma)

# Save the filtered image
img_filtered = Image.fromarray(img_filtered)
img_filtered.save('filtered_image.png')

# Display the original and filtered images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(img_filtered, cmap='gray')
plt.title('Filtered Image')
plt.show()
