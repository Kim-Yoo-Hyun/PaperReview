# Insights — HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=h7aQxzKbq6; PDF retrieval source: https://openreview.net/pdf/eafdc79dd4a2aa8bac8cced6ed84a72b790f2bcd.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 INTRODUCTION - extractive body cue:** It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose a hierarchical architecture for VLAs, HAMSTER (Hierarchical Action Models with SeparaTEd Path Representations), where large fine-tuned VLMs are connected to ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** It consists of two interconnected models: first, a higher-level VLM that is finetuned on large-scale, off-domain data to produce intermediate 2D path guidance (detailed in ...
- **p. 6 / 3 BACKGROUND - extractive body cue:** A sample consists of a prompt z like Locate object between the marked items, an input image img and answer ans like [(0.25, 0.11), (0.22, ...
- **p. 6 / 3 BACKGROUND - extractive body cue:** This dataset consists of data automatically generated in simulation and collected from existing real-world datasets; its diverse tasks enable the HAMSTER VLM to reason about ...
- **p. 20 / B.1 VLM IMPLEMENTATION DETAILS - extractive body cue:** We condition the model on an image and the prompt, except when training on Pixel Point Prediction data (i.e., from Robopoint (Yuan et al., 2024b)) ...
- **p. 20 / B.2 LOW-LEVEL POLICY TRAINING DETAILS - extractive body cue:** For low-level policy training, we train the policies on ground truth paths constructed by projecting trajectory end-effector points to the camera image.
- **Contribution anchor:** p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 6 (3 BACKGROUND), p. 6 (3 BACKGROUND), p. 20 (B.1 VLM IMPLEMENTATION DETAILS)

### Strongest assumption and failure boundary

- **p. 1 / 1 INTRODUCTION - extractive body cue:** A line of prior work (Brohan et al., 2023a; Kim et al., 2024; Black et al., 2024) builds open-world vision-language-action models (VLAs) by finetuning off-the-shelf ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** The primary advantages of finetuning such a hierarchical VLM that produces intermediate representations as opposed to directly producing actions a with a monolithic model (Kim ...
- **p. 10 / 3 BACKGROUND - extractive body cue:** 6 CONCLUSION AND LIMITATIONS In summary, we study hierarchical VLA models that achieve robust generalization in robotic manipulation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing general robot manipulation policies has been notoriously difficult.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We hypothesize, and show experimentally in Fig 7, that this hierarchical separation can allow VLA models to more effectively bridge the domain gap between off-domain ...
- **p. 9 / 3 BACKGROUND - extractive body cue:** See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes.
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 15: Performance Distribution of RVT2+Sketch and 3DDA+Sketch This section outlines the failure modes observed during our experiments and provides a detailed breakdown of the ...
- **Boundary to test:** See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., 2024a), we propose the novel insight that ... | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 2: Real world results demonstrate HAMSTER general- izes to better to novel camera views (see Fig.Figure 6). We ran 10 trails and report averaged success score (success) described in Table 4 ... | p. 9 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Failure/limitation | See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes. | p. 9 (3 BACKGROUND), p. 10 (3 BACKGROUND) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Imitation learning trains a policy πθ(a / s, o, z) from expert demonstrations, where s denotes proprioceptive inputs, o includes perceptual observations (e.g., RGB images, depth), and z provides task instructions.를 These VLA models, which we refer to in this work as monolithic VLA models, rely crucially on large robotics datasets, complete with on-robot observations, e.g., images and proprioceptive states, and actions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: It is important to note that while we are certainly not the first to propose hierarchical VLA models (Gu et al., 2023; Nasiriany et al., 2024a), we propose the novel insight that ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, Reinforcement Learning`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E for failure modes.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Provide a sequence of points denoting the trajectory of a robot gripper to achieve the goal..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different axes of generalization and across both prehensile and non-prehensile tasks. Across all generalization axes, HAMSTE ....
4. Report the body metric and its denominator/aggregation: Table 1: Results on Colosseum demon- strate that HAMSTER is data efficient, achieving 2X the success score of 3D-DA with just 50% of the data..
5. Re-run the body-reported ablation/failure condition: Table 6: Real world average success rates grouped by task type. G DIFFERENT WAYS OF REPRESENTING 2D PATHS To investigate the effect of the number of points on the 2D path, we ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 20 (B.1 VLM IMPLEMENTATION DETAILS), p. 20 (B.2 LOW-LEVEL POLICY TRAINING DETAILS), p. 21 (B.2 LOW-LEVEL POLICY TRAINING DETAILS); the primary result is directionally consistent at p. 9 (Figure/Table caption), p. 25 (Figure/Table caption), p. 2 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 important, note, while mechanism이 Figure 4: Depiction of quantitative real-world policy execution results on a real-world robot, evaluated across different ... 대비 Table 1: Results on Colosseum demon- strate that HAMSTER is data efficient, achieving 2X the success score of ...을 개선하고, See Appendix C for evaluation conditions, a task list, and other experiment details, and Appendix E ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
