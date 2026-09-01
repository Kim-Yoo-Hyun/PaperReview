# IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2305.17110.
> PDF retrieval source: https://arxiv.org/pdf/2305.17110. Reading tracker status/evidence was not changed.

- Year/Venue: 2023 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, assembly, contact-rich manipulation, Reinforcement Learning, sim-to-real, industrial robotics
- Official paper: https://arxiv.org/abs/2305.17110
- Full-text retrieval: https://arxiv.org/pdf/2305.17110
- Code/Project: https://research.nvidia.com/labs/srl/projects/industreal/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics.를 문제로 두고, Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as a list of all purchased parts.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robotic assembly is a longstanding challenge, requiring contact-rich interaction and high precision and accuracy.
- **p. 1 / Abstract - extractive body cue:** Many applications also require adaptivity to diverse parts, poses, and environments, as well as low cycle times.
- **p. 1 / Abstract - extractive body cue:** In other areas of robotics, simulation is a powerful tool to develop algorithms, generate datasets, and train agents.
- **p. 1 / Abstract - extractive body cue:** However, simulation has had a more limited impact on assembly.
- **p. 1 / Abstract - extractive body cue:** We present IndustReal, a set of algorithms, systems, and tools that solve assembly tasks in simulation with reinforcement learning (RL) and successfully achieve policy transfer ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To our knowledge, this is the first system for sim-to-real of all phases of the assembly problem: from detection, to grasping, to part alignment, to ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** IndustRealKit allows the research community to easily replicate our experimental hardware and benchmark their performance. • Software: We present IndustRealLib, a lightweight Python library that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We present IndustReal, a set of algorithms, systems, and tools for solving contact-rich assembly tasks in simulation and transferring behaviors to reality (Figure 1).
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** In addition, for the Insert policies, we introduced observation noise.
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and ...
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Joint Evaluation As described in Sections IV-E-IV-G, we proposed three algorithms for improving learning of contact-rich Insert policies: Simulation-Aware Policy Update to adapt to simulator ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Thus, we propose our first algorithm, a simulation-aware policy update (SAPU), where the agent is encouraged to learn policies that avoid interpenetrations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and parameterized by a network with weights θ; ... | RGB-D/point cloud, object state와 contact/task observation | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |
| State/latent | proximal, policy, optimization, PPO, learn, stochastic, actor, mapping, observations, actions, parameterized, network | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 1 (I. INTRODUCTION) |
| Output/action | An established approach for applying policy actions is sd t+1 = st ⊕at = st ⊕Π(ot), (2) where sd t+1 is the desired state, at is an action expressed as an incremental ... | grasp, pose, force 또는 end-effector trajectory | p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 1 (I. INTRODUCTION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |
| Objective/outcome | The objective was to learn a policy π : O →P(A) that maximized the expected sum of discounted rewards Eπ[ΣT -1 t=0 γtr(st)]. | task completion, contact success, pose/force error와 generalization | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 3 (IV. POLICY LEARNING IN SIMULATION) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** IndustRealKit allows the research community to easily replicate our experimental hardware and benchmark their performance. • Software: We present IndustRealLib, a lightweight Python library that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We present IndustReal, a set of algorithms, systems, and tools for solving contact-rich assembly tasks in simulation and transferring behaviors to reality (Figure 1).
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** In addition, for the Insert policies, we introduced observation noise.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value at ...
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III).
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Key Results: The system demonstrated even higher success rates than during the Insert experiment: 80% and 88.3% success/engagement rates for peg insertion, 97.5% and 100% ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| Embodiment/environment | The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects before releasing them. | hardware/simulator version and reset protocol | p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS) |
| Dataset/benchmark | Sort Demonstration This experiment qualitatively demonstrated the ability of the robot to execute a realistic sorting procedure. | role, split, size and leakage | p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS) |
| Metric | Key Results: The system demonstrated extremely high success rates (98.8%) across all pegs (Table III). | definition, denominator, direction and uncertainty | p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 4 (Figure/Table caption) |
| Baseline/ablation | Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the specified value at test time. Boxes indicate median and IQR. ... | fair input/data/compute/action matching | p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their ...
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this ...
- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Our work has limitations, which lend themselves naturally to future research directions.
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Failure cases were one missed detection of a peg, as well as one grasp of both a peg and its corresponding peg tray.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. Bottom: ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Joint evaluation of Simulation-Based Policy Update, SDF-Based Dense Reward, and Sampling-Based Curriculum. (A) Pegs and Holes assembly Insert policy. (B) Gears and Gearshafts ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Evaluation of PLAI in simulation. Results of Nominal are annotated when outside of plot bounds. Full-axis plot is in Figure S13. conditions in ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics.를 문제로 두고, Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as a list of all purchased parts.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. PROBLEM DESCRIPTION), p. 3 (III. PROBLEM DESCRIPTION), p. 3 (IV. POLICY LEARNING IN SIMULATION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
