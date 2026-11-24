# From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Abstract-Conference.html.
> PDF retrieval source: https://openreview.net/pdf/d6aae457099a5d9e50bba1a6bbc48d8756a15c91.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Zhengshen Zhang, Hao Li, Yalun Dai, Zhengbang Zhu, Lei Zhou, Chenchen Liu, Dong Wang, Francis E. H. Tay, Sijin Chen, Ziwei Liu, Yuxiao Liu, Xinghang Li, Pan Zhou
- 저자 판본: 논문 표제면의 저자 표기와 순서. [표제면](https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf#page=1)
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf
- Code/Project: https://falcon-vla.github.io/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

FALCON은 RGB로 추정한 3차원 구조를 행동 헤드에 제공해 VLA 정책이 공간 변화에 대응하게 한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability.
- **p. 1 / Abstract - extractive body cue:** Recent 3D integration techniques for VLAs either require specialized sensors and transfer poorly across modalities, or inject weak cues that lack geometry and degrade vision-language ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.
- **p. 1 / Abstract - extractive body cue:** FALCON leverages spatial foundation models to deliver strong geometric priors from RGB alone, and includes an Embodied Spatial Model that can optionally fuse depth, or ...
- **p. 1 / Abstract - extractive body cue:** To preserve language reasoning, spatial tokens are consumed by a Spatial-Enhanced Action Head rather than being concatenated into the vision-language backbone.
- **p. 2 / 1 Introduction - extractive body cue:** This discrepancy results in a critical gap: current VLAs lack reliable 3D spatial understanding, leading to persistent challenges in generalization and adaptability.
- **p. 2 / 1 Introduction - extractive body cue:** These limitations now form a major bottleneck in developing reliable generalist robot policies.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection ...
- **p. 2 / 1 Introduction - extractive body cue:** Overall Benchmark Bridge Calvin (Zero-shot) Google Robot Calvin Real-World Real-World (Few-Shot) Figure 1 We propose FALCON, a vision-language-action model that achieves robust 3D spatial understanding ...
- **p. 3 / 1 Introduction - extractive body cue:** For limitation (2) of poor modality transferability, we introduce an Embodied Spatial Model that can optionally integrate extra 3D modalities (e.g., depth, poses).
- **p. 4 / 3 Methodology - extractive body cue:** We introduce a lightweight fusion mechanism that aligns and combines these complementary representations (see Sec.
- **p. 4 / 3 Methodology - extractive body cue:** To this end, we propose FALCON, a generalist robot policy that overcomes limitations of prior VLAs by integrating rich geometric priors from spatial foundation models ...
- **p. 6 / 3 Methodology - extractive body cue:** These are then concatenated with a learnable camera token tcam ∈RDs and fed into a Spatial Encoder Espl(·), which consists of N cross-attention and self-attention ...
- **p. 4 / 3 Methodology - extractive body cue:** 2, FALCON is an end-to-end VLA consists of three core components: (1) a 2D VLM for multimodal semantic representation, (2) an ESM for extracting 3D ...
- **p. 6 / 3 Methodology - extractive body cue:** To address this limitation, we propose an Embodied Spatial Model that injects 3D conditions (i.e., depth, pose) to build more accurate spatial representations, enabling our ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 Problem Definition We study the problem of task-oriented robot control, where a robot must interpret visual observations Ot = {I1 t , . . . , In t } at time ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 Methodology), p. 5 (3 Methodology) |
| State/latent | Problem, Definition, study, task-oriented, robot, control, where, must, interpret, visual, observations, time | geometry, map, object/relationship state | p. 4 (3 Methodology), p. 5 (3 Methodology), p. 4 (3 Methodology) |
| Output/action | At timestep t, the VLM processes visual observations Ot and language instructions L to produce a semantic action token ˆtact. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology) |
| Objective/outcome | 3.3 Training Objective During the training process of FALCON, the objective for action sequence generation is formulated as the minimization of a composite loss function over the predicted action horizon. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology) |

## Main Claims and Actual Contribution

- 공간 기초 모델에서 얻은 토큰을 행동 헤드에 주입하며, 깊이 또는 자세가 주어지면 같은 모델에 추가할 수 있다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf#page=5)
- 시뮬레이션과 실물 조작에서 물체 크기·높이와 장면 혼잡도를 바꿔 공간 단서가 행동에 주는 효과를 비교했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Paper-Conference.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | All models are initially pre-trained on a mixture of the Open X-Embodiment dataset [29] and then fine-tuned with multi-task real-robot data. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | Base Tasks contains a total of nine distinct task suites, encompassing language grounding (cluttered scenes with random distractors) and semantic understanding (unseen object poses). | role, split, size and leakage | p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Metric | In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 4 Experiments - extractive body cue:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure.
- **p. 11 / 5 Conclusion - extractive body cue:** In this work, we introduce FALCON, a vision-language-action model that augments generalist robot policies with robust 3D spatial understanding.
- **p. 11 / 5 Conclusion - extractive body cue:** Experiments across both simulation and real-world tasks show that FALCON consistently surpasses existing VLA methods, achieving state-of-the-art performance and robustness on spatially demanding tasks.
- **p. 7 / 4 Experiments - extractive body cue:** For real-world tasks, we design settings that span from simple interactions (e.g., lifting a yellow pepper) to long-horizon, spatially demanding activities (e.g., placing a red ...
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios.
- **p. 10 / 4 Experiments - extractive body cue:** 4, this approach results in significant performance degradation compared to the standard FALCON paradigm.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Methodology), p. 4 (3 Methodology)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** These limitations now form a major bottleneck in developing reliable generalist robot policies. (p. 2, 1 Introduction).
- **Actual contribution:** We propose FALCON (From Spatial to Action), a novel paradigm that integrates richer and more representative 3D spatial tokens into VLAs through an improved injection scheme. (p. 2, 1 Introduction).
- **Evaluation boundary:** 2 reports the results on the Bridge-WidowX setup, where FALCON consistently outperforms all baselines and achieves best performance. (p. 8, 4 Experiments).
- **Explicit failure boundary:** For larger blocks, collisions frequently occur during the placement of the blue block, while smaller blocks are prematurely released before placement, leading to task failure. (p. 9, 4 Experiments).

## 공개 자료 대조

- **코드** · FALCON의 학습 손실 코드 및 CALVIN·SimplerEnv 평가 진입점. [배포 파일](https://raw.githubusercontent.com/FALCON-VLA/FALCON/a30c80aef8fc5e95badaa1b65ca40e25004bc87c/falcon/train/loss.py) · [저자 배포 안내](https://raw.githubusercontent.com/FALCON-VLA/FALCON/a30c80aef8fc5e95badaa1b65ca40e25004bc87c/README.md)
- **가중치** · CALVIN ABC에서 학습한 FALCON 정책. 저장소는 다른 변형과 사전학습 파일도 제공한다. [배포 파일](https://huggingface.co/FALCON-VLA/FALCON-series/blob/902eec199093478b500edd2cde2d8728c556d5de/falcon-esm-fc-calvin-abc/ckpts/falcon_esm_fc_calvin_abc.pt) · [저자 배포 안내](https://raw.githubusercontent.com/FALCON-VLA/FALCON/a30c80aef8fc5e95badaa1b65ca40e25004bc87c/README.md)
- **데이터** · 저자가 전처리한 CALVIN의 카메라·3차원 입력 자료. 원래 로봇 데이터 전체의 재배포를 뜻하지 않는다. [배포 파일](https://huggingface.co/datasets/FALCON-VLA/CALVIN-3D_cam-params/blob/f7d9c7bd21f054180bddc8ac4b64ee799d7a7556/packaged_ABC_D/packaged_ABC_D.tar.gz) · [저자 배포 안내](https://raw.githubusercontent.com/FALCON-VLA/FALCON/a30c80aef8fc5e95badaa1b65ca40e25004bc87c/README.md)
