# Problem

- Year/Venue: 2023 / TMLR
- Category: Foundations: Vision Foundation Models
- Tags: self-supervised, representation
- Paper link: ./2023/TMLR/2023_TMLR_DINOv2-Learning-Robust-Visual-Features-without-Supervision/paper.pdf
- Code/Project: https://github.com/facebookresearch/dinov2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.

## 해결하려는 문제
- This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised ...

## 선행 연구 / 배경 단서
- This success has been fueled by pretraining on large quantities of raw text using pretext objectives, such as language modeling (Radford et al., 2017) or word vectors (Devlin ...
- Most promising efforts towards these foundation models focus on text-guided pretraining, i.e., using a form of textual supervision to guide the training of the features (Joulin et al., ...
