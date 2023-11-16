from enum import Enum

class PromptTemplate:
    BASIC = "Translate the following English text to {target_language}:"

    MARKETING = """You are an experianced marketing expert. Translate the following English text to {target_language}. 
    Don't focus to much on the literal translation, but rather on the meaning and the feeling of the text. Text to translate:"""