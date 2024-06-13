import os
import streamlit as st
from dotenv import load_dotenv

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call(["pip", "install", "python-dotenv"])
    from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# # Function to check login credentials
def authenticate(username, password):
    # Define hardcoded credentials
    # CORRECT_USERNAME = secrets["username"]
    # CORRECT_PASSWORD = secrets["password"]
    # CORRECT_USERNAME = "soj"
    # CORRECT_PASSWORD = "soj"
    CORRECT_USERNAME = os.getenv('USERNAME')
    CORRECT_PASSWORD = os.getenv('PASSWORD')

    # Print the loaded credentials for debugging
    st.write(f"Correct Username from .env: {CORRECT_USERNAME}")
    st.write(f"Correct Password from .env: {CORRECT_PASSWORD}")

    return username == CORRECT_USERNAME and password == CORRECT_PASSWORD

# Function to check login credentials
# def authenticate(username, password):
#     return username == os.environ["username"] and password == os.environ["password"]

# Main function for the login page
def login():    
    st.markdown("""
        <style>
            .reportview-container {margin-top: -2em;}
            .st-emotion-cache-1jicfl2 {padding: 2rem 3rem 10rem;}
            h1#login-to-your-app, h1#student-atendance-report {text-align: center;}
            header #MainMenu {visibility: hidden; display: none;}
            .stActionButton {visibility: hidden; display: none;}
            # .stDeployButton {display:none;}
            footer {visibility: hidden;}
            stDecoration {display:none;}
            .stTabs button {margin-right: 50px;}
            .st-emotion-cache-15ecox0, .viewerBadge_container__r5tak, .styles_viewerBadge__CvC9N {display: none;}
            p.credits {user-select: none; filter: opacity(0);}
        </style>
    """, unsafe_allow_html=True)

    
    st.markdown("<p class='credits'>Made by <a href='https://github.com/sojith29034'>Sojith Sunny</a></p>", unsafe_allow_html=True)
    st.title("Login to Your App")
    
    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # try:
    #     secrets = {
    #         "username": st.secrets["login"]["username"],
    #         "password": st.secrets["login"]["password"]
    #     }
    # except KeyError:
    #     st.error("Could not find secrets. Please make sure they are added to Streamlit Cloud app settings.")
    #     return

    # try:
    #     credentials = {
    #         "username": st.secrets["username"],
    #         "password": st.secrets["password"]
    #     }
    # except KeyError:
    #     st.error("Could not find secrets. Please make sure they are added to Streamlit Cloud app settings.")
    #     return
    
    # os.environ["username"] == st.secrets["username"]
    # os.environ["password"] == st.secrets["password"]
    
    # Check if login button is clicked
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password. Please try again.")

def main():
    if st.session_state.logged_in:
        import index
        index.run_main_app()
    else:
        login()

if __name__ == "__main__":
    main()
