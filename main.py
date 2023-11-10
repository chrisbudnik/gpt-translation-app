import streamlit as st
import time
from languages import SupportedLanguages
from translation_engine import TranslationEngine

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
    st.title("Upload Sales Copy")
    st.write("Upload your marketing copy to database.")

    supported_countries = SupportedLanguages.REFERENCE.keys()
    selected_countries = st.multiselect("Choose country languages for upload", supported_countries)

    sales_copy_upload = {}
    for country in selected_countries:
        language = SupportedLanguages.REFERENCE.get(country)
        st.write(f"Upload copy for {country} ({language})")

        sales_copy_upload[country] = st.text_area(f"{language}")

    if st.button("Upload"):
        if not sales_copy_upload.values():
            st.warning("Please select countries and enter sales copy to upload.")

        with st.status("Uploading data...", expanded=True):
            st.write("Searching for data...")
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)

        st.success("Data successfully uploaded.")

    #Formating helper
    st.write(sales_copy_upload)




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
