import os

def get_github_token():
    """Retrieves the GitHub access token from environment variables."""
    return os.getenv("GITHUB_ACCESS_TOKEN")
