# Problem - SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p128.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p128.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 1 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION)): These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real world, Further, these methods require extensive ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Kor robots to become efficient helpers in the home, they must learn to perform new mobile manipulation tasks simply by watching humans perform them.
- **p. 1 / Abstract - extractive body cue:** Learning from a single video demonstration from a human is challenging as the robot needs to first extract from the demo what needs to be ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, to mitigate the dependency on costly human ‘monitoring, this learning process should be performed in a sale 1d autonomous manner.
- **p. 1 / Abstract - extractive body cue:** We present SAFEMIMIC, a framework to learn new mobile manipulation skills safely and autonomously from a single third-person human video, Given an initial human ideo ...
- **p. 1 / Abstract - extractive body cue:** Then, it adapts the behavior to the robot's own morphology by sampling candidate actions around the human ones, and verifying them for safety before execution ...
- **p. 2 / I. INrRopucTION - extractive body cue:** These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real world, ...
- **p. 3 / I. INrRopucTION - extractive body cue:** However, these approaches assume access to a black box policy or dynamics model of the environment, both which are unknown in the ‘case of learning ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | evaluate, data, generated, train, safety, Qfunctions, would, suffice, training, task | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | then, train, action, prediction, policy, network, maps, point | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: evaluate, data, generated, train, safety, Qfunctions, would, suffice, training, task | p. 6 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 5 (C. Learning from Previous Successful Exploration) |
| Decision / output variable | base plus arm/gripper action; body terms: environments, different, human, teachers, observe, experimentally, framework, enables | p. 2 (I. INrRopucTION), p. 1 (Abstract), p. 2 (I. INrRopucTION) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Given, function, robot, objective, find, policy, maps, states | p. 2 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 4 (B. Safe and Autonomous Real-World Adaptation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION) |
| Success / guarantee | task completion and recovery | p. 6 (Figure/Table caption), p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 3 / I. INrRopucTION - extractive body cue:** However, these approaches assume access to a black box policy or dynamics model of the environment, both which are unknown in the ‘case of learning ...
- **p. 1 / I. INrRopucTION - extractive body cue:** Learning multi-step tasks from a human video in a safe and self-supervised manner presents multiple technical challenges. rst, it requires for the robot to understand ...
- **p. 2 / I. INrRopucTION - extractive body cue:** ‘overcomes all aforementioned challenges: firs, it parses the
- **p. 3 / I. INrRopucTION - extractive body cue:** SAFEMIMIC provides a unified framework for failure prediction when learning mobile manipulation behaviors from hhuman videos.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INrRopucTION), p. 1 (Abstract), p. 2 (I. INrRopucTION), p. 1 (Abstract), p. 4 (B. Safe and Autonomous Real-World Adaptation)): environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more efficiently than direct sim-to-real imitation learning ...

- **p. 1 / Abstract - extractive body cue:** Our experiments show that our method allows robots to safely fand efficiently learn multistep mobile manipulation behaviors from a single human demonstration, from different users, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** In summary, SAFEMIMIC introduces several novel contributions:
- **p. 1 / Abstract - extractive body cue:** We present SAFEMIMIC, a framework to learn new mobile manipulation skills safely and autonomously from a single third-person human video, Given an initial human ideo ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** The state representation consists of simulated pointclouds and robot proprioceptive information (for details of the network architecture, see Appendix A).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Scaling to other types of safety violations or task failures presents an opportunity for future work. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We evaluate SaFEMIMIC in 7 challenging multi-step mobile ‘manipulation tasks demonstrated by humans. ‘The tasks all consist of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | While SAFEMIMIC is generic and can include many possible failure modes, we consider the following in this work: ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | However, there are some limitations of the method that offer exciting avenues for future work. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 5 (C. Learning from Previous Successful Exploration), p. 2 (I. INrRopucTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 1 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), interface p. 6 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 5 (C. Learning from Previous Successful Exploration), p. 2 (I. INrRopucTION), objective p. 2 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 4 (B. Safe and Autonomous Real-World Adaptation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, these approaches assume access to a black box policy or dynamics model of the environment, both which are unknown in the ‘case of learning a new task from human ... (p. 3, I. INrRopucTION).
- **Formulation-changing contribution:** In summary, SAFEMIMIC introduces several novel contributions: (p. 2, I. INrRopucTION).
- **Assumption/failure evidence:** Similarly, motion planning methods [61, 62] ‘enable collision-free motion generation for a given environment geometry but fail to capture other possible failure modes involving contact, such as force-torque limit violations ... (p. 3, I. INrRopucTION).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
