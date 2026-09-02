# Problem - 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p067.html; PDF retrieval source: https://arxiv.org/pdf/2403.03954.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): To collect the required extensive number of demonstrations, the entire data-gathering process can span several days due to its long-horizon nature and failure-prone process.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations.
- **p. 1 / Abstract - extractive body cue:** To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations ...
- **p. 1 / Abstract - extractive body cue:** The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder.
- **p. 1 / Abstract - extractive body cue:** In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement.
- **p. 1 / Abstract - extractive body cue:** In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To collect the required extensive number of demonstrations, the entire data-gathering process can span several days due to its long-horizon nature and failure-prone process.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Nevertheless, online learning in real-world scenarios introduces its own challenges, such as safety considerations, the necessity for automatic resetting, human intervention, and additional robot hardware ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To collect the required extensive number of demonstrations, the entire data-gathering process can span several days due to its long-horizon nature and ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | End-to-End, Training, Policy, Expert, Demonstrations, Evaluation, Action, Observation, Decision, Diffusion | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Visual, imitation, learning, takes, high-dimensional, observations, images, depth | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: End-to-End, Training, Policy, Expert, Demonstrations, Evaluation, Action, Observation, Decision, Diffusion | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: introduce, Diffusion, Policy, DP3, mainly, consists, critical, parts | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective / loss / cost | task/contact/pose objective; cue terms: training, objective, predict, noise, added, original, data, MSE | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHOD), p. 6 (2) Learning efficiency. While we train all the algorithms) |
| Success / guarantee | completion, contact success and robustness | p. 5 (IV. SIMULATION EXPERIMENTS), p. 5 (IV. SIMULATION EXPERIMENTS), p. 4 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Nevertheless, online learning in real-world scenarios introduces its own challenges, such as safety considerations, the necessity for automatic resetting, human intervention, and additional robot hardware ...

## What the Paper Changes

PDF body contribution framing (p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION)): To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.

- **p. 1 / I. INTRODUCTION - extractive body cue:** To tackle this challenging problem, we introduce 3D Diffusion Policy (DP3), a simple yet effective visual imitation learning algorithm that integrates the strengths of 3D ...
- **p. 3 / III. METHOD - extractive body cue:** The network, termed as DP3 Encoder, is conceptually simple: it consists of a three-layer MLP, a max-pooling function as an order-equivariant operation to pool point ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To comprehensively evaluate DP3, we have developed a simulation benchmark comprising 72 diverse robotic tasks from 7 domains, alongside 4 real-world tasks including challenging dexterous ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Fig. 3: Generalization in 3D space with few data. We use MetaWorld Reach as an example task, given ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | For instance, the image-based diffusion policy excels in the Drill task but fails entirely in Roll-Up. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | It is noteworthy that the depthbased diffusion policy also does not incorporate color as input. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 6 (2) Learning efficiency. While we train all the algorithms). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 6 (2) Learning efficiency. While we train all the algorithms), objective p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
