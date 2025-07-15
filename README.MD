# 🤖 AI To-Do Assistant with LangChain & Gemini

An AI-powered assistant that can add, remove, and list to-do items via natural language. Built using Python (LangChain + Gemini), FastAPI, and a minimal JS frontend.

---

## 🔧 Architecture Diagram

```text
User
 ↓ (prompt)
Frontend (index.html)
 ↓ (POST)
FastAPI backend (main.py)
 ↓
LangChain Agent (agent.py)
 ↓
Custom Tools (tools.py)
```

---

## 🧠 Memory Management

We use LangChain’s `ConversationBufferMemory`, which:

* Stores the full conversation history
* Is passed to the agent to maintain context between user interactions
* Example:

```python
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
```

---

## 🛠️ Tool Registration

Tools are functions registered like this:

```python
from langchain.agents import Tool

tools = [
    Tool(name="add_todo", func=add_todo, description="Add an item to to-do list"),
    Tool(name="list_todos", func=list_todos, description="List all to-do items"),
    Tool(name="remove_todo", func=remove_todo, description="Remove a to-do item"),
]
```

These tools are then passed to the agent using `initialize_agent()`:

```python
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)
```

---

## 🚀 Setup & Run Instructions

### 📦 1. Clone and Install

```bash
git clone https://github.com/your-username/ai-todo-agent.git
cd ai-todo-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🔐 2. Setup Environment

Create a `.env` file:

```
GOOGLE_API_KEY=your-valid-gemini-api-key
```

> Make sure the key is valid and not expired.

### 🧠 3.  Run Everything

```bash
chmod +x run.sh
./run.sh

```

## 💬 Example Prompts

* `Add buy milk to my to-do list`
* `List all to-do items`
* `Remove buy milk from my list`
* `exit`

---

## 📁 Folder Structure

```
ai-todo-agent/
├── main.py
├── agent.py
├── tools.py
├── index.html
├── .env.example
├── requirements.txt
└── README.md
```

---

