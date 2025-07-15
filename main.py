# # main.py

# from agent import agent

# def chat_loop():
#     print("🤖 Welcome to your AI To-Do Assistant!")
#     print("Type 'exit' to quit.\n")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Goodbye!")
#             break
#         response = agent.run(user_input)
#         print("Agent:", response)

# if __name__ == "__main__":
#     chat_loop()
# # main.py (with error handling)
# def chat_loop():
#     print("🤖 Welcome to your AI To-Do Assistant!")
#     print("Type 'exit' to quit.\n")
#     while True:
#         try:
#             user_input = input("You: ")
#             if user_input.lower() in ["exit", "quit"]:
#                 print("Goodbye!")
#                 break
#             response = agent.run(user_input)
#             print("Agent:", response)
#         except Exception as e:
#             print(f"⚠️ Error: {str(e)}")
#             print("Please try again or type 'exit' to quit\n")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str

@app.post("/chat")
def chat(user_input: UserInput):
    result = agent.invoke({"input": user_input.message})
    return {"response": result["output"]}  # ✅ clean, final response only
