# Evaluation

- Year/Venue: 2024 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Robotics, Imitation Learning
- Paper link: ./2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/paper.pdf
- Code/Project: https://github.com/openvla/openvla
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- BridgeData
- Open X-Embodiment

## Metrics
- accuracy
- success rate

## Evaluation Protocol and Results
- OpenVLA achieves highest overall performance and even outperforms closed-source model RT-2-X in all categories except for semantic generalization.
- Concretely, we aim to answer the following questions: (1) How does OpenVLA compare to prior generalist robot policies, when evaluating on multiple robots and various types of generalization? ...
- We find that OpenVLA and RT-2-X attain comparable performance and significantly outperform RT-1-X and Octo overall.
- RT-2-X clearly outperforms both RT-1-X and Octo, demonstrating the benefits of large, pretrained VLMs for robotics.
- As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% ...
- OpenVLA achieves highest overall performance and even outperforms closed-source model RT-2-X in all categories except for semantic generalization.

## Baselines
- Concretely, we aim to answer the following questions: (1) How does OpenVLA compare to prior generalist robot policies, when evaluating on multiple robots and various types of generalization? ...
- We compare OpenVLA’s performance to three prior generalist manipulation policies: RT-1-X , RT-2-X , and Octo .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
