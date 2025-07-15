from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import add_todo, list_todos, remove_todo
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key directly from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Create LLM instance with explicit API key
# agent.py (updated model name)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  
    temperature=0.3,
    google_api_key=api_key
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    Tool(name="add_todo", func=add_todo, description="Add an item to to-do list"),
    Tool(name="list_todos", func=list_todos, description="List all to-do items"),
    Tool(name="remove_todo", func=remove_todo, description="Remove a to-do item"),
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)