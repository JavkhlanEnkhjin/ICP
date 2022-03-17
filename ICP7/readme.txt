
1.

a. To start we initialized the TfidfVectorizer using the TfidfVectorizer() method after that we fit_transform the twenty_train.data to convert them to data points 
and then store them in X_train_tfidf. Which is train data. We initialized the SVC() method and then fit the train data with the twent_train.target. 
After that we create the twenty_test data which contains the test data and then transform the twenty_test.data using the TfidfVectorizer() variable 
and store them in X_test_tfidf. Next we predict the X_test_tfidf and store it into the predicted variable. Finally we calculate the score using the 
metrics.accuracy_score() using the twent_test.target and predicted variables. In order to print the classification report with the names of the classes, 
we extract the target names from the twenty train and then pass them in the parameter of the classification_report method 
classification_report(twenty_test.target, predicted, target_names = classes)

The score for SVC is 0.81864

b. Similarly for B, we use the exact same steps but intead of initializing the SVM algorithm we used the KNeighborsClassfier 
method KNeighborsClassifier(n_neighbors=5) we intialize KNN with 5 as the number of neighbors and follow the exact same steps done in a.

The score for KNN is 0.65918

c. Same steps as b but we initialized the TfidfVectorizer using TfidfVectorizer(ngram_range=(1,2)) to use bigram. 
and then continue the same steps in b.

The score while using the bigram is 0.619622

d. Same steps as b but we initialized the TfidfVectorizer using TfidfVectorizer(stop_words = 'english') to use stop_words = 'english'. 
and then continue the same steps in b.

The score while using stop_words = 'english' is 0.67578

2. Before we begin we will need to import most of the nltk packages that can be used in order to get the icp completed, including
beatiful soup and requests. After that we download the nltk packages using nltk.download().

We being by requesting the url using requests.get("https://www.storynory.com/fox-and-the-crow/"). After that we store the 
html content into a soup object using the BeautifulSoup(response.content, "html.parser") method. We printed the title and 
searched in the soup varible for all the paragraph tags in it <p> using find_all. Then we store them all in a paragraphs list.

We first started with sentence tokenize, and sentence tokenized the first paragraph in the list using sent_tokenize(paragraphs[0]) 
which will split the paragraphs to sentences in a list then we do the same thing to word tokenize using word_tokenize(paragraphs[0]) 
which will split the paragraphs into words in a list.

Next for the Part of Speech part  we used the nltk.pos_tag(w_tokens) method and passed it the words tokens inorder to 
label them according to their part of speech tagging. Which will place either NNP, CC, or JJ next to each word.

After that we have the stemming and lemmatization. First we initialized the LancasterStemmer variable using the LancasterStemmer() 
and then for every word token we have we used the Stemmer.stem(i) to stem the value and then print the output. Similarly for 
Lemmatization we initialized the WordNetLemmatizer variable using the WordNetLemmatizer() and using a for loop we 
iterated over each word token and used Lemmatizer.lemmatize(i) to lemmatize the word the print it.

Next we have the trigram where we loop around all the word tokens and printed only 3 varibale on each line to creat the bigram 
and wrapping the print statment with a try catch exception to make sure it don't return an error at the last 3 values.

Next for the Named Entity Recognition we used the method nltk.ne_chunk(nltk.pos_tag(nltk.wordpunct_tokenize(paragraphs[0]))) 
which will tokenize the paragraph and then part of speech tag the tokenizes values and then ne_chunk to locate and classify 
elements in text into pre-definded categories.

Finally, we set the stop words to english using stop_words = set(stopwords.words('english')) and then iterated over the words 
tokens in the paragraph to remove the stopwords. We then appended the variables that are not stop words into a list which we 
passed to the Counter method that will count the occurance of each words and then create a dataframe out of it using 
pandas.DataFrame.from_dict(freq, orient='index') and finally plotting the freqency after removing stop words bar graph 
using paragraphdf.plot(kind='bar')
