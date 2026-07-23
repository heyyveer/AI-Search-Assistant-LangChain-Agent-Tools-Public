# 🤖 AI Search Assistant

An AI-powered web search chatbot built with **LangChain**, **Groq**, **You.com Search API**, and **Streamlit**. The application can answer both general knowledge and real-time web search queries through an intuitive chat interface.

---

## 🚀 Features

* 🔍 Real-time web search using You.com Search API
* 🤖 AI-powered responses with Groq's GPT-OSS-20B model
* 💬 ChatGPT-style conversation interface
* 📝 Persistent conversation history during the session
* ⚡ Fast inference using Groq
* 🌐 Streamlit web application
* 🔧 Easy deployment on Streamlit Community Cloud

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* LangGraph Agent
* Groq API
* You.com Search API
* Python Dotenv

---

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git

cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
YDC_API_KEY=your_you_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🌍 Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app from your repository.
4. Set the main file as:

```
app.py
```

5. Add your API keys in **Secrets**:

```toml
GROQ_API_KEY = "your_groq_api_key"
YDC_API_KEY = "your_you_api_key"
```

6. Deploy.

---

## 💡 Example Questions

* What are today's AI news headlines?
* Explain Retrieval-Augmented Generation (RAG).
* Who won the latest Wimbledon championship?
* Summarize the latest developments in Python.
* Compare LangChain and LangGraph.

---

## 📦 Dependencies

* streamlit
* langchain
* langchain-groq
* langchain-youdotcom
* python-dotenv

Install them with:

```bash
pip install -r requirements.txt
```

---

## 📸 Demo

Add screenshots or a GIF of the application here.

```
assets/demo.png
```

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* LangChain
* LangGraph
* Groq
* You.com Search
* Streamlit
