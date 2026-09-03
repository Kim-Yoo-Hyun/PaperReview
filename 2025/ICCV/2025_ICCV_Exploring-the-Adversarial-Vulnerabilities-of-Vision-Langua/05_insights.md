# Insights — Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom.
- **p. 3 / 3. Methodology - extractive body cue:** Finally, we introduce the Normalized Action Discrepancy (NAD) metric in §3.5.
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** To exacerbate action discrepancies, we introduce the Untargeted Action Discrepancy Attack (UADA), which aims to maximize deviations in robot actions.
- **p. 4 / 3.3. Untargeted Position-aware Attack - extractive body cue:** Recognizing the importance of Ap = DT(yp) in controlling the end-effector's path, we introduce a position-aware attack to disrupt the intended movement trajectory.
- **p. 4 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** Instead of directly using yi adv as the misclassification target, we introduce a soft attack objective to capture the discrepancy between actions, ensuring smooth gradient ...
- **p. 3 / 3.1. Preliminary - extractive body cue:** By categorizing action values into discrete class labels, the model converts continuous probability outputs into discrete signals, this simplification facilitates quicker convergence and faster training ...
- **p. 3 / 3.2. Untargeted Action Discrepancy Attack - extractive body cue:** To define UADA's objective, we first identify the most distant action yi adv, which maximizes the discrepancy from the i-th DoF ground truth action yi.
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3.2. Untargeted Action Discrepancy Attack), p. 4 (3.3. Untargeted Position-aware Attack), p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.1. Preliminary)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This offers valuable insights for the research community to explore systemic failures in similar concurrent generative foundation models;  We rigorously evaluate our approach in ...
- **p. 1 / 1. Introduction - extractive body cue:** Failure Rate Comparison BV2 LIBERO A.
- **p. 1 / 1. Introduction - extractive body cue:** Comparison of failure rates across different attack schemes (UADA, UPA, and TMA).
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, our work intensifies the adversarial threats posed to VLA-based systems by both developing specialized attack objectives and designing effective attack methods.
- **p. 3 / 3.1. Preliminary - extractive body cue:** This control design presents a unique challenge for adversarial attacks, as finely divided bins result in minimal action discrepancies between neighboring bins (e.g., ±0.007/bin).
- **p. 6 / 4.3. Main Result - extractive body cue:** Both UADA and UPA effectively disrupt robot execution, yielding maximum average failure rates of 100% and 89.7%, respectively.
- **p. 6 / 4.3. Main Result - extractive body cue:** For UADA and UPA, our methods effectively amplify action discrepancies, leading to a notable transfer attack ability in increasing failure rates (see Tab.
- **Boundary to test:** Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ated by proposed methods. (C). Compa ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom. | p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Reported outcome | Specifically, while attacking DoF1 and DoF1∼3 in the Simulation setup, UADA and UPA achieve NAD of 21.0% and 14.5%, significantly outperforming UMA scenarios with increments of 6.9% and 3.1%, respectively. | p. 6 (4.3. Main Result), p. 8 (4.3. Main Result) |
| Failure/limitation | Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ated by proposed methods. (C). Compa ... | p. 1 (Figure/Table caption), p. 6 (4.3. Main Result) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 2) are built on large language models integrated with visual encoders, enabling robots to interpret human instructions and process visual input from a camera to perform context-aware actions.를 This attack is based on the observation that larger robot actions usually correlate with intense physical movements, which, in turn, may amplify the potential for real-world hazards [28-30].로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ated by proposed methods. (C). Compa ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Additionally, we introduce Geometry-Aware Objective that considers the robot's movement in three-dimensional space, characterized by three degrees of freedom.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic task execution. (B). Example of semantic-rich adversarial patches gener- ated by proposed methods. (C). Compa ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The increased variability in real-world data, including environmental complexity, object diversity, and task difficulty, allows the robot more opportunities to generate larger action discrepancies within the validation dataset..
3. Compare against the body-reported baseline or a matched simpler baseline: Therefore, we adapt prior work in adversarial learning as one of our baseline methods [66]..
4. Report the body metric and its denominator/aggregation: Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of our patches in physical-world applications as well without the need for further adaptations..
5. Re-run the body-reported ablation/failure condition: Subsequently, we evaluate the performance of generated adversarial patches on victim models (i.e., OpenVLA LIBERO variants) trained on different tasks suites to rigorously prove the robustness and effectiveness of our method..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Untargeted Action Discrepancy Attack), p. 3 (3.1. Preliminary), p. 3 (3.2. Untargeted Action Discrepancy Attack); the primary result is directionally consistent at p. 6 (4.3. Main Result), p. 8 (4.3. Main Result), p. 8 (4.4. Diagnostic Experiment); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Additionally, introduce, Geometry-Aware mechanism이 Therefore, we adapt prior work in adversarial learning as one of our baseline methods [66]. 대비 Although this success rate is lower than the corresponding digital-world performance (i.e., 100%), it highlights the effectiveness of ...을 개선하고, Figure 1. Adversarial Vulnerabilities induced by malicious ma- nipulation. (A). Illustration of adversarial threats in robotic ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
