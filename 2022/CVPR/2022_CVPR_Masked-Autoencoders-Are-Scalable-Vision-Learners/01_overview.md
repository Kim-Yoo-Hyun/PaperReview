# Masked Autoencoders Are Scalable Vision Learners

- Year/Venue: 2022 / CVPR
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2022/CVPR/2022_CVPR_Masked-Autoencoders-Are-Scalable-Vision-Learners/paper.pdf
- Code/Project: https://github.com/facebookresearch/mae
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision.
- Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels.
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...

## Core Idea
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...
- We attempt to answer this question from the following perspectives: (i) Until recently, architectures were different.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...
- Our scalable approach allows for learning high-capacity models that generalize well: e.g., a vanilla ViT-Huge model achieves the best accuracy (87.8%) among methods that use only ImageNet-1K data.
- Coupling these two designs enables us to train large models efficiently and effectively: we accelerate training (by 3× or more) and improve accuracy.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...
- After pre-training, the decoder is discarded and the encoder is applied to uncorrupted images (full sets of patches) for recognition tasks. in vision preceded BERT.

## Abstract Cue
- This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision.
