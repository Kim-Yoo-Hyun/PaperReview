# Problem - Joint Navigation and Manipulation Planning with 3D Interaction Chains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oVB2xYWvpv; PDF retrieval source: https://openreview.net/pdf/fa35fc3f33ae33100b9b86126d95a99def1057d8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminaries of Mobile Manipulation)): However, such independently designed policies and limited heuristics struggle to generalize across diverse situations.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary mobile manipulation (OVMM) requires long-horizon navigation in unseen environments and object-centric manipulation.
- **p. 1 / Abstract - extractive body cue:** Most existing methods treat navigation and manipulation as separate stages, which can yield navigation endpoints that are poor for manipulation or manipulation-friendly poses that are ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose 3D Interaction Chains (3D-IC), a unified framework that couples multi-stage navigation and manipulation planning.
- **p. 1 / Abstract - extractive body cue:** 3D-IC maintains a shared 3D feature map for both skills, generates stage-aligned interaction waypoints, and links them into candidate multi-stage chains.
- **p. 1 / Abstract - extractive body cue:** A hierarchical policy then scores these chains by jointly considering feasibility (via VLM reasoning over waypointcentric 3D features) and transition cost, selecting the best trade-off ...
- **p. 2 / 1. Introduction - extractive body cue:** However, such independently designed policies and limited heuristics struggle to generalize across diverse situations.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, a 3D feature map (Wang et al., 2025b; Wang & Lee, 2025) is constructed to fuse map-level context with egocentric visual ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, such independently designed policies and limited heuristics struggle to generalize across diverse situations. | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | The navigation policy πn takes mt as input and outputs base actions an t ∈{Forward, Left, Right}, whereas the manipulation policy πm ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | navigation, policy, takes, input, outputs, base, actions, Forward, Left, Right | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | shared, high-level, policy, takes, feature, input, predicts, interaction | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: navigation, policy, takes, input, outputs, base, actions, Forward, Left, Right | p. 3 (3. Preliminaries of Mobile Manipulation), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | base plus arm/gripper action; body terms: summary, Interaction, Chains, D-IC, OVMM, task, includes, feature | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2. 3D-IC Construction) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: policy, optimized, standard, autoregressive, cross-entropy, loss, xprompt, where | p. 6 (4.3. Joint Planning with 3D-IC), p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.2. 3D-IC Construction), p. 5 (4.2. 3D-IC Construction), p. 5 (4.2. 3D-IC Construction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.2. 3D-IC Construction), p. 4 (4.1. Unified Modeling of Multi-stage Interaction) |
| Success / guarantee | task completion and recovery | p. 7 (5.2. Evaluation Results), p. 9 (5.3. Real-world Evaluation), p. 6 (5.1. Experimental Setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, a 3D feature map (Wang et al., 2025b; Wang & Lee, 2025) is constructed to fuse map-level context with egocentric visual ...
- **p. 1 / 1. Introduction - extractive body cue:** Existing OVMM methods can be broadly categorized into modular and reinforcement learning (RL)-based approaches.
- **p. 1 / 1. Introduction - extractive body cue:** (a) Existing methods for OVMM typically plan navigation and manipulation as separate stages, which can result in navigation endpoints that are suboptimal for subsequent interaction.
- **p. 3 / 3. Preliminaries of Mobile Manipulation - extractive body cue:** Since the two policies differ in both inputs and action spaces, existing approaches, whether modular pipelines or RL-based methods, typically make decisions with independent policies.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.2. 3D-IC Construction)): In summary, we propose 3D Interaction Chains (3D-IC) for the OVMM task in this paper.

- **p. 2 / 1. Introduction - extractive body cue:** Our 3D-IC includes: (1) a 3D feature map that captures information needed for both navigation and manipulation, (2) an interaction chain that enables unified planning ...
- **p. 5 / 4.2. 3D-IC Construction - extractive body cue:** Following frontier-based exploration (FBE) (Yamauchi, 1997), repeatedly navigating to frontier locations enables the robot to progressively reveal unknown areas and discover targets.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Each Move tomato from table to counter Move apple from couch to table Move knife from cabinet to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Consequently, the agent navigated back to a nightstand in the initial room to complete the placement, thereby avoiding ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The consistently high SPL scores indicate that our method achieves efficient trajectory, rather than merely reducing step counts ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | Figure 5. Failure cases of 3D-IC on OVMM Dataset. The failure cases are categorized according to the four ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (3. Preliminaries of Mobile Manipulation), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminaries of Mobile Manipulation), interface p. 3 (3. Preliminaries of Mobile Manipulation), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4.1. Unified Modeling of Multi-stage Interaction), objective p. 6 (4.3. Joint Planning with 3D-IC), p. 6 (4.3. Joint Planning with 3D-IC), p. 4 (4.2. 3D-IC Construction), p. 5 (4.2. 3D-IC Construction), p. 5 (4.2. 3D-IC Construction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
