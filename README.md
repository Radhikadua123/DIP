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
 Input image <br />
 ![Input](./results/original.png)  <br />
 
 Output  <br />
 ![Output](./results/zoom.png)
 
 ### Execution
 To execute the code to zoom an image with given pivot coordinates and scale, run the following command:
 
python zooom.py  -i "Image_path" -p x,y -s 2
