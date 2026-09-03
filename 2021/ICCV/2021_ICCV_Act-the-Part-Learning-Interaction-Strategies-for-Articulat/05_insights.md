# Insights — Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2105.01047; PDF retrieval source: https://arxiv.org/pdf/2105.01047. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we introduce Act the Part.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 4 / 3.4. History Aggregation - extractive body cue:** We introduce a history aggregation algorithm to updated part memory V , based on predicted Mt and Mt+1.
- **p. 2 / 3. Approach - extractive body cue:** We then explain the three components of our approach: an interaction network (Sec.
- **p. 1 / 1. Introduction - extractive body cue:** Our task and approach novelty are highlighted in Fig.
- **p. 4 / 3.2. Learning to Act to Discover Parts - extractive body cue:** Mask 𝑀!"# Part Network Mask Decoder Mask Decoder ResNet18 Image Observation Action Applied Figure 4.
- **p. 4 / 3.5. Reward - extractive body cue:** At inference, we first predict and execute an action.
- **Contribution anchor:** p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. History Aggregation), p. 2 (3. Approach), p. 1 (1. Introduction), p. 4 (3.2. Learning to Act to Discover Parts)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** Passive part segmentation algorithms require detailed annotation and cannot generalize to new categories.
- **p. 1 / 1. Introduction - extractive body cue:** While motion can help discover new objects, prior work cannot infer actions for understanding individual parts.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** However, we also show our model generalizes to real-world images without finetuning.
- **p. 2 / 1. Introduction - extractive body cue:** (2) Our method generalizes to unseen object instances and categories with different numbers of parts and joints.
- **p. 2 / 1. Introduction - extractive body cue:** By reasoning about changes in visual observations, our perception algorithm is able to discover new parts, keep track of existing ones, and update the part ...
- **p. 5 / 4.1. Metrics and Points of Comparison - extractive body cue:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%).
- **p. 8 / 4.3. Real World Results - extractive body cue:** G for more real world experiment results and failure case analysis.
- **Boundary to test:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%).

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To address these challenges, we introduce Act the Part | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | While other algorithms' performance saturate quickly with one or two interactions, [Ours-Touch] and [Ours-NoTouch] are able to improve with more interactions. | p. 5 (4.2. Benchmark Results), p. 7 (4.2. Benchmark Results) |
| Failure/limitation | The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). | p. 5 (4.1. Metrics and Points of Comparison), p. 8 (4.3. Real World Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** (a) The interaction network computes hold and push from an image observation and current part memory. (p. 3, 3.1. Problem Formulation).
- **Paper-specific mechanism:** Our task and approach novelty are highlighted in Fig. (p. 1, 1. Introduction).
- **Evidence boundary:** the reported outcome is Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. (p. 7, 4.2. Benchmark Results); the relevant task/metric cue is The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D Vision, active perception, articulated objects, part discovery`.
- **Reading predecessor in the generated track queue:** Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%).; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: (a) The interaction network computes hold and push from an image observation and current part memory. (p. 3, 3.1. Problem Formulation); preserve the objective/update rule: First, a hold action parameterized by its location and implemented as a fixed point constraint between the gripper and a part. (p. 3, 3.1. Problem Formulation).
2. Use the paper-reported task/data/environment cue: Dataset, test initialization, and pre-trained models will be released for reproducibility and benchmarking. (p. 5, 4. Evaluation).
3. Compare against the reported or matched baseline: Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. (p. 7, 4.2. Benchmark Results).
4. Report the body metric with its denominator and aggregation: The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
5. Re-run the reported ablation or stress/failure condition: To provide a better metric for these structures, we measure dH95, which is a part-aware variant of a common metric in medical image segmentation [8]. (p. 5, 4.1. Metrics and Points of Comparison); if none is reported, design one around: The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. Introduction), p. 1 (1. Introduction), match the reported outcome at p. 7 (4.2. Benchmark Results), p. 8 (4.3. Real World Results), p. 8 (4.3. Real World Results), and measure the boundary at p. 5 (4.1. Metrics and Points of Comparison), p. 8 (4.3. Real World Results).

## Falsifiable research question

Under the paper's stated interface ((a) The interaction network computes hold and push from an image observation and current part memory.), does the paper-specific mechanism (Our task and approach novelty are highlighted in Fig.) retain the reported evaluation outcome (The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two ...) when tested against the paper's strongest explicit boundary (The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our task and approach novelty are highlighted in Fig. (p. 1, 1. Introduction).
- **Paper-supported outcome:** Results on two unseen object categories show our methods (pink and brown) approach the oracle baseline over time. (p. 7, 4.2. Benchmark Results).
- **Strongest explicit boundary:** The metric penalizes both errors in mask prediction and failure to discover masks (e.g. if one of two parts is discovered, maximum IoU is 50%). (p. 5, 4.1. Metrics and Points of Comparison).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
