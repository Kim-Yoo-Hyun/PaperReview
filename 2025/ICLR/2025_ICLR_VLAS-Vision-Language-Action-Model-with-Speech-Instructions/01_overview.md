# VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/804a1a9de5787e3597b4bb64e1a48ec3-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/112658. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Wei Zhao, Pengxiang Ding, Zhang Min, Zhefei Gong, Shuanghao Bai, Han Zhao, Donglin Wang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/804a1a9de5787e3597b4bb64e1a48ec3-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

VLAS는 음성으로 지시한 조작을 수행하고 화자별 선호나 소유 관계까지 반영하도록 음성 표현을 로봇 정책에 통합한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=1)

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

- 음성·텍스트 정렬과 행동 학습에 사용할 SQA·CSI 자료를 구성하고, 음성과 영상에서 행동을 생성하도록 단계별로 학습했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=6)
- 화자의 목소리로 관련 개인 정보를 검색하는 방식을 도입하고, 화자에 따라 정답 행동이 달라지는 맞춤형 조작을 평가했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf#page=9)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 3 (3 METHOD)이다.
