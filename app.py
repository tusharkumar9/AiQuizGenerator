from flask import Flask, render_template, request
from groq import Groq
import os

app = Flask(__name__)

# Load Groq API key from environment variable (Hugging Face Secrets)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_quiz(topic, num_questions):
    try:
        prompt = f"""
        Generate {num_questions} multiple choice questions on {topic}.

        Format:
        Question
        A)
        B)
        C)
        D)

        Correct Answer:
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating quiz: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form["topic"]
    num_questions = int(request.form["num_questions"])

    quiz = generate_quiz(topic, num_questions)

    return render_template("result.html", quiz=quiz)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)