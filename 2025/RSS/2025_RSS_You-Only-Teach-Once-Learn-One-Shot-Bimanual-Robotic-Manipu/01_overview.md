# You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p149.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p149.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: Huayi Zhou, Ruixiang Wang, Yunxin Tai, Yueci Deng, Guiliang Liu, Kui Jia
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, bimanual manipulation, human video, Imitation Learning, diffusion policy, long-horizon
- Official paper: https://www.roboticsproceedings.org/rss21/p149.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p149.pdf
- Code/Project: https://hnuzhy.github.io/projects/YOTO
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

YOTO는 사람의 양손 시연을 한 번 스테레오로 관찰해 얻은 동작을 여러 변형 시연으로 확장하고 양팔 정책을 학습한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p149.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Bimanual robotic manipulat challenge of embodied intelligence duc
- **p. 1 / Abstract - extractive body cue:** dual-arm spatialtemporal coordination and high-dimensional
- **p. 1 / Abstract - extractive body cue:** ies or direct teleoperation to alleviate or circumvent these i sues, often making them lack simplicity, versatility and scalability Differently, we believe that the most ...
- **p. 1 / Abstract - extractive body cue:** ach Once), which can extract and then inject patterns of bimanual actions from as few as a single binocular observation of hand movements, and teach ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, based on keyframes= based motion trajectories, we devise as fe if training demonstrations
- **p. 4 / A. Problem Formulation - extractive body cue:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for ...

## Core Idea

- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the ...
- **p. 4 / A. Problem Formulation - extractive body cue:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 1) Spaces of observation and action: We adopt a 13 ‘dimensional proprioception vector and a 7-dimensional action, space for each robot arm, respectively. ‘The proprioception ...
- **p. 5 / B. Hand Motion Extraction and Injection - extractive body cue:** In the following, we show that the extracted fine-grained keyframes-based motion actions A along with the corresponding motion mask C will continue to play a ...
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** This core design relies on the stil rapidly developing capabilities of vision foundation models (VEMs).
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** 2) Network architecture: In all tasks, we use a SIM(3)- equivariant PointNet++ (96, 95] with 4 layers and hidden dimensionality 128 as the ‘feature encoder.
- **p. 17 / A. Implementation Details of Our BiDP - extractive body cue:** For the noise prediction network, we inherits hyperparameters from the ‘original Diffusion Policy [15], Specifically, to optimize for inference speed in all experiments, we use ...
- **p. 4 / B. Hand Motion Extraction and Injection - extractive body cue:** Then, we leverage favourable vision techniques to extract rich manipulation features from recorded videos by a single binocular ‘camera, Extracted features will be post-processed to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | For all our bimanual tasks, the observation horizon is set to 1, so we only use the initial state observation of the left arm as one of the network inputs. | observation history와 expert trajectory/action | p. 17 (A. Implementation Details of Our BiDP), p. 4 (A. Problem Formulation) |
| State/latent | bimanual, tasks, observation, horizon, only, initial, state, left, network, inputs, action, space | behavior policy와 temporal action context | p. 17 (A. Implementation Details of Our BiDP), p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation) |
| Output/action | As for the action space A= {a? & R¥,a" © SO(3),a & {0,1}}. it includes the target 6-DoF pose of each robot arm and the binary openiclosed state of the gripper. | predicted action 또는 action chunk | p. 4 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP) |
| Objective/outcome | The learning objective can be simply ‘concluded as maximum likelihood observation-conditioned, imitation objective to learn the policy =: | imitation error, task success, robustness와 compounding error | p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP), p. 17 (A. Implementation Details of Our BiDP) |

## Main Claims and Actual Contribution

- 양손 궤적의 핵심 프레임을 추출한 뒤 물체와 배치를 바꾼 시연을 생성해 양팔 확산 정책의 학습 자료로 사용한다. [PDF 4쪽](https://www.roboticsproceedings.org/rss21/p149.pdf#page=4) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p149.pdf#page=6)
- 다단계 양팔 조작 다섯 개에서 성공률을 측정하고 시각·공간 조건 변화와 설계 요소의 효과를 비교했다. [PDF 8쪽](https://www.roboticsproceedings.org/rss21/p149.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss21/p149.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (B. Results Comparison), p. 9 (B. Results Comparison) |
| Embodiment/environment | We then processed these data into the form suitable for BiDP, including extracting 3D point clouds of manipulated objects and saving the corresponding multi-step end-effector keyposes Note that we also recorded the ... | hardware/simulator version and reset protocol | p. 8 (A. Experiment Setups), p. 7 (A. Experiment Setups) |
| Dataset/benchmark | The task pull drawer with 243 episodes is used to train all models. | role, split, size and leakage | p. 8 (A. Experiment Setups), p. 7 (A. Experiment Setups), p. 8 (A. Experiment Setups), p. 11 (B. Results Comparison) |
| Metric | ‘TABLE V: Comparison of the average success rate of various ‘methods on all five tasks (in-distribution evaluations), | definition, denominator, direction and uncertainty | p. 9 (B. Results Comparison), p. 9 (B. Results Comparison), p. 10 (B. Results Comparison) |
| Baseline/ablation | also makes our model more robust compared to all baselines The core idea here is to rely on the still rapidly developing capabilities of vision foundation models, such as the open voccabulary ... | fair input/data/compute/action matching | p. 11 (B. Results Comparison), p. 8 (A. Experiment Setups), p. 8 (B. Results Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 11 / VI. CONCLUSION AND Limitation - extractive body cue:** In short, these limitations highlight the need for further innovations to enhance robustness, generalization, and scalability in bimanual robot manipulation,
- **p. 11 / VI. CONCLUSION AND Limitation - extractive body cue:** tation: Although YOTO has achieved impressive performance on various long-horizon bimanual manipulation tasks, we conclude that it has at least the following limitations.
- **p. 21 / Figure/Table caption - extractive body cue:** Fig. 15: From top to bottom, we have examples of failed cases in all five tasks during evaluation, We have outlined and magnified the areas ...
- **p. 9 / B. Results Comparison - extractive body cue:** Firstly, when directly applying advanced 3D hand mesh reconstruction methods (ei ther HaMeR [67] or WiLoR [71)) the resulting hand trajectory is always unstable and ...
- **p. 8 / B. Results Comparison - extractive body cue:** Here, we answer the questions raised at the beginning one by one, including basic in-distribution results and generalizations to out-of-distribution settings,
- **p. 8 / A. Experiment Setups - extractive body cue:** Although above tests have new variations in object placements, we choose two tasks pul drawer and uncover 1id to perform more challenging ‘out-of-distribution (QOD) evaluations ...
- **p. 10 / B. Results Comparison - extractive body cue:** (Q3) BIDP has satisfactory out-of-domain generalization To further illustrate the superiority of BIDP, we de~ signed tests under out-of-distribution (OOD) settings.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (A. Problem Formulation), p. 17 (A. Implementation Details of Our BiDP), p. 4 (B. Hand Motion Extraction and Injection), p. 5 (B. Hand Motion Extraction and Injection)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Next, we present how to obtain sufficient training demonstrations proliferated from only a single-shot human teaching and how to improve existing diffusion-based imitation policies for addressing the bimanual manipulation problem. (p. 4, A. Problem Formulation).
- **Actual contribution:** As an altemative, we propose to project all 3D points {f!"°}/_, onto the 2D image, nd then lft these points to 3D by applying the stereo matching algorithm {92}. (p. 4, B. Hand Motion Extraction and Injection).
- **Evaluation boundary:** ong-horizon bimanual manipulation tasks, the existing stateof-the-art methods still have a lot of room for improvement, such as the gradually decaying effect over multiple substeps and less exploration of efficient ... (p. 10, B. Results Comparison).
- **Explicit failure boundary:** Due to space limitations, we did not continue the demonstration proliferation and policy training. (p. 11, B. Results Comparison).
