import os
from google import genai
from google.genai import types
from dotenv import load_dotenv         

def start_chat():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3.1-flash-lite-preview" #  model version
    
    config = types.GenerateContentConfig(
        system_instruction="""You will be receiving a fast food order from the user. 
        Review the order. If they order non-fast food items, be creative in telling them 
        it's not on the menu. Otherwise, return the order as a Python list in parentheses.""",
    )

    # Initialize the chat session
    chat = client.chats.create(model=model, config=config)

    print("--- Fast Food Order Bot (Type 'exit' or 'quit' to stop) ---")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Send message and stream the response
        try:
            response_stream = chat.send_message_stream(user_input)
            print("Bot: ", end="")
            for chunk in response_stream:
                if chunk.text:
                    print(chunk.text, end="")
            print() # New line after response
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    load_dotenv()      
    start_chat()