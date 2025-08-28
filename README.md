# Critical News Analysis Tool

## Overview

This project provides a Python-based tool to **fetch online news
articles**, extract their text, and generate a **detailed critical
analysis report** using Google's **Gemini Generative AI** model.\
It is designed to help readers critically evaluate online articles by
summarizing claims, analyzing tone, detecting biases, and generating
verification questions.

## Features

-   **Article Scraping**: Automatically fetches article text from any
    provided URL using `requests` and `BeautifulSoup`.
-   **Data Storage**: Saves the extracted article content into a CSV
    file using `pandas` for further analysis or record-keeping.
-   **AI-Powered Analysis**: Leverages Google's Gemini model to generate
    a structured "Critical Analysis Report" in Markdown format.
-   **Bias Detection**: Identifies potential red flags such as loaded
    language, lack of evidence, or one-sided reporting.
-   **Entity Recognition**: Highlights key people, organizations, and
    locations in the article and suggests how they should be critically
    examined.
-   **Counter-Arguments**: Simulates an opposing viewpoint to reveal
    potential biases.

## Installation

1.  Clone this repository:

    ``` bash
    git clone https://github.com/yourusername/critical-news-analysis.git
    cd critical-news-analysis
    ```

2.  Install required dependencies:

    ``` bash
    pip install requests pandas beautifulsoup4 google-generativeai
    ```

3.  Set up your **Gemini API key** by replacing the placeholder in the
    script:

    ``` python
    GEMINI_API_KEY = "your_api_key_here" (already present in this project)
    ```

## Usage

Run the script and provide the URL of a news article when prompted:

``` bash
python analysis_tool.py
```

Example input:

    Enter article URL: https://www.bbc.com/news/articles/cx29z9g2kl2o

The program will: 1. Fetch and extract the text of the article. 2. Save
the article text to `articles.csv`. 3. Generate and display a **Critical
Analysis Report** with sections: - Core Claims - Language & Tone
Analysis - Potential Red Flags - Verification Questions - Entity
Recognition - Counter-Argument Simulation

## Example Output

    # Critical Analysis Report for: News Article

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

