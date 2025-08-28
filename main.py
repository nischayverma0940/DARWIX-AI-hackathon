import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import torch
from transformers import pipeline


# -----------------------------
# STEP 1: Extract article text
# -----------------------------
def fetch_article_bs4(url: str) -> str:
    """Fetch article text using BeautifulSoup"""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        article_tags = soup.find_all(['article', 'p'])
        text = " ".join(tag.get_text(strip=True) for tag in article_tags)
        return text.strip()
    except Exception as e:
        print(f"[ERROR] Could not fetch with BeautifulSoup: {e}")
        return ""


# -----------------------------
# STEP 2: Save into CSV (overwrite)
# -----------------------------
def save_article(text: str, filename: str = "articles.csv") -> str:
    df = pd.DataFrame({"text": [text]})
    df.to_csv(filename, index=False)   # overwrite every time
    return filename


# -----------------------------
# STEP 3: Load model for analysis
# -----------------------------
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = 0
else:
    device = -1

report_generator = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-beta",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device=device
)


# -----------------------------
# STEP 4: Generate Critical Report
# -----------------------------
def generate_critical_report(article_text: str, article_title: str = "Untitled Article") -> str:
    prompt = f"""
You are a critical thinking assistant.
Required Output: Your program must produce a single "Critical Analysis Report"
in Markdown format. This report must contain the following distinct sections:

1. Core Claims: A bulleted list summarizing the 3-5 main factual claims the
article makes.
2. Language & Tone Analysis: A brief analysis and classification of the article's
language (e.g., "Appears neutral and factual," "Uses emotionally charged and
persuasive language," "Reads as a strong opinion piece").
3. Potential Red Flags: A bulleted list identifying any detected signs of bias or
poor reporting, such as loaded terminology, anonymous sources, lack of data,
or ignoring opposing viewpoints.
4. Verification Questions: 3-4 insightful, specific questions a reader should ask
to independently verify the article's content.

Now analyze the following article:

# Critical Analysis Report for: {article_title}

Article: {article_text}
"""
    response = report_generator(prompt, max_new_tokens=600, do_sample=True, temperature=0.7)
    return response[0]["generated_text"]


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    url = "https://indianexpress.com/article/cities/chandigarh/haryana-cm-nayab-singh-saini-offers-support-to-punjab-amid-devastating-flood-10216378/"  # example URL

    article_text = fetch_article_bs4(url)
    if not article_text:
        print("❌ Failed to extract article text.")
        exit()

    save_article(article_text)  # save to CSV (overwrite)

    # Run analysis
    report = generate_critical_report(article_text, article_title="Haryana CM on Punjab Floods")
    print(report)
