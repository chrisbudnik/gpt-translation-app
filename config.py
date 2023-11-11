import os
import streamlit as st

class Config:

    SERVICE_NAME = "marketing-translator"
    BIGQEURY_MARKETING_TABLE_ID = "chris-sandbox-2023.apps.marketing_translations"



    def __init__(self) -> None:
        """Perform configuration checks."""

        if not os.getenv("OPENAI_API_KEY"):
            st.error("Please set your OPENAI_API_KEY environment variable.")

        #TODO: add google vertex ai credentials?
        
        if not os.getenv("GLOBAL_PASSWORD"):
            st.error("Please set your GLOBAL_PASSWORD environment variable.")

        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            st.error("Please set your GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        