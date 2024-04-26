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

chunks_path = "/data/mybndatasets/splited_data/train"

files = glob.glob(chunks_path + '/*.jsonl')
print(f"total files: {len(files)}")

output_base_dir = "/data/output/train"

def process(file: str) -> None:
    filename = os.path.basename(file).replace('.jsonl', '')
    output_file_dir = os.path.join(output_base_dir, filename)
    os.makedirs(output_file_dir, exist_ok=True)

    command = f"""python convert_dataset_json.py \
    --path {file} \
    --out_root {output_file_dir} \
    --split train \
    --concat_tokens 2048 \
    --tokenizer hishab/Sentencepiece_47GB_72k_test \
    --eos_text '</s>' \
    --bos_text '<s>' \
    --trust_remote_code \
    --hf_cache_dir /data/cached"""

    os.system(command)

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

list(tqdm(pool.imap_unordered(process, files), total=len(files)))

