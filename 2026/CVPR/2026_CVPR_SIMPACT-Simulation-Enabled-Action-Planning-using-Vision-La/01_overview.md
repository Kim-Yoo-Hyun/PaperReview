# SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLM, Planning, simulation
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, despite their remarkable commonsense and semantic reasoning capabilities, VLMs lack a grounded understanding of physical dynamics.를 문제로 두고, In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present a pipeline for automatically generating multi-physics simulatio ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Models (VLMs) exhibit remarkable common-sense and semantic reasoning capabilities.
- **p. 1 / Abstract - extractive body cue:** However, they lack a grounded understanding of physical dynamics.
- **p. 1 / Abstract - extractive body cue:** This limitation arises from training VLMs on static internet-scale visual-language data that contain no causal interactions or action-conditioned changes.
- **p. 1 / Abstract - extractive body cue:** Consequently, it remains challenging to leverage VLMs for fine-grained robotic manipulation tasks that require physical understanding, reasoning, and corresponding action planning.
- **p. 1 / Abstract - extractive body cue:** To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any ...
- **p. 2 / 1. Introduction - extractive body cue:** Lacking physical understanding, VLMs often propose plans that appear reasonable in language but fail during execution.
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose a framework that augments VLMs with physical simulation rollouts as contextual feedback, enabling test-time physical reasoning for action planning.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present ...
- **p. 2 / 1. Introduction - extractive body cue:** By augmenting VLMs with physical simulation, our framework enables them to anticipate action consequences, evaluate predicted outcomes, and iteratively adjust their decisions at test time, ...
- **p. 3 / 3. Method - extractive body cue:** Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs robot action sequence ...
- **p. 4 / 3.1. Simulation Construction - extractive body cue:** Our method first instantiates a physics simulator given the real-world scene.
- **p. 3 / 3.1. Simulation Construction - extractive body cue:** Our approach employs a physics-based simulator to predict the consequences of actions for manipulation planning.
- **p. 4 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** 1, our planner takes as input the initial RGB-D observation I0, the initial simulator state s0, task description `task, VLM, and SIM.
- **p. 5 / 3.2. Action Planning via Simulation-enabled VLM - extractive body cue:** In particular, at each selected time step t, we render a simulator observation image Ii t and include the numerical action ai t and state ...
- **p. 3 / 3. Method - extractive body cue:** The resulting visual observations and object states from each rollout are then fed back to the VLM as additional context for iterative refinement.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs robot action sequence a = {at}1tT , where at 2 ... | image/video, language instruction, proprioception과 history | p. 3 (3. Method), p. 5 (3.2. Action Planning via Simulation-enabled VLM) |
| State/latent | framework, enables, zero-shot, robotic, manipulation, action, generation, single, RGB-D, image, input, natural | language-grounded task state와 action-policy context | p. 3 (3. Method), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM) |
| Output/action | In particular, at each selected time step t, we render a simulator observation image Ii t and include the numerical action ai t and state si t in the context. | continuous action, pose 또는 action chunk | p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3.1. Simulation Construction) |
| Objective/outcome | If the VLM determines that the proposed action sequence achieves the task objective, the sequence is executed in the real environment. | instruction following, task success, generalization과 latency | p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present ...
- **p. 2 / 1. Introduction - extractive body cue:** By augmenting VLMs with physical simulation, our framework enables them to anticipate action consequences, evaluate predicted outcomes, and iteratively adjust their decisions at test time, ...
- **p. 3 / 3. Method - extractive body cue:** Our framework enables zero-shot robotic manipulation action generation from a single RGB-D image input I0 and natural language instruction `task and outputs robot action sequence ...
- **p. 4 / 3.1. Simulation Construction - extractive body cue:** Our method first instantiates a physics simulator given the real-world scene.
- **p. 3 / 3.1. Simulation Construction - extractive body cue:** Our approach employs a physics-based simulator to predict the consequences of actions for manipulation planning.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** Our approach consistently achieves a substantially higher success rate than baselines, highlighting the effectiveness of simulation-enabled VLMs for action planning.
- **p. 7 / 4.2. Results - extractive body cue:** VLM-based methods, VoxPoser and MOKA, leveraging VLM's strong sceneunderstanding and reasoning capabilities, achieve non-zero success rates on tasks such as bowl stacking, shape rope and ...
- **p. 8 / 4.3. Ablation study - extractive body cue:** 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide sufficient ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results) |
| Embodiment/environment | We use ⇡0.5 [2], a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative baseline. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | 5 shows simulation and real-world rollouts of six of our seven tasks. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Results), p. 5 (4. Experiments) |
| Metric | 1) affects performance, reporting success rates over 10 trials in Table 4: using only 3 samples degrades performance, as limited rollouts fail to provide sufficient task information, leading to poor optimization; Increasing ... | definition, denominator, direction and uncertainty | p. 8 (4.3. Ablation study), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Baseline/ablation | Overall, our method consistently outperforms baseline methods across all evaluated tasks, highlighting its strong performance on challenging, physicsaware, fine-grained manipulation tasks. | fair input/data/compute/action matching | p. 7 (4.2. Results), p. 8 (4.3. Ablation study), p. 7 (4.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Failure Case Analysis - extractive body cue:** Planning failures occur when the robot fails to generate a feasible action sequence even after multiple rounds of action optimization.
- **p. 8 / 4.4. Failure Case Analysis - extractive body cue:** Failures are categorized as perception, planning, or execution. successful action sequence is particularly challenging.
- **p. 7 / 4.1. Experimental Setup - extractive body cue:** We show representative failures from baseline methods that lack simulationenabled reasoning.
- **p. 7 / 4.2. Results - extractive body cue:** However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling push) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Definition of tasks. For each manipulation task, we list the corresponding instruction and success criteria. Tasks Instruction Success Condition Non-toppling push Push the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Action optimization process. We show a representative example from the non-toppling push task. The left three images show simulation rollouts from initial VLM-sampled ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, despite their remarkable commonsense and semantic reasoning capabilities, VLMs lack a grounded understanding of physical dynamics.를 문제로 두고, In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present a pipeline for automatically generating multi-physics simulatio ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Action Planning via Simulation-enabled VLM), p. 5 (3.2. Action Planning via Simulation-enabled VLM), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, despite their remarkable commonsense and semantic reasoning capabilities, VLMs lack a grounded understanding of physical dynamics. (p. 1, 1. Introduction).
- **Actual contribution:** In summary, this paper makes the following contributions: • We introduce a test-time, zero-shot framework enabling VLMs to plan physics-aware embodied actions; • We present a pipeline for automatically generating ... (p. 2, 1. Introduction).
- **Evaluation boundary:** Table 3. Ablation. Success rates (%) over 10 trials for each task after removing each component of our method. Results demonstrate the importance of VLM-conditioned sampling and the VLM's simulation-enabled ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** However, they struggle with tasks that require precise action planning, where small errors, such as pushing the wrong part of an object (in non-toppling push) or squeezing an incorrect region ... (p. 7, 4.2. Results).
