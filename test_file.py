from langchain.llms import OpenAI
import os

# Instantiate the OpenAI LLM
api_key = os.environ['OPENAI_API_KEY']
llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo-1106")


# Function to preprocess code using OpenAI LLM
def preprocess_code(llm, code):
    # Generate preprocessed code using the OpenAI model
    # For chat-based models, include a conversation context in the prompt
    prompt = ["User: Please preprocess the following code:", f"Code: {code}", "User:"]
    generation_result = llm.generate(prompt, stop=["\n"], endpoint="v1/chat/completions")

    # Extract the generated preprocessed code from the generation result
    preprocessed_code = generation_result.choices[0].text.strip()

    return preprocessed_code


# Example usage:
processed_data = []

for root, _, files in os.walk("/Users/vishaltripathi/Downloads/RedditSentiment"):
    for file in files:
        if file.endswith(".py") or file.endswith(".scala"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                code = f.read()
            preprocessed_code = preprocess_code(llm, code)
            processed_data.append(preprocessed_code)
