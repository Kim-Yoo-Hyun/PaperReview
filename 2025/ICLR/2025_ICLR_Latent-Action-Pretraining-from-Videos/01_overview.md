# Latent Action Pretraining from Videos

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html.
> PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Sejune Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter Fox, Minjoon Seo
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, latent action, human video, video pretraining, action representation
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html
- Code/Project: https://latentactionpretraining.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Latent Action Pretraining은 실제 행동 라벨 없이 영상 프레임 사이의 변화를 이산 행동으로 학습한 뒤 이를 로봇 제어에 연결한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45d74e190008c7bff2845ffc8e3facd3-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We introduce Latent Action Pretraining, the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels.
- **p. 1 / ABSTRACT - extractive body cue:** Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose a method to learn from internet-scale videos that do not have robot action labels.
- **p. 1 / ABSTRACT - extractive body cue:** We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to ...
- **p. 1 / ABSTRACT - extractive body cue:** Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the web lacks explicit ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, diverse real-world robot datasets mostly require human teleoperation, which makes scaling difficult.

## Core Idea

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Latent Action Pretraining consists of two models that are learned sequentially, followed by a finetuning stage to map the latent actions to real robot actions.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We expect that our method opens up the potential for building foundation models for robotics by pretraining on much larger web-scale video data.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, on real-world manipulation tasks, our method leads to a new monolithic VLA model, outperforming OPENVLA, the current state-of-the-art model Vision Language Action (VLA) model ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** The VQ-VAE objective enables the latent action zt to be discrete tokens (codebooks), making it easy for VLMs to predict zt.
- **p. 4 / 2. Latent Pretraining - extractive body cue:** 3.2 LATENT PRETRAINING We use the encoder of the latent action quantization model as an inverse dynamics model to label all frames xt, given frame ...
- **p. 4 / 2. Latent Pretraining - extractive body cue:** Our latent action quantization model is an encoder-decoder architecture where the encoder takes the current frame xt and the future frame xt+H of a video ...
- **p. 3 / 2. Latent Pretraining - extractive body cue:** Note that we use the same pretraining dataset for Latent Action Quantization and Latent Pretraining.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then, we do action pretraining by using a pretrained VLM to predict the zt given the language instruction of a video clip and the current image xt. | image/video, language instruction, proprioception과 history | p. 4 (2. Latent Pretraining), p. 2 (1 INTRODUCTION) |
| State/latent | Then, action, pretraining, pretrained, VLM, predict, given, language, instruction, video, clip, current | language-grounded task state와 action-policy context | p. 4 (2. Latent Pretraining), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining) |
| Output/action | In the second stage, we perform behavior cloning by pretraining a Vision-Language Model to predict latent actions derived from the first stage based on video observations and task descriptions. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining), p. 1 (1 INTRODUCTION) |
| Objective/outcome | (1) Latent Action Quantization: We first learn discrete latent actions in a fully unsupervised manner using the VQ-VAE objective (Detail in Figure 8). | instruction following, task success, generalization과 latency | p. 3 (2. Latent Pretraining), p. 3 (2. Latent Pretraining), p. 4 (2. Latent Pretraining) |

## Main Claims and Actual Contribution

- 양자화 모델이 만든 잠재 행동을 관측·지시에서 예측하도록 사전학습하고 소량의 로봇 데이터로 실행 가능한 행동을 학습한다. [PDF 3쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45d74e190008c7bff2845ffc8e3facd3-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45d74e190008c7bff2845ffc8e3facd3-Paper-Conference.pdf#page=4)
- 실물 탁상 조작에서 새 물체·언어 지시로의 일반화와 사람 조작 영상만 사용한 사전학습의 전이 효과를 평가했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45d74e190008c7bff2845ffc8e3facd3-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/45d74e190008c7bff2845ffc8e3facd3-Paper-Conference.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption) |
| Embodiment/environment | 4.1 BENCHMARKS AND ENVIRONMENTS We evaluate the effectiveness of LAPA on 9 different task categories in 2 different simulation environments and 3 different real-world robotic tasks. | hardware/simulator version and reset protocol | p. 5 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Dataset/benchmark | Real-World Tabletop Manipulation experiments used a 7 DOF Franka Emika Panda robot arm in three environments (shown in Figure 9 (c)). | role, split, size and leakage | p. 5 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Metric | Average Success Rate (%) ± StdErr across the three different pretrainfinetune combinations from the Language Table benchmark as described in Table 3. | definition, denominator, direction and uncertainty | p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | (2024) since it is not a behavior cloning baseline. | fair input/data/compute/action matching | p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 25 / Figure/Table caption - extractive body cue:** Figure 17: Success and Failure Cases of UNIPI. (Top) Given the instruction of ‘move the green block away from the red cube and red pentagon', ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We observe that most failures of LAPA are due to early grasping.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** Like before, UNIPI is constrained by its diffusion model's planning limitations, while VPT performs strongly, even surpassing ACTIONVLA in the unseen setting.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** 6 LIMITATIONS AND CONCLUSION In this paper, we introduce Latent Action Pretraining, a scalable pretraining method for building VLAs without using ground-truth action labels.
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** 3We leave parameter efficient fine-tuning approaches as future work for finetuning (Hu et al., 2022).
- **p. 5 / 4 EXPERIMENTS - extractive body cue:** UNIPI (Du et al., 2023) uses a video diffusion model during pretraining to generate video rollouts given a language instruction, which does not require any ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Furthermore, by comparing LAPA which does not leverage action-labeled trajectories during pretraining with models that use action-labeled trajectories during pretraining (ACTIONVLA and OPENVLA), we observe ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (2. Latent Pretraining)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (27 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, it is challenging to learn from internet video data for two major challenges: first, much of the raw data on the web lacks explicit action labels; second, the data ... (p. 1, 1 INTRODUCTION).
- **Actual contribution:** Vision-Language-Action Models (VLA) for robotics (Brohan et al., 2023; Kim et al., 2024) are trained by aligning large language models with vision encoders, and then finetuning it on on diverse ... (p. 1, 1 INTRODUCTION).
- **Evaluation boundary:** 4.5 LEARNING FROM HUMAN MANIPULATION VIDEOS Scratch UniPi VPT LAPA 0 10 20 30 40 50 60 AVG Success Rate (%) 34.4 0.7 45.8 52.1 (a) SIMPLER Results Average Knock ... (p. 8, 4 EXPERIMENTS).
- **Explicit failure boundary:** We observe that most failures of LAPA are due to early grasping. (p. 7, 4 EXPERIMENTS).

## 원문과 공개 자료

- 저자 표기와 순서를 표제면에서 확인했다. [저자 원문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45d74e190008c7bff2845ffc8e3facd3-Paper-Conference.pdf#page=1)
- 코드 — 잠재 행동 조건부 정책 모델 · latent_pretraining/llama_action.py [배포 파일](https://raw.githubusercontent.com/LatentActionPretraining/LAPA/46aca51d7faebcec02d7d323bbb3820c2df07bc6/latent_pretraining/llama_action.py)
- 가중치 — LAPA-7B-openx 모델 매개변수 · params [배포 파일](https://huggingface.co/latent-action-pretraining/LAPA-7B-openx/blob/b5397375f9dd5e07fcaf2e88e6da8690524058b2/params)
- 데이터 — Open X 동영상에서 만든 잠재 행동 학습 기록 · latent_action_pretraining_openx.jsonl [배포 파일](https://huggingface.co/latent-action-pretraining/LAPA-7B-openx/blob/b5397375f9dd5e07fcaf2e88e6da8690524058b2/latent_action_pretraining_openx.jsonl)
