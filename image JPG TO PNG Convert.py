from PIL import Image

# Open the PNG Image's 
img = Image.open('input.jpg')

# Convert the image to RGB mode. which does not have an alpha channel
img = img.convert('RGB')

# Save the PJG image
img.save('output.png','PNG')

print('Done JPG TO PNG')