import openai

openai.api_key = api_key = "your_api_key"

def chat_with_bot(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye", "goodbye", "see ya"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_bot(user_input)
        print("Chatbot:", response)
