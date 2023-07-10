import cv2

# Load the JPEG image
image_jpeg = cv2.imread('image.jpg')

# Load the PNG image with alpha channel (RGBA)
image_png = cv2.imread('image.png', cv2.IMREAD_UNCHANGED)

# Extract the alpha channel from the PNG image
alpha_channel = image_png[:, :, 3]

# Resize the PNG image to match the dimensions of the JPEG image
resized_image_png = cv2.resize(image_png[:, :, 0:3], (image_jpeg.shape[1], image_jpeg.shape[0]))

# Create a mask from the alpha channel
_, mask = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)

# Invert the mask
inverted_mask = cv2.bitwise_not(mask)

# Apply the mask to the JPEG image
background = cv2.bitwise_and(image_jpeg, image_jpeg, mask=inverted_mask)

# Apply the resized PNG image to the JPEG image
foreground = cv2.bitwise_and(resized_image_png, resized_image_png, mask=mask)

# Combine the background and foreground
output = cv2.add(background, foreground)

# Save the resulting image
cv2.imwrite('output.jpg', output)
