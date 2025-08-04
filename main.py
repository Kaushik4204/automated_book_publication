from scraping.fetch_and_screenshot import fetch_and_screenshot
from agents.ai_writer import generate_chapter
from agents.ai_reviewer import review_chapter
from agents.rl_reward import calculate_reward
from versioning.chromadb_handler import store_version
from utils.io import save_text, save_json
from dotenv import load_dotenv
import uuid
import os

# Load environment variables from .env
load_dotenv()

def run_pipeline(url):
    print("📥 Step 1: Fetching and screenshotting content...")
    content = fetch_and_screenshot(url, save_path="data/raw")
    if not content:
        print("❌ Failed to fetch content.")
        return
    print(f"✅ Fetched content (length: {len(content)})")

    print("\n✍️ Step 2: Rewriting content with AI writer...")
    rewritten = generate_chapter(content)
    if not rewritten:
        print("❌ Failed to rewrite content.")
        return
    print(f"✅ Rewritten content (length: {len(rewritten)})")

    print("\n🧠 Step 3: Reviewing rewritten content with AI reviewer...")
    feedback = review_chapter(content, rewritten)
    if not feedback:
        print("❌ Review failed.")
        return
    print(f"✅ Review Feedback:\n{feedback}")

    print("\n📊 Step 4: Calculating reward score...")
    reward = calculate_reward(feedback)
    print(f"✅ Reward: {reward}")

    print("\n💾 Step 5: Storing version to ChromaDB and local folders...")
    version_id = str(uuid.uuid4())[:8]  # short unique ID

    # Save processed data
    save_text(rewritten, f"data/processed/{version_id}_rewritten.txt")
    save_json(feedback, f"data/processed/{version_id}_review.json")
    save_json({"reward": reward}, f"data/processed/{version_id}_reward.json")

    # Save final version
    version_data = {
        "id": version_id,
        "original": content,
        "rewritten": rewritten,
        "review": feedback,
        "reward": reward
    }
    save_json(version_data, f"data/versions/version_{version_id}.json")

    # Store to vector DB
    store_version(rewritten, metadata={"id": version_id, "reward": reward})

    print(f"✅ Stored version with ID: {version_id} to disk and ChromaDB.")

if __name__ == "__main__":
    test_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    run_pipeline(test_url)
