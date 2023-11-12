# Marketing Automation Tool
*Automated sales copy translation and database upload*

## 🔍 Project Overview

The Marketing Copy Translation and Upload Tool is designed to streamline the process for marketers and copywriters to translate and upload their marketing content into a database. This tool stands out with its integration of advanced language models for translation and a user-friendly interface developed using Streamlit.

## 🛠️ Key Functionalities

#### Translation of Marketing Copy

- **Language Selection**: Users can choose from a list of multiple target languages for translation.
- **Translation Engine Choice**: Flexibility to select between different translation engines like OpenAI and Google.
- **Mode Options**: Additional options for translation modes such as Creative, Reserved, and Technical.
- **Input and Translation Display**: A dedicated area for inputting marketing copy and a display section showing translations for each selected language.

#### Uploading Translations to Database

- **Campaign Management**: Facility to input a campaign name and check existing campaign names.
- **Language-Specific Uploads**: Capability to upload marketing copies for each selected language.
- **Preview of Export Data**: Users can review the JSON format of the data before uploading.
- **Database Upload**: Secure upload feature with user authentication token verification.

#### User Interface and Navigation

- **Password Protected Access**: The tool is secured with password-based access.
- **Streamlit Based UI**: An intuitive sidebar for navigation, including interactive elements like multiselect, text inputs, and buttons.
- **Status and Error Handling**: Provides real-time status updates and displays error messages for enhanced user interaction.

### Additional Features

- **Environment Variable Integration**: Utilizes environment variables for managing sensitive data like global passwords.
- **Session State Management**: Efficiently manages user sessions for password verification and token inputs.

### Code Highlights

- **Streamlit Integration**: Utilizes Streamlit for crafting interactive web-based interfaces.
- **Language Model and Database Integration**: Incorporates language models and database connectivity for real-time translation and data handling.
- **Security**: Implements secure password and token management using environment variables and session states.
