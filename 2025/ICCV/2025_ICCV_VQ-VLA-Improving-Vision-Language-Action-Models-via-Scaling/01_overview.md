# VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.를 문제로 두고, In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers can be effectively scaled by leveraging large-scale ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce an innovative vector quantization based action tokenizer built upon the largest-scale action trajectory dataset to date, leveraging over 100 times ...
- **p. 1 / Abstract - extractive body cue:** This extensive dataset enables our tokenizer to capture rich spatiotemporal dynamics, resulting in a model that not only accelerates inference but also generates smoother and ...
- **p. 1 / Abstract - extractive body cue:** Once trained, the tokenizer can be seamlessly adapted to a wide range of downstream tasks in a zero-shot manner, from short-horizon reactive behaviors to long-horizon ...
- **p. 1 / Abstract - extractive body cue:** A key finding of our work is that the domain gap between synthetic and real action trajectories is marginal, allowing us to effectively utilize a ...
- **p. 1 / Abstract - extractive body cue:** To validate our approach, we conducted extensive experiments in both simulated environments and on real robotic platforms.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers ...
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, we propose a convolutional residual VQVAE [5, 28, 52] framework for training action tokenizers.
- **p. 1 / 1. Introduction - extractive body cue:** To effectively train the model, we propose a progressive training strategy: Initially, we train the tokenizer on realworld robotic datasets, such as OpenX-Embodiment [34], which ...
- **p. 2 / 1. Introduction - extractive body cue:** Compared to previous approaches that typically rely on training with single-task datasets, our method expands the tokenizer training dataset by more than 100 times, effectively ...
- **p. 3 / 3.3. Training Residual VQ-VAE - extractive body cue:** To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into the ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive body cue:** Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE encoder ϕ(·), generating ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive body cue:** By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures stable loss convergence ...
- **p. 3 / 3. Methods - extractive body cue:** Conv Residual VQ Encoder � Action sequence Conv Residual VQ Decoder � � q(�) Action Reconstruction Quantizer ⊕ - + Quantizer ⊕ - + VQVAE ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences. | image/video, language instruction, proprioception과 history | p. 2 (3. Methods), p. 3 (3. Methods) |
| State/latent | frames, action, prediction, vision-language, task, mapping, input, observation, images, natural, language, instructions | language-grounded task state와 action-policy context | p. 2 (3. Methods), p. 3 (3. Methods), p. 4 (3.3. Training Residual VQ-VAE) |
| Output/action | A: Input image Language Instruction VQ Decoder � language tokenizer task: Put all cups into the basket predicted robot actions XYZ positions, Euler angles, gripper states Lora Figure 1. | continuous action, pose 또는 action chunk | p. 3 (3. Methods), p. 4 (3.3. Training Residual VQ-VAE), p. 3 (3.2. Action Tokenizer via Residual VQ-VAE) |
| Objective/outcome | To train the framework, we minimize the total loss L, a weighted combination of reconstruction loss Lrec, vector quantization (VQ) loss Lcodebook, and commitment loss Lcommit: L =∥at:t+n -ˆat:t+n∥2 2 + λ ... | instruction following, task success, generalization과 latency | p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3. Methods) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers ...
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, we propose a convolutional residual VQVAE [5, 28, 52] framework for training action tokenizers.
- **p. 1 / 1. Introduction - extractive body cue:** To effectively train the model, we propose a progressive training strategy: Initially, we train the tokenizer on realworld robotic datasets, such as OpenX-Embodiment [34], which ...
- **p. 2 / 1. Introduction - extractive body cue:** Compared to previous approaches that typically rely on training with single-task datasets, our method expands the tokenizer training dataset by more than 100 times, effectively ...
- **p. 3 / 3.3. Training Residual VQ-VAE - extractive body cue:** To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into the ...
- **p. 5 / 4.1.2. Effectiveness of Conv Residual VQ-VAE - extractive body cue:** The evaluation results of residual VQ-VAE architectures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on the full LIBERO ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Real-world experimental results: We compare the performance of Baseline, VQO, VQO+L, and VQO+L+M on both short-horizon and long-horizon tasks. In terms of the ...
- **p. 6 / 4.2.3. Performance on Long-Horizon Tasks - extractive body cue:** VQ-VLA demonstrates outstanding performance on longhorizon tasks ("Put all cups in the basket" and "Put the toy into the drawer"), significantly outperforming baseline model in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption) |
| Embodiment/environment | In simulation, evaluations are performed on the LIBERO90 benchmark within the LIBERO dataset. | hardware/simulator version and reset protocol | p. 6 (4.2.1. Experiment Setup), p. 4 (4.1.1. Experiment Setup) |
| Dataset/benchmark | Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity of data types, which effectively enhances the model's ... | role, split, size and leakage | p. 6 (4.2.1. Experiment Setup), p. 4 (4.1.1. Experiment Setup), p. 7 (4.2.4. Sim&Real Domain Gap Analysis), p. 4 (4.1.1. Experiment Setup) |
| Metric | In the "Pull out a tissue paper" task, which tests the robot's performance in high-precision dynamic operations (as this task requires continuous, fine-grained grasping and pulling motions), the baseline model achieved only ... | definition, denominator, direction and uncertainty | p. 6 (4.2.2. Performance on Short-Horizon Tasks), p. 6 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE) |
| Baseline/ablation | Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness of incorporating synthetic data during training without compromising real-world performance. compared to baseline ... | fair input/data/compute/action matching | p. 7 (4.2.3. Performance on Long-Horizon Tasks), p. 5 (4.1.3. Scaling Data Improves VQ-VAE Action Tokenizer), p. 6 (4.2.3. Performance on Long-Horizon Tasks) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Limitations and Future Works - extractive body cue:** Despite these promising results, there still remain some limitations and opportunities for future work.
- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** 4) Flip the pot upright: We set a flipped pot on the platform, the robot need to flip and upright a fallen cooking pot.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity of ...
- **p. 6 / 4.2.3. Performance on Long-Horizon Tasks - extractive body cue:** In contrast, the VQO+L+M model successfully opened the drawer in all test cases, demonstrating its robustness and reliability in handling complex sequential tasks.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.를 문제로 두고, In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers can be effectively scaled by leveraging large-scale ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3.3. Training Residual VQ-VAE), p. 3 (3. Methods), p. 2 (3. Methods) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
