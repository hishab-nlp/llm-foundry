composer train/train.py \
  train/yamls/pretrain/mpt-1b-bn.yaml \
  train_loader.dataset.split=train \
  eval_loader.dataset.split=val \
  max_duration=2ep \
  eval_interval=10000ba
  # save_folder=mpt-125m-bn-1
