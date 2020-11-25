#!/bin/bash
DATA=../data/wiki
MODEL=../model/mbart.cc25/sentence.bpe.model
TRAIN=train
VALID=valid
TEST=test
SRC=en_XX
TGT=fr_XX


spm_encode --model=${MODEL} < ${DATA}/${TRAIN}.${SRC} > ${DATA}/${TRAIN}.spm.${SRC} &
spm_encode --model=${MODEL} < ${DATA}/${TRAIN}.${TGT} > ${DATA}/${TRAIN}.spm.${TGT} &
spm_encode --model=${MODEL} < ${DATA}/${VALID}.${SRC} > ${DATA}/${VALID}.spm.${SRC} &
spm_encode --model=${MODEL} < ${DATA}/${VALID}.${TGT} > ${DATA}/${VALID}.spm.${TGT} &
spm_encode --model=${MODEL} < ${DATA}/${TEST}.${SRC} > ${DATA}/${TEST}.spm.${SRC} &
spm_encode --model=${MODEL} < ${DATA}/${TEST}.${TGT} > ${DATA}/${TEST}.spm.${TGT} &