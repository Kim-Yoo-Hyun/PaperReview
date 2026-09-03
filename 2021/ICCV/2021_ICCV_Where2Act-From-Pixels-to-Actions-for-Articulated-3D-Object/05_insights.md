# Insights — Where2Act: From Pixels to Actions for Articulated 3D Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2101.02692; PDF retrieval source: https://arxiv.org/pdf/2101.02692. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 2 / 1. Introduction - extractive body cue:** We empirically show that our method successfully learns to predict possible actions for novel objects, and does so even for previously unseen categories.
- **p. 3 / 4. Method - extractive body cue:** We propose a learning-from-interaction approach to tackle this task.
- **p. 3 / 4.1. Network Modules - extractive body cue:** To decode the per-pixel actionable information, we propose three decoding heads: (c) an actionability scoring module Da that predicts a score ap ∈[0,1]; (d) an ...
- **p. 4 / 4.2. Collecting Training Data - extractive body cue:** Instead, we propose to let the agent learn by interacting with objects in simulation.
- **p. 3 / 4.1. Network Modules - extractive body cue:** For the 3D experiments, we use PointNet++ segmentation network [34] and implementation [47] with 4 set abstraction layers with single-scale grouping for the encoder and ...
- **p. 4 / 4.3. Training and Losses - extractive body cue:** We empirically find it beneficial to first train the action scoring module Ds and then train the three decoders jointly.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (4. Method), p. 3 (4.1. Network Modules), p. 4 (4.2. Collecting Training Data), p. 3 (4.1. Network Modules)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** We therefore limit our work to considering the plausible short-term interactions that an agent can perform given the current state of the object.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; ...
- **p. 3 / 3. Problem Statement - extractive body cue:** We formulate a new challenging problem Where2Act - inferring per-pixel ‘actionable information' for manipulating 3D articulated objects.
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. We visualize (a) the actionability scoring and (b) the action proposal predictions on an example cabinet with a door that can be slipped ...
- **p. 8 / 6. Conclusion - extractive body cue:** Finally, our method does not explicitly model the part segmentation and part motion axis, which may be incorporated in the future works to further improve ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The Proposed Where2Act Task. Given as input an ar- ticulated 3D object, we learn to propose the actionable information for different robotic manipulation ...
- **Boundary to test:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach that can ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | We observe that 3D-ours achieves the best performance. validates that our network learns geometric features more than local normals and curvatures. | p. 7 (5.2. Metrics and Baselines), p. 7 (5.2. Metrics and Baselines) |
| Failure/limitation | Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ... | p. 12 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features and design three decoding branches to predict the ... (p. 3, 4. Method).
- **Paper-specific mechanism:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach ... (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Figure 4. We visualize the per-pixel action scoring predictions over the articulated parts given certain gripper orientations for interaction. In each set of results, the left two shapes shown in ... (p. 7, Figure/Table caption); the relevant task/metric cue is We set up an interactive simulation environment in SAPIEN [49] and benchmark performance of the proposed method both qualititively and quantitatively. (p. 5, 5. Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** With random interactions, there are many more failed interaction trials than the successful ones. (p. 6, 5.2. Metrics and Baselines).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D Vision, affordance, articulated objects, active perception, point cloud`.
- **Reading predecessor in the generated track queue:** DUSt3R: Geometric 3D Vision Made Easy (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 7. Failure Cases. We visualize some interesting failure cases, which demonstrate the difficulty of the task and some am- biguous cases that are hard for robot to figure out. For the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features and design three decoding branches to predict the ... (p. 3, 4. Method); preserve the objective/update rule: After adjusting the relative loss scales to the same level, we obtain the final objective function L = Ls +Lr +100×La. (p. 5, 4.3. Training and Losses).
2. Use the paper-reported task/data/environment cue: Equipped with a large-scale PartNetMobility dataset, SAPIEN [49] provides a physics-rich simulation environment that supports robot actuators interacting with 2,346 3D CAD models from 46 object categories. (p. 5, 5.1. Framework and Settings).
3. Compare against the reported or matched baseline: We define the final measure as below. ssr = # successful proposals # total proposals (8) Baselines and Ablation Study. (p. 6, 5.2. Metrics and Baselines).
4. Report the body metric with its denominator and aggregation: We set up an interactive simulation environment in SAPIEN [49] and benchmark performance of the proposed method both qualititively and quantitatively. (p. 5, 5. Experiments).
5. Re-run the reported ablation or stress/failure condition: To validate the effectiveness of the proposed method and provide benchmarks for the proposed task, we compare to three baseline methods and one ablated version of our method: • B-Random: ... (p. 6, 5.2. Metrics and Baselines); if none is reported, design one around: With random interactions, there are many more failed interaction trials than the successful ones. (p. 6, 5.2. Metrics and Baselines).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 2 (1. Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5.1. Framework and Settings), and measure the boundary at p. 6 (5.2. Metrics and Baselines), p. 7 (5.3. Results and Analysis).

## Falsifiable research question

Under the paper's stated interface (Taking as input a single RGB image or a partial 3D point cloud, we employ an encoder-decoder backbone to extract per-pixel features ...), does the paper-specific mechanism (In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action ...) retain the reported evaluation outcome (We set up an interactive simulation environment in SAPIEN [49] and benchmark performance of the proposed method both ...) when tested against the paper's strongest explicit boundary (With random interactions, there are many more failed interaction trials than the successful ones.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We set up an interactive simulation environment in SAPIEN [49] and benchmark performance of the proposed method both ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In summary, our contributions are: • we formulate the task of inferring affordances for manipulating 3D articulated objects by predicting per-pixel action likelihoods and proposals; • we propose an approach ... (p. 2, 1. Introduction).
- **Paper-supported outcome:** Figure 4. We visualize the per-pixel action scoring predictions over the articulated parts given certain gripper orientations for interaction. In each set of results, the left two shapes shown in ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** With random interactions, there are many more failed interaction trials than the successful ones. (p. 6, 5.2. Metrics and Baselines).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
