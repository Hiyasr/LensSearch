from src.search_engine import LensSearch

print("Starting LensSearch...")

engine = LensSearch()

print("Building image index...")
engine.build_index()

print("Ready! 🔍")

while True:
    query = input("\nSearch images: ")

    results = engine.search(query)

    print("\nTop Matches:")
    for r in results:
        print(r)