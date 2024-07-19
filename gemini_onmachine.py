import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import os

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return textwrap.indent(text, '> ', predicate=lambda _: True)

def format_markdown(text):
    text = text.replace('•', '  *')  # Convert bullet points to markdown format
    text = textwrap.indent(text, '  ', predicate=lambda line: not line.startswith('>'))
    return text

# Used to securely store your API key
# from google.colab import userdata

GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

Generate text from text inputs

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Why is the sky blue?")

print(response.text)

# formatted_response = format_markdown(response.text)
# print(formatted_response)
# print(to_markdown(response.text))

# response.prompt_feedback