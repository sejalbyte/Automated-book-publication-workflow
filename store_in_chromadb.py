from chromadb import Client
from chromadb.config import Settings
import os

INPUT_FILE = os.path.abspath("data/spun_chapter1_v1.txt")

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"❌ File not found: {INPUT_FILE}")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    chapter_text = f.read()

client = Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="chromadb_store"
))

collection = client.get_or_create_collection(name="chapters")

collection.add(
    documents=[chapter_text],
    metadatas=[{"chapter": "1", "version": "v1_edited"}],
    ids=["chapter1_v1_edited"]
)

print("✅ Chapter stored successfully in ChromaDB!")