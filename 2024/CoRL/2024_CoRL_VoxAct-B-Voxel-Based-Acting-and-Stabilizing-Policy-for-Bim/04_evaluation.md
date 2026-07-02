# Evaluation

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, 3D manipulation, bimanual, Robotics
- Paper link: ./2024/CoRL/2024_CoRL_VoxAct-B-Voxel-Based-Acting-and-Stabilizing-Policy-for-Bim/paper.pdf
- Code/Project: https://voxact-b.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- mAP
- collision

## Evaluation Protocol and Results
- For simulation experiments, we build on top of RLBench , a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct.
- We adapt the Mobile ALOHA repository for ACT and a CNN-based Diffusion Policy, and we tune their parameters (e.g., chunk size and action horizon) to improve performance.
- ACT is a state-of-the-art method for bimanual manipulation.
- Additionally, we include a Bimanual PerActs baseline, which trains separate PerAct policies for the left and right arms, to show how a straightforward bimanual adaptation of a single-arm, ...
- In simulation, we show that VoxAct-B outperforms strong baselines on fine-grained bimanual manipulation tasks.
- For simulation experiments, we build on top of RLBench , a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct.

## Baselines
- 5.1 Baselines and Ablations In simulation, we compare against several strong baseline methods: Action Chunking with Transformers (ACT) , Diffusion Policy , and VoxPoser .
- Additionally, we include a Bimanual PerActs baseline, which trains separate PerAct policies for the left and right arms, to show how a straightforward bimanual adaptation of a single-arm, ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
