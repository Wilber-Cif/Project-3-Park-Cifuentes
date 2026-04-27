class MovieNode:
    """A single node in the BST, storing one movie."""

    def __init__(self, title, genre, year, rating):
        self.title = title          # used as the BST key
        self.genre = genre
        self.year = year
        self.rating = rating
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.title} ({self.year}) | Genre: {self.genre} | Rating: {self.rating}"


class MovieBST:
    """
    Binary Search Tree that stores movies sorted alphabetically by title.
    - insert:  O(log n) average
    - search:  O(log n) average
    - in-order traversal gives alphabetically sorted list
    """

    def __init__(self):
        self.root = None

    # ------------------------------------------------------------------ insert
    def insert(self, title, genre, year, rating):
        """Insert a new movie. Ignores duplicates (same title)."""
        new_node = MovieNode(title, genre, year, rating)
        if self.root is None:
            self.root = new_node
            return True
        return self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.title.lower() < current.title.lower():
            if current.left is None:
                current.left = new_node
                return True
            return self._insert_recursive(current.left, new_node)
        elif new_node.title.lower() > current.title.lower():
            if current.right is None:
                current.right = new_node
                return True
            return self._insert_recursive(current.right, new_node)
        else:
            return False  # duplicate title — do nothing

    # ------------------------------------------------------------------ search
    def search(self, title):
        """Return the MovieNode with this title, or None if not found."""
        return self._search_recursive(self.root, title)

    def _search_recursive(self, current, title):
        if current is None:
            return None
        if title.lower() == current.title.lower():
            return current
        elif title.lower() < current.title.lower():
            return self._search_recursive(current.left, title)
        else:
            return self._search_recursive(current.right, title)

    # ----------------------------------------------------------- prefix search
    def search_by_prefix(self, prefix):
        """Return all movies whose title starts with the given prefix."""
        results = []
        self._prefix_recursive(self.root, prefix.lower(), results)
        return results

    def _prefix_recursive(self, current, prefix, results):
        if current is None:
            return
        if current.title.lower().startswith(prefix):
            results.append(current)
        # BST property: still need to explore both sides for prefix matches
        self._prefix_recursive(current.left, prefix, results)
        self._prefix_recursive(current.right, prefix, results)

    # --------------------------------------------------------- in-order (A–Z)
    def get_all_sorted(self):
        """Return all movies in alphabetical order (in-order traversal)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current is None:
            return
        self._inorder(current.left, result)
        result.append(current)
        self._inorder(current.right, result)

    def is_empty(self):
        return self.root is None
