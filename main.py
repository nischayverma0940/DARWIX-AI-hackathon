import requests
import pandas as pd
from bs4 import BeautifulSoup
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyB1mQFvHOjhpV4eigJ2WdJhDzIKAbcbtBE"
genai.configure(api_key=GEMINI_API_KEY)

def fetch_article(url: str) -> str:
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    article_text = " ".join(p.get_text(strip=True) for p in soup.find_all("p"))
    return article_text.strip()

def save_article(text: str, fname="articles.csv"):
    pd.DataFrame({"text": [text]}).to_csv(fname, index=False)

def generate_critical_report(article_text: str, title="Untitled") -> str:
    prompt = f"""
Required Output: Your program must produce a single "Critical Analysis Report"
in Markdown format. This report must contain the following distinct sections:

1. Core Claims: A bulleted list summarizing the 3–5 main factual claims the article makes.
2. Language & Tone Analysis: A brief analysis and classification of the article's language 
   (e.g., "Appears neutral and factual," "Uses emotionally charged and persuasive language," 
   "Reads as a strong opinion piece").
3. Potential Red Flags: A bulleted list identifying any detected signs of bias or poor reporting, 
   such as the use of loaded terminology, an over-reliance on anonymous sources, a lack of cited data, 
   or failing to present opposing viewpoints.
4. Verification Questions: A list of 3–4 insightful, specific questions a reader should ask 
   to independently verify the article's content.
5. Entity Recognition: Identify the key people, organizations, and locations mentioned in the article. 
   For each entity, suggest what a reader should critically investigate 
   (e.g., "Check the author's previous work," "Look into the funding of 'The XYZ Institute'").
6. Counter-Argument Simulation: Provide a short summary of the article from the perspective of a hypothetical 
   opposing viewpoint. This should starkly highlight potential biases by presenting how the same facts 
   might be framed differently.

Example Output Structure:
# Critical Analysis Report for: [Article Title]

### Core Claims
* Claim 1...
* Claim 2...

### Language & Tone Analysis
The language is highly persuasive and uses emotionally charged words like "disastrous".

### Potential Red Flags
* Relies on a single anonymous insider.
* No independent data is cited.

### Verification Questions
1. Can I find corroboration in other independent outlets?
2. Who funds the organization publishing this piece?

### Entity Recognition
* John Doe (politician): Investigate prior policy positions.
* The XYZ Institute (think tank): Research funding sources.
* City of Springfield: Check local government reports on this issue.

### Counter-Argument Simulation
From an opposing viewpoint, the article could be summarized as: 
"While the government claims to be providing support, critics argue that the response is inadequate 
and primarily serves political interests rather than genuine relief efforts."
    
Now, generate the "Critical Analysis Report" for the following article:

Article Title: {title}  
Article Text: {article_text}
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text 

if __name__ == "__main__":
    url = input("Enter article URL: ").strip()
    article_text = fetch_article(url)

    if not article_text:
        print("Failed to extract article text.")
        exit()

    save_article(article_text)
    report = generate_critical_report(article_text, title="News Article")

    print("\n--- Critical Analysis Report ---\n")
    print(report)
