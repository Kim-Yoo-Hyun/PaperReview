# Insights — OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=UHF0km7R5M; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/167304. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language ...
- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.
- **p. 3 / 3. Method - extractive body cue:** We propose OTTER, a vision-language-action model for learning a robot manipulation policy through extraction of text-aware vision features from a pre-trained VLM.
- **p. 1 / 1. Introduction - extractive body cue:** OTTER exhibits better zero-shot generalization to unseen objects, maintaining strong performance across a variety of novel tasks.
- **p. 3 / 3. Method - extractive body cue:** We first describe how OTTER utilizes the vision-language alignment of pre-trained vision and language encoders to extract text-aware vision features, then provide a more detailed ...
- **p. 4 / 3.2. Model Architecture - extractive body cue:** Policy Network and Action Head OTTER uses a transformer as the policy network, consisting of 4 layers and 8 heads, with a hidden dimension of ...
- **p. 5 / 3.2. Model Architecture - extractive body cue:** OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction Figure 4: Example scenes in the simulation (left) and in the physical environments (right) using a ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction), p. 3 (3. Method), p. 4 (3.2. Model Architecture)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** This approach requires the policy network to connect the vision and language information and conduct precise robot control, which often presents significant challenges, especially in ...
- **p. 2 / 1. Introduction - extractive body cue:** Both physical and simulation experiments demonstrate that OTTER outperforms existing VLA models, showing strong generalization to novel objects and environments with less performance degradation (Figure ...
- **p. 1 / 1. Introduction - extractive body cue:** OTTER exhibits better zero-shot generalization to unseen objects, maintaining strong performance across a variety of novel tasks.
- **p. 2 / 1. Introduction - extractive body cue:** We propose OTTER, a VLA model that leverages the semantic alignment capabilities of pre-trained VLMs for better generalization.
- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.
- **p. 6 / 5.1. Real-world Experiments - extractive body cue:** For a fair comparison, we extended the context history length of Octo to 10 (Octo cannot exceed a context length of 10 due to its ...
- **p. 7 / 5.1. Real-world Experiments - extractive body cue:** Finetuned π0-Fast-Droid achieves non-zero success rate on Drawer and Poking primitives, but still fails on the pouring primitive.
- **Boundary to test:** As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language instructions. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | OTTER achieves a similar success rate on the in-distribution training tasks and unseen tasks, significantly outperforming the baselines, highlighting the benefits of extracting text-aware visual features and a frozen pre-trained VLM. la ... | p. 6 (4.2. Baselines), p. 7 (Figure/Table caption) |
| Failure/limitation | As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length. | p. 6 (5.1. Real-world Experiments), p. 6 (5.1. Real-world Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Different input modalities are usually encoded into separate tokens: multi-view images encoded via visual feature extractors, along with tokenized language instructions, optionally with the robot's proprioceptive states, are fed into a ...를 This token serves as input to a policy network for action prediction.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To this end, we propose OTTER, a novel VLA architecture that freezes pre-trained vision and language encoders and extracts taskrelevant visual features guided by language instructions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** As OpenVLA has many tokens per timestep, its context length cannot be extended and we use its default context length.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We collect robotic datasets on multi-task scenes using a Franka robot, where there are multiple tasks that can be completed in the same scene..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks we constructed, each task 50 trials. The numbers ....
4. Report the body metric and its denominator/aggregation: The overall performance is measured by calculating the average success rate with standard error across all trials for the training and unseen tasks..
5. Re-run the body-reported ablation/failure condition: Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks in LIBERO- Spatial/Object/Goal and on 10 unseen tasks we constructed, each task 50 trials. The numbers ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3. Method), p. 3 (3. Method), p. 4 (3.2. Model Architecture); the primary result is directionally consistent at p. 6 (4.2. Baselines), p. 7 (Figure/Table caption), p. 6 (5.1. Real-world Experiments); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 OTTER, novel, VLA mechanism이 Table 3: Simulation results on LIBERO. We evaluate OTTER and other baselines on 30 in-distribution tasks ... 대비 The overall performance is measured by calculating the average success rate with standard error across all trials for ...을 개선하고, As OpenVLA has many tokens per timestep, its context length cannot be extended and we use ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
