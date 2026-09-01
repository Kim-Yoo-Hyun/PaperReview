# VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2312.03275.
> PDF retrieval source: https://arxiv.org/pdf/2312.03275. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Vision-Language Navigation, Robotics, Navigation, semantic
- Official paper: https://arxiv.org/abs/2312.03275
- Full-text retrieval: https://arxiv.org/pdf/2312.03275
- Code/Project: https://github.com/bdaiinstitute/vlfm
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Natural language can further enhance this prior semantic knowledge, depending on the context.를 문제로 두고, In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Understanding how humans leverage semantic knowledge to navigate unfamiliar environments and decide where to explore next is pivotal for developing robots capable of human-like search ...
- **p. 1 / Abstract - extractive body cue:** We introduce a zero-shot navigation approach, Vision-Language Frontier Maps (VLFM), which is inspired by human reasoning and designed to navigate towards unseen semantic objects in ...
- **p. 1 / Abstract - extractive body cue:** VLFM builds occupancy maps from depth observations to identify frontiers, and leverages RGB observations and a pre-trained vision-language model to generate a language-grounded value map.
- **p. 1 / Abstract - extractive body cue:** VLFM then uses this map to identify the most promising frontier to explore for finding an instance of a given target object category.
- **p. 1 / Abstract - extractive body cue:** We evaluate VLFM in photo-realistic environments from the Gibson, Habitat-Matterport 3D (HM3D), and Matterport 3D (MP3D) datasets within the Habitat simulator.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Natural language can further enhance this prior semantic knowledge, depending on the context.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In contrast to prior language-based zero-shot semantic navigation methods [2]-[4], our method does not rely on object detectors and language models (e.g., ChatGPT, BERT) to ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In contrast to prior language-based zero-shot semantic navigation methods [2]-[4], our method does not rely on object detectors and language models (e.g., ChatGPT, BERT) to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also demonstrate our approach in the real world on a Boston Dynamics Spot mobile manipulation platform by navigating efficiently to unseen semantic targets across ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** How do humans navigate in novel environments?
- **p. 2 / III. PROBLEM FORMULATION - extractive body cue:** The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), and STOP.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | VLFM builds occupancy maps from depth observations to identify frontiers of the explored map region. | camera/depth stream, pose, map와 language goal | p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM FORMULATION) |
| State/latent | VLFM, builds, occupancy, maps, depth, observations, identify, frontiers, explored, region, action, space | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION) |
| Output/action | The action space consists of the following: MOVE FORWARD (0.25m), TURN LEFT (30◦), TURN RIGHT (30◦), LOOK UP (30◦), LOOK DOWN (30◦), and STOP. | collision-free trajectory 또는 velocity command | p. 2 (III. PROBLEM FORMULATION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | goal reach, safety, localization error와 replanning latency | goal reach, safety, localization error와 replanning latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In contrast to prior language-based zero-shot semantic navigation methods [2]-[4], our method does not rely on object detectors and language models (e.g., ChatGPT, BERT) to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also demonstrate our approach in the real world on a Boston Dynamics Spot mobile manipulation platform by navigating efficiently to unseen semantic targets across ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** How do humans navigate in novel environments?
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31].
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** Our method outperforms previous zero-shot methods and performs competitively against methods directly trained on the Object Navigation task.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Left: Visualization of how the confidence score of a pixel within the robot's FOV is determined based on its location relative to the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: VLFM iteratively constructs value maps for target-driven navigation by using BLIP-2 to compute the cosine similarity between a text prompt incorporating the target ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption) |
| Embodiment/environment | We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world environments; Gibson [6], HM3D [8], and MP3D [7]. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Dataset/benchmark | We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world environments; Gibson [6], HM3D [8], and MP3D [7]. | role, split, size and leakage | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Metric | For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31]. | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 3 (Figure/Table caption) |
| Baseline/ablation | We evaluate VLFM by comparing it to several state-of-the-art (SOTA) techniques for zero-shot object navigation: CLIP on Wheels (CoW) [1], ESC [2], SemUtil [3], and ZSON [32]. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VII. CONCLUSION - extractive body cue:** VLFM has a number of limitations that could be addressed by future work.
- **p. 6 / VII. CONCLUSION - extractive body cue:** So, we cannot leverage this map in sequentially executed semantic navigation tasks to different objects or in executing other navigation tasks requiring targets specified by ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Natural language can further enhance this prior semantic knowledge, depending on the context.를 문제로 두고, In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. PROBLEM FORMULATION), p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
