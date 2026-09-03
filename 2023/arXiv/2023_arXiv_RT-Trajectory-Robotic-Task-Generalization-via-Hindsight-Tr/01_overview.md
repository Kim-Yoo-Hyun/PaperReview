# RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2311.01977.
> PDF retrieval source: https://arxiv.org/pdf/2311.01977. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, VLA, trajectory representation, spatial reasoning, task generalization
- Official paper: https://arxiv.org/abs/2311.01977
- Full-text retrieval: https://arxiv.org/pdf/2311.01977
- Code/Project: https://rt-trajectory.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, which makes it difficult to generalize to a new motion ...를 문제로 두고, The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Generalization remains one of the most important desiderata for robust robot learning systems.
- **p. 1 / ABSTRACT - extractive body cue:** While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging.
- **p. 1 / ABSTRACT - extractive body cue:** For example, a language-conditioned policy trained on pick-andplace tasks will not be able to generalize to a folding task, even if the arm trajectory of ...
- **p. 1 / ABSTRACT - extractive body cue:** Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches.
- **p. 1 / ABSTRACT - extractive body cue:** We propose a policy conditioning method using such rough trajectory sketches, which we call RTTrajectory, that is practical, easy to specify, and allows the policy ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, which makes it ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our experiments show that RT-Trajectory outperforms existing policy conditioning techniques, particularly in terms of generalization to novel motions, an open challenge in robotics.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose to use a coarse trajectory as a middle-ground solution between expressiveness and ease of use.
- **p. 3 / 3 METHOD - extractive body cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- **p. 4 / 3 METHOD - extractive body cue:** Trajectory Representations In this work, we propose two forms of trajectory representation from different combinations of the basic elements.
- **p. 4 / 3 METHOD - extractive body cue:** In the second representation, we introduce a more detailed trajectory representation RT-Trajectory (2.5D), which includes the height information in the 2D trajectory (Fig.
- **p. 3 / 3 METHOD - extractive body cue:** We then train a transformer-based control policy that is conditioned on the 2D trajectory sketches using imitation learning (Section 3.3).
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** For each scene, we use a held-out RT-Trajectory (2.5D) policy to explore different trajectory "prompts" given a budget of trials, and save the trajectory sketch ...
- **p. 5 / 3 METHOD - extractive body cue:** In our work, we use a PaLM-E style (Driess et al., 2023) model that generates vector-quantized tokens derived from ViT-VQGAN (Yu et al., 2022) that ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Human Demonstration Videos with Hand-object Interaction First-person human demonstration videos are an alternative input. | multi-view observation, language/task label과 action trajectory | p. 5 (3 METHOD), p. 5 (3 METHOD) |
| State/latent | Human, Demonstration, Videos, Hand-object, Interaction, First-person, alternative, input, Behavior, Cloning, Pomerleau, following | shared representation, embodiment/task identity와 data distribution | p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Output/action | Behavior Cloning (Pomerleau, 1988) following the RT-1 framework (Brohan et al., 2023b), by minimizing the log-likelihood of predicted actions at given the input image and trajectory sketch. | dataset sample 또는 learned policy action | p. 5 (3 METHOD), p. 4 (3 METHOD), p. 3 (3 METHOD) |
| Objective/outcome | Behavior Cloning (Pomerleau, 1988) following the RT-1 framework (Brohan et al., 2023b), by minimizing the log-likelihood of predicted actions at given the input image and trajectory sketch. | coverage, cross-embodiment transfer, data efficiency와 task success | p. 5 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose to use a coarse trajectory as a middle-ground solution between expressiveness and ease of use.
- **p. 3 / 3 METHOD - extractive body cue:** We introduce three basic elements for constructing the trajectory representation format: 2D Trajectories, Color Grading, and Interaction Markers.
- **p. 4 / 3 METHOD - extractive body cue:** Trajectory Representations In this work, we propose two forms of trajectory representation from different combinations of the basic elements.
- **p. 4 / 3 METHOD - extractive body cue:** In the second representation, we introduce a more detailed trajectory representation RT-Trajectory (2.5D), which includes the height information in the 2D trajectory (Fig.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Success rate of different trajectory generation approaches across tasks. Details about video collection and how trajectory sketches are derived from videos are described ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8: Example RT-Trajectory evaluations in realistic scenarios involving (a) novel articulated objects requiring new motions, (b) manipulation on new surfaces in new buildings in ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 14: Evaluation trajectories for new skills and their 10 closest trajectories from the training set. Each row shows three frames of a skill evaluation ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | Can RT-Trajectory generalize to tasks beyond those contained in the training dataset? | hardware/simulator version and reset protocol | p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Dataset/benchmark | Our real robot experiments aim to study the following questions: 1. | role, split, size and leakage | p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES), p. 5 (4 EXPERIMENTS), p. 15 (B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES) |
| Metric | Figure 5: Success rates for unseen tasks when conditioning with human drawn sketches. Scenarios contain a variety of difficult settings which require combining seen motions in novel ways or generalizing to new ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Baseline/ablation | Figure 11: First-interaction height alignment compares the relative difference between the z-height of the first gripper interactions of query trajectories to the first gripper interactions of the most similar training trajectories, as ... | fair input/data/compute/action matching | p. 10 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 22 / Figure/Table caption - extractive body cue:** Figure 19: Case studies in prompt engineering. Each row shows the trajectory sketch overlaid on the first frame and the corresponding rollout. As seen in ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** We find that changing trajectory sketches induces RT-Trajectory to change behavior modes in a reproducible manner, which suggests an intriguing opportunity: if a trajectory-conditioned robot ...
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** Though we demonstrate that our proposed approach achieves encouraging generalization capabilities for novel manipulation tasks, there are a few remaining limitations.
- **p. 9 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** 5 CONCLUSION AND LIMITATIONS In this work, we propose a novel policy-conditioning method for training robot manipulation policies capable of generalizing to tasks and motions ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 20: Example of retry behavior. The first image is the trajectory sketch generated from the CaP overlaid on the initial observation. The remaining images ...
- **p. 8 / 3. What emergent capabilities are enabled by RT-Trajectory? - extractive body cue:** With little to moderate trajectory prompt engineering, we find that RT-Trajectory is able to successfully perform a variety of tasks requiring novel motion generalization and ...
- **p. 15 / B.2 COLLECTING HUMAN-DRAWN TRAJECTORY SKETCHES - extractive body cue:** If all attempts fail, we just save the trajectory sketch from the last episode.

## Why Read It

VLA and generalist robot policies의 robot_data 문제를 이해하기 위해 읽는다. 본문은 Recently, language conditioning significantly improves generalization to new language commands (Brohan et al., 2023b), but it suffers from the lack of specificity, which makes it difficult to generalize to a new motion ...를 문제로 두고, The main contribution of this paper is a novel policy conditioning framework RT-Trajectory that fosters task generalization.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
