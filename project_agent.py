import streamlit as st

def get_project_details():
    """Gets project details from user input."""
    repo_name = st.text_input("Enter repository name:")
    description = st.text_area("Enter description:")
    private = st.checkbox("Private repository", value=True)
    return repo_name, description, private
