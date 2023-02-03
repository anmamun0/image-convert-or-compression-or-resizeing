import os
from PIL import Image

# Open the image
img = Image.open("input.jpg")

# Set the target file size limit (in MB)
file_size_limit = 1  # 1 MB

# Start with the maximum compression quality
compression_quality = 100

# Compress the image until its file size is below the limit
while True:
    # Save a temporary copy of the image with the current compression quality
    img.save("temp.jpg", "JPEG", quality=compression_quality)
    
    # Check the file size of the temporary image
    file_size = os.path.getsize("temp.jpg") / (1024 * 1024)
    
    # If the file size is below the limit, break the loop
    if file_size <= file_size_limit:
        break
    
    # If the file size is above the limit, reduce the compression quality and try again
    compression_quality -= 5

# Save the final compressed image
img.save("output.jpg", "JPEG", quality=compression_quality)
print("successfully done compression  ")