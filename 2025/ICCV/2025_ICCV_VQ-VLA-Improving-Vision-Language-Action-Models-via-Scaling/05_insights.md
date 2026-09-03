# Insights — VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers ...
- **p. 1 / 1. Introduction - extractive body cue:** Specifically, we propose a convolutional residual VQVAE [5, 28, 52] framework for training action tokenizers.
- **p. 1 / 1. Introduction - extractive body cue:** To effectively train the model, we propose a progressive training strategy: Initially, we train the tokenizer on realworld robotic datasets, such as OpenX-Embodiment [34], which ...
- **p. 2 / 1. Introduction - extractive body cue:** Compared to previous approaches that typically rely on training with single-task datasets, our method expands the tokenizer training dataset by more than 100 times, effectively ...
- **p. 3 / 3.3. Training Residual VQ-VAE - extractive body cue:** To improve the encoder's ability to process temporal and spatial information, we introduced two types of embeddings before the action sequences are passed into the ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive body cue:** Instead of discretizing action sequences into uniform bins, the action sequence at:t+n is first processed through a pre-trained and frozen Residual VQVAE encoder ϕ(·), generating ...
- **p. 4 / 3.4. Integrating Residual VQ-VAE as Action Tok - extractive body cue:** By leveraging hierarchical quantization with non-overlapping token ID ranges, the model achieves better action representation, avoids semantic confusion between layers, and ensures stable loss convergence ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.3. Training Residual VQ-VAE), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we delve deeper into the potential of action tokenization, with a specific emphasis on its scalability and accuracy.
- **p. 8 / 5. Limitations and Future Works - extractive body cue:** Despite these promising results, there still remain some limitations and opportunities for future work.
- **p. 6 / 4.2.1. Experiment Setup - extractive body cue:** 4) Flip the pot upright: We set a flipped pot on the platform, the robot need to flip and upright a fallen cooking pot.
- **p. 7 / 4.2.4. Sim&Real Domain Gap Analysis - extractive body cue:** Although real-world data may contain noise, the inclusion of Open X-Embodiment data as a real-world dataset expands the data sources and enriches the diversity of ...
- **p. 6 / 4.2.3. Performance on Long-Horizon Tasks - extractive body cue:** In contrast, the VQO+L+M model successfully opened the drawer in all test cases, demonstrating its robustness and reliability in handling complex sequential tasks.
- **Boundary to test:** Despite these promising results, there still remain some limitations and opportunities for future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers can be effectively scaled by leveraging large-scale ... | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Reported outcome | The evaluation results of residual VQ-VAE architectures.The results demonstrate that the Conv Residual VQ-VAE outperforms the MLP-based version, particularly when trained on the full LIBERO dataset (ALL-LIBERO), highlighting its ability ... | p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption) |
| Failure/limitation | Despite these promising results, there still remain some limitations and opportunities for future work. | p. 8 (5. Limitations and Future Works), p. 6 (4.2.1. Experiment Setup) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 The method frames action prediction as a vision-language task, mapping input observation images and natural language instructions to discrete robot action sequences.를 A: Input image Language Instruction VQ Decoder � language tokenizer task: Put all cups into the basket predicted robot actions XYZ positions, Euler angles, gripper states Lora Figure 1.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Despite these promising results, there still remain some limitations and opportunities for future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We propose a general convolutional residual VQ-VAEbased framework for action tokenizers. • We demonstrate that action tokenizers can be effectively scaled by leveraging large-scale ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Despite these promising results, there still remain some limitations and opportunities for future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In simulation, evaluations are performed on the LIBERO90 benchmark within the LIBERO dataset..
3. Compare against the body-reported baseline or a matched simpler baseline: Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness of incorporating synthetic data during training without compromising real-world performance. compared to baseline ....
4. Report the body metric and its denominator/aggregation: In the "Pull out a tissue paper" task, which tests the robot's performance in high-precision dynamic operations (as this task requires continuous, fine-grained grasping and pulling motions), the baseline model achieved only ....
5. Re-run the body-reported ablation/failure condition: To evaluate the impact of embeddings, we conducted an ablation study comparing the model's performance with and without embeddings..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 4 (3.4. Integrating Residual VQ-VAE as Action Tok), p. 3 (3.3. Training Residual VQ-VAE); the primary result is directionally consistent at p. 5 (4.1.2. Effectiveness of Conv Residual VQ-VAE), p. 7 (Figure/Table caption), p. 6 (4.2.3. Performance on Long-Horizon Tasks); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 Additionally, the results show that VQO+L+M outperforms VQO+L, which in turn outperforms VQO, indicating the effectiveness ... 대비 In the "Pull out a tissue paper" task, which tests the robot's performance in high-precision dynamic operations (as ...을 개선하고, Despite these promising results, there still remain some limitations and opportunities for future work. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
