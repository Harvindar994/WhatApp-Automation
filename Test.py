# First import wget python module.
import wget

# Set up the image URL
image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# Use wget download method to download specified image url.
image_filename = wget.download(image_url)

print('Image Successfully Downloaded: ', image_filename)