# SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p128.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p128.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, mobile manipulation, Imitation Learning, safety constraints
- Official paper: https://www.roboticsproceedings.org/rss21/p128.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p128.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p128.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real world, Further, these methods require extensive trial-anderror learning ...를 문제로 두고, environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more efficiently than direct sim-to-real imitation learning approaches ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Kor robots to become efficient helpers in the home, they must learn to perform new mobile manipulation tasks simply by watching humans perform them.
- **p. 1 / Abstract - extractive body cue:** Learning from a single video demonstration from a human is challenging as the robot needs to first extract from the demo what needs to be ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, to mitigate the dependency on costly human ‘monitoring, this learning process should be performed in a sale 1d autonomous manner.
- **p. 1 / Abstract - extractive body cue:** We present SAFEMIMIC, a framework to learn new mobile manipulation skills safely and autonomously from a single third-person human video, Given an initial human ideo ...
- **p. 1 / Abstract - extractive body cue:** Then, it adapts the behavior to the robot's own morphology by sampling candidate actions around the human ones, and verifying them for safety before execution ...
- **p. 2 / I. INrRopucTION - extractive body cue:** These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real world, ...
- **p. 3 / I. INrRopucTION - extractive body cue:** However, these approaches assume access to a black box policy or dynamics model of the environment, both which are unknown in the ‘case of learning ...

## Core Idea

- **p. 2 / I. INrRopucTION - extractive body cue:** environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more efficiently ...
- **p. 1 / Abstract - extractive body cue:** Our experiments show that our method allows robots to safely fand efficiently learn multistep mobile manipulation behaviors from a single human demonstration, from different users, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** In summary, SAFEMIMIC introduces several novel contributions:
- **p. 1 / Abstract - extractive body cue:** We present SAFEMIMIC, a framework to learn new mobile manipulation skills safely and autonomously from a single third-person human video, Given an initial human ideo ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** The state representation consists of simulated pointclouds and robot proprioceptive information (for details of the network architecture, see Appendix A).
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** The architecture for the action prediction policy network is composed by a PointNet [66] encoder for the visual information, and a SentenceTransformer [67] for the ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based ...
- **p. 1 / Abstract - extractive body cue:** Then, it adapts the behavior to the robot's own morphology by sampling candidate actions around the human ones, and verifying them for safety before execution ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based on a BCRNN Behavior Cloning policy with ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 6 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation) |
| State/latent | evaluate, data, generated, train, safety, Qfunctions, would, suffice, training, task, policies, include | map/object/contact state와 base-arm coordination decision | p. 6 (C. Learning from Previous Successful Exploration), p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 5 (C. Learning from Previous Successful Exploration) |
| Output/action | Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, given formally by: | base motion plus arm/gripper action | p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 5 (C. Learning from Previous Successful Exploration), p. 2 (I. INrRopucTION) |
| Objective/outcome | Given this function, the robot's objective is to find a policy that maps states to the actions that maximize the task reward while remaining safe, given formally by: | long-horizon task success, reachability, collision과 recovery | p. 4 (B. Safe and Autonomous Real-World Adaptation), p. 2 (I. INrRopucTION), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / I. INrRopucTION - extractive body cue:** environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more efficiently ...
- **p. 1 / Abstract - extractive body cue:** Our experiments show that our method allows robots to safely fand efficiently learn multistep mobile manipulation behaviors from a single human demonstration, from different users, ...
- **p. 2 / I. INrRopucTION - extractive body cue:** In summary, SAFEMIMIC introduces several novel contributions:
- **p. 1 / Abstract - extractive body cue:** We present SAFEMIMIC, a framework to learn new mobile manipulation skills safely and autonomously from a single third-person human video, Given an initial human ideo ...
- **p. 4 / B. Safe and Autonomous Real-World Adaptation - extractive body cue:** The state representation consists of simulated pointclouds and robot proprioceptive information (for details of the network architecture, see Appendix A).
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** We observe that SAFEMIMIC achieves a minimum of 40% final suc- ‘cess rate over the seven tasks, significantly outperforming all baselines.
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** The Direct Execution baseline achieves 0% final success rate on all the seven tasks, demonstrating the need for exploration in order to effectively adapt the ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** Note as well hat some lines overlap at the Same ly outperforms all baselines and achieves upto 100% sucess ia exploratory adaptation, indcaling © superior

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration) |
| Embodiment/environment | We also evaluate if the data generated to train our safety Qfunctions would suffice for training task policies: we include Imitation Learning (1L) baselines based on a BCRNN Behavior Cloning policy with ... | hardware/simulator version and reset protocol | p. 6 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration) |
| Dataset/benchmark | In our experiments, we aim to answer four questions: QI) Does SAFEMIMIC enable a robot to successfully complete a multi-step mobile manipulation task from a third-person demonstration? | role, split, size and leakage | p. 6 (C. Learning from Previous Successful Exploration), p. 8 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration) |
| Metric | Fig. 4. Accumulated Success on Mult-Step Tasks. Accumulated success rate at each stage of each ofthe seven evaluated multi-step mobile manipulation tasks, indicating the percentage ofthe five tals each method completed up ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration) |
| Baseline/ablation | Note as well hat some lines overlap at the Same ly outperforms all baselines and achieves upto 100% sucess ia exploratory adaptation, indcaling © superior | fair input/data/compute/action matching | p. 6 (C. Learning from Previous Successful Exploration), p. 7 (C. Learning from Previous Successful Exploration), p. 6 (C. Learning from Previous Successful Exploration) |

## Explicit Limitations and Failure Boundary

- **p. 8 / V. LIMITATIONS AND FUTURE WORK - extractive body cue:** Scaling to other types of safety violations or task failures presents an opportunity for future work.
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** We evaluate SaFEMIMIC in 7 challenging multi-step mobile ‘manipulation tasks demonstrated by humans. ‘The tasks all consist of multiple stages and require navigation, rigid-body pick-and-place, ...
- **p. 6 / C. Learning from Previous Successful Exploration - extractive body cue:** While SAFEMIMIC is generic and can include many possible failure modes, we consider the following in this work: arm collisions, base collisions, joint limit violations, ...
- **p. 8 / V. LIMITATIONS AND FUTURE WORK - extractive body cue:** However, there are some limitations of the method that offer exciting avenues for future work.
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** Q2) How effectively does SAFEMIMIC reduce safetycritical failures?
- **p. 5 / C. Learning from Previous Successful Exploration - extractive body cue:** This task requires differentiating the human's semantic goal, and avoiding collisions and adapting grasps for successful placement.
- **p. 7 / C. Learning from Previous Successful Exploration - extractive body cue:** While the imitation-learning baselines demonstrate some successes, they fail to reliably perform the tasks, indicating that while the small amount of noisy data we generate ...

## Why Read It

World models, safety, uncertainty, and recovery의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 These works address the requirement of autonomy, but generally sidestep the question of safety - ‘critical challenge when learning mobile manipulation in the real world, Further, these methods require extensive trial-anderror learning ...를 문제로 두고, environments with different human teachers, and observe experimentally that our framework enables the robot to suc cessfully acquire the desired behaviors safely and more efficiently than direct sim-to-real imitation learning approaches ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 1 (I. INrRopucTION), p. 2 (I. INrRopucTION), p. 3 (I. INrRopucTION), p. 5 (C. Learning from Previous Successful Exploration) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
