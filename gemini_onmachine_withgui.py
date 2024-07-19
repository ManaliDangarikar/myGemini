import tkinter as tk
import google.generativeai as genai
import os

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)    

# model = genai.GenerativeModel('gemini-1.5-flash')
model = genai.GenerativeModel('gemini-1.0-pro')

def get_answer():
    question = question_entry.get("1.0", tk.END).strip()
    if question:
        response = model.generate_content(question)
        answer_text.set(response.text)

# Create the main window
root = tk.Tk()
root.title("Ask Me Anything!")

# Create a text entry for the question
question_label = tk.Label(root, text="Enter your question:")
question_label.pack(pady=5)
question_entry = tk.Text(root, height=4, width=50)
question_entry.pack(pady=5)

# Create a button to submit the question
submit_button = tk.Button(root, text="Get Answer", command=get_answer)
submit_button.pack(pady=5)

# Create a text area to display the answer
answer_label = tk.Label(root, text="Answer:")
answer_label.pack(pady=5)
answer_text = tk.StringVar()
answer_display = tk.Label(root, textvariable=answer_text, wraplength=400, justify="left")
answer_display.pack(pady=5)

# Run the application
root.mainloop()
