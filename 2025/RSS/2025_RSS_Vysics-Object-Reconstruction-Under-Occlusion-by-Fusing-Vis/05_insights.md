# Insights — Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p034.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p034.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in ...
- **p. 4 / IV. APPROACH - extractive body cue:** Beyond the insights that led to this systems integration, our main contribution lies in how Vysies incorporates these two powerful tools together such that they ...
- **p. 4 / IV. APPROACH - extractive body cue:** ‘The basis of our contribution is in how we unify the visible and "physible" geometry measurements together. §IV-A di cusses how vision helps in the ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** We first compare the geometry reconstruction of our method with that of shape completion models and single-view 3D generation models.
- **p. 8 / 200.0 BundlesDF - extractive body cue:** Our method recovers the occluded geometry through physics-based reasoning over the observed trajectories, substantially and consistently improving the geometric accuracy in both metrics.
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** Trajectory-Based Dynamics Model Learning
- **p. 2 / C. Simultaneous Tracking and Shape Reconstruction - extractive body cue:** ‘System identification is an important robotics subfield that aims to build accurate system models, which can then be leveraged via model-based control techniques.
- **Contribution anchor:** p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH), p. 4 (IV. APPROACH), p. 8 (A. Geometry Reconstruction), p. 8 (200.0 BundlesDF), p. 2 (C. Simultaneous Tracking and Shape Reconstruction)

### Strongest assumption and failure boundary

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Estimating geometry through contact-rich interactions is not a trivial problem.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** While some might be recognized from an existing database, others will require physical interaction to be newly understood on the spot.
- **p. 9 / B. Dynamics Predictions - extractive body cue:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics ...
- **p. 8 / A. Geometry Reconstruction - extractive body cue:** Under severe occlusion, while the shape completion ‘models can achieve similar or slightly lower chamfer distance than pure vision-based reconstruction, BundleSDF, they fall behind Vysics ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Vision-based shape reconstruction (projection shown in green) can be limited by occlusion. Fusing vision and contact rich physics, our method recovers the occluded ...
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** There are substantial visual ‘occlusions preventing the camera from directly seeing much of the object geometry.
- **p. 6 / V. EXPERIMENTAL SETUP - extractive body cue:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory.
- **Boundary to test:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction, | p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH) |
| Reported outcome | Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Failure/limitation | A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ... | p. 9 (B. Dynamics Predictions), p. 8 (A. Geometry Reconstruction) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Referring to the labeled arrows in Figure 3, we obtain the object trajectory (b) and the initial shape estimates (c) from masked input RGBD images (a) via BundleSDF. (p. 4, IV. APPROACH).
- **Paper-specific mechanism:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction, (p. 1, 1. INTRODUCTION).
- **Evidence boundary:** the reported outcome is These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as ... (p. 6, V. EXPERIMENTAL SETUP); the relevant task/metric cue is Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose stays within 10em of position error and within 45 degrees of rotational ... (p. 9, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory. (p. 6, V. EXPERIMENTAL SETUP).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Robotics-enabling 3D perception`; tags: `Robotics, 3D perception, object reconstruction, contact-rich manipulation, dynamics, occlusion`.
- **Reading predecessor in the generated track queue:** PointVLA: Injecting the 3D World into Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** A limitation of Vysics is that it does not incorporate notions of object elasticity or bounciness into the learning problem, ‘This shortcoming means the dynamics predictions of our earned models could deviate ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Referring to the labeled arrows in Figure 3, we obtain the object trajectory (b) and the initial shape estimates (c) from masked input RGBD images (a) via BundleSDF. (p. 4, IV. APPROACH); preserve the objective/update rule: While [56] avoids the problematic gradients in contactrch scenarios by using a gradient-free search over a discrete set of hypothesized geometries, Vysics leverages smooth, implicit-based losses and thus can directly ... (p. 3, C. Simultaneous Tracking and Shape Reconstruction).
2. Use the paper-reported task/data/environment cue: These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as ... (p. 6, V. EXPERIMENTAL SETUP).
3. Compare against the reported or matched baseline: Fig. 7: A qualitative comparison of the geometry reconstruc tion under heavy occlusion between our method and the vision-only baseline. In the image view, the mesh projection is shown in ... (p. 7, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose stays within 10em of position error and within 45 degrees of rotational ... (p. 9, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Fig. 8: The quantitative comparison of the geometric recon- struction accuracy. Each dot is one session. The results of the (p. 8, Figure/Table caption); if none is reported, design one around: In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory. (p. 6, V. EXPERIMENTAL SETUP).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1. INTRODUCTION), p. 4 (IV. APPROACH), match the reported outcome at p. 6 (V. EXPERIMENTAL SETUP), p. 6 (V. EXPERIMENTAL SETUP), p. 8 (Figure/Table caption), and measure the boundary at p. 6 (V. EXPERIMENTAL SETUP), p. 9 (B. Dynamics Predictions).

## Falsifiable research question

Under the paper's stated interface (Referring to the labeled arrows in Figure 3, we obtain the object trajectory (b) and the initial shape estimates (c) from masked ...), does the paper-specific mechanism (Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot ...) retain the reported evaluation outcome (Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose ...) when tested against the paper's strongest explicit boundary (In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Fig. 12: For quantifying dynamics prediction performance, wwe compare how far into an open-loop rollout the predicted pose ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Fusing vision and contact rich physics, our method recovers the occluded geometry through object interactions with the robot and environment, The robot end effector in yellow shows the robot-object interaction, (p. 1, 1. INTRODUCTION).
- **Paper-supported outcome:** These robot interactions were teleoperated via commanded end effector poses tracked with impedance control. ‘The dataset includes the RGBD videos of the objects in interactions with object ‘mask annotations, as ... (p. 6, V. EXPERIMENTAL SETUP).
- **Strongest explicit boundary:** In the evaluation, we excluded the sessions in which BundleSDF lost track of the object and failed to yield the object trajectory. (p. 6, V. EXPERIMENTAL SETUP).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
