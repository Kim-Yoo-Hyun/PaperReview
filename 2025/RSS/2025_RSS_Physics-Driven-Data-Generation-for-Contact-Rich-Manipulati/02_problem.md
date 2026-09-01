# Problem - Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p053.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p053.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (4) We achieve high success rates in zero-shot hardware), p. 1 (1. IyTRODUCTION), p. 1 (1. IyTRODUCTION), p. 2 (B. Data Augmentation), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks)): data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse control (33). ‘These technologies offer a more intuitive ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...
- **p. 1 / Abstract - extractive body cue:** Starting with a small number of emb human demonstrations collected in a virtual reality simulation ‘environment, the pipeline refines these demonstrations using ‘oplimization-hased Kinematic retargeting ...
- **p. 1 / Abstract - extractive body cue:** This process yields a diverse, physically ‘consistent, contact-rich dataset that enables cross-embodiment data transfer, and offers the potential to reuse legacy datasets collected under different ...
- **p. 1 / Abstract - extractive body cue:** We validate the pipeline's effectiveness by training diffusion polices from the generated datasets for challenging Tong-horizon contact-rich manipulation tasks across. multiple robot embodiments, including a ...
- **p. 1 / Abstract - extractive body cue:** The trained policies are deployed zeroshot on hardware for bimanual liwa arms, achieving high success rates with minimal human input.
- **p. 2 / 4) We achieve high success rates in zero-shot hardware - extractive body cue:** data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse control (33). ‘These ...
- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, the significant embodiment gap and limited action labeling make this data difficult 10 transfer effectively to robot policies.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | data collection [31, 32], reducing cognitive load, physical strain, and user frustration compared to traditional techniques like kinesthetic teaching or 3D mouse ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | We train UNet-based diffusion policies [25] for all tasks, The action space is the robot configuration (joint angles, and additional floating base ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | train, UNet-based, diffusion, policies, tasks, action, space, robot, configuration, joint | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | cost, matrices, state, input, respectively, isthe, matrix, terminal | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: train, UNet-based, diffusion, policies, tasks, action, space, robot, configuration, joint | p. 14 (B. Policy Implementation Details), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: section, present, automatically, generating, large, quantities, physically, feasible | p. 4 (IV. AUTOMATED DATA GENERATION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 1 (Abstract) |
| Objective / loss / cost | task/contact/pose objective; cue terms: iiwa, Panda, arms, differ, contact, geometry, velocity, limits | p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 7 (B. Demonstration-Guided Trajectory Optimization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 4 (C. Trajectory Optimization for Contact-Rich Tasks), p. 4 (C. Trajectory Optimization for Contact-Rich Tasks) |
| Success / guarantee | completion, contact success and robustness | p. 7 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation), p. 8 (A. Policy Evaluation in Simulation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, the significant embodiment gap and limited action labeling make this data difficult 10 transfer effectively to robot policies.
- **p. 1 / 1. IyTRODUCTION - extractive body cue:** However, collecting real-world, contact-rich manipulation data through teleoperation is, challenging due to the need for precise multi-contact interactions, which are difficult to achieve in practice ...
- **p. 2 / B. Data Augmentation - extractive body cue:** To address these challenges, significant effort has been devoted to automating the data generation process through data augmentation techniques.
- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** To tackle these challenges, researchers have explored various trajectory optimization for- ‘ulations for multi-contact interactions.

## What the Paper Changes

PDF contribution framing (p. 4 (IV. AUTOMATED DATA GENERATION), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 1 (Abstract), p. 1 (Front matter), p. 2 (1. IyTRODUCTION)): In this section, we present our method for automatically generating large quantities of physically feasible trajectories for contact-rich manipulation tasks across a range of objects, initial conditions, and embodiments from ...

- **p. 3 / C. Trajectory Optimization for Contact-Rich Tasks - extractive body cue:** We present a Virtual Reality (VR)-based data collection pipeline designed for intuitive and efficient collection of hu- ‘man demonstrations across multiple robot embodiments. ‘The pipeline ...
- **p. 1 / Abstract - extractive body cue:** We present a low-cost data generation pipeline that integrates physics-based. simulation, human demonstrations, and model-based planning to efficiently generate large- ‘sale, high-quality datasets for contact-rich ...
- **p. 1 / Front matter - extractive body cue:** Leveraging trajectory optimization, our framework automatically generates thousands of ‘dynamically feasible contactrich trajectories across a range of embodiments and physical parameters from only 24 human ...
- **p. 2 / 1. IyTRODUCTION - extractive body cue:** 1) We present an intuitive, embodiment-flexible demonstration interface based on virtual reality and physics simulation, enabling fast data collection for dexterous contact-rich manipulation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Fig. 11: Policy failure and recovery on hardware. The baseline policy frequently (a) gets stuck on the box ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Simply transforming the end-effector pose in an object-centric manner as in MimicGen disregards the contact between the rest ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Fig. 8: Failure cases of baselines. (a) The baseline policy trained on the original 24 demonstrations forthe floating ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Common failure modes include the Allegro hand repeatedly missing contact with the cube or becoming stuck on its ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 14 (B. Policy Implementation Details), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (4) We achieve high success rates in zero-shot hardware), p. 1 (1. IyTRODUCTION), p. 1 (1. IyTRODUCTION), p. 2 (B. Data Augmentation), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), interface p. 14 (B. Policy Implementation Details), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization), objective p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 3 (C. Trajectory Optimization for Contact-Rich Tasks), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 5 (B. Demonstration-Guided Trajectory Optimization), p. 7 (B. Demonstration-Guided Trajectory Optimization), p. 7 (B. Demonstration-Guided Trajectory Optimization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
