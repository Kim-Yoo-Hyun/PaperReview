# Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p017.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p017.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency
- Official paper: https://www.roboticsproceedings.org/rss21/p017.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p017.pdf
- Code/Project: https://openvla-oft.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable for high-frequency control, and unreliable task execution on bimanual mani ...를 문제로 두고, In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent vision-language-action models (VLAS) build ‘upon pretrained vision-language model and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization.
- **p. 1 / Abstract - extractive body cue:** Despite these successes, VLAS struggle with novel robot setups and require fine= tuning to achieve good performance, yet how to most effectively fine-tune them is ...
- **p. 1 / Abstract - extractive body cue:** In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations,
- **p. 1 / Abstract - extractive body cue:** ‘decoding, action chunking, a conti and a simple L1 regression-based lea ference efficiency, policy performance, and flex inthe rodel's input-output opecicatios.
- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 3 / A. VIA Fine-Tuning Design Decisions - extractive body cue:** Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable for high-frequency control, ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** We address this gap by exploring VLA adaptation design decisions for fast inference and reliable task execution on a real-world bimanual ‘manipulator with a 25 ...

## Core Idea

- **p. 3 / 1. Iyrropucrion - extractive body cue:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.
- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, ...
- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** With 25-timestep action ‘chunks, OpenVLA-OFT+ achieves 43% faster throughput than base OpenVLA, demonstrating that our new fine-tuning recipe ‘enables real-time robot control with strong task ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** For Diffusion Policy training, we use the DROID implementation [22], which conditions action predictions on DistilBERT [42] language embeddings of the task description, We list ...
- **p. 7 / 3) LI regression objective - extractive body cue:** Given that the alternative fine-tuning formulation, along with additional model inputs and outputs, induces a distri bution shift between the base VLA's pretraining and finetuning, ...
- **p. 14 / A. Model Architecture Details - extractive body cue:** These projected features are concatenated with language ‘embeddings along the sequence dimension before being pro- ‘cessed by the Llama-2 decoder to output a 7-limensional robot, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | ‘decoding, action chunking, a conti and a simple L1 regression-based lea ference efficiency, policy performance, and flex inthe rodel's input-output opecicatios. | image/video, language instruction, proprioception과 history | p. 1 (Abstract), p. 7 (3) LI regression objective) |
| State/latent | decoding, action, chunking, conti, simple, regression-based, ference, efficiency, policy, performance, flex, inthe | language-grounded task state와 action-policy context | p. 1 (Abstract), p. 7 (3) LI regression objective), p. 1 (1. Iyrropucrion) |
| Output/action | This setup differs significantly from OpenVLA's pretraining, which includes single-arm robot data only, a single camera viewpoint from 4 third-person camera, no robot state inputs, low-frequency control (3-10 Hz), and relative end-effec ... | continuous action, pose 또는 action chunk | p. 7 (3) LI regression objective), p. 1 (1. Iyrropucrion), p. 4 (B. Implementing Alternative Design Components) |
| Objective/outcome | We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate decay strategy (again 10% reduction, but after SOK ... | instruction following, task success, generalization과 latency | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (3) LI regression objective), p. 14 (B. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 3 / 1. Iyrropucrion - extractive body cue:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.
- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, ...
- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** With 25-timestep action ‘chunks, OpenVLA-OFT+ achieves 43% faster throughput than base OpenVLA, demonstrating that our new fine-tuning recipe ‘enables real-time robot control with strong task ...
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** Finally, OpenVLA-OFT+ achieves the highest performance across both task execution and language following (see Figure 7 for examples of successful task rollouts).
- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** For methods using action chunking, we set chunk size to A' = 8 to match the Diffusion Policy baseline [5], and execute full chunks before ...
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** ACT, while able to complete basic tasks, produces less precise actions and achieves the lowest overall performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup) |
| Embodiment/environment | We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, robot state, task annotations, and delta end-effector pose actions. | hardware/simulator version and reset protocol | p. 5 (A. LIBERO Experimental Setup), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| Dataset/benchmark | datasets (6K episodes and 8K hours of bimanual data, respec tively). ‘This suggests that the fine-tuning technique can be more crucial than pretraining data coverage for downstream performance. | role, split, size and leakage | p. 5 (A. LIBERO Experimental Setup), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup) |
| Metric | Success rates in approaching for language-dependent tasks. | definition, denominator, direction and uncertainty | p. 9 (C. ALOHA Task Performance Results), p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results) |
| Baseline/ablation | Fine-tuned VLA pol cies generally outperform the from-scratch baselines in both task execution and language following, consistent with prior findings (27, 3]. | fair input/data/compute/action matching | p. 8 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 5 (A. LIBERO Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown ...
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** Among VLAs, we observe distinct charac teristics: RDT-IB achieves good language following through its "Alternating Condition Injection" scheme (27], but shows a limitation in handling ...
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** Top In some cases, RDT-IB fails 10 respond to missed howl placement, coatiauing 10 pour iagredieats into empey space.
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate decay ...
- **p. 10 / VII. Discussion - extractive body cue:** While LI regression may help smoothen out noise in training demonstrations by encouraging the policy to learn the median mode in demonstrated actions, it may ...
- **p. 14 / B. Implementation Details - extractive body cue:** + 4-layer noise predictor with same MLP architecture as

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable for high-frequency control, and unreliable task execution on bimanual mani ...를 문제로 두고, In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (A. VIA Fine-Tuning Design Decisions), p. 2 (1. Iyrropucrion), p. 3 (A. VIA Fine-Tuning Design Decisions), p. 4 (B. Implementing Alternative Design Components), p. 1 (1. Iyrropucrion), p. 14 (B. Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
