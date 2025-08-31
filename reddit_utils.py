import os
import praw
from dotenv import load_dotenv

load_dotenv()


def get_reddit_data(username: str, limit: int = 100) -> list:
    """
    Scrape a Redditor's comments and posts.

    Args:
        username (str): The Reddit username.
        limit (int): The number of items to fetch (for both posts and comments).

    Returns:
        list: A list of dictionaries, each containing the text and permalink.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
        )

        print(f"Reddit API Read-Only: {reddit.read_only}")

        redditor = reddit.redditor(username)
        user_data = []

        print(f"Fetching data for u/{username}...")

        for comment in redditor.comments.new(limit=limit):
            user_data.append({
                "type": "comment",
                "text": comment.body,
                "permalink": f"https://www.reddit.com{comment.permalink}"
            })

        for submission in redditor.submissions.new(limit=limit):
            user_data.append({
                "type": "post",
                "text": f"Title: {submission.title}\n\n{submission.selftext}",
                "permalink": f"https://www.reddit.com{submission.permalink}"
            })

        print(f"Found {len(user_data)} total items.")
        return user_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
