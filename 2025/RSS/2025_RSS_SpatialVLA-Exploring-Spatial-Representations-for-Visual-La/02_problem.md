# Problem - SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p011.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p011.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to ‘explore effective spatial representations for the robot ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce Fgo3D Position Encoding 10 inject 3D information into the input observations of the visuallanguage-action model, and propose Adaptive Action Grids to represent ...
- **p. 1 / Abstract - extractive body cue:** SpatialVLA is, first prestrained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot ...
- **p. 1 / Abstract - extractive body cue:** After pre-training, SpatialVLA is directly applied to perform ‘numerous tasks in a zero-shot manner.
- **p. 1 / Abstract - extractive body cue:** The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong indomain multitask generalization ability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Secondly, different robots have different action movement characteristics to accomplish diverse tasks, due to different degrees of freedom, motion controllers, workspace configurations, and task complexity, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, developing such generalist robot policies with 3D spatial intelligence encounters two primary challenges in the aspects of robot observation and action. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | We find that the proposed model Spatial VLA bridges observation inputs and aetion outputs in a universal robot-agnostic manner, which explores powerful ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | find, model, Spatial, VLA, bridges, observation, inputs, aetion, outputs, universal | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | During, training, SpatialVLA, model, trained, take, ego3D, position | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: find, model, Spatial, VLA, bridges, observation, inputs, aetion, outputs, universal | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (A. The SpatialVLA Model Architecture) |
| Decision / output variable | action, pose, option or chunk a; body terms: summary, contributions, consist, novel, generalist, robot, policy, explores | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (B. The Pre-training and Post-training Scheme) |
| Objective / loss / cost | policy/action modeling objective; cue terms: detail, Gaussian, distribution, Yacw, action, variable, posttraining, datasets | p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture), p. 4 (A. The SpatialVLA Model Architecture) |
| Success / guarantee | instruction-conditioned task success | p. 8 (B. Adapting to New Robot Setups), p. 9 (B. Adapting to New Robot Setups), p. 7 (10 Ablations on Design) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** Secondly, different robots have different action movement characteristics to accomplish diverse tasks, due to different degrees of freedom, motion controllers, workspace configurations, and task complexity, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The key to the success of this paradigm lies in adapting the generalization power of VLMs to numerous robot manipulation tasks, as well

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture)): In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on Ego3D Posi tion Encoding and ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** OpenVLA [30] adopts a similar action discretization approach and fine-tune Prismatic VLM [28] only on the OXE dataset [13], which consists of robot data from ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** space consists Of Myax = Mg *Mo ~M,. diserete spatial stids Ons = {2,...a%}, Similarly, there are Myr = Meat » Myick *Myaw 3D discrete ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, SpatialVLA is developed based on a vision-language model to inherit the general world knowledge.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | However, in moderately complex tasks (#3-7), ‘most policies, such as RT-1-X, Octo, and RoboVLM struggle with manipulation, frequently ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Compared to OpenVLA, ‘our method demonstrates superior robustness in handling motion disturbances (human-induced dynamic object movement in tasks ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | To assess the robustness of Spatial VLA in diverse environmental variations, we employ the SimplerEnv simulation benchmark [35] ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Qualitatively, we find that SpatialVLA exhibits greater generalizability and robustness across diverse robotic manipulation tasks and environmental | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture), objective p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
