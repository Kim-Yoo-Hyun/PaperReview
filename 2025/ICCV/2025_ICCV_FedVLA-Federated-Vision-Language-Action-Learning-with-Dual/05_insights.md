# Insights — FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the ...
- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions in this work can be summarized as follows: • We propose FedVLA, the first privacy-preserving federated learning framework for VLA training, ensuring ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike traditional centralized training, which requires aggregating all user data on a central server, FL enables distributed model training across multiple clients without transferring raw ...
- **p. 1 / 1. Introduction - extractive body cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...
- **p. 5 / 3.4. Algorithms - extractive body cue:** The aggregated global trunk module is then redistributed to clients for the next training round.
- **p. 5 / 3.4. Algorithms - extractive body cue:** At the start of each training round t, each client processes task-specific data using Instruction-Oriented Scene-Parsing to extract structured features, followed by Dual Gating MoE ...
- **p. 6 / 3.4. Algorithms - extractive body cue:** Algorithm 2 FedVLA: Server Input: T is the number of training rounds. θ represents the global trunk parameters.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, existing methods typically select a fixed number of experts, lacking adaptability to tasks of varying complexity.
- **p. 2 / 1. Introduction - extractive body cue:** These limitations highlight the need for a task-adaptive and flexible FL framework, specifically designed for multi-modal robotic learning.
- **p. 1 / 1. Introduction - extractive body cue:** Our federated VLA framework enables decentralized training on user devices, preserving privacy while utilizing expertdriven aggregation to enhance model generalization across diverse tasks. enabling robots ...
- **p. 6 / 4. Experiments - extractive body cue:** For evaluation, the success and failure of a trial are recoreded as 1 and 0.
- **p. 6 / 4.1. Simulation - extractive body cue:** For collision detection and dynamics simulation, we employ official physics engines to ensure accurate robotic interactions within the simulation environment.
- **p. 7 / 4.3. Ablation Studies - extractive body cue:** The integration of these modules together results in a architecture that supports FedVLA's robustness and adaptability across diverse tasks.
- **Boundary to test:** For evaluation, the success and failure of a trial are recoreded as 1 and 0.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the Dual Gating Mixture-of-Experts, where ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. | p. 6 (4.1. Simulation), p. 6 (Figure/Table caption) |
| Failure/limitation | For evaluation, the success and failure of a trial are recoreded as 1 and 0. | p. 6 (4. Experiments), p. 6 (4.1. Simulation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 In contrast, VLA models operate in multi-modal environments, requiring the joint processing of visual observations, language instructions, and robotic actions, which significantly increases the complexity of federated training.를 IOSP decomposes observation images into object-level representations guided by task instructions and leverages vision-language alignment techniques to improve contextual understanding.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 For evaluation, the success and failure of a trial are recoreded as 1 and 0.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Extensive experiments in both simulation and real-world environments demonstrate that FedVLA achieves performance comparable to centralized training while preserving data privacy. • We introduce the Dual Gating Mixture-of-Experts, where ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** For evaluation, the success and failure of a trial are recoreded as 1 and 0.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We collect real-world robotic demonstrations for household-related tasks, including Clean Up, Trash Collection, Open Drawer, and Sorting Pills, as shown in Figure 4..
3. Compare against the body-reported baseline or a matched simpler baseline: Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%..
4. Report the body metric and its denominator/aggregation: We compare the task success rate and record the validation loss during the training process..
5. Re-run the body-reported ablation/failure condition: To further explore the effectiveness of the IOSP, DGMOE and EDA in FedVLA, we conduct ablation experiments by individually removing each module while keeping the other components..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. Algorithms), p. 5 (3.4. Algorithms), p. 6 (3.4. Algorithms); the primary result is directionally consistent at p. 6 (4.1. Simulation), p. 6 (Figure/Table caption), p. 7 (4.2. Real-World); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Extensive, experiments, simulation mechanism이 Furthermore, FedVLA consistently outperforms FedAvg, which only achieves an average success rate of 51.7%. 대비 We compare the task success rate and record the validation loss during the training process.을 개선하고, For evaluation, the success and failure of a trial are recoreded as 1 and 0. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
