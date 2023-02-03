from PIL import Image
import os

# List of JPG files to be converted
jpg_files = ["image1.jpg", "image2.jpg", "image3.jpg","image4.jpg"]

# Create a new PDF file with PIL
pdf_file = Image.open(jpg_files[0])
pdf_file.save("images.pdf", save_all=True, append_images=[Image.open(jpg) for jpg in jpg_files[1:]])

# Print confirmation
print("Images converted to PDF and saved as 'images.pdf'.")


# 1- 'import' img2pdf imports the img2pdf library, which allows you to convert image files to PDF.
#  2- jpg_files = ["image1.jpg", "image2.jpg", "image3.jpg"] creates a list of the JPG files that you want to convert to PDF.
#  3 - with open("images.pdf","wb") as f: opens a new file named "images.pdf" in binary write mode and assigns the file object to the variable "f".
# 4 - f.write(img2pdf.convert([i for i in jpg_files])) takes the list of jpg_files and converts it to binary pdf data using the img2pdf.convert function. Then it writes the binary pdf data to the "images.pdf" file using the .write() method of the file object.
# 5- print("Images converted to PDF and saved as 'images.pdf'.") prints a confirmation message indicating that the JPG images have been successfully converted to a PDF file.
