import os
from typing import List, Literal
import openai 
from openai.openai_object import OpenAIObject


class TranslationEngine:
    def __init__(
            self, 
            languages: List[str], 
            engine = Literal["OpenAi", "Google"]
        ) -> None:

        self.languages = languages
        self.engine = engine

        if self.engine == "OpenAi":
            self.api_key = os.getenv("OPENAI_API_KEY")
            openai.api_key = self.api_key

        if self.engine == "Google":
            raise NotImplementedError("Google translation engine not implemented yet.")

    @staticmethod
    def _process_openai_response(response: OpenAIObject) -> str:
        """Processes openai chat response and saves message output as string."""

        response_dict: dict = response.to_dict_recursive()
        response_choice: dict[str: dict] = response_dict.get("choices", {})[0]
        return response_choice.get("message", {}).get("content", None)

    def get_openai_response(self, context: str, prompt: str, **kwargs) -> str:
        """Query openai api for chat response based on provided context, prompt and extra kwargs."""

        response: OpenAIObject = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt},
            ],
            **kwargs
            )
        return self._process_openai_response(response)
    
    def translate_with_openai(self, text: str, target_language):
        # Set up the context for translation
        context = f"Translate the following English text to {target_language}:"
        
        # Call the OpenAI API
        translated_text = self.get_chat_response(context, text)
        return translated_text