# RoboDreamer: Learning Compositional World Models for Robot Imagination

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v235/zhou24f.html.
> PDF retrieval source: https://arxiv.org/pdf/2404.12377. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, video prediction, language planning, compositional generalization
- Official paper: https://proceedings.mlr.press/v235/zhou24f.html
- Full-text retrieval: https://arxiv.org/pdf/2404.12377
- Code/Project: https://robodreamer.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 This is crucially important in robotics, where there is a lack of systematic data covering all possible actions in an environment and a need to be able to generalize to new unseen ...를 문제로 두고, Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of natural language. • We illustrate how RoboDream ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Text-to-video models have demonstrated substantial potential in robotic decision-making, enabling the imagination of realistic plans of future actions as well as accurate environment simulation.
- **p. 1 / Abstract - extractive body cue:** However, one major issue in such models is generalization - models are limited to synthesizing videos subject to language instructions similar to those seen at ...
- **p. 1 / Abstract - extractive body cue:** This is heavily limiting in decision-making, where we seek a powerful world model to synthesize plans of unseen combinations of objects and actions in order ...
- **p. 1 / Abstract - extractive body cue:** To resolve this issue, we introduce RoboDreamer, an innovative approach for learning a compositional world model by factorizing the video generation.
- **p. 1 / Abstract - extractive body cue:** We leverage the natural compositionality of language to parse instructions into a set of lowerlevel primitives, which we condition a set of models on to ...
- **p. 2 / 1. Introduction - extractive body cue:** This is crucially important in robotics, where there is a lack of systematic data covering all possible actions in an environment and a need to ...
- **p. 2 / 1. Introduction - extractive body cue:** Prior approaches, such as ControlNet (Zhang et al., 2023) introduce an additional encoder upon pre-trained text-to-image models to tackle this challenge, but this requires the ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables our approach to generalize to both new combinations of language and multimodal input. process by leveraging the inherent compositionality of natural language.
- **p. 1 / 1. Introduction - extractive body cue:** In response, we introduce RoboDreamer, a compositional world model capable of factorizing the video generation 1 arXiv:2404.12377v1 [cs.RO] 18 Apr 2024
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** This enables us to convert planning directly into a text-to-video generation problem.
- **p. 1 / 1. Introduction - extractive body cue:** Such models have recently been applied in robotics, demonstrating significant potential in the development of policies, dynamic models, and planners (Du et al., 2023b; Ajay ...
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** Given a UPDP G, we then use a trajectory-task conditioned policy π(·/{xh}H h=0, c) : X H+1×C →∆(AH) to infer executable actions from synthesized videos.
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** To implement this generation problem, we use the video diffusion model and use the base source code from (Ko et al., 2023).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy takes as input two adjacent image observations xt and xt+1 in the synthesized video τ and outputs an action a to execute. | observation, uncertainty/risk estimate와 task command | p. 3 (2.2. Executing Videos Plans), p. 3 (2.1. Planning with Text-Conditioned Video Generation) |
| State/latent | policy, takes, input, adjacent, image, observations, synthesized, video, outputs, action, execute, RoboDreamer | safe set, recovery state 또는 constraint margin | p. 3 (2.2. Executing Videos Plans), p. 3 (2.1. Planning with Text-Conditioned Video Generation), p. 2 (1. Introduction) |
| Output/action | RoboDreamer: Learning Compositional World Models for Robot Imagination pick orange from bottom drawer and place on counter Language Instruction Parsing pick orange VP / action place on counter VP / action from ... | shielded, recovery 또는 safe action | p. 3 (2.1. Planning with Text-Conditioned Video Generation), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | task return과 violation/failure probability | task return과 violation/failure probability | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of ...
- **p. 2 / 1. Introduction - extractive body cue:** This enables our approach to generalize to both new combinations of language and multimodal input. process by leveraging the inherent compositionality of natural language.
- **p. 1 / 1. Introduction - extractive body cue:** In response, we introduce RoboDreamer, a compositional world model capable of factorizing the video generation 1 arXiv:2404.12377v1 [cs.RO] 18 Apr 2024
- **p. 3 / 2.1. Planning with Text-Conditioned Video Generation - extractive body cue:** This enables us to convert planning directly into a text-to-video generation problem.
- **p. 1 / 1. Introduction - extractive body cue:** Such models have recently been applied in robotics, demonstrating significant potential in the development of policies, dynamic models, and planners (Du et al., 2023b; Ajay ...
- **p. 7 / 4.2. Evaluation on Robotic Planning - extractive body cue:** According to the results presented in Table 3, RoboDreamer achieves superior task success rates compared to baseline models even if RoboDreamer is only given observation ...
- **p. 8 / 4.2. Evaluation on Robotic Planning - extractive body cue:** On the other hand, RoboDreamer achieves a success rate of 15% with the help of predicted future observations.
- **p. 7 / 4.1. Evaluation on Video Generation - extractive body cue:** RoboDreamer (t+s) and RoboDreamer (t+i) achieve strong performance on human evaluation and good video quality.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Evaluation on Robotic Planning), p. 8 (4.2. Evaluation on Robotic Planning) |
| Embodiment/environment | We take the real-world robotics dataset RT-1 (Brohan et al., 2022) to evaluate video generation. | hardware/simulator version and reset protocol | p. 6 (4.1. Evaluation on Video Generation), p. 6 (4.1. Evaluation on Video Generation) |
| Dataset/benchmark | (Section 4.1) • RQ3: Can RoboDreamer be deployed on robot manipulation tasks? | role, split, size and leakage | p. 6 (4.1. Evaluation on Video Generation), p. 6 (4.1. Evaluation on Video Generation), p. 5 (4. Experiments), p. 7 (4.2. Evaluation on Robotic Planning) |
| Metric | According to the results presented in Table 3, RoboDreamer achieves superior task success rates compared to baseline models even if RoboDreamer is only given observation from single cameras. | definition, denominator, direction and uncertainty | p. 7 (4.2. Evaluation on Robotic Planning), p. 8 (4.2. Evaluation on Robotic Planning), p. 8 (4.2. Evaluation on Robotic Planning) |
| Baseline/ablation | According to the results presented in Table 3, RoboDreamer achieves superior task success rates compared to baseline models even if RoboDreamer is only given observation from single cameras. | fair input/data/compute/action matching | p. 7 (4.2. Evaluation on Robotic Planning), p. 5 (Figure/Table caption), p. 6 (4.1. Evaluation on Video Generation) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Limitations Although RoboDreamer exhibits strong performance in robot planning tasks, it has several limitations.
- **p. 6 / 4.1. Evaluation on Video Generation - extractive body cue:** The scores are 0, 1, where 0 means the robotic planning in the generated videos is unreasonable or fails to solve tasks and 1 means ...
- **p. 8 / 4.2. Evaluation on Robotic Planning - extractive body cue:** UniPi performs poorly as it does not align with task instructions well.
- **p. 7 / 4.1. Evaluation on Video Generation - extractive body cue:** As is illustrated in Figure 4, the baseline method AVDC and HiP fail to accurately infer the spatial relationship between objects, incorrectly placing them in ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 This is crucially important in robotics, where there is a lack of systematic data covering all possible actions in an environment and a need to be able to generalize to new unseen ...를 문제로 두고, Our contributions are three-fold. • We introduce RoboDreamer, a compositional world model capable of factorizing the video generation process by leveraging the inherent compositionality of natural language. • We illustrate how RoboDream ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (2.1. Planning with Text-Conditioned Video Generation), p. 3 (2.1. Planning with Text-Conditioned Video Generation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
