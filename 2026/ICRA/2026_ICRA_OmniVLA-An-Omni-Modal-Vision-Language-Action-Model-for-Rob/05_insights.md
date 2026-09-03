# Insights — OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2509.19480. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information ...
- **p. 5 / Method - extractive body cue:** To ensure fair comparison with our approach, which relies solely on a single RGB camera without depth or LiDAR, we estimate depth using Depth360 [37] ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By training on omni-modal goals, we aim to enable stronger and more flexible policies, ultimately acquiring a foundation model that exhibits high adaptability to novel ...
- **p. 5 / Method - extractive body cue:** A state lattice motion planner is then used to generate velocity commands.
- **p. 5 / Method - extractive body cue:** Other VLA backbones: To further understand the role of VLA architectures and pre-training, we also implement our omni-modal goal-conditioning strategy for the 1B MiniVLA [38] ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (Method), p. 1 (I. INTRODUCTION), p. 5 (Method), p. 5 (Method)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, prior work in robot navigation typically trains policies with single modalities based on narrow applications.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we address the problem of modality imbalance and scarcity by using modality dropout during training, and modality masking during inference.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As a result, our policy exhibits strong generalization and fine-tuning capabilities, following language instructions not seen in the training data, and adapting to completely new ...
- **p. 3 / Dataset - extractive body cue:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets ...
- **p. 4 / Dataset - extractive body cue:** Since we cannot secure a sufficiently large batch size for some models even on a server with multiple GPUs, we accumulate the gradient for several ...
- **p. 5 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive body cue:** However, NaVILA fails, scoring 0.0 on all metrics, due to a domain gap in prompt style: it requires
- **p. 6 / V. EVALUATING OMNI-MODAL NAVIGATION - extractive body cue:** The smaller OmniVLA variant fails to handle the language instructions due to limited modal capacity.
- **Boundary to test:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets we use otherwise), we train a reannotation ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage more than one kind of information about ... | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language instructions out of the box and reach ... | p. 7 (Figure/Table caption), p. 3 (Dataset) |
| Failure/limitation | Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets we use otherwise), we train a reannotation ... | p. 3 (Dataset), p. 4 (Dataset) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 In this study, we propose a family of Omni-Modal VisionLanguage-Action Models (OmniVLA) for autonomous navigation that can ingest goals expressed in multiple modalities, leveraging information across modalities, and achieving a more fle ...를 As a result, our policy exhibits strong generalization and fine-tuning capabilities, following language instructions not seen in the training data, and adapting to completely new modalities.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets we use otherwise), we train a reannotation ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Moreover, our method allows the user to instruct the robot with multiple modalities, making it more user friendly and directly allowing the policy to leverage more than one kind of information about ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, Navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset (an autonomous vehicle dataset vs. the small robot datasets we use otherwise), we train a reannotation ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Training OmniVLA While using multi-modal inputs is enticing, training policies to accept omni-modal inputs requires compiling robot datasets that support training and addressing the relative imbalance and scarcity of the available modal ....
3. Compare against the body-reported baseline or a matched simpler baseline: We conduct extensive real-world evaluations and compare against state-of-the-art specialist and generalist baselines..
4. Report the body metric and its denominator/aggregation: Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language instructions out of the box and reach ....
5. Re-run the body-reported ablation/failure condition: Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 robots. Our policy can follow natural language instructions out of the box and reach ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (Method), p. 5 (Method); the primary result is directionally consistent at p. 7 (Figure/Table caption), p. 3 (Dataset), p. 3 (Dataset); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Moreover, allows, user mechanism이 We conduct extensive real-world evaluations and compare against state-of-the-art specialist and generalist baselines. 대비 Fig. 6: Deploying OmniVLA on multiple embodi- ments. We deploy our policy on the Vizbot and Unitree Go1 ...을 개선하고, Since existing reannotation approaches cannot account for the large embodiment gap of the BDD-V [29] dataset ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
