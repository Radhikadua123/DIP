# Code to implement zooming of images using Python and OpenCV.
import cv2
import argparse
import numpy as np

# Function to crop the region of interest around pivot 
######### Boundary Conditions handled ##################

def region(imgpath, x_pivot, y_pivot,scale):
    image = cv2.imread(imgpath)
    width_orig = image.shape[0]
    height_orig = image.shape[1]

    width_new = float(width_orig)/float(scale)
    height_new = float(height_orig)/float(scale)

    x1 = int(x_pivot - height_new/float(2))
    y1 = int(y_pivot - width_new/float(2))

    x2 = int(x_pivot + height_new/float(2))
    y2 = int(y_pivot + width_new/float(2))

    if(x1<0):
        temp1 = 0-x1
        x1 = 0
        x2 = x2+temp1
    if(y1<0):
        temp2 = 0-y1
        y1 = 0
        y2 = y2+temp2
    if(x2>height_orig):
        temp3 = x2-height_orig
        x2 = height_orig
        x1 = x1-temp3
    if(y2>width_orig):
        temp4 = y2 - width_orig
        y2 = width_orig
        y1 = y1 -temp4

    new_image = image[y1:y2, x1:x2 :]

    return new_image


# Function to zoom the region of interest using replication method.
def zoom(img, width, height, scale):

    img_out = np.zeros((width, height, 3))

    crop_width = img.shape[0]
    crop_height = img.shape[1]

    if(crop_width % 2 != 0):
        crop_width  = crop_width -1
        i,l = 0,0
        for i in range(img.shape[0]):
            s = 0;
            for s in range(scale):
                img_out[l+s ,img_out.shape[1]-1] = img [i,img.shape[1]-1]
            l =l+s

    if(crop_height % 2 != 0):
        crop_height  = crop_height -1
        i,l = 0,0
        for i in range(img.shape[1]):
            s=0;
            for s in range(scale):
                img_out[img_out.shape[0]-1, l+s] = img [img.shape[0]-1,i]
            l =l+s

    l,k = 0,0
    i,j = 0,0
    for i in range(crop_width):
        j =0; k =0
        for j in range(crop_height):
            for s1 in range(scale):
                s2 =0
                for s2 in range(scale):
                    img_out[l+s1,k+s2] = img[i,j]
            k = k+scale
        l = l+scale

    return img_out


#Main function

if __name__=="__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="Path to input image", required=True)
    ap.add_argument("-p", "--pivot-point", help="Pivot point coordinates x, y separated by comma (,)", required=True)
    ap.add_argument("-s", "--scale", help="Scale to zoom", type=int, required=True)
    args = vars(ap.parse_args())

    image_path = args["image"]
    x, y = map(int, args["pivot_point"].split(","))
    scale = args["scale"]

    image = cv2.imread(image_path)
    img = image
    print(image.shape)

    x_coord = x
    y_coord = y
    scale = scale

    width_orig = img.shape[0]
    height_orig = img.shape[1]
    print(img.shape)

    final_img=region(image_path,x_coord,y_coord,scale)
    final_img2 = zoom(final_img, width_orig, height_orig, scale)
    print(img.shape, final_img2.shape)

    cv2.imshow('Original',img)
    cv2.imshow('Final',final_img)
   # cv2.imshow('Final image',final)

    cv2.imwrite('zoom_img.jpg',final_img)
    cv2.imwrite('zoom_img2.jpg',final_img2)
    cv2.waitKey(20)
cv2.destroyAllWindows()

