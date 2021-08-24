from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords 
import nltk

def clean_sentences(sentences):
    '''
    
    Parameters
    ----------
    sentences : str
        a sentence to be filtered. the function will change all words into their root form and also remove all stop words.

    Raises
    ------
    TypeError
        when other than string type is given
    Returns
    -------
    filtered_sentence : list
        a list of filtered root words.

    '''
    try:
        if not isinstance(sentences, str):
            raise TypeError
        stemmer = SnowballStemmer("english")
        stop_words = set(stopwords.words('english')) 
        tokenizer = nltk.RegexpTokenizer(r"\w+") 
        sentences = sentences.lower()
        filtered_sentence = tokenizer.tokenize(sentences)
        filtered_sentence  = [stemmer.stem(new_word) for new_word in filtered_sentence]
        filtered_sentence = [word for word in filtered_sentence if not word in stop_words] 
    except TypeError:
        print(f'string type is expected but {type(sentences)} is given.')
    return filtered_sentence 
        
    
    