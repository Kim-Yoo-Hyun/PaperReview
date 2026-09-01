# Problem - Where2Act: From Pixels to Actions for Articulated 3D Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02692; PDF retrieval source: https://arxiv.org/pdf/2101.02692. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Problem Statement)): We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** One of the fundamental goals of visual perception is to allow agents to meaningfully interact with their environment.
- **p. 1 / Abstract - extractive body cue:** In this paper, we take a step towards that long-term goal - we extract highly localized actionable information related to elementary actions such as pushing ...
- **p. 1 / Abstract - extractive body cue:** For example, given a drawer, our network predicts that applying a pulling force on the handle opens the drawer.
- **p. 1 / Abstract - extractive body cue:** We propose, discuss, and evaluate novel network architectures that given image and depth data, predict the set of actions possible at each pixel, and the ...
- **p. 1 / Abstract - extractive body cue:** We propose a learning-from-interaction framework with an online data sampling strategy that allows us to train the network in simulation (SAPIEN) and generalizes across categories.
- **p. 2 / 1. Introduction - extractive body cue:** We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Taking, input, single, RGB, image, partial, point, cloud, employ, encoder-decoder | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | therefore, on-policy, data, sampling, strategy, alleviate, issue, biasing | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Taking, input, single, RGB, image, partial, point, cloud, employ, encoder-decoder | p. 3 (4. Method), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, formulate, task, inferring, affordances, manipulating, articulated | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: After, adjusting, relative, loss, scales, same, level, obtain | p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.3. Training and Losses), p. 4 (4.1. Network Modules), p. 4 (4.2. Collecting Training Data) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 1 (Figure/Table caption), p. 6 (5.2. Metrics and Baselines), p. 8 (5.3. Results and Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 3 / 3. Problem Statement - extractive body cue:** We formulate a new challenging problem Where2Act - inferring per-pixel ‘actionable information' for manipulating 3D articulated objects.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method), p. 3 (4.1. Network Modules), p. 4 (4.2. Collecting Training Data)): In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach ...

- **p. 2 / 1. Introduction - extractive body cue:** We empirically show that our method successfully learns to predict possible actions for novel objects, and does so even for previously unseen categories.
- **p. 3 / 4. Method - extractive body cue:** We propose a learning-from-interaction approach to tackle this task.
- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** Instead, we propose to let the agent learn by interacting with objects in simulation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Finally, our method does not explicitly model the part segmentation and part motion axis, which may be incorporated ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (4. Method), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Network Modules). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Problem Statement), interface p. 3 (4. Method), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Network Modules), objective p. 5 (4.3. Training and Losses), p. 5 (4.3. Training and Losses).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
