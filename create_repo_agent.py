import os
import requests

def create_github_repo(repo_name: str, description: str, private: bool):
    """Creates a new GitHub repository."""
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    headers = {"Authorization": f"token {access_token}"}
    payload = {"name": repo_name, "description": description, "private": private}
    response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
    if response.status_code == 201:
        return response.json().get("html_url")
    return None
