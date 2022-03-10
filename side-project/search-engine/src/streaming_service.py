from show import Show
from sentence import clean_sentences
import time
import random

class StreamingService:
    
    def __init__(self, paltform_name, data):
        '''
        Parameters
        ----------
        paltform_name : str
            name of the streaming service
        data : pandas DataFrame
            each row contains the information about title, type, year added, rating, duration, description
            assume show title is unique
        '''
        data_dict = data.set_index('title').T.to_dict('list')
        self._name = paltform_name
        self._show = {}
        self._index = {}
        for each in data_dict:
            self._show[each] = Show(each, *data_dict[each]) #get the list of coresponding details of the movie and unpack them
            for word in clean_sentences(each) + clean_sentences(str(data_dict[each][1])) + clean_sentences(data_dict[each][-1]): 
                if word not in self._index: #if the word does not have inverted index we assign a new index it 
                    self._index[word] = {self._show[each].get_title()}  
                else:
                    word_set = self._index[word] #if the word does have inverted index we update it by adding a new index corresonding to a new movie
                    word_set.add(self._show[each].get_title())
                    self._index[word] = word_set
                
    def get_service(self):
        '''
        return the name of the platform used. example Netflix
        '''
        return self._name
    
    def get_index(self):
        return list(self._index.keys())
    
    def add_show(self, title, show_type, cast, year_added, rating, duration, description):
        '''
        add a show to the streaming service. Assume show title is unique

        Parameters
        ----------
        title : str
            title of the show
        show_type : str
            whether the show is a TV show or a movie
        cast : str
            the characters in the movie
        year_added : int
            the year added to the streaming service
        rating : str
            parental guidelines rating
        duration : str
            length of the movie or the TV show
        description : str
            description of the show

        Returns
        -------
        None.

        '''
        try: 
            if not isinstance(title, str) or not isinstance(show_type, str) or not isinstance(description, str) or not isinstance(cast, str): 
                raise TypeError
            self._show[title] = Show(title, show_type, cast, year_added, rating, duration, description)
            for word in clean_sentences(title) + clean_sentences(cast) + clean_sentences(description): 
                if word not in self._index: #if the word does not have inverted index we assign a new index it 
                    self._index[word] = {title}  
                else:
                    word_set = self._index[word] #if the word does have inverted index then we update it by adding a new index corresonding to a new movie
                    word_set.add(title)
                    self._index[word] = word_set
        except TypeError:
            print('Error: add_show arguments is not the right type')
    
    def get_all_shows(self):
        '''
        Return a list of all shows avalible in the data

        '''
        return list(self._show.keys())
    
    def remove_show(self, show_name):
        '''
        Parameters
        ----------
        show_name : the name of the movie to be remove. Assume the argument in the form of string

        '''
        try: 
            if not isinstance(show_name, str): 
                raise TypeError
            del self._show[show_name]
            print('Successfullly removed')
        except KeyError:
            print(f'Error: The movie does not exist')
        except TypeError:
            print(f'Error: Expected a string but {type(show_name)} is given.')
            
    def get_shows(self):
        '''
        Return a dictionary of all movies with their coresponding discription

        '''
        return self._show
            
    def get_show(self, show_name):
        '''
        Parameters
        ----------
        show_name : string type. the name of the show

        Returns
        -------
        corresponding show details (an instance of Show) if the show is available

        '''
        try:
            if show_name not in self.get_all_shows():
                raise ValueError
            else:
                return self._show[show_name]
        except ValueError:
            print(f'Sorry {show_name} is not available at the moment')
            

    def search(self, words):
        '''
        Parameters
        ----------
        words : str
            input from user. user can enter any word and the search engine will look up for related movies .

        Raises
        ------
        ValueError
            when search engine cant find any related movies corresponding to the word given

        Returns
        -------
        list_movies : list
            a collection of list of Show

        '''

        words_copy = clean_sentences(words)
        try:
            for word in words_copy:
                if word not in self.get_index():
                    raise ValueError
            
            list_movies = []
            if len(words_copy) == 1:
                 related_movies = self._index[words_copy[0]]
            
            elif len(words_copy) == 0:
                raise ValueError
                 
            else:
                one_set = self._index[words_copy[0]] #finding the index location of corresponding to the first word
                other = [self._index[words_copy[x]] for x in range(1, len(words_copy))] #finding the index location corresponding to other words 
                assert len(other) == len(words_copy)-1, 'Some words are not compared'
                related_movies = one_set.intersection(*other)
            for movie in related_movies:
                list_movies.append(self._show[movie])
            return list_movies
        except ValueError:
            print(f'Sorry {words} is not found')    
            
    def experiment(self, num_to_select):
        '''
        a search simulation to measure the actual retrieval time fpr two different search method and calculate the number of irrelevant shows
        Parameters
        ----------
        num_to_select : int
            the number of searches to simulate

        Returns
        -------
        naive_time, smart_time, average : list
            naive time is the actual retrieval time for get_show() method
            smet_time is the acua; retrieval time for search() method
            average is the average number of irrelevant shows
            
        '''
        random_shows = random.sample(self.get_all_shows(), num_to_select)
        start = time.time()
        naive = [self.get_show(x) for x in random_shows]
        mid = time.time()
        smart = [self.search(i) for i in random_shows]
        end = time.time()
        naive_time = mid - start
        smart_time = end - mid
        unwanted_shows = sum( [len(sublist) for sublist in smart if sublist is not None]) - num_to_select
        average = round(unwanted_shows/num_to_select, 2)
        return [naive_time, smart_time, average]
            
    