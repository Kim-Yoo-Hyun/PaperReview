# CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.03227.
> PDF retrieval source: https://arxiv.org/pdf/2112.03227. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Vision-Language-Action, Benchmark, Robotics
- Official paper: https://arxiv.org/abs/2112.03227
- Full-text retrieval: https://arxiv.org/pdf/2112.03227
- Code/Project: https://calvin.cs.uni-freiburg.de/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.를 문제로 두고, In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** General-purpose robots coexisting with humans in their environment must learn to relate human language to their perceptions and actions to be useful in a range ...
- **p. 1 / Abstract - extractive body cue:** Moreover, they need to acquire a diverse repertoire of general-purpose skills that allow composing long-horizon tasks by following unconstrained language instructions.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.
- **p. 1 / Abstract - extractive body cue:** Our aim is to make it possible to develop agents that can solve many robotic manipulation tasks over a long horizon, from onboard sensors, and ...
- **p. 1 / Abstract - extractive body cue:** CALVIN tasks are more complex in terms of sequence length, action space, and language than existing vision-and-language task datasets and supports flexible specification of sensor ...
- **p. 2 / 1. CALVIN includes ∼24 hours teleoperated unstructured play - extractive body cue:** Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.
- **p. 1 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** This stands in contrast to current robots, which typically lack this generalization ability and learn individual tasks one at a time.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.
- **p. 2 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** To address this problem we present CALVIN, a new opensource simulated benchmark that links human language to robot motor skills, behaviors, and objects in interactive ...
- **p. 3 / III. CALVIN - extractive body cue:** The CALVIN benchmark consists of three key components, which are:
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** This style of data is very different from commonly used task-specific data, which only consists of expert trajectories.
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** Thus, to accelerate progress in language-driven robotics, we present a set of evaluation protocols of varying difficulty by choosing different combinations of sensor suites and ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get ...
- **p. 6 / IV. BASELINE MODELS - extractive body cue:** The encoder for the gripper camera takes an image of 84 × 84 as input and consists of 3 convolutional layers with 32, 64, and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The decoder is a policy trained to reconstruct input actions, conditioned on state xt, goal xg, and an inferred plan z for how to get from xt to xg. | standardized observation, action, task state와 evaluation split | p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN) |
| State/latent | decoder, policy, trained, reconstruct, input, actions, conditioned, state, goal, inferred, plan, Observation | benchmark state/goal와 method decision | p. 6 (IV. BASELINE MODELS), p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge) |
| Output/action | 2: Observation and action spaces supported by CALVIN. only allow feasible sequences that can be achieved from a predefined initial environment state. | policy/controller trajectory 또는 measured result | p. 3 (III. CALVIN), p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS) |
| Objective/outcome | These short horizon goal image conditioned demonstrations can be fed to a simple maximum likelihood goal conditioned imitation objective: LLfP = E(τ,xg)∼Dplay   /τ/ X t=0 log πθ(at / xt, xg) ... | success metric, robustness, generalization과 reproducibility | p. 6 (IV. BASELINE MODELS), p. 6 (IV. BASELINE MODELS) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.
- **p. 2 / A LONG-STANDING goal for robotics and embodied - extractive body cue:** To address this problem we present CALVIN, a new opensource simulated benchmark that links human language to robot motor skills, behaviors, and objects in interactive ...
- **p. 3 / III. CALVIN - extractive body cue:** The CALVIN benchmark consists of three key components, which are:
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** This style of data is very different from commonly used task-specific data, which only consists of expert trajectories.
- **p. 4 / 3) CALVIN Challenge - extractive body cue:** Thus, to accelerate progress in language-driven robotics, we present a set of evaluation protocols of varying difficulty by choosing different combinations of sensor suites and ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and ...
- **p. 7 / V. EXPERIMENTAL RESULTS - extractive body cue:** The best MCIL model achieves a success rate of 0.08% when following chains of five language instructions in a row when training and testing on ...
- **p. 6 / V. EXPERIMENTAL RESULTS - extractive body cue:** The success rate stays comparable when including a gripper camera, depth channels or tactile sensing.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Embodiment/environment | MEES et al.: CALVIN: A BENCHMARK FOR LANGUAGE-CONDITIONED POLICY LEARNING FOR LONG-HORIZON ROBOT MANIPULATION TASKS 7 Input Train →Test MTLC LH-MTLC Static Camera Gripper Camera Tactile (34 tasks) No. | hardware/simulator version and reset protocol | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Dataset/benchmark | We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks on the ... | role, split, size and leakage | p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS) |
| Metric | The success rate stays comparable when including a gripper camera, depth channels or tactile sensing. | definition, denominator, direction and uncertainty | p. 6 (V. EXPERIMENTAL RESULTS), p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |
| Baseline/ablation | We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks on the ... | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS), p. 7 (V. EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. CONCLUSION - extractive body cue:** In this paper, we presented CALVIN, the first public benchmark of instruction following that combines natural language conditioning, multimodal high-dimensional inputs, 7-DOF continuous control, and ...
- **p. 7 / VI. CONCLUSION - extractive body cue:** As the field of language-driven robotics evolves, a need arises to standardize research for better benchmarks and more reproducible results.
- **p. 7 / VI. CONCLUSION - extractive body cue:** CALVIN has the goal of providing researchers with a modular framework that has been developed from the ground up to support training, prototyping, and validation ...

## Why Read It

VLA and generalist robot policies의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Models that can overcome these challenges will begin to close the gap towards scalable, general-purpose, language-driven robotics.를 문제로 두고, In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 1 (A LONG-STANDING goal for robotics and embodied), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. CALVIN includes ∼24 hours teleoperated unstructured play), p. 3 (3) CALVIN Challenge), p. 6 (IV. BASELINE MODELS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The long horizon of CALVIN tasks poses a significant challenge with sub-problems including the acquisition of a diverse repertoire of general-purpose skills, object detection, referring expression and action grounding, and ... (p. 7, VI. CONCLUSION).
- **Actual contribution:** In this paper, we present CALVIN (Composing Actions from Language and Vision), an open-source simulated benchmark to learn longhorizon language-conditioned tasks. (p. 1, Abstract).
- **Evaluation boundary:** We observe that the baseline with images of the static camera achieves a success rate of 53.9% for the MTLC evaluation setting, when training and testing the 34 manipulation tasks ... (p. 6, V. EXPERIMENTAL RESULTS).
- **Explicit failure boundary:** For the Long-Horizon MTLC evaluation we observe that the agents perform poorly on CALVIN's long-horizon tasks with high-dimensional state spaces. (p. 7, V. EXPERIMENTAL RESULTS).
