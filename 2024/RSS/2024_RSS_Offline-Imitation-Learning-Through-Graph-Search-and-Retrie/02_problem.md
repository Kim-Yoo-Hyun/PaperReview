# Problem - Offline Imitation Learning Through Graph Search and Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p054.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p054.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES)): Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Imitation learning is a powerful machine learning algorithm for a robot to acquire manipulation skills.
- **p. 1 / Abstract - extractive body cue:** Nevertheless, many real-world manipulation tasks involve precise and dexterous robot-object interactions, which make it difficult for humans to collect high-quality expert demonstrations.
- **p. 1 / Abstract - extractive body cue:** As a result, a robot has to learn skills from suboptimal demonstrations and unstructured interactions, which remains a key challenge.
- **p. 1 / Abstract - extractive body cue:** Existing works typically use offline deep reinforcement learning (RL) to solve this challenge, but in practice these algorithms are unstable and fragile due to the ...
- **p. 1 / Abstract - extractive body cue:** To overcome this problem, we propose GSR, a simple yet effective algorithm that learns from suboptimal demonstrations through Graph Search and Retrieval.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Despite numerous challenges in both perception and action, our method can consistently improve baselines' success rate by 10% to 30% and proficiency by over 30%.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Moreover, there usually exist suboptimal behaviors within a successful demonstration, such as retrying to grip the item if the first attempt fails. | offline robot transition/trajectory dataset과 deployment MDP | body wording is the source claim |
| Observation / input | If we define w(o, a) = exp(A(o, a)) where A is the advantage of taking action a at observation o, this corresponds ... | dataset state/observation, action, reward와 return-to-go | exact sensor/frame/preprocessing from PDF body |
| State / latent | define, where, advantage, taking, action, observation, corresponds, policy, extraction, objective | Q/value 또는 sequence-policy state | notation and tensor shape require body check |
| Output / action | experiments, test, simulation, real-world, robotic, manipulation, tasks, various | dataset-supported action sequence | exact unit/frame/decoder require body check |
| Target outcome | offline return and deployment safety | offline policy value, OOD safety와 closed-loop success | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | dataset transition (s,a,r,s′); body terms: define, where, advantage, taking, action, observation, corresponds, policy, extraction, objective | p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 2 (I. INTRODUCTION) |
| Decision / output variable | dataset-supported policy action; body terms: direct, uses, graph, search, rather, deep, enjoys, high | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. POLICY LEARNING) |
| Objective / loss / cost | offline value with OOD control; cue terms: Algorithm, GSR, Optional, Finetune, pretrained, Build, graph, procedure | p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING) |
| Success / guarantee | offline return and deployment safety | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** Despite numerous challenges in both perception and action, our method can consistently improve baselines' success rate by 10% to 30% and proficiency by over 30%.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite the remarkable strides made so far, we notice that most existing works usually assume expert-level task demonstrations, while many real-world robotic manipulation tasks involve ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Problem Formulation In this paper, we study an offline policy learning setup.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING)): As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.

- **p. 2 / I. INTRODUCTION - extractive body cue:** We also provide various quantitative and qualitative analyses to show that our method is capable of identifying good behaviors in the dataset.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** We introduce the implementation details in the remaining sections.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To address the first problem, we propose to identify and connect similar states in the dataset to form a better distance estimate in section IV-B.
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** The pseudo-code of our method is summarized in Algorithm 1.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | However, in many cases, they will get stuck or go out of distribution, leading to a complete failure. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Interestingly, we have the following findings: (1) All the temporal segments that lead to the failures are weakened ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The robot is required to push a blue cylinder toward a green cube on the table. • Spoon ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This task highlights the challenge of robust perception against partial occlusion and fine-grained manipulation. • Tweezer Manipulation In ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

offline_rl writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 2 (I. INTRODUCTION), p. 4 (IV. POLICY LEARNING). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. PRELIMINARIES), interface p. 3 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 2 (I. INTRODUCTION), p. 4 (IV. POLICY LEARNING), objective p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
