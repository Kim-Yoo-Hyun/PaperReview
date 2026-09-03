# Insights — FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving the ...
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, we propose a cascaded action denoising mechanism that distributes the denoising computation across the original VLA and a separate Lite-Flow denoiser, ...
- **p. 3 / 3. Preliminaries - extractive body cue:** The model typically consists of a VLM backbone and a flow matching expert.
- **p. 3 / 3. Preliminaries - extractive body cue:** A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, and robot state ...
- **p. 6 / Model - extractive body cue:** We present the success rate (SR) and standard error for each method across four task suites.
- **p. 4 / 4.1. Value-Guided Test-Time Sampling - extractive body cue:** During training, we use the calibrated Q-learning [49] to optimize the intermediate flow verifier φ.
- **p. 4 / 4.2. Cascaded Action Denoising - extractive body cue:** For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 6 (Model), p. 4 (4.1. Value-Guided Test-Time Sampling)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, robot control has stricter real-time requirements than text generation: extra inference computation can introduce delays, causing jitter or even task failure.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce FM-Steer, a framework that enhances flow-based VLA models at test time with value-guided test-time sampling and cascaded action denoising.
- **p. 8 / 6. Conclusion - extractive body cue:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.
- **p. 8 / 6. Conclusion - extractive body cue:** FM-Steer combines valueguided test-time sampling with effective best-of-N selection and cascaded action denoising, integrating the original VLA with a lightweight denoiser to achieve rapid and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of FM-Steer. FM-Steer augments a flow-based VLA with two modules: the intermediate flow verifier and the Lite- Flow denoiser. Given an observation, ...
- **p. 5 / 5.1. Implementation Details - extractive body cue:** FMSteer sets the noise-level bound T in the range of 0.7 to 0.9 and selects N = 5 candidates from the original VLA at each ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Experimental setups on WidowX, AgiBot G-1, and Franka. We evaluate FM-Steer across 3 simulation environments and 3 different real-world robotic platforms, covering 15 ...
- **Boundary to test:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving the robot control frequency. • We introduce value-guided ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves the highest average success rate and ranking, followed ... | p. 6 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Failure/limitation | The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies. | p. 8 (6. Conclusion), p. 8 (6. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 A flow-based VLA aims to model the data distribution p(At/ot), mapping the observation ot, which consists of images it, language instructions ℓt, and robot state information st, to a sequence of H ...를 For the k-th sub-action chunk Aτ ∗ t,k, it contains the noisy action from time step t + kh to t + (k + 1)h -1, and its corresponding observation is ot,k ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, the main contributions of this work are: • We propose FM-Steer, a test-time computing framework that enhances flow-based Vision-Language-Action models while improving the robot control frequency. • We introduce value-guided ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, VLA, test-time computation, value guidance, dexterous manipulation, real-time control`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction for generalist robot policies.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing frameworks..
3. Compare against the body-reported baseline or a matched simpler baseline: We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it with previous state-of-the-art generalist policies, including prior test-time computing frameworks..
4. Report the body metric and its denominator/aggregation: Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across four task suites. FM-Steer (π0) achieves the highest average success rate and ranking, followed ....
5. Re-run the body-reported ablation/failure condition: Table 3. Ablations on LIBERO and SimplerEnv. We conduct ablation studies across LIBERO [44] and SimplerEnv [39] on Wid- owX and Google Robot tasks. In the SimplerEnv experiments, models are trained with ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. Value-Guided Test-Time Sampling), p. 4 (4.2. Cascaded Action Denoising), p. 7 (5.3. Efficiency Improvement); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, main, contributions mechanism이 We study FM-Steer across diverse simulated and real-world robotic platforms, including humanoid robots, and compare it ... 대비 Table 1. LIBERO Benchmark Results. We present the success rate (SR) and standard error for each method across ...을 개선하고, The gains are especially clear on complex tasks that require failure recovery, highlighting a promising direction ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
