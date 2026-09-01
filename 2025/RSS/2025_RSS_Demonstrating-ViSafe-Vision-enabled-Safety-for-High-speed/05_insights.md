# Insights — Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p002.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS ...
- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 2 / I. INTRopI - extractive body cue:** We present ViSafe, a vision-only airborne collision avoidance system to impart see-and-avoid capabilities to sUAS.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** The control input w < R? consists of the rate of change of speed and heading, ic., Yown and Zoun Additionally, we also consider control ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Inspired by [32], we propose the following CBF:
- **p. 7 / C. Supervisory Safety Controller - extractive body cue:** We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be ...
- **Contribution anchor:** p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 1 (Abstract), p. 2 (I. INTRopI), p. 3 (B. Control Barrier Functions for Aerial Collision Avoidance), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller)

### Strongest assumption and failure boundary

- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** However, most existing avoidance logics require special sensors and information to provide RAS.
- **p. 2 / I. INTRopI - extractive body cue:** These tests were run using the same hardware as the real-world payload, thereby minimizing our sim-to-real gap for testing.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** Squires er al{51] identify key challenges with designing CBF for collision avoidance and propose a construction technique.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** In particular, for aireraft detection, the challenge is detecting small objects within high-resolution images, where keypoint-based architectures prove more effective than traditional anchor-based methods like ...
- **p. 1 / Abstract - extractive body cue:** Existing solutions, such 4s Autonomous Collision Avoidance Systems (ACAS) [33] and Unmanned ‘Traffic Management (UTM) [18] frameworks,
- **p. 10 / VI. LEARNED CHALLENGES AND LIMITATIONS - extractive body cue:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use ...
- **p. 7 / A. Experiment Design - extractive body cue:** The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.
- **Boundary to test:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS algorithms is the availability of extended surveillance ... | p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 1 (Abstract) |
| Reported outcome | paper-specific outcome not recovered | 본문 anchor 없음 |
| Failure/limitation | 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ... | p. 10 (VI. LEARNED CHALLENGES AND LIMITATIONS), p. 7 (A. Experiment Design) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 These logics involve generating cost tables for agent states and possible actions through simulation and optimization [8].를 streams multiple camera inputs, provides state estimation, performs deep learning model edge inference, and computes avoidance maneuvers on board in real time.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS algorithms is the availability of extended surveillance ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, safe control, collision avoidance, control barrier function, aerial robotics, sim-to-real`.
- **Reading predecessor in the generated track queue:** Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings..
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. Across the diferent weather scenarios, ViSafeshoweases consistent b ....
4. Report the body metric and its denominator/aggregation: The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries..
5. Re-run the body-reported ablation/failure condition: 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller); the primary result is directionally consistent at result anchor 없음; and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 There, variants, algorithm mechanism이 Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher ... 대비 The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.을 개선하고, 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
