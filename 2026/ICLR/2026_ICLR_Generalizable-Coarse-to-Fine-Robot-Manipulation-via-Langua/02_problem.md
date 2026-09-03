# Problem - Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WXFfMLyB6y; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/244660. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 BACKGROUND)): For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty levels.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Hierarchical coarse-to-fine policy, where a coarse branch predicts a region of interest to guide a fine-grained action predictor, has demonstrated significant potential in robotic 3D ...
- **p. 1 / ABSTRACT - extractive body cue:** However, even augmented with pre-trained models, these hierarchical policies still suffer from generalization issues.
- **p. 1 / ABSTRACT - extractive body cue:** To enhance generalization to novel instructions and environment variations, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a framework that integrates three key components: 1) task ...
- **p. 1 / ABSTRACT - extractive body cue:** Through comprehensive experiments in simulation and on a real robot, we demonstrate its superior generalization capability.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, on GemBench, a benchmark designed for evaluating generalization, our approach achieves a 12% higher average success rate than the SOTA method while using only ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, scaling these methods to a broader range of real-world applications (e.g., industrial, service, or home robotics) requires enhancing both (G1) their generalization to environment ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | The fine-grained action predictor takes as input both the step instruction and the multi-view RGB-D images and outputs an action. | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF body |
| State / latent | fine-grained, action, predictor, takes, input, step, instruction, multi-view, RGB-D, images | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | However, directly, training, model, simultaneously, generate, task, plan | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: fine-grained, action, predictor, takes, input, step, instruction, multi-view, RGB-D, images | p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: real-world, experiments, demonstrate, strong, generalization, ability, novel, tasks | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (4 METHOD) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Instead, inspired, Chain-of-Thought, reasoning, Zawalski, Zhao, robotics, design | p. 6 (4 METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4 METHOD), p. 7 (4 METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, scaling these methods to a broader range of real-world applications (e.g., industrial, service, or home robotics) requires enhancing both (G1) their generalization to environment ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Empirical evaluations in simulation and on a real robot demonstrate state-of-the-art performance in both robustness to visual and object changes and generalization to unseen tasks.
- **p. 4 / 3 BACKGROUND - extractive body cue:** As a result, it suffers from deficient generalization to visual changes, object variations, and novel tasks.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 6 (4 METHOD)): In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** To mitigate this, we introduce two ideas.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Furthermore, our design leads to substantial performance gain on the most challenging Level-4 tasks, where several baselines methods ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 4 (3 BACKGROUND). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 BACKGROUND), interface p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD), p. 4 (3 BACKGROUND), objective p. 6 (4 METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
