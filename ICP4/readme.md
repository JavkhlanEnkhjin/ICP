Write brief explanation here:

we first imported the numpy lib. using np.random.randint(1,20,15) we were able to create an array of length 15 and contains random numbers in between the range from 1 to 20. Then using the reshape(3,5) we set the shape of the array to contain 3 rows and 5 columns. Next we found the max value of each row using the .max(axis=1) using np.where() we set the condition which was so check if the values of vector_shape[0] equal to one of the values in maxRow[0] if true we swap the value at vector_shape[0] with 0. We did the same for the next 2 rows using the vector_shape[1] and vector_shape[2] comparing them with the maxRow[1] and maxRow[2] respectively. Finally we use the np.diag(vector_shape) function to extract the diagonal from the array then using np.savetxt("diag.npy",d) to save the diagonal in an npy file.

we first imported pandas lib, to read the csv we use the pd.read_csv('data.csv') function to read the file. We then printed the data frame.Using df.describe() we printed the basic statistical description. To replace the null values with the mean we used the df.fillna() function and passed it the df.mean() function which represents the mean.

The two columns selected were Pulse and Maxpulse and aggregated the data using the .agg(['min','max','count','mean']) function. We used df[ (df['Calories'] > 500) & (df['Calories'] < 1000)] to filter the values between 500 and 1000 calories and then we used df[ (df['Calories'] > 500) & (df['Pulse'] < 100)] to filter values over 500 calories but less than 100 pulse.

we created the df_modified using df_modified = pd.DataFrame(df, columns=['Duration', 'Pulse', 'Calories']) and passing it the first data frame with the columns that we want to include in the new data frame which were only duration, pulse, and calories without the Max pulse. we then dropped maxpulse from the main data frame using df.drop. Then we converted the calories datatype to int using .astype(int) after which we generated the scatter plot of the data frame for the duration and calories using df.plot.scatter(x='Duration', y='Calories')

Using matplotlib, we were able to crop the image, using the pimg.imread and inserting the image path, we were able to show the image in the console using imshow and then printing the image.shape.

After printing we converted the image to an array in order to crop the image. we then used image[##:## , ##:## , :] the first colon represents the height in pixels and the second colon is used for the width in pixels. Adjusting both allowed us to perfectly crop the UMKC logo from the image. Then we printed the cropped image shape using the img_cropped.shape then imshow to show the image. Finally for the image cropping task we saved the file using savefig() and giving the name of the image as parameter.

For the second part, we selected 2 samples on the exsisting image to acquire the RGB scale of the 2 colors that we want to keep in the image. the first sample coordinates were image_arr[150:151, 50:51] for white and the second image_arr[50:51, 300:301] for yellow. using np.where we created a condition if the pixel is not equal to the first or second sample, it will be converted to 0 else it will remain the same. Meaning that any pixel that is not white or yellow will change to black. We displayed the image using .imshow() and then saved it using imsave(Path, np_whereImg).


https://github.com/UMKC-APL-PythonDeepLearing/icp_4-JavkhlanEnkhjin
https://github.com/UMKC-APL-PythonDeepLearing/icp_4-MoAbboud
https://youtu.be/aFKBzNKmNK0
