# Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=fm6Z3wfTae.
> PDF retrieval source: https://openreview.net/pdf/68e389cf48e82eb16b32f886139baddd9122f43d.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=fm6Z3wfTae
- Full-text retrieval: https://openreview.net/pdf/68e389cf48e82eb16b32f886139baddd9122f43d.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To bridge this semantic gap, we formulate the challenge of manipulating personal objects.를 문제로 두고, Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on ...
- **p. 1 / Abstract - extractive body cue:** We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with topdown selective attention.
- **p. 1 / Abstract - extractive body cue:** VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then ...
- **p. 1 / Abstract - extractive body cue:** We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipu1GSAI, POSTECH 2IME, POSTECH.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this semantic gap, we formulate the challenge of manipulating personal objects.
- **p. 2 / 1. Introduction - extractive body cue:** In each benchmark, one object is replaced by a user-specific instance, same-category distractors are added, and the policy must ground the correct instance from a ...

## Core Idea

- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** The category is known, but the specific instance is novel and unseen during training, and at test time the robot encounters o amidst visually similar ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We consider a pre-trained VLA policy πVLA(a / x, ℓ) mapping observation x = (I, s) and instruction ℓto action a, where I = {I(v)}V v=1 denotes multi-view RGB images from V ... | image/video, language instruction, proprioception과 history | p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction) |
| State/latent | consider, pre-trained, VLA, policy, mapping, observation, instruction, action, where, denotes, multi-view, RGB | language-grounded task state와 action-policy context | p. 4 (3.1. Problem Formulation), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation) |
| Output/action | Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ... | continuous action, pose 또는 action chunk | p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 2 (1. Introduction) |
| Objective/outcome | While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation. | instruction following, task success, generalization과 latency | p. 4 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Introduction - extractive body cue:** Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose Visual Attentive Prompting (VAP), a training-free framework that injects instance-awareness into frozen VLAs by intervening only on their inputs.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** While exact gradientbased optimization would be computationally prohibitive, we propose VAP as a zero-shot approximation.
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** The category is known, but the specific instance is novel and unseen during training, and at test time the robot encounters o amidst visually similar ...
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive body cue:** VAP improves average SR from 18.8% to 58.8%, significantly outperforming soft/hard prompts which remain in the 27.5-31.2% range.
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** VAP's modular perception pipeline achieves consistently high success rates, whereas prior methods struggle to personalize.
- **p. 8 / 5.2. Baselines - extractive body cue:** This optimized setup achieves > 95% accuracy on VQA recognition probes, and we further verify that the learned token transfers to the VLA with minimal ...
- **p. 7 / 5.1. Experimental Setup - extractive body cue:** We report Success Rate (SR), the fraction of episodes that complete the task, following standard VLA evaluations (Intelligence et al., 2025; Kim et al., 2024).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup) |
| Embodiment/environment | Spanning both selection and pick-and-place tasks, this benchmark rigorously evaluates whether VAP can reliably identify and manipulate userspecified objects on physical hardware. | hardware/simulator version and reset protocol | p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks) |
| Dataset/benchmark | We evaluate VAP on a real-world benchmark comprising four selection and four pick-and-place tasks (Figure 5). | role, split, size and leakage | p. 6 (4.2. Real-world Benchmarks), p. 6 (4.2. Real-world Benchmarks), p. 8 (5.4. Results on Real-world Benchmark), p. 7 (5.1. Experimental Setup) |
| Metric | Table 18. Controlled occlusion sweep on Personalized-SIMPLER. We vary the number of consecutive frames during which the target is fully occluded and report tracking accuracy and task success rate. The spatio-temporal tracker ... | definition, denominator, direction and uncertainty | p. 45 (Figure/Table caption), p. 7 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Baseline/ablation | VAP outperforms other baselines across all scenarios. | fair input/data/compute/action matching | p. 7 (5.1. Experimental Setup), p. 8 (5.3. Results on Simulation Benchmarks), p. 8 (5.2. Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 42 / Figure/Table caption - extractive body cue:** Figure 23. Case 3 (correct prompt): correct instance highlighted but manipulation fails. The mask prompt consistently highlights the intended personal object in all relevant views, ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 9. Soft Prompt: relatively consistent localization yet failed execution. Across the rollout, the token-patch similarity heatmaps remain largely concentrated near the intended personal object, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Manipulating personal objects with VLA. Existing vision-language-action (VLA) models cannot handle per- sonal objects such as <my cup>, because they can only interpret ...
- **p. 9 / 5.5. Error Case Analysis - extractive body cue:** First, the sequential factorization of grounding and manipulation does not itself bound performance: reliable spatio-temporal tracking maintains target identity through several seconds of complete invisibility, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. VAP builds a visual memory from a few reference images, grounds the target with frozen detection and segmentation, and prompts a frozen VLA ...
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive body cue:** Failure analysis across benchmarks.
- **p. 8 / 5.4. Results on Real-world Benchmark - extractive body cue:** We report the overall failure rate for each setting.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 To bridge this semantic gap, we formulate the challenge of manipulating personal objects.를 문제로 두고, Our main contributions are as follows: • Personal Object Manipulation: We introduce a personalization task for VLAs where the policy must manipulate user-specific objects among visually similar distractors using only a few ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (3.1. Problem Formulation), p. 1 (1. Introduction), p. 4 (3.1. Problem Formulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
