# Method - Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p053.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p053.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 6 (B. Demonstration-Guided Trajectory Optimization), p. 6 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization)): While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a complementary tool to locally refine ...

## Method Body Digest

- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** To tackle these challenges, researchers have explored various trajectory optimization for- ‘ulations for multi-contact interactions.
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In contrast, trajectory optimization accounts for the system's true dynamics and can adjust the robot's actions accordingly.
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** The necessary frequent contact mode switches and high-dimensional action space pose great challenges for traditional model-based planners, while the precise contact interactions require fine-grained control ...
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In particular, human demonstrations provide global information about hen and where to make contact with the object, which modelbased planning can then locally refine.
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In general, model-based planners can struggle to discover high-quality longchorizon contactrich trajectories without demonstrations.
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** Contact-Implicit Trajectory Optimization Existing works based on contact-implicit trajectory optimization (CITO) [22, 21] have sought to formulate the combinatorial problem into 4 smooth optimization problem ...

## Design Rationale

- **p. 4 / IV. AUTOMATED DATA GENERATION - extractive body cue:** In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** We present a Virtual Reality (VR)-based data collection pipeline designed for intuitive and efficient collection of hu- ‘man demonstrations across multiple robot embodiments. ‘The pipeline ...
- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...

## Source Evidence Cues

- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** To tackle these challenges, researchers have explored various trajectory optimization for- ‘ulations for multi-contact interactions.
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In contrast, trajectory optimization accounts for the system's true dynamics and can adjust the robot's actions accordingly.
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** The necessary frequent contact mode switches and high-dimensional action space pose great challenges for traditional model-based planners, while the precise contact interactions require fine-grained control ...
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In particular, human demonstrations provide global information about hen and where to make contact with the object, which modelbased planning can then locally refine.
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In general, model-based planners can struggle to discover high-quality longchorizon contactrich trajectories without demonstrations.
- **Detected method headings:** A. Policy Evaluation in Simulation (p. 7); B. Policy Evaluation on Hardware (p. 9); B. Policy Implementation Details (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory ... | p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 7 (B. Demonstration-Guided Trajectory Optimization) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the ... | p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | To tackle these challenges, researchers have explored various trajectory optimization for- ‘ulations for multi-contact interactions. | p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 6 (B. Demonstration-Guided Trajectory Optimization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** Contact-Implicit Trajectory Optimization Existing works based on contact-implicit trajectory optimization (CITO) [22, 21] have sought to formulate the combinatorial problem into 4 smooth optimization problem ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a ...
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** CITO requires good initial guesses and can easily get stuck in local optima without making progress Human demonstrations offer valuable global guidance that helps overcome ...
- **p. 4 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** Our demonstration interface is fast and cost-effective.
- **p. 4 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** Since the system operates entirely in simulation, it removes. the dependency on robot hardware, significantly reducing the cost and complexity of data collection.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 7 (B. Demonstration-Guided Trajectory Optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | train, UNet-based, diffusion, policies, tasks, action, space, robot, configuration, joint, angles, additional, floating, base | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | train, UNet-based, diffusion, policies, tasks, action, space, robot, configuration, joint | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | section, present, automatically, generating, large, quantities, physically, feasible, trajectories, contact-rich | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | iiwa, Panda, arms, differ, contact, geometry, velocity, limits, joint, constraints | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 14 / B. Policy Implementation Details - extractive body cue:** We train UNet-based diffusion policies [25] for all tasks, The action space is the robot configuration (joint angles, and additional floating base coordinates for the ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** [62] extend the path integral formulation to handle state-input constraints and validate the approach on quadruped stabilization on hardware.
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** Qr, Re are the cost matrices for the state and input, respectively, and (Jr isthe cost matrix for the terminal state.
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** Here, u is the control input, f is obtained by time-stepping the dynamics engine, zrgin/Tmax (min/ ax) aFe the lower and upper bounds on the ...
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** The necessary frequent contact mode switches and high-dimensional action space pose great challenges for traditional model-based planners, while the precise contact interactions require fine-grained control ...
- **p. 1 / Abstract - extractive body cue:** The trained policies are deployed zeroshot on hardware for bimanual liwa arms, achieving high success rates with minimal human input.
- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, the significant embodiment gap and limited action labeling make this data difficult 10 transfer effectively to robot policies.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | We solve (1) using 4 Sequential Quadratic Programming (SQP)-style algorithm: during each iteration, the nonpenetration constraint (1b) is linearized and the matching ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | space of the Allegro hand and the Iong-horizon nature of the task, which requires a sequence of coordinated rolling, pitching, and yawing ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **p. 7 / VI. BEHAVIOR CLONING EXPERIMENTS - extractive body cue:** We illustrate our framework's capability to efficiently produce diverse, high-quality contactich datasets for training behavior cloning policies across multiple robotic platforms, including the floating Allegro ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** [62] extend the path integral formulation to handle state-input constraints and validate the approach on quadruped stabilization on hardware.
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, approaches, search, over, parameters, neural, network, policy, potentially, optimize, more, global, objective, leverage, trajectory, optimization, complementary, tool, locally, refine.
- **Relevant PDF headings:** A. Policy Evaluation in Simulation (p. 7); B. Policy Evaluation on Hardware (p. 9); B. Policy Implementation Details (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | We illustrate our framework's capability to efficiently produce diverse, high-quality contactich datasets for training behavior cloning policies across multiple robotic platforms, including ... | p. 7 (VI. BEHAVIOR CLONING EXPERIMENTS), p. 8 (A. Policy Evaluation in Simulation) |
| Grasp / trajectory generation | The baseline behavior cloning policy trained on the original | p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation) |
| Contact execution / correction | In contrast, policies trained on the expanded dataset generated by our pipeline demonstrate a higher likelihood of re-establishing contact with the object ... | p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation) |

## Failure and Ablation Link

- **p. 8 / A. Policy Evaluation in Simulation - extractive body cue:** These factors together present significant challenges for traditional model-based planners without guidance.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** Simply transforming the end-effector pose in an object-centric manner as in MimicGen disregards the contact between the rest of the robot and the object, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Failure cases of baselines. (a) The baseline policy trained on the original 24 demonstrations forthe floating Allegro hand frequently
- **p. 8 / A. Policy Evaluation in Simulation - extractive body cue:** Common failure modes include the Allegro hand repeatedly missing contact with the cube or becoming stuck on its surface while attempting reorientation (visualized in Fig.
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** While kinematic retargeting of demonstrations might suffice to generate data for simpler manipulation tasks such as pick and place, it often falls short for the ...
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In addition, replaying the kinematically retargeted trajectory often fails when the object pose deviates slightly from the demonstration, driving the object out of reach (visualized ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 6 (B. Demonstration-Guided Trajectory Optimization), p. 6 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization), objective p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 4 (C. Trajectory Optimization for Contact-Rich Tasks), p. 4 (C. Trajectory Optimization for Contact-Rich Tasks), temporal p. 4 (A. Kinematic Motion Retargeting), p. 8 (A. Policy Evaluation in Simulation), p. 4 (A. Kinematic Motion Retargeting), p. 7 (A. Policy Evaluation in Simulation), p. 7 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
