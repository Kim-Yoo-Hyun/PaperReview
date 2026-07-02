# Evaluation

- Year/Venue: 2023 / RSS
- Category: Foundations: RL and Imitation Learning
- Tags: Diffusion, Imitation Learning, robotics
- Paper link: ./2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/paper.pdf
- Code/Project: https://github.com/real-stanford/diffusion_policy
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- accuracy
- IoU
- mAP
- success rate
- collision

## Evaluation Protocol and Results
- We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%.
- For each variant, we report results for both stateand image-based observations.
- We systematically evaluate Diffusion Policy on 15 tasks from 4 benchmarks Florence et al. (2021); Gupta et al. (2019); Mandlekar et al. (2021); Shafiullah et al. (2022).
- This evaluation suite includes both simulated and real environments, single and multiple task benchmarks, fully actuated and under-actuated systems, and rigid and fluid objects.
- We benchmark Diffusion Policy across 15 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average ...
- We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%.

## Baselines
- We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
