from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("CreativeWriting\gpt2-dpo-final-model")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

generation_params = {
    "max_length": 512,
    "num_beams": 1, # Keep num_beams if you intend greedy search
    # Removed 'temperature' and 'top_p' as they are often ignored with num_beams=1
    'repetition_penalty': 1.1,
    'pad_token_id': tokenizer.eos_token_id,
}

test_prompt = input("Enter a prompt for creative writing: ")

# Encode the input and get both input_ids and attention_mask
inputs = tokenizer.encode_plus(
    test_prompt,
    return_tensors="pt",
    padding=True, # Ensure padding is applied if needed
    truncation=True, # Truncate if prompt is too long for model's max input
)
input_ids = inputs["input_ids"]
attention_mask = inputs["attention_mask"] # Get the attention mask

# Pass the attention_mask to the generate method
output = model.generate(input_ids, attention_mask=attention_mask, **generation_params)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:\n", output_text)