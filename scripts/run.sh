composer train/train.py \
  train/yamls/pretrain/mpt-1b-bn.yaml \
  data_local=/llm-foundry/dataset \
  train_loader.dataset.split=train \
  eval_loader.dataset.split=val \
  max_duration=2ba \
  eval_interval=0
  # save_folder=mpt-125m-bn-1