# Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2403.08605.
> PDF retrieval source: https://arxiv.org/pdf/2403.08605. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, Graph Reasoning
- Official paper: https://arxiv.org/abs/2403.08605
- Full-text retrieval: https://arxiv.org/pdf/2403.08605
- Code/Project: https://moma-llm.cs.uni-freiburg.de/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 To address these challenges, we propose grounding LLMs in dynamically built scene graphs.를 문제로 두고, Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** To fully leverage the capabilities of mobile manipulation robots, it is imperative that they are able to autonomously execute long-horizon tasks in large unexplored environments.
- **p. 1 / Abstract - extractive body cue:** While large language models (LLMs) have shown emergent reasoning skills on arbitrary tasks, existing work primarily concentrates on explored environments, typically focusing on either navigation ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 1 / Abstract - extractive body cue:** We tightly interleave these representations with an object-centric action space.
- **p. 1 / Abstract - extractive body cue:** Given object detections, the resulting approach is zero-shot, open-vocabulary, and readily extendable to a spectrum of mobile manipulation and household robotic tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Furthermore, the presence of interactive scenes and articulated objects introduces a multitude of potential states and failure cases.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the path on the Voronoi graph GV, and the Euclidean distances d from the Voronoi nodes no and nvp to the object ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from openvocabulary scene graphs, dynamically updated as the ...
- **p. 1 / 2 Toyota Motor Europe (TME) - extractive body cue:** These diverse representations are then tightly interweaved with an object-centric action space.
- **p. 5 / IV. MOMA-LLM - extractive body cue:** If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We rely on a simple success state to the action history, stating "success", "failure", or "invalid argument" in case the output of the LLM could not be matched to the scene graph. | egocentric RGB-D, language/task goal, base-arm proprioception | p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM) |
| State/latent | rely, simple, success, state, action, history, stating, failure, invalid, argument, case, output | map/object/contact state와 base-arm coordination decision | p. 5 (IV. MOMA-LLM), p. 5 (IV. MOMA-LLM), p. 3 (IV. MOMA-LLM) |
| Output/action | If a subpolicy attempted execution but failed to complete its task, we re-encode the latest scene, update the action history, and let the LLM make a normal next decision with the updated ... | base motion plus arm/gripper action | p. 5 (IV. MOMA-LLM), p. 3 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM) |
| Objective/outcome | Objects are then assigned to the room label R of the node no that minimizes Eq. | long-horizon task success, reachability, collision과 recovery | p. 4 (IV. MOMA-LLM), p. 4 (IV. MOMA-LLM), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose grounding LLMs in dynamically built scene graphs.
- **p. 3 / IV. MOMA-LLM - extractive body cue:** To address the challenges of interactive open-vocabulary household tasks, we propose MoMa-LLM, which intertwines high-level reasoning with scalable dynamic scene representations.
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the path on the Voronoi graph GV, and the Euclidean distances d from the Voronoi nodes no and nvp to the object ...
- **p. 4 / IV. MOMA-LLM - extractive body cue:** It consists of the following high-level actions: navigate(room_name, object_name): Navigation to an object in a room via an A∗planner in the explored BEV-map Bt, inflated ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Similarly, while HIMOS achieves a high success rate, it is unable to explore efficiently.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This results in an efficiency curve, in which the best policies are located in the top left corner, enabling the comparison of success rates for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Embodiment/environment | Simulation Experiments We instantiate the task in the iGibson simulator [32] with a Fetch robot. | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Dataset/benchmark | Evaluated across 10 episodes and all test scenes with 2D grid resolution of 0.05 m to account for thin walls. | role, split, size and leakage | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |
| Metric | In contrast, MoMa-LLM achieves similar success rates as HIMOS with a much higher search efficiency, both in terms of SPL and AUC-E. | definition, denominator, direction and uncertainty | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Baseline/ablation | Unstructured LLM: This baseline provides the scene graph in a JSON format without any additional structure to the language model. | fair input/data/compute/action matching | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Furthermore, the agent was able to react to the (unseen) subpolicy failures, such as re-trying to open a drawer when the gripper slipped off the ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** The two failures stemmed from irrecoverable failures of the subpolicies, in particular, collisions of the base during navigation or of the arm while opening the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Object interactions, distance travelled and infeasible actions averaged over all episodes, including early terminated failures.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This metric does not take into account the costs of object interactions.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. We construct a real-world apartment covering four rooms and 54 objects and transfer the model to a Toyota HSR robot. these objects would ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 To address these challenges, we propose grounding LLMs in dynamically built scene graphs.를 문제로 두고, Our approach incorporates a scene understanding module that, given object detections, constructs open-vocabulary scene ∗Equal contribution.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 4 (IV. MOMA-LLM), p. 1 (2 Toyota Motor Europe (TME)), p. 3 (IV. MOMA-LLM) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
