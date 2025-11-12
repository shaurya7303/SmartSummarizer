Text Summarizer App

A simple yet powerful AI-powered web app that takes any news article or blog post and summarizes it into 3 concise sentences — built using Hugging Face Transformers, Stramlit.
<img width="1697" height="881" alt="Screenshot 2025-10-05 234934" src="https://github.com/user-attachments/assets/c5700933-ac21-4745-8465-b6654ac243e9" />


 Motivation

This project was built to showcase effort, creativity, and curiosity in building something AI-powered from scratch — not perfection. I wanted to see how far I could go by combining public AI tools, documentation, and experimentation to build a working product within a short time.

Even though it’s simple, this project helped me learn:

How to integrate Hugging Face models in a Python backend.

How to deploy AI apps using free platforms like Hugging Face Spaces.

How to design a user-friendly Gradio interface for text processing tasks.

 What It Does

Takes any text input (like a blog or news article).

Automatically summarizes it into 3 meaningful sentences using a Transformer model.

Displays both original text and AI summary instantly.

 Tech Stack

Python 3.10+

Transformers (Hugging Face) — pre-trained summarization model.

Streamlit

Flask (optional) — for backend deployment.

Render / Hugging Face Spaces — for free deployment.

 Installation

Clone this repository and install dependencies:

git clone https://github.com/<your-username>/text-summarizer.git
cd text-summarizer
pip install -r requirements.txt


Run the app locally:

python app.py


It will open automatically in your browser! 

 Example

Input:

“Artificial Intelligence is transforming industries by automating complex tasks, enabling data-driven decisions, and unlocking new possibilities for creativity and efficiency.”

Output Summary:

“AI is revolutionizing industries through automation and intelligent insights. It enables better decision-making and boosts innovation. This marks a major shift in how technology impacts society.”

 Deployment

You can run this project for free using:

Hugging Face Spaces
 (recommended)

Render.com (simple Flask app deployment)

To deploy on Hugging Face Spaces:

Create a new Space.

Choose Gradio as the SDK.

Upload your files (app.py, requirements.txt, README.md).

Hit Deploy 

 Extra Effort

Added error handling for empty text.

Used a fine-tuned summarization model from Hugging Face (facebook/bart-large-cnn).

Kept the UI clean, minimal, and beginner-friendly.

Documented my process and reasoning clearly .

 What I Learned

How to read and use Hugging Face model documentation.

How to structure a simple AI project for deployment.

That even small projects can teach a lot when done with purpose.

Future Improvements

Add a feature for multi-length summaries (short / medium / long).

Allow URL-based article fetching.

Support for multiple languages using translation models.

 Acknowledgments

Special thanks to Hugging Face, Gradio, and OpenAI for making it possible for learners to build real AI projects without needing big compute power.

 Author

Shaurya Singh
AI Developer | ML Enthusiast | Always Learning
