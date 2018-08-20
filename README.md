# Digital image processing

## Zooming of images
Code to implement zooming of images using Python and OpenCV.

### Input
* Path of the image.
* Pivot point coordinates ( x coordinate, y coordinate)
* Scale 

 ### Output
 A  zoomed image of the same size as the input image.
 
 ### Example
 #### Input
 Pivot point (x, y): (133, 72)  <br />
 Scale: 2   <br />
 Input image                                       
 ![Input](./results/original.png)                  
 
Output  <br />
 ![Output](./results/zoom.png)
 
 ### Execution
 To execute the code to zoom an image with given pivot coordinates and scale, run the following command:
 
python zooom.py  -i "Image_path" -p x,y -s 2

### Algorithm
1. Read input image <br />
2. Crop the region of interest around the pivot point (where to zoom) and scale as
parameters.<br / >
    * Get the width and height of original image. <br />
    * New width = width / scale; New height = height/ scale <br />
    * x_Top left of cropped image= x_Top left of original image + New width/2, 
      y_Top left of cropped image= y_Top left of original image + New height/2 <br />
    * The cropped image is the region of interest. <br />
3. Zoom the image by replicating the pixel values. <br />
   Replication method pseudocode: <br />
   * Take the pixel of the image <br />
   * For i in range(scale): <br />
     i. Copy the pixel value row wise <br />
    ii. Copy the pixel value column wise <br />
   iii. Copy the pixel value diagonal wise <br />
   
### Results

 ![Input](./results/original4.jpeg) ![](./results/zoom4jpg) <br />
 ![Input](./results/original5.jpeg) ![](./results/zoom5.jpg) <br />
 ![Input](./results/original6.jpeg) ![](./results/zoom6.jpg) <br />
 ![Input](./results/original2.png) ![](./results/zoom2jpg) <br />
 
 
   
   
   *
