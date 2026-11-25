# A Generalist Agent

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2205.06175.
> PDF retrieval source: https://arxiv.org/abs/2205.06175. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / TMLR
- Authors: Scott Reed, Konrad Żołna, Emilio Parisotto, Sergio Gómez Colmenarejo, Alexander Novikov, Gabriel Barth-Maron, Mai Giménez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom Eccles, Jake Bruce, Ali Razavi, Ashley Edwards, Nicolas Heess, Yutian Chen, Raia Hadsell, Oriol Vinyals, Mahyar Bordbar, Nando de Freitas
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Generalist Agent, Transformer, Multimodal Learning, Google DeepMind
- Official paper: https://arxiv.org/abs/2205.06175
- Venue verification: https://openreview.net/attachment?id=1ikK0kHjvj&name=pdf
- Full-text retrieval: https://arxiv.org/abs/2205.06175
- Code/Project: https://deepmind.google/discover/blog/a-generalist-agent/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Gato는 영상·텍스트·행동을 일련의 토큰으로 표현해 동일한 가중치로 게임, 언어 과제와 로봇팔 조작을 수행한다. [PDF 1쪽](https://arxiv.org/pdf/2205.06175v3#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Inspired by progress in large-scale language modeling, we apply a similar approach towards building a single generalist agent beyond the realm of text outputs.
- **p. 1 / Abstract - extractive body cue:** The agent, which we refer to as Gato, works as a multi-modal, multi-task, multi-embodiment generalist policy.
- **p. 1 / Abstract - extractive body cue:** The same network with the same weights can play Atari, caption images, chat, stack blocks with a real robot arm and much more, deciding based ...
- **p. 1 / Abstract - extractive body cue:** In this report we describe the model and the data, and document the current capabilities of Gato.
- **p. 1 / Abstract - extractive body cue:** A man surfing in the ocean as the sun sets G G What is the capital of France?
- **p. 7 / 1 Introduction - extractive body cue:** There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it is later tested ...
- **p. 10 / 1 Introduction - extractive body cue:** Agent Group 1 Group 2 Group 3 Group 4 Group 5 Average Gato 24.5% 33% 50.5% 76.5% 66.5% 50.2% BC-IMP (Lee et al., 2021) 23% ...

## Core Idea

- **p. 4 / 1 Introduction - extractive body cue:** During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results that ...
- **p. 6 / 1 Introduction - extractive body cue:** ALIGN (Jia et al., 2021) consists of 1.8B images and their alternative text (alt-text) annotations.
- **p. 6 / 1 Introduction - extractive body cue:** LTIP (Long Text & Image Pairs), consists of 312 million images with captions (Alayrac et al., 2022).
- **p. 7 / 1 Introduction - extractive body cue:** The environment consists of a Sawyer robot arm with 3-DoF cartesian velocity control, an additional DoF for velocity, and a discrete gripper action.
- **p. 8 / 1 Introduction - extractive body cue:** While the single-task online RL agents which generated the data still outperform Gato, this may be overcome by adding capacity or using offline RL training ...
- **p. 4 / 1 Introduction - extractive body cue:** The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 m (b, l) ...
- **p. 3 / 1 Introduction - extractive body cue:** After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw input text. • ...
- **p. 2 / Abstract - extractive body cue:** Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2.2 Embedding input tokens and setting output targets After tokenization and sequencing, we apply a parameterized embedding function f(·; θe) to each token (i.e. it is applied to both observations and actions) ... | image/video, language instruction, proprioception과 history | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| State/latent | Embedding, input, tokens, setting, output, targets, After, tokenization, sequencing, apply, parameterized, function | language-grounded task state와 action-policy context | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (Abstract) |
| Output/action | After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw input text. • Image patch tokens in raster order. • ... | continuous action, pose 또는 action chunk | p. 3 (1 Introduction), p. 2 (Abstract), p. 5 (1 Introduction) |
| Objective/outcome | Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions. | instruction following, task success, generalization과 latency | p. 2 (Abstract), p. 3 (1 Introduction), p. 4 (1 Introduction) |

## Main Claims and Actual Contribution

- 관측과 행동 양식마다 정한 토큰화를 거쳐 하나의 시퀀스 모델이 문맥에 맞는 출력을 생성하도록 학습한다. [PDF 3쪽](https://arxiv.org/pdf/2205.06175v3#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2205.06175v3#page=4)
- 실물 로봇팔의 RGB Stacking에서 물체 묶음별 쌓기 성능을 측정해 다중 과제 학습이 실제 조작으로 이어지는 범위를 평가했다. [PDF 7쪽](https://arxiv.org/pdf/2205.06175v3#page=7) · [PDF 10쪽](https://arxiv.org/pdf/2205.06175v3#page=10)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 14 (1 Introduction), p. 14 (1 Introduction) |
| Embodiment/environment | However, the Skill Mastery allows the agent to train on data involving the object shapes used for evaluation, i.e. the test set in Skill Generalization becomes a part of the Skill Mastery ... | hardware/simulator version and reset protocol | p. 14 (1 Introduction), p. 14 (1 Introduction) |
| Dataset/benchmark | For each task, we randomly sample 100 episodes and tokenize each of them. | role, split, size and leakage | p. 14 (1 Introduction), p. 14 (1 Introduction), p. 15 (1 Introduction), p. 15 (1 Introduction) |
| Metric | Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained on 35k expert episodes (upper bound). Right: Comparison ... | definition, denominator, direction and uncertainty | p. 12 (Figure/Table caption), p. 14 (1 Introduction), p. 14 (1 Introduction) |
| Baseline/ablation | Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained on 35k expert episodes (upper bound). Right: Comparison ... | fair input/data/compute/action matching | p. 12 (Figure/Table caption), p. 39 (Figure/Table caption), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 13: Embedding visualization. T-SNE visualization of embeddings from different tasks. A large part of the vision-language embeddings (M3W) overlaps with the language cluster (MassiveText). ...
- **p. 18 / 6 Related Work - extractive body cue:** 8 Limitations and Future work 8.1 RL data collection Gato is a data-driven approach, as it is derived from imitation learning.
- **p. 18 / 6 Related Work - extractive body cue:** This limitation underscores the need for a careful design and a deployment process that incorporates multiple disciplines and viewpoints.
- **p. 19 / 6 Related Work - extractive body cue:** Context-length is therefore a current limitation of our architecture, mainly due to the quadratic scaling of self-attention.
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 9: Few-shot performance, ablating over various pretraining settings. Orange corresponds to the base Gato pretrained on all data. Red is trained from scratch only ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 11: Comparing training/test task goal variations. Top: the standard "stack red on blue" task tested in the Skill Generalization benchmark. Bottom: the novel "stack ...
- **p. 19 / 6 Related Work - extractive body cue:** We hope to explore these architectures in future work.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 7 (1 Introduction), p. 10 (1 Introduction), p. 14 (1 Introduction), p. 8 (1 Introduction), p. 9 (1 Introduction), p. 4 (1 Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (42 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** There are two challenges in this benchmark: Skill Mastery (where the agent is provided data from the 5 test object triplets it is later tested on) and Skill Generalization (where ... (p. 7, 1 Introduction).
- **Actual contribution:** During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results that we present here. (p. 4, 1 Introduction).
- **Evaluation boundary:** Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained on 35k expert episodes (upper bound). ... (p. 12, Figure/Table caption).
- **Explicit failure boundary:** After this point (at 5000), performance degrades slightly but does not drop far below the expert's performance. (p. 12, 1 Introduction).

## 원문과 공개 자료

- TMLR 게재 표제면에 따라 세 저자의 발음 구별 기호를 복원했다. [표제면](https://arxiv.org/pdf/2205.06175v3#page=1)
