#!/bin/bash
FAIRSEQ=../fairseq
PRETRAIN=../mbart.cc25/model.pt
langs=ar_AR,cs_CZ,de_DE,en_XX,es_XX,et_EE,fi_FI,fr_XX,gu_IN,hi_IN,it_IT,ja_XX,kk_KZ,ko_KR,lt_LT,lv_LV,my_MM,ne_NP,nl_XX,ro_RO,ru_RU,si_LK,tr_TR,vi_VN,zh_CN
SRC=en_XX
TGT=fr_XX
NAME=en-fr
DATADIR=../data_final/en-fr
SAVEDIR=../data_final/out
TOKENS=1024

python ${FAIRSEQ}/train.py ${DATADIR} --memory-efficient-fp16 \
--encoder-normalize-before --decoder-normalize-before \
--arch mbart_large --task translation_from_pretrained_bart \
--source-lang ${SRC} --target-lang ${TGT} --criterion label_smoothed_cross_entropy \
--label-smoothing 0.2  --dataset-impl mmap --optimizer adam --adam-eps 1e-06 --adam-betas '(0.9, 0.98)' \
--lr-scheduler polynomial_decay --lr 3e-05 --min-lr -1 --warmup-updates 2500 --total-num-update 102501 --dropout 0.3 \
--attention-dropout 0.1  --weight-decay 0.0  --update-freq 2 --save-interval 1 --save-interval-updates 20000 \
--keep-interval-updates 10 --no-epoch-checkpoints --seed 222 --log-format simple --log-interval 2 --reset-optimizer --reset-meters \
--reset-dataloader --reset-lr-scheduler --restore-file $PRETRAIN --langs $langs --layernorm-embedding  \
--max-tokens $TOKENS --max-epoch 2  --ddp-backend no_c10d --save-dir ${SAVEDIR}\
