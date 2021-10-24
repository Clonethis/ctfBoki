from PIL import Image

image = Image.open('old_image.png')
newImage = image.resize((440, 600))
newImage.save('old_image_440&600.png')
