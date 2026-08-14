# Evaluation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Generative Models
- Tags: Diffusion, Generation
- Paper link: ./2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/paper.pdf
- Code/Project: https://github.com/hojonathanho/diffusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Metrics
- mAP
- RMSE

## Evaluation Protocol and Results
- With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models.
- We set T = 1000 for all experiments so that the number of neural network evaluations needed during sampling matches previous work .
- These constants were chosen to be small relative to data scaled to [−1, 1], ensuring that reverse and forward processes have approximately the same functional form while keeping ...
- 4.1 Sample quality Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths) on CIFAR10.
- With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models.
- On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17.

## Baselines
- We set T = 1000 for all experiments so that the number of neural network evaluations needed during sampling matches previous work .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
