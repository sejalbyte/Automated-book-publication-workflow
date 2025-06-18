import chromadb

# Use the new PersistentClient (recommended after ChromaDB update)
client = chromadb.PersistentClient(path="chromadb_store")

# Get or create the collection
collection = client.get_or_create_collection(name="chapters")

# 🔍 Take user input for search query
query = input("🔍 Enter your search query: ").strip()

# Perform the query
results = collection.query(
    query_texts=[query],
    n_results=1
)

# 📘 Display the result
print("\n📘 Top Matching Passage:\n")
if results.get("documents") and results["documents"][0]:
    for doc in results["documents"][0]:
        print(doc)
else:
    print("No matching passages found.")