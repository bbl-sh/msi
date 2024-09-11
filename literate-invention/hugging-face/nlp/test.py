from transformers import AutoTokenizer, AutoModelForCausalLM
from jinja2 import Template

# Define the chat template function
def get_llama3_chat_template():
    return (
        "<|begin_of_text|>"
        "{% for message in messages %}"
            "{% if message.role == 'system' %}"
                "<|start_header_id|>system<|end_header_id|>"
                "{{message.content}}"
                "<|eot_id|>"
            "{% endif %}"
            "{% if message.role == 'user' %}"
                "<|start_header_id|>user<|end_header_id|>"
                "{{message.content}}"
                "<|eot_id|>"
            "{% endif %}"
            "{% if message.role == 'assistant' %}"
                "<|start_header_id|>assistant<|end_header_id|>"
                "{{message.content}}"
                "<|eot_id|>"
            "{% endif %}"
        "{% endfor %}"
        "<|end_of_text|>"
    )

# Load the tokenizer
model_id = "meta-llama/Llama-3.1"  # Replace with your actual model ID
tokenizer = AutoTokenizer.from_pretrained(model_id, revision="refs/pr/8")
tokenizer.padding_side = 'right'
tokenizer.pad_token = tokenizer.eos_token

# Assign the chat template to the tokenizer
tokenizer.chat_template = get_llama3_chat_template()

# Example messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."}
]

# Format the messages using the template
template = Template(tokenizer.chat_template)
formatted_input = template.render(messages=messages)

# Tokenize the formatted input
tokens = tokenizer(formatted_input, return_tensors="pt")

# Load the model
model = AutoModelForCausalLM.from_pretrained(model_id)

# Generate a response from the model
output = model.generate(
    input_ids=tokens.input_ids,
    attention_mask=tokens.attention_mask,
    max_length=100,  # Adjust as needed
    num_return_sequences=1,  # Number of sequences to generate
    do_sample=True,  # Whether to sample or use greedy decoding
    temperature=0.7,  # Sampling temperature
)

# Decode the generated tokens back to text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Response:", generated_text)
