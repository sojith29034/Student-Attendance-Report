import streamlit as st

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# # Function to check login credentials
# def authenticate(username, password):
#     # Define hardcoded credentials
#     # CORRECT_USERNAME = secrets["username"]
#     # CORRECT_PASSWORD = secrets["password"]
#     CORRECT_USERNAME = "soj"
#     CORRECT_PASSWORD = "soj"
#     return username == CORRECT_USERNAME and password == CORRECT_PASSWORD

# Function to check login credentials
def authenticate(username, password, credentials):
    return username == credentials["username"] and password == credentials["password"]

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

    try:
        credentials = st.secrets["login"]
    except KeyError:
        st.error("Could not find secrets. Please make sure they are added to Streamlit Cloud app settings.")
        return
    
    # Check if login button is clicked
    if st.button("Login"):
        if authenticate(username, password, credentials):
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
