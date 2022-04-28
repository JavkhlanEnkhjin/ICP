# Write brief explanation here:

1-

1. For the first and second part we need to import the sentiment dataset that was given with the ICP, also most of the code was given for those 2 parts and were explained in the lecture. We first imported the data and then performed a few preprocessing lines, first to convert all the text to lower case, then to remove punctuation then we removed the rt string from the data. Next we set the max_features to 2000 and after thaat we tokenized the data. Finally we converted the text to sequence after that paded the sequences so that they all become the same size.

2. The keras model was then built by creating a sequential model and then adding a Embedding layer with 128 embedding dimensions. After that we added an LSTM layer with 196 out featurs of lstm. We then added a final dense layer with 3 neurons and softmax activations since there is more than 2 classes to classify from. We compiled the model then performed the labeleconder on the sentiment target column followed by converting the class vector to binary class matrix. We creted the test and train data then set the batch size to 32. We finally fit the model and evaluated it and got an accuracy of 0.65. Then we saved the model so we can use it in the next part.

3. We loaded the previously saved model and created the new text data to test our model from the ICP. We created a new dataframe and performed the same preproccessing techniques performed in the first question while preprocessing the sentiment data. We predicted the text using  result = model.predict(X) and the result showed the correct output which was positive sentiment.

4. Now we need to use the spam data. We created the dataframe and used the 2 important columnsn we want v2 and v1. Similarly to question 1 and 3 we used the same preprocessing data converting to lower case then removing punctions, then tokenizing and converted text to sequences and finally padding the sequence. We created the model similarly to previous steps but the final layer will only contain 2 neurons with sigmoid activation since we have only 2 classes to classify between. We perform label encoding and then fit and evaluate the model.

2-

I used the cats and dogs dataset from kaggle to create a model to use. It contains a test and train model that i imported from my google drive. I used an imagedatagenerator to normalize the images, also similarly for building the training and test data storing them into objects to be used by the model.

Once the test and train were ready I used the resnet50 as the finaly layer using ResNet50( input_shape=(32,32,3), include_top=False). Next we set the layer.trainable to false to freeze the layers. then we created the resnet output and the globalaveragepooling2d layer after that we added the dropout layer and then a couple of dense layers to complete our model, and then added a last dense layer with 1 neuron with sigmoid activation. We created the model then summary and fitted the model to evaluate it.


https://github.com/UMKC-APL-PythonDeepLearing/icp_12-MoAbboud

https://youtu.be/uUD6QDStl0A
