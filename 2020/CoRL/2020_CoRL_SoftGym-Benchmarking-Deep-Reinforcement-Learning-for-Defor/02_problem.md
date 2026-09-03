# Problem - SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2011.07215; PDF retrieval source: https://arxiv.org/pdf/2011.07215. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, programming a robot to perform these tasks has long been a challenge in robotics due to the high dimensional state representation and complex dynamics [1, 2, 3].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Manipulating deformable objects has long been a challenge in robotics due to its high dimensional state representation and complex dynamics.
- **p. 1 / Abstract - extractive body cue:** Recent success in deep reinforcement learning provides a promising direction for learning to manipulate deformable objects with data driven methods.
- **p. 1 / Abstract - extractive body cue:** However, existing reinforcement learning benchmarks only cover tasks with direct state observability and simple low-dimensional dynamics or with relatively simple image-based environments, such as those ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and a Python ...
- **p. 1 / Abstract - extractive body cue:** Our benchmark will enable reproducible research in this important area.
- **p. 1 / 1 Introduction - extractive body cue:** However, such low-dimensional sufficient state representations are difficult to perceive (or sometimes even define) for many deformable object tasks, such as laundry folding or dough ...
- **p. 2 / 1 Introduction - extractive body cue:** These environments highlight the difficulty in performing robot manipulation tasks in environments that have complex visual observations with partial observability and an inherently high dimensional ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, programming a robot to perform these tasks has long been a challenge in robotics due to the high dimensional state representation ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | We benchmark a range of algorithms on these environments assuming different observation spaces for the policy, including full knowledge of the ground-truth ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | benchmark, range, algorithms, environments, assuming, different, observation, spaces, policy, including | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Reduced, State, Oracle, avoid, challenges, high-dimensional, spaces, uses | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: benchmark, range, algorithms, environments, assuming, different, observation, spaces, policy, including | p. 2 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction) |
| Decision / output variable | method trajectory/action; body terms: present, SoftGym, open-source, simulated, benchmarks, manipulating, deformable, objects | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: Given, information, gradient, free, optimization, maximize, return, Among | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 16 (Figure/Table caption), p. 16 (Figure/Table caption), p. 6 (6 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** However, such low-dimensional sufficient state representations are difficult to perceive (or sometimes even define) for many deformable object tasks, such as laundry folding or dough ...
- **p. 2 / 1 Introduction - extractive body cue:** These environments highlight the difficulty in performing robot manipulation tasks in environments that have complex visual observations with partial observability and an inherently high dimensional ...
- **p. 2 / 1 Introduction - extractive body cue:** Due to the large number of samples required by reinforcement learning, as well as the difficulty in specifying a reward function, all these works start ...
- **p. 3 / 1 Introduction - extractive body cue:** 4.1 Action Space We aim to decouple the challenges in learning low-level grasping skills from high-level planning.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction)): In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments.

- **p. 3 / 1 Introduction - extractive body cue:** SoftGym consists of three parts: SoftGym-Medium, SoftGym-Hard and SoftGym-Robot, visualized in Figure 1.
- **p. 3 / 1 Introduction - extractive body cue:** 4 SoftGym To advance research in reinforcement learning in complex environments with an inherently high dimensional state, we propose SoftGym.
- **p. 2 / 1 Introduction - extractive body cue:** As such, we believe that SoftGym would be a unique and valuable contribution to the reinforcement learning and robotics communities, by enabling new methods to ...
- **p. 4 / 1 Introduction - extractive body cue:** This action space is designed to enable the user to focus on the challenges of high-level planning and to abstract away the low-level manipulation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | from a policy that always does nothing. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | On the other hand, this method does not perform very well on the FoldCloth task. | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Table 7: Architecture of the deconvolutional neural network (VAE decoder) in PlaNet. We use a GRU [56] with ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, programming a robot to perform these tasks has long been a challenge in robotics due to the high dimensional state representation and complex dynamics [1, 2, 3]. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** In this paper, we present SoftGym, a set of open-source simulated benchmarks for manipulating deformable objects, with a standard OpenAI Gym API and Python interface for creating new environments. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** We do not include the latent over-shooting in our experiment as it does not improve much over the one-step case. (p. 17, B.4 PlaNet).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
