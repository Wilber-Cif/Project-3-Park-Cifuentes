class WatchlistNode:
    """A single node in the singly linked list."""

    def __init__(self, movie):
        self.movie = movie   # a MovieNode from bst.py
        self.next = None


class Watchlist:
    """
    Singly Linked List — the user's personal watchlist.
    Chosen over an array because:
      - Frequent insertions / deletions at arbitrary positions → O(1) with a pointer
      - No need for random access by index
    Operations:
      - add (append):   O(n) — keeps insertion-order, no duplicates
      - remove:         O(n) — must traverse to find the node
      - display:        O(n)
    """

    def __init__(self):
        self.head = None
        self.size = 0

    # --------------------------------------------------------------------- add
    def add(self, movie):
        """Append a movie to the end of the watchlist. Rejects duplicates."""
        # Check for duplicate
        if self._find(movie.title) is not None:
            return False  # already in watchlist

        new_node = WatchlistNode(movie)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        return True

    # ------------------------------------------------------------------ remove
    def remove(self, title):
        """Remove a movie by title. Returns the MovieNode or None."""
        if self.head is None:
            return None

        # Special case: removing the head
        if self.head.movie.title.lower() == title.lower():
            removed = self.head.movie
            self.head = self.head.next
            self.size -= 1
            return removed

        current = self.head
        while current.next:
            if current.next.movie.title.lower() == title.lower():
                removed = current.next.movie
                current.next = current.next.next
                self.size -= 1
                return removed
            current = current.next

        return None  # not found

    # ----------------------------------------------------------------- pop top
    def pop_first(self):
        """Remove and return the first movie (used when the user starts watching)."""
        if self.head is None:
            return None
        movie = self.head.movie
        self.head = self.head.next
        self.size -= 1
        return movie

    # ------------------------------------------------------------------ helper
    def _find(self, title):
        current = self.head
        while current:
            if current.movie.title.lower() == title.lower():
                return current
            current = current.next
        return None

    def is_empty(self):
        return self.head is None

    def get_all(self):
        """Return all movies in watchlist order."""
        result = []
        current = self.head
        while current:
            result.append(current.movie)
            current = current.next
        return result
