python convert_dataset_json.py \
  --path ./example_data/arxiv.jsonl \
  --out_root temp \
  --split train \
  --concat_tokens 2048 \
  --tokenizer hishab/Sentencepiece_47GB_72k_test \
  --eos_text '</s>' \
  --bos_text '<s>' \
  --trust_remote_code \
  --hf_cache_dir hf_cache