# Insights — Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.07473; PDF retrieval source: https://arxiv.org/pdf/2309.07473. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 Introduction - extractive body cue:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.
- **p. 2 / 1 Introduction - extractive body cue:** We evaluate our framework by training our model on constrained object categories and applying few-shot learning to novel categories with limited shapes.
- **p. 5 / 4 Method - extractive body cue:** As shown in the right part of figure 2, when faced with a novel category, our framework will first predict the similarity of the objects.
- **p. 3 / 4 Method - extractive body cue:** Next, we introduce the ‘similarity module' to form a representation that connects the geometries in the supporting set with geometries across category boundaries.
- **p. 3 / 4 Method - extractive body cue:** As shown in Figure 2, we propose the ‘Where2Explore' framework to explicitly leverage the similar semantics on local geometries shared across different categories for cross-category ...
- **p. 6 / 4 Method - extractive body cue:** 4.4 Network Architecture and Training Strategy Our network consists of two modules - the affordance module and the similarity module.
- **p. 6 / 4 Method - extractive body cue:** We use a PointNet++ segmentation network [29] encoder for extracting features from 3D partial point clouds.
- **Contribution anchor:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (4 Method), p. 3 (4 Method), p. 3 (4 Method), p. 6 (4 Method)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** This limitation hinders the efficiency and safety of real-world applications of robots.
- **p. 1 / 1 Introduction - extractive body cue:** However, due to the significant variance in the objects' structure, 3D geometry, and articulation types across categories, developing efficient perception and manipulation systems that can ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering the substantial semantic and geometric gap between known shapes and novel categories, forming an efficient exploration strategy for out-of-distribution objects is challenging.
- **p. 2 / 1 Introduction - extractive body cue:** Via fine-tuning our network with the interactions on novel objects, the model could generalize to unseen objects within this novel category (Bottom Right).
- **p. 3 / 1 Introduction - extractive body cue:** • Exploring the challenging task of cross-category few-shot learning for articulated object manipulation, requiring the model to capture fine-grained geometric information from an entirely new ...
- **p. 8 / 5 Experiments - extractive body cue:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.
- **p. 9 / 5 Experiments - extractive body cue:** Although Affordance fails to directly generalize to novel categories (Left) via interacting on low-similarity areas (Middle), our framework could learn the semantic information on them ...
- **Boundary to test:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | For both the F-score and sample success rate, we use the average score of the four different training category combinations. | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Failure/limitation | Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. | p. 8 (5 Experiments), p. 9 (5 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and gripper orientations {Ri} on each point, and is ... (p. 4, 4 Method).
- **Paper-specific mechanism:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity. (p. 2, 1 Introduction).
- **Evidence boundary:** the reported outcome is Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario. Table ... (p. 8, Figure/Table caption); the relevant task/metric cue is For both the F-score and sample success rate, we use the average score of the four different training category combinations. (p. 7, 5 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. (p. 8, 5 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D Vision, active exploration, affordance, articulated objects, few-shot learning`.
- **Reading predecessor in the generated track queue:** Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Clio: Real-time Task-Driven Open-Set 3D Scene Graphs (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and gripper orientations {Ri} on each point, and is ... (p. 4, 4 Method); preserve the objective/update rule: Finally, both the affordance module and the similarity module will be updated by this interaction (Oi, pi, Ri, mi) and be ready for the next prediction on the object to ... (p. 5, 4 Method).
2. Use the paper-reported task/data/environment cue: Compared with PointEncoder, we show that our framework better understands the semantic information for manipulation than a pre-trained encoder, even if it is trained on a large-scale dataset and achieves ... (p. 7, 5 Experiments).
3. Compare against the reported or matched baseline: We set up three baselines for comparisons. (p. 6, 5 Experiments).
4. Report the body metric with its denominator and aggregation: For both the F-score and sample success rate, we use the average score of the four different training category combinations. (p. 7, 5 Experiments).
5. Re-run the reported ablation or stress/failure condition: Besides, we compare to ablated versions of our method to verify our exploration strategy: • No-explore (lower bound): our affordance model directly evaluated on novel categories without few-shot exploration, which ... (p. 7, 5 Experiments); if none is reported, design one around: Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. (p. 8, 5 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 8 (Figure/Table caption), p. 13 (Figure/Table caption), p. 9 (5 Experiments), and measure the boundary at p. 8 (5 Experiments), p. 9 (5 Experiments).

## Falsifiable research question

Under the paper's stated interface (The similarity module is designed to take a partial point cloud of an object Oi ∈R3×N, a set of action directions and ...), does the paper-specific mechanism (The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity.) retain the reported evaluation outcome (For both the F-score and sample success rate, we use the average score of the four different training ...) when tested against the paper's strongest explicit boundary (Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (For both the F-score and sample success rate, we use the average score of the four different training ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The results demonstrate our framework's capability to efficiently explore novel categories by exploiting geometric similarity. (p. 2, 1 Introduction).
- **Paper-supported outcome:** Table 3: Ablations on the exploration strategy using different interaction budget (1, 2, 5). We also conduct few-shot affordance learning on representative categories separately to match the real-world scenario. Table ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** Compared with AdaAfford, which fails to generalize to novel categories, our framework could still propose reasonable exploration strategies on novel categories leveraging local similarity. (p. 8, 5 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
