def load_sample_movies(catalog):
    """
    Populate the catalog with sample movies.
    In a real system this would read from a CSV or database.
    """
    movies = [
        # (title,                        genre,       year,  rating)
        ("Inception",                    "Sci-Fi",    2010,  8.8),
        ("Interstellar",                 "Sci-Fi",    2014,  8.6),
        ("The Matrix",                   "Sci-Fi",    1999,  8.7),
        ("Arrival",                      "Sci-Fi",    2016,  7.9),
        ("Dune",                         "Sci-Fi",    2021,  8.0),
        ("The Dark Knight",              "Action",    2008,  9.0),
        ("Mad Max: Fury Road",           "Action",    2015,  8.1),
        ("John Wick",                    "Action",    2014,  7.4),
        ("Top Gun: Maverick",            "Action",    2022,  8.3),
        ("Mission Impossible",           "Action",    1996,  7.1),
        ("The Shawshank Redemption",     "Drama",     1994,  9.3),
        ("Forrest Gump",                 "Drama",     1994,  8.8),
        ("The Godfather",                "Drama",     1972,  9.2),
        ("Schindler's List",             "Drama",     1993,  8.9),
        ("Parasite",                     "Drama",     2019,  8.5),
        ("Get Out",                      "Horror",    2017,  7.7),
        ("A Quiet Place",                "Horror",    2018,  7.5),
        ("Hereditary",                   "Horror",    2018,  7.3),
        ("The Conjuring",                "Horror",    2013,  7.5),
        ("It",                           "Horror",    2017,  7.3),
        ("The Grand Budapest Hotel",     "Comedy",    2014,  8.1),
        ("Superbad",                     "Comedy",    2007,  7.6),
        ("Knives Out",                   "Comedy",    2019,  7.9),
        ("The Princess Bride",           "Comedy",    1987,  8.0),
        ("Crazy Rich Asians",            "Comedy",    2018,  6.9),
        ("Avengers: Endgame",            "Adventure", 2019,  8.4),
        ("The Lion King",                "Adventure", 1994,  8.5),
        ("Jurassic Park",                "Adventure", 1993,  8.1),
        ("Indiana Jones",                "Adventure", 1981,  8.4),
        ("Up",                           "Adventure", 2009,  8.2),
    ]

    for title, genre, year, rating in movies:
        catalog.add_movie(title, genre, year, rating)
