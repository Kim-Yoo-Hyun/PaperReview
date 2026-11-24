# AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v306/sun26an.html.
> PDF retrieval source: https://openreview.net/pdf/fa8a077d4c454280e6633258b55a9ff0b4d204e5.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Jianli Sun, Bin Tian, Qiyao Zhang, Chengxiang Li, Song Zihan, Zhiyong Cui, Yisheng Lv, Yonglin Tian
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Benchmark
- Official paper: https://proceedings.mlr.press/v306/sun26an.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v306/main/assets/sun26an/sun26an.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.
- Metadata refresh: 2026-10-25 PMLR ICML 2026 공식 proceedings metadata 재확인. 기존 OpenReview PDF의 본문 검토 근거는 보존하며 final 본문 동등성은 재검토하지 않았다.

## Why This Paper Is Here

AIR-VLA는 공중에 떠 있는 기체와 부착된 로봇팔이 함께 물체를 조작할 때 정책을 평가하기 위한 물리 시뮬레이션 벤치마크다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=1) · [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action (VLA) models have achieved remarkable success in groundbased embodied intelligence, their application to Aerial Manipulation Systems (AMS) remains a largely unexplored frontier.
- **p. 1 / Abstract - extractive body cue:** The inherent characteristics of AMS, including floating-base dynamics, strong coupling between the UAV and the manipulator, and the multi-step, long-horizon nature of operational tasks, pose ...
- **p. 1 / Abstract - extractive body cue:** February 4, 2026. to existing VLA paradigms designed for static or 2D mobile bases.
- **p. 1 / Abstract - extractive body cue:** To bridge this gap, we propose AIR-VLA, the first VLA benchmark specifically tailored for aerial manipulation.
- **p. 1 / Abstract - extractive body cue:** We construct a physics-based simulation environment and release a high-quality multimodal dataset comprising 3000 manually teleoperated demonstrations, covering base manipulation, object & spatial understanding, semantic ...
- **p. 2 / 1. Introduction - extractive body cue:** However, extending VLA models to aerial platforms introduces unique physical and control challenges.
- **p. 2 / 1. Introduction - extractive body cue:** However, existing VLA research is predominantly confined to Ground Mobile Manipulators, where the operational space is restricted to 2D planar navigation and limited working heights.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose AIR-VLA, the first VLA training and evaluation benchmark designed specifically for Aerial Manipulation Systems.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Standardized data interfaces ensure compatibility with the input layers of diverse VLA models.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Tailored to aerial perspectives, the sensor configuration comprises: (1) a UAV front-down RGB-D camera for global bird's-eye views, (2) a manipulator wrist RGB-D camera for ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Tailored to the unique characteristics of aerial operations, we design a multi-suite dataset rich in sensory information (RGB, depth, proprioception) and diverse language instructions, providing high-quality data support for training ae ... | standardized observation, action, task state와 evaluation split | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | Tailored, unique, characteristics, aerial, operations, design, multi-suite, dataset, rich, sensory, information, RGB | benchmark state/goal와 method decision | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Output/action | Recently, VisionLanguage-Action (VLA) models, represented by RT-1 (Brohan et al., 2023), OpenVLA (Kim et al., 2024), and π0 (Black et al., 2026), have demonstrated exceptional capability in handling open-world tasks driven by ... | policy/controller trajectory 또는 measured result | p. 2 (1. Introduction), p. 3 (1. Introduction), p. 5 (3.4. Dataset Construction) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 기체·팔·그리퍼의 동작을 함께 기록하는 환경을 만들고 사람이 원격조작한 시연 3,000개를 시각·언어·행동 자료로 정리했다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=1) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=5)
- 시뮬레이션에서 VLA들의 공중 조작 수행 점수를 비교하고, 고수준 VLM의 절차 계획·공간 판단·물체 지시·기술 선택은 별도의 지표로 평가했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/sun26an/sun26an.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS) |
| Embodiment/environment | Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, and temporal complexity of long-horizon tasks. | hardware/simulator version and reset protocol | p. 4 (3.2. Evaluation Framework), p. 5 (4.1. VLA Experiments) |
| Dataset/benchmark | The training dataset is derived from our human-teleoperated simulation data, fully reflecting the 5 | role, split, size and leakage | p. 4 (3.2. Evaluation Framework), p. 5 (4.1. VLA Experiments), p. 5 (4.1.1. EXPERIMENTAL SETUP), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |
| Metric | The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task scenarios and instruction types. | definition, denominator, direction and uncertainty | p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS) |
| Baseline/ablation | Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in the AIR-VLA evaluation, outperforming traditional imitation learning baselines such as ACT and Diffusio ... | fair input/data/compute/action matching | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 4 (3.2. Evaluation Framework) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Notably, in spatial understanding tasks, the models exhibit Spatial Grounding Failure: although the correct object category is identified, the agent manipulates an identical object at ...
- **p. 7 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** In summary, VLMs hold immense potential for high-level planning in aerial manipulation, particularly in mitigating the long-horizon reasoning limitations of VLA models.
- **p. 8 / 5. Conclusion - extractive body cue:** Our findings reveal that while transferring pre-trained VLA models to aerial platforms is feasible, existing models still face severe challenges in handling floating-base dynamic coupling, ...
- **p. 7 / 4.2. VLM Experiments - extractive body cue:** Robustness evaluation of π0.5 under disturbance and perception-deprived conditions.
- **p. 5 / 4.1. VLA Experiments - extractive body cue:** Q2: Can VLA models cope with external disturbances in AMS and complete tasks under random base jitter?
- **p. 5 / 4.1.1. EXPERIMENTAL SETUP - extractive body cue:** Diffusion Policy (Chi et al., 2024) utilizes conditional diffusion for iterative denoising, robustly handling multi-modal distributions essential for floating-base stability.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (1. Introduction), p. 5 (3.4. Dataset Construction), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS)이다.
