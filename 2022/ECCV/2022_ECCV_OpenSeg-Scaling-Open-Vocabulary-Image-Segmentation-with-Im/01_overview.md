# OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, semantic, open-vocabulary, segmentation
- Paper link: ./2022/ECCV/2022_ECCV_OpenSeg-Scaling-Open-Vocabulary-Image-Segmentation-with-Im/paper.pdf
- Code/Project: https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/openseg
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Image segmentation is an important step to organize an image into a small number of regions in order to understand “what” and “where” are in an image.
- Each region represents a semantically meaningful entity, which can be a thing (e.g., a chair) or stuff (e.g., floor).
- Language is a natural interface to describe what is in an image.

## Core Idea
- 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) for multi-scale feature extraction and a cross-attention module for segmentation region ...
- We use a cross-attention module taking inputs as FsP E and a randomly initialized queries q0 ∈ RN ×D to generate mask queries q ∈ RN ×D .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- OpenSeg significantly outperforms the recent openvocabulary method of LSeg by +19.9 mIoU on PASCAL dataset, thanks to its scalability. bride groom hills field sky cow calf grass trees ...

## Limitation
- We hope to encourage future works to learn a generalist segmentation model that can transfer across datasets using language as the interface.

## Contribution
- We propose OpenSeg to address the above issue while still making use of scalable image-level supervision of captions.
- We propose a model, called OpenSeg, that can organize pixels into meaningful regions indicated by texts.
- OpenSeg significantly outperforms the recent openvocabulary method of LSeg by +19.9 mIoU on PASCAL dataset, thanks to its scalability. bride groom hills field sky cow calf grass trees ...

## Abstract Cue
- We design an open-vocabulary image segmentation model to organize an image into meaningful regions indicated by arbitrary texts.
