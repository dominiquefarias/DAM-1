from PIL import Image

# Open the image
img = Image.open("camara_imagen.png")

# Get the first pixel (top-left corner)
first_pixel = img.getpixel((0, 0))

# Print the pixel tuple
print(first_pixel)