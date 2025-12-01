class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        print("Комедии:", self.movies)

class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        self.movies.append(movie)
        print("Драмы:", self.movies)

Comedy().add_movie("Большой куш")
Drama().add_movie("Оружейный барон")