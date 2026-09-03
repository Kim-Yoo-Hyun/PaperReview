# Insights — Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p036.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p036.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** By combining object particles with spatial grids, our framework parameterizes dynamics in both Lagrangian and Eulerian coordinates, drawing an analogy to physics-based deformable object simulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In deformable object manipulation, an accurate predictive object dynamics model enables model-based planning, policy evaluation, and real-to-sim asset generation.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** The application of this model within a Model Predictive Control (MPC) framework is covered in Section IILE, An overview of our method is also provided ...
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ...
- **p. 5 / B. Model Components - extractive body cue:** We apply the Model-Predictive Path Integral (MPPD) [50] trajectory optimization algorithm to minimize the cost and to synthesize the robots actions.
- **Contribution anchor:** p. 3 (B. Learning-Based Deformable Modeling), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, developing dynamics models for deformable objects that are both accurate and generalizable remains a significant challenge.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these methods face significant challenges: the effectiveness of message passing is highly sensitive to the spatial distribution and connectivity of the graph nodes, making ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.
- **Boundary to test:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by reconstructing objects with 3D Gaussian Splatting and int ... | p. 3 (B. Learning-Based Deformable Modeling), p. 2 (I. INTRODUCTION) |
| Reported outcome | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | p. 5 (IV. EXPERIMENTS), p. 9 (Figure/Table caption) |
| Failure/limitation | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | p. 5 (IV. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ‘encoder to extract particle features ... (p. 3, B. Learning-Based Deformable Modeling).
- **Paper-specific mechanism:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Fig. 13: Additional Qualitative Comparisons on Dynamics Prediction. Given the initial states and actions (leftmost column), we present the prediction results of the MPM with parameter identification baseline, the GBND ... (p. 19, Figure/Table caption); the relevant task/metric cue is Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. (p. 5, IV. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, ... (p. 1, I. INTRODUCTION).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, deformable objects, dynamics, RGB-D, model-based planning`.
- **Reading predecessor in the generated track queue:** Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Map Space Belief Prediction for Manipulation-Enhanced Mapping (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ‘encoder to extract particle features ... (p. 3, B. Learning-Based Deformable Modeling); preserve the objective/update rule: Since the ‘dynamics function fy is fully differentiable, we optimize the network parameters «and 1 using gradient descent. (p. 5, B. Model Components).
2. Use the paper-reported task/data/environment cue: ‘€) Box: Two robot arms are used to open and close shipping boxes. (p. 6, A. Experiment Setup).
3. Compare against the reported or matched baseline: Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. (p. 5, IV. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. (p. 5, IV. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: ‘+ Can the model improve the performance of 3D actionconditioned video prediction and model-based planning? (p. 5, IV. EXPERIMENTS); if none is reported, design one around: For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, ... (p. 1, I. INTRODUCTION).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 19 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (A. Experiment Setup), and measure the boundary at p. 1 (I. INTRODUCTION), p. 10 (V. Liimarions).

## Falsifiable research question

Under the paper's stated interface (Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first ...), does the paper-specific mechanism (To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics.) retain the reported evaluation outcome (Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete ...) when tested against the paper's strongest explicit boundary (For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To address these limitations, we introduce a novel class of/ dynamic models called particle-grid neural dynamics. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Fig. 13: Additional Qualitative Comparisons on Dynamics Prediction. Given the initial states and actions (leftmost column), we present the prediction results of the MPM with parameter identification baseline, the GBND ... (p. 19, Figure/Table caption).
- **Strongest explicit boundary:** For example, physics-based simulators [12, 31] often struggle to generalize to the real world due to the inherent simto-real gap and the difficulties of system identification and state estimation, Meanwhile, ... (p. 1, I. INTRODUCTION).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
