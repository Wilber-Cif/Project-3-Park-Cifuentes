from bst import MovieBST


class Catalog:
    """
    The central movie catalog.

    Two data structures work together:
      1. BST  (bst.py)   — stores every movie, searchable by title in O(log n)
      2. dict (hash map) — maps genre → list of movies, for O(1) genre lookup

    Having both avoids a slow O(n) scan of the entire tree every time a user
    browses by genre.
    """

    def __init__(self):
        self.bst = MovieBST()                  # non-linear: for title search
        self.genre_map = {}                    # linear (hash map): genre index

    # ------------------------------------------------------------------- add
    def add_movie(self, title, genre, year, rating):
        """
        Add a movie to both the BST and the genre hash map.
        Returns True on success, False if the title already exists.
        """
        inserted = self.bst.insert(title, genre, year, rating)
        if not inserted:
            return False  # duplicate

        genre_key = genre.lower()
        if genre_key not in self.genre_map:
            self.genre_map[genre_key] = []
        # Store the actual node so both structures share the same object
        node = self.bst.search(title)
        self.genre_map[genre_key].append(node)
        return True

    # --------------------------------------------------------------- search
    def search_title(self, title):
        """Exact title search via BST — O(log n)."""
        return self.bst.search(title)

    def search_prefix(self, prefix):
        """Partial title search — returns all matching MovieNodes."""
        return self.bst.search_by_prefix(prefix)

    # --------------------------------------------------------- browse genre
    def browse_genre(self, genre):
        """
        Return all movies in a genre — O(1) hash map lookup.
        Returns an empty list if the genre doesn't exist.
        """
        return self.genre_map.get(genre.lower(), [])

    def list_genres(self):
        """Return a sorted list of all available genres."""
        return sorted(self.genre_map.keys())

    # ---------------------------------------------------------- all movies
    def get_all_movies(self):
        """Return every movie sorted A–Z (BST in-order traversal)."""
        return self.bst.get_all_sorted()

    # --------------------------------------------------------- recommend
    def recommend(self, genre, exclude_title=None, top_n=5):
        """
        Simple recommendation: return top-rated movies in the same genre,
        excluding a movie the user just watched.
        Time complexity: O(k log k) where k = movies in that genre.
        """
        candidates = self.browse_genre(genre)
        candidates = [m for m in candidates
                      if exclude_title is None
                      or m.title.lower() != exclude_title.lower()]
        # Sort by rating descending
        candidates.sort(key=lambda m: m.rating, reverse=True)
        return candidates[:top_n]

    def is_empty(self):
        return self.bst.is_empty()
