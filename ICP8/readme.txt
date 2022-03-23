Brief Discription


1. using the code already given we began to answer each question.

a. to add more dense layers we used the function model.add(layers.Dense(128, activation='relu')) which contains the value 128
which is a multiple of 8, so as we increase layers thier values will increase as such 256, 512...

b. next we added the validation_data=(X_test, Y_test) inside the model.fit method as such nn_fitted = model.fit(X_train, Y_train,
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

a. similarly to question 1 we reused the code that was given with the ICP however for this data set it required some cleaning
before it can be used to evaluate and test.
