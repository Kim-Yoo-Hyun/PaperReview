# Problem - SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html; PDF retrieval source: https://arxiv.org/pdf/2509.18610. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): [8] introduces FiGS, a high-fidelity Gaussian-Splatting-based drone simulator to narrow the sim-to-real gap for stronger real-world transfer; however, FiGS lacks the semantic knowledge required for open-world drone navigation, limiting ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Large vision-language models have driven remarkable progress in open-vocabulary robot policies, e.g., generalist robot manipulation policies, that enable robots to complete complex tasks specified in ...
- **p. 1 / Abstract - extractive PDF cue:** Despite these successes, open-vocabulary autonomous drone navigation remains an unsolved challenge due to the scarcity of largescale demonstrations, real-time control demands of drones for stabilization, ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we present SINGER for language-guided autonomous drone navigation in the open world using only onboard sensing and compute.
- **p. 1 / Abstract - extractive PDF cue:** To train robust, open-vocabulary navigation policies, SINGER leverages three central components: (i) a photorealistic language-embedded flight simulator with minimal sim-to-real gap using Gaussian Splatting for ...
- **p. 1 / Abstract - extractive PDF cue:** Through extensive hardware flight experiments, we demonstrate superior zero-shot sim-to-real transfer of our policy to unseen environments and unseen language-conditioned goal objects.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** [8] introduces FiGS, a high-fidelity Gaussian-Splatting-based drone simulator to narrow the sim-to-real gap for stronger real-world transfer; however, FiGS lacks the semantic knowledge required for ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address the data scarcity challenge, prior work [6], [7] trains visuomotor policies for drone navigation in simulation, but the effectiveness of the resulting policies ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | [8] introduces FiGS, a high-fidelity Gaussian-Splatting-based drone simulator to narrow the sim-to-real gap for stronger real-world transfer; however, FiGS lacks the semantic ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | In this work, we ask the question: "Can we train a visionlanguage drone navigation policy to reach previously unseen goal objects in ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | question, train, visionlanguage, drone, navigation, policy, reach, previously, unseen, goal | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | SINGER, consists, three, central, components, semantics-rich, photorealistic, flight | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: question, train, visionlanguage, drone, navigation, policy, reach, previously, unseen, goal | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: summarize, contributions, follows, introduce, high-fidelity, drone, simulator, efficient | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: full, network, trained, loss, expert, demonstrator, motor, commands | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To address the data scarcity challenge, prior work [6], [7] trains visuomotor policies for drone navigation in simulation, but the effectiveness of the resulting policies ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This is exacerbated by inherent challenges in collecting large quantities of high quality visuomotor data on highly dynamic and naturally unstable drones.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this paper, we introduce SINGER (Semantic In-situ Navigation and Guidance for Embodied Robots), a pipeline for training language-conditioned drone navigation policies addressing the aforementioned ...

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We summarize our contributions as follows: • We introduce a high-fidelity drone simulator for efficient imitation learning in language-specified drone navigation problems built on language embedded Gaussian Splatting. • We ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this paper, we introduce SINGER (Semantic In-situ Navigation and Guidance for Embodied Robots), a pipeline for training language-conditioned drone navigation policies addressing the aforementioned ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | SINGER performs the best at this experiment difficulty, reaching the goal region 73% of the time, and reaching ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This results in one more failure case (6/30) vs. the baseline at (5/30) due to tracking the incorrect ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Crosshatching direction on unsuccessful trials denotes the reason for failure, where collisions are counted while the policy has ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The policy is evaluated on successful flight towards the queried object without collisions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective p. 5 (V. SINGER POLICY ARCHITECTURE AND TRAINING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
