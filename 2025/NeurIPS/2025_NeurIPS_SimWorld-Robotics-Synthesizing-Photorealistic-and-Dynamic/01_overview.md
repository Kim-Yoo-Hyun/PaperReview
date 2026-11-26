# SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (41 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://papers.neurips.cc/paper_files/paper/2025/hash/4a81c1aad3064fb8243b8938a49ecca0-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2512.10046. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Yan Zhuang, Jiawei Ren, Xiaokang Ye, Jianzhi Shen, ruixuan zhang, Tianai Yue, Muhammad Faayez, Xuhong He, Xiyan Zhang, Ziqiao Ma, Lianhui Qin, Zhiting Hu, Tianmin Shu
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Robotics, Navigation, Benchmark
- Official paper: https://papers.neurips.cc/paper_files/paper/2025/hash/4a81c1aad3064fb8243b8938a49ecca0-Abstract-Conference.html
- Full-text retrieval: https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (41 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

SimWorld-Robotics는 보행자와 차량이 움직이는 가상 도시를 생성해 로봇의 장거리 지시 이행과 로봇 간 협력을 평가한다. [PDF 1쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advances in foundation models have shown promising results in developing generalist robotics that can perform diverse tasks in open-ended scenarios given multimodal inputs.
- **p. 1 / Abstract - extractive body cue:** However, current work has been mainly focused on indoor, household scenarios.
- **p. 1 / Abstract - extractive body cue:** In this work, we present SimWorldRobotics (SWR), a simulation platform for embodied AI in large-scale, photorealistic urban environments.
- **p. 1 / Abstract - extractive body cue:** Built on Unreal Engine 5, SWR procedurally generates unlimited photorealistic urban scenes populated with dynamic elements such as pedestrians and traffic systems, surpassing prior urban ...
- **p. 1 / Abstract - extractive body cue:** It also supports multi-robot control and communication.
- **p. 2 / 1 Introduction - extractive body cue:** However, to address the critical challenges faced by real-world robotics in urban environments, they lack the necessary realism, customizability, scalability, and versatility.
- **p. 2 / 1 Introduction - extractive body cue:** However, the simulated environments still lack photorealism as shown in Figure 2.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 3 / 1 Introduction - extractive body cue:** To address this gap, we introduce SimWorld-20K, a large-scale dataset for benchmarking multimodal robot navigation in photo-realistic urban environments.
- **p. 2 / 1 Introduction - extractive body cue:** It offers diverse high-fidelity building and object assets, supports embodied agents with rich action spaces, includes a background traffic system powered by city-scale waypoint generation, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present SimWorldRobotics (SWR), a simulation platform for embodied AI in large-scale, photorealistic urban environments.
- **p. 2 / 1 Introduction - extractive body cue:** By leveraging SWR, we develop two novel benchmarks for robots in large, urban environments.
- **p. 1 / 1 Introduction - extractive body cue:** Training these models requires a large amount of data, much of which can be generated in high-fidelity embodied simulators, such as Habitat 3 [40], RoboTHOR ...
- **p. 1 / Abstract - extractive body cue:** Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for urban ...
- **p. 3 / 1 Introduction - extractive body cue:** Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | There has been tremendous progress in engineering general-purpose robotics that can follow human instructions and perform open-ended tasks [2, 28, 15, 27, 46], thanks to the advances in robot foundation models. | camera/depth stream, pose, map와 language goal | p. 1 (1 Introduction), p. 1 (Abstract) |
| State/latent | There, been, tremendous, progress, engineering, general-purpose, robotics, follow, human, instructions, perform, open-ended | robot pose, free-space/semantic map와 local goal | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |
| Output/action | Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for urban environments. | collision-free trajectory 또는 velocity command | p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | There has been tremendous progress in engineering general-purpose robotics that can follow human instructions and perform open-ended tasks [2, 28, 15, 27, 46], thanks to the advances in robot foundation models. | goal reach, safety, localization error와 replanning latency | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- 절차적으로 도로와 도시 장면을 구성하고 동적 교통과 여러 로봇의 제어·통신을 지원하는 Unreal Engine 환경을 만들었다. [PDF 4쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=6)
- 한 로봇이 영상·언어 지시로 목적지에 도달하는 과제와 두 로봇이 통신하며 서로를 찾는 과제를 별도 벤치마크로 평가했다. [PDF 7쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Embodiment/environment | In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban environments with diverse embodied agents; (2) two ... | hardware/simulator version and reset protocol | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Dataset/benchmark | To address this gap, we introduce SimWorld-20K, a large-scale dataset for benchmarking multimodal robot navigation in photo-realistic urban environments. | role, split, size and leakage | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Metric | After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics. | definition, denominator, direction and uncertainty | p. 3 (1 Introduction), p. 34 (Figure/Table caption), p. 3 (1 Introduction) |
| Baseline/ablation | Figure 11: Example communication for ROCO baseline Baseline 2 - ROCO The ROCO-based [33] setting extends the oracle setup by introducing collaborative planning and communication between two robots. After the two agents ... | fair input/data/compute/action matching | p. 30 (Figure/Table caption), p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Explicit Limitations and Failure Boundary

- **p. 32 / Figure/Table caption - extractive body cue:** Figure 13: Qualitative result - lack of distance grounding Spatial Reasoning The VLM exhibits limitations in reasoning about spatial relationships, particularly in estimating distance, maintaining ...
- **p. 33 / Figure/Table caption - extractive body cue:** Figure 15: Qualitative result - lack of perspective-adaptive matching These limitations also manifest when matching buildings from different perspectives. The target building is provided as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Most common failure modes in SIMWORLD-MMNAV. Subtask Failure Mode Frequency (%) Moving to Intersection Misestimate the distance to the intersection 53.33 Fail to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed relatively ...
- **p. 33 / Figure/Table caption - extractive body cue:** Figure 14: Qualitative result - lack of embodied reasoning Given a working memory, an embodied agent would robustly infer that it has aligned accordingly. However, ...
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 16: Qualitative result key-step VLM outputs from the finetuned model successfully completing the task However, finetuning also exhibits certain limitations. First, when the target ...
- **p. 5 / 2 Related Work - extractive body cue:** Buildings are then placed along roads using collision-aware sampling and greedy gap-filling to maximize coverage and maintain uniformity.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction)이다.
