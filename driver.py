import Automold as am
import Helpers as hp
import cv2
path='./test_augmentation/image4.jpg'
images= hp.load_images(path)

snowy_images= am.add_snow(images, snow_coeff=0.3) 
cv2.imwrite('./home-new.jpg',snowy_images[0])