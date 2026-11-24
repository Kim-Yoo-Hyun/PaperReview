# JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/3812c3c803e986eca64000fe92467991-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248109. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Shuang Zeng, Dekang Qi, Xinyuan Chang, Feng Xiong, Shichao Xie, Xiaolong Wu, Shiyi Liang, Mu Xu, Xing Wei
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, 3D Vision, Navigation, semantic
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/3812c3c803e986eca64000fe92467991-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

JanusVLN은 영상열을 따라 이동할 때 의미 정보와 3차원 기하 정보를 별개의 고정 크기 기억에 보관해 다음 내비게이션 행동을 정한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-and-Language Navigation (VLN) requires an embodied agent to navigate through unseen environments, guided by natural language instructions and a continuous video stream.
- **p. 1 / ABSTRACT - extractive body cue:** Recent advances in VLN have been driven by the powerful semantic understanding of Multimodal Large Language Models (MLLMs).
- **p. 1 / ABSTRACT - extractive body cue:** However, these methods typically rely on explicit semantic memory, such as building textual cognitive maps or storing historical visual frames.
- **p. 1 / ABSTRACT - extractive body cue:** This type of method suffers from spatial information loss, computational redundancy, and memory bloat, which impede efficient navigation.
- **p. 1 / ABSTRACT - extractive body cue:** Inspired by the implicit scene representation in human navigation, analogous to the left brain's semantic understanding and the right brain's spatial cognition, we propose JanusVLN, ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation LLM. • We ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This makes it exceedingly difficult for the model to extract critical information from a vast, cluttered, and fragmented memory, thereby leading to severe inefficiency.

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.
- **p. 4 / 3 METHOD - extractive body cue:** To address these challenges, we introduce the VGGT as a spatial geometry encoder and propose a novel dual implicit memory paradigm for VLN research in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce JanusVLN, a dual implicit memory framework for VLN that features both spatialgeometric and visual-semantic memory in Figure 1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by the human brain's hemispheric specialization for navigation, where the left hemisphere handles semantic understanding and the right manages 3D spatial cognition to form ...
- **p. 6 / 3 METHOD - extractive body cue:** Building upon the dual implicit memory paradigm, we propose JanusVLN in Figure 2, enhances the spatial understanding capabilities without requiring costly 3D data (e.g., depth).
- **p. 4 / 3 METHOD - extractive body cue:** VGGT (Wang et al., 2025a), which is based on a transformer feed-forward architecture, comprises three key components: an encoder for extracting single-image feature, a fusion ...
- **p. 5 / 3 METHOD - extractive body cue:** These KV, derived from the output of attention modules such as transformers, constitute high-level semantic abstractions and structured representations of the past environment.
- **p. 4 / 3 METHOD - extractive body cue:** As our focus is on feature extraction, which embeds 3D geometry prior information, rather than directly outputting 3D attributes, we leverage the encoder and the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Vision-and-Language Navigation (VLN) is a foundational task in embodied AI, requiring an agent to navigate through unseen environments guided by visual inputs and natural language instructions. | camera/depth stream, pose, map와 language goal | p. 1 (1 INTRODUCTION), p. 4 (3 METHOD) |
| State/latent | Vision-and-Language, Navigation, VLN, foundational, task, embodied, requiring, agent, navigate, through, unseen, environments | robot pose, free-space/semantic map와 local goal | p. 1 (1 INTRODUCTION), p. 4 (3 METHOD), p. 4 (3 METHOD) |
| Output/action | Upon executing the action at`1, the agent receives a new observation xt`1. | collision-free trajectory 또는 velocity command | p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD) |
| Objective/outcome | 3.2 DUAL IMPLICIT MEMORY The limitations of traditional explicit semantic memory, including memory inflation, computational redundancy, and the loss of spatial information, coupled with the original VGGT's requirement to reprocess the e ... | goal reach, safety, localization error와 replanning latency | p. 4 (3 METHOD), p. 5 (3 METHOD), p. 6 (3 METHOD) |

## Main Claims and Actual Contribution

- 시각·의미 인코더와 공간·기하 인코더 각각에서 초기 토큰과 최근 창의 키·값을 유지해 RGB 관측이 들어올 때마다 기억을 갱신한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=6)
- 연속 환경의 지시 기반 내비게이션에서 성공률을 비교하고, 두 기억의 역할 및 경로가 길어질 때의 추론 비용을 분석했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/3812c3c803e986eca64000fe92467991-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Embodiment/environment | These datasets comprise trajectories collected from Matterport3D (Chang et al., 2017) scenes using the Habitat simulator (Savva et al., 2019). | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | In real-world experiments, we use the Unitree Go2 as the robotic platform, equipped with an Insta360 X5 camera to capture front RGB. | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Metric | Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on the unseen splits using standard VLN metrics, including ... | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Baseline/ablation | Consistent with prior work (Cheng et al., 2025; Dai et al., 2025; Yin et al., 2025; Lu et al., 2024), we report performance on the unseen splits using standard VLN metrics, including ... | fair input/data/compute/action matching | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 21 / Figure/Table caption - extractive body cue:** Figure 9: Visualization and presentation of the types of failure cases. on relatively simple instructions (1-150 words). However, their performance declines on moderately complex instructions ...
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 8: Performance on various instruction lengths/complexity. larger-scale external datasets, akin to the approaches of StreamVLN and NaVILA, is reserved for future work to construct ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Finally, when we omit the preservation of the initial window's KV, a slight performance degradation is observed, indicating that the first few frames of memory ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 METHOD), p. 5 (3 METHOD)이다.
