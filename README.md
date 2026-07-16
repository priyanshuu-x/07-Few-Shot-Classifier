# 🧠 Few-Shot Intent Classifier

A simple intent classifier built with **LangChain** and **Ollama** using **Few-Shot Prompting**. The model classifies customer messages into predefined categories without any model training.

## 📸 Demo

<p align="center">
  <img src="image/output.png" alt="Demo" width="800">
</p>

## 🚀 Features

- Few-Shot Prompting
- Intent Classification
- LangChain
- Ollama (Llama 3.2)
- Interactive CLI

## 🛠️ Tech Stack

- Python
- LangChain
- Ollama
- Llama 3.2

## 📂 Project Structure

```text
07-Few-Shot-Classifier/
├── image/
│   └── output.png
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/07-Few-Shot-Classifier.git
cd 07-Few-Shot-Classifier

pip install -r requirements.txt
ollama pull llama3.2

python main.py
```

## ⭐ Example

```text
Customer message: My order arrived damaged.
Predicted label: complaint

Customer message: What are your store hours?
Predicted label: question

Customer message: Amazing service!
Predicted label: praise
```

---
Give the repository a ⭐ if you found it useful.
