# Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Taowen Wang, Cheng Han, James Liang, Wenhao Yang, Dongfang Liu, Luna Xinyu Zhang, Qifan Wang, Jiebo Luo, Ruixiang Tang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 2. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

로봇 VLA의 시각 입력이 교란됐을 때 행동과 과제 성공이 얼마나 달라지는지 시뮬레이션과 실물에서 평가했다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recently in robotics, Vision-Language-Action (VLA) models have emerged as a transformative approach, enabling robots to execute complex tasks by integrating visual and linguistic inputs within ...
- **p. 1 / Abstract - extractive body cue:** Despite their significant capabilities, VLA models introduce new attack surfaces.
- **p. 1 / Abstract - extractive body cue:** This paper systematically evaluates their robustness.
- **p. 1 / Abstract - extractive body cue:** Recognizing the unique demands of robotic execution, our attack objectives target the inherent spatial and functional characteristics of robotic systems.
- **p. 1 / Abstract - extractive body cue:** In particular, we introduce two untargeted attack objectives that leverage spatial foundations to destabilize robotic actions, and a targeted attack objective that manipulates the robotic ...
- **PDF p. 2, §1 / contribution list (DOC-QA2 원문 대조):** Visual adversarial patch와 VLA-specific attack objective를 제시하고 simulation 및 real-world setting에서 평가한다. 추출된 C1 문자는 contribution 목록의 원형 숫자 3 기호였다.
- **p. 1 / 1. Introduction - extractive body cue:** Failure Rate Comparison BV2 LIBERO A.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom.
- **p. 3 / 3. Methodology - extractive body cue:** Finally, we introduce the Normalized Action Discrepancy (NAD) metric in §3.5.
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** To exacerbate action discrepancies, we introduce the Untargeted Action Discrepancy Attack (UADA), which aims to maximize deviations in robot actions.
- **p. 4 / 3.3. Untargeted Position-aware Attack - extractive body cue:** Recognizing the importance of Ap = DT(yp) in controlling the end-effector's path, we introduce a position-aware attack to disrupt the intended movement trajectory.
- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** By categorizing action values into discrete class labels, the model converts continuous probability outputs into discrete signals, this simplification facilitates quicker convergence and faster training ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** To define UADA's objective, we first identify the most distant action yi adv, which maximizes the discrepancy from the i-th DoF ground truth action yi.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2) are built on large language models integrated with visual encoders, enabling robots to interpret human instructions and process visual input from a camera to perform context-aware actions. | image/video, language instruction, proprioception과 history | p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack) |
| State/latent | built, large, language, models, integrated, visual, encoders, enabling, robots, interpret, human, instructions | language-grounded task state와 action-policy context | p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack) |
| Output/action | This attack is based on the observation that larger robot actions usually correlate with intense physical movements, which, in turn, may amplify the potential for real-world hazards [28-30]. | continuous action, pose 또는 action chunk | p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack) |
| Objective/outcome | Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient optimization and stable attack performance. | instruction following, task success, generalization과 latency | p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack) |

## Main Claims and Actual Contribution

- 과제 실패와 행동 편차를 서로 다른 지표로 측정해 LIBERO 과제의 결과를 비교했다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf#page=1) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf#page=7)
- 실물 실험과 추가 진단을 통해 평가 환경 및 과제에 따라 정책의 시각적 견고성이 달라질 수 있음을 보였다. [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.3. Main Result), p. 8 (4.3. Main Result) |
| Embodiment/environment | The increased variability in real-world data, including environmental complexity, object diversity, and task difficulty, allows the robot more opportunities to generate larger action discrepancies within the validation dataset. | hardware/simulator version and reset protocol | p. 6 (4.3. Main Result), p. 6 (4.2. Experiment Setup) |
| Dataset/benchmark | These findings underscore a pressing security concern during the deployment of generalist robots, especially when considering application scenes that require reliable operations [11, 68]. | role, split, size and leakage | p. 6 (4.3. Main Result), p. 6 (4.2. Experiment Setup), p. 7 (4.3. Main Result), p. 8 (4.3. Main Result) |
| Metric | Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as well without the need for further adaptations. | definition, denominator, direction and uncertainty | p. 8 (4.3. Main Result), p. 8 (Figure/Table caption), p. 6 (4.2. Experiment Setup) |
| Baseline/ablation | Therefore, we adapt prior work in adversarial learning as one of our baseline methods [66]. | fair input/data/compute/action matching | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 4 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ...
- **p. 6 / 4.3. Main Result - extractive body cue:** Both UADA and UPA effectively disrupt robot execution, yielding maximum average failure rates of 100% and 89.7%, respectively.
- **p. 6 / 4.3. Main Result - extractive body cue:** For UADA and UPA, our methods effectively amplify action discrepancies, leading to a notable transfer attack ability in increasing failure rates (see Tab.
- **p. 7 / 4.3. Main Result - extractive body cue:** Failure Rate (FR, ↑) and its standard deviation across tasks within LIBERO [44] suite are reported.
- **p. 7 / 4.3. Main Result - extractive body cue:** This failure can be attributed to the fact that DoF4 controls the orientation along the x-axis, which can be redundant DoF in tasks.
- **p. 8 / 4.3. Main Result - extractive body cue:** The figure shows how varying Inner-loop affects NAD in UADA, and patch sizes affect L1 distance and the failure rates in TMA, both targeting at ...
- **p. 8 / 4.3. Main Result - extractive body cue:** (a) Impact of Inner-loop, (b) Impact of Patch Size and (c-f) the effect of four different defenses on failure rates. generated with UADA demonstrated the ...

## Why Read It

VLA의 visual adversarial patch가 action에 미치는 취약성을 읽기 위한 논문이다. PDF p. 2의 contribution 목록은 attack objective와 simulation/real-world 평가를 설명한다. 손상된 항목 번호를 본문 내용으로 읽거나 평가 범위를 보편적 안전 보장으로 확대하지 않는다. (DOC-QA2 원문 대조)
