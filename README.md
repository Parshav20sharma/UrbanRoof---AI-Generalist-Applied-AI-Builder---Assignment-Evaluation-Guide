# UrbanRoof – Option B - AI Lead Response Assistant

AI Generalist | Applied AI Builder – Assignment Submission

Submitted By:
PARSHAV SHARMA
Email: [20sharmaparshav@gmail.com](mailto:20sharmaparshav@gmail.com)

---

## Project Overview

This project is an AI-powered Lead Response Assistant built as part of the AI Generalist | Applied AI Builder Assignment (Option B – Lead Response Assistant).

The system reads customer enquiries and generates professional, safe, and helpful responses in a chatbot format.

The assistant is designed to:

* Understand customer intent
* Acknowledge the issue professionally
* Ask relevant follow-up questions
* Provide safe precautions
* Avoid hallucinated or false claims
* Recommend scheduling an inspection when appropriate
* Work as a real-time chatbot

This project uses a local LLM via Ollama (llama3.2:3b) and Streamlit for the user interface.

---

## Features

* Real-time chatbot interface
* Professional and structured responses
* Intent detection (problem, service inquiry, general inquiry)
* Safe and reliable output
* Runs completely locally (no paid API required)
* Privacy-friendly (no external data sharing)

---

## Technology Stack

* Python 3.10+
* Streamlit (UI)
* Ollama (Local LLM runtime)
* Llama 3.2 (3B model)
* Prompt engineering
* Modular architecture

---

## Project Structure

```
lead-response-assistant/
│
├── app/
│   ├── __init__.py
│   ├── ai_engine.py
│   ├── prompt.py
│   └── validator.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
```

---

## System Requirements

Before running this project, install:

* Python 3.10 or higher
* Ollama

Download Ollama from:
https://ollama.com/download

Install and verify:

```
ollama --version
```

---

## Step-by-Step Installation Guide

Follow these steps carefully.

---

### Step 1: Clone the Repository

```
git clone https://github.com/Parshav20sharma/UrbanRoof---AI-Generalist-Applied-AI-Builder---Assignment-Evaluation-Guide.git

cd UrbanRoof---AI-Generalist-Applied-AI-Builder---Assignment-Evaluation-Guide/lead-response-assistant
```

---

### Step 2: Create Virtual Environment

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 4: Install and Pull AI Model

Run:

```
ollama pull llama3.2:3b
```

Wait until the model downloads completely.

---

### Step 5: Start Ollama Server

Run:

```
ollama serve
```

Keep this terminal open.

---

### Step 6: Run the Application

Open a new terminal in the project folder and run:

```
streamlit run streamlit_app.py
```

---

### Step 7: Open in Browser

Streamlit will open automatically.

If not, open manually:

```
http://localhost:8501
```

---

## How to Use the Application

1. Enter your Name
2. Enter your Location
3. Type your issue or question

Example:

```
Hi, I am getting damp patches on my bedroom wall after rain. What should I do?
```

The AI assistant will:

* Acknowledge your issue
* Explain possible risks
* Ask relevant questions
* Suggest safety precautions
* Recommend scheduling inspection

You can continue chatting in the same conversation.

---

## Example Use Cases

Customer Issues:

* Damp walls
* Water leakage
* Roof cracks
* Waterproofing problems

General Questions:

* Services offered
* Inspection process
* Maintenance guidance

---

## How the System Works

Flow:

User Input → Prompt Engineering → Ollama LLM → Response Validation → Professional Output → Chat UI

Modules:

ai_engine.py
Handles AI model communication

prompt.py
Controls response format and behavior

validator.py
Ensures safe and structured responses

streamlit_app.py
Provides chatbot interface

---

## Safety and Reliability

The assistant is designed to:

* Avoid false claims
* Avoid unsafe recommendations
* Ask clarification questions
* Provide only general guidance
* Recommend professional inspection when needed

---

## Limitations

* Uses local model (limited compared to large cloud models)
* Does not access real inspection data
* Provides guidance, not final diagnosis

---

## Future Improvements

* Integration with company database
* Appointment booking system
* Image upload support
* Cloud deployment
* Better intent classification

---

## Assignment Objective – Completed

This project successfully demonstrates:

* AI workflow design
* Prompt engineering
* Chatbot implementation
* Reliable AI response generation
* Real-world applied AI solution

---

## Contact

PARSHAV SHARMA
Email: [20sharmaparshav@gmail.com](mailto:20sharmaparshav@gmail.com)


