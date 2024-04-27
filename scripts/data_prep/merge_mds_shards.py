"""
Merge the MDS shards created using convert_dataset_json_multiprocessing.py
This script reads all the shards index.json file and combine into one index file.
Also move all the files with shard naming in same directory without the subdirectory.
"""
from argparse import ArgumentParser
from llmfoundry.utils.data_prep_utils import merge_shard_groups

args = ArgumentParser(
        description=
        'Merge all MDS shards generated using multiprocessing of convert dataset json'
    )

args.add_argument(
    '--root_dir', 
    type=str, 
    required=True,
    help='root directory where each sub direcotry of shards exist'
)

parsed = args.parse_args()

def main():
    merge_shard_groups(parsed.root_dir)

if __name__ == "__main__":
    main()