# VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2410.08792.
> PDF retrieval source: https://arxiv.org/pdf/2410.08792. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics
- Official paper: https://arxiv.org/abs/2410.08792
- Full-text retrieval: https://arxiv.org/pdf/2410.08792
- Code/Project: https://ai4ce.github.io/SeeDo/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans.를 문제로 두고, In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon human demonstration ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability.
- **p. 1 / Abstract - extractive body cue:** Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning.
- **p. 1 / Abstract - extractive body cue:** In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning.
- **p. 1 / Abstract - extractive body cue:** Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline.
- **p. 1 / Abstract - extractive body cue:** We named it SeeDo because it enables the VLM to "see" human demonstrations and explain the corresponding plans to the robot for it to "do".
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To mitigate these limitations, SeeDo integrates not only with a VLM interpreter module but also with a ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Inspired by this capability, we propose SeeDo, a modularized agent centered around a VLM.
- **p. 3 / III. METHOD - extractive body cue:** To alleviate these issues, we introduce a visual prompting module in SeeDo that enhances the visual capabilities of the VLM.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, VLMs' rich commonsense knowledge enables them to understand objects and their relationships, helping robots understand the task goals despite the embodiment gap.
- **p. 3 / III. METHOD - extractive body cue:** The module first instructs the VLM to identify objects in the frames and then use an open-vocabulary object detector [53] to extract object bounding boxes ...
- **p. 4 / III. METHOD - extractive body cue:** In real-world experiment, we follow [1, 20] and first use a segmentation model to segment all objects of interest in the RGB images, then query ...
- **p. 3 / III. METHOD - extractive body cue:** The speed valleys are identified as keyframes. b) The Visual Prompting module detects and tracks objects and then applies the tracking results as visual prompts ...
- **p. 4 / III. METHOD - extractive body cue:** Specifically, following the approaches in [1] and [20], we use Language Model Programs (LMPs) to implement the task plans on a UR10e robot arm in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Some employ pretrained VLMs for further fine-tuning to learn the mapping from visual inputs and language instructions to actions [5, 6], or leverage the general knowledge of VLMs to identify salient objects ... | image/video, language instruction, proprioception과 history | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| State/latent | Some, employ, pretrained, VLMs, further, fine-tuning, learn, mapping, visual, inputs, language, instructions | language-grounded task state와 action-policy context | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Output/action | In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon human demonstration ... | continuous action, pose 또는 action chunk | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | Context length becomes a major constraint when VLMs process long-horizon videos. | instruction following, task success, generalization과 latency | p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Inspired by this capability, we propose SeeDo, a modularized agent centered around a VLM.
- **p. 3 / III. METHOD - extractive body cue:** To alleviate these issues, we introduce a visual prompting module in SeeDo that enhances the visual capabilities of the VLM.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, VLMs' rich commonsense knowledge enables them to understand objects and their relationships, helping robots understand the task goals despite the embodiment gap.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** To achieve success (TSR=1), each step in the plan must match the demo's action sequence in both content and temporal order. • FSR is equivalent ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Conventional evaluation metric reports success rate (SR) of each task which could only reflect the completion at the final state of operation.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This indicates room for future improvement.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or brief descriptions. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | Real-world Experiment Setup Real-world experiments have demonstrated that SeeDo can manipulate objects in the physical world using an appropriate LMP. | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the total success rates on all tasks is ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | SeeDo outperforms all closed-source and open-source video VLM baselines across TSR, FSR, and SSR. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Additionally, we identify three types of errors from the failure cases to analyze and provide insights on the strengths and weaknesses of various models on ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** However, spatial errors remain the main source of SeeDo 's failures.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Model Success Rate Failure Reason TSR↑ FSR↑ SSR↑ Vision↓ Spatial↓ Temporal↓ SeeDo w/o V.P.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Error type percentages of all the failure cases of all the methods. Note that error types are not exclusive. The barplot of the ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** These tasks represent some common robotics scenarios that feature a clear temporal sequence and dynamic interactions that cannot be adequately captured with still images or ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, significant challenges remain in teaching robots to learn from human videos due to the substantial domain gap between robots and humans.를 문제로 두고, In summary, the contributions of this work are as follows: • We introduce SeeDo, a VLM-based agent that integrates keyframe selection, visual prompting, and VLM interpreter modules to interpret long-horizon human demonstration ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
