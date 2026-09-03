# RoboOmni: Actions Are Just Another Modality for Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=qdXOfyGMuB.
> PDF retrieval source: https://openreview.net/pdf/b090562c668703f4568061335c66e0e592e16d9d.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics
- Official paper: https://openreview.net/forum?id=qdXOfyGMuB
- Full-text retrieval: https://openreview.net/pdf/b090562c668703f4568061335c66e0e592e16d9d.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in their parent models.를 문제로 두고, To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Integrating Vision-Language Models (VLMs) into robotics has facilitated the development of generalizable Vision-Language Action (VLA) policies.
- **p. 1 / Abstract - extractive body cue:** However, unified discrete frameworks lag behind decoupled continuous designs due to limitations in action chunking and temporal modeling.
- **p. 1 / Abstract - extractive body cue:** To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.
- **p. 1 / Abstract - extractive body cue:** Challenging the assumption that continuous modeling is essential for high-performance manipulation, RoboOmni demonstrates that actions are just another modality capable of being effectively modeled discretely.
- **p. 1 / Abstract - extractive body cue:** At the core of our method is Multi-Token Action Prediction (MTAP), which integrates action chunking directly into the discrete tokenizer.
- **p. 1 / 1. Introduction - extractive body cue:** However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in ...
- **p. 1 / 1. Introduction - extractive body cue:** The generalization gap between the VLM backbone and the downstream VLA is tied to the underlying architectural design and training paradigm (Li et al., 2026).

## Core Idea

- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.
- **p. 2 / 1. Introduction - extractive body cue:** This design enables long-context, multimodal co-training and allows the model to explicitly reason over historical observations and actions.
- **p. 1 / 1. Introduction - extractive body cue:** To overcome these limitations, we present RoboOmni, a 1
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we introduce Multi-Token Action Prediction (MTAP), which performs parallel decoding of H actions by repeating only the last layer for action tokens, inspired by ...
- **p. 5 / 3.2. Multi-Modal Action Co-Training - extractive body cue:** To encourage short-horizon temporal reasoning and motion understanding, we introduce a 2D end-effector trace prediction task inspired by (Li et al., 2025).
- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** Each state zk is then passed through a shared language model head (LMHead) to produce logits for the future action 3
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A).
- **p. 4 / 3.1. MTAP for Action Chunking - extractive body cue:** Therefore, we employ MTAP primarily as an auxiliary training objective to facilitate backbone modeling of the complex frequency tokens, rather than solely for inference acceleration.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The model processes multi-modal interleaved input sequences comprising visual observations (V ), text instructions (T), robot states (S), and actions (A). | image/video, language instruction, proprioception과 history | p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training) |
| State/latent | model, processes, multi-modal, interleaved, input, sequences, comprising, visual, observations, text, instructions, robot | language-grounded task state와 action-policy context | p. 4 (3.1. MTAP for Action Chunking), p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM) |
| Output/action | RoboOmni: Actions Are Just Another Modality for Vision-Language Models clude Visual inputs, Text inputs, Bounding Box and Pixel Point, as well as Robot State and Action modalities. | continuous action, pose 또는 action chunk | p. 5 (3.2. Multi-Modal Action Co-Training), p. 5 (3.3. Training VLA as VLM), p. 2 (1. Introduction) |
| Objective/outcome | By jointly optimizing for these diverse objectives alongside the primary action prediction task, the model learns more robust and generalizable representations. | instruction following, task success, generalization과 latency | p. 5 (3.3. Training VLA as VLM), p. 4 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking) |

## Main Claims and Actual Contribution

- **p. 3 / 3.1. MTAP for Action Chunking - extractive body cue:** To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.
- **p. 2 / 1. Introduction - extractive body cue:** This design enables long-context, multimodal co-training and allows the model to explicitly reason over historical observations and actions.
- **p. 1 / 1. Introduction - extractive body cue:** To overcome these limitations, we present RoboOmni, a 1
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we introduce Multi-Token Action Prediction (MTAP), which performs parallel decoding of H actions by repeating only the last layer for action tokens, inspired by ...
- **p. 5 / 3.2. Multi-Modal Action Co-Training - extractive body cue:** To encourage short-horizon temporal reasoning and motion understanding, we introduce a 2D end-effector trace prediction task inspired by (Li et al., 2025).
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** On average, RoboOmni achieves a 91% success rate, significantly surpassing π0-FAST (68%) and RoboVLMs (60%).
- **p. 7 / 4.4. Ablation Study - extractive body cue:** For the FAST tokenizer, enabling MTAP improves the 5-task success rate from 80.1% to 88.1%.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Comparison of success rates in the real-world setting. RoboOmni consistently outperforms baselines, including π0-FAST and RoboVLMs, particularly in the challenging Unseen Objects setting. ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Real Robot Experiments), p. 7 (4.4. Ablation Study) |
| Embodiment/environment | We evaluate RoboOmni across three complementary settings: (1) long-horizon multi-task manipulation on the CALVIN benchmark, (2) Google Robot tasks in the SimplerEnv simulator, and (3) real-world robot experiments. | hardware/simulator version and reset protocol | p. 5 (4. Experiment), p. 6 (4.2. Evaluation on SimplerEnv) |
| Dataset/benchmark | CALVIN (Mees et al., 2022b) is a simulation benchmark for multi-task tabletop manipulation. | role, split, size and leakage | p. 5 (4. Experiment), p. 6 (4.2. Evaluation on SimplerEnv), p. 5 (4.1. Evaluation on Calvin), p. 7 (4.3. Real Robot Experiments) |
| Metric | Ablating the history length reveals that increasing the window size from 1 to 5 yields a significant performance gain (81.3% to 83.4% 5-task success rate), while a further increase to 10 offers ... | definition, denominator, direction and uncertainty | p. 8 (4.4. Ablation Study), p. 7 (4.3. Real Robot Experiments), p. 7 (4.2. Evaluation on SimplerEnv) |
| Baseline/ablation | Figure 3. Comparison of success rates in the real-world setting. RoboOmni consistently outperforms baselines, including π0-FAST and RoboVLMs, particularly in the challenging Unseen Objects setting. ms/action. This not only makes the Bin ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 6 (4.2. Evaluation on SimplerEnv), p. 7 (4.2. Evaluation on SimplerEnv) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** The table evaluates models on two settings: in-distribution performance (Train: ABCD, Eval: D) and out-of-distribution generalization (Train: ABC, Eval: D).
- **p. 6 / 4.1. Evaluation on Calvin - extractive body cue:** Notably, the FAST variant exhibits superior out-of-distribution generalization (ABC→D), suggesting the frequency-domain representation effectively offloads temporal modeling pressure from the backbone.
- **p. 7 / 4.3. Real Robot Experiments - extractive body cue:** Robust Generalization to Novel Scenarios.
- **p. 7 / 4.2. Evaluation on SimplerEnv - extractive body cue:** RoboOmni demonstrates superior robustness to visual domain shifts compared to baselines.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Finally, removing any of our core training strategies degrades performance.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** A similar trend is observed for the Bin tokenizer, where performance is highest with 128 bins (83.7%) and 256 bins (83.4%), but degrades significantly when ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in their parent models.를 문제로 두고, To overcome these challenges, we introduce a versatile Multi-Token Action Prediction (MTAP) framework that enables efficient, parallelized action prediction within a unified discrete architecture.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. MTAP for Action Chunking), p. 3 (3.1. MTAP for Action Chunking), p. 4 (3.1. MTAP for Action Chunking) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
