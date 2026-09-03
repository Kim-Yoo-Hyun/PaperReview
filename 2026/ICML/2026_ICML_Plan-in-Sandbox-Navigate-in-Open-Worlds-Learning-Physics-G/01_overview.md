# Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=W5e8c9nwNo.
> PDF retrieval source: https://openreview.net/pdf/27299763732e881621b2b6f37e47e47722f2e575.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: Navigation, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=W5e8c9nwNo
- Full-text retrieval: https://openreview.net/pdf/27299763732e881621b2b6f37e47e47722f2e575.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (28 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 navigation 문제를 이해하기 위해 읽는다. 본문은 In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. • ...를 문제로 두고, In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** However, their performance in embodied navigation remains hindered by a scarcity of aligned open-world vision and robot control data.
- **p. 1 / Abstract - extractive body cue:** Despite simulators providing a cost-effective alternative for data collection, the inherent reliance on photorealistic simulations often limits the transferability of learned policies.
- **p. 1 / Abstract - extractive body cue:** To this end, we propose Sandbox-Abstracted Grounded Experience (SAGE), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic ...
- **p. 1 / Abstract - extractive body cue:** SAGE system operates via three synergistic phases: (1) Genesis: constructing diverse, physics-constrained semantic environments to bootstrap experience; (2) Evolution: distilling experiences through Reinforcement Learning (RL), ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, fully unleashing the potential of VLMs within embodied environments remains fraught with challenges.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead of relying on difficult exploration in the real world, we propose operating the VLM within a physics-grounded sandbox to synthesize diverse tasks and proactively ...
- **p. 3 / 2.3. Navigation Task - extractive body cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.
- **p. 1 / 1. Introduction - extractive body cue:** Motivated by these strides, the research community has increasingly focused on developing general-purpose embodied navigation agents.
- **p. 3 / 2.3. Navigation Task - extractive body cue:** Intuitively, the core objective is to optimize the policy against the synthesized experiences: Jϕ(θ) = E o∼O, at∼πθ(·/st,o), st+1∼P(·/st,at) "X t=0 γtrϕ(st, at, o) # ...
- **p. 3 / 2.1. Physics-Grounded Interaction Sandbox - extractive body cue:** P(s′/s, a) denotes the state transition dynamics.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A represents the agent's action space, which we decompose into the selection of discrete intermediate observations and their corresponding navigable waypoints. | camera/depth stream, pose, map와 language goal | p. 3 (2.1. Physics-Grounded Interaction Sandbox), p. 3 (2.3. Navigation Task) |
| State/latent | represents, agent, action, space, decompose, selection, discrete, intermediate, observations, corresponding, navigable, waypoints | robot pose, free-space/semantic map와 local goal | p. 3 (2.1. Physics-Grounded Interaction Sandbox), p. 3 (2.3. Navigation Task), p. 2 (1. Introduction) |
| Output/action | For any specific task n ∼N, the agent aims to reach the target state via a policy πθ(a/s, n), which maximizes the expected cumulative reward over the target distribution: JN (θ) = ... | collision-free trajectory 또는 velocity command | p. 3 (2.3. Navigation Task), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | 3 within the abstracted sandbox, the agent progressively acquires robust priors, ultimately allowing transfer to minimize the realworld objective JN (θ). | goal reach, safety, localization error와 replanning latency | p. 3 (2.3. Navigation Task), p. 3 (2.3. Navigation Task) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead of relying on difficult exploration in the real world, we propose operating the VLM within a physics-grounded sandbox to synthesize diverse tasks and proactively ...
- **p. 3 / 2.3. Navigation Task - extractive body cue:** To address this, we propose approximating the optimal behavior by maximizing a surrogate objective Jϕ(θ) within the sandbox task distribution O.
- **p. 1 / 1. Introduction - extractive body cue:** Motivated by these strides, the research community has increasingly focused on developing general-purpose embodied navigation agents.
- **p. 3 / 2.3. Navigation Task - extractive body cue:** Intuitively, the core objective is to optimize the policy against the synthesized experiences: Jϕ(θ) = E o∼O, at∼πθ(·/st,o), st+1∼P(·/st,at) "X t=0 γtrϕ(st, at, o) # ...
- **p. 6 / 4.2. Main Navigation Results - extractive body cue:** SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin.
- **p. 8 / 4.5. Analysis and Ablation - extractive body cue:** As shown in Table 3, the full SAGE framework achieves substantial improvements of 9.70%/6.03% on A-EQA and 7.52%/8.09% on GOATBench compared to the baselines (Qwen3-VL-2B/4B).
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and LLM-Match Success weighted by Path Length (SPL†), ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation) |
| Embodiment/environment | GOAT-Bench: This benchmark challenges robots to sequentially execute 5 to 10 subtasks within unseen real-world scenes. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Dataset/benchmark | This confirms that our approach effectively mitigates the dependency on massive datasets, paving a scalable avenue for enhancing navigation policies by integrating abundant, low-cost sandbox tasks. | role, split, size and leakage | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data), p. 7 (4.3. Analysis on Sandbox Data) |
| Metric | Adhering to the OpenEQA (Majumdar et al., 2024) standards, we quantify performance using LLM-Match Success Rate (SR†) and LLM-Match Success weighted by Path Length (SPL†), utilizing Qwen3-235B-A22B (Yang et al., 2025a) as ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.3. Analysis on Sandbox Data) |
| Baseline/ablation | SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin. | fair input/data/compute/action matching | p. 6 (4.2. Main Navigation Results), p. 6 (4.2. Main Navigation Results), p. 8 (4.5. Analysis and Ablation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Experimental Settings - extractive body cue:** (15) In cases of navigation failure, the agent defaults to blind guessing; the contribution to SPL† is set to 0.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 7. Visualization of the word cloud. rules using regular expressions. The entire trajectory is discarded if the generated output fails to match the required ...
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** Furthermore, we demonstrate the system's practical robustness via Real-World Deployment in Appendix J.
- **p. 7 / 4.3. Analysis on Sandbox Data - extractive body cue:** All experiments use the model with 2B parameters on A-EQA. ing complementary environments during the Genesis phase, the agent learns more robust navigation priors that ...
- **p. 8 / 4.4. Analysis on Evolution - extractive body cue:** Conservative clipping (ϵexp = 0.4) causes underfitting, failing to exploit Genesis signals.
- **p. 8 / 4.4. Analysis on Evolution - extractive body cue:** Conversely, aggressive updates (ϵexp = 1.2) lead to instability and performance degradation after 100 steps.

## Why Read It

RL, IL, offline learning, and robot data의 navigation 문제를 이해하기 위해 읽는다. 본문은 In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. • ...를 문제로 두고, In summary, the key contributions of our work are: • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (2. Problem Formulation), p. 3 (2.3. Navigation Task) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
