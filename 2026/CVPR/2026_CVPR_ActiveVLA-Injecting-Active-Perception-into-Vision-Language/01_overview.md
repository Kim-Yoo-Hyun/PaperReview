# ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Zhenyang Liu, Yongchong Gu, Yikai Wang, Xiangyang Xue, Yanwei Fu
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, active perception, 3D manipulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf
- Code/Project: https://zhenyangliu.github.io/ActiveVLA/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

ActiveVLA는 조작에 중요한 3D 영역을 먼저 찾고 그 영역의 관측 방향과 해상도를 조절해 행동을 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf#page=1) · [PDF 2쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in robot manipulation have leveraged pretrained vision-language models (VLMs) and explored integrating 3D spatial signals into these models for effective action prediction, giving ...
- **p. 1 / Abstract - extractive body cue:** However, most existing approaches overlook the importance of active perception: they typically rely on static, wrist-mounted cameras that provide an end-effector-centric viewpoint.
- **p. 1 / Abstract - extractive body cue:** As a result, these models are unable to adaptively select optimal viewpoints or resolutions during task execution, which significantly limits their performance in long-horizon tasks ...
- **p. 1–2 / Abstract - 원문 대조 요지:** ActiveVLA는 정밀 조작에 필요한 영역을 찾아 관측 시점과 공간 해상도를 조절한다.
- **p. 1 / Abstract - extractive body cue:** Except for this watermark, it is identical to the accepted version; the final published version of the proceedings is available on IEEE Xplore.
- **p. 2 / 1. Introduction - extractive body cue:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this limitation is crucial for developing embodied agents capable of adaptive and reliable interaction in complex, real-world environments.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose ActiveVLA, a novel vision-language-action framework that explicitly integrates active perception into robotic manipulation.
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** This global-local fusion allows the model to combine overall scene understanding with fine spatial precision, enabling accurate and safe manipulation in complex environments.
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: ...
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** All tokens are concatenated and passed through an MLP head to predict rotation, gripper, and collision actions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA designs a novel coarse-to-fin ... | image/video, language instruction, proprioception과 history | p. 3 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | framework, equips, robots, active, perception, capabilities, enabling, adaptive, viewpoint, selection, zoomin, mechanisms | language-grounded task state와 action-policy context | p. 3 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | This closed-loop, coarse-to-fine perception-action pipeline allows ActiveVLA to dynamically adapt its sensory inputs and maintain high effectiveness across complex, multi-step, and long-horizon manipulation tasks. | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. 3D Action Prediction) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 여러 투영 영상에서 중요한 영역을 찾은 뒤 가림과 시점의 다양성을 고려해 관측을 고르고 국소 3D 영역을 확대한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf#page=4)
- GemBench의 일반화 과제와 구성 요소 제거 실험으로 시점 선택과 국소 확대가 조작 성공에 미치는 영향을 평가했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results) |
| Embodiment/environment | Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 7 (4.1. Experimental Results) |
| Dataset/benchmark | RLBench [23] features 18 tasks using a Franka Panda robot with RGB-D inputs from four calibrated cameras and 100 demonstrations per task. | role, split, size and leakage | p. 6 (4. Experiments), p. 7 (4.1. Experimental Results), p. 6 (4. Experiments), p. 8 (4.1. Experimental Results) |
| Metric | Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 6 Number of View 80.0 82.0 84.0 86.0 ... | definition, denominator, direction and uncertainty | p. 8 (4.2. Ablation Study), p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results) |
| Baseline/ablation | We compare ActiveVLA with state-of-the-art baselines. | fair input/data/compute/action matching | p. 6 (4. Experiments), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, ...
- **p. 6 / 4. Experiments - extractive body cue:** COLOSSEUM [48] extends RLBench with 12 perturbation types involving object, scene, and camera variations for robustness evaluation.
- **p. 7 / 4.1. Experimental Results - extractive body cue:** It remains robust to variations in object size, color, lighting, and texture, obtaining 72.4% on MO-SIZE and 64.4% on RO-SIZE.
- **p. 8 / 4.2. Ablation Study - extractive body cue:** Adding A-VS dynamically selects informative views, raising performance to 89.4% at 0.45 s by improving scene coverage and reducing occlusion.
- **p. 8 / 4.1. Experimental Results - extractive body cue:** It actively perceives and precisely completes tasks despite severe occlusions and complex spatial structures. baselines such as 3D-LOTUS++ and BridgeVLA.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (1. Introduction), p. 5 (3.3. 3D Action Prediction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action. (p. 2, 1. Introduction).
- **Actual contribution:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 (p. 2, 1. Introduction).
- **Evaluation boundary:** Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and an average rank of 1.07, outperforming ... (p. 7, 4.1. Experimental Results).
- **Explicit failure boundary:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, 65.6%). (p. 6, 4.1. Experimental Results).

## 원문과 공개 자료

- 코드 · 저자 저장소는 학습·추론 코드와 실물 제어 코드 공개를 미완료 항목으로 명시한다. [저자 공개 안내](https://github.com/ZhenyangLiu/ActiveVLA-Injecting-Active-Perception-into-VLA/blob/4450b1188a24f3f1d1d3fb3e47d226d150b9e470/README.md)
- 데이터 · 저자 저장소는 ActiveVLA 코드를 비롯한 데이터 공개를 준비 중이라고 명시한다. [저자 공개 안내](https://github.com/ZhenyangLiu/ActiveVLA-Injecting-Active-Perception-into-VLA/blob/4450b1188a24f3f1d1d3fb3e47d226d150b9e470/README.md)
