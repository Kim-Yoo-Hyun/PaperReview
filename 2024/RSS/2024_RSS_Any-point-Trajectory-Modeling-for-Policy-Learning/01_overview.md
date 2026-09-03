# Any-point Trajectory Modeling for Policy Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p092.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p092.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, human video, video pretraining, trajectory prediction, Imitation Learning, language-conditioned
- Official paper: https://www.roboticsproceedings.org/rss20/p092.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p092.html
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, the lack of action labels makes utilization of video data in policy learning difficult.를 문제로 두고, We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, leveraging the structured representation of particle trajectories.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Learning from demonstration is a powerful method for teaching robots new skills, and having more demonstration data often improves policy learning.
- **p. 1 / Abstract - extractive body cue:** However, the high cost of collecting demonstration data is a significant bottleneck.
- **p. 1 / Abstract - extractive body cue:** Videos, as a rich data source, contain knowledge of behaviors, physics, and semantics, but extracting control-specific information from them is challenging due to the lack ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a novel framework, Any-point Trajectory Modeling (ATM), that utilizes video demonstrations by pre-training a trajectory model to predict future trajectories ...
- **p. 1 / Abstract - extractive body cue:** Once trained, these trajectories provide detailed control guidance, enabling the learning of robust visuomotor policies with minimal action-labeled data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, the lack of action labels makes utilization of video data in policy learning difficult.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, learning a video prediction model for control introduces two challenges.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we demonstrate that our method facilitates effective transfer learning from human videos and videos of a robot with a different morphology.
- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...
- **p. 4 / IV. METHOD - extractive body cue:** Guidance from the predicted track enables us to learn robust policies from only a few action-labeled demonstrations. most of the points that are sampled randomly ...
- **p. 3 / IV. METHOD - extractive body cue:** As illustrated in Figure 2, ATM is a two-stage framework: first learn to predict future point trajectories in a video frame as the pre-training with ...
- **p. 4 / IV. METHOD - extractive body cue:** Track-guided Policy Learning After training a track transformer to predict future tracks based on observations, we can then learn policies guided by these predicted trajectories. ...
- **p. 4 / IV. METHOD - extractive body cue:** Action-labeled Demos (b) Stage 2: Track-guided Policy Learning (a) Stage 1: Any-point Trajectory Modeling action Track-guided Policy 𝜋 Track Transformer Language Instruction Off-the-shelf Tracker Fig.
- **p. 5 / IV. METHOD - extractive body cue:** Note that, the weights of our policy model are randomly initialized rather than copied from the pretrained Track Transformer like other video-pretraining methods [33, 28], ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To begin with, we denote the action-free video dataset as To = {(τ (i) o , ℓ(i))}No i=1, where ℓ(i) is the language instruction for the ith episode and τ (i) o ... | observation history와 expert trajectory/action | p. 3 (III. PRELIMINARY), p. 4 (IV. METHOD) |
| State/latent | begin, denote, action-free, video, dataset, where, language, instruction, episode, denotes, observation-only, trajectory | behavior policy와 temporal action context | p. 3 (III. PRELIMINARY), p. 4 (IV. METHOD), p. 4 (IV. METHOD) |
| Output/action | ATM is permutation invariant to the input set of points, and we also find ATM to be robust to the distribution of the points, allowing us to use a different point sampling ... | predicted action 또는 action chunk | p. 4 (IV. METHOD), p. 4 (IV. METHOD), p. 3 (IV. METHOD) |
| Objective/outcome | Our track-guided policy is trained with MSE loss. | imitation error, task success, robustness와 compounding error | p. 5 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we demonstrate that our method facilitates effective transfer learning from human videos and videos of a robot with a different morphology.
- **p. 3 / IV. METHOD - extractive body cue:** To model the tracks, we propose a track transformer and illustrate the architecture in Figure 2 (a). a) Self-supervised Track Annotation.: Initially, we generate point ...
- **p. 4 / IV. METHOD - extractive body cue:** Guidance from the predicted track enables us to learn robust policies from only a few action-labeled demonstrations. most of the points that are sampled randomly ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: We implement ATM Diffusion Policy by adding the predicted future trajectories as additional conditioning and show consistent improvement over the base diffusion policies ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 10: We plot the success rates of the policies learned with predicted trajectories of different lengths. Generally, longer trajectory length improves the performance, but ...
- **p. 2 / 2) Through extensive experiments on simulated bench - extractive body cue:** marks and in the real world, we demonstrate that our method can effectively utilize video data in pre-training and significantly outperform various video pre-training baselines ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably to ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Embodiment/environment | All methods are trained on 10 action-labeled demonstration trajectories and 50 action-free video demonstration trajectories of the robot for each task, amounting to 500 videos for each 10-task suite. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Dataset/benchmark | All methods are trained on 10 action-labeled demonstration trajectories and 50 action-free video demonstration trajectories of the robot for each task, amounting to 500 videos for each 10-task suite. | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Metric | Fig. 9: Success rate of our policy trained with 4%, 10% and 20% action-labeled demos. Our policy trained with only 4% demos performs comparably to BC baseline with 20% demos on LIBERO-Spatial, ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Baseline/ablation | Fig. 4: We compare with state-of-the-art video pre-training methods on language-conditioned manipulation tasks in the LIBERO benchmark [27]. (a) Visualization of the LIBERO tasks separated into four suites, focusing on different aspects ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 2 (2) Through extensive experiments on simulated bench), p. 5 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 1) BC denotes the vanilla behavioral cloning which trains - extractive body cue:** Please see our video for failure cases of a video prediction model.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of our framework. (a) In the first stage, given an action-free video dataset, we first sample 2D points on one video frame ...
- **p. 8 / 160 Franka Videos - extractive body cue:** On the other hand, as the number of action-labeled trajectories is small, BC baselines that only use action-labeled trajectories fail.
- **p. 8 / 160 Franka Videos - extractive body cue:** Experiments show that training the trajectory model on additional cross-embodiment videos makes the trajectory prediction more robust and accurate, significantly improving policy learning.
- **p. 9 / 160 Franka Videos - extractive body cue:** The subgoal prediction is more robust as it is trained on a larger video dataset.
- **p. 9 / 160 Franka Videos - extractive body cue:** We hypothesize that the longer tracks might interfere with the learning of inverse dynamics due to noise.

## Why Read It

RL, IL, offline learning, and robot data의 il 문제를 이해하기 위해 읽는다. 본문은 However, the lack of action labels makes utilization of video data in policy learning difficult.를 문제로 두고, We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, leveraging the structured representation of particle trajectories.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, the lack of action labels makes utilization of video data in policy learning difficult. (p. 2, I. INTRODUCTION).
- **Actual contribution:** We summarize our main contributions below: 1) We propose an Any-point Trajectory Model, a simple and novel framework that bridges video pre-training to policy learning, leveraging the structured representation of ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Fig. 5: Real robot experiments on a dining table setup consisting of five tasks. The left figure shows our real-world setup and the tasks. The top right figure shows an ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** Another limitation of our method is that the video dataset we use in this paper only contains small domain gaps. (p. 10, VI. LIMITATIONS).
