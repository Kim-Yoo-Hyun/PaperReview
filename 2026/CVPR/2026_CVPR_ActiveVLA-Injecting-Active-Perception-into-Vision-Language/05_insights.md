# Insights — ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142
- **p. 2 / 1. Introduction - extractive body cue:** To address this limitation, we propose ActiveVLA, a novel vision-language-action framework that explicitly integrates active perception into robotic manipulation.
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** This global-local fusion allows the model to combine overall scene understanding with fine spatial precision, enabling accurate and safe manipulation in complex environments.
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** A hierarchical feature fusion module then integrates global and local context to predict rotation, gripper state, and a binary collision flag. • Global Context Encoding: ...
- **p. 5 / 3.3. 3D Action Prediction - extractive body cue:** After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps.
- **p. 6 / 3.3. 3D Action Prediction - extractive body cue:** All tokens are concatenated and passed through an MLP head to predict rotation, gripper, and collision actions.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 6 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, most current VLA approaches primarily process 2D visual inputs, requiring massive datasets to bridge the gap between perception and action.
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this limitation is crucial for developing embodied agents capable of adaptive and reliable interaction in complex, real-world environments.
- **p. 3 / 1. Introduction - extractive body cue:** Real-world robot evaluations show strong generalization and high success rates, highlighting the practical impact of active perception in long-horizon and precision-critical tasks.
- **p. 3 / 1. Introduction - extractive body cue:** framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their ...
- **p. 6 / 4.1. Experimental Results - extractive body cue:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, ...
- **p. 6 / 4. Experiments - extractive body cue:** COLOSSEUM [48] extends RLBench with 12 perturbation types involving object, scene, and camera variations for robustness evaluation.
- **Boundary to test:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their fixed cameras miss critical details or become ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and an average rank of 1.07, outperforming all previous ... | p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results) |
| Failure/limitation | Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their fixed cameras miss critical details or become ... | p. 1 (Figure/Table caption), p. 6 (4.1. Experimental Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 framework that equips robots with active perception capabilities, enabling adaptive viewpoint selection and zoomin mechanisms for precise, fine-grained manipulation. • A Novel ActiveVLA Framework: ActiveVLA designs a novel coarse-to-fin ...를 This closed-loop, coarse-to-fine perception-action pipeline allows ActiveVLA to dynamically adapt its sensory inputs and maintain high effectiveness across complex, multi-step, and long-horizon manipulation tasks.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their fixed cameras miss critical details or become ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, active perception, 3D manipulation`.
- **Reading predecessor in the generated track queue:** PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their fixed cameras miss critical details or become ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: We compare ActiveVLA with state-of-the-art baselines..
4. Report the body metric and its denominator/aggregation: Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 51.3/0.59 1 2 3 4 5 6 Number of View 80.0 82.0 84.0 86.0 ....
5. Re-run the body-reported ablation/failure condition: Results are reported as mean success rates without confidence intervals..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.3. 3D Action Prediction), p. 5 (3.3. 3D Action Prediction), p. 6 (3.3. 3D Action Prediction); the primary result is directionally consistent at p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, summarized, Active mechanism이 We compare ActiveVLA with state-of-the-art baselines. 대비 Component Performance A-VS A-3Z RLBench COLOSSEUM GemBench 87.6/0.26 63.6/0.33 48.9/0.21 " 89.4/0.45 64.5/0.51 49.4/0.48 " " 91.8/0.53 65.9/0.62 ...을 개선하고, Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
