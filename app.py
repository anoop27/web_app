import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import streamlit as st

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status is None:
    st.warning('Please enter your username and password')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status:
    st.sidebar.title(f'Welcome {name}')  # Display welcome message in sidebar
    authenticator.logout('Logout', 'sidebar')
        
    # Define the URLs of your HTML files
    html_urls = [
        "https://anoop27.github.io/sales_analysis/sheet1.html",
        "https://anoop27.github.io/sales_analysis/sheet2.html",
        "https://anoop27.github.io/sales_analysis/sheet3.html",
        "https://anoop27.github.io/sales_analysis/sheet4.html",
        "https://anoop27.github.io/sales_analysis/sheet5.html",
        "https://anoop27.github.io/sales_analysis/sheet6.html"
    ]


     # Set initial selected_sheet
    selected_sheet = 1

    # Sidebar to toggle between sheets
    st.sidebar.title("Select a graph")

    # Create radio buttons for each sheet
    selected_sheet = st.sidebar.radio("", ["Product Sales", "Revenue", "Frequency of transactions", "Price vs. Quantity", "Yearly sales", "Monthly sales"])

    # Map the selected sheet to its index
    sheet_mapping = {
        "Product Sales": 1,
        "Revenue": 2,
        "Frequency of transactions": 3,
        "Price vs. Quantity": 4,
        "Yearly sales": 5,
        "Monthly sales": 6
    }

    # Get the selected sheet index
    selected_sheet_index = sheet_mapping[selected_sheet]

    # Embed the selected HTML file
    st.markdown(f'<iframe src="{html_urls[selected_sheet_index - 1]}" style="width: 100%; height: 80vh; border: none;"></iframe>', unsafe_allow_html=True)
