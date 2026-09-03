# SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2606.25497.
> PDF retrieval source: https://arxiv.org/pdf/2606.25497. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Navigation, Graph Reasoning
- Official paper: https://arxiv.org/abs/2606.25497
- Full-text retrieval: https://arxiv.org/pdf/2606.25497
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 Large Language Models (LLMs) offer this capability through the vast commonsense priors, yet they lack spatial grounding required for navigation.를 문제로 두고, In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation 를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Object-Goal Navigation (ObjNav) requires embodied agents to autonomously locate specified targets using only egocentric visual observations.
- **p. 1 / Abstract - extractive body cue:** Existing monolithic methods struggle with long-horizon reasoning and generalize poorly to novel environments.
- **p. 1 / Abstract - extractive body cue:** To address these limitations, we propose SAGE-Nav, a novel hierarchical framework that integrates the reasoning capabilities of Large Language Models (LLMs) with dynamic scene graphs.
- **p. 1 / Abstract - extractive body cue:** Crucially, it decouples asynchronous global semantic planning from the high-frequency reactive control loop.
- **p. 1 / Abstract - extractive body cue:** The LLM serves as a global planner, decomposing abstract instructions into a sequence of semantically grounded waypoints.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Large Language Models (LLMs) offer this capability through the vast commonsense priors, yet they lack spatial grounding required for navigation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This challenge has also motivated recent efforts toward unified embodied navigation paradigms [7], which emphasize the importance of data generation, simulation, evaluation, and policy learning ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our method constructs a hierarchical scene graph as an explicit environment prior.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By leveraging relational graph convolutions, it produces structure-aware embeddings designed to capture both semantic and spatial hierarchies. • We develop the Goal-aware Alignment-Fusion Network (GAFN) ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** LLM-Guided Global Planning over Hierarchical Scene Graphs Inspired by recent advances that extend RAG to embodied environments [41, 42], we develop an LLM-driven global planner ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence and generate the ...
- **p. 3 / IV. PROPOSED METHOD - extractive body cue:** 1: Pipeline Overview: (i) LLM-Guided Hierarchical Global Planner (H-GP) generates semantic waypoint sequences; (ii) Hierarchical Scene Graph Encoder (HSGE) grounds the plan in structured spatial-semantic ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** These structural priors are then adaptively fused with real-time egocentric observations via the Goal-Aware Alignment-Fusion Network (GAFN).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Finally, the unified state representation is fed into an attentive Actor-Critic [6] network featuring a two-layer LSTM [40] to maintain temporal coherence and generate the action policy πθ(at / ht, q). | camera/depth stream, pose, map와 language goal | p. 2 (IV. PROPOSED METHOD), p. 2 (I. INTRODUCTION) |
| State/latent | Finally, unified, state, representation, attentive, Actor-Critic, network, featuring, two-layer, LSTM, maintain, temporal | robot pose, free-space/semantic map와 local goal | p. 2 (IV. PROPOSED METHOD), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | It decomposes abstract instructions into semantic waypoints, effectively decoupling asynchronous global reasoning from high-frequency control. • We design the Hierarchical Scene Graph Encoder (HSGE) to translate abstract plans into acti ... | collision-free trajectory 또는 velocity command | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. PROPOSED METHOD) |
| Objective/outcome | Upon merging, the cluster's spatial and visual attributes (pk, fk) are updated via online averaging of its children. | goal reach, safety, localization error와 replanning latency | p. 2 (IV. PROPOSED METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast, our method constructs a hierarchical scene graph as an explicit environment prior.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By leveraging relational graph convolutions, it produces structure-aware embeddings designed to capture both semantic and spatial hierarchies. • We develop the Goal-aware Alignment-Fusion Network (GAFN) ...
- **p. 2 / IV. PROPOSED METHOD - extractive body cue:** LLM-Guided Global Planning over Hierarchical Scene Graphs Inspired by recent advances that extend RAG to embodied environments [41, 42], we develop an LLM-driven global planner ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by absolute ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** These results show that decoupling high-level semantic planning from local reactive control improves inference efficiency while preserving navigation performance.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 2) Evaluation Metrics: To comprehensively assess navigation performance, we adopt three standard Object-Goal Navigation metrics [2]: Success Rate (SR), Success weighted by Path Length (SPL), ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Embodiment/environment | Experimental Setup 1) Datasets: We evaluate the proposed framework across two widely used embodied simulation datasets: iTHOR [45] and RoboTHOR [46]. iTHOR comprises 120 photorealistic indoor scenes evenly distributed among four room ... | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | 4: Visualization of the agent trajectories in unfamiliar scenes in the AI2-THOR environment. | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Metric | 2) Evaluation Metrics: To comprehensively assess navigation performance, we adopt three standard Object-Goal Navigation metrics [2]: Success Rate (SR), Success weighted by Path Length (SPL), and Distance to Success (DTS). | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Baseline/ablation | In iTHOR, SAGE-Nav achieves state-of-the-art Success Rates (SR) of 82.47% overall and 77.22% in challenging long-horizon scenarios (L ≥5), outperforming TSOG and CGI-GAIL by absolute margins of 3.76 and 8.04 percentage points, ... | fair input/data/compute/action matching | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Limitations We analyze the failure cases (Fig.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** 5), which fall into four categories: (a) Target Visibility Failure, where the agent terminates despite the target (e.g., plates on high shelves) being outside the ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** This performance comprehensively validates the robustness of our hierarchical priors and dynamic scheduling mechanism.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Crucially, leveraging waypoint guidance for hardto-find targets, our method improves both the navigation success rate and overall robustness.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Replacing the LLM with heuristic rules that select waypoints based solely on graph scores highlights the critical role of commonsense priors, which rigid graph searches ...

## Why Read It

Planning and control의 navigation 문제를 이해하기 위해 읽는다. 본문은 Large Language Models (LLMs) offer this capability through the vast commonsense priors, yet they lack spatial grounding required for navigation.를 문제로 두고, In summary, the contributions of this work are threefold: • We propose SAGE-Nav, a hierarchical navigation 를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (IV. PROPOSED METHOD), p. 3 (IV. PROPOSED METHOD), p. 2 (IV. PROPOSED METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
