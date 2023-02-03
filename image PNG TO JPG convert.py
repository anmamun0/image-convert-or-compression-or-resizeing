from PIL import Image

# Open the PNG Image's 
img = Image.open('input.png')

# Convert the image to RGB mode. which does not have an alpha channel
img = img.convert('RGB')

# Save the PJG image
img.save('output.jpg','JPEG')
print('Done PNG TO JPG')