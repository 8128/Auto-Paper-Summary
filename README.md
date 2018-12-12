Automatic Paper Summary
================
The goal of this project is to create a system which generates a short and accurate summary from longer text. We constructed a user friendly website for usage at the following link.
```bash
http://34.221.113.97:8000/
```
Short text summary is designed to generate a summary within a length of three thousands words. For anything longer than three thousand words, user can upload a .txt file. Short text and Long text examples are provided for trials. 

The results could differ under different methods and ratio. The ratio of the content could be higher using short text summary, thus more comprehensive. For long text summary, the ratio of content could be slighter, thus more tough to understand the whole article. 

Usage
================

Project Sprint
================


Challenges
================
**Dataset Selection**

  * Finding appropriate datasets was a very tough task. The biggest reason was because not many existed or similar experiments before
  * First stage of project was using Document Understanding Conference(DUC) 2003 and 2004 dataset. This dataset doesn't actually contain the summaries we could use to train our model. It also has bizarre instructions on the usage. Therefore, we moved on to the next selection. 
  * Next stage of project was using NIST 2015 dataset from Kaggle. This dataset contains summarized text that can train the model which is the most fitted dataset we've found so far. 

**Training Model**

  * Most of the datasets contain equations, graphs, pictures and charts. It’s hard to train the model for pure text summarization. We've tried a serveral ways to optimize this problem but garbled summaries were inevitable.
  
**Word Embedding**

  * Since we were using seq2seq method to create abstract summary but some terms in datasets are very rare. The model is hard to relate or recognize the words to form an accurate summary. 




We want to build a auto-paper-summary based on LSTM.

For the dataset part, we have two candidates. The first one is DUC 2003 and 2004 dataset. The second one is NIST 2015 dataset. Both of those two have great reputation. However, DUC dataset contains lots of unnecessary massages so we prefer NIST 2015 dataset for now.

First, we turn word into vectors which the computer should recognize. Second, we use the method of LSTM to train our label and vectors. This give us our model. Then, we turn the paper from the user into vectors and use it as the input of our model, we should get output vectors. At last, we turn the output vectors into words and print out the summary we make. 

For the website building part, we want to use Django based on Python. User can input a paper on our website and we are able to give them a summarization directly. For now, we prefer the default database sqlite3. If it fails to fulfill our needs, we would try MySQL.
