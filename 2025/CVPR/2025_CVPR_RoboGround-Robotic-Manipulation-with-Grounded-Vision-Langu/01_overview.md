# RoboGround: Robotic Manipulation with Grounded Vision-Language Priors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Haifeng Huang, Xinyi Chen, Yilun Chen, Hao Li, Xiaoshen Han, Zehan Wang, Tai Wang, Jiangmiao Pang, Zhou Zhao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLM, grounding, Robotics
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf) 기준이다.

## Why This Paper Is Here

RoboGround는 지시가 가리키는 물체와 배치 영역의 마스크를 로봇 정책에 전달해 조작 행동의 공간적 목표를 지정한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in robotic manipulation have highlighted the potential of intermediate representations for improving policy generalization.
- **p. 1 / Abstract - extractive body cue:** In this work, we explore grounding masks as an effective intermediate representation, balancing two key advantages: (1) effective spatial guidance that specifies target objects and ...
- **p. 1 / Abstract - extractive body cue:** We introduce ROBOGROUND, a groundingaware robotic manipulation policy that leverages grounding masks as an intermediate representation to guide policy networks in object manipulation tasks.
- **p. 1 / Abstract - extractive body cue:** To further explore and enhance generalization, we propose an automated pipeline for generating large-scale, simulated data with a diverse set of objects and instructions.
- **p. 1 / Abstract - extractive body cue:** Extensive experiments show the value of our dataset and the effectiveness of grounding masks as intermediate guidance, significantly enhancing the generalization abilities of robot policies.
- **p. 1 / 1. Introduction - extractive body cue:** However, it is still challenging for these methods to generalize
- **p. 1 / 1. Introduction - extractive body cue:** Research in this area typically falls into two categories: accessible yet coarse-grained representations, such as language instructions [2, 49], which are easy to generate but ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce grounding masks as a promising intermediate representation that balances two key aspects: (1) Effective spatial guidance, which not only specifies ...
- **p. 2 / 1. Introduction - extractive body cue:** To address dataset limitations, we propose an automated pipeline for generating simulated manipulation data with a diverse set of objects and instructions.
- **p. 5 / 4.3. Grounded Policy Network - extractive body cue:** To address this, we propose guiding attention toward regions defined by grounded masks, ensuring that essential information is preserved for effective manipulation.
- **p. 5 / 4.3. Grounded Policy Network - extractive body cue:** The encoded feature Zv consists of a global representation ZCLS v ∈R1×Dv, obtained from the CLS token, and a set of local patch representations ZP ...
- **p. 6 / 4.3. Grounded Policy Network - extractive body cue:** To integrate grounded masks, we introduce two additional sets of query tokens: Qo ∈Rk×Dp for the target object and Qp ∈ Rk×Dp for the target ...
- **p. 6 / 4.4. Training and Inference - extractive body cue:** Since arm actions are continuous, we use Smooth-L1 loss Larm for optimization.
- **p. 5 / 4.3. Grounded Policy Network - extractive body cue:** For the policy network, we employ a language-conditioned transformer architecture, following the GR-1 model [43].
- **p. 4 / 4.1. Overview - extractive body cue:** We then incorporate this grounding knowledge into the low-level policy network, where the grounded masks function as both an attention mechanism within the Grounded Perceiver ...

## Observation, State, and Output Interface

RoboCasa에서 만든 시연으로 팔·그리퍼 행동을 학습한다. GLaMM은 지시와 영상에서 목표와 배치 영역의 마스크를 만든다. §4의 정책은 여러 시점의 관측 이력, 로봇 상태, 지시를 받고 마스크로 영상 특징을 선택한다. 성공률은 시뮬레이션 결과다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=6)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As shown in Figure 3(b), this model processes a sequence of historical image observations, robot states and a language instruction as input to predict future robot actions. | 영상·로봇 상태·언어 지시와 VLM이 추정한 마스크 | p. 5 (4.3. Grounded Policy Network), p. 5 (4.2. Grounded Vision-Language Model) |
| State/latent | Figure, model, processes, sequence, historical, image, observations, robot, states, language, instruction, input | 목표·배치 영역에 집중한 시각 특징 | p. 5 (4.3. Grounded Policy Network), p. 5 (4.2. Grounded Vision-Language Model), p. 6 (4.4. Training and Inference) |
| Output/action | The grounded vision-language model takes an image observation and a language instruction as input and outputs binary masks for target objects and/or target placement areas specified by the instruction, as shown in ... | 팔 및 그리퍼 행동 | p. 5 (4.2. Grounded Vision-Language Model), p. 6 (4.4. Training and Inference), p. 4 (4.1. Overview) |
| Objective/outcome | For binary gripper actions, we apply Binary Cross Entropy (BCE) loss Lgripper. | 조건별 조작 성공과 마스크 품질 | p. 6 (4.4. Training and Inference), p. 6 (4.4. Training and Inference), p. 5 (4.3. Grounded Policy Network) |

## Main Claims and Actual Contribution

- 여러 물체와 지시를 포함하는 시뮬레이션 자료를 자동 생성하고 마스크 정보를 조건으로 사용하는 조작 정책을 구성했다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=5)
- 물체와 언어가 달라지는 조작 조건에서 정책 성공률을 비교하고 마스크와 학습 자료가 일반화에 주는 영향을 조사했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (5.3. Zero-shot Evaluation), p. 8 (5.4. Ablation Study) |
| Embodiment/environment | Specifically, we create an instruction-following dataset based on simulated data using the following prompt format: "Given a robotic manipulation instruction: <Instruction>, identify the target object for manipulation and, if applicable ... | hardware/simulator version and reset protocol | p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results) |
| Dataset/benchmark | In these tasks, target masks (e.g., for a drawer handle) are also generated to guide the robot's policy in precise manipulation. | role, split, size and leakage | p. 8 (5.4. Ablation Study), p. 7 (5.2. Main Results), p. 6 (5.1. Simulation Setting), p. 6 (5.2. Main Results) |
| Metric | Metrics for pick-and-place tasks are reported as "a / b", where a is the contact rate (%) and b is the success rate (%). | definition, denominator, direction and uncertainty | p. 6 (5.2. Main Results), p. 6 (5.2. Main Results), p. 7 (5.2. Main Results) |
| Baseline/ablation | Compared to baseline models, our method consistently outperforms across all tasks. | fair input/data/compute/action matching | p. 7 (5.2. Main Results), p. 6 (5.2. Main Results), p. 6 (5.2. Main Results) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Data Generation Pipeline. The pipeline is composed of three key stages: (a) First, we extract informative object attributes in both keyword and descriptive ...
- **p. 7 / 5.2. Main Results - extractive body cue:** This limitation likely arises from design shortcomings, as these models encode language input as a single, global text feature, which is inadequate for the nuanced ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.4. Training and Inference), p. 5 (4.3. Grounded Policy Network)이다.
