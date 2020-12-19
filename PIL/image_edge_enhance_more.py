
# Importing Image and ImageFilter module from PIL package  
from PIL import Image, ImageFilter 
  
# creating a image object 
im1 = Image.open(r"mathintro.JPG") 
  
# applying the EDGE_ENHANCE_MORE filter 
im2 = im1.filter(ImageFilter.EDGE_ENHANCE_MORE) 
  
im2.show() 
