
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

# Set your Hugging Face authentication token
HUGGINGFACE_TOKEN = "your_token_here"

# Use the FoodBERT model with the authentication token
model_name = "microsoft/FoodBertBaseUncased"

# Load the FoodBERT model using transformers' AutoModelForTokenClassification
model = AutoModelForTokenClassification.from_pretrained(model_name, auth_token=HUGGINGFACE_TOKEN)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set up the NER pipeline
food_ner = pipeline("ner", model=model, tokenizer=tokenizer)

# Now you can use the food_ner pipeline as before
text = "Your sample text here."
food_entities = food_ner(text)
print(food_entities)
