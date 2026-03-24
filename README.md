# 🤖 AI Quiz Generator (Flask + Groq)

An AI-powered quiz generator web application that creates multiple-choice questions on any topic using the Groq API and LLaMA model.

---

## 🚀 Features

* Generate quizzes on any topic
* Choose number of questions
* Uses AI (LLaMA model via Groq)
* Clean and simple web interface
* Fast and lightweight Flask backend

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **AI API:** Groq (LLaMA 3.3 70B model)
* **Environment Management:** python-dotenv

---

## 📂 Project Structure

```
ai-quiz-generator-python/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env (not included in repo)
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
└── venv/ (not included)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/tusharkumar9/AiQuizGenerator.git

```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

🔑 Get your API key from Groq website.

---

### 5️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:7860
```

---



---

## 📄 requirements.txt

Generate it using:

```bash
pip freeze > requirements.txt
```

---

## 🧠 How It Works

1. User enters topic & number of questions
2. Flask sends prompt to Groq API
3. AI generates MCQs
4. Results are displayed on the webpage

---



## 👨‍💻 Author

Developed by **TUSHAR KUMAR**
Feel free to connect and contribute 🚀
Gmail : tusharkumarofficial9@gmail.com


---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
