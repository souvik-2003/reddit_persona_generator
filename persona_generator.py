import openai
import os

def create_persona_prompt(username: str, user_data: list) -> str:
    """
    Create a detailed, structured prompt for the LLM based on the persona template.

    Args:
        username (str): The Reddit username.
        user_data (list): The scraped data from Reddit.

    Returns:
        str: The prompt for the LLM.
    """
    combined_text = ""
    for item in user_data:
        combined_text += (
            f"Source [{item['permalink']}]: {item['text']}\n\n---\n\n"
        )

    prompt = f"""
You are an expert User Experience (UX) Researcher and Psychologist. Your task is to analyze the provided Reddit user data and generate a detailed user persona. The output MUST strictly follow the text-based template provided below.

**CRUCIAL INSTRUCTION:** For every single point, conclusion, or inference you make, you MUST cite the source. Use the format `[Source: URL]`. If information cannot be determined, you MUST state "Cannot be determined from data" and cite that as a general conclusion.

**USER DATA TO ANALYZE:**
---
{combined_text}
---

**PERSONA OUTPUT TEMPLATE (Use this exact format):**

***************************************************
      USER PERSONA: u/{username}
***************************************************

"[A short, summarizing quote that captures the user's essence in one sentence, written in the first person]"

===================================================
DEMOGRAPHICS
===================================================
- AGE: [Infer an age range, e.g., 20-25. Justify with citations.]
- OCCUPATION: [Infer their profession. Justify with citations.]
- LOCATION: [Infer their country, state, or city. Justify with citations.]
- STATUS: [Infer relationship status, e.g., Single, In a relationship. Justify.]
- ARCHETYPE: [Assign a Jungian archetype (e.g., The Sage, The Creator, The Jester) that fits their personality. Justify with citations.]

===================================================
PERSONALITY & TRAITS
===================================================
- KEYWORDS: [List 4-5 single-word adjectives that describe the user.]

- PERSONALITY SPECTRUM (MBTI-Style Analysis):
  - Introvert <[Place progress bar on scale of 10 '-']> Extrovert: [Justification and citation]
  - Intuition <[Place progress bar on scale of 10 '-']> Sensing: [Justification and citation]
  - Thinking <[Place progress bar on scale of 10 '-']> Feeling: [Justification and citation]
  - Judging <[Place progress bar on scale of 10 '-']> Perceiving: [Justification and citation]

===================================================
MOTIVATIONS (Rated 1-5, list the top 3-4)
===================================================
- [MOTIVATION 1]: [Rating]/5 - [Justification and citation]
- [MOTIVATION 2]: [Rating]/5 - [Justification and citation]
- [MOTIVATION 3]: [Rating]/5 - [Justification and citation]
- [MOTIVATION 4]: [Rating]/5 - [Justification and citation]
===================================================
BEHAVIOUR & HABITS
===================================================
- [List of observed behaviors as bullet points, each with a citation.]
- [Example: Enjoys discussing specific TV shows like 'The Office'. [Source: URL]]

===================================================
GOALS & NEEDS
===================================================
- GOAL: [Inferred primary goal, with citation]
- GOAL: [Inferred secondary goal, with citation]
- NEED: [Inferred primary need, with citation]
- NEED: [Inferred secondary need, with citation]

===================================================
FRUSTRATIONS
===================================================
- [List of things the user seems to dislike or complain about, as bullet points, each with a citation.]
- [Example: Becomes frustrated with political misinformation. [Source: URL]]

"""
    return prompt


def generate_persona(username: str, user_data: list) -> str:
    """
    Generate a user persona using an LLM.

    Args:
        username (str): The Reddit username.
        user_data (list): The scraped data from Reddit.

    Returns:
        str: The generated user persona text.
    """
    if not user_data:
        return f"Could not generate persona for u/{username}: No data found."

    prompt = create_persona_prompt(username, user_data)

    print(f"Generating structured persona for u/{username} with LLM...")

    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a User Experience (UX) Researcher and Psychologist."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred with the OpenAI API: {e}"


def save_persona_to_file(username: str, persona_text: str):
    """
    Save the generated persona to a text file.

    Args:
        username (str): The Reddit username.
        persona_text (str): The generated persona text.
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{username}_persona.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"Persona saved to {file_path}")

