# Evaluation

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Diffusion and Generative Models
- Tags: Diffusion, generation
- Paper link: ./2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/paper.pdf
- Code/Project: https://github.com/hojonathanho/diffusion
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

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
