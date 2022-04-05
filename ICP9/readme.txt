
Name: Mohamad Abboud
Email: Maadz9@umsystem.edu

https://github.com/UMKC-APL-PythonDeepLearing/icp_9-MoAbboud


https://youtu.be/oUgplC7efbw

Q1.

1. We changed the model by adding 2 new layers using these lines of code by modifying the first line model.add(Dense(64, activation='elu', input_shape=(dimData,))) 
and added the model.add(Dense(128, activation='elu')) and model.add(Dense(256, activation='elu')) as a result we changed the number of layers which 
as a result increased the accuracy and decreased the loss of the model. Moreover, the activation was changed to elu since elus have a negative value 
which allows them to push mean unit activations closer to zero.

Before adding and changing layers: Loss = 1.769, accuracy = 0.420

After adding layers: Loss = 0.130, accuracy = 0.976

Modifying the layers reflected a significant improvement in accuracy.

2. Using the history object, we were able to point to the history value for accuracy using history.history['accuracy'] and then we plotted the
acurracy and the value accuracy using plt.plot(history.history['accuracy']) and plt.plot(history.history['val_accuracy']) and then plotted the loss 
using plt.plot(history.history['loss']) and plt.plot(history.history['val_loss']) to display the plots.

3. To rerun the code on non normalized or non scaled data, i used the same code that was given for the icp and ran it again while commenting 
#train_data = train_data /255.0 and #test_data = test_data /255.0 as a result our data is now not scaled. We then ran the same model again with
the 2 added layers and obtained a new accuracy and loss. Which was extremely minor compared the normalized and scaled model that was ran in part b.

Minor change without unscaling the images: Loss = 0.472, accuracy = 0.955

4. To convert the model from a sequential to a functional model, we have to create a new model. We first initialize an input layer that will contains 
the dimData as shape, then we start creating the hidden layers as muchs as needed with activation elu. Each hidden layer will take the layer created 
before it as input hidden_layer=Dense(512, activation='elu')(hidden_layer) so they are all connected. Finally for the output layer it take the last
hidden layer as input and has the activation of softmax. Then the model is created using this function Model(inputs= input_layer, outputs=output_layer),
then compiled then fitted. We received an evaluation accuarcy of 0.97 and loss of 0.11

5. We selected a random image to plot using plt.imshow(test_images[3,:,:],cmap='gray') then predicted the image using the model model.predict(test_data[[3],:])
 and then used the numpy function np.argmax(predict,axis=1) to predict the class to classify the image and the model classified the image correctly.

Q2.

1. The error that we got was:
 "'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits'
logits and labels must have the same first dimension, got logits shape [256,10] and labels shape [2560]"

Since our target needs to be a 1D integer encoded target. in the given code we were changing the labels from interger to one hot encoding which 
was causing the problem. We replaced the code that was used for train_labels_one_hot and test_labels_one_hot with train_labels and test_labels. 
So we commented out the lines of code that were responsible for converting the labels from intergers to one hot encoding and in the model.fit 
function we replaced the train_labels_one_hot and test_labels_one_hot with train_labels and test_labels and we got an evaluation acc of 0.97 and 0.13.

2. Finally we repeated the same steps we did for Q1. 5 and plotted the image then predicted the class of the image using the numpy function 
argmax() after predicting the image on our model and it predicated the correct class.

