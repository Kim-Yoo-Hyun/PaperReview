# WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.02247.
> PDF retrieval source: https://arxiv.org/pdf/2503.02247. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Vision-Language Model, Navigation, Reinforcement Learning
- Official paper: https://arxiv.org/abs/2503.02247
- Full-text retrieval: https://arxiv.org/pdf/2503.02247
- Code/Project: https://b0b8k1ng.github.io/WMNav/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge.를 문제로 두고, Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and novel modules. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Object Goal Navigation--requiring an agent to locate a specific object in an unseen environment--remains a core challenge in embodied AI.
- **p. 1 / Abstract - extractive body cue:** Although recent progress in Vision-Language Model (VLM)--based agents has demonstrated promising perception and decision-making abilities through prompting, none has yet established a fully modular world ...
- **p. 1 / Abstract - extractive body cue:** We introduce WMNav, a novel World Model-based Navigation framework powered by Vision-Language Models (VLMs).
- **p. 1 / Abstract - extractive body cue:** It predicts possible outcomes of decisions and builds memories to provide feedback to the policy module.
- **p. 1 / Abstract - extractive body cue:** To retain the predicted state of the environment, WMNav proposes the online maintained Curiosity Value Map as part of the world model memory to provide ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the true challenge lies in creating a versatile world model that can faithfully capture the landscape of an indoor environment.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the key insight that VLMs inherently encode comprehensive knowledge about indoor layout and spatial relationships of objects, we propose WMNav as shown in ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** To guide the VLM to make reasonable predictions about the indoor scene, we design a novel prompting strategy as illustrated in Figure 3 (a).
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** Then, the direction in the panoramic image with the highest score is selected and sent to the navigation policy module.
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M ...
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** Then, actions falling within explored regions are filtered out based on the exploration state map, and the action sequence is further refined by limiting the ...
- **p. 4 / III. WMNAV APPROACH - extractive body cue:** The cost is fed into PlanVLM and ReasonVLM as part of their prompts to implicitly optimize the outputs in the navigation policy.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and novel modules. ... | camera/depth stream, pose, map와 language goal | p. 2 (I. INTRODUCTION), p. 5 (III. WMNAV APPROACH) |
| State/latent | contributions, summarized, follows, introduce, direction, object, goal, navigation, complex, unknown, environment, world | robot pose, free-space/semantic map와 local goal | p. 2 (I. INTRODUCTION), p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH) |
| Output/action | Choose your action from the image prompt.' Image Prompt Exploration Stage Action VLM Update Navigable Area Candidate Actions Initial Actions Exploration State Map Filter 2 1 2 3 4 5 6 7 ... | collision-free trajectory 또는 velocity command | p. 5 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH) |
| Objective/outcome | Then M cv t (st in Figure 2) is updated by combining M nav t with the curiosity value map in the previous step M cv t-1 (st-1 in Figure 2): M ... | goal reach, safety, localization error와 replanning latency | p. 4 (III. WMNAV APPROACH), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** In our framework, the world model consists of PredictVLM and the memory constructed by curiosity value map and cost.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the key insight that VLMs inherently encode comprehensive knowledge about indoor layout and spatial relationships of objects, we propose WMNav as shown in ...
- **p. 3 / III. WMNAV APPROACH - extractive body cue:** To guide the VLM to make reasonable predictions about the indoor scene, we design a novel prompting strategy as illustrated in Figure 3 (a).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** SPL quantifies the agent's navigation efficiency by calculating the inverse ratio of the actual path length traversed to the optimal path length weighted by success ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The WMNav framework. After acquiring the RGB-D panoramic image and pose information at step t, the PredictVLM first predicts the state of the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Predict the Likelihood. (a) The world model predicts the Curiosity Value for each direction in the panoramic image based on the likelihood of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation environments with 6 goal object categories. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | Datasets and Evaluation Metrics Datasets The HM3D v0.1 [38] is used in the Habitat 2022 ObjectNav challenge, providing 2000 validation episodes on 20 validation environments with 6 goal object categories. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | Metrics We adopt Success Rate (SR) and Success Rate Weighted by Inverse Path Length (SPL) as the evaluation metrics. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Baseline/ablation | Memory SD TAP SR(%)↑SPL(%)↑ a No ✗ ✗ 65.8 25.8 b No ✓ ✗ 67.4 33.1 c Text-Image ✓ ✗ 62.0 29.6 d CVM(Ours) ✗ ✗ 69.5 34.9 e CVM(Ours) ✓ ✗ ... | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / III. WMNAV APPROACH - extractive body cue:** If there is no sofa, then return failure message.
- **p. 5 / III. WMNAV APPROACH - extractive body cue:** 2) Goal-approaching Stage: Due to the limitations of the existing VLMs' capability, we do not rely on the VLM to estimate the stopping condition directly ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** But textual information cannot accurately describe the spatial relationships in the scene, and it is difficult for LLM to make good spatial decisions.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, since VLM is trained on egocentric image data, it does not take advantage of VLM's powerful egocentric reasoning ability.

## Why Read It

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, due to the limited field of view of egocentric images, capturing environmental information outside the immediate perspective remains a significant challenge.를 문제로 두고, Our contributions can be summarized as follows: • We introduce a new direction for object goal navigation in a complex, unknown environment using a world model consisting of VLMs and novel modules. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. WMNAV APPROACH), p. 4 (III. WMNAV APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
