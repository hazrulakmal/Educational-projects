## Natural language processing (NLP)

Natural language processing (NLP) concerns about the interactions between computers and human language, in particular how to program computers to process and analyse large amounts of natural language data. For this project, we are only concerned about the "processing" part. Essentially we want to do the following:

1. Filter out the stop words like `a`, `is`, etc
2. Normalise the terms. For example, we want to treat the term `begin`, `begins`, `beginning` to be the same so that the user should get the same result if he/she searches with the word `begin`, `begins` or `beginning`. This can be done by either [stemming](https://en.wikipedia.org/wiki/Stemming) or [lemmatisation](https://en.wikipedia.org/wiki/Lemmatisation), but in this project we only consider stemming.

Stemming aims to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. It is done by reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form. For example, after stemming, the word `reveals` becomes `reveal`, `astonishing` becomes `astonish`, `grappling` becomes `grappl`, `addition` becomes `addict`.

For the description of `"The Queen's Gambit"` (with stop words and punctuations already removed), stemming will convert the description from

```
1950s orphanage young girl reveals astonishing talent chess begins unlikely journey stardom grappling addiction
```
to something like:
```
1950 orphanag young girl reveal astonish talent chess begin unlik journey stardom grappl addict
```

---

## NLP with `NLTK` package

We will use the `Python` package `NLTK` do both stop words filtering and stemming.

[NLTK](https://www.nltk.org) is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language. You need to install it (instruction [here](https://anaconda.org/anaconda/nltk). If that does not work, please try [this](https://www.nltk.org/install.html) instead) and run the following lines after installation:

```
import nltk
nltk.download('popular')
```

in Python before you can use it. If you have any problem with the installation, feel free to contact the lecturer.

You will need to figure out how to use `NLTK` and for this part you can google as much as you want. You may find the following functionality/data from `NLTK` useful:

* `nltk.stem.porter.PorterStemmer` or `nltk.stem.SnowballStemmer`: for the stemming part. Feel free to user other stemmers available in NLTK
* `nltk.corpus.stopwords`: return the a list of stop words

You can also do tokenisation and punctuation removal with NLTK as well with the following functionality from `NLTK`:

* `nltk.word_tokenize`: break a sentence to words. You can see the example usage [here](https://www.nltk.org)
* `nltk.tokenize.RegexpTokenizer`: for tokenising the words, but also provides you ways to remove the punctuations

Note that previously in this course, we have done the tokenisation and punctuation removal with the use of `split()` and `strip()`. Both ways are fine for this project.
