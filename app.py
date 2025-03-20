import streamlit as st
import os
from dotenv import load_dotenv
from auth_agent import github_login
from project_agent import get_project_details
from create_repo_agent import create_github_repo
from save_project_agent import save_project_details

# Load environment variables
load_dotenv()

st.title("Multi-Agent GitHub Project Creator")

# Authentication
github_login()

# Get project details
repo_name, description, private = get_project_details()
if st.button("Create Repository"):
    repo_url = create_github_repo(repo_name, description, private)
    if repo_url:
        save_project_details(repo_name, description, repo_url)
        st.success(f"Repository created successfully! [View Repo]({repo_url})")
    else:
        st.error("Failed to create repository.")
