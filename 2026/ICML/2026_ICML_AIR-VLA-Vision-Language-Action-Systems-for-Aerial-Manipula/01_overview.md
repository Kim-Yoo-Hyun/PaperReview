# AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=NuR4lG4gKB.
> PDF retrieval source: https://openreview.net/pdf/fa8a077d4c454280e6633258b55a9ff0b4d204e5.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Benchmark
- Official paper: https://openreview.net/forum?id=NuR4lG4gKB
- Full-text retrieval: https://openreview.net/pdf/fa8a077d4c454280e6633258b55a9ff0b4d204e5.pdf
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, extending VLA models to aerial platforms introduces unique physical and control challenges.를 문제로 두고, The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed for AMS, filling the evaluation gap in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose AIR-VLA, the first VLA training and evaluation benchmark designed specifically for Aerial Manipulation Systems.
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success rate in Base ...
- **p. 8 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task scenarios and instruction types.
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in the AIR-VLA evaluation, outperforming traditional imitation learning baselines such ...
- **p. 7 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** Notably, Qwen3-VL achieves state-ofthe-art (SOTA) performance across all baseline models in four core dimensions: Process Planning, Spatial Navigation, Object Grounding, and Skill Selection, highlighting its ...
- **p. 7 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** In-depth analysis indicates that this lack of 3D spatial awareness is the primary bottleneck limiting the end-to-end planning Success Rate.
- **p. 4 / 3.2. Evaluation Framework - extractive body cue:** To comprehensively evaluate the limit performance of embodied intelligence models in this high-dimensional domain, we constructed a two-layer evaluation framework covering perception, planning, and control.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, extending VLA models to aerial platforms introduces unique physical and control challenges.를 문제로 두고, The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed for AMS, filling the evaluation gap in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 5 (3.4. Dataset Construction), p. 5 (3.4. Dataset Construction), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
