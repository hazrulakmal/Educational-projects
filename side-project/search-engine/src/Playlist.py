import random

class RedundancyError(Exception):
    '''
    error to raise when the same show is to be added to the playlist
    '''
    pass

class Playlist:
    '''
    playlist class has 2 arguments namely playlist name and the max number of movies/series that can be included 
    '''
    def __init__(self, playlist_name, capacity):
        '''
        Parameters
        ----------
        playlist_name : str
            name of the playlist
        capacity : positive int
            maximum number of shows can be stored in the playlist

        Raises
        ------
        TypeError
            when the given capacity is not int
        ValueError
            when the given capacity is not positive

        Returns
        -------
        None.

        '''        
        if not isinstance(capacity, int):
            raise TypeError(f"Capacity needs to be an integer, but {type(capacity)} is given.")
        if capacity <= 0:
            raise ValueError(f"Capacity of the playlist is expected to be a positive integer, but {capacity} is given.")
        self._playlist = playlist_name
        self._capacity = capacity
        self._data = {} # data is stored in dictionary with title as key and instance of show as value
        
    def get_playlist(self):
        return self._playlist
    
    def is_full(self):
        return self._capacity <= len(self._data)
           
    def add_to_playlist(self, instance):
        '''
        Add a new a new show into the playlist

        Parameters
        ----------
        instance : an instance of a show
        
        Raises
        ----------
        TypeError 
            when the given new movies is alredy in the playlist

        '''
        try:  
            if instance.get_title() in self._data:
                raise RedundancyError
            if not self.is_full():
                self._data[instance.get_title()] = instance
            else:
                return print(f'Sorry, playlist is full. {instance.get_title()} is not included')
        except AttributeError:
            pass
        except RedundancyError:
            print(f'sorry, {instance.get_title()} is already in the playlist')
            
    def remove(self, title):
        '''
        Remove a show from the data attribute

        Parameters
        ----------
        title : assume title is a string

        '''
        try: 
            if not isinstance(title, str): 
                raise TypeError
            del self._data[title]
        except KeyError:
            print(f'Error: {title} is not in the playlist. Nothing is removed')
        except TypeError:
            print(f'Error: Expected a string but {type(title)} is given.')
        
    def get_data(self):
        '''
        Returns
        -------
        A list of movies in the playlist
        '''
        return list(self._data)
    
    def play(self, title = None):
        '''
       "play" a show with a given title in the playlist by printing string describing 1. which show was played and 2. the duration of the show. If show_title is not given, the show that has been added to the playlist first will be play

        Parameters
        ----------
        title : str, optional
            Show to play. It has to match the title perfectly (including case, spacing, etc)
            The default is None and the first show added to the playlist will be played.

        Raises
        ------
        IndexError
            when the playlist is empty
        KeyError
            when the given show is not in the playlist
            
        Return
        ------
        show : Show class
        
        '''
        if title is None:
            try:
                title = list(self._data)[0] # first show name in the playlist
            except IndexError:
                raise IndexError("No show is in the playlist.")
        try:
            show = self._data[title]
        except KeyError:
            raise KeyError(f"The show {title} is not in the playlist.")
        del self._data[title]
        print(f"Playing the show {show.get_title()} ({show.get_duration()})")
        return show

            
    def shuffle_play(self):
        try:
            data_copy = self._data.copy()
            tur = list(data_copy.items()) #transform dict items into list of turples so that it can be shuffled
            random.shuffle(tur)
            first_show = tur[0][0] #select the first tuple in the list which is the title of the show
            print(f'playing the show {first_show} ({data_copy[first_show].get_duration()})')
            del self._data[first_show]
        except IndexError:
            raise IndexError("No show is in the playlist.")
                     
    def __len__(self):
        '''
        return the number of shows in the playlist
        '''
        return len(self._data)
    

class FavouritePlaylist(Playlist):
    def __init__(self, playlist_name, capacity):
        Playlist.__init__(self, playlist_name, capacity)
        self._history = []
        
      
    def play(self, title = None):
        '''
       "play" a show with a given title in the playlist by printing string describing 1. which show was played and 2. the duration of the show. If title is not given, the show that has been added to the playlist first will be play
        Different movie will be play for every function called without title.
        Parameters
        ----------
        title : str, optional
            Show to play. It has to match the title perfectly (including case, spacing, etc)
            The default is None and the first show added to the playlist will be played.

        Raises
        ------
        IndexError
            when the playlist is empty
        KeyError
            when the given show is not in the playlist
        
        Return
        ------
        show : Show class
        
        '''
        if len(self._history) == len(self._data):
            del self._history[:] #delete history after all movies in the playlist have been played. After one circle completes, the first movie in list will be play again if title is not given.
        
        if title is None:
            try:
                show = len(self._history)
                title = list(self._data)[show] # if the first favourite movie is already played, a second one in the list will be play and so on
            except IndexError:
                raise IndexError("No show is in the playlist.")   
        try:
            show = self._data[title]
            self._history.append(title)
        except KeyError:
            raise KeyError(f"The show {title} is not in the playlist.")
        print(f"Playing the show {show.get_title()} ({show.get_duration()})")
        return show

    
    
    