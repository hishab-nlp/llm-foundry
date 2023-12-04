python inference/convert_composer_to_hf.py \
  --composer_path llm_125m/run3/ep1-ba4000-rank0.pt \
  --hf_output_path mpt-125m-bn-4k-hf \
  --output_precision bf16 \
  --trust_remote_code
