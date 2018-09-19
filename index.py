# import the necessary packages
import numpy as np
import argparse
import _pickle as cPickle
import glob
import imutils
import cv2
import mahotas

# python index.py --library --index index.cpickle

class ZernikeMoments:
	def __init__(self, radius):
		# store the size of the radius that will be
		# used when computing moments
		self.radius = radius
 
	def describe(self, image):
		# return the Zernike moments for the image
		return mahotas.features.zernike_moments(image, self.radius)
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--library", required = True,
                #help = "/home/pi/Desktop/DoorMasks")
    help = "/Users/jaspreetranjit/ghostbird-master/contours/library/")
ap.add_argument("-i", "--index", required = True,
                #help = "/home/pi/Desktop/indexFiles")
    help = "/Users/jaspreetranjit/ghostbird-master/contours/indexFiles/")
args = vars(ap.parse_args())
 
# initialize our descriptor (Zernike Moments with a radius
# of 21 used to characterize the shape) and
# our index dictionary
desc = ZernikeMoments(21)
index = {}

# loop over the sprite images
for spritePath in glob.glob(args["library"] + "/*.JPG"):
    # parse out the pokemon name, then load the image and
    # convert it to grayscale
    door = spritePath[spritePath.rfind("/") + 1:].replace(".JPG", "")
    image = cv2.imread(spritePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
	# pad the image with extra white pixels to ensure the
	# edges of the pokemon are not up against the borders
	# of the image
    image = cv2.copyMakeBorder(image, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value = 255)
 
	# invert the image and threshold it
    thresh = cv2.bitwise_not(image)
    thresh[thresh > 0] = 255
	
	
	# initialize the outline image, find the outermost
	# contours (the outline) of the pokemone, then draw
	# it
    outline = np.zeros(image.shape, dtype = "uint8")
    if imutils.is_cv2():
        #(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        #cv2.CHAIN_APPROX_SIMPLE) [-2]
        (cnts, _) = cv2.findContours(im_thresh1.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE) [-2]
    elif imutils.is_cv3():
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2]

    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    cv2.drawContours(outline, [cnts], -1, 255, -1)
	
    moments = desc.describe(outline)
    index[door] = moments
	
f = open(args["index"], "wb")
f.write(cPickle.dumps(index))
f.close()

##########################################################
###########       SIMPLE PHEUDOCODE            ###########
##########################################################
from imutils.video import VideoStream

'''
@param directory A filepath to a directory containing zernike moments that need to be loaded. Example: "moments/door/"
@return a list of loaded zernike moments that were in 'directory'
'''
def load_zernike_moments(directory):
    print("loading zernike moments. . .")

'''
@param image an RGB image
@return a transformed image.
Currently, this function is intended to apply color simplification to the image. It may be extended later for further transformations
'''
def transform(image):
    print("transforming image. . .")

'''
@param moment a Zernike moment
@param image a transformed image
@return the hitbox the Zernike moment sees in the image. This may be NULL.
@pre the imagemust be transformed
This function extracts a hitbox from an image using a Zernike moment. If the moment doesn't see an object in the image, it should return null.
'''
def getHitbox(moment, image):
        print("getting hitbox. . .")

'''
@param hitboxes A list of hitboxes extracted from an image using different Zernike moments
@return an 'average' hitbox: ideally, where the object is
'''
def avgHitbox(hitboxes):
    print("getting average hitbox. . . ")

vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
moments_directory = ""
moments = load_zernike_moments(moments_directory)
while True:
    # grab the current frame and initialize the status text
    image = vs.read()
    image = transform(image)

    hitboxes = []
    for moment in moments:
        hitboxes.append(getHitbox(moment, image))
    hitbox = avgHitbox(hitboxes)
