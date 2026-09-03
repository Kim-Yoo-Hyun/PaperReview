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
| Reported outcome | PDF body did not yield a recoverable outcome statement; no claim inferred | 본문 anchor 없음 |
| Failure/limitation | 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ... | p. 10 (VI. LEARNED CHALLENGES AND LIMITATIONS), p. 7 (A. Experiment Design) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions in the form of velocity ... (p. 7, C. Supervisory Safety Controller).
- **Paper-specific mechanism:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, a high-speed vi ‘only airborne ... (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. (p. 7, A. Experiment Design); the relevant task/metric cue is The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. (p. 7, A. Experiment Design). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the intruder is below the horizon, As acknowledged in the benchmarking of ‘our ... (p. 11, B. Limitations).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, safe control, collision avoidance, control barrier function, aerial robotics, sim-to-real`.
- **Reading predecessor in the generated track queue:** Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use Kalman filtering to ensure minimal false positives ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions in the form of velocity ... (p. 7, C. Supervisory Safety Controller); preserve the objective/update rule: Note that the non-linear constraint h(x) <0 is not necessarily a subset of d > dhiresk when d > 0. (p. 6, C. Supervisory Safety Controller).
2. Use the paper-reported task/data/environment cue: These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. (p. 7, A. Experiment Design).
3. Compare against the reported or matched baseline: Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. Across the diferent weather scenarios, ViSafeshoweases ... (p. 10, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. (p. 7, A. Experiment Design).
5. Re-run the reported ablation or stress/failure condition: PDF body did not yield a recoverable ablation/stress condition; no ablation inferred; if none is reported, design one around: Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the intruder is below the horizon, As acknowledged in the benchmarking of ‘our ... (p. 11, B. Limitations).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 2 (I. INTRopI), match the reported outcome at p. 7 (A. Experiment Design), p. 7 (A. Experiment Design), p. 10 (Figure/Table caption), and measure the boundary at p. 11 (B. Limitations), p. 10 (VI. LEARNED CHALLENGES AND LIMITATIONS).

## Falsifiable research question

Under the paper's stated interface (We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level ...), does the paper-specific mechanism (Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, ...) retain the reported evaluation outcome (The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.) when tested against the paper's strongest explicit boundary (Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, a high-speed vi ‘only airborne ... (p. 1, Abstract).
- **Paper-supported outcome:** These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. (p. 7, A. Experiment Design).
- **Strongest explicit boundary:** Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the intruder is below the horizon, As acknowledged in the benchmarking of ‘our ... (p. 11, B. Limitations).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
