Question 1:

a. we first converted all the male and female strings to integers of 1 and 0 using train.replace({'Sex':{'male':1,'female':0}}) to be able to be used by the correlation function through train_s['Survived'].corr(train_s['Sex']) which gave us a value of -0.54335 which makes sex an important feature to determine survival rate

b. to visualze first we had to convert the data from string to integers to be able to represent them on a bar graph then using those values we are able to plot the bar graph using  df_sur.plot(kind='bar', stacked=True, figsize=(8, 5),title="Survived/Not survived by gender") according to the people who survived or didn't according to the sex. Similarly for the second graph we converted the data of passenger class who survived or not then plotted it using df_class.plot(kind='bar', stacked=True, figsize=(8, 5),title="Survived/Not survived by Class")

c. First we cleaned our test and train data, then removed the 3 columns name, ticket, cabin we then filled all the empty values in the embarked column with the value "S" to not allow any inaccuracy when mapping the values. In that dataset, we converted the female and male values to 0 and 1 respectivaly and also for Embarked, convered S, C, Q to 0, 1, 2 and depending on the Fare we assign a value that represents the ammount from 1 to 6. then set the type of fare varible to int. We dropped the columns SibSp, Parch and Age. Then performed the SVM method to report the accuracy after creatting the X_train, Y_train, X_test.

Using SVC() we called the function and used svc.fit for X_train on Y_train then svc predict to predict the accuracy. Followed by generating the SVM confusion matrix.

d. similary like the SVC() method we performed the gaussain by calling GaussianNB() then fitting the on the X_train, Y_train then predicting the accuracy, next we did the same steps but calling a different function BernoulliNB() for bernoulli and MultinomialNB() for multinomial. After each predication we create the coonfusion matric using confusion_matrix(Y_train, Y_pred) from the result we get a step earlier then using sns.heatmap(cmat, cmap='Set3', annot=True, fmt = '4.0f') we draw the heat map.

e. similarly for KN, we call KNeighborsClassifier(n_neighbors=5) and pass the number of neighbors as parameter, in this case it in 5. Then fit and predict the accuracy then draw the confusion matrix.


Question 2:

1. we imported the sklearn dataset to apply the SVM, Naive Bayes, KNN methods on. we first explored the data set then printed one of the imagres using plt.imshow(digits.images[0], cmap='binary') then we created the features and target arrays using X, y = digits.data, digits.target followed by splitting the train and test set using train_test_split(). We then applied the method similary like the questions above, use call the function, SVC(), GaussianNB(), BernoulliNB(), KNeighborsClassifier(). 

2. we loaded the optdigits.tes from the dataset using ds_test = pd.read_csv('./optdigits.tes')

3. using d = X[13] we selected which image we wanted and then shaped the image d.shape = (8, 8) and then selected how we want to draw it using plt.imshow(d,cmap='binary') we got the number 9 and then we did the same thing d = X[54] which gave us a 0

4. we used the train_test_split for the X_train, X_test, y_train, y_test to split the dataset into train and test as text size = 20.

5. After using each methods predict function such as (svc.predict(X_test), gaussian.predict(X_test), bernoulli.predict(X_test), knn.predict(X_test)) and storing the prediction accuracy in the y_pred we then used the classification_report(y_test, y_pred) to obtain a full classification report for each of the methods used. 

6. using plt.imshow(digits.images[555], cmap='binary') we printed the image which gave us a 9 then using img = digits.images[555].reshape(1,-1) we printed the array as and 8*8 array. Then using the knn.predict(img) we can visualize its own class which turned out the be array([9])

7. Finally using the KNN algorithim we used the KNeighborsClassifier(n_neighbors=n) to specify the range of neighbors we want to test, we used the range from 1 to 10 and then fitted the X_train and y_train for each of those ranges, the final result showed that 1 is the value that give good results.
