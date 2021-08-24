class Show:
    
    id_ecounter = 0
    def __init__(self, title, show_type, cast, year_added, rating, duration, description):
        '''     
        Parameters
        ----------
        title : str
            title of the show
        show_type : str
            whether the show is a TV show or a movie
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
        self._id = Show.id_ecounter
        self._title = title
        self._type = show_type
        self._cast = cast
        self._year = year_added
        self._rating = rating
        self._duration = duration
        self._description = description
        Show.id_ecounter += 1
        
    def get_id(self):
        '''
        return the unique id of the show (int)
        '''
        return self._id

    def get_title(self):
        '''
        return the title of the show (string)
        '''
        return self._title
    
    def get_cast(self):
        '''
        return the cast of the show (string)
        '''
        return self._cast

    def get_show_type(self):
        '''
        return the show type like TV show or Movie (string)
        '''
        return self._type
    
    def get_year_added(self):
        '''
        return the year the show is added (int)
        '''
        return self._year

    def get_rating(self):
        '''
        return the parental guidelines rating (string)
        '''
        return self._rating

    def get_duration(self):
        '''
        return the duration description (string)
        '''
        return self._duration

    def get_description(self):
        '''
        return the description of the show (string)
        '''
        return self._description
    
    def __str__(self):
        return f"ID: {self._id} Title: {self._title} Show Type: {self._type} Year: {self._year} Raiting: {self._rating} Duration: {self._duration} Description: {self._description}"
