# Method

- Year/Venue: 2022 / CVPR
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2022/CVPR/2022_CVPR_Masked-Autoencoders-Are-Scalable-Vision-Learners/paper.pdf
- Code/Project: https://github.com/facebookresearch/mae
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...
- We attempt to answer this question from the following perspectives: (i) Until recently, architectures were different.
- Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...

## 원리적 동기
- This paper shows that masked autoencoders (MAE) are scalable self-supervised learners for computer vision.
- Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels.
- First, we develop an asymmetric encoder-decoder architecture, with an encoder that operates only on the visible subset of patches (without mask tokens), along with a lightweight decoder that ...

## 핵심 방법론
- The pre-training data is the ImageNet-1K training set (except the tokenizer in BEiT was pre-trained on 250M DALLE data ).
