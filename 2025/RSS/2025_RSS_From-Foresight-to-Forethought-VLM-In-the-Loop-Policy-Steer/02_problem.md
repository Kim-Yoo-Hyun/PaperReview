# Problem - From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p076.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p076.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1. InTRopucTION), p. 1 (1. InTRopucTION), p. 3 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 2 (1. InTRopucTION)): Initially, it may be tempting use the VLM directly as a black-box solver of Eq.1 (ie. t0 solve the overarching behavior generation problem) by simply passing it the Ix action ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While generative robot policies have demonstrated significant potential in learning complex, multimodal behaviors from demonstrations, they still exhibit diverse failures at eployment-time, Policy steering offers ...
- **p. 1 / Abstract - extractive body cue:** Here, one might hope to use a Vision Language Model (VLM) as a verifier leveraging its open-world reasoning capa bilities.
- **p. 1 / Abstract - extractive body cue:** However, off-the-shelf VLMs struggle to understand the ‘consequences of low-level robot actions as they are represented Tandamentally differently than the text and images the VIM ...
- **p. 1 / Abstract - extractive body cue:** In response, we propoxe FOREWARN, a novel Framework to unlock the potential of VLMs as open-vocabulary verifies for runtime poliy steering.
- **p. 1 / Abstract - extractive body cue:** Our key idea i to decouple the VEM's burden of predicting action outcomes Voresight) from ‘valuation forethought.
- **p. 3 / 1. InTRopucTION - extractive body cue:** Initially, it may be tempting use the VLM directly as a black-box solver of Eq.1 (ie. t0 solve the overarching behavior generation problem) by simply ...
- **p. 1 / 1. InTRopucTION - extractive body cue:** However, at runtime, the policy exhibits a range of degradations, from complete task failures (such as the robot knocking down the cup during grasping, shown ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Initially, it may be tempting use the VLM directly as a black-box solver of Eq.1 (ie. t0 solve the overarching behavior generation ... | uncertain robot state와 safe/unsafe operating region | body wording is the source claim |
| Observation / input | The robot's observations 0 < O :=ZxQ combine RGB image data I € T and proprioceptive states q © Q(eg., end-effector pose, ... | observation, uncertainty/risk estimate와 task command | exact sensor/frame/preprocessing from PDF |
| State / latent | robot, observations, ZxQ, combine, RGB, image, data, proprioceptive, states, end-effector | safe set, recovery state 또는 constraint margin | notation and tensor shape require body check |
| Output / action | contribute, predictive, category, methods, anticipates, future, outcomes, policy | shielded, recovery 또는 safe action | exact unit/frame/decoder require body check |
| Target outcome | low violation/failure probability with useful intervention | task return과 violation/failure probability | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | state/history and risk h(s); body terms: robot, observations, ZxQ, combine, RGB, image, data, proprioceptive, states, end-effector | p. 3 (1. InTRopucTION), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION) |
| Decision / output variable | filtered/recovery action u_safe; body terms: Figure, present, examples, runtime, policy, steering, Fork, task | p. 8 (B. Policy Steering for Open-World Alignment), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION) |
| Objective / loss / cost | task utility subject to safety constraint; cue terms: Inthe, Bag, task, modify, original, description, Please, pick | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (B. Policy Steering for Open-World Alignment), p. 6 (A. From Action Rollouts to Behavior Narration), p. 9 (B. Policy Steering for Open-World Alignment) |
| Success / guarantee | low violation/failure probability with useful intervention | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. InTRopucTION - extractive body cue:** However, at runtime, the policy exhibits a range of degradations, from complete task failures (such as the robot knocking down the cup during grasping, shown ...
- **p. 3 / 1. InTRopucTION - extractive body cue:** However, this strategy is sampleinefficient, requiring extensive embodied rollouts and human annotations to generate labels, Instead, we propose tackling the problem in Eq.1 in a ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** complexity of dynamics modeling and the difficulty of hand
- **p. 2 / 1. InTRopucTION - extractive body cue:** Here, existing approaches [22, 24, 25] often rely on out-of-distribution (OOD) detection in a latent space or dense human labels to train a binary classifier ...

## What the Paper Changes

PDF contribution framing (p. 8 (B. Policy Steering for Open-World Alignment), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 1 (Front matter), p. 1 (Abstract)): In Figure 4, we present examples of runtime policy steering using our approach for the Fork task and additional examples for Cup and Bag tasks are included in Appendix B2.

- **p. 4 / 1. InTRopucTION - extractive body cue:** The training data consists of both successful and failed rollouts from the base policy (a / 0) and additional demonstration data, This allows the world ...
- **p. 2 / 1. InTRopucTION - extractive body cue:** Ultimately, this alignment step enables ‘our "VLM-in-the-loop" policy steering approach to interpret, action plans as behavior narrations and select high-quality plans by reasoning over those ...
- **p. 1 / Front matter - extractive body cue:** 1: We present FOREWARN, an VLM-in-the-loop policy steering algorithm for multi-modal generative robot policies.
- **p. 1 / Abstract - extractive body cue:** We validate our framework across diverse robotic manipulation tasks, demonstrating its ability to bridge representational gaps and provide robust, generalizable policy steering.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | We consider three real-world robot manipulation tasks that exhibit underlying multi-modal behavio hhard-to-model outcomes, and nuanced failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We use this task to study how our framework performs when faced with harder-to-predict interaction outcomes and nuanced ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | (4) Classfier-Dyn-Latent, which is similar to VLM-DynLat-Category, but instead of relying ‘on a VLM, it directly takes the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | B2 revealed that our system's primary failures stem from the world model's imprecise "imagination", exacerbated by our limited ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

safety writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1. InTRopucTION), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 2 (1. InTRopucTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1. InTRopucTION), p. 1 (1. InTRopucTION), p. 3 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 2 (1. InTRopucTION), interface p. 3 (1. InTRopucTION), p. 4 (1. InTRopucTION), p. 2 (1. InTRopucTION), p. 2 (1. InTRopucTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
