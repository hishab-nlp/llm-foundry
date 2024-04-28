"""
As convert_data_json.py script is not multiprocessing enable,
This script runs the script on several json chunks using multiprocessing.
Later another script will merge the outputs chunks together using the below function
https://github.com/mosaicml/llm-foundry/blob/f43d1cfb1ef8f38ca90fee68b0643f45d6d5b2da/llmfoundry/utils/data_prep_utils.py#L29
Idea gather from this issue: https://github.com/mosaicml/llm-foundry/issues/870
"""

import os
import glob
import multiprocessing
from tqdm import tqdm


json_chunk_path = "/data/mybndatasets/web_data_only/train"
output_dir = "/data/mybndatasets/web_data_only/mds/train"
os.makedirs(output_dir, exist_ok=True)

files = glob.glob(json_chunk_path + '/*.jsonl')
print(f"total jsonl files: {len(files)}")

def process(file: str) -> None:
    filename = os.path.basename(file).replace('.jsonl', '')
    output_file_dir = os.path.join(output_dir, filename)
    os.makedirs(output_file_dir, exist_ok=True)

    command = f"""python convert_dataset_json.py \
    --path {file} \
    --out_root {output_file_dir} \
    --split train \
    --concat_tokens 2048 \
    --tokenizer hishab/titulm-sentencepiece-72k \
    --eos_text '</s>' \
    --bos_text '<s>' \
    --trust_remote_code \
    --hf_cache_dir /data/cached"""

    os.system(command)

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

list(tqdm(pool.imap_unordered(process, files), total=len(files)))


