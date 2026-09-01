# Insights — Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p001.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p001.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / Front matter - extractive body cue:** To overcome these issues, we propose a novel learned perceptive
- **p. 3 / B. Planning - extractive body cue:** Our method addresses domain discrepancies by incorporating real-world data into the ‘dynamics model while maintaining platform awareness through earning from past experiences.
- **p. 5 / B. Model Architecture - extractive body cue:** The Forward Dynamics Model loss £ consists of supervised terms for network outputs.
- **p. 2 / 1. Inrropucrion - extractive body cue:** The main contributions of this work are as follows:
- **p. 2 / 1. Inrropucrion - extractive body cue:** by reducing the need for extensive parameter tuning and providing a flexible solution for non-task-specific planning. ‘This enables zero-shot adaptation to new environments without requiring ...
- **p. 2 / A. Dynamics Modeling - extractive body cue:** Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **Contribution anchor:** p. 1 (Front matter), p. 3 (B. Planning), p. 5 (B. Model Architecture), p. 2 (1. Inrropucrion), p. 2 (1. Inrropucrion), p. 2 (A. Dynamics Modeling)

### Strongest assumption and failure boundary

- **p. 2 / 1. Inrropucrion - extractive body cue:** However, open challenges remain to incorporate 3) perception to target rough environments and the transfer from simulation to the real system.
- **p. 2 / 1. Inrropucrion - extractive body cue:** However, training neural networks to represent robot dynamics often requires substantial amounts of state-action trajectories, motivating the use of synthetic data to mitigate the challenges ...
- **p. 1 / Front matter - extractive body cue:** The FDM is trained on multiple years of simulated navigation experience, including high-risk ‘maneuvers, and real-world interactions to incorporate the full system dynamics beyond rigid ...
- **p. 3 / B. Planning - extractive body cue:** While unsupervised approaches rely on simplified dynamics and require manual ccost-map tuning, RL-based planners learn platform-aware behaviors through experience but face sim-to-real transfer challenges due ...
- **p. 3 / A. Dynamics Modeling - extractive body cue:** We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure ...
- **p. 7 / A. FDM Percepriveness - extractive body cue:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate ...
- **p. 8 / B. Baseline Comparison - extractive body cue:** Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to the more conservative baseline.
- **Boundary to test:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To overcome these issues, we propose a novel learned perceptive | p. 1 (Front matter), p. 3 (B. Planning) |
| Reported outcome | Il, our approach achieves the highest success rate across both environments. | p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |
| Failure/limitation | Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ... | p. 7 (A. FDM Percepriveness), p. 8 (B. Baseline Comparison) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, terrain/perception observation과 velocity command → body/contact state, foothold 또는 behavior mode → joint target, torque, footstep 또는 locomotion action`.
- 이 논문의 재사용 가능한 지점은 We define ihe state ¥ to be the tuple (p,r), where p © SE2 is the robot's pose and r < {0,1} is the failure risk of the trajectory where 0 indicates ...를 Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can also be used to directly estimate the next ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 body/contact state, foothold 또는 behavior mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To overcome these issues, we propose a novel learned perceptive
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, model predictive control, safe navigation, sim-to-real, legged`.
- **Reading predecessor in the generated track queue:** Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate perceptiveness, we apply the same action sequence ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the risk of hardware damage, leaving fa persistent ....
3. Compare against the body-reported baseline or a matched simpler baseline: Further, the better accuracy compared to the baselines becomes clearly.
4. Report the body metric and its denominator/aggregation: Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate in complex environments..
5. Re-run the body-reported ablation/failure condition: Fig, 5: Comparison of the postion error atthe final prediction step in different environments for the presented FDM I, the perceptive FDM by Kim etal [5] and the constant velocity model Ml ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (B. Model Architecture), p. 2 (A. Dynamics Modeling), p. 6 (B. Model Architecture); the primary result is directionally consistent at p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 6 (B. Model Architecture); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 overcome, issues, novel mechanism이 Further, the better accuracy compared to the baselines becomes clearly 대비 Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate ...을 개선하고, Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
