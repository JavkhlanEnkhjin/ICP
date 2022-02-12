Write brief explanation here:

1.

using np.random.randint(1,20,15) we were able to create an array of length 15 and contains random numbers in between the range from 1 to 20. Then using the reshape(3,5) we set the shape of the array to contain 3 rows and 5 columns.
Next we found the max value of each row using the .max(axis=1)
using np.where() we set the condition which was so check if the values of vector_shape[0] equal to one of the values in maxRow[0] if true we swap the value at vector_shape[0] with 0. We did the same for the next 2 rows using the vector_shape[1] and vector_shape[2] comparing them with the maxRow[1] and maxRow[2] respectively.
Finally we use the np.diag(vector_shape) function to extract the diagonal from the array then using np.savetxt("diag.npy",d) to save the diagonal in an npy file. 

2.



3.

Using matplotlib, we were able to crop the image, using the pimg.imread and inserting the image path, we were able to show the image in the console using imshow and then printing the image.shape. 

To crop the image we used image[##:## , ##:## , :] the first colon represents the height and the second colon is used for the width. Adjusting both allowed us to perfectly crop the UMKC logo from the image. Then we printed the cropped image shape using the img_cropped.shape then imshow to show the image. Finally for the image cropping task we saved the file using savefig() and giving the name of the image as parameter.
