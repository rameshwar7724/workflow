# Multi-Agent GitHub Project Creator

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi_agent_github.git
   cd multi_agent_github
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up GitHub OAuth credentials:
   - Go to [GitHub Developer Settings](https://github.com/settings/developers)
   - Register an OAuth app and get:
     - **Client ID**
     - **Client Secret**
   - Create a `.env` file:
     ```
     GITHUB_CLIENT_ID=your_client_id
     GITHUB_CLIENT_SECRET=your_client_secret
     GITHUB_ACCESS_TOKEN=your_access_token
     ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   
