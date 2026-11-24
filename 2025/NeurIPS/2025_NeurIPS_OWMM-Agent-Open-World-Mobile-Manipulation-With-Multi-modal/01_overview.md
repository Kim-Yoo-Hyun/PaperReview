# OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/115408.
> PDF retrieval source: https://arxiv.org/pdf/2506.04217. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Junting Chen, Haotian Liang, Lingxiao Du, Weiyun Wang, Mengkang Hu, Yao Mu, Wenhai Wang, Jifeng Dai, Ping Luo, Wenqi Shao, Lin Shao
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Official paper: https://neurips.cc/virtual/2025/poster/115408
- Published PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf
- Full-text retrieval at original review: https://arxiv.org/pdf/2506.04217
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

OWMM-Agent는 여러 시점의 장면 기억과 현재 로봇 상태를 함께 읽고 조작·이동 함수를 호출해 개방형 이동 조작 지시를 수행한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The rapid progress of navigation, manipulation, and vision models has made mobile manipulators capable in many specialized tasks.
- **p. 1 / Abstract - extractive body cue:** However, the open-world mobile manipulation (OWMM) task remains a challenge due to the need for generalization to open-ended instructions and environments, as well as the ...
- **p. 1 / Abstract - extractive body cue:** To address this complexity, we propose a novel multi-modal agent architecture that maintains multi-view scene frames and agent states for decision-making and controls the robot ...
- **p. 1 / Abstract - extractive body cue:** A second challenge is the hallucination from domain shift.
- **p. 1 / Abstract - extractive body cue:** To enhance the agent performance, we further introduce an agentic data synthesis pipeline for the OWMM task to adapt the VLM model to our task ...
- **p. 2 / 1 Introduction - extractive body cue:** However, directly applying pre-trained VLMs to our embodied agent presents challenges of domain shift: 1) Rare grounding tasks: Robotic planners and controllers require multi-modal inputs, ...
- **p. 2 / 1 Introduction - extractive body cue:** A central difficulty in OWMM is the need for comprehensive global scene understanding and reasoning conditioned on natural language instructions and agent state.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose OWMM-Agent, a unified VLM-based agent architecture for open-world mobile manipulation, capable of global scene understanding, ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on the aforementioned observations, we propose a novel VLM agent framework, OWMM-Agent, to address these challenges and leverage the power of VLMs for OWMM ...
- **p. 3 / 1 Introduction - extractive body cue:** • We introduce a foundation model for OWMM, capable of multi-image reasoning and executable multi-modal action generation, with extensive experiments analyzing the model's performance.
- **p. 4 / 3 Methodology - extractive body cue:** The overview of our method is shown in Figure 2.
- **p. 4 / 3 Methodology - extractive body cue:** In this section, we introduce the definition of OWMM in section 3.1.
- **p. 5 / 3 Methodology - extractive body cue:** Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to ...
- **p. 6 / 3 Methodology - extractive body cue:** We instruct the VLM model to monitor the state through robot history and to infer the subsequent action by considering both the history and the ...
- **p. 4 / 3 Methodology - extractive body cue:** The right panel showcases the Agent Space, where OWMM-VLM processes task instructions, robot history, and visual inputs to perform chain-of-thought reasoning and generate high-level actions ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Thus, we introduce a pose graph G and associated RGB images I as the output of the pre-mapping stage on the basis of [37], and define our OWMM problem as follows: In ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 4 (3 Methodology), p. 5 (3 Methodology) |
| State/latent | Thus, introduce, pose, graph, associated, RGB, images, output, pre-mapping, stage, basis, define | map/object/contact state와 base-arm coordination decision | p. 4 (3 Methodology), p. 5 (3 Methodology), p. 2 (1 Introduction) |
| Output/action | Then the linked planner takes the state of the robot xt, and point clouds converted from depth map Dc t as an additional input to calculate the low-level action at. | base motion plus arm/gripper action | p. 5 (3 Methodology), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | These planners generate waypoints that satisfy mechanical constraints for base chassis and arm joints through sampling-based methods. | long-horizon task success, reachability, collision과 recovery | p. 5 (3 Methodology), p. 16 (C Implementation Details), p. 5 (3 Methodology) |

## Main Claims and Actual Contribution

- 오래 유지되는 장면 영상과 수시로 바뀌는 로봇 상태를 분리해 저장하고, 에이전트가 생성한 과제 자료로 지시 미세조정을 수행했다. [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=5) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=7)
- 기록된 상태에서 한 단계 결정을 내리는 평가와 여러 단계를 연결하는 수행을 비교하고, 실물 이동 조작으로의 전이를 시험했다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/bc97207e3979d1cc23109db0be0e8ed2-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 15 (Figure/Table caption), p. 9 (5 Experiments) |
| Embodiment/environment | In each scene, objects were randomly placed for the robot to pick and relocate to another receptacle, resulting in 400 episodes per scene for our experiments. | hardware/simulator version and reset protocol | p. 7 (4 Dataset), p. 13 (C Implementation Details) |
| Dataset/benchmark | In our datasets, we also apply a re-labeling process for objects and receptacles, unlike HomeRobot's fixed criteria[37]. | role, split, size and leakage | p. 7 (4 Dataset), p. 13 (C Implementation Details), p. 7 (4 Dataset), p. 8 (5 Experiments) |
| Metric | Model/ Task Score Ego-centric Decisionmaking↑ Image Retrieval↑ Affordance Grounding (object)↑ Affordance Grounding (receptacle)↑ Affordance Grounding (navigation)↑ Time Consumption(s)↓ OWMM-VLM-38B(ours) 97.85% 87.54% 0.97(±0.14) 0.94(± ... | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 15 (Figure/Table caption), p. 8 (5 Experiments) |
| Baseline/ablation | OWMM-VLM-38B model achieved the best performance, and OWMM-VLM-8B model also outperformed the baseline. | fair input/data/compute/action matching | p. 9 (5 Experiments), p. 17 (C Implementation Details), p. 7 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 6 Conclusion - extractive body cue:** Episodic evaluations in simulated environments further confirmed the OWMM-Agent's superior success rates and robustness against common failure modes like dead loops, while real-world tests on ...
- **p. 9 / 6 Conclusion - extractive body cue:** Future work will focus on addressing limitations like pre-mapping reliance and enhancing cross-embodiment adaptability for more complex manipulation tasks.
- **p. 8 / 5 Experiments - extractive body cue:** For safety reasons, we cannot allow the agent to fully operate the fetch robot in the real world.
- **p. 14 / C Implementation Details - extractive body cue:** This division resulted in a total of 152k training data entries and 4k testing data entries, establishing a robust dataset for training and testing in ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Methodology), p. 6 (3 Methodology)이다.
