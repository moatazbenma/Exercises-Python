import google.generativeai as genai

genai.configure(api_key="AIzaSyApvhXw8wCkLFqMoccb_Y_kjj3_WvcAakU") 

def chat_with_gemini(user_input):
    model = genai.GenerativeModel("gemini-pro")  
    response = model.generate_content(user_input) 
    return response.text

print("AI Chatbot (Type 'exit' to stop)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chat_with_gemini(user_input)
    print("Bot:", response)