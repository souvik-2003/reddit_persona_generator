# Reddit User Persona Generator 🤖👤

This project is a Python script designed to generate a detailed user persona from a public Reddit profile. It scrapes a user's recent comments and posts, then leverages a Large Language Model (LLM) to analyze the content and construct a structured persona, complete with citations for each inferred characteristic.

This was developed as a submission for the AI/LLM Engineer Intern assignment at **BeyondChats**.

---

## ✨ Features

-   **Reddit Data Scraping**: Utilizes the PRAW library to reliably fetch user comments and submissions via the official Reddit API.
-   **LLM-Powered Analysis**: Employs the OpenAI API to perform nuanced analysis of the user's text data.
-   **Structured Persona Output**: Generates a detailed persona in a clean, readable text format, inspired by classic UX persona templates.
-   **Cited Inferences**: A core feature where every piece of the persona (e.g., interests, personality traits) is backed by a citation linking to the specific post or comment it was derived from.
-   **CLI Interface**: Simple and easy to run from the command line with a single Reddit profile URL as an argument.
-   **Organized Output**: Saves each generated persona in a dedicated `output/` directory for easy access.

---

## 📝 Sample Output

The generated persona is saved as a `.txt` file. Here is a sample of the structure:

```text
***************************************************
      USER PERSONA: u/example_user
***************************************************

"I'm a developer who enjoys diving deep into technical topics, helping others, and engaging with my favorite gaming communities."

===================================================
DEMOGRAPHICS
===================================================
- AGE: 25-30 [Source: Cannot be determined from data]
- OCCUPATION: Software Developer / Engineer [Source: https://www.reddit.com/r/learnpython/comments/...]
- ARCHETYPE: The Sage / The Helper [Source: Frequent helpful and detailed answers in programming subreddits https://www.reddit.com/r/learnpython/comments/...]

===================================================
PERSONALITY & TRAITS
===================================================
- KEYWORDS: Technical, Helpful, Inquisitive, Gamer

- PERSONALITY SPECTRUM (MBTI-Style Analysis):
  - Introvert <---●-----> Extrovert: Leans Introvert. Engages in deep, text-based discussions rather than broad social posts. [Source: Overall comment history]
  - Thinking <---●-------> Feeling: Strongly Thinking. Provides logical, fact-based answers. [Source: https://www.reddit.com/r/learnpython/comments/...]

... and so on for other sections.
```

---

## ⚙️ Setup and Installation

Follow these steps to set up the project on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   Git

### 2. Clone the Repository

```bash
git clone https://github.com/SudoAnxu/Reddit_Persona_Summarizer.git
cd Reddit_Persona_Summarizer
```

### 3. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

-   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 4. Install Dependencies

Install all the required Python libraries from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Configure API Keys (Crucial Step)

This project requires API keys for both Reddit and OpenAI. These keys should be kept private and are managed using a `.env` file.

i. **Create the `.env` file:**
   Create a file named `.env` in the root of the project directory. You can do this by copying the example file:
   ```bash
   cp .env.example .env
   ```
   *(If you're on Windows, you can manually create and rename the file.)*

ii. **Populate `.env` with your credentials:**
   Open the `.env` file and add your secret keys.

   ```ini
   # Reddit API Credentials (from https://www.reddit.com/prefs/apps)
   REDDIT_CLIENT_ID="your_client_id_here"
   REDDIT_CLIENT_SECRET="your_client_secret_here"
   REDDIT_USER_AGENT="PersonaGenerator v1.0 by u/your_reddit_username"
   REDDIT_USERNAME="your_reddit_username"
   REDDIT_PASSWORD="your_reddit_password"

   # OpenAI API Key (from https://platform.openai.com/account/api-keys)
   OPENAI_API_KEY="sk-your_openai_api_key_here"
   ```

   **Note:** The `.env` file is listed in `.gitignore` and will not be committed to the repository.

---

## 🚀 How to Execute

Run the script from the root of the project directory using your terminal. Pass the full URL of the Reddit user's profile as a command-line argument.

**Syntax:**
```bash
python main.py "REDDIT_PROFILE_URL"
```

**Examples from the assignment:**

1.  To generate a persona for the user `kojied`:
    ```bash
    python main.py "https://www.reddit.com/user/kojied/"
    ```

2.  To generate a persona for the user `Hungry-Move-6603`:
    ```bash
    python main.py "https://www.reddit.com/user/Hungry-Move-6603/"
    ```

The script will print progress updates to the console and save the final persona as a `.txt` file inside the `output/` directory (e.g., `output/kojied_persona.txt`).

---

## 🛠️ Technologies Used

-   **Python 3**
-   **PRAW (Python Reddit API Wrapper)**: For scraping data from Reddit.
-   **OpenAI Python Library**: For interacting with the GPT models.
-   **python-dotenv**: For managing environment variables and API keys securely.

---

## 🔮 Future Improvements

While this script fulfills the assignment requirements, here are some ways it could be extended:

-   **Web Interface**: Build a simple web UI using Streamlit or Flask where anyone can paste a URL and see the generated persona without using the command line.
-   **Advanced NLP**: Incorporate more specific NLP techniques like sentiment analysis over time or named-entity recognition (NER) to enrich the persona.
-   **Data Caching**: Implement caching to avoid re-scraping and re-processing data for the same user within a short time frame.
-   **Local LLM Support**: Add an option to use a locally running LLM (e.g., via Ollama) to remove the dependency on the OpenAI API.
-   **Error Handling**: More robust handling for various edge cases, such as suspended users, private users, or users with no posts/comments.
