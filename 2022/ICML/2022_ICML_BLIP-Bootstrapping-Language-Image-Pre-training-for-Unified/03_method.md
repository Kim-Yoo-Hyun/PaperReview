# Method

- Year/Venue: 2022 / ICML
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, alignment, generation
- Paper link: ./2022/ICML/2022_ICML_BLIP-Bootstrapping-Language-Image-Pre-training-for-Unified/paper.pdf
- Code/Project: https://github.com/salesforce/BLIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.
- In this paper, we propose BLIP, a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks.
- Parameter Sharing and Decoupling During pre-training, the text encoder and decoder share all parameters except for the self-attention layers.

## 원리적 동기
- However, existing methods have two major limitations: (1) Model perspective: most methods either adopt an encoder-based model (Radford et al., 2021; Li et al., 2021a), or an encoder-decoder ...
- However, most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks.
- To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.

## 핵심 방법론
- Parameter Sharing and Decoupling During pre-training, the text encoder and decoder share all parameters except for the self-attention layers.
- Comparison between different parameter sharing strategies for the text encoder and decoder during pre-training.
- In Table 4, we study the effect if the captioner and filter share parameters in the same way as pre-training.
