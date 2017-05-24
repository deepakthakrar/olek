import cv2

#Second parameter - how to read image(rgb, bw, transparency)
#RGB or nothing - 1
#Black and white - 0
#Transparency - -1

img = cv2.imread("galaxy.jpg", 0)
print(img)
print(img.shape)
print(type(img))

#resize img - rake average/ most similar value of pixels
resized_img = cv2.resize(img, (500, 500))


#Size of image in pixels
#print(img.shape)

#Nu,ber of dimensions in array
print(img.ndim)

#Show image object
cv2.imshow("Galaxy", resized_img)

#Write new image
#cv2.imwrite("Galaxy_resized.jpg", resized_img)
#0 - any button
#Time in milliseconds
cv2.waitKey(0)

#Destroy open window with image
cv2.destroyAllWindows()
