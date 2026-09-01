# Problem - SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 4 (Front matter)): We also show that SIMPACT demonstrates robustness under randomized scene variations, and provide representative failure cases.

## PDF Body Digest

- **p. 1 / Front matter - extractive body cue:** SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models Supplementary Material This supplementary material provides additional implementation details, experiment analyses, and qualitative results supporting our main paper.
- **p. 1 / Front matter - extractive body cue:** We describe the full simulation-construction pipeline, including VLMbased prediction of rigid and deformable object parameters, as well as the symbolic action space and prompting strategy ...
- **p. 1 / Front matter - extractive body cue:** Additionally, we present more qualitative examples, an ablation on the number of VLM-sampled action proposals, and a study comparing a CEM-based Prompting-with-theFuture-style variant [45], which ...
- **p. 1 / Front matter - extractive body cue:** We also show that SIMPACT demonstrates robustness under randomized scene variations, and provide representative failure cases.
- **p. 1 / Front matter - extractive body cue:** Importantly, we perform an additional experiment that analyzes the consistency between simulation and real-world performance, showing strong alignment (89% agreement) while noting remaining sim-real gaps.
- **p. 2 / Front matter - extractive body cue:** Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts the ...
- **p. 3 / Front matter - extractive body cue:** 5, this figure shows the initial state, execution progress, and final state for the sweeping tasks. better understand the sim-to-real gap.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We also show that SIMPACT demonstrates robustness under randomized scene variations, and provide representative failure cases. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Input Specification • Task Instruction: Main task goal. • Real-World Context: Workspace limits, safe ranges • Simulation Rollouts: Specify the format of ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | Input, Specification, Task, Instruction, Main, goal, Real-World, Context, Workspace, limits | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | prompt, includes, task, specifications, input, requirements, action, primitive | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: Input, Specification, Task, Instruction, Main, goal, Real-World, Context, Workspace, limits | p. 4 (Front matter), p. 2 (Front matter), p. 2 (Front matter) |
| Decision / output variable | action, pose, option or chunk a; body terms: rigid, objects, numerical, state, consists, full, DoF, transformation | p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Your, objective, analyze, simulation, rollouts, optimized, action, plan | p. 2 (Front matter), p. 2 (Front matter), p. 4 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 6 (Front matter) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Front matter), p. 1 (Front matter), p. 3 (Front matter) |
| Success / guarantee | instruction-conditioned task success | p. 2 (Front matter), p. 2 (Front matter), p. 5 (Front matter) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / Front matter - extractive body cue:** Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether success or failure in simulation predicts the ...
- **p. 3 / Front matter - extractive body cue:** 5, this figure shows the initial state, execution progress, and final state for the sweeping tasks. better understand the sim-to-real gap.
- **p. 3 / Front matter - extractive body cue:** Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all cases exhibiting aligned success or failure.
- **p. 4 / Front matter - extractive body cue:** 2) Infer Logic & Physics: Identify the causes of failures and the characteristics of successful attempts.

## What the Paper Changes

PDF contribution framing (p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 4 (Front matter)): For rigid objects, the numerical state consists of their full 6-DoF rigid transformation.

- **p. 1 / Front matter - extractive body cue:** Additionally, we present more qualitative examples, an ablation on the number of VLM-sampled action proposals, and a study comparing a CEM-based Prompting-with-theFuture-style variant [45], which ...
- **p. 2 / Front matter - extractive body cue:** Further Ablation Analysis We additionally consider a variant of our method in which we simultaneously replace the VLM sampler with a random sampler and switch ...
- **p. 3 / Front matter - extractive body cue:** Computation Time Table 5 reports the runtime of each component in our method.
- **p. 4 / Front matter - extractive body cue:** These results demonstrate that our method naturally generalizes to a wide range of scene variations, owing to the

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Correlation Between Simulation and RealWorld Performance This section examines the correlation between simulation and real-world results, specifically whether ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Across tasks, we observe a high degree of consistency between simulation and real-world outcomes, with 89% of all ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Simulated failures enable the VLM to avoid similar real-world failures, while simulated successes offer informative guidance for selecting ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | 2) Infer Logic & Physics: Identify the causes of failures and the characteristics of successful attempts. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 4 (Front matter), interface p. 4 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), objective p. 2 (Front matter), p. 2 (Front matter), p. 4 (Front matter), p. 5 (Front matter), p. 5 (Front matter), p. 6 (Front matter).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
