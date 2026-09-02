# Insights — RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1.1 Hz - extractive body cue:** In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, ...
- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 2 / 1.1 Hz - extractive body cue:** Subsequently, we introduce an efficient fine-tuning strategy to equip RoboMamba with pose prediction abilities, requiring a few dozen minutes to fine-tune a simple policy head ...
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba Language Model Tokenizer ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 3 / 1.1 Hz - extractive body cue:** Moreover, RoboMamba achieves an inference speed that is 3 times faster than previous robotic VLA models [29, 15].
- **Contribution anchor:** p. 3 (1.1 Hz), p. 2 (1.1 Hz), p. 2 (1.1 Hz), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract)

### Strongest assumption and failure boundary

- **p. 2 / 1.1 Hz - extractive body cue:** While existing MLLM-based policies can handle a range of basic tasks, they still face challenges in two aspects.
- **p. 2 / 1.1 Hz - extractive body cue:** As shown in Figure 1 (reasoning example), this deficiency presents challenges for fine-tuned robot MLLMs when they encounter complex reasoning tasks.
- **p. 1 / 1 Introduction - extractive body cue:** The scaling up of data has significantly propelled research on Large Language Models (LLMs) [1-3], showcasing notable advancements in reasoning and generalization abilities within Natural ...
- **p. 10 / 4 Experiment - extractive body cue:** Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances ...
- **p. 10 / 4 Experiment - extractive body cue:** Meanwhile, as shown in Figure 5, we also visualize the failure cases of RoboMamba's predictions in both reasoning and manipulation tasks.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 6: The visualization of reasoning failure cases. In the bottom right corner of the image, we re-select the qualitative results from our real-world demonstration. ...
- **p. 17 / A Appendix - extractive body cue:** Due to space limitations, we provide additional details of the proposed method in this supplementary material.
- **Boundary to test:** Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances the robustness of future manipulation pose generation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, which possesses visual common sense and robotic-related ... | p. 3 (1.1 Hz), p. 2 (1.1 Hz) |
| Reported outcome | As shown in Table 2, our RoboMamba achieves a 7.0% improvement on seen tasks and a 2.0% improvement on unseen tasks compared to the previous SOTA ManipLLM. | p. 8 (4 Experiment), p. 9 (4 Experiment) |
| Failure/limitation | Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances the robustness of future manipulation pose generation. | p. 10 (4 Experiment), p. 10 (4 Experiment) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, which possesses visual common sense and robotic-related ...를 With its strong reasoning abilities, RoboMamba achieves state-of-the-art (SOTA) manipulation performance in the SAPIEN simulation [28], requiring only a 7MB policy head and a few dozen minutes of fine-tuning on a single ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances the robustness of future manipulation pose generation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, which possesses visual common sense and robotic-related ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, Mamba, SE(3) pose, efficient inference, manipulation`.
- **Reading predecessor in the generated track queue:** Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Latent Action Pretraining from Videos (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Prediction of past and future actions is crucial in robotic manipulation, as it not only enables effective rethinking of past failure actions but also enhances the robustness of future manipulation pose generation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Datasets (Stage 2) For the dataset used in the robot manipulation fine-tuning stage, we follow the data collection process of previous works [61, 15], adopting the SAPIEN engine [28] to set up ....
3. Compare against the body-reported baseline or a matched simpler baseline: We choose LLaMA-AdapterV2 as a baseline because it serves as the base model for the current state-of-the-art (SOTA) robot MLLM, ManipLLM [15]..
4. Report the body metric and its denominator/aggregation: To measure the model's performance, we use the classical manipulation success rate, defined as the ratio of successfully manipulated samples to the total test samples..
5. Re-run the body-reported ablation/failure condition: validate the effectiveness of each method design, we perform an ablation study in Section 4.4..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (1.1 Hz), p. 1 (Abstract), p. 2 (1 Introduction); the primary result is directionally consistent at p. 8 (4 Experiment), p. 9 (4 Experiment), p. 8 (4 Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 We choose LLaMA-AdapterV2 as a baseline because it serves as the base model for the current ... 대비 To measure the model's performance, we use the classical manipulation success rate, defined as the ratio of successfully ...을 개선하고, Prediction of past and future actions is crucial in robotic manipulation, as it not only enables ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
