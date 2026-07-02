# BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

- Year/Venue: 2022 / ICML
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, alignment, generation
- Paper link: ./2022/ICML/2022_ICML_BLIP-Bootstrapping-Language-Image-Pre-training-for-Unified/paper.pdf
- Code/Project: https://github.com/salesforce/BLIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing methods have two major limitations: (1) Model perspective: most methods either adopt an encoder-based model (Radford et al., 2021; Li et al., 2021a), or an encoder-decoder ...
- However, most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks.
- BLIP is a new VLP framework which enables a wider range of downstream tasks than existing methods.

## Core Idea
- To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.
- In this paper, we propose BLIP, a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We achieve state-of-the-art results on a wide range of vision-language tasks, such as image-text retrieval (+2.7% in average recall@1), image captioning (+2.8% in CIDEr), and VQA (+1.6% in ...
- Furthermore, performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web, which is a suboptimal source of supervision.
- However, encoder-based models are less straightforward to directly transfer to text generation tasks (e.g. image captioning), whereas encoder-decoder models have not been successfully adopted for image-text retrieval tasks. ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- However, existing methods have two major limitations: (1) Model perspective: most methods either adopt an encoder-based model (Radford et al., 2021; Li et al., 2021a), or an encoder-decoder ...
- However, encoder-based models are less straightforward to directly transfer to text generation tasks (e.g. image captioning), whereas encoder-decoder models have not been successfully adopted for image-text retrieval tasks. ...
- To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.

## Abstract Cue
- Vision-Language Pre-training (VLP) has advanced the performance for many vision-language tasks.
