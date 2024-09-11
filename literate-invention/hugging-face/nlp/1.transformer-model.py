from transformers import pipeline

classifier = pipeline("sentiment-analysis")

print(classifier("wow so good"))

# zero shot classification

# classifier = pipeline("zero-shot-classification")
# classifier(
#     "I am learning hugging face ",
#     candidate_labels=["education", "politics", "business"],
# )
