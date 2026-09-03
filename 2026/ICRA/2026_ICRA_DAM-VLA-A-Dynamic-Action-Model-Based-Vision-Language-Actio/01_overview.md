# DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html.
> PDF retrieval source: https://arxiv.org/pdf/2603.00926v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html
- Full-text retrieval: https://arxiv.org/pdf/2603.00926v1
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A central challenge in robotics is enabling robots to perform diverse tasks in dynamic environments.를 문제로 두고, Rather than loosely coupling a VLM with separate action models, we introduce the DAM-VLA framework (Figure 1), which fully exploits the strengths of VLMs to support both task-specific precision and generalization in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In dynamic environments such as warehouses, hospitals, and homes, robots must seamlessly transition between gross motion and precise manipulations to complete complex tasks.
- **p. 1 / Abstract - extractive body cue:** However, current Vision-Language-Action (VLA) frameworks, largely adapted from pre-trained Vision-Language Models (VLMs), often struggle to reconcile general task adaptability with the specialized precision required for ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose DAMVLA, a dynamic action model-based VLA framework.
- **p. 1 / Abstract - extractive body cue:** DAMVLA integrates VLM reasoning with diffusion-based action models specialized for arm and gripper control.
- **p. 1 / Abstract - extractive body cue:** Specifically, it introduces (i) an action routing mechanism, using task-specific visual and linguistic cues to select appropriate action models (e.g., arm movement or gripper manipulation), ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A central challenge in robotics is enabling robots to perform diverse tasks in dynamic environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although these approaches achieve high precision in targeted scenarios, they generalize poorly across varying environments and tasks.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Rather than loosely coupling a VLM with separate action models, we introduce the DAM-VLA framework (Figure 1), which fully exploits the strengths of VLMs to ...
- **p. 3 / III. METHOD - extractive body cue:** Overall Architecture Our goal is to develop a dynamic action model-based VLA framework that enables different robots to physically execute diverse tasks in dynamic environments ...
- **p. 3 / III. METHOD - extractive body cue:** The vision model consists of powerful
- **p. 4 / III. METHOD - extractive body cue:** (1) To fully leverage the specific manipulation capabilities of different diffusion action models and the VLM's inherent reasoning capabilities, we propose the dynamic action model.
- **p. 4 / III. METHOD - extractive body cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 4 / III. METHOD - extractive body cue:** The resulting output consists of the cognition and reasoning latents, f cog and f rea, respectively. f rea and f cog are derived from the ...
- **p. 3 / III. METHOD - extractive body cue:** In Figure 3, the architecture of DAM-VLA is shown to consist of three key components: 1) A vision-language model, that encodes information from observation ot ...
- **p. 5 / III. METHOD - extractive body cue:** To reflect the prior that the action model requires higher precision and supervision focus immediately before the state change, we assign a larger variance to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Overall Architecture Our goal is to develop a dynamic action model-based VLA framework that enables different robots to physically execute diverse tasks in dynamic environments while receiving an RGB image observation and ... | image/video, language instruction, proprioception과 history | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | Overall, Architecture, goal, develop, dynamic, action, model-based, VLA, framework, enables, different, robots | language-grounded task state와 action-policy context | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Formally, given the language instruction l and visual observation ot at time t, the model π predicts a temporal action sequence [at, at+1, ..., at+N] = π(l, ot). | continuous action, pose 또는 action chunk | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Objective/outcome | The output is the predicted weight w, which is supervised by the following cross-entropy loss: Lclass = // -( ˆw log(w) + (1 -ˆw) log(1 -w))//1. | instruction following, task success, generalization과 latency | p. 4 (III. METHOD), p. 5 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Rather than loosely coupling a VLM with separate action models, we introduce the DAM-VLA framework (Figure 1), which fully exploits the strengths of VLMs to ...
- **p. 3 / III. METHOD - extractive body cue:** Overall Architecture Our goal is to develop a dynamic action model-based VLA framework that enables different robots to physically execute diverse tasks in dynamic environments ...
- **p. 3 / III. METHOD - extractive body cue:** The vision model consists of powerful
- **p. 4 / III. METHOD - extractive body cue:** (1) To fully leverage the specific manipulation capabilities of different diffusion action models and the VLM's inherent reasoning capabilities, we propose the dynamic action model.
- **p. 4 / III. METHOD - extractive body cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized diffusion-based ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Our model achieves the highest average success rate of 71%, outperforming competing methods by a substantial margin.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. We conduct 50 evaluation trials with randomized initial furniture placements. As shown in Table IV are the success rates of each step of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | Simulated Evaluations We first evaluate our method using the SIMPLER simulation [14], a suite of open-source simulated environments designed to mirror common real-world robot manipulation setups. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | Furthermore, we fine-tune our DAM-VLA model on both simulated and real-world datasets. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | The success rate of task completion is used as the evaluation metric for all VLA models. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | Fig. 1: DAM-VLA framework and experimental results. (a) We propose a DAM-VLA framework that dynamically integrates the inherent reasoning capabilities of VLMs with specialized diffusion-based action models tailored for arm movement and ... | fair input/data/compute/action matching | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: The evaluation encompasses both in-distribution and out-of-distribution scenarios. The in-distribution setting includes variations in object positions and lighting conditions consistent with the training ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: The architecture of our DAM-VLA. Given an RGB image observation and a task description, the model predicts a sequence of temporal actions. The ...
- **p. 4 / III. METHOD - extractive body cue:** Additionally, both models receive random noise nrand as input to facilitate the diffusion process.
- **p. 4 / III. METHOD - extractive body cue:** Dual-Scale Action Weighting To enhance the robustness in distinguishing between arm movement and gripper manipulation, we propose a dualscale action weighting mechanism for model training, ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To assess robustness, we divide the evaluation into in-distribution and out-ofdistribution scenarios, as illustrated in Figure 6.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 A central challenge in robotics is enabling robots to perform diverse tasks in dynamic environments.를 문제로 두고, Rather than loosely coupling a VLM with separate action models, we introduce the DAM-VLA framework (Figure 1), which fully exploits the strengths of VLMs to support both task-specific precision and generalization in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
