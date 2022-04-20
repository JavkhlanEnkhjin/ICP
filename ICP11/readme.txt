
```
Video Link: https://youtu.be/6pZhPci5tzk
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
```

To start we mounted google drive to allow us to get the dataframe which was too big to be stored in collab. We created the df using 
df = pd.read_csv. To drop the unsup label we used df.drop(df[df['label']=='unsup'].index, inplace = True) next we need to perform 
word tokenization df['review'].apply(word_tokenize) and to remove lower case words df['review'].apply(lambda words: [x.lower() for x in words]) 
then to remove punctuation we used df['review'].apply(lambda words: [x for x in words if not x in punctuation]) We stored the review 
values in sentences using df['review'].values and the labels in y using df['label'].values.

Next we tokenized the text using the given code, then we converted the text to a matrix of 0s and 1s using tokenizer.texts_to_matrix(sentences) 
we checked the shape to make sure that we are working with the right shape. Next we used the preprocessing.LabelEncoder() given then used it 
to fit transform the label values using le.fit_transform(y). We split the data to train and test using 25% of the data as test. Errors found 
when running the given model: Adjusted the input dimension to be similar to the shape of the train and test data. Changing optimizer to 
sigmoid since we only need to classify 2 classes. Using binary_crossentropy since we only have pos and neg reviews to classify.

We created the sequential model and modified the given model to remove the errors stated above. We used input_dim=2000 to match the shape of 
the X_train data. and converted the activation of the output layer to sigmoid. We then compiled the model using the binary croessentropy. We 
fitted the model and got an accuracy of 0.87.

To create the embedded layer we repeated some steps from the previous model but added 2 new variabls, one to get the longest review in the 
dataset max_review and another for the vocab size. This time we used tokenizer.texts_to_sequences(sentences) to convert the text to sequence.
We padded the sequence using the code that was given and then used the label encoder to fit transform the labels. We split the data and started 
to create the model.

The sequential model will contain an extra layed called the embedding layer that will contain an input dim which is the vocab size, an output 
dim which is 120 and an input length which us the max_review. Then we added an flatten layer, then an output layer containing the sigmoid 
activation and then finally compiled the model using binary crossentropy. We then fit the model and evaluated getting the 0.87

To check if the model is underfitting or overfitting we plotted the loss and validation of the train data. We found out there is underfitting. 
To solve that we created a similar sequential model but changing the output dim in the embedding layer to 20 and then fit and evaluated the 
model showed no major change but after plotting the loss we noticed an improvement in underfitting.

For the 20_news group we created the dataset using twenty_train=fetch_20newsgroups(subset='train',shuffle=True) then repeated some of the steps 
used for the previous questions. We tokenized the text then converted the text to sequence and then padded the sequesnces to the same length. 
Finally we predited the padded value on the new model and got 0 which is neg.

For the bonus part we added a 1D conv layer model.add(Conv1D(64, (3), activation='relu')) and a MaxPooling1D layer model.add(MaxPooling1D(2))
which we then flattened and used sigmoidd activation then compiled using the binary crossentropy. We fitted and evaluated the model to get 0.88



```