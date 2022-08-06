import cv2
img = cv2.imread('img0.webp',0)
print("Height = " + str(len(img)))
print("Weight = " +str(len(img[0])))
print(img[0])
cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()