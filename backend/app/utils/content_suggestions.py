from transformers import pipeline

content_generator = pipeline("text-generation", model="gpt-2")

def generate_suggestions(content):
    generated = content_generator(content, max_length=50, num_return_sequences=1)
    return generated[0]["generated_text"]
