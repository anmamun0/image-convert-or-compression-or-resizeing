import fitz

def pdf_to_jpg(pdf_path, jpg_path, dpi=300):
    # Open the PDF
    pdf_doc = fitz.open(pdf_path)
    # Get the first page
    page = pdf_doc[0]
    # Render the page at a high DPI
    pix = page.get_pixmap(dpi=dpi, alpha=False)
    # Save the image as a JPEG
    pix.save(jpg_path, "JPEG")
    print("PDF converted to JPEG successfully!")

# Usage example
pdf_to_jpg("example.pdf", "example.jpg", dpi=300)


# Sure, I can explain the code to you.

#     The first line imports the fitz module, which is a part of the PyMuPDF library. This library is used to work with PDF files in Python.

#     The next line defines a function called "pdf_to_jpg" which takes in three parameters:
#         pdf_path: the path to the PDF file that needs to be converted
#         jpg_path: the path where the resulting JPEG image should be saved
#         dpi (optional): the DPI (dots per inch) at which the image should be rendered. The default value is 300.

#     Inside the function, the first thing we do is open the PDF file using the fitz.open() function. This function returns a pdf_doc object, which is a handle to the PDF file.

#     Next, we get the first page of the PDF using pdf_doc[0].

#     Then, we render the page at a high DPI using the page.get_pixmap() function. This function takes in two parameters: dpi and alpha. Dpi is the resolution of the image and alpha is a boolean value indicating whether or not to include an alpha channel in the image.

#     We then save the image as a JPEG using the pix.save() function. This function takes in two parameters: the path to save the image and the image format.

#     Finally, we print a message indicating that the conversion was successful.

#     In the last line, we call the function with three parameters, where "example.pdf" is the pdf_path, "example.jpg" is the jpg_path and dpi = 300.

# You can call this function by passing the path of your pdf and jpg file to the function and also you can change the dpi value if you want a higher quality image.

