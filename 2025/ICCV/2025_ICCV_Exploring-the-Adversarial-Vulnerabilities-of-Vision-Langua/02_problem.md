# Problem - Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary)): This offers valuable insights for the research community to explore systemic failures in similar concurrent generative foundation models;  We rigorously evaluate our approach in both simulated and real-world environments ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recently in robotics, Vision-Language-Action (VLA) models have emerged as a transformative approach, enabling robots to execute complex tasks by integrating visual and linguistic inputs within ...
- **p. 1 / Abstract - extractive body cue:** Despite their significant capabilities, VLA models introduce new attack surfaces.
- **p. 1 / Abstract - extractive body cue:** This paper systematically evaluates their robustness.
- **p. 1 / Abstract - extractive body cue:** Recognizing the unique demands of robotic execution, our attack objectives target the inherent spatial and functional characteristics of robotic systems.
- **p. 1 / Abstract - extractive body cue:** In particular, we introduce two untargeted attack objectives that leverage spatial foundations to destabilize robotic actions, and a targeted attack objective that manipulates the robotic ...
- **p. 2 / 1. Introduction - extractive body cue:** This offers valuable insights for the research community to explore systemic failures in similar concurrent generative foundation models;  We rigorously evaluate our approach in ...
- **p. 1 / 1. Introduction - extractive body cue:** Failure Rate Comparison BV2 LIBERO A.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This offers valuable insights for the research community to explore systemic failures in similar concurrent generative foundation models;  We rigorously evaluate ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | 2) are built on large language models integrated with visual encoders, enabling robots to interpret human instructions and process visual input from ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | built, large, language, models, integrated, visual, encoders, enabling, robots, interpret | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | next, calculate, applied, action, discrepancy, measure, deviation, between | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: built, large, language, models, integrated, visual, encoders, enabling, robots, interpret | p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack) |
| Decision / output variable | action, pose, option or chunk a; body terms: Additionally, introduce, Geometry-Aware, Objective, considers, robot, movement, three-dimensional | p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3.2. Untargeted Action Discrepancy Attack) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Instead, directly, misclassification, target, introduce, soft, attack, objective | p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.4. Targeted Manipulation Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack) |
| Success / guarantee | instruction-conditioned task success | p. 8 (4.3. Main Result), p. 8 (Figure/Table caption), p. 6 (4.2. Experiment Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Failure Rate Comparison BV2 LIBERO A.
- **p. 1 / 1. Introduction - extractive body cue:** Comparison of failure rates across different attack schemes (UADA, UPA, and TMA).
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, our work intensifies the adversarial threats posed to VLA-based systems by both developing specialized attack objectives and designing effective attack methods.
- **p. 3 / 3.1. Preliminary - extractive body cue:** This control design presents a unique challenge for adversarial attacks, as finely divided bins result in minimal action discrepancies between neighboring bins (e.g., ±0.007/bin).

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.3. Untargeted Position-aware Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack)): Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom.

- **p. 3 / 3. Methodology - extractive body cue:** Finally, we introduce the Normalized Action Discrepancy (NAD) metric in §3.5.
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** To exacerbate action discrepancies, we introduce the Untargeted Action Discrepancy Attack (UADA), which aims to maximize deviations in robot actions.
- **p. 4 / 3.3. Untargeted Position-aware Attack - extractive body cue:** Recognizing the importance of Ap = DT(yp) in controlling the end-effector's path, we introduce a position-aware attack to disrupt the intended movement trajectory.
- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Both UADA and UPA effectively disrupt robot execution, yielding maximum average failure rates of 100% and 89.7%, respectively. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | For UADA and UPA, our methods effectively amplify action discrepancies, leading to a notable transfer attack ability in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Failure Rate (FR, ↑) and its standard deviation across tasks within LIBERO [44] suite are reported. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Preliminary), interface p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack), objective p. 4 (3.4. Targeted Manipulation Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.2. Untargeted Action Discrepancy Attack).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
