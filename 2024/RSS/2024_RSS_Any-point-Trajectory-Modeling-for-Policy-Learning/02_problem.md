# Problem - Any-point Trajectory Modeling for Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p092.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p092.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, the lack of action labels makes utilization of video data in policy learning difficult.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Learning from demonstration is a powerful method for teaching robots new skills, and having more demonstration data often improves policy learning.
- **p. 1 / Abstract - extractive body cue:** However, the high cost of collecting demonstration data is a significant bottleneck.
- **p. 1 / Abstract - extractive body cue:** Videos, as a rich data source, contain knowledge of behaviors, physics, and semantics, but extracting control-specific information from them is challenging due to the lack ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a novel framework, Any-point Trajectory Modeling (ATM), that utilizes video demonstrations by pre-training a trajectory model to predict future trajectories ...
- **p. 1 / Abstract - extractive body cue:** Once trained, these trajectories provide detailed control guidance, enabling the learning of robust visuomotor policies with minimal action-labeled data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the lack of action labels makes utilization of video data in policy learning difficult.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, learning a video prediction model for control introduces two challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the lack of action labels makes utilization of video data in policy learning difficult. | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | To begin with, we denote the action-free video dataset as To = {(τ (i) o , ℓ(i))}No i=1, where ℓ(i) is the ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF body |
| State / latent | begin, denote, action-free, video, dataset, where, language, instruction, episode, denotes | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Action-labeled, Demos, Stage, Track-guided, Policy, Learning, Any-point, Trajectory | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: begin, denote, action-free, video, dataset, where, language, instruction, episode, denotes | p. 3 (III. PRELIMINARY), p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: summarize, main, contributions, below, Any-point, Trajectory, Model, simple | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHOD) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: track-guided, policy, trained, MSE, loss | p. 5 (IV. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (IV. METHOD) |
| Success / guarantee | closed-loop task success and robustness | p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, learning a video prediction model for control introduces two challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** For instance, collecting 130K trajectories in [6] took 17 months, making data collection a major bottleneck in robot learning.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. METHOD), p. 4 (IV. METHOD)): We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, leveraging the structured representation of ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we demonstrate that our method facilitates effective transfer learning from human videos and videos of a robot with a different morphology.
- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...
- **p. 4 / IV. METHOD - extractive body cue:** Guidance from the predicted track enables us to learn robust policies from only a few action-labeled demonstrations. most of the points that are sampled randomly ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Please see our video for failure cases of a video prediction model. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | On the other hand, as the number of action-labeled trajectories is small, BC baselines that only use action-labeled ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Experiments show that training the trajectory model on additional cross-embodiment videos makes the trajectory prediction more robust and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. PRELIMINARY), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. PRELIMINARY), p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD), objective p. 5 (IV. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, the lack of action labels makes utilization of video data in policy learning difficult. (p. 2, I. INTRODUCTION).
- **Formulation-changing contribution:** We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, leveraging the structured representation of ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** Another limitation of our method is that the video dataset we use in this paper only contains small domain gaps. (p. 10, VI. LIMITATIONS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
