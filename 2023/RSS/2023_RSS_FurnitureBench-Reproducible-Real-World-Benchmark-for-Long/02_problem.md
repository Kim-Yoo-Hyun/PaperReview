# Problem - FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.12821; PDF retrieval source: https://arxiv.org/pdf/2305.12821. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to solve.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Reinforcement learning (RL), imitation learning (IL), and task and motion planning (TAMP) have demonstrated impressive performance across various robotic manipulation tasks.
- **p. 1 / Abstract - extractive PDF cue:** However, these approaches have been limited to learning simple behaviors in current real-world manipulation benchmarks, such as pushing or pick-and-place.
- **p. 1 / Abstract - extractive PDF cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...
- **p. 1 / Abstract - extractive PDF cue:** We present FurnitureBench, a reproducible real-world furniture assembly benchmark aimed at providing a low barrier for entry and being easily reproducible, so that researchers across ...
- **p. 1 / Abstract - extractive PDF cue:** For ease of use, we provide 200+ hours of precollected data (5000+ demonstrations), 3D printable furniture models, a robotic environment setup guide, and systematic task ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must be addressed to ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Furniture assembly is a proper task suite to benchmark a difficult, long-horizon manipulation task through which many challenges in robotic manipulation must ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Our reproducible robot system (a) and visual observations from the front-view camera (b) and wrist camera (c). of long-horizon complex robotic manipulation ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | reproducible, robot, system, visual, observations, front-view, camera, wrist, long-horizon, complex | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | Reinforcement, learning, imitation, task, motion, planning, TAMP, have | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: reproducible, robot, system, visual, observations, front-view, camera, wrist, long-horizon, complex | p. 2 (I. INTRODUCTION), p. 7 (2) The furniture parts are rearranged using our provided), p. 1 (Abstract) |
| Decision / output variable | method trajectory/action; body terms: main, contributions, follows, introduce, FurnitureBench, real-world, furniture, assembly | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | comparable score and protocol validity | p. 8 (Figure/Table caption), p. 7 (VI. BENCHMARKING RESULTS), p. 7 (VI. BENCHMARKING RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Due to the limitations imposed by using a single robotic arm, we modify some furniture pieces feasible to be assembled with one hand. strations that ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To further robotics research toward solving people's everyday tasks, it is crucial to tackle challenges in more complex and longer-horizon tasks.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 1 (Abstract)): The main contributions of this paper are as follows: • We introduce FurnitureBench, a real-world furniture assembly benchmark, which allows robotics researchers to investigate RL, IL, and TAMP algorithms on ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** To this end, we propose to focus on furniture assembly as the next milestone for complex, long-horizon robotic manipulation, and present FurnitureBench, a reproducible real-world ...
- **p. 1 / Abstract - extractive PDF cue:** To enable more complex, long-horizon behaviors of an autonomous robot, we propose to focus on real-world furniture assembly, a complex, longhorizon robot manipulation task that ...
- **p. 1 / Abstract - extractive PDF cue:** We present FurnitureBench, a reproducible real-world furniture assembly benchmark aimed at providing a low barrier for entry and being easily reproducible, so that researchers across ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 18 | Fig. 17: Furniture 3D models. IKEA model furniture (left), 3D furniture model (middle), and 3D printed furniture model ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The failure of these algorithms to even attach a pair of furniture parts despite the high-quality demonstration dataset ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | On the other hand, both algorithms struggle at "inserting" skill, which shows from 0% to 20% success rates. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 3: 3D printed furniture models. Each furniture is designed inspired by IKEA furniture. Due to the limitations ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (I. INTRODUCTION), p. 7 (2) The furniture parts are rearranged using our provided), p. 1 (Abstract), p. 1 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 7 (2) The furniture parts are rearranged using our provided), p. 1 (Abstract), p. 1 (Abstract), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
