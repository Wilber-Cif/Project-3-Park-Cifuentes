"""
StreamSmart Test Suite
Tests correctness of all data structures and edge cases.
Run with: python test_streamsmart.py
"""

from catalog import Catalog
from linked_list import Watchlist
from stack_queue import Stack, Queue
from data import load_sample_movies


def test_bst_insert_and_search():
    print("── BST: Insert & Search ──────────────────")
    catalog = Catalog()
    catalog.add_movie("Inception", "Sci-Fi", 2010, 8.8)
    catalog.add_movie("The Matrix", "Sci-Fi", 1999, 8.7)

    # Normal search
    result = catalog.search_title("Inception")
    assert result is not None, "Should find Inception"
    assert result.title == "Inception"
    print("  ✅ Found 'Inception'")

    # Case-insensitive
    result = catalog.search_title("inception")
    assert result is not None, "Search should be case-insensitive"
    print("  ✅ Case-insensitive search works")

    # Not found
    result = catalog.search_title("Avatar")
    assert result is None, "Should return None for missing title"
    print("  ✅ Returns None for missing title")

    # Duplicate insert
    added = catalog.add_movie("Inception", "Sci-Fi", 2010, 8.8)
    assert added is False, "Duplicate insert should return False"
    print("  ✅ Duplicate insert rejected")


def test_prefix_search():
    print("\n── BST: Prefix Search ────────────────────")
    catalog = Catalog()
    load_sample_movies(catalog)

    results = catalog.search_prefix("in")
    titles = [m.title for m in results]
    assert "Inception" in titles, "Should find Inception with prefix 'in'"
    assert "Interstellar" in titles, "Should find Interstellar with prefix 'in'"
    print(f"  ✅ Prefix 'in' matched: {titles}")

    # No match
    results = catalog.search_prefix("zzz")
    assert results == [], "Should return empty list for no match"
    print("  ✅ No match returns empty list")


def test_genre_map():
    print("\n── Hash Map: Genre Browse ────────────────")
    catalog = Catalog()
    load_sample_movies(catalog)

    sci_fi = catalog.browse_genre("Sci-Fi")
    assert len(sci_fi) > 0, "Should have Sci-Fi movies"
    print(f"  ✅ Sci-Fi has {len(sci_fi)} movies")

    # Non-existent genre
    none_genre = catalog.browse_genre("Western")
    assert none_genre == [], "Non-existent genre should return empty list"
    print("  ✅ Non-existent genre returns empty list")


def test_watchlist():
    print("\n── Linked List: Watchlist ────────────────")
    catalog = Catalog()
    load_sample_movies(catalog)

    watchlist = Watchlist()
    movie = catalog.search_title("Inception")

    # Add
    assert watchlist.add(movie) is True
    print("  ✅ Added movie to empty watchlist")

    # Duplicate
    assert watchlist.add(movie) is False
    print("  ✅ Duplicate add rejected")

    # Remove
    removed = watchlist.remove("Inception")
    assert removed is not None and removed.title == "Inception"
    print("  ✅ Movie removed successfully")

    # Remove from empty
    removed = watchlist.remove("Inception")
    assert removed is None
    print("  ✅ Remove from empty returns None")

    # Pop first
    m2 = catalog.search_title("The Matrix")
    watchlist.add(movie)
    watchlist.add(m2)
    first = watchlist.pop_first()
    assert first.title == "Inception"
    print("  ✅ pop_first() returns head correctly")


def test_stack():
    print("\n── Stack: Watch History ──────────────────")
    catalog = Catalog()
    load_sample_movies(catalog)

    stack = Stack()
    m1 = catalog.search_title("Inception")
    m2 = catalog.search_title("Interstellar")

    # Empty stack
    assert stack.peek() is None
    assert stack.pop() is None
    print("  ✅ Empty stack peek/pop return None")

    stack.push(m1)
    stack.push(m2)

    # Peek = most recent
    assert stack.peek().title == "Interstellar"
    print("  ✅ peek() returns most recently pushed movie")

    popped = stack.pop()
    assert popped.title == "Interstellar"
    print("  ✅ pop() returns and removes most recent movie")


def test_queue():
    print("\n── Queue: Up Next ────────────────────────")
    catalog = Catalog()
    load_sample_movies(catalog)

    q = Queue()
    m1 = catalog.search_title("Inception")
    m2 = catalog.search_title("Interstellar")

    assert q.dequeue() is None
    print("  ✅ Empty queue dequeue returns None")

    q.enqueue(m1)
    q.enqueue(m2)

    first = q.dequeue()
    assert first.title == "Inception"
    print("  ✅ FIFO order correct — first enqueued is first dequeued")


def test_recommendations():
    print("\n── Recommendations ───────────────────────")
    catalog = Catalog()
    load_sample_movies(catalog)

    recs = catalog.recommend("Sci-Fi", exclude_title="Inception")
    titles = [m.title for m in recs]
    assert "Inception" not in titles, "Should exclude watched movie"
    print(f"  ✅ Recommendations exclude watched: {titles}")

    # Empty genre
    recs = catalog.recommend("Western")
    assert recs == []
    print("  ✅ No recs for unknown genre returns empty list")


# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 45)
    print("   StreamSmart Test Suite")
    print("=" * 45)
    test_bst_insert_and_search()
    test_prefix_search()
    test_genre_map()
    test_watchlist()
    test_stack()
    test_queue()
    test_recommendations()
    print("\n" + "=" * 45)
    print("   ✅ All tests passed!")
    print("=" * 45)
