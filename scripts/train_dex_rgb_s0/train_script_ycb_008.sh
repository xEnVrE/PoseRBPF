#!/usr/bin/env bash

python3 train_aae.py \
  --cfg_dir ./config/train/YCB/ \
  --obj 008_pudding_box \
  --epochs 200 \
  --save 25 \
  --modality rgb \
  --dis_dir data/coco/train2014/train2014 \
  --dataset dex_ycb_s0_train \
