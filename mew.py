import streamlit as st

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Define hardcoded credentials
CORRECT_USERNAME = "soj"
CORRECT_PASSWORD = "soj"

# Function to check login credentials
def authenticate(username, password):
    return username == CORRECT_USERNAME and password == CORRECT_PASSWORD

# Main function for the login page
def login():
    st.title("Login to Your App")
    
    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
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
