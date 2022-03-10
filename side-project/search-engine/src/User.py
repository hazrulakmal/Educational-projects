from show import Show
from Playlist import Playlist, FavouritePlaylist
from datetime import date

class User:
    '''
    Class should be used alongside Playlist, FavouritePlaylist, Show and StreamingService class
    '''
    def __init__(self, birthday, watch_later, favourite):
        '''
        Users represents users of an streaming service.

        Parameters
        ----------
        birthday : str
            should follow this format "year-month-day". example '2000-3-27'.
        watch_later : Playlist Class

        favourite : FavouritePlaylist Class

        Raises
        ------
        TypeError
           when the given inputs do not follow each type

        Returns
        -------
        None.

        '''
        if not isinstance(birthday, str):
            raise TypeError(f"birthday needs to be a str but {type(birthday)} is given.")
        if not isinstance(watch_later, Playlist) or not isinstance(favourite, FavouritePlaylist):
            raise TypeError(f'watch_later and favourite should be in class type but {type(watch_later), type(favourite)} are given')
            
        self._birthday = tuple(map(int, birthday.split("-")))
        self._history = []
        self._watch_later = watch_later
        self._favourite = favourite
    
    def get_history(self):
        '''
        Returns
        -------
        TYPE list
            A list of movies that have been played

        '''
        return self._history.copy()
    
    def get_watch_later(self):
        '''
        Returns
        -------
        TYPE List
            A list of movie titles in the watch later playlist

        '''
        return self._watch_later.get_data()
    
    def get_favourite(self):
        '''
        Returns
        -------
        TYPE List
            A list of movie titles in the favourite playlist

        '''
        return self._favourite.get_data()
    
    def clear_history(self):
        '''
        delete all the movies in the history list
        '''
        del self._history[:]
          
    def add_watch_later(self, show):
        '''
        add a show to the 'watch later' playlist

        Parameters
        ----------
        show : Show class
            show to add to the playlist

        Raises
        ------
        TypeError
            when the given show is not a type of Show class.

        Returns
        -------
        None.

        '''
        try:
            if not isinstance(show, Show): 
                raise TypeError
            self._watch_later.add_to_playlist(show)
        except TypeError:
            print(f" Input should be Show class, but {type(show)} is given.")
            
    def remove_watch_later(self, show_title):
        '''
        Remove a show corresponding to the given show_title from a 'watch later' playlist

        Parameters
        ----------
        show_title : str
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)

        Returns
        -------
        None.
        '''
        self._watch_later.remove(show_title)
        
    def play_watch_later(self, show_title = None):
        '''
        "play" a show with a given title in the 'watch later' playlist by printing string describing 1. which show was played and 2. the duration of the show. 
         If show_title is not given, the show that has been added to the playlist first will be play

        Parameters
        ----------
        title : str, optional
            Show to play. It has to match the title perfectly (including case, spacing, etc)
            The default is None and the first show added to the playlist will be played.
        '''
        show_played = self._watch_later.play(show_title)
        self._history.append(show_played.get_title())

    def add_favourite(self, show):
        '''
        add a show to the 'favourite' playlist

        Parameters
        ----------
        show : Show class
            show to add to the playlist

        Raises
        ------
        TypeError
            when the given show is not a type of Show class.

        Returns
        -------
        None.

        '''
        try:
            if not isinstance(show, Show): 
                raise TypeError
            self._favourite.add_to_playlist(show)
        except TypeError:
            print(f" Input should be Show class, but {type(show)} is given.")
    
    def remove_favourite(self, show_title):
        '''
        Remove a show corresponding to the given show_title from a 'favourite' playlist

        Parameters
        ----------
        show_title : str
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)

        Returns
        -------
        None.
        '''
        self._favourite.remove(show_title)
        
    def play_favourite(self, show_title = None):
        '''
        "play" a show with a given title from the 'favourite' playlist by printing string describing 1. which show was played and 2. the duration of the show. 
         If show_title is not given, the show that has been added to the playlist first will be play

        Parameters
        ----------
        title : str, optional
            Show to play. It has to match the title perfectly (including case, spacing, etc)
            The default is None and the first show added to the playlist will be played.
        '''
        show_played = self._favourite.play(show_title)
        if show_played.get_title() in self._watch_later.get_data():
             self._watch_later.remove(show_title)
        self._history.append(show_played.get_title())
        
    def get_age(self):
        '''
        Returns
        -------
        age : int
            the age of the user.
        '''
        today = date.today()
        age = today.year - date(*self._birthday).year
        return age
        





















