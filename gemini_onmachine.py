import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import os

def format_markdown(text):
    text = text.replace('*', '')
    text = textwrap.indent(text, '  ', predicate=lambda line: not line.startswith('>'))
    return text

GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

# Generate text from text inputs
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Why is the sky blue?")

print(format_markdown(response.text))