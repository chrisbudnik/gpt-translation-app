import streamlit as st
import os
import time
import hmac
from config import Config
from languages import SupportedLanguages
from translation_engine import TranslationEngine
from database import check_latest_campaigns, save_translations_to_bigquery


def translation_page():
    st.title("Translate Sales Copy")
    st.write("Quickly translate your marketing copy using advanced LLMs.")

    col1, col2 = st.columns(2)

    # Choose languages to translate to
    supported_countries = SupportedLanguages.REFERENCE.keys()
    with col1:
        selected_countries = st.multiselect("Choose country languages", supported_countries)

    # Choose translation engine
    with col2:
        engine = st.selectbox("Choose translation engine", ["OpenAI", "Google"])

    extra_options = st.checkbox("Extra Options")

    # Select extra options
    mode = "default"
    if extra_options:
        mode = st.selectbox("Mode", ["Creative", "Reserved", "Technical"])

    # Provide text for translation
    text = st.text_area("Input your text here:")

    # Set up translation engine and options
    translation_engine = TranslationEngine(selected_countries, engine)

    if st.button("Translate"):
        if not text:
            st.warning("Please enter some text to translate.")
        
        translations: dict = translation_engine.generate_translations(text)

        for header, translation in translations.items():
            with st.expander(header):
                st.write(translation)

def upload_page():
    st.title("Upload to Database")
    st.write("Upload your marketing copy to database.")


    campaign_name = st.text_input("Enter campaign name")

    if st.toggle("Check lates campaign name"):
        if st.button("Check"):
            campaign_name_suggestion = check_latest_campaigns()
            st.write(f"Lates campaign found: {campaign_name_suggestion}")


    supported_countries = SupportedLanguages.REFERENCE.keys()
    selected_countries = st.multiselect("Choose country languages for upload", supported_countries)

    sales_copy_upload = {}
    for country in selected_countries:
        language = SupportedLanguages.REFERENCE.get(country)
        st.write(f"Upload copy for {country} ({language})")

        sales_copy_upload[country] = st.text_area(f"{language}")

    #Formating helper
    if st.toggle("Preview export JSON data"):
        st.write(sales_copy_upload)

    if not user_token:
        st.warning("Please enter your user token to preceed with upload.")
        st.stop()

    # Upload to database
    if st.button("Upload"):
        # Check if all fields are filled
        if not selected_countries:
            st.warning("Please select countries to upload.")
            st.stop()

        if not all(sales_copy_upload.values()):
            st.warning("Enter sales copy for all countries before uploading.")
            st.stop()

        with st.status("Uploading data...", expanded=True):
            st.write("Checking access policy...")
            time.sleep(1)

            st.write("Uploading to database...")

            save_translations_to_bigquery(
                campaign_name=campaign_name, 
                translations_upload=sales_copy_upload,
                token=user_token,
                details=sales_copy_upload
            )

        st.success("Data successfully uploaded.")

# Page config
st.set_page_config(
    page_title='marketing automation', 
    )

# Transform into get environment variable GLOBAL_PASSWORD
password = os.getenv("GLOBAL_PASSWORD")

# Check password func with state management
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], password):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

# Do not continue if check_password is not True.
if not check_password():
    st.stop() 

# UI definitions
    
# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to page:", ['Create Translation', 'Upload to Database'], index=0)

user_token = st.sidebar.text_input("Enter your user token", type="password", help="Required for interacting with the database.")

# Page dispatching
if page == 'Create Translation':
    translation_page()
elif page == 'Upload to Database':
    upload_page()
