# Evaluation

- Year/Venue: 2020 / EMNLP
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, Navigation, grounding, Benchmark
- Paper link: ./2020/EMNLP/2020_EMNLP_Room-Across-Room-Multilingual-Vision-and-Language-Navigati/paper.pdf
- Code/Project: https://github.com/google-research-datasets/RxR
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- Matterport3D
- R2R
- RxR

## Metrics
- SPL
- SR
- nDTW
- success rate

## Evaluation Protocol and Results
- In preliminary experiments, we found that pretraining the CNN in this way gave noticeable improvements over the same CNN pretrained for image classification on ImageNet (Russakovsky et al., ...
- We report en-US and en-IN results together as en.
- In preliminary experiments on R2R we find that encoding word embeddings via successive 1D convolutions with rectified linear (ReLU) activations and residual connections (He et al., 2016) is ...
- In both monolingual and multilingual experiments we use features extracted from a pre-trained multilingual BERT model (Devlin et al., 2019) for the word embeddings.
- In preliminary experiments, we found that pretraining the CNN in this way gave noticeable improvements over the same CNN pretrained for image classification on ImageNet (Russakovsky et al., ...
- We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended to in human demonstrations.

## Baselines
- Experiments 1–3 compare agents trained (1) only on G-paths, (2) only on F-paths, and (3) on both.
- The LSTM decoder computes an updated hidden state ht by conditioning on the previous selected action in at−1 and attending over the panoptic encoding vt and the instruction ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
