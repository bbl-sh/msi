import warnings
warnings.filterwarnings('ignore')
# Behind the pipeline
# from transformers import pipeline, AutoTokenizer

# checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# text_inputs = [
#     "This is test input "
# ]

# input = tokenizer(text_inputs, padding = True, truncation = True, return_tensors = "pt")
# print(input)


# # Tokenizers

# from transformers import AutoTokenizer

# checkpoint = "bert-base-cased"
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# input = "sample text"
# # print(tokenizer("sample text "))
# ## you can also save the tokenizer using tokenizer.save_pretrained("directory_on_my_computer")

# tokens = tokenizer.tokenize(input)
# # print(tokens)

# ids =  tokenizer.convert_tokens_to_ids(tokens)
# # print(ids)

# decode = tokenizer.decode(ids)
# # print(decode)

# Handling multiple sequences

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

sequence = "This is a simple example "

tokens = tokenizer(sequence, padding = True, truncation = True, return_tensors = "pt")
output = model(**tokens)
print(output)
