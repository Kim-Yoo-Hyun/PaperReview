# TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.12514.
> PDF retrieval source: https://arxiv.org/pdf/2409.12514. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://arxiv.org/abs/2409.12514
- Full-text retrieval: https://arxiv.org/pdf/2409.12514
- Code/Project: https://tiny-vla.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Our results show that TinyVLA-H outperforms OpenVLA, achieving superior performance with 20 times less inference latency. challenges due to limited data and the difficulty of learning physical motion [1], [2].를 문제로 두고, Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast inference, strong performance, and excellent generalization capabilitie ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes.
- **p. 1 / Abstract - extractive body cue:** However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a new family of compact vision-languageaction models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster ...
- **p. 1 / Abstract - extractive body cue:** Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, highspeed multimodal models, and (2) integrating a diffusion policy ...
- **p. 1 / Abstract - extractive body cue:** We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our results show that TinyVLA-H outperforms OpenVLA, achieving superior performance with 20 times less inference latency. challenges due to limited data and the difficulty of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Given these challenges, a natural question arises: How can we build VLA models that retain the advantages of existing VLA models while being both fast ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast inference, ...
- **p. 6 / 1 Background - extractive body cue:** In Figure 9, we present the spatial generalization performance of our methods.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we propose TinyVLA, a compact visionlanguage-action model designed for fast inference.
- **p. 3 / III. METHOD - extractive body cue:** We report the average success rate on multiple tasks, We use TinyVLA-H as our method.
- **p. 3 / III. METHOD - extractive body cue:** We posit that this approach enables the pre-trained model to process inputs with maximum linguistic fidelity while retaining flexibility.
- **p. 2 / III. METHOD - extractive body cue:** TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we ...
- **p. 3 / III. METHOD - extractive body cue:** After training is completed, we apply re-parameterization techniques to integrate the LoRA module seamlessly into the standard language model, thereby enhancing inference speed.
- **p. 3 / III. METHOD - extractive body cue:** Then, these normalized features are subsequently concatenated with the robot's proprioceptive state vector.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we freeze the pre-trained parts and utilize the ... | image/video, language instruction, proprioception과 history | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | TinyVLA, encompasses, several, crucial, designs, adopt, pre-trained, VLM, initialization, policy, network, During | language-grounded task state와 action-policy context | p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/action | First, the visuallanguage model (VLM) backbone encodes raw observations and language instructions into multimodal embedding vectors. | continuous action, pose 또는 action chunk | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Objective/outcome | We adopt diffusion policy as our policy head. limits gradient updates to a low-dimensional space. | instruction following, task success, generalization과 latency | p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast inference, ...
- **p. 6 / 1 Background - extractive body cue:** In Figure 9, we present the spatial generalization performance of our methods.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we propose TinyVLA, a compact visionlanguage-action model designed for fast inference.
- **p. 3 / III. METHOD - extractive body cue:** We report the average success rate on multiple tasks, We use TinyVLA-H as our method.
- **p. 3 / III. METHOD - extractive body cue:** We posit that this approach enables the pre-trained model to process inputs with maximum linguistic fidelity while retaining flexibility.
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** As shown in Table III, while the Diffusion Policy excels in the PlaceTennisBag task, our TinyVLA-H model achieved an average success rate of 44.5%, surpassing ...
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** It is evaluated with 3 seeds, and for each seed, the success rate was averaged over five different iterations.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | More Real-World Experiments: Bimanual Robot We further conducted experiments on the Bimanual UR5 Robot, applying it to three distinct tasks: PlaceBread, StackCube, and PlaceTennisBag. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Dataset/benchmark | We suspect this is because OpenVLA is pre-trained on the OpenX dataset, which consists entirely of single-arm robot data, making it ineffective when applied to bimanual robots. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Metric | We report the mean and standard deviation of success rates across 3 checkpoints. | definition, denominator, direction and uncertainty | p. 4 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Baseline/ablation | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the baselines? • Can TinyVLA interpret and follow ... | fair input/data/compute/action matching | p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / VI. CONCLUSION - extractive body cue:** Our approach overcomes the limitations of previous methods by
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We use a cross mark to denote the failure of the model and a checkmark to indicate successful task completion.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 10: Types of failure for TinyVLA with different sizes of pre-trained vision-language models.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Notably, the OpenVLA fails in every trial.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Secondly, the vanilla DP does not incorporate language instructions.
- **p. 3 / IV. EXPERIMENTS - extractive body cue:** In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation compared to the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 9: Spatial generalization. We conducted evaluations at multiple positions thoroughly outside the training zone on two position-sensitive tasks:place tennis and flip mug. For each ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Our results show that TinyVLA-H outperforms OpenVLA, achieving superior performance with 20 times less inference latency. challenges due to limited data and the difficulty of learning physical motion [1], [2].를 문제로 두고, Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast inference, strong performance, and excellent generalization capabilitie ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (1 Background), p. 6 (1 Background), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
