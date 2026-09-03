# Insights — Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2509.23107. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address this, we propose Spatio-Temporal OpenVocabulary Scene Graph (ST-OVSG), an open-vocabulary spatio-temporal scene graph designed for teleoperation.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To address this, we propose ST-OVSG that integrates object nodes, spatial relations, and temporal correspondences.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Formally, the challenge is to maintain a representation that allows the system to (i) recover the scene as it existed at the command-issue time, (ii) ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** This allows the planner to interpret userissued commands with respect to the scene state observed by the operator.
- **p. 4 / III. METHODOLOGY - extractive body cue:** The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** User commands are used to query node features, filtering relevant nodes to form an ST-OVSG subgraph, which is then serialized into JSON and provided to ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Taken together, these challenges reveal a fundamental gap: latency distorts the temporal alignment between operator intent and robot execution, while static representations fail to capture ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, directly applying these models to teleoperation robotics still faces several challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The second challenge is the static nature of current scene representations.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In practice, many predicted actions were semantically correct but expressed with different phrasing or level of detail, which lowers embedding-based similarity without indicating execution failure.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Because our representation is designed for openvocabulary settings, automated evaluation of nodes and edges is unreliable: object categories and relational boundaries under open vocabulary cannot ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Motion blur, viewpoint shifts, and occlusions destabilize open-vocabulary detections.
- **Boundary to test:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both the spatial structure and temporal dynamics of ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges in ConceptGraph. | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Failure/limitation | Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** An image encoder Φv and a text encoder Φt (e.g., CLIP [27]) are adopted to extract masked visual features f img i = Φv(Irgb n ; bi,n) and natural-language features ... (p. 3, III. METHODOLOGY).
- **Paper-specific mechanism:** The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both the spatial structure and temporal ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is These static results establish a baseline for subsequent experiments on dynamic environments, where temporal reasoning and latency-awareness play a central role. (p. 5, IV. EXPERIMENTS); the relevant task/metric cue is Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges in ConceptGraph. (p. 5, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses. (p. 6, IV. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Robotics, Graph Reasoning, semantic`.
- **Reading predecessor in the generated track queue:** Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: An image encoder Φv and a text encoder Φt (e.g., CLIP [27]) are adopted to extract masked visual features f img i = Φv(Irgb n ; bi,n) and natural-language features ... (p. 3, III. METHODOLOGY); preserve the objective/update rule: The cost is cspa j,k,n = wiou (1 -IoU(uj,k,n, zj,k,n)) + warea (p. 4, III. METHODOLOGY).
2. Use the paper-reported task/data/environment cue: Static Representation Construction To evaluate the quality of the proposed static scene representation, we conducted experiments on the Replica dataset [32], which provides high-fidelity indoor environments. (p. 5, IV. EXPERIMENTS).
3. Compare against the reported or matched baseline: With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG. (p. 6, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds to spatial edges in ConceptGraph. (p. 5, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed. (p. 5, IV. EXPERIMENTS); if none is reported, design one around: Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses. (p. 6, IV. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), and measure the boundary at p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (An image encoder Φv and a text encoder Φt (e.g., CLIP [27]) are adopted to extract masked visual features f img i ...), does the paper-specific mechanism (The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which ...) retain the reported evaluation outcome (Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower ...) when tested against the paper's strongest explicit boundary (Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both the spatial structure and temporal ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** These static results establish a baseline for subsequent experiments on dynamic environments, where temporal reasoning and latency-awareness play a central role. (p. 5, IV. EXPERIMENTS).
- **Strongest explicit boundary:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion blur or unusual poses. (p. 6, IV. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
