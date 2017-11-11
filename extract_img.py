import cv2

im = cv2.imread('imgs/httpsmagiccards.infoscansen4e175.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
test = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(len(test))
# contours,hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# idx =0 
# for cnt in contours:
#     idx += 1
#     x,y,w,h = cv2.boundingRect(cnt)
#     roi=im[y:y+h,x:x+w]
#     cv2.imwrite(str(idx) + '.jpg', roi)
#     #cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)
cv2.imshow('img', gray)
cv2.waitKey(0)    