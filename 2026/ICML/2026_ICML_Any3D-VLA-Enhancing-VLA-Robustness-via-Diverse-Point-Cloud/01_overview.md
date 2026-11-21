# Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/60472.
> PDF retrieval source: https://openreview.net/pdf/01fd7931fc7be08bf369b6a34264822e6d1de9b9.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Xianzhe Fan, Shengliang Deng, Xiaoyang Wu, Yuxiang Lu, Zhuoling Li, Mi Yan, Yujia Zhang, Zhizheng Zhang, He Wang, Hengshuang Zhao
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Vision-Language Model, 3D Vision
- Official paper: https://icml.cc/virtual/2026/poster/60472
- Full-text retrieval: https://arxiv.org/pdf/2602.00807
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Any3D-VLA는 출처가 다른 점군을 같은 학습 과정에서 사용해 VLA의 깊이와 장면 변화에 대한 민감도를 줄인다. [PDF 1쪽](https://arxiv.org/pdf/2602.00807#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing Vision-Language-Action (VLA) models typically take 2D images as visual input, which limits their spatial understanding in complex scenes.
- **p. 1 / Abstract - extractive body cue:** How can we incorporate 3D information to enhance VLA capabilities?
- **p. 1 / Abstract - extractive body cue:** We conduct a pilot study across different observation spaces and visual representations.
- **p. 1 / Abstract - extractive body cue:** The results show that explicitly lifting visual input into point clouds yields representations that better complement their corresponding 2D representations.
- **p. 1 / Abstract - extractive body cue:** To address the challenges of (1) scarce 3D data and (2) the domain gap induced by cross-environment differences and 1School of Computing and Data Science, ...
- **p. 2 / 1. Introduction - extractive body cue:** (2) To address the scaling bottlenecks of 3D VLA training and the cross-environment domain gap, we introduce a hybrid point-cloud training strategy and construct a ...
- **p. 2 / 1. Introduction - extractive body cue:** However, 3D VLAs still face bottlenecks in scalable training and real deployment: (1) compared to the massive amount of 2D image data, 3D data is ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA.
- **p. 2 / 1. Introduction - extractive body cue:** We propose ANY3D-VLA, a plug-in pipeline for existing VLA backbones (Figure 1).
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** The VLM comprises a trainable large language model InternLM2 1.8B (Cai et al., 2024), a visual observation module (§5.2), and a trainable projector that maps ...
- **p. 4 / 5.1. Overall Architecture - extractive body cue:** We use a conditional flow-matching action expert (Lipman et al., 2023) to generate fine-grained end-effector actions.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data.
- **p. 5 / 5.3. Training Strategy - extractive body cue:** We do not incorporate any explicit reconstruction losses for depth or point clouds, aiming to demonstrate that the performance gains stem primarily from superior spatial ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The model takes as input image observations and the corresponding point clouds, the language instruction, and proprioceptive data. | image/video, language instruction, proprioception과 history | p. 5 (5.3. Training Strategy), p. 1 (1. Introduction) |
| State/latent | model, takes, input, image, observations, corresponding, point, clouds, language, instruction, proprioceptive, data | language-grounded task state와 action-policy context | p. 5 (5.3. Training Strategy), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Vision-Language-Action (VLA) models, trained on massive collections of action trajectories paired with language instructions, hold great promise for achieving general-purpose embodied intelligence (Kim et al., 2025b; Deng et al., 2025; ... | continuous action, pose 또는 action chunk | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The full form of the loss function is provided in Appendix F.1. | instruction following, task success, generalization과 latency | p. 5 (5.3. Training Strategy), p. 5 (5.3. Training Strategy), p. 4 (5.1. Overall Architecture) |

## Main Claims and Actual Contribution

- 시뮬레이터·깊이 센서·영상 기반 깊이 추정기에서 얻은 점군을 다양화해 출처에 덜 의존하는 3차원 특징을 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2602.00807#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2602.00807#page=4)
- 점군 특징과 대응하는 2차원 특징을 결합하고, 시뮬레이션과 실물에서 관측 표현과 깊이 편차의 영향을 비교했다. [PDF 6쪽](https://arxiv.org/pdf/2602.00807#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2602.00807#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 8 (6.5. LIBERO and CALVIN Benchmarks) |
| Embodiment/environment | This dataset includes 15 object categories that appeared in the pre-training data, while the layouts and backgrounds are randomly generated and unseen during pre-training, resulting in 95 distinct scenes. | hardware/simulator version and reset protocol | p. 3 (3. Dataset and Benchmark), p. 3 (3. Dataset and Benchmark) |
| Dataset/benchmark | Simulator Only Hybrid Point Cloud Sensor Only Simulation (Test SR, %) Simulator 80.0 81.1 N/A DA3 78.9 82.1 N/A Real-World (Zero-Shot) (Average SR, %) RealSense 55.0 57.5 N/A DA3 60.0 62.5 N/A ... | role, split, size and leakage | p. 3 (3. Dataset and Benchmark), p. 3 (3. Dataset and Benchmark), p. 8 (6.3. Diverse Point-Cloud Inputs as Data Augmentation), p. 6 (6.1.1. REAL-WORLD SETUP) |
| Metric | We evaluate the models in simulation, training until the success rate converges, and then select the best-performing checkpoint for real-world testing. | definition, denominator, direction and uncertainty | p. 6 (6.1.1. REAL-WORLD SETUP), p. 7 (6.1.3. REAL-WORLD POST-TRAINING), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD) |
| Baseline/ablation | ANY3DVLA outperforms the baselines on both tasks. | fair input/data/compute/action matching | p. 7 (6.1.3. REAL-WORLD POST-TRAINING), p. 7 (6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD), p. 6 (6.1.1. REAL-WORLD SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single ...
- **p. 7 / 6.1.2. ZERO-SHOT COMPARISONS IN THE REAL WORLD - extractive body cue:** We also conduct a qualitative analysis to highlight the robustness of our method compared to baselines and to discuss shared limitations (Appendix J).
- **p. 8 / 7. Limitations and Future Work - extractive body cue:** Future work could extend to additional robot platforms and environments, and evaluate more complex, long-horizon tasks.
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** Expert trajectories are produced by generating candidate grasp poses with BoDex (Chen et al., 2025b), performing oneshot collision-avoidance trajectory planning with CuRobo (Sundaralingam et al., ...
- **p. 3 / 3. Dataset and Benchmark - extractive body cue:** To isolate the impact of observation space design and visual representation construction on VLA performance, we adopt the following controlled settings: (1) We use the ...
- **p. 4 / 3. Dataset and Benchmark - extractive body cue:** 2D backbones struggle to effectively infer occlusion relationships and absolute scales from flattened depth maps.
- **p. 6 / 6.1.1. REAL-WORLD SETUP - extractive body cue:** To ensure the reliability of real-world deployment, we first verify that the policy trained solely on simulator point clouds remains robust when exposed to relatively ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (5.1. Overall Architecture), p. 5 (5.3. Training Strategy)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, 3D VLAs still face bottlenecks in scalable training and real deployment: (1) compared to the massive amount of 2D image data, 3D data is extremely scarce; (2) 3D data ... (p. 2, 1. Introduction).
- **Actual contribution:** The contributions of this paper are summarized as follows: (1) We propose ANY3D-VLA. (p. 2, 1. Introduction).
- **Evaluation boundary:** Method Single-Trial Test Grasp SR (%) SR (%) SR (%) 2D-only 45.3 72.6 80.0 Implicit-depth RGB 55.8 78.9 85.3 Implicit-3D RGB 46.3 78.9 87.4 RGBD image-plane 56.8 76.8 87.4 Point ... (p. 4, 3. Dataset and Benchmark).
- **Explicit failure boundary:** Although we have evaluated this work in both simulation and real-world manipulation settings, several limitations remain: (1) Our real-world experiments currently cover only a single robotic arm and a limited ... (p. 8, 7. Limitations and Future Work).
