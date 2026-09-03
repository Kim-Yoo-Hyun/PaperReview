# Method - IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.17110; PDF retrieval source: https://arxiv.org/pdf/2305.17110. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 6 (V. POLICY DEPLOYMENT IN REAL WORLD)): We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and parameterized by a network with ...

## Method Body Digest

- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and ...
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Joint Evaluation As described in Sections IV-E-IV-G, we proposed three algorithms for improving learning of contact-rich Insert policies: Simulation-Aware Policy Update to adapt to simulator ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Thus, we propose our first algorithm, a simulation-aware policy update (SAPU), where the agent is encouraged to learn policies that avoid interpenetrations.
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Inspired by classical PID control, which can minimize steady-state error and reject disturbances on linear systems, we propose a Policy-Level Action Integrator (PLAI), which integrates ...
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Policy-Level Action Integrator Method: Robotics simulations can exhibit marked discrepancies with the real world due to incomplete models, inaccurate parameters, and numerical artifacts [14]; although ...
- **p. 6 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** We then describe and evaluate our deployment-time algorithm, the Policy-Level Action Integrator (PLAI), in Section V-D.
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used TSI rather than operational-space control (OSC) because Franka provides a high-performance implementation of TSI, and OSC relies on an accurate dynamics model.
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** The objective was to learn a policy π : O →P(A) that maximized the expected sum of discounted rewards Eπ[ΣT -1 t=0 γtr(st)].

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** IndustRealKit allows the research community to easily replicate our experimental hardware and benchmark their performance. • Software: We present IndustRealLib, a lightweight Python library that ...

## Source Evidence Cues

- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and ...
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Joint Evaluation As described in Sections IV-E-IV-G, we proposed three algorithms for improving learning of contact-rich Insert policies: Simulation-Aware Policy Update to adapt to simulator ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Thus, we propose our first algorithm, a simulation-aware policy update (SAPU), where the agent is encouraged to learn policies that avoid interpenetrations.
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Inspired by classical PID control, which can minimize steady-state error and reject disturbances on linear systems, we propose a Policy-Level Action Integrator (PLAI), which integrates ...
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Policy-Level Action Integrator Method: Robotics simulations can exhibit marked discrepancies with the real world due to incomplete models, inaccurate parameters, and numerical artifacts [14]; although ...
- **p. 6 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** We then describe and evaluate our deployment-time algorithm, the Policy-Level Action Integrator (PLAI), in Section V-D.
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used TSI rather than operational-space control (OSC) because Franka provides a high-performance implementation of TSI, and OSC relies on an accurate dynamics model.
- **Detected method headings:** IV. POLICY LEARNING IN SIMULATION (p. 3); V. POLICY DEPLOYMENT IN REAL WORLD (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions ... | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | Joint Evaluation As described in Sections IV-E-IV-G, we proposed three algorithms for improving learning of contact-rich Insert policies: Simulation-Aware Policy Update to ... | p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | Thus, we propose our first algorithm, a simulation-aware policy update (SAPU), where the agent is encouraged to learn policies that avoid interpenetrations. | p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** The objective was to learn a policy π : O →P(A) that maximized the expected sum of discounted rewards Eπ[ΣT -1 t=0 γtr(st)].
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Unfortunately, in simulation for RL, an agent can exploit inaccurate collision dynamics to maximize reward, learning policies that are unlikely to transfer to the real ...
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** However, all rewards could be expressed in the following general form: G = wh0..whm  H-1 X t=0 [wd0Rd0(t) + ... + wdnRdn(t)] + ws0Rs0 ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** This procedure is performed each episode, and the depth is used to weight the cumulative reward during the policy update.
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Joint Evaluation As described in Sections IV-E-IV-G, we proposed three algorithms for improving learning of contact-rich Insert policies: Simulation-Aware Policy Update to adapt to simulator ...
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Thus, SDF Query Distance was by far the most effective reward formulation for policy learning.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | proximal, policy, optimization, PPO, learn, stochastic, actor, mapping, observations, actions, parameterized, network, weights, well | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | proximal, policy, optimization, PPO, learn, stochastic, actor, mapping, observations, actions | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | secondary, contributions, following, Hardware, present, IndustRealKit, contains, CAD, models, parts | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | objective, learn, policy, maximized, expected, discounted, rewards, Unfortunately, simulation, agent | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and ...
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** An established approach for applying policy actions is sd t+1 = st ⊕at = st ⊕Π(ot), (2) where sd t+1 is the desired state, at ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** For sim-to-real transfer, we also propose a policy-level action integrator (PLAI), which reduces steady-state error in ...
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Inspired by classical PID control, which can minimize steady-state error and reject disturbances on linear systems, we propose a Policy-Level Action Integrator (PLAI), which integrates ...
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Formulation We formulated the problem as a Markov decision process (MDP) with state space S, observation space O, action space A, state transition dynamics T ...
- **p. 5 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** When training and testing with moderate state randomization (plug/hole randomization of ±10 mm/±10 cm, respectively) and observation noise (±1 mm), the Pegs and Holes assembly ...
- **p. 6 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** In summary, we developed the IndustRealLib library, which accepts trained policy checkpoints from Isaac Gym as input, and outputs targets for a Franka robot controlled ...
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | We thus set our physics frequency during training to the highest practical rate (120 Hz) given our compute, and restricted our control ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | This procedure is performed at each timestep in each environment and is used to generate a reward signal. | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | We thus set our physics frequency during training to the highest practical rate (120 Hz) given our compute, and restricted our control ... | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Policy-Level Action Integrator Method: Robotics simulations can exhibit marked discrepancies with the real world due to incomplete models, inaccurate parameters, and numerical artifacts [14]; although ...
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** After training policies with each strategy, we tested each policy in simulation over 5 seeds, with 1000 trials per seed; quantified dmax ip for each ...
- **p. 7 / V. POLICY DEPLOYMENT IN REAL WORLD - extractive body cue:** Policy-Level Action Integrator Method: Robotics simulations can exhibit marked discrepancies with the real world due to incomplete models, inaccurate parameters, and numerical artifacts [14]; although ...
- **p. 3 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** Training Environments We developed our code within the Factory simulation framework [48].

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** proximal, policy, optimization, PPO, learn, stochastic, actor, mapping, observations, actions, parameterized, network, weights, well, approximation, on-policy, value, function, critic, states.
- **Relevant PDF headings:** IV. POLICY LEARNING IN SIMULATION (p. 3); V. POLICY DEPLOYMENT IN REAL WORLD (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | The goal was for the robot to detect all the pegs and use the simulation-trained Pick policy to pick up the objects ... | p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 7 (VI. REAL-WORLD EXPERIMENTS) |
| Grasp / trajectory generation | Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the ... | p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS) |
| Contact execution / correction | Fig. 3: Evaluation of Simulation-Aware Policy Update. Success rates are computed for episodes where the maximum interpenetration distance was less than the ... | p. 4 (Figure/Table caption), p. 8 (VI. REAL-WORLD EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** To our knowledge, IndustReal is the first system to demonstrate RL-based sim-to-real transfer for the end-to-end assembly task (i.e., detection, grasping, part transport, and insertion) ...
- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Second, our primary failure cases on the real system were due to slip of the object in the gripper and wedging of plugs in their ...
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this ...
- **p. 9 / VIII. LIMITATIONS & FUTURE WORK - extractive body cue:** Our work has limitations, which lend themselves naturally to future research directions.
- **p. 8 / VI. REAL-WORLD EXPERIMENTS - extractive body cue:** Failure cases were one missed detection of a peg, as well as one grasp of both a peg and its corresponding peg tray.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Overview. Top: Simulation-based policy learning for one of our tasks, gear assembly. Middle: Proposed algorithms to facilitate sim-based learning and real-world deployment. Bottom: ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Joint evaluation of Simulation-Based Policy Update, SDF-Based Dense Reward, and Sampling-Based Curriculum. (A) Pegs and Holes assembly Insert policy. (B) Gears and Gearshafts ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 6 (V. POLICY DEPLOYMENT IN REAL WORLD), objective p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION), temporal p. 6 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 6 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions a ∈A and parameterized by a network with ... (p. 3, IV. POLICY LEARNING IN SIMULATION).
- **Objective/update evidence:** The objective was to learn a policy π : O →P(A) that maximized the expected sum of discounted rewards Eπ[ΣT -1 t=0 γtr(st)]. (p. 3, IV. POLICY LEARNING IN SIMULATION).
- **Temporal/runtime evidence:** We thus set our physics frequency during training to the highest practical rate (120 Hz) given our compute, and restricted our control rate during training to 60 Hz to prevent ... (p. 6, V. POLICY DEPLOYMENT IN REAL WORLD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
