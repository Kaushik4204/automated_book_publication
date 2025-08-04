# 📚 Automated Book Publication Workflow

A modular AI-driven pipeline that scrapes book chapters, rewrites them using LLMs, evaluates with reinforcement learning-based rewards, and supports human-in-the-loop editing, content versioning, and semantic search.

---

## 🎯 Objective

To build a system that:
- Extracts content from structured book sources (like Wikisource)
- Rewrites and refines it using AI Writer & AI Reviewer agents
- Allows human intervention for editing and feedback
- Applies RL-inspired reward scoring
- Maintains versioning and enables semantic content search

---

## 🧠 Features

| Module                        | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 🔍 **Scraping**              | Scrapes text and screenshots from chapters using Playwright                 |
| ✍️ **AI Writer**             | Uses an LLM (OpenAI or Gemini) to "spin" the scraped content                |
| 🕵️ **AI Reviewer**          | Critically evaluates the rewritten text and scores it                       |
| 🧠 **RL Reward Model**       | Calculates a reward based on reviewer feedback (basic RL loop)              |
| 👨‍💻 **Human-in-the-loop**   | Prompts for human approval or edits in multiple iterations                  |
| 🧠 **ChromaDB Versioning**   | Saves content versions as embeddings for comparison and search              |
| 🔍 **Semantic Search**       | Find similar chapters/versions using vector search                          |
| 🔊 **(Optional) Voice TTS**  | Text-to-speech support for accessibility                                   |

---

## 🗂️ Project Structure
automated_book_publication/

├── scraping/

│ └── fetch_and_screenshot.py # Scrape HTML + take screenshots

├── agents/

│ ├── ai_writer.py # AI Writer using OpenAI/Gemini

│ ├── ai_reviewer.py # AI Reviewer + scoring

│ └── rl_reward.py # Reward based on reviewer feedback

├── human_loop/

│ └── feedback_interface.py # Collect human edits, rerun pipeline

├── versioning/

│ └── chromadb_handler.py # Save, retrieve versions semantically

├── utils/

│ └── io.py # File read/write utilities

├── data/

│ ├── raw/ # Raw screenshots and HTML

│ ├── processed/ # Intermediate human-reviewed outputs

│ └── versions/ # Final versioned content

├── main.py # Orchestration pipeline

├── requirements.txt # All Python dependencies

└── README.md # Project overview (this file)


---

## 🛠️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/automated_book_publication.git
cd automated_book_publication
```
### 2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Run the pipeline
```bash
python main.py
```

### 4. Sample URL to test

```bash
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
```

### Human-in-the-Loop Editing
During the pipeline run:

After AI writing and reviewing, you are prompted to edit the content manually or approve.
Your feedback determines whether the version is stored or rewritten again.
This loop can continue until you're satisfied.

---

##📦 Dependencies
playwright

chromadb

openai or google-generativeai

langchain (optional)

beautifulsoup4

pandas

tqdm

Install via:
```bash
pip install -r requirements.txt
```
---

## 📹 Demo Video
