import argparse
from urllib.parse import urlparse

from reddit_utils import get_reddit_data
from persona_generator import generate_persona, save_persona_to_file


def extract_username_from_url(url: str) -> str:
    """
    Extract the username from a Reddit user profile URL.

    Args:
        url (str): The Reddit user profile URL.

    Returns:
        str: The extracted username or None if extraction fails.
    """
    try:
        path_parts = urlparse(url).path.strip("/").split("/")
        if len(path_parts) >= 2 and path_parts[0].lower() == 'user':
            return path_parts[1]
    except Exception:
        return None
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Reddit user persona from a profile URL."
    )
    parser.add_argument(
        "url",
        type=str,
        help="Reddit user profile URL (e.g., https://www.reddit.com/user/username)"
    )
    args = parser.parse_args()

    username = extract_username_from_url(args.url)

    if not username:
        print("Error: Could not extract username from the provided URL.")
        return

    reddit_data = get_reddit_data(username, limit=100)

    if not reddit_data:
        print(f"No Reddit data found for user '{username}'.")
        return

    persona = generate_persona(username, reddit_data)

    save_persona_to_file(username, persona)


if __name__ == "__main__":
    main()
