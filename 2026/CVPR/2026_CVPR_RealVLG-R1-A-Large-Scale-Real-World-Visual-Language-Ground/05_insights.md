# Insights — RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our main contributions are as follows: • RealVLG-11B Dataset: The largest real-world grounding and grasping dataset with multi-granularity annotations from semantic localization to ...
- **p. 5 / 4.1. Overview - extractive body cue:** 3, we propose a unified framework, RealVLG-R1, which fine-tunes pretrained LVLMs using a reinforcement-style optimization strategy inspired by DeepSeek-R1 [22].
- **p. 5 / 4.1. Overview - extractive body cue:** Furthermore, we introduce a Verifiable Reward Mechanism that dynamically evaluates and guides model predictions in terms of both semantic correctness and physical feasibility.
- **p. 8 / Method - extractive body cue:** Building upon this, our proposed RealVLG-R1 model employs Qwen2.5-VL as its backbone and is developed within the VERL framework [68].
- **p. 6 / 4.3. Task-Specific Pipelines and Verifiable Rewards - extractive body cue:** 3, the policy model receives an image and a task prompt, then generates structured outputs according to task requirements.
- **p. 6 / 4.2. Policy Optimization with Verifiable Rewards - extractive body cue:** Grasp Contact SAM2 Answer Reference Model Reinforcement Fine-tuning KL Reward Policy Model (LVLMs) Figure 3.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (4.1. Overview), p. 5 (4.1. Overview), p. 8 (Method), p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** In summary, current VLG and grasping research highlight a clear gap between semantic understanding and manipulation reasoning, making them insufficient for real-world robotic scenarios that ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, as shown in Fig.
- **p. 8 / 6. Conclusions - extractive body cue:** Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning.
- **p. 3 / 3.1. Overview - extractive body cue:** Existing grasping datasets generally suffer from two major limitations.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Dataset split for RealVLG-11B. age instance. 5 Based on the resulting Rect Grasp Poses and segmentation masks, grasp contact points are subse- quently ...
- **p. 7 / 5.1. Data Quality Evaluation - extractive body cue:** Linguistic and grounding quality comparison. grasp points located within segmentation masks (Rg), and proportion of contact centers falling inside segmentation masks (Rc).
- **Boundary to test:** Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm. | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | In rectangular grasp pose prediction, performance relies on mean IoU (mIoU) and Grasp Accuracy (gAcc) [26], where gAcc is achieved when the IoU exceeds 0.25 and the angular deviation is below 30◦. | p. 7 (5.2. RealVLG Benchmark), p. 7 (5.1. Data Quality Evaluation) |
| Failure/limitation | Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning. | p. 8 (6. Conclusions), p. 3 (3.1. Overview) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 During training, input images and task prompts are processed through a policy optimization module to generate candidate outputs, which are then updated using verifiable reward signals.를 The core of RealVLG-R1 is its composite reward function R(q, o), providing hierarchical and verifiable feedback by combining output format compliance with task-specific geometric accuracy: R( q, o) = R_ { \text ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 1, we propose the RealVLG framework, which unifies visuallanguage grounding and grasping tasks within a single research paradigm.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Visual-Language Grounding, Benchmark, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] to improve runtime without extra fine-tuning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The dataset contains approximately 165,000 images, over 800 object instances, 1.3 million segmentation, detection, and language annotations, and 11 billion grasp examples, providing a high-quality benchmark for multi-granularity percept ....
3. Compare against the body-reported baseline or a matched simpler baseline: As shown in Table 3, benefiting from our carefully designed LVLM-assisted and human double-review annotation pipeline, RealVLG-11B consistently outperforms existing datasets across all comparable metrics..
4. Report the body metric and its denominator/aggregation: In rectangular grasp pose prediction, performance relies on mean IoU (mIoU) and Grasp Accuracy (gAcc) [26], where gAcc is achieved when the IoU exceeds 0.25 and the angular deviation is below 30◦..
5. Re-run the body-reported ablation/failure condition: Figure 3. Framework of RealVLG-R1. RealVLG-R1 fine-tunes pretrained LVLMs via reward-driven RL using task-specific verifiable rewards, enabling adaptive learning and improved generalization over bounding boxes, segmentation, grasp recta ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 6 (4.3. Task-Specific Pipelines and Verifiable Rewards), p. 5 (4.1. Overview), p. 6 (4.2. Policy Optimization with Verifiable Rewards); the primary result is directionally consistent at p. 7 (5.2. RealVLG Benchmark), p. 7 (5.1. Data Quality Evaluation), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 RealVLG, framework, unifies mechanism이 As shown in Table 3, benefiting from our carefully designed LVLM-assisted and human double-review annotation pipeline, ... 대비 In rectangular grasp pose prediction, performance relies on mean IoU (mIoU) and Grasp Accuracy (gAcc) [26], where gAcc ...을 개선하고, Future work will extend RealVLG to 3D space, and explore efficient models such as SmolVLM [43] ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
