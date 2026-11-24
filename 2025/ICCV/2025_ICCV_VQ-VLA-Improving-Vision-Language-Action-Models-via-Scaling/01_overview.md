# VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Yating Wang, Haoyi Zhu, Mingyu Liu, Jiange Yang, Hao-Shu Fang, Tong He
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

VQ-VLA는 연속적인 로봇 행동 구간을 벡터 양자화하고 합성 궤적과 실제 궤적으로 토크나이저를 학습한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=1)

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
- 그림 1에서 합성곱 인코더는 행동 구간을 잠재 표현으로 바꾸고, 잔차 양자화기와 디코더는 이산 코드로 연속 행동을 복원한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=3)

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences. | image/video, language instruction, proprioception과 history | p. 2 (3. Methods), p. 3 (3. Methods) |
| State/latent | frames, action, prediction, vision-language, task, mapping, input, observation, images, natural, language, instructions | language-grounded task state와 action-policy context | p. 2 (3. Methods), p. 3 (3. Methods), p. 4 (3.3. Training Residual VQ-VAE) |
| Output/action | 디코더가 위치·오일러 각·그리퍼 상태로 구성된 행동열을 복원한다. | 연속 행동 구간 | 그림 1에서 출력 표현을 확인할 수 있다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=3) |
| Objective/outcome | To train the framework, we minimize the total loss L, a weighted combination of reconstruction loss Lrec, vector quantization (VQ) loss Lcodebook, and commitment loss Lcommit: L =∥at:t+n -ˆat:t+n∥2 2 + λ ... | instruction following, task success, generalization과 latency | p. 3 (3.2. Action Tokenizer via Residual VQ-VAE), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3. Methods) |

## Main Claims and Actual Contribution

- 잔차 벡터 양자화 자동인코더가 여러 시점의 행동을 짧은 이산 코드열로 표현하고 다시 연속 행동으로 복원한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=4)
- 행동 복원과 정책의 실제 과제 성공을 별도로 측정하고 궤적 자료 규모와 행동 청크 구성의 영향을 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=5) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3.3. Training Residual VQ-VAE), p. 3 (3. Methods), p. 2 (3. Methods)이다.
