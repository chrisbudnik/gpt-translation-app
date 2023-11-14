import os
import streamlit as st


class Config:
    """Configuration class for the marketing translator app."""

    SERVICE_NAME = "marketing-translator"
    AUTH_SERVICE_URL = "https://my-custom-auth-service.com/grant_access"
    AUTH_VALIDATION_ON = False # turned of for testing purposes
    BIGQEURY_MARKETING_TABLE_ID = "chris-sandbox-2023.apps.marketing_translations"


    def __init__(self) -> None:
        """Perform configuration checks."""

        if not os.getenv("OPENAI_API_KEY"):
            st.error("Please set your OPENAI_API_KEY environment variable.")
        
        if not os.getenv("GLOBAL_PASSWORD"):
            st.error("Please set your GLOBAL_PASSWORD environment variable.")

        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            st.error("Please set your GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        