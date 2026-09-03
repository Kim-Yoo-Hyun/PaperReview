# Insights — Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p001.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p001.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / body section boundary not confidently recovered - extractive body cue:** To overcome these issues, we propose a novel learned perceptive
- **p. 3 / B. Planning - extractive body cue:** Our method addresses domain discrepancies by incorporating real-world data into the ‘dynamics model while maintaining platform awareness through earning from past experiences.
- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / 1. Inrropucrion - extractive body cue:** The main contributions of this work are as follows:
- **p. 2 / 1. Inrropucrion - extractive body cue:** by reducing the need for extensive parameter tuning and providing a flexible solution for non-task-specific planning. ‘This enables zero-shot adaptation to new environments without requiring ...
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **Contribution anchor:** p. 1 (body section boundary not confidently recovered), p. 3 (B. Planning), p. 5 (B. Model Architecture), p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion), p. 2 (A. Dynamics Modeling)

### Strongest assumption and failure boundary

- **p. 2 / 1. Inrropucrion - extractive body cue:** However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.
- **p. 2 / 1. Inrropucrion - extractive body cue:** However, training neural networks to represent robot dynamics often requires substantial amounts of state-action trajectories, motivating the use of synthetic data to mitigate the challenges ...
- **p. 1 / body section boundary not confidently recovered - extractive body cue:** The FDM is trained on multiple years of simulated navigation experience, including high-risk ‘maneuvers, and real-world interactions to incorporate the full system dynamics beyond rigid ...
- **p. 3 / B. Planning - extractive body cue:** While unsupervised approaches rely on simplified dynamics and require manual ccost-map tuning, RL-based planners learn platform-aware behaviors through experience but face sim-to-real transfer challenges due ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure ...
- **p. 7 / A. FDM Percepriveness - extractive body cue:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate ...
- **p. 8 / B. Baseline Comparison - extractive body cue:** Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to the more conservative baseline.
- **Boundary to test:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To overcome these issues, we propose a novel learned perceptive | p. 1 (body section boundary not confidently recovered), p. 3 (B. Planning) |
| Reported outcome | Il, our approach achieves the highest success rate across both environments. | p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |
| Failure/limitation | Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ... | p. 7 (A. FDM Percepriveness), p. 8 (B. Baseline Comparison) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure risk of the trajectory where ... (p. 3, A. Dynamics Modeling).
- **Paper-specific mechanism:** To overcome these issues, we propose a novel learned perceptive (p. 1, Body text (section boundary not confidently recovered)).
- **Evidence boundary:** the reported outcome is Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of the planning objective. ‘The presented network ... (p. 10, C. Platform-aware Predictions); the relevant task/metric cue is Regarding the collision estimation, the developed FDM demonstrates an accuracy of at least 89% over all ‘environments, Our method predicts collision in environments with 2D obstacles correctly with an FI ... (p. 8, B. Baseline Comparison). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving ... (p. 10, C. Platform-aware Predictions).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, model predictive control, safe navigation, sim-to-real, legged`.
- **Reading predecessor in the generated track queue:** Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure risk of the trajectory where ... (p. 3, A. Dynamics Modeling); preserve the objective/update rule: These weights are computed based on the reward 7, of each trajectory, ensuring higherreward trajectories contrite more significantly to the update: (p. 3, B. Model Predictive Path Integral Control).
2. Use the paper-reported task/data/environment cue: Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving ... (p. 10, C. Platform-aware Predictions).
3. Compare against the reported or matched baseline: Further, the better accuracy compared to the baselines becomes clearly (p. 7, B. Baseline Comparison).
4. Report the body metric with its denominator and aggregation: Regarding the collision estimation, the developed FDM demonstrates an accuracy of at least 89% over all ‘environments, Our method predicts collision in environments with 2D obstacles correctly with an FI ... (p. 8, B. Baseline Comparison).
5. Re-run the reported ablation or stress/failure condition: These obstacles cannot be differentiated from walls using only a horizontal 2D sensor without actively changing the observation angle. (p. 6, B. Model Architecture); if none is reported, design one around: Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving ... (p. 10, C. Platform-aware Predictions).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1. Inrropucrion), match the reported outcome at p. 10 (C. Platform-aware Predictions), p. 7 (B. Baseline Comparison), p. 7 (B. Baseline Comparison), and measure the boundary at p. 10 (C. Platform-aware Predictions), p. 7 (A. FDM Percepriveness).

## Falsifiable research question

Under the paper's stated interface (We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} ...), does the paper-specific mechanism (To overcome these issues, we propose a novel learned perceptive) retain the reported evaluation outcome (Regarding the collision estimation, the developed FDM demonstrates an accuracy of at least 89% over all ‘environments, Our ...) when tested against the paper's strongest explicit boundary (Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Regarding the collision estimation, the developed FDM demonstrates an accuracy of at least 89% over all ‘environments, Our ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To overcome these issues, we propose a novel learned perceptive (p. 1, Body text (section boundary not confidently recovered)).
- **Paper-supported outcome:** Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of the planning objective. ‘The presented network ... (p. 10, C. Platform-aware Predictions).
- **Strongest explicit boundary:** Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving ... (p. 10, C. Platform-aware Predictions).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
