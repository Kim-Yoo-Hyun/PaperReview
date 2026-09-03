# VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=K4FAFNRpko.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/112658. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=K4FAFNRpko
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/112658
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you want.를 문제로 두고, To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for robot manipulation without needing external speech recognition ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance.
- **p. 1 / ABSTRACT - extractive body cue:** However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction.
- **p. 1 / ABSTRACT - extractive body cue:** Traditional speech integration methods usually involves a separate speech recognition system, which complicates the model and introduces error propagation.
- **p. 1 / ABSTRACT - extractive body cue:** Moreover, the transcription procedure would lose nonsemantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized ...
- **p. 1 / ABSTRACT - extractive body cue:** To overcome above challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you want.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Based on the above analysis, we propose guiding a robot's behavior through speech rather than text.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.
- **p. 3 / 3 METHOD - extractive body cue:** We present VLAS, a VLA model directly supporting speech instructions for robot manipulation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.
- **p. 3 / 3 METHOD - extractive body cue:** 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.
- **p. 3 / 3 METHOD - extractive body cue:** As illustrated in Figure 2, we first provide an overview of the VLAS architecture (Section 3.1).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a. | image/video, language instruction, proprioception과 history | p. 3 (3 METHOD), p. 1 (1 INTRODUCTION) |
| State/latent | ARCHITECTURE, VLAS, Overall, Framework, takes, human, speech, instructions, visual, observations, input, directly | language-grounded task state와 action-policy context | p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Output/action | VLAs, such as RT-2 (Brohan et al., 2023), which are fine-tuned from foundation VLMs like PaLM-E (Driess et al., 2023) using robotic trajectory data, can take human instructions and visual observations as ... | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 3 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Objective/outcome | instruction following, task success, generalization과 latency | instruction following, task success, generalization과 latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Based on the above analysis, we propose guiding a robot's behavior through speech rather than text.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.
- **p. 3 / 3 METHOD - extractive body cue:** We present VLAS, a VLA model directly supporting speech instructions for robot manipulation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to Whisper large-v2 on ...
- **p. 8 / 1. I have a blue - extractive body cue:** Meanwhile, when our RAG module is integrated with the VLA, its performance significantly improves.
- **p. 9 / 1. I have a blue - extractive body cue:** As can be observed, VLAS-Base obtains nearly the same performance to LLaVA, while significantly outperforming other VLMs.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 10 (Figure/Table caption), p. 8 (1. I have a blue) |
| Embodiment/environment | 4.3 EXPERIMENTS WITH A REAL-WORLD UR5 ROBOT ARM We fine-tune our VLAS-Base by utilizing both the Berkeley UR5 demonstration dataset and our own cup-picking dataset. | hardware/simulator version and reset protocol | p. 8 (1. I have a blue), p. 8 (1. I have a blue) |
| Dataset/benchmark | CALVIN with Speech Instructions (CSI) Dataset Given that conventional robot manipulation datasets contain only textual task instructions, we utilized the aforementioned TTS model to generate the corresponding speech instructions. | role, split, size and leakage | p. 8 (1. I have a blue), p. 8 (1. I have a blue), p. 6 (1. I have a blue), p. 6 (1. I have a blue) |
| Metric | Table 4: Performance comparison on LibriSpeech and SGQA benchmark, using word error rate (WER) and accuracy as evaluation metrics. LLaVA and BLIP-2 employ the ground truth textual insturctions on SGQA. | definition, denominator, direction and uncertainty | p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 8 (1. I have a blue) |
| Baseline/ablation | Moreover, our VLAS is compared for speech modality input with the baseline VLA model and another powerful VLA model, Roboflamingo, both similarly derived from the VLM. | fair input/data/compute/action matching | p. 7 (1. I have a blue), p. 7 (1. I have a blue), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** Our future work may focus on exploring other auxiliary information in human speech or environmental sounds to enable the robot to better understand and complete ...
- **p. 10 / 1. I have a blue - extractive body cue:** Moreover, although VLAS-Base falls behind LLaVA with ground-truth textual instructions on the SGQA benchmark, it still surpasses BLIP-2.
- **p. 9 / 1. I have a blue - extractive body cue:** These results indicate that the introduction of the speech modality does not degrade the performance of the foundation model.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: For personalization tasks, (a) previous VLAs with text instructions fail, while (b) our VLAS with speech in- structions could successfully address them. To ...
- **p. 8 / 1. I have a blue - extractive body cue:** It can be seen from Table 2 that when the RAG module is removed, the performance of VLAS significantly degrades on the customized benchmark.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you want.를 문제로 두고, To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for robot manipulation without needing external speech recognition ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
