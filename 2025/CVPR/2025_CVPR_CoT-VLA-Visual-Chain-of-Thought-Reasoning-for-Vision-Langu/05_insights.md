# Insights — CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. ...
- **p. 2 / 1. Introduction - extractive body cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** This enables autoregressive image and video generation while significantly enhancing the understanding capabilities of VLMs that leverage discrete visual features.
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** We use the VILA-U model trained on 256 × 256 resolution images, where each image is encoded into 16 × 16 × 4 tokens with ...
- **p. 4 / 3.2. The Base Vision-Language Model - extractive body cue:** VILA-U utilizes residual quantization [32] to improve the representational capacity of discrete visual features - incorporating a depth transformer, as introduced in RQ-VAE [32], to ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive body cue:** Algorithm 1 CoT-VLA test-time closed-loop control Require: CoT-VLA Model Pθ, initial state sobs 0 , language instruction l 0: t ←0 0: while True do ...
- **p. 5 / 10. For complete dataset specifications and training hyper - extractive body cue:** During this phase, we optimize the LLM backbone, projector, and depth transformer while keeping the vision tower frozen, maintaining the same training setup as the ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. The Base Vision-Language Model), p. 4 (3.2. The Base Vision-Language Model), p. 4 (3.2. The Base Vision-Language Model), p. 5 (10. For complete dataset specifications and training hyper)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** We outline the robot arm for better visualization. structions, leading to better generalization capabilities when fine-tuned for downstream testing scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** Prior VLA models (top) directly predict robot actions from task inputs without explicit reasoning steps and only use action-annotated robot demonstration data for training.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive experiments in both simulation benchmarks [37] and real-world experiments[48, 60], we demonstrate that our visual chain-of-thought reasoning helps improve policy performance compared to ...
- **p. 2 / 1. Introduction - extractive body cue:** Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual ...
- **p. 8 / 4.4. Better Visual Reasoning Helps - extractive body cue:** Conclusion, Limitations and Future Work In this work, we introduce CoT-VLA, bridging visionlanguage-action models with chain-of-thought reasoning by introducing intermediate visual goals as explicit reasoning ...
- **p. 6 / 4.2. Evaluations Results - extractive body cue:** By analyzing rollout videos of failure cases, we found that baseline methods occasionally overfit to visual cues while disregarding language instructions.
- **Boundary to test:** Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual reasoning (simulated by ground-truth goals) ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. • We introduce a system CoT-VLA that ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 1. LIBERO benchmark experimental results. For each task suite (Spatial, Object, Goal, Long), we report the average success rate and standard error across 3 seeds with 500 episodes each. CoT-VLA achieves ... | p. 5 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual reasoning (simulated by ground-truth goals) ... | p. 8 (Figure/Table caption), p. 8 (4.4. Better Visual Reasoning Helps) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 One promising direction is vision-language-action (VLA) models, which leverage the rich understanding capabilities of pretrained vision-language models (VLMs) to map natural language instructions and visual observations to robot actions ...를 Rather than directly predicting actions, our method first generates a subgoal image that represents the robot's planned state in pixel space, and then conditions its action on both the current observation and ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual reasoning (simulated by ground-truth goals) ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our key contributions include: • We introduce a method of visual chain-of-thought reasoning through subgoal image generation as an intermediate reasoning step for robotic control. • We introduce a system CoT-VLA that ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Chain-of-Thought, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal images on out-of-distribution tasks. Results demonstrate that improved visual reasoning (simulated by ground-truth goals) ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We conduct evaluations across three complementary settings: the LIBERO benchmark [37] for evaluation in simulation environments, the Bridge-V2 platform [60] with its dataset of 45k robot demonstrations, and the Franka-Tabletop setup wit ....
3. Compare against the body-reported baseline or a matched simpler baseline: Our experiments aim to addresses following questions: • How does our system perform compared to state-of-the-art baselines across multiple benchmarks and embodiments?.
4. Report the body metric and its denominator/aggregation: Success rates are reported with means and standard error..
5. Re-run the body-reported ablation/failure condition: Ablation studies of CoT-VLA components. a) Results on LIBERO-Spatial and LIBERO-Goal benchmarks demonstrate the effectiveness of three components: action chunking, hybrid attention, and visual chain-of-thought reasoning. b) Pretraining ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. The Base Vision-Language Model), p. 4 (3.2. The Base Vision-Language Model), p. 5 (10. For complete dataset specifications and training hyper); the primary result is directionally consistent at p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.2. Evaluations Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, include, introduce mechanism이 Our experiments aim to addresses following questions: • How does our system perform compared to state-of-the-art ... 대비 Success rates are reported with means and standard error.을 개선하고, Table 3. Better visual reasoning helps. Success rates compar- ing CoT-VLA using generated versus ground-truth goal ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
