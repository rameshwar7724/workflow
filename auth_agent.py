import streamlit as st
import os

def github_login():
    """Handles GitHub authentication."""
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    auth_url = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&scope=repo"
    st.write("## Step 1: GitHub Authentication")
    st.markdown(f"[Login with GitHub]({auth_url})")
