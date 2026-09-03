# Insights — Vision-Language-Action Instruction Tuning: From Understanding to Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=tsxwloasw5; PDF retrieval source: https://openreview.net/pdf/479b7c7653cdbe865ebb138a22008c6e15adc46f.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)).
- **p. 2 / 3. Atomic-Instruction Manipulation - extractive body cue:** To validate the performance of InstructVLA, we introduce the SimplerEnv-Instruct benchmark, a manually designed evaluation suite featuring 80 zero-shot manipulation tasks.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The first aims to retain general multimodal capabilities while learning manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation ...
- **p. 2 / 3. Atomic-Instruction Manipulation - extractive body cue:** Building on these observations, we propose InstructVLA, a generalist VLA model that extends pretrained VLMs for accurate action generation while preserving strong multimodal understanding.
- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** It takes image features from DINOv2 (Oquab et al., 2023) vision encoder, latent actions, noisy action embeddings and optional information such as proprioception, and fuses ...
- **p. 4 / 3. Atomic-Instruction Manipulation - extractive body cue:** The model produces textual outputs to preserve the strong language understanding and multimodal inference capabilities of the pretrained VLM, while subsequently generating latent action representations ...
- **Contribution anchor:** p. 4 (3. Atomic-Instruction Manipulation), p. 2 (3. Atomic-Instruction Manipulation), p. 1 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 2 (3. Atomic-Instruction Manipulation), p. 4 (3. Atomic-Instruction Manipulation)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address these challenges and utilize VLMs more effectively, prior work has primarily adopted two strategies.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Current attempts to incorporate the reasoning capabilities of VLMs into action learning face three main obstacles: (1) task interference, catastrophic forgetting (French, 1999) of multimodal ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection ...
- **p. 29 / Figure/Table caption - extractive body cue:** Figure 18: Reasoning cases in SimplerEnv-Instruct. Three cases of the VL fine-tuned OpenVLA and InstructVLA-Generalist. "SR" denotes success rate. We present three representative reasoning cases ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 19: Failure case 1 of InstructVLA. The model receives only a third-person view image as visual input, making it difficult to estimate depth or ...
- **p. 8 / 5 EXPERIMENT - extractive body cue:** However, GPT-4o faces the same challenges in accurate instruction rewriting as noted in Section 4.1, and fails to outperform InstructVLA (Generalist).
- **p. 46 / Figure/Table caption - extractive body cue:** Figure 34: Light distraction. Stable visual features from DINO and SigLIP enable the model to operate robustly under extreme out-of-distribution lighting conditions. 46
- **Boundary to test:** Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection on the table, which causes the robot ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)). | p. 4 (3. Atomic-Instruction Manipulation), p. 2 (3. Atomic-Instruction Manipulation) |
| Reported outcome | Meanwhile, InstructVLA (generalist) not only maintains strong performance on SimplerEnv's atomic instructions but also achieves a 31.7% relative improvement on SimplerEnv-Instruct over the state-of-the-art baseline (OpenVLA with GPT-4o). | p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT) |
| Failure/limitation | Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection on the table, which causes the robot ... | p. 30 (Figure/Table caption), p. 29 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Our key observation is that once the action expert has been pretrained to follow latent actions generated by the VLM, further adapting the LLM backbone enables the model to handle manipulation tasks ...를 Scenario Caption Command Rewriting Context Creation Question Answering Utility Material Appearance Situated Noval Action Long horizon Original Dataset Embodied Scene Understanding Instruction Understanding and Planning Figure 3: Vision- ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection on the table, which causes the robot ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose a unified framework that enables simultaneous multimodal reasoning and language-steered latent action planning using a single VLM (Figure 2 (1) and (2)).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to the real-to-sim gap, specifically the absence of arm reflection on the table, which causes the robot ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: (b) SimplerEnv: This benchmark (Li et al., 2024d) provides real-to-sim evaluation on large-scale manipulation datasets, incorporating visual matching and variance aggregation to assess generalization..
3. Compare against the body-reported baseline or a matched simpler baseline: In Table 2, InstructVLA (expert) outperforms the expert baseline SpatialVLA by 33.3% on SimplerEnv..
4. Report the body metric and its denominator/aggregation: Table 10: LIBERO benchmark results. We present the success rate and standard error for each method across four task suites, which are averaged over three random seeds with 500 trials. "KI" denotes ....
5. Re-run the body-reported ablation/failure condition: Figure 11: Test-time tinking and dual-frequency evaluation. "Expert" refers to the model after action pretraining, while "Generalist" denotes the model after VLA-IT tuning. For dual-frequency evaluation, the horizontal axis represents t ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3. Atomic-Instruction Manipulation), p. 4 (3. Atomic-Instruction Manipulation), p. 2 (3. Atomic-Instruction Manipulation); the primary result is directionally consistent at p. 8 (5 EXPERIMENT), p. 9 (5 EXPERIMENT), p. 30 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 unified, framework, enables mechanism이 In Table 2, InstructVLA (expert) outperforms the expert baseline SpatialVLA by 33.3% on SimplerEnv. 대비 Table 10: LIBERO benchmark results. We present the success rate and standard error for each method across four ...을 개선하고, Figure 20: Failure case 2 of InstructVLA. The model fails to accurately estimate depth due to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
