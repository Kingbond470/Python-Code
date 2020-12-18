from PIL import Image, ImageFilter 
  
# creating a image object 
im1 = Image.open(r"mathintro.JPG") 
  
# applying the blur filter 
im2 = im1.filter(ImageFilter.BLUR) 
  
im2.show() 