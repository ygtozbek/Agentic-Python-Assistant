import os
from groq import Groq
from dotenv import load_dotenv

# Loading my secret key from the .env file
load_dotenv()
my_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_key)

def get_ai_help(user_input):
    # Setting up for my assistant
    my_messages = [
        {"role": "system", "content": "You are a helpful coding buddy. Give short and clean Python examples."},
        {"role": "user", "content": user_input}
    ]
    
    response = client.chat.completions.create(
        messages=my_messages,
        model="llama-3.1-8b-instant",
        temperature=0.5
    )
    return response.choices[0].message.content


print("--- My Python Coding Buddy ---")
print("(Type 'exit' to stop the program)")

while True:
    task = input("\nWhat should I code for you?: ")
    
    if task.lower() == "exit":
        print("Goodbye!")
        break
        
    print("AI is thinking...")
    answer = get_ai_help(task)
    print(answer)