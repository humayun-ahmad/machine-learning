import cv2

def main():
	imgpath = "C:\\Users\\C.S.C\\Desktop\\home\\mandril_color.tif"
	img = cv2.imread(imgpath)
	cv2.imshow("picture", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows

if __name__ == '__main__':
	main()