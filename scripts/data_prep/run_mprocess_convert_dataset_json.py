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
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument('--json_chunk_path', type=str, required=True, help="json lines chunk path where several jsonl files exist")
args.add_argument('--output_dir', type=str, required=True, help='path where each json output sub directory will be saved')
args.add_argument('--num_worker', type=int, default=None, help='number of worker for multiprocessing')

parsed = args.parse_args()

def main():
    files = glob.glob(parsed.json_chunk_path + '/*.jsonl')
    print(f"total jsonl files: {len(files)}")

    def process(file: str) -> None:
        filename = os.path.basename(file).replace('.jsonl', '')
        output_file_dir = os.path.join(parsed.output_dir, filename)
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

    pool = multiprocessing.Pool(processes=parsed.num_worker if parsed.num_worker else multiprocessing.cpu_count())

    list(tqdm(pool.imap_unordered(process, files), total=len(files)))

if __name__ == "__main__":
    main()

