# JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=RnuB0Nlbd5.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248109. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, 3D Vision, Navigation, semantic
- Official paper: https://openreview.net/forum?id=RnuB0Nlbd5
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/248109
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation LLM. • We unlock the potential of spatial geometric foundation ...를 문제로 두고, In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.
- **p. 4 / 3 METHOD - extractive body cue:** To address these challenges, we introduce the VGGT as a spatial geometry encoder and propose a novel dual implicit memory paradigm for VLN research in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we introduce JanusVLN, a dual implicit memory framework for VLN that features both spatialgeometric and visual-semantic memory in Figure 1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by the human brain's hemispheric specialization for navigation, where the left hemisphere handles semantic understanding and the right manages 3D spatial cognition to form ...
- **p. 6 / 3 METHOD - extractive body cue:** Building upon the dual implicit memory paradigm, we propose JanusVLN in Figure 2, enhances the spatial understanding capabilities without requiring costly 3D data (e.g., depth).
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Compared to methods utilizing multiple input types like panoramic views and odometry, JanusVLN achieves a 10.5-35.5 improvement in SR using only a single RGB input, ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Against methods employing explicit textual cognitive maps (e.g., MapNav) or historical frames (e.g., NaVILA, StreamVLN), JanusVLN achieves improvements of 20.8, 10.8, and 3.6, respectively, while ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** When the spatial geometric encoder VGGT in JanusVLN is replaced by other visual encoders (e.g., DINOv2 (Oquab et al., 2023), and SigLIP 2 (Tschannen et ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Inspired by human cognitive science, this framework simultaneously captures visual semantics and spatial geometry to overcome the inherent limitations of existing navigation LLM. • We unlock the potential of spatial geometric foundation ...를 문제로 두고, In summary, our contributions are as follows: • We introduce a novel dual implicit memory paradigm for VLN.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 METHOD), p. 5 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
