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

- **Paper-specific interface:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 (p. 2, 1. Introduction).
- **Paper-specific mechanism:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and an average rank of 1.07, outperforming ... (p. 7, 4.1. Experimental Results); the relevant task/metric cue is As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of 92.4%, 66.3%, and 45.1%, surpassing 8147 (p. 7, 4.1. Experimental Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, 65.6%). (p. 6, 4.1. Experimental Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, active perception, 3D manipulation`.
- **Reading predecessor in the generated track queue:** PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1. Comparison between previous VLA methods and ActiveVLA. Traditional VLA systems often fail in tasks like "bring the apples on the table" because their fixed cameras miss critical details or become ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 (p. 2, 1. Introduction); preserve the objective/update rule: After obtaining the actively selected and zoom-in views, we feed them into the VLM to generate attention heatmaps. (p. 5, 3.3. 3D Action Prediction).
2. Use the paper-reported task/data/environment cue: Real-world experiments are conducted on a KINOVA GEN2 robot with a RealSense D455 camera in an eye-to-hand setup, covering occlusion-rich manipulation tasks. (p. 6, 4. Experiments).
3. Compare against the reported or matched baseline: We compare ActiveVLA with state-of-the-art baselines. (p. 6, 4. Experiments).
4. Report the body metric with its denominator and aggregation: As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of 92.4%, 66.3%, and 45.1%, surpassing 8147 (p. 7, 4.1. Experimental Results).
5. Re-run the reported ablation or stress/failure condition: Results are reported as mean success rates without confidence intervals. (p. 7, 4.1. Experimental Results); if none is reported, design one around: It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, 65.6%). (p. 6, 4.1. Experimental Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 7 (4.1. Experimental Results), p. 7 (4.1. Experimental Results), p. 8 (4.2. Ablation Study), and measure the boundary at p. 6 (4.1. Experimental Results), p. 6 (4. Experiments).

## Falsifiable research question

Under the paper's stated interface (The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142), does the paper-specific mechanism (The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142) retain the reported evaluation outcome (As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of ...) when tested against the paper's strongest explicit boundary (It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (As shown in Table 3, ActiveVLA achieves the best performance across core levels L1-L3, with success rates of ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The contributions of this paper are summarized: • Active Perception for Vision-Language-Action Models: We propose ActiveVLA, a novel vision-language-action 8142 (p. 2, 1. Introduction).
- **Paper-supported outcome:** Results in Table 2 show that ActiveVLA achieves a new state of the art on COLOSSEUM, with an average success rate of 65.9% and an average rank of 1.07, outperforming ... (p. 7, 4.1. Experimental Results).
- **Strongest explicit boundary:** It performs exceptionally well in precision-demanding and contact-rich tasks such as Insert Peg and Open Drawer, and remains robust even under occlusions (e.g., Place Cups, 65.6%). (p. 6, 4.1. Experimental Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
