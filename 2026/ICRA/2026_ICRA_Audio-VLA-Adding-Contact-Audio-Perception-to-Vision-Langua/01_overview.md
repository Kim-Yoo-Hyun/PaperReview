# Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html.
> PDF retrieval source: https://arxiv.org/pdf/2511.09958v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html
- Full-text retrieval: https://arxiv.org/pdf/2511.09958v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency contact audio, and the lack of audio-enh ...를 문제로 두고, 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The Vision-Language-Action models (VLA) have achieved significant advances in robotic manipulation recently.
- **p. 1 / Abstract - extractive body cue:** However, vision-only VLA models create fundamental limitations, particularly in perceiving interactive and manipulation dynamic processes.
- **p. 1 / Abstract - extractive body cue:** This paper proposes Audio-VLA, a multimodal manipulation policy that leverages contact audio to perceive contact events and dynamic process feedback.
- **p. 1 / Abstract - extractive body cue:** AudioVLA overcomes the vision-only constraints of VLA models.
- **p. 1 / Abstract - extractive body cue:** Additionally, this paper introduces the Task Completion Rate (TCR) metric to systematically evaluate dynamic operational processes.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency contact audio, and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current VLA methods exhibit a fundamental limitation as they rely exclusively on visual perception [6]- [10].

## Core Idea

- **p. 2 / III. METHOD - extractive body cue:** 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we propose Audio-VLA, a multimodal manipulation policy that combines acoustic and visual perception.
- **p. 3 / III. METHOD - extractive body cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 3 / III. METHOD - extractive body cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Large-scale vision-language pretraining [4] enables VLA models to achieve generalizable manipulation capabilities across diverse scenarios.
- **p. 2 / III. METHOD - extractive body cue:** This section first details the Audio-VLA architecture, then presents our training objective and audio-enhanced simulation environments for LIBERO [8] and RLBench [9].
- **p. 4 / III. METHOD - extractive body cue:** This enables Faud to capture high-frequency acoustic features and temporal dynamics of contact events, providing physical interaction information unavailable through visual perception alone.
- **p. 4 / III. METHOD - extractive body cue:** The input of the proprio encoder is proprioceptive robot state pt, which includes information such as joint angles, encoded via an MLP layer ϕstate(·) to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Furthermore, recognizing the limitations of existing evaluation metrics that focus primarily on final task outcomes, the Task Completion Rate (TCR) evaluation metric is proposed to quantify dynamic process perceptual feedback capabiliti ... | image/video, language instruction, proprioception과 history | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| State/latent | Furthermore, recognizing, limitations, existing, evaluation, metrics, focus, primarily, final, task, outcomes, Completion | language-grounded task state와 action-policy context | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Subsequently, we extract the action hidden states Hact from Hdec, where each vector h(m) ∈Rdllm for m = 1, . . . , K · D encodes contextual information from all input ... | continuous action, pose 또는 action chunk | p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | This is achieved through the minimization of the mean L1 loss function: L = 1 K · D K-1 X k=0 D X i=1 | instruction following, task success, generalization과 latency | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / III. METHOD - extractive body cue:** 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this paper, we propose Audio-VLA, a multimodal manipulation policy that combines acoustic and visual perception.
- **p. 3 / III. METHOD - extractive body cue:** It consists of two powerful vision transformers, DINOv2 [23] and SigLIP [24], pre-trained on Internet-scale image data to capture rich visual features and comprehensive spatial ...
- **p. 3 / III. METHOD - extractive body cue:** The model consists of multi-modal encoders including audio, vision, and proprioceptive modules, multi-modal Projector that map heterogeneous features to a unified representation space, a 7B-parameter ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Large-scale vision-language pretraining [4] enables VLA models to achieve generalizable manipulation capabilities across diverse scenarios.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** I, AudioVLA achieves 97.6% average success rate on LIBERO and 55.1% on RLBench, outperforming all comparative methods.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** II, in seen environmental conditions, our Audio-VLA achieves threefold improvements in success rates compared to OpenVLA-OFT [39] and π0-FAST [5] on both EAWM and S5GO ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** The doubling of EAWM success rates after LoRA finetuning [26] and consistent improvements across both simulation and real-world experiments demonstrate that LoRA [26] is particularly ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Embodiment/environment | The performance gap reveals that in tasks requiring precise force control and continuous state monitoring, visual modality nearly loses its ability to perceive contact states under domain shift, whereas contact audio provide ... | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Dataset/benchmark | 3: Experimental setup showing the hardware platform and real-world manipulation tasks of contact audio feedback: Erasing All Whiteboard Marks (EAWM) and Scooping 5 Grams of Oatmeal (S5GO). | role, split, size and leakage | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Metric | AudioVLA preserves 30% and 20% success rates on EAWM and S5GO respectively, whereas vision-only methods approach near-zero performance. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Baseline/ablation | The inferior performance of the vision-only configuration compared to the full configuration demonstrates that audio provides critical information for TABLE IV: Ablation study results on Real-world Configuration EAWS S5GO Success rate T ... | fair input/data/compute/action matching | p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENT - extractive body cue:** Our proposed Audio-VLA demonstrates that acoustic perception addresses fundamental limitations of vision-only approaches in manipulation tasks, providing irreplaceable information particularly when visual perception fails to ...
- **p. 7 / V. CONCLUSION - extractive body cue:** This paper presents Audio-VLA, a multimodal manipulation policy that integrates acoustic perception into VLA models to overcome vision-only limitations.
- **p. 7 / V. CONCLUSION - extractive body cue:** Experimental results demonstrate that Audio-VLA achieves superior performance in both simulation environments and real-world tasks, proving the contribution of contact audio perception in overcoming visual ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Audio-VLA overcomes these limitations through acoustic signatures of interaction physics.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite these promising capabilities, integrating acoustic information into existing VLA frameworks presents technical challenges, such as extracting contact event information from high-frequency contact audio, and the lack of audio-enh ...를 문제로 두고, 2, the proposed Audio-VLA consists of four components including a multi-modal encoder, multi를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 2 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
