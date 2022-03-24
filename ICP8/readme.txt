Brief Discription


1. using the code already given we began to answer each question.

a. to add more dense layers we used the function model.add(layers.Dense(128, activation='relu')) which contains the value 128
which is a multiple of 8, so as we increase layers thier values will increase as such 256, 512...

b. I recreated the model so that it wouldnt have to fit twice which will affect the data of the accuracy and loss and then added
the validation_data=(X_test, Y_test) inside the model.fit method as such nn_fitted = model.fit(X_train, Y_train,
epochs=100, validation_data=(X_test, Y_test), shuffle=True) which will create a new set of validation data which can be used
later on to evalute the accuracy and the loss.

c. next we plot the accuracy using the plt.plot(nn_fitted.history['accuracy']) which will display the accuracy in the grap and 
then also using plt.plot(nn_fitted.history['val_accuracy']) which will display its val. 

d. Similary for the loss we used this to plot the loss plt.plot(nn_fitted.history['loss']) and then used this function 
plt.plot(nn_fitted.history['val_loss']) val of the loss. We then evaluated the model on the x test and y test to print the scores of the loss.

e. after normalizing previously using the sc = StandardScaler() and scaled_data = sc.fit_transform(dataset). the scaled_data 
object contained the normalized data set which was then used to create the new X_train, X_test, Y_train, Y_test using this 
method train_test_split(scaled_data[:,0:8], scaled_data[:,8], test_size=0.25, random_state=42). Then we evaluated the model
using the x test and y test and got the new test scores of the loss.

2.

a. similarly to question 1 we reused the code that was given with the ICP however for this data set for breast cancer required some 
cleaning before it can be used to evaluate and test. So first we needed to drop the id column, then we droped the unnamed column 
which were not needed and the unnamed data is not labeled so didnt provide any significance. they were dropped using dataset.drop('id') 
and dataset.drop('Unnamed: 32') functions. Next we split had to create our X dataset that contained all the columns except the last one 
and the y dataset that contained the last column. then ran the code to be completed by the already given code. we added more dense layers 
using the function model.add(layers.Dense(128, activation='relu')) which contains the value 128

b. I recreated the model so that it wouldnt have to fit twice which will affect the data of the accuracy and loss and then added 
the validation_data=(X_test, Y_test) inside the model.fit method as such nn_fitted = model.fit(X_train, Y_train,
epochs=100, validation_data=(X_test, Y_test), shuffle=True) which will create a new set of validation data which can be used
later on to evalute the accuracy and the loss.

c. similarly to question one we plotted the accuracy and val

d. similarly to question one we plotted the loss and val then printed the evaluation score.

e. Finally we used the sc = StandardScaler() and scaled_data = sc.fit_transform(dataset) to store the scaled data in 
scaled_data and then created a new X_train, X_test, Y_train, Y_test the same way we did in question 1 then evaluated the model and printed the score.


https://youtu.be/zFzzW2Jp4us

https://github.com/UMKC-APL-PythonDeepLearing/icp_8-MoAbboud
