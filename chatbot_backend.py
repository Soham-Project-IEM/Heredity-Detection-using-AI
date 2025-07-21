import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="YOUR API KEY")  # Replace with your actual API key

# Use a supported Gemini model (e.g., gemini-1.5-pro or gemini-pro)
model = genai.GenerativeModel('gemini-1.5-pro')  # You can change model if needed

# Start a chat session
chat_session = model.start_chat()

def get_ai_response(user_query):
    """
    Function to get a response from the Gemini model using chat session
    """
    try:
        response = chat_session.send_message(user_query)
        return response.text
    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == "__main__":
    sample_query = "What are the admission requirements for your university?"
    print(f"User query: {sample_query}")
    response = get_ai_response(sample_query)
    print(f"Gemini Response: {response}")
