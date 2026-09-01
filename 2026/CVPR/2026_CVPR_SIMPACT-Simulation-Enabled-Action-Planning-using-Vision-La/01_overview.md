# SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLM, Planning, simulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 We also show that SIMPACT demonstrates robustness under randomized scene variations, and provide representative failure cases.를 문제로 두고, For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Front matter - extractive body cue:** SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models Supplementary Material This supplementary material provides additional implementation details, experiment analyses, and qualitative results supporting our main paper.
- **p. 1 / Front matter - extractive body cue:** We describe the full simulation-construction pipeline, including VLMbased prediction of rigid and deformable object parameters, as well as the symbolic action space and prompting strategy ...
- **p. 1 / Front matter - extractive body cue:** Additionally, we present more qualitative examples, an ablation on the number of VLM-sampled action proposals, and a study comparing a CEM-based Prompting-with-theFuture-style variant [45], which ...
- **p. 1 / Front matter - extractive body cue:** We also show that SIMPACT demonstrates robustness under randomized scene variations, and provide representative failure cases.
- **p. 1 / Front matter - extractive body cue:** Importantly, we perform an additional experiment that analyzes the consistency between simulation and real-world performance, showing strong alignment (89% agreement) while noting remaining sim-real gaps.
- **p. 2 / Front matter - extractive body cue:** Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts the ...
- **p. 3 / Front matter - extractive body cue:** 5, this figure shows the initial state, execution progress, and final state for the sweeping tasks. better understand the sim-to-real gap.

## Core Idea

- **p. 1 / Front matter - extractive body cue:** For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.
- **p. 1 / Front matter - extractive body cue:** Additionally, we present more qualitative examples, an ablation on the number of VLM-sampled action proposals, and a study comparing a CEM-based Prompting-with-theFuture-style variant [45], which ...
- **p. 2 / Front matter - extractive body cue:** Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and switch ...
- **p. 3 / Front matter - extractive body cue:** Computation Time Table 5 reports the runtime of each component in our method.
- **p. 4 / Front matter - extractive body cue:** These results demonstrate that our method naturally generalizes to a wide range of scene variations, owing to the
- **p. 1 / Front matter - extractive body cue:** Optimization Context c Generation To instantiate the OPTIMIZE function, we construct the context ci from the action sequence ai and the simulated state rollout si.
- **p. 3 / Front matter - extractive body cue:** These tasks appear more sensitive to accurate physical modeling and contact dynamics.
- **p. 3 / Front matter - extractive body cue:** Only the first entry is shown for repeated fields, with omitted entries summarized using comments. quences for task success, we also include 10 unoptimized VLM ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input Specification • Task Instruction: Main task goal. • Real-World Context: Workspace limits, safe ranges • Simulation Rollouts: Specify the format of input context describing action and state. | image/video, language instruction, proprioception과 history | p. 4 (Front matter), p. 2 (Front matter) |
| State/latent | Input, Specification, Task, Instruction, Main, goal, Real-World, Context, Workspace, limits, safe, ranges | language-grounded task state와 action-policy context | p. 4 (Front matter), p. 2 (Front matter), p. 2 (Front matter) |
| Output/action | Input Specification • Image of the Scene: Visual observation of the workspace. • Additional Scene Context: Object and end-effector coordinates in the world frame, workspace constraints. • Natural Language Instruction: High-level task ... | continuous action, pose 또는 action chunk | p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter) |
| Objective/outcome | Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task. | instruction following, task success, generalization과 latency | p. 4 (Front matter), p. 2 (Front matter), p. 2 (Front matter) |

## Main Claims and Actual Contribution

- **p. 1 / Front matter - extractive body cue:** For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.
- **p. 1 / Front matter - extractive body cue:** Additionally, we present more qualitative examples, an ablation on the number of VLM-sampled action proposals, and a study comparing a CEM-based Prompting-with-theFuture-style variant [45], which ...
- **p. 2 / Front matter - extractive body cue:** Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and switch ...
- **p. 3 / Front matter - extractive body cue:** Computation Time Table 5 reports the runtime of each component in our method.
- **p. 4 / Front matter - extractive body cue:** These results demonstrate that our method naturally generalizes to a wide range of scene variations, owing to the
- **p. 2 / Front matter - extractive body cue:** We evaluate this variant and find that it consistently achieves a zero success rate across all of our real-world tasks.
- **p. 5 / Front matter - extractive body cue:** Our framework can also incorporate real-world feedback to improve the success rate after execution failures.
- **p. 5 / Front matter - extractive body cue:** Increasing the number of sampled proposals may improve performance in such cases.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 2 (Front matter), p. 5 (Front matter) |
| Embodiment/environment | Your objective is to analyze simulation rollouts and propose one optimized action plan for a real-world task. | hardware/simulator version and reset protocol | p. 4 (Front matter), p. 3 (Front matter) |
| Dataset/benchmark | Input Specification • Task Instruction: Main task goal. • Real-World Context: Workspace limits, safe ranges • Simulation Rollouts: Specify the format of input context describing action and state. | role, split, size and leakage | p. 4 (Front matter), p. 3 (Front matter), p. 4 (Front matter), p. 5 (Front matter) |
| Metric | Avoid aggressive or risky proposals and focus on plans with high success rates. | definition, denominator, direction and uncertainty | p. 2 (Front matter), p. 2 (Front matter), p. 5 (Front matter) |
| Baseline/ablation | Our zero-shot method outperforms imitation learning baseline HULC [40] and VLA baseline Figure 14. | fair input/data/compute/action matching | p. 5 (Front matter), p. 5 (Front matter), p. 2 (Front matter) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Front matter - extractive body cue:** Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts the ...
- **p. 3 / Front matter - extractive body cue:** Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure.
- **p. 3 / Front matter - extractive body cue:** Simulated failures enable the VLM to avoid similar real-world failures, while simulated successes offer informative guidance for selecting effective action sequences.
- **p. 4 / Front matter - extractive body cue:** 2) Infer Logic & Physics: Identify the causes of failures and the characteristics of successful attempts.
- **p. 4 / Front matter - extractive body cue:** Simulation and real outcomes match in 89% of cases (both success or both failure), with 11% showing sim-success/real-fail.
- **p. 5 / Front matter - extractive body cue:** The pivoting and shape rope failures are both planning failures.
- **p. 5 / Front matter - extractive body cue:** The bowl stacking and shape dough failures are both execution failures.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 We also show that SIMPACT demonstrates robustness under randomized scene variations, and provide representative failure cases.를 문제로 두고, For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 4 (Front matter), p. 1 (Front matter) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
