# Our LLM Training

## Installation
- Pull the docker mosaicml docker image by `docker pull mosaicml/llm-foundry:2.1.0_cu121-latest`
- Clone our forked repo by `git clone https://github.com/hishab-nlp/llm-foundry.git`
- Run the docker image with necessary arguments

  ```
  sudo docker run -it --gpus all --shm-size=1g --ulimit memlock=-1 -v /data1/sagor/hishab_nlp/llm-foundry:/llm-foundry --rm mosaicml/llm-foundry:2.1.0_cu121-latest
  ```
- Change directory to `/llm-foundry` and install dependencies

  ```
  cd /llm-foundry
  pip install -e ".[gpu]"
  ```
- Authenticate huggingface by `huggingface-cli login`

## Data preparation
- To convert JSONL text files to MDS format
- Change directory to `scripts/data_prep` and run

  ```bash
  python convert_dataset_json.py \
  --path ./splited_data/train \
  --out_root ./output/train \
  --split train \
  --concat_tokens 2048 \
  --tokenizer hishab/Sentencepiece_47GB_72k_test \
  --eos_text '</s>' \
  --bos_text '<s>'
  ```

## Training
- Change directory to `scripts`
- Check your desire settings in config `train/yamls/pretrain` files
- Run training by `run.sh`

## Tips
- To save checkpoints in Google cloud bucket authenticate google cloud by

  ```
  export GOOGLE_APPLICATION_CREDENTIALS=/path/gc_auth.json
  ```

- While running your training you might provide wandb project API key to authenticate wandb

