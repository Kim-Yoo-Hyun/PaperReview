# Evaluation

- Year/Venue: 2023 / NeurIPS
- Category: Benchmarks and Datasets
- Tags: Robotics, Imitation Learning, Benchmark
- Paper link: ./2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/paper.pdf
- Code/Project: https://libero-project.github.io/main.html
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- LIBERO

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- We first introduce the evaluation metric used in experiments, and present analysis of empirical results in LIBERO.
- Then, we find the earliest epoch e∗i in which the agent achieves the best performance on task i (i.e., e∗i = arg mine ci,i,ei = ci,i ), and ...
- Our experiments focus on addressing the following research questions: Q1: How do different architectures/LL algorithms perform under specific distribution shifts?
- Q6: Can supervised pretraining improve downstream lifelong learning performance in LLDM?
- Our extensive experiments present several insightful or even unexpected discoveries: sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all ...
- We first introduce the evaluation metric used in experiments, and present analysis of empirical results in LIBERO.

## Baselines
- All metrics are computed in terms of success rate, as previous literature has shown that the success rate is a more reliable metric than training loss for manipulation ...
- Lower NBT means a policy has better performance in the previously seen tasks, higher FWT means a policy learns faster on a new task, and higher AUC means ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
