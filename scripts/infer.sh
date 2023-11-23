python inference/hf_generate.py \
  --name_or_path mpt-125m-bn-4k-hf \
  --max_new_tokens 256 \
  --prompts \
    "The answer to life, the universe, and happiness is" \
    "Here's a quick recipe for baking chocolate chip cookies: Start by"
