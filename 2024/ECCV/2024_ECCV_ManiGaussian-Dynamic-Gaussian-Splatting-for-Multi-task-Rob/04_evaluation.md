# Evaluation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- AP
- mAP
- PSNR
- success rate
- collision

## Evaluation Protocol and Results
- Then we compare our method with the state-of-the-art approaches to show the superiority in success rate (Section 4.2), and conduct an ablation study to verify the effectiveness of ...
- The diversity of these tasks requires the agent to acquire generalizable knowledge about the intrinsical scene-level spatial-temporal dynamics for manipulation, rather than solely relying on mimicking the provided ...
- Finally, we also illustrate the visualization results to depict our intuition (Section 4.4).
- Our experiments are conducted in the popular RLBench simulated tasks.
- We evaluate our ManiGaussian on 10 RLBench tasks with 166 variations, and the results demonstrate our framework can outperform the state-of-the-art methods by 13.1% in average success rate1 ...
- Then we compare our method with the state-of-the-art approaches to show the superiority in success rate (Section 4.2), and conduct an ablation study to verify the effectiveness of ...

## Baselines
- Baselines: We compare our ManiGaussian with the previous state of the arts including the perceptive method PerAct and its modified version using 4 camera inputs to cover the ...
- In this section, we first introduce the experiment setup including datasets, baseline methods, and implementation details (Section 4.1).

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
