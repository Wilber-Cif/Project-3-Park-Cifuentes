class Stack:
    """
    Watch History — implemented as a Stack (LIFO).
    Most recently watched movie is always on top.
    Chosen because:
      - We always care about the LAST thing watched (for recommendations)
      - push / pop / peek are all O(1)
    Internally uses a Python list with append/pop at the end.
    """

    def __init__(self, max_size=20):
        self._data = []
        self.max_size = max_size  # cap history so it doesn't grow forever

    def push(self, movie):
        """Add a movie to the top of the history."""
        if len(self._data) >= self.max_size:
            self._data.pop(0)  # drop the oldest entry to stay within cap
        self._data.append(movie)

    def pop(self):
        """Remove and return the most recently watched movie."""
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        """Return the most recently watched movie without removing it."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def get_all(self):
        """Return history from most-recent to oldest."""
        return list(reversed(self._data))

    def __len__(self):
        return len(self._data)


# ---------------------------------------------------------------------------

class Queue:
    """
    Up-Next Queue — implemented as a Queue (FIFO).
    Movies play in the order they were added.
    Chosen because:
      - First movie added should be first movie played
      - enqueue / dequeue are O(1)
    Internally uses a Python list (enqueue at end, dequeue at front).
    For true O(1) dequeue you'd use collections.deque, but a list is
    fine at this scale and keeps the implementation transparent.
    """

    def __init__(self):
        self._data = []

    def enqueue(self, movie):
        """Add a movie to the back of the queue."""
        self._data.append(movie)

    def dequeue(self):
        """Remove and return the movie at the front of the queue."""
        if self.is_empty():
            return None
        return self._data.pop(0)

    def peek(self):
        """Return the next movie without removing it."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def get_all(self):
        return list(self._data)

    def __len__(self):
        return len(self._data)
