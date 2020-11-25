#!/bin/bash
DATA=../data/wiki
MODEL=../model/mbart.cc25/sentence.bpe.model
TRAIN=train
VALID=valid
TEST=test
SRC=en_XX
TGT=fr_XX
FAIRSEQ=../fairseq/fairseq_cli
NAME=en-fr
DEST=../postprocessed
DICT=../model/mbart.cc25/dict.txt

python ${FAIRSEQ}/preprocess.py \
--source-lang ${SRC} \
--target-lang ${TGT} \
--trainpref ${DATA}/${TRAIN}.spm \
--validpref ${DATA}/${VALID}.spm \
--testpref ${DATA}/${TEST}.spm  \
--destdir ${DEST}/${NAME} \
--thresholdtgt 0 \
--thresholdsrc 0 \
--srcdict ${DICT} \
--tgtdict ${DICT} \
--workers 70