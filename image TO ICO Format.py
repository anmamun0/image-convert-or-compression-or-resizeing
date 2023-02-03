from PIL import Image

# Open the PGP / PNG Image's 
img = Image.open('logo-windows.png')

# Resize the image to fit the ICO format (Usually 256x256)
img = img.resize((256,256))

# Save the ICO Image
img.save('output1.ico','ico')

print('Success YOur converter')