# Problem - ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): Consequently, MLLMs lack prior knowledge in this field while successful training for these tasks necessitates extensive data to achieve desired generalization ability.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Robot manipulation relies on accurately predicting contact points and end-effector directions to ensure successful operation.
- **p. 1 / Abstract - extractive PDF cue:** However, learning-based robot manipulation, trained on a limited category within a simulator, often struggles to achieve generalizability, especially when confronted with extensive categories.
- **p. 1 / Abstract - extractive PDF cue:** Therefore, we introduce an innovative approach for robot manipulation that leverages the robust reasoning capabilities of Multimodal Large Language Models (MLLMs) to enhance the stability ...
- **p. 1 / Abstract - extractive PDF cue:** By fine-tuning the injected adapters, we preserve the inherent common sense and reasoning ability of the MLLMs while equipping them with the ability for manipulation.
- **p. 1 / Abstract - extractive PDF cue:** The fundamental insight lies in the introduced fine-tuning paradigm, encompassing object category understanding, affordance prior reasoning, and object-centric pose prediction to stimulate the reasoning ability ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Consequently, MLLMs lack prior knowledge in this field while successful training for these tasks necessitates extensive data to achieve desired generalization ability.
- **p. 1 / 1. Introduction - extractive PDF cue:** Additionally, ManipLLM predicts the gripper's up direction (xu, yu, zu) and forward direction (xf, yf, zf), forming the end-effector SO(3) rotation. demonstrate impressive performance, they ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Consequently, MLLMs lack prior knowledge in this field while successful training for these tasks necessitates extensive data to achieve desired generalization ability. | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | To deal with these difficulties, the proposed policy aims to adjust how we interact with things based on impedance force feedback, which ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | deal, difficulties, policy, aims, adjust, interact, things, impedance, force, feedback | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Given, text, prompt, RGB, image, depth, inputs, obtain | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: deal, difficulties, policy, aims, adjust, interact, things, impedance, force, feedback | p. 5 (3.2. Active Impedance Adaptation Policy), p. 5 (3.2. Active Impedance Adaptation Policy), p. 1 (1. Introduction) |
| Decision / output variable | action, pose, option or chunk a; body terms: Meanwhile, real-world, experiments, strong, generalization, ability, without, TTA | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | policy/action modeling objective; cue terms: supervised, under, cross-entropy, loss, enabling, model, aware, where | p. 4 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 6 (3.3. Sim-to-real Transfer) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.1. Fine-tuning Strategy), p. 3 (3.1. Fine-tuning Strategy), p. 6 (3.3. Sim-to-real Transfer) |
| Success / guarantee | instruction-conditioned task success | p. 6 (4.1. Training Details), p. 7 (4.2. Quantitative Comparison), p. 7 (4.3. Ablation and Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Additionally, ManipLLM predicts the gripper's up direction (xu, yu, zu) and forward direction (xf, yf, zf), forming the end-effector SO(3) rotation. demonstrate impressive performance, they ...
- **p. 2 / 1. Introduction - extractive PDF cue:** action trajectories (i.e. end-effector trajectories) [4, 40] poses challenges in generalization due to minimal low-level action samples in their pretraining data.
- **p. 1 / 1. Introduction - extractive PDF cue:** Existing advancements in Multimodal Large Language Models (MLLMs)[1, 19, 22, 38] highlight their proficiency in common sense reasoning and remarkable generalization in vision tasks [2, ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Meanwhile, in real-world experiments, our method shows strong generalization ability, with or without TTA strategy.

- **p. 2 / 1. Introduction - extractive PDF cue:** Experiments show that in the simulator, our method achieves a promising manipulation success rate across 30 categories.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Additionally, its head is relatively short, which presents a collision risk when interacting with the protruding handle. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 5 (3.2. Active Impedance Adaptation Policy), p. 5 (3.2. Active Impedance Adaptation Policy), p. 1 (1. Introduction), p. 4 (3.1. Fine-tuning Strategy). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 5 (3.2. Active Impedance Adaptation Policy), p. 5 (3.2. Active Impedance Adaptation Policy), p. 1 (1. Introduction), p. 4 (3.1. Fine-tuning Strategy), objective p. 4 (3.1. Fine-tuning Strategy), p. 4 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 5 (3.1. Fine-tuning Strategy), p. 6 (3.3. Sim-to-real Transfer).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
