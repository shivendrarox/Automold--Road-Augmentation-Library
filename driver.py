import Automold as am
import Helpers as hp
import cv2
import math
path='./image6.jpg'
images= hp.load_images(path)

##snowy_images= am.add_snow(images, snow_coeff=0.3) 
#cv2.imwrite('./home-new.jpg',cv2.cvtColor(snowy_images[0], cv2.COLOR_RGB2BGR))

#rainy_images= am.add_rain(images, rain_type='heavy', slant=20) 
#cv2.imwrite('./rainy_images.jpg',rainy_images[0])

fall_images= am.add_autumn(images) 
cv2.imwrite('./fall_images.jpg',cv2.cvtColor(fall_images[0], cv2.COLOR_RGB2BGR))

sunny_images= am.add_sun_flare(images,flare_center=(100,100), angle=-math.pi/4) 
cv2.imwrite('./sunny_images.jpg',cv2.cvtColor(sunny_images[0], cv2.COLOR_RGB2BGR))