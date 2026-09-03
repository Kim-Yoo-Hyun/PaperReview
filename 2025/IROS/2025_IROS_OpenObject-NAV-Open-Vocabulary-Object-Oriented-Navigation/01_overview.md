# OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.18743.
> PDF retrieval source: https://arxiv.org/pdf/2409.18743. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Navigation, Graph Reasoning, semantic
- Official paper: https://arxiv.org/abs/2409.18743
- Full-text retrieval: https://arxiv.org/pdf/2409.18743
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, they struggle to represent everyday dynamic environments due to two key challenges.를 문제로 두고, In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried relationships between objects. • We design a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In everyday life, frequently used objects like cups often have unfixed positions and multiple instances within the same category, and their carriers frequently change as ...
- **p. 1 / Abstract - extractive body cue:** As a result, it becomes challenging for a robot to efficiently navigate to a specific instance.
- **p. 1 / Abstract - extractive body cue:** To tackle this challenge, the robot must capture and update scene changes and plans continuously.
- **p. 1 / Abstract - extractive body cue:** However, current object navigation approaches primarily focus on semantic-level and lack the ability to dynamically update scene representation.
- **p. 1 / Abstract - extractive body cue:** This paper captures the relationships between frequently used objects and their static carriers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they struggle to represent everyday dynamic environments due to two key challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they are often limited to searching for semantic-level objects and lack the capability to update scenes.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried ...
- **p. 3 / III. METHOD - extractive body cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This update enables efficient point-to-point navigation for the third task. dynamic and subject to interference, making it challenging to efficiently and effectively navigate to them.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Based on the CRSG, we designed an object-oriented navigation strategy, modeling the object search process as a Markov Decision Process (MDP) [21].
- **p. 3 / III. METHOD - extractive body cue:** The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) ...
- **p. 4 / III. METHOD - extractive body cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 2 / III. METHOD - extractive body cue:** Unlike ConceptGraph [19], each instance object Oi ∈O (O is the set of all objects) not only contains a CLIP feature V Fi but also ...
- **p. 4 / III. METHOD - extractive body cue:** The RGB images are processed through CropFormer [38], Tokenize Anything model [35], CLIP [22] and SBERT [36] to obtain instance masks, captions, encoded CLIP features ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) (8) policy π(·): Given current state St ... | camera/depth stream, pose, map와 language goal | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | robot, selects, next, action, current, state, according, specific, policy, Given, CRt, CTt | robot pose, free-space/semantic map와 local goal | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | We model the exploration of a displaced object as a fixedpolicy Markov decision process (MDP) below. state space S: In the current step t, we define: 1. the robot's pose Lt ∈L, ... | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Objective/outcome | The cost function is defined as follows: P L = T X t=1 Length(Lt, Lt+1) (1) Let Lt represent the position of the exploration target at step t, and Length(Lt, Lt+1) denote ... | goal reach, safety, localization error와 replanning latency | p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried ...
- **p. 3 / III. METHOD - extractive body cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This update enables efficient point-to-point navigation for the third task. dynamic and subject to interference, making it challenging to efficiently and effectively navigate to them.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Based on the CRSG, we designed an object-oriented navigation strategy, modeling the object search process as a Markov Decision Process (MDP) [21].
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** 4 illustrates an example of long-sequence navigation, where the efficiency of navigating to the target significantly improves as the number of navigated objects increases.
- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39].
- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** I, where our object query success rate averages 86% and is the highest in all three scenarios.
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** Tasks SR(i) represents the success rate of correctly navigating to all i objects.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Embodiment/environment | Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX 3080. | hardware/simulator version and reset protocol | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD) |
| Dataset/benchmark | Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object where the target object is most likely ... | role, split, size and leakage | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Metric | We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39]. | definition, denominator, direction and uncertainty | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Baseline/ablation | The resulting feature is then compared with the SBERT or CLIP features of each object in the CRSG S G using cosine similarity, similar to Eq. | fair input/data/compute/action matching | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** If the robot fails to reach the target, the SPL score is zero.
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: Failed ---Find chairs Task 1: black bottle ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, they struggle to represent everyday dynamic environments due to two key challenges.를 문제로 두고, In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried relationships between objects. • We design a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
