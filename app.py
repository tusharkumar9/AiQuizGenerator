from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

# Groq API
client = Groq(api_key="GROQ_API_KEY")

def generate_quiz(topic, num_questions):
    prompt = f"Generate {num_questions} MCQ questions on {topic} with 4 options and correct answer."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form["topic"]
    num_questions = request.form["num_questions"]

    quiz = generate_quiz(topic, num_questions)

    return render_template("result.html", quiz=quiz)


if __name__ == "__main__":
    app.run(debug=True)