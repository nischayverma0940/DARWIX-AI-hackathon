# 📰 Critical News Analysis Tool

This project is an **AI-powered pipeline** that extracts news articles from the web, saves them into a structured dataset, and generates a **Critical Analysis Report** using a large language model (LLM).  

The goal is to encourage **critical thinking** by breaking down an article into:  
- Core claims  
- Language & tone  
- Potential red flags  
- Verification questions  

---

## Project Overview

When you run this tool:  

1. **Scrape a news article** from a given URL using `BeautifulSoup`.  
2. **Store the article** inside a CSV file (`articles.csv`).  
3. **Run AI analysis** using HuggingFace Transformers (`HuggingFaceH4/zephyr-7b-beta`).  
4. **Generate a Markdown report** in the terminal, highlighting claims, tone, and fact-checking questions.  

---

## Prerequisites

Before you begin, make sure you have:  

- **Python 3.9+** installed (recommended 3.10 or higher).  
- A machine with:  
  - Apple Silicon (M1/M2/M3) → uses **Metal/MPS acceleration**  
  - NVIDIA GPU → uses **CUDA**  
  - If neither, it runs on **CPU** (slower, but works).  

Check your Python version:  
```bash
python3 --version
```

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/nischayverma0940/DARWIX-AI-hackathon.git
cd DARWIX-AI-hackathon
```

This creates a local copy of the project on your system.  

---

## Step 2: Create a Virtual Environment

Creating a **virtual environment** ensures dependencies are isolated from your system Python.  

```bash
python3 -m venv venv
```

Activate it:  

- On **macOS/Linux**:
```bash
source venv/bin/activate
```

- On **Windows**:
```bash
venv\Scripts\activate
```

Once activated, you should see `(venv)` in your terminal prompt.  

---

## Step 3: Install Dependencies

If a `requirements.txt` is provided:
```bash
pip install -r requirements.txt
```

If not, install manually:
```bash
pip install requests beautifulsoup4 pandas torch transformers
```

Verify installation:
```bash
pip list
```

You should see at least:  
- `requests`  
- `beautifulsoup4`  
- `pandas`  
- `torch`  
- `transformers`  

---

## Step 4: Run the Script

Run the main file:
```bash
python main.py
```

### What happens internally:
1. **URL Fetching** – The script downloads the news article.  
2. **Text Extraction** – It pulls `<p>` and `<article>` tags from the HTML.  
3. **Save to CSV** – Extracted text is saved to `articles.csv`.  
4. **AI Model** – Hugging Face LLM (`zephyr-7b-beta`) is used to generate analysis.  
5. **Report Output** – A structured **Markdown report** is printed in your terminal.  

---

## Example Report

Running the script on an article generates something like this:

```
# Critical Analysis Report for: Haryana CM on Punjab Floods

### Core Claims
- Haryana CM Nayab Singh Saini pledged support to Punjab amid floods.
- Relief efforts include inter-state coordination.
- Government promises aid for affected citizens.

### Language & Tone Analysis
Appears factual but contains persuasive undertones emphasizing unity.

### Potential Red Flags
- Lack of detailed statistics on flood impact.
- No opposition viewpoints mentioned.
- Reliance on CM’s statements without independent verification.

### Verification Questions
1. What official relief measures have been initiated so far?
2. Are independent agencies confirming the extent of damage?
3. How have past flood relief efforts compared in scale and speed?
```

---
 
