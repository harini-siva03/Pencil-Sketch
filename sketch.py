import cv2

# Step 1: Load the image
image = cv2.imread('flower.jpg')

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Invert the grayscale image
inverted_gray = 255 - gray_image

# Step 4: Apply Gaussian Blur
blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

# Step 5: Invert the blurred image
inverted_blur = 255 - blurred

# Step 6: Create the sketch by dividing grayscale by inverted blur
sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# Step 7: Display
cv2.imshow('Original Image', image)
cv2.imshow('Pencil Sketch', sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
