import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="your api key")

# List all models accessible to your account
models = genai.list_models()

print("Available models:")
for model in models:
    print(f"- {model.name}")
