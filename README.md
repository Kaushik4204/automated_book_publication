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

