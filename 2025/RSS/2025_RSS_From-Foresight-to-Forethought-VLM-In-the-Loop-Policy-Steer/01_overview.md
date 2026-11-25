# From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p076.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p076.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Yilin Wu, Ran Tian, Gokul Swamy, Andrea Bajcsy
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, VLM verifier, policy steering, failure prevention, latent alignment
- Official paper: https://www.roboticsproceedings.org/rss21/p076.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p076.pdf
- Code/Project: https://yilin-wu98.github.io/forewarn/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

FOREWARN은 생성 정책이 제안한 행동들의 결과를 잠재 세계 모델로 예측한 뒤 시각언어모델의 판단으로 실행할 행동을 고른다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p076.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While generative robot policies have demonstrated significant potential in learning complex, multimodal behaviors from demonstrations, they still exhibit diverse failures at eployment-time, Policy steering offers ...
- **p. 1 / Abstract - extractive body cue:** Here, one might hope to use a Vision Language Model (VLM) as a verifier leveraging its open-world reasoning capa bilities.
- **p. 1 / Abstract - extractive body cue:** However, off-the-shelf VLMs struggle to understand the ‘consequences of low-level robot actions as they are represented Tandamentally differently than the text and images the VIM ...
- **p. 1 / Abstract - extractive body cue:** In response, we propoxe FOREWARN, a novel Framework to unlock the potential of VLMs as open-vocabulary verifies for runtime poliy steering.
- **p. 1 / Abstract - extractive body cue:** Our key idea i to decouple the VEM's burden of predicting action outcomes Voresight) from ‘valuation forethought.
- **p. 3 / 1. InTRopucTION - extractive body cue:** Initially, it may be tempting use the VLM directly as a black-box solver of Eq.1 (ie. t0 solve the overarching behavior generation problem) by simply ...
- **p. 1 / 1. InTRopucTION - extractive body cue:** However, at runtime, the policy exhibits a range of degradations, from complete task failures (such as the robot knocking down the cup during grasping, shown ...

## Core Idea

- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag tasks ...
- **p. 4 / 1. InTRopucTION - extractive body cue:** The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** Ultimately, this alignment step enables ‘our "VLM-in-the-loop" policy steering approach to interpret, action plans as behavior narrations and select high-quality plans by reasoning over those ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 1: We present FOREWARN, an VLM-in-the-loop policy steering algorithm for multi-modal generative robot policies.
- **p. 1 / Abstract - extractive body cue:** We validate our framework across diverse robotic manipulation tasks, demonstrating its ability to bridge representational gaps and provide robust, generalizable policy steering.
- **p. 9 / B. Policy Steering for Open-World Alignment - extractive body cue:** Our system queries the VLM twice to first generate behavior narrations and then select the best action plan, The overall inference time is 3.7 seconds ...
- **p. 6 / A. From Action Rollouts to Behavior Narration - extractive body cue:** This method uses the encoder £4 on ground-truth future observations 10 get privileged (posterior) future latent states Zeer as input for the VLM.
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** This indicates that the VLM struggles to reason directly about predicted action outcomes from the world model's latent states and essentially degrades toa traditional end-to-end ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The robot's observations 0 < O :=ZxQ combine RGB image data I € T and proprioceptive states q © Q(eg., end-effector pose, gripper state), and ay := ay.¢.7 denotes a robot's T ... | observation, uncertainty/risk estimate와 task command | p. 3 (1. InTRopucTION), p. 4 (1. InTRopucTION) |
| State/latent | robot, observations, ZxQ, combine, RGB, image, data, proprioceptive, states, end-effector, pose, gripper | safe set, recovery state 또는 constraint margin | p. 3 (1. InTRopucTION), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION) |
| Output/action | The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world model to accurately predict the outcomes of ... | shielded, recovery 또는 safe action | p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 2 (1. InTRopucTION) |
| Objective/outcome | Inthe Bag task, we modify the original task description from "Please pick up a bag of chips from the table and minimize the contact region to avoid crushing contents inside" to 4 ... | task return과 violation/failure probability | p. 8 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), p. 9 (B. Policy Steering for Open-World Alignment) |

## Main Claims and Actual Contribution

- 계획별 미래 잠재 상태를 언어 표현에 정렬해 행동의 결과를 서술하고 과제 기준으로 평가할 수 있게 한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p076.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p076.pdf#page=4)
- 예측한 행동 설명과 실제 결과의 일치도, 그리고 계획 선택이 최종 조작 성공률에 주는 영향을 구분해 측정했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p076.pdf#page=6) · [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p076.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Embodiment/environment | We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Dataset/benchmark | In this task, the robot must pick up a fork from the table and place it inside a bowl. | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | V-A).Then we evaluate the closed: loop policy steering performance as well as our method' robustness to novel task descriptions, £ (Sec. | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 3: Examples of Behavior Narrations Predicted by Each Approach. The top row displays the ground-truth robot ‘observations and the prompt used for querying VLMs. Only FOREWARN and FOREWARN-Oracle consistently produce accurate ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use this task to study how our framework performs when faced with harder-to-predict interaction outcomes and nuanced failures (e.g., crushing the chips inside the ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** (4) Classfier-Dyn-Latent, which is similar to VLM-DynLat-Category, but instead of relying ‘on a VLM, it directly takes the predicted latent embeddings Seq 88 input and ...
- **p. 9 / VI. Limrrations - extractive body cue:** B2 revealed that our system's primary failures stem from the world model's imprecise "imagination", exacerbated by our limited training data.
- **p. 9 / VI. Limrrations - extractive body cue:** Our experiments across diverse manipulation tasks confirm that FOREWARN not only provides interpretable and reliable failure detection, but also significantly enhances policy success rates through ...
- **p. 8 / B. Policy Steering for Open-World Alignment - extractive body cue:** In contrast, the baselines either fail to interpret action outcomes effectively, resulting in unsafe behaviors, or experience severe performance degradation in novel task specifications.
- **p. 7 / A. From Action Rollouts to Behavior Narration - extractive body cue:** As shown in Table 1, these methods fall behind FOREWARN by at least 30% in GT Accuracy und 16% in LLM Score.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1. InTRopucTION), p. 1 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 9 (B. Policy Steering for Open-World Alignment)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, this strategy is sampleinefficient, requiring extensive embodied rollouts and human annotations to generate labels, Instead, we propose tackling the problem in Eq.1 in a way that leverages the unique ... (p. 3, 1. InTRopucTION).
- **Actual contribution:** Ultimately, this alignment step enables ‘our "VLM-in-the-loop" policy steering approach to interpret, action plans as behavior narrations and select high-quality plans by reasoning over those narrations even under novel task ... (p. 2, 1. InTRopucTION).
- **Evaluation boundary:** In this task, the robot must pick up a fork from the table and place it inside a bowl. (p. 5, V. EXPERIMENTS).
- **Explicit failure boundary:** However, at runtime, the policy exhibits a range of degradations, from complete task failures (such as the robot knocking down the cup during grasping, shown in the center of Figure ... (p. 1, 1. InTRopucTION).

## 원문과 공개 자료

- RSS 게재본에서 두 번째 저자가 사용하는 이름은 Ran Tian이다. [표제면](https://www.roboticsproceedings.org/rss21/p076.pdf#page=1)
- 가중치 · FOREWARN 봉투 조작 세계 모델의 저장 가중치 · bag_ckpt/0106/234547/best_pretrain_joint_444_68.pt [배포 파일](https://huggingface.co/yilin-wu/Forewarn_WMs/blob/3ab74faba14db800dc4d5e085fca9008d2a33d18/bag_ckpt/0106/234547/best_pretrain_joint_444_68.pt)
- 코드 · 기본 정책 후보를 잠재 세계 모델과 VLM으로 평가하는 실행 루프 · examples/policy_loop.py [배포 파일](https://raw.githubusercontent.com/CMU-IntentLab/Forewarn/7e0b505436a7c9702b0fdcfef3d2b897f102906f/examples/policy_loop.py)
- 데이터 · FOREWARN 봉투 조작 세계 모델 학습 시연 · GraspBag_data/GraspBag_demo.hdf5 [배포 파일](https://huggingface.co/datasets/yilin-wu/Forewarn_WM_data/blob/63adf739cc1e5a0330e59bcfa0cbee5729c4f0f3/GraspBag_data/GraspBag_demo.hdf5)
