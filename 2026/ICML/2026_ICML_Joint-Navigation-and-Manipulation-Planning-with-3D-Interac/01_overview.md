# Joint Navigation and Manipulation Planning with 3D Interaction Chains

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=oVB2xYWvpv.
> PDF retrieval source: https://openreview.net/pdf/fa35fc3f33ae33100b9b86126d95a99def1057d8.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, 3D Vision, Navigation
- Official paper: https://openreview.net/forum?id=oVB2xYWvpv
- Full-text retrieval: https://openreview.net/pdf/fa35fc3f33ae33100b9b86126d95a99def1057d8.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, such independently designed policies and limited heuristics struggle to generalize across diverse situations.를 문제로 두고, In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary mobile manipulation (OVMM) requires long-horizon navigation in unseen environments and object-centric manipulation.
- **p. 1 / Abstract - extractive body cue:** Most existing methods treat navigation and manipulation as separate stages, which can yield navigation endpoints that are poor for manipulation or manipulation-friendly poses that are ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose 3D Interaction Chains (3D-IC), a unified framework that couples multi-stage navigation and manipulation planning.
- **p. 1 / Abstract - extractive body cue:** 3D-IC maintains a shared 3D feature map for both skills, generates stage-aligned interaction waypoints, and links them into candidate multi-stage chains.
- **p. 1 / Abstract - extractive body cue:** A hierarchical policy then scores these chains by jointly considering feasibility (via VLM reasoning over waypointcentric 3D features) and transition cost, selecting the best trade-off ...
- **p. 2 / 1. Introduction - extractive body cue:** However, such independently designed policies and limited heuristics struggle to generalize across diverse situations.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, a 3D feature map (Wang et al., 2025b; Wang & Lee, 2025) is constructed to fuse map-level context with egocentric visual ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.
- **p. 2 / 1. Introduction - extractive body cue:** Our 3D-IC includes: (1) a 3D feature map that captures information needed for both navigation and manipulation, (2) an interaction chain that enables unified planning ...
- **p. 5 / 4.2. 3D-IC Construction - extractive body cue:** Following frontier-based exploration (FBE) (Yamauchi, 1997), repeatedly navigating to frontier locations enables the robot to progressively reveal unknown areas and discover targets.
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive body cue:** Formally, given RGB-D observations It, the robot first builds a 3D feature map Mt.
- **p. 3 / 4.1. Unified Modeling of Multi-stage Interaction - extractive body cue:** On the action side, the policy is decomposed into: (1) a high-level policy operating on Mt that outputs a sequence of interaction waypoints and action ...
- **p. 4 / 4.1. Unified Modeling of Multi-stage Interaction - extractive body cue:** In the chain decision stage, joint planning is employed to ultimately select the interaction waypoints for execution, which are then dispatched to the local policy ...
- **p. 5 / 4.2. 3D-IC Construction - extractive body cue:** To obtain an interaction chain ct = {(wk, uk)}K k=1, candidate interaction waypoints wk and their associated action tokens uk are first generated from the ...
- **p. 6 / 4.3. Joint Planning with 3D-IC - extractive body cue:** Then we execute actions on sampled waypoints to gather simulator feedback and post-execution RGB images.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The navigation policy πn takes mt as input and outputs base actions an t ∈{Forward, Left, Right}, whereas the manipulation policy πm takes the single-step observation It as input and outputs continuous ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 3 (3. Preliminaries of Mobile Manipulation), p. 2 (1. Introduction) |
| State/latent | navigation, policy, takes, input, outputs, base, actions, Forward, Left, Right, whereas, manipulation | map/object/contact state와 base-arm coordination decision | p. 3 (3. Preliminaries of Mobile Manipulation), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | Our goal is joint planning for OVMM, while navigation and manipulation differ substantially in both inputs and outputs: navigation typically conditions on the accumulated history of observations (e.g., a semantic map) and ... | base motion plus arm/gripper action | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction) |
| Objective/outcome | The policy is optimized using a standard autoregressive cross-entropy loss: L(θ) = -PT t=1 log pθ (xt / xprompt, x<t), where the loss is computed only on the answer tokens xt, while ... | long-horizon task success, reachability, collision과 recovery | p. 6 (4.3. Joint Planning with 3D-IC), p. 5 (4.3. Joint Planning with 3D-IC), p. 5 (4.3. Joint Planning with 3D-IC) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.
- **p. 2 / 1. Introduction - extractive body cue:** Our 3D-IC includes: (1) a 3D feature map that captures information needed for both navigation and manipulation, (2) an interaction chain that enables unified planning ...
- **p. 5 / 4.2. 3D-IC Construction - extractive body cue:** Following frontier-based exploration (FBE) (Yamauchi, 1997), repeatedly navigating to frontier locations enables the robot to progressively reveal unknown areas and discover targets.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Experimental results validate improvements in both success rate and efficiency (SPL).
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5. Comparisons with the related works. We report Success Rate (SR) and Success weighted by Path Length (SPL) across all four stages. Note that ...
- **p. 9 / 5.4. Comparison with SOTA Methods - extractive body cue:** Notably, while our method is built upon the OVMM (Heuristic) baseline, which originally exhibited significantly lower Overall Success Rate (SR) compared to the OVMM (RL) ...
- **p. 8 / 5.3. Real-world Evaluation - extractive body cue:** Experimental results demonstrate that our method yields significant performance improvements, particularly in long-horizon cross-room tasks and during the Place stage.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Our approach, which utilizes a 3D feature map to construct interaction point representations, achieves the highest performance (Row 4).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.2. Evaluation Results), p. 9 (Figure/Table caption) |
| Embodiment/environment | In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes. | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Dataset/benchmark | Real-world Experiment. "Intra" denotes intra-room tasks where the object and goal receptacle are co-located in the same room. "Cross" refers to cross-room tasks where they are positioned in different rooms, requiring long-horizon ... | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 8 (5.2. Evaluation Results), p. 8 (5.3. Real-world Evaluation) |
| Metric | Experimental results validate improvements in both success rate and efficiency (SPL). | definition, denominator, direction and uncertainty | p. 7 (5.2. Evaluation Results), p. 9 (5.3. Real-world Evaluation), p. 6 (5.1. Experimental Setup) |
| Baseline/ablation | Our method consistently outperforms prior works, establishing new state-of-the-art performance across all metrics. | fair input/data/compute/action matching | p. 9 (5.3. Real-world Evaluation), p. 8 (5.2. Evaluation Results), p. 9 (5.4. Comparison with SOTA Methods) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.2. Evaluation Results - extractive body cue:** Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to table baseline baseline 3D-IC 3D-IC High Navigation ...
- **p. 8 / 5.3. Real-world Evaluation - extractive body cue:** Consequently, the agent navigated back to a nightstand in the initial room to complete the placement, thereby avoiding a potential failure.
- **p. 9 / 5.4. Comparison with SOTA Methods - extractive body cue:** The consistently high SPL scores indicate that our method achieves efficient trajectory, rather than merely reducing step counts through premature termination or failure cases (i.e., ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 5. Failure cases of 3D-IC on OVMM Dataset. The failure cases are categorized according to the four standard stages of the Open Vocabulary Mobile ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** These examples highlight the advantages of 3D-IC over the baseline, specifically in considering optimal docking orientation, avoiding obstacle occlusion during placement, and generating more efficient ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** In the OVMM benchmark, the "steps" metric calculates the average number of steps across all episodes where the agent actively terminates, including failed episodes.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To provide a more robust assessment of execution efficiency, we employ the standard Success weighted by normalized inverse Path Length (SPL) (Anderson et al., 2018) ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 However, such independently designed policies and limited heuristics struggle to generalize across diverse situations.를 문제로 두고, In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminaries of Mobile Manipulation), p. 3 (4.1. Unified Modeling of Multi-stage Interaction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
