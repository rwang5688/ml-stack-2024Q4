from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='distilgpt2', device='cuda', truncation=True)
set_seed(42)
print(generator("Hello, I’m a language model", max_length=20, num_return_sequences=5))
