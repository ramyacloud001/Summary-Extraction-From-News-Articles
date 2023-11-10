from flask import Flask,request,render_template
import numpy as np
import re
import nltk
nltk.download("punkt")
import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS
stopwords = list(STOP_WORDS)
nlp1 = spacy.load('en_core_web_sm')
import string
from string import punctuation
punctuation = punctuation + '\n'
from heapq import nlargest
app = Flask(__name__)
from newspaper import Article
@app.route('/')
def fun1():
    return render_template('index.html')


@app.route('/predict',methods = ['GET','POST'])
def fun2():
    if request.method == 'POST':
        text = request.form["message"]
        d = text
        reg = Article(d)
        reg.download()
        reg.parse()
        reg.download('punkt')
        reg.nlp()
        text = reg.text
        doc = nlp1(text)
        word_frequencies = {}
        for i in doc:
            if i.text.lower() not in stopwords:
                if i.text.lower() not in punctuation:
                    if i.text not in word_frequencies.keys():
                        word_frequencies[i.text] = 1
                    else:
                        word_frequencies[i.text] += 1
        max_frequency = max(word_frequencies.values())
        for j in word_frequencies.keys():
            word_frequencies[j] = word_frequencies[j] / max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
        select_length = int(len(sentence_tokens) * 0.3)
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary_main = ' '.join(final_summary)
        review = re.sub('http\S+\s*', ' ', summary_main)  # remove URLs
        review = re.sub('RT|cc', '', review)  # remove RT and cc
        review = re.sub('#\S+', ' ', review)  # remove hashtags
        review = re.sub('@\S+', ' ', review)  # remove mentions
        review = re.sub('[%s]' % re.escape("""!"#%&'()*+,/;<=>?@[\]^_`-{|}—~”“"""), '', review)  # remove punctuations
        # review = re.sub(r'[^\x00-\x7f]',r' ', review)
        review = re.sub('\s+', ' ', review)  # remove extra whitespace
        # review = review.lower()
        review = review.split()
        # review = [lemma.lemmatize(word) for word in review if not word in stopwords.words("english")]
        review = ' '.join(review)
        if review == '':
            return render_template("index.html",prediction_text = "Not Enough data to Extract Summary from the URL .Check With Another Article URL")
        else:
            return render_template("index.html",prediction_text = review)


if __name__ == '__main__':
    app.run(debug=True)