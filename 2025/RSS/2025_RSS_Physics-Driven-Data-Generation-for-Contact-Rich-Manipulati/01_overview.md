# Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p053.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p053.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, trajectory optimization, synthetic data
- Official paper: https://www.roboticsproceedings.org/rss21/p053.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p053.pdf
- Code/Project: https://www.roboticsproceedings.org/rss21/p053.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse control (33). ‘These technologies offer a more intuitive data collection ...를 문제로 두고, In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from only a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...
- **p. 1 / Abstract - extractive body cue:** Starting with a small number of emb human demonstrations collected in a virtual reality simulation ‘environment, the pipeline refines these demonstrations using ‘oplimization-hased Kinematic retargeting ...
- **p. 1 / Abstract - extractive body cue:** This process yields a diverse, physically ‘consistent, contact-rich dataset that enables cross-embodiment data transfer, and offers the potential to reuse legacy datasets collected under different ...
- **p. 1 / Abstract - extractive body cue:** We validate the pipeline's effectiveness by training diffusion polices from the generated datasets for challenging Tong-horizon contact-rich manipulation tasks across. multiple robot embodiments, including a ...
- **p. 1 / Abstract - extractive body cue:** The trained policies are deployed zeroshot on hardware for bimanual liwa arms, achieving high success rates with minimal human input.
- **p. 2 / 4) We achieve high success rates in zero-shot hardware - extractive body cue:** data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse control (33). ‘These ...
- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, the significant embodiment gap and limited action labeling make this data difficult 10 transfer effectively to robot policies.

## Core Idea

- **p. 4 / IV. AUTOMATED DATA GENERATION - extractive body cue:** In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** We present a Virtual Reality (VR)-based data collection pipeline designed for intuitive and efficient collection of hu- ‘man demonstrations across multiple robot embodiments. ‘The pipeline ...
- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...
- **p. 1 / Front matter - extractive body cue:** Leveraging trajectory optimization, our framework automatically generates thousands of ‘dynamically feasible contactrich trajectories across a range of embodiments and physical parameters from only 24 human ...
- **p. 2 / 1. IyTRODUCTION - extractive body cue:** 1) We present an intuitive, embodiment-flexible demonstration interface based on virtual reality and physics simulation, enabling fast data collection for dexterous contact-rich manipulation.
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** While these approaches search over the parameters of a neural network policy and potentially optimize 4 more global objective, we leverage trajectory optimization as a ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** To tackle these challenges, researchers have explored various trajectory optimization for- ‘ulations for multi-contact interactions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We train UNet-based diffusion policies [25] for all tasks, The action space is the robot configuration (joint angles, and additional floating base coordinates for the Allegro hand), while the observation space is ... | RGB-D/point cloud, object state와 contact/task observation | p. 14 (B. Policy Implementation Details), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks) |
| State/latent | train, UNet-based, diffusion, policies, tasks, action, space, robot, configuration, joint, angles, additional | object geometry, affordance, contact mode 또는 end-effector state | p. 14 (B. Policy Implementation Details), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization) |
| Output/action | [62] extend the path integral formulation to handle state-input constraints and validate the approach on quadruped stabilization on hardware. | grasp, pose, force 또는 end-effector trajectory | p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization) |
| Objective/outcome | ‘The iiwa and Panda arms differ in contact geometry, velocity limits, and joint constraints, all of which are explicitly modeled within the trajectory optimization framework described in 2), For safe hardware deployment, ... | task completion, contact success, pose/force error와 generalization | p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks) |

## Main Claims and Actual Contribution

- **p. 4 / IV. AUTOMATED DATA GENERATION - extractive body cue:** In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, ...
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** We present a Virtual Reality (VR)-based data collection pipeline designed for intuitive and efficient collection of hu- ‘man demonstrations across multiple robot embodiments. ‘The pipeline ...
- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...
- **p. 1 / Front matter - extractive body cue:** Leveraging trajectory optimization, our framework automatically generates thousands of ‘dynamically feasible contactrich trajectories across a range of embodiments and physical parameters from only 24 human ...
- **p. 2 / 1. IyTRODUCTION - extractive body cue:** 1) We present an intuitive, embodiment-flexible demonstration interface based on virtual reality and physics simulation, enabling fast data collection for dexterous contact-rich manipulation.
- **p. 8 / A. Policy Evaluation in Simulation - extractive body cue:** In contrast, policies trained on the expanded dataset generated by our pipeline demonstrate a higher likelihood of re-establishing contact with the object after initial misses, ...
- **p. 8 / A. Policy Evaluation in Simulation - extractive body cue:** 2) Bimanual Robot Arms: ‘The baseline policy trained on the original set of 24 human demonstrations achieves a success rate of 27/48 = 56% on ...
- **p. 7 / A. Policy Evaluation in Simulation - extractive body cue:** We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success rates in Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation) |
| Embodiment/environment | We illustrate our framework's capability to efficiently produce diverse, high-quality contactich datasets for training behavior cloning policies across multiple robotic platforms, including the floating Allegro hand and the bimanual Pan ... | hardware/simulator version and reset protocol | p. 7 (VI. BEHAVIOR CLONING EXPERIMENTS), p. 8 (A. Policy Evaluation in Simulation) |
| Dataset/benchmark | 9: Success rates of policy evaluation in simulation and hardware, | role, split, size and leakage | p. 7 (VI. BEHAVIOR CLONING EXPERIMENTS), p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation), p. 14 (B. Policy Implementation Details) |
| Metric | We evaluate the performance by conducting 48 policy rollouts for each embodiment in simulation and record the success rates in Fig. | definition, denominator, direction and uncertainty | p. 7 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation) |
| Baseline/ablation | The baseline behavior cloning policy trained on the original | fair input/data/compute/action matching | p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box surface when small deviations from the demonstration ...
- **p. 7 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** Simply transforming the end-effector pose in an object-centric manner as in MimicGen disregards the contact between the rest of the robot and the object, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Failure cases of baselines. (a) The baseline policy trained on the original 24 demonstrations forthe floating Allegro hand frequently
- **p. 8 / A. Policy Evaluation in Simulation - extractive body cue:** Common failure modes include the Allegro hand repeatedly missing contact with the cube or becoming stuck on its surface while attempting reorientation (visualized in Fig.
- **p. 5 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** While kinematic retargeting of demonstrations might suffice to generate data for simpler manipulation tasks such as pick and place, it often falls short for the ...
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** In addition, replaying the kinematically retargeted trajectory often fails when the object pose deviates slightly from the demonstration, driving the object out of reach (visualized ...
- **p. 6 / B. Demonstration-Guided Trajectory Optimization - extractive body cue:** Some trajectories still succeed under certain perturbations thanks to caging grasps or other strategies that ‘encourage robustness during the human demonstration.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse control (33). ‘These technologies offer a more intuitive data collection ...를 문제로 두고, In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from only a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (4) We achieve high success rates in zero-shot hardware), p. 1 (1. IyTRODUCTION), p. 1 (1. IyTRODUCTION), p. 2 (B. Data Augmentation), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
