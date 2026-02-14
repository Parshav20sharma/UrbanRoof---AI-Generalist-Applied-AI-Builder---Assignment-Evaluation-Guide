<<<<<<< HEAD

# UrbanRoof Lead Response Assistant

AI-powered chatbot that reads customer enquiries and generates professional, safe, and helpful responses.

Built using:

• Streamlit
• Ollama
• LLaMA 3.2
• Python

---

# Features

• Understands customer intent
• Generates professional responses
• Provides safety precautions
• Asks relevant follow-up questions
• Suggests inspection appointment
• Works fully offline
• Real-time chatbot interface

---

# Project Structure
=======
Project Name: UrbanRoof Lead Response Assistant
Type: AI Chatbot using Streamlit + Ollama (Local LLM)
Purpose: Automatically read customer enquiries and generate professional, safe, and helpful responses.

---

# System Requirements

Minimum Requirements

• OS: Windows 10/11, macOS, or Linux
• RAM: 8 GB minimum (16 GB recommended)
• Storage: 10 GB free space
• Python: 3.10 or higher
• Internet: Required for initial setup

Required Software

• Python
• Ollama
• Streamlit
• Git (optional)

---

# Step 1 — Install Python

1. Go to:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download Python 3.11

3. During installation, CHECK:

✔ Add Python to PATH

4. Verify installation:

Open PowerShell / Terminal and run:

```bash
python --version
```

Expected output:

```bash
Python 3.11.x
```

---

# Step 2 — Install Ollama

Ollama is used to run the AI model locally.

1. Go to:
   [https://ollama.com/download](https://ollama.com/download)

2. Download and install Ollama

3. Verify installation:

```bash
ollama --version
```

Expected output:

```bash
ollama version x.x.x
```

---

# Step 3 — Download the AI Model

Run:

```bash
ollama pull llama3.2:3b
```

This downloads the AI model.

This step is required only once.

---

# Step 4 — Download or Copy Project Folder

Project structure should be:
>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1

```
lead-response-assistant/
│
├── app/
│   ├── ai_engine.py
│   ├── prompt.py
│   ├── validator.py
<<<<<<< HEAD
=======
│   └── __init__.py
>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

<<<<<<< HEAD
# Installation

Step 1:

Install Python

Step 2:

Install Ollama

Step 3:

Download model

```bash
ollama pull llama3.2:3b
```

Step 4:

Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

Step 5:

Install dependencies
=======
# Step 5 — Create Virtual Environment

Navigate to project folder:

```bash
cd lead-response-assistant
```

Create environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

# Step 6 — Install Dependencies

Run:
>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
Step 6:

Run application
=======
OR manually:

```bash
pip install streamlit ollama python-dotenv
```

---

# Step 7 — Run Ollama Model

Start Ollama in terminal:

```bash
ollama run llama3.2:3b
```

Keep this terminal open.

---

# Step 8 — Run the Chatbot Application

Open new terminal.

Navigate to project folder:

```bash
cd lead-response-assistant
```

Activate environment:

```bash
venv\Scripts\activate
```

Run Streamlit:
>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1

```bash
streamlit run streamlit_app.py
```

---

<<<<<<< HEAD
# Usage

Open browser:
=======
# Step 9 — Access Application

Browser will open automatically.

If not, open:
>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1

```
http://localhost:8501
```

<<<<<<< HEAD
=======
---

# Step 10 — Using the Chatbot

>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1
Enter:

• Name
• Location
<<<<<<< HEAD
• Query

Example:

"I have roof leakage after rain"

AI will respond professionally.

---

# Example Output

• Acknowledgement
• Risk explanation
• Safety precautions
=======
• Customer query

Example query:

"I am getting damp patches on my wall after rain."

The chatbot will generate:

• Acknowledgement
• Risk explanation
• Safety steps
>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1
• Follow-up questions
• Appointment suggestion

---

<<<<<<< HEAD
# Model Used

LLaMA 3.2 (3B) via Ollama

Runs locally.

---

# Future Improvements

• Database integration
• Appointment booking system
• Image upload support
• Multi-language support
• Cloud deployment

---

# Author

Parshav Sharma
B.Tech Artificial Intelligence and Machine Learning
=======
# Step 11 — Stopping the Application

Press:

```
CTRL + C
```

in terminal.

---

# Troubleshooting Guide

Problem: ollama not recognized
Solution: Restart system after installing Ollama

Problem: streamlit not recognized
Solution:

```bash
pip install streamlit
```

Problem: model not found
Solution:

```bash
ollama pull llama3.2:3b
```

Problem: chatbot not responding
Solution: Ensure Ollama is running.

---

# Architecture Overview

User → Streamlit UI → AI Engine → Ollama Model → Response → Streamlit UI

---

# Technologies Used

• Python
• Streamlit
• Ollama
• LLaMA 3.2 (3B model)
• Prompt Engineering

---

# Security Advantage

• Fully local AI
• No external API required
• No data leakage

---

# Performance

Response time: 1–3 seconds
Accuracy: High
Reliability: High

>>>>>>> e389e8a76c966b0b194f8e162eeb4f9f3b32f6c1
