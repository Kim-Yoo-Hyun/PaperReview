# Insights — RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (71 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=OGxalNUHbJ; PDF retrieval source: https://openreview.net/pdf/81387e1e7f5169279b63c293ca88b1e4a8bc7e35.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions ...
- **p. 2 / 1 Introduction - extractive body cue:** To advance spatial referring, we introduce RefSpatial, a large-scale dataset of 2.5M high-quality examples with 20M QA pairs (2× prior [3]).
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose RoboRefer, a 3D-aware VLM that not only acquires precise spatial understanding via SFT but also exhibits generalized strong reasoning capabilities ...
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 4 / 3 Method - extractive body cue:** To address this, we propose a simple yet effective approach: a dedicated depth encoder and projector, initialized from their RGB counterparts.
- **p. 3 / 3 Method - extractive body cue:** Then, we elaborate on RoboRefer, including its architecture and training strategies (Sec.
- **p. 4 / 3 Method - extractive body cue:** 2, RoboRefer employs separate RGB and depth encoders to extract features, which are then aligned via projectors with the LLM for VQA or point prediction.
- **Contribution anchor:** p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (3 Method), p. 3 (3 Method)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Thus, this work attempts to address this gap by integrating both levels for comprehensive spatial referring.
- **p. 3 / 1 Introduction - extractive body cue:** To address the lack of multi-step spatial referring benchmarks, we introduce RefSpatial-Bench, comprising 200 real-world images with manually annotated tasks for object location and placement.
- **p. 3 / 1 Introduction - extractive body cue:** (2) We construct RefSpatial, a well-annotated dataset tailored for spatial referring, facilitating both SFT and RFT training, and introduce RefSpatial-Bench, a benchmark that fills the ...
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, current VLMs depend heavily on supervised fine-tuning (SFT) for implicit reasoning, risking memorizing answers over explicit reasoning and thereby hindering generalization and accuracy in ...
- **p. 52 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion ...
- **p. 21 / B.3.5 Question-Answer Pair Generation - extractive body cue:** 53 F More Demonstrations 54 G More Discussion on Limitations and Future Work 54 H Broader Impacts 54 I Licenses 54
- **p. 54 / C Implementation Details and Samples of RefSpatial-Bench - extractive body cue:** G More Discussion on Limitations and Future Work Despite achieving promising results, our model still has limitations.
- **Boundary to test:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring. | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | By using a single target point predicted by RoboRefer, the system can generate more accurate masks and corresponding grasp poses than those from 2D boxes under occlusion in cluttered scenes, yielding a ... | p. 9 (4 Experiments), p. 8 (Figure/Table caption) |
| Failure/limitation | Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ... | p. 52 (C Implementation Details and Samples of RefSpatial-Bench), p. 21 (B.3.5 Question-Answer Pair Generation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** 3.1 Problem Formulation We formulate spatial referring as predicting a single 2D point (x, y) in image space to specify a target location or destination, given visual inputs O (e.g., ... (p. 4, 3 Method).
- **Paper-specific mechanism:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring. (p. 3, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. SFT stage enables strong spatial understanding. ... (p. 8, Figure/Table caption); the relevant task/metric cue is Manipulation or Navigation tasks with spatial referring Success Rate(%) ↑ OpenVLA RoboPoint Ours Pick the specific hamburger closest to the mug nearest 0.00 0.00 80.00 the camera and place it ... (p. 9, 4 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Another major limitation of CA-1M is the lack of semantic labels for most annotated objects. (p. 34, B.2.2 Inherent Challenges and Limitations in CA-1M).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Vision-Language Model, Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Notably, we find that our model achieves nearly 100% success in the perception stage (i.e., determining location and placement), with failures primarily attributed to motion planning errors such as IK failures or ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 3.1 Problem Formulation We formulate spatial referring as predicting a single 2D point (x, y) in image space to specify a target location or destination, given visual inputs O (e.g., ... (p. 4, 3 Method); preserve the objective/update rule: Unlike PPO [154], which relies on a costly value network, GRPO estimates relative advantages by comparing intra-group rewards, reducing computation, and simplifying optimization. (p. 49, C Implementation Details and Samples of RefSpatial-Bench).
2. Use the paper-reported task/data/environment cue: To evaluate more complex multi-step spatial referring, we propose RefSpatial-Bench, a challenging benchmark based on real-world cluttered scenes. (p. 8, 4 Experiments).
3. Compare against the reported or matched baseline: 2, the 2B-RFT variant outperforms all baselines, exceeding the prior SOTA (Gemini-2.5-Pro [9]) by 17.4% (absolute) on RefSpatial-Bench. (p. 8, 4 Experiments).
4. Report the body metric with its denominator and aggregation: Manipulation or Navigation tasks with spatial referring Success Rate(%) ↑ OpenVLA RoboPoint Ours Pick the specific hamburger closest to the mug nearest 0.00 0.00 80.00 the camera and place it ... (p. 9, 4 Experiments).
5. Re-run the reported ablation or stress/failure condition: Moreover, our 2B variant outperforms NVILA-2B by 21.7% (absolute). (p. 8, 4 Experiments); if none is reported, design one around: Another major limitation of CA-1M is the lack of semantic labels for most annotated objects. (p. 34, B.2.2 Inherent Challenges and Limitations in CA-1M).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 23 (B.1.1 Multi-Stage Image Filtering), and measure the boundary at p. 34 (B.2.2 Inherent Challenges and Limitations in CA-1M), p. 34 (B.2.2 Inherent Challenges and Limitations in CA-1M).

## Falsifiable research question

Under the paper's stated interface (3.1 Problem Formulation We formulate spatial referring as predicting a single 2D point (x, y) in image space to specify a target ...), does the paper-specific mechanism (Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive ...) retain the reported evaluation outcome (Manipulation or Navigation tasks with spatial referring Success Rate(%) ↑ OpenVLA RoboPoint Ours Pick the specific hamburger closest ...) when tested against the paper's strongest explicit boundary (Another major limitation of CA-1M is the lack of semantic labels for most annotated objects.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Manipulation or Navigation tasks with spatial referring Success Rate(%) ↑ OpenVLA RoboPoint Ours Pick the specific hamburger closest ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (71 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our contributions are summarized as follows: (1) We propose RoboRefer, a 3D-aware reasoning VLM trained using a sequential SFT-RFT strategy with metric-sensitive process reward functions to achieve spatial referring. (p. 3, 1 Introduction).
- **Paper-supported outcome:** Figure 4: RefSpatial-Bench results. G.P., M.M., and R.P. donate Gemini-2.5-Pro [9], Molmo- 72B [15], and RoboPoint [5]. RoboRefer-RFT excels in unseen and multi-step cases. SFT stage enables strong spatial understanding. ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** Another major limitation of CA-1M is the lack of semantic labels for most annotated objects. (p. 34, B.2.2 Inherent Challenges and Limitations in CA-1M).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
