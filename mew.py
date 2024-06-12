import streamlit as st

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
            st.success("Login successful! Redirecting to main app...")
            # Redirect to main app
            # Replace 'main_app_url' with the URL of your main app
            st.experimental_set_query_params(login=True)
        else:
            st.error("Invalid username or password. Please try again.")

def main():
    if "login" not in st.query_params:
        login()
    else:
        # Redirect to main app
        st.title("Main App")
        st.write("Welcome to the main app!")

if __name__ == "__main__":
    main()
