from catalog import Catalog
from linked_list import Watchlist
from stack_queue import Stack, Queue
from data import load_sample_movies


# ─────────────────────────────────────────────────────────────────────────────
#  Display helpers
# ─────────────────────────────────────────────────────────────────────────────

def print_header():
    print("\n" + "═" * 45)
    print("          🎬  S T R E A M S M A R T")
    print("═" * 45)

def print_menu():
    print("""
  [1] Browse all movies (A–Z)
  [2] Search by title
  [3] Browse by genre
  [4] Add to watchlist
  [5] View / remove from watchlist
  [6] Watch next in queue
  [7] View watch history
  [8] Get recommendations
  [9] Quit
""")

def print_movie_list(movies, numbered=True):
    if not movies:
        print("  (none)")
        return
    for i, m in enumerate(movies, 1):
        prefix = f"  {i}. " if numbered else "  • "
        print(f"{prefix}{m}")

def prompt(msg):
    return input(f"\n  {msg}: ").strip()


# ─────────────────────────────────────────────────────────────────────────────
#  Feature handlers
# ─────────────────────────────────────────────────────────────────────────────

def browse_all(catalog):
    print("\n  📋 All Movies (A–Z)")
    print("  " + "─" * 40)
    print_movie_list(catalog.get_all_movies())

def search_title(catalog):
    query = prompt("Enter title (or first few letters)")
    if not query:
        return
    # Try exact match first
    result = catalog.search_title(query)
    if result:
        print(f"\n  ✅ Found: {result}")
    else:
        # Fall back to prefix search
        results = catalog.search_prefix(query)
        if results:
            print(f"\n  🔍 Partial matches for '{query}':")
            print_movie_list(results)
        else:
            print(f"\n  ❌ No movies found matching '{query}'.")

def browse_genre(catalog):
    genres = catalog.list_genres()
    print("\n  Available genres:")
    for g in genres:
        print(f"    • {g.title()}")
    genre = prompt("Enter genre")
    movies = catalog.browse_genre(genre)
    if movies:
        print(f"\n  🎭 {genre.title()} movies:")
        print_movie_list(movies)
    else:
        print(f"\n  ❌ Genre '{genre}' not found.")

def add_to_watchlist(catalog, watchlist):
    title = prompt("Enter movie title to add")
    movie = catalog.search_title(title)
    if movie is None:
        print(f"\n  ❌ '{title}' not found in catalog.")
        return
    success = watchlist.add(movie)
    if success:
        print(f"\n  ✅ '{movie.title}' added to your watchlist.")
    else:
        print(f"\n  ⚠️  '{movie.title}' is already in your watchlist.")

def view_watchlist(watchlist):
    print("\n  📌 Your Watchlist:")
    print("  " + "─" * 40)
    movies = watchlist.get_all()
    print_movie_list(movies)
    if not movies:
        return
    title = prompt("Enter title to remove (or press Enter to skip)")
    if title:
        removed = watchlist.remove(title)
        if removed:
            print(f"\n  🗑️  '{removed.title}' removed from watchlist.")
        else:
            print(f"\n  ❌ '{title}' not found in watchlist.")

def watch_next(watchlist, history, up_next_queue):
    """
    Workflow:
      1. Pop the first movie from the watchlist (linked list)
      2. Push it onto watch history (stack)
      3. Enqueue in the up-next queue (for this session's autoplay)
    """
    movie = watchlist.pop_first()
    if movie is None:
        print("\n  ⚠️  Your watchlist is empty. Add some movies first!")
        return
    history.push(movie)
    up_next_queue.enqueue(movie)
    print(f"\n  ▶️  Now watching: {movie}")
    print(f"     (Added to your watch history)")

def view_history(history):
    print("\n  🕐 Watch History (most recent first):")
    print("  " + "─" * 40)
    print_movie_list(history.get_all())

def get_recommendations(catalog, history):
    last = history.peek()
    if last is None:
        print("\n  ⚠️  Watch something first to get recommendations!")
        return
    print(f"\n  🎯 Because you watched '{last.title}' ({last.genre}):")
    recs = catalog.recommend(last.genre, exclude_title=last.title)
    print_movie_list(recs)


# ─────────────────────────────────────────────────────────────────────────────
#  Main loop
# ─────────────────────────────────────────────────────────────────────────────

def main():
    catalog = Catalog()
    watchlist = Watchlist()
    history = Stack()
    up_next = Queue()

    load_sample_movies(catalog)

    print_header()
    print("  Welcome! 30 movies loaded.\n")

    while True:
        print_menu()
        choice = prompt("Choose an option").strip()

        if choice == "1":
            browse_all(catalog)
        elif choice == "2":
            search_title(catalog)
        elif choice == "3":
            browse_genre(catalog)
        elif choice == "4":
            add_to_watchlist(catalog, watchlist)
        elif choice == "5":
            view_watchlist(watchlist)
        elif choice == "6":
            watch_next(watchlist, history, up_next)
        elif choice == "7":
            view_history(history)
        elif choice == "8":
            get_recommendations(catalog, history)
        elif choice == "9":
            print("\n  👋 Thanks for using StreamSmart. Goodbye!\n")
            break
        else:
            print("\n  ❌ Invalid option. Please enter a number 1–9.")


if __name__ == "__main__":
    main()
