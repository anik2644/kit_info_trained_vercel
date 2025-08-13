from transformers import T5Tokenizer, T5ForConditionalGeneration
from app import config

print("Loading T5 model...")
tokenizer = T5Tokenizer.from_pretrained(str(config.MODEL_DIR))
model = T5ForConditionalGeneration.from_pretrained(str(config.MODEL_DIR))
model.eval()
print(f"T5 loaded from {config.MODEL_DIR}")

def generate_answer(prompt: str, max_length=128):
    input_ids = tokenizer.encode(prompt, return_tensors="pt", truncation=True)
    output_ids = model.generate(input_ids, max_length=max_length, num_beams=4, early_stopping=True)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
