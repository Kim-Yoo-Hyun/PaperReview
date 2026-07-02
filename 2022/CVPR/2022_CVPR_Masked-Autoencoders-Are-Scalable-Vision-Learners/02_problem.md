# Problem

- Year/Venue: 2022 / CVPR
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2022/CVPR/2022_CVPR_Masked-Autoencoders-Are-Scalable-Vision-Learners/paper.pdf
- Code/Project: https://github.com/facebookresearch/mae
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision.
- Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels.
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...

## 해결하려는 문제
- Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...
- After pre-training, the decoder is discarded and the encoder is applied to uncorrupted images (full sets of patches) for recognition tasks. in vision preceded BERT.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
