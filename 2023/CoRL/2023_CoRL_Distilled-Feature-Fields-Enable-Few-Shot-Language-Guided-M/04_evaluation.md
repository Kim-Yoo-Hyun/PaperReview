# Evaluation

- Year/Venue: 2023 / CoRL
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, NeRF, Vision-Language, manipulation
- Paper link: ./2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/paper.pdf
- Code/Project: https://f3rm.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LERF

## Metrics
- success rate
- collision

## Evaluation Protocol and Results
- While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the objects we care ...
- We include three types of objects in our test scenes: (1) novel objects from the same categories as the demonstrations, (2) out-ofdistribution (OOD) objects from new categories that ...
- We break down the success rates by category in Table 2, and show the robot’s execution sequence for an example scene in Figure 7 (video).
- For each task, we evaluate in ten scenes that contain novel objects in arbitrary poses and distractor objects.
- We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen objects.
- While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the objects we care ...

## Baselines
- We consider three baselines, including (1) using density σ from the NeRF, (2) the intermediate NeRF features, and (3) the RGB color value as features, and compare against ...
- While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the objects we care ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
