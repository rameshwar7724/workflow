def save_project_details(repo_name, description, repo_url):
    """Saves project details to a local file."""
    with open("projects.txt", "a") as f:
        f.write(f"{repo_name} | {description} | {repo_url}\n")
