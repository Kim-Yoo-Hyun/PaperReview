# Learning Interactive Real-World Simulators

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/c4d66eae503694424123b93ac0fbaf17-Abstract-Conference.html.
> PDF retrieval source: https://arxiv.org/pdf/2310.06114. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, world model, interactive simulator, Vision-Language, zero-shot transfer
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/c4d66eae503694424123b93ac0fbaf17-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2310.06114
- Code/Project: https://universal-simulator.github.io/
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We illustrate that the observation prediction model can be rolled out autoregressively to obtain consistent and long-horizon videos. • We illustrate how the simulator can enable both high-level language policies, low-level control ...를 문제로 두고, In this work, we propose to combine a wealth of data in a conditional video generation framework to instantiate a universal simulator (UniSim)1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Generative models trained on internet data have revolutionized how text, image, and video content can be created.
- **p. 1 / ABSTRACT - extractive body cue:** Perhaps the next milestone for generative models is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents.
- **p. 1 / ABSTRACT - extractive body cue:** Applications of a real-world simulator range from controllable content creation in games and movies, to training embodied agents purely in simulation that can be directly ...
- **p. 1 / ABSTRACT - extractive body cue:** We explore the possibility of learning a universal simulator (UniSim) of real-world interaction through generative modeling.
- **p. 1 / ABSTRACT - extractive body cue:** We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We illustrate that the observation prediction model can be rolled out autoregressively to obtain consistent and long-horizon videos. • We illustrate how the simulator can ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Since different datasets are curated by different industrial or research communities for different purposes, divergence in information is natural and hard to overcome, posing difficulties ...

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we propose to combine a wealth of data in a conditional video generation framework to instantiate a universal simulator (UniSim)1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Nevertheless, we propose specific strategies for processing each type of data to unify the action space and align videos of variable lengths to actions in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Under a unified action-in-video-out interface, the simulator enables rich interaction through fine-grained motion control of otherwise static scenes and objects.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We first show how the simulator enables a vision-language policy to perform long-horizon goal-conditioned tasks through hindsight relabeling of simulated experience (Andrychowicz et al., 2017).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction by combining diverse ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We then formulate the universal simulator as an observation prediction model that predicts observations conditioned on actions and previous observations as shown in Figure 2.
- **p. 1 / ABSTRACT - extractive body cue:** We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2 LEARNING AN INTERACTIVE REAL-WORLD SIMULATOR We define a simulator of the real world as a model that, given some state of the world (e.g., an image frame), can take in some ... | observation, uncertainty/risk estimate와 task command | p. 2 (1 INTRODUCTION), p. 7 (1. Put cup 2. Pen 3. Apple) |
| State/latent | LEARNING, INTERACTIVE, REAL-WORLD, SIMULATOR, define, real, world, model, given, some, state, image | safe set, recovery state 또는 constraint margin | p. 2 (1 INTRODUCTION), p. 7 (1. Put cup 2. Pen 3. Apple), p. 7 (1. Put cup 2. Pen 3. Apple) |
| Output/action | In addition to testing the language instructions and simulated video by converting video trajectory into robot actions executed on the real robot, we also conduct simulator based evaluation to compare the reduction ... | shielded, recovery 또는 safe action | p. 7 (1. Put cup 2. Pen 3. Apple), p. 7 (1. Put cup 2. Pen 3. Apple), p. 3 (1 INTRODUCTION) |
| Objective/outcome | One advantage of this observation prediction model is that the simulator stays the same across all tasks and can be used in combination with any reward function, which can be separately learned. | task return과 violation/failure probability | p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 8 (1. Put cup 2. Pen 3. Apple) |

## Main Claims and Actual Contribution

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we propose to combine a wealth of data in a conditional video generation framework to instantiate a universal simulator (UniSim)1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Nevertheless, we propose specific strategies for processing each type of data to unify the action space and align videos of variable lengths to actions in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Under a unified action-in-video-out interface, the simulator enables rich interaction through fine-grained motion control of otherwise static scenes and objects.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We first show how the simulator enables a vision-language policy to perform long-horizon goal-conditioned tasks through hindsight relabeling of simulated experience (Andrychowicz et al., 2017).
- **p. 22 / Figure/Table caption - extractive body cue:** Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot data ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning on ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Diverse and stochastic simulations. On the left, we use text to specify the object being revealed by suffixing "uncovering" with the object name. ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** Purely finetuning on generated data drastically improves the captioning performance from no finetuning at all on ActivityNet (15.2 to 46.23), while achieving 84% performance of ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 22 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | [Bottom] Real-robot execution of an RL policy trained in simulation and zero-shot onto the real Language Table task. | hardware/simulator version and reset protocol | p. 8 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple) |
| Dataset/benchmark | [Bottom] Real-robot execution of an RL policy trained in simulation and zero-shot onto the real Language Table task. | role, split, size and leakage | p. 8 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple) |
| Metric | Figure 8: [Top] Simulation from low-level controls. UniSim supports low-level control actions as inputs to move endpoint horizontally, vertically, and diagonally. [Bottom] Real-robot execution of an RL policy trained in simulation and ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 22 (Figure/Table caption) |
| Baseline/ablation | Table 2: Evaluation of long-horizon actions. Re- duction in distance to goal (RDG) defined in Equa- tion 3 across 5 evaluation runs of VLM trained using simulated long-horizon data (bottom row) compared ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple), p. 5 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 8. Close top - extractive body cue:** Flexibility in diffusion models promotes simulation of highly stochastic environments that cannot be controlled by actions, so that a policy can learn to only control ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We see that the simulated rollouts capture both the endpoint movements and the physics of collision.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Training and inference of UniSim. UniSim is a video diffusion model trained to predict the next (variable length) set of observation frames (ot) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Specifically, the reverse process learns a denoising model ϵθ(o(k) t , k/ht-1, at-1) that, conditioned on the history, generates the next observationfrom initial ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 13: Failed environment simulation from the action "uncover bottle" without training on broad data as in UniSim. Top two videos are generated from only ...
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 14: When the text-to-video model behind UniSim is only trained on data from Brohan et al. (2022) as opposed incorporating broad data from the ...

## Why Read It

World models, safety, uncertainty, and recovery의 safety 문제를 이해하기 위해 읽는다. 본문은 We illustrate that the observation prediction model can be rolled out autoregressively to obtain consistent and long-horizon videos. • We illustrate how the simulator can enable both high-level language policies, low-level control ...를 문제로 두고, In this work, we propose to combine a wealth of data in a conditional video generation framework to instantiate a universal simulator (UniSim)1.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Since different datasets are curated by different industrial or research communities for different purposes, divergence in information is natural and hard to overcome, posing difficulties to a real-world simulator that ... (p. 1, 1 INTRODUCTION).
- **Actual contribution:** The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction by combining diverse datasets rich in along different ... (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot data in UniSim achieves the best ... (p. 22, Figure/Table caption).
- **Explicit failure boundary:** The model only trained on generic internet data, without action-rich manipulation data such as EPICKITCHENS (Damen et al., 2018), fails to simulate action-rich manipulations (Appendix F). (p. 4, 1 INTRODUCTION).
