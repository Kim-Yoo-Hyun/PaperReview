# GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/deng25a.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: Shengliang Deng, Mi Yan, Songlin Wei, Haixin Ma, Yuxin Yang, Jiayi Chen, Zhiqi Zhang, Taoyu Yang, Xuheng Zhang, Heming Cui, Zhizheng Zhang, He Wang
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, grasping, synthetic data
- Official paper: https://proceedings.mlr.press/v305/deng25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf
- Code/Project: https://pku-epic.github.io/GraspVLA-web/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

GraspVLA는 시뮬레이터에서 생성한 파지 행동과 웹의 의미 정보를 함께 학습해 언어로 지정한 물체를 잡는다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf#page=1)

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** The fields of Natural Language Processing (NLP) and Computer Vision (CV) have undergone a paradigm shift with the advent of foundation models.
- **p. 2 / 1 Introduction - extractive body cue:** Large-scale models pretrained on vast amounts of Internet data exhibit zero-shot generalization to unseen scenarios [1, 2, 3] and few-shot adaptation for aligning with human ...
- **p. 2 / 1 Introduction - extractive body cue:** Inspired by this success, the foundation model for actions in the physical world has recently been introduced in Vision-Language-Action (VLA) models [5, 6, 7, 8].
- **p. 2 / 1 Introduction - extractive body cue:** These models process robotic visual observations and human instructions to directly generate robot actions.
- **p. 2 / 1 Introduction - extractive body cue:** However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.
- **p. 2 / 1 Introduction - extractive body cue:** In addition, GraspVLA shows excellent generalization to long-tail object categories absent from synthetic action data, such as chargers, towels, and swimming goggles.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks.
- **p. 8 / 5 Hz - extractive body cue:** GraspVLA shows superior adaptability to novel tasks, surpassing the model without pretraining and all baselines.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
- **p. 7 / 5 Hz - extractive body cue:** We benchmark GraspVLA against AnyGrasp [14], a state-of-the-art grasp detection model specialized in grasping.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Compared to AnyGrasp [14], the state-of-the-art in traditional grasping detection algorithms, GraspVLA supports natural language instructions and delivers a robust closed-loop grasping policy. | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Compared, AnyGrasp, state-of-the-art, traditional, grasping, detection, algorithms, GraspVLA, supports, natural, language, instructions | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)) |
| Output/action | These models process robotic visual observations and human instructions to directly generate robot actions. | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction) |
| Objective/outcome | Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. | instruction following, task success, generalization과 latency | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 다양한 장면을 렌더링해 SynGrasp-1B를 만들고, 자기회귀 지각 예측과 플로 매칭 행동 생성을 같은 모델에서 학습한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf#page=4)
- 시뮬레이션과 실물에서 처음 보는 대상의 파지를 평가하고 소수 예시로 특정 파지 선호에 적응하는 실험을 수행했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 24 (Figure/Table caption), p. 6 (5 Experiments) |
| Embodiment/environment | We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding dataset. b) Synthetic categories c) Web categories 0.2m a) Robot ... | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Dataset/benchmark | For generalists, we use π0 [7], OpenVLA [6], and Octo [26], three transformer-based policies pre-trained on large-scale real-world datasets. | role, split, size and leakage | p. 6 (5 Experiments), p. 7 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Metric | For each object group, we also report the average Success weighted by Path Length (SPL) [76], a widely used metric that weights success rate with motion efficiency by penalizing unnecessarily long paths. | definition, denominator, direction and uncertainty | p. 6 (5 Experiments), p. 8 (Figure/Table caption), p. 19 (Figure/Table caption) |
| Baseline/ablation | Additionally, the SPL metric reveals that GraspVLA grasps objects with shorter path lengths compared to π0 baselines which often exhibit hesitation. | fair input/data/compute/action matching | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 24 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Conclusion - extractive body cue:** 7 Limitations and Future Work Currently, our data generation and evaluation are conducted exclusively on the Franka Panda arm with front and side views.
- **p. 9 / 6 Conclusion - extractive body cue:** Like most grasping policies, we synthesize grasp labels using force-closure, which do not account for deformability-a limitation common to all such methods.
- **p. 7 / 5 Experiments - extractive body cue:** We provide failure analysis in the supplementary.
- **p. 7 / 5 Experiments - extractive body cue:** We evaluate on three LIBERO suites (Long, Goal, Object), excluding Spatial, as its focus on spatial reasoning falls outside our scope.
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 11: Examples of LIBERO Benchmark. We visualize both front and side views side by side. is considered a success. Similarly, if the target is ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered))이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection. (p. 2, 1 Introduction).
- **Actual contribution:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while multiple views significantly improve performance, our single-view implementation ... (p. 24, Figure/Table caption).
- **Explicit failure boundary:** Finally, the remaining failures (7%) include minor errors such as early gripper closure or collisions with the environment, which reinforcement learning could potentially address. (p. 26, C Details about Data Generation).

## 공개 자료 대조

- **코드** · 언어·영상·연속 행동 모듈을 결합하는 GraspVLA 모델. [배포 파일](https://raw.githubusercontent.com/PKU-EPIC/GraspVLA/6acd035edf7fee9ef7d90246bd9911ccf2232b8e/vla_network/model/vla/assembled_vla.py) · [저자 배포 안내](https://raw.githubusercontent.com/PKU-EPIC/GraspVLA/6acd035edf7fee9ef7d90246bd9911ccf2232b8e/README.md)
- **가중치** · 저자가 배포한 GraspVLA 모델 체크포인트. [배포 파일](https://huggingface.co/vegebirrd/GraspVLA/blob/e0b642edc7dfdf8e76cb7883320a0bbd85145f53/checkpoint/model.safetensors) · [저자 배포 안내](https://raw.githubusercontent.com/PKU-EPIC/GraspVLA/6acd035edf7fee9ef7d90246bd9911ccf2232b8e/README.md)
- **데이터** · SynGrasp-1B의 LeRobot 형식 파지 궤적 샤드. 웹 공동학습 자료는 별도 범위다. [배포 파일](https://huggingface.co/datasets/vegebirrd/SynGrasp-1B/blob/411e82e0f40b1d95e05962a9cf3d881aa76c6443/front-side-290cat-500w_lerobot/000b701e-1381-43e6-a966-d03342f30f0e/data/chunk-000/file-000.parquet) · [저자 배포 안내](https://raw.githubusercontent.com/PKU-EPIC/GraspVLA/6acd035edf7fee9ef7d90246bd9911ccf2232b8e/README.md)
