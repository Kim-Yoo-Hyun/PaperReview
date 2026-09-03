# Insights — Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7BLXhmWvwF; PDF retrieval source: https://arxiv.org/pdf/2502.07005. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** The architecture's equivariance allows generalizing between poses and its heterogeneity enables us to include and exploit knowledge about the scene as well as the unactuated ...
- **p. 3 / 3 METHODOLOGY - extractive body cue:** To handle the complexities of robotic manipulation, where actuators and objects play distinct roles, we propose the Heterogeneous Equivariant Policy (HEPi), which comprises three key ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** For actuator nodes, the output consists of both a scalar c and a vector vout, where the final output vector is computed as vout = ...
- **p. 4 / 3 METHODOLOGY - extractive body cue:** Our approach captures these roles by first processing local information within the object and actuator clusters and then aggregating it globally to the actuators via ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** These node features may differ from those used in the policy network to capture task-specific observations.
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Trust-Region Projection Layers Standard on-policy reinforcement learning approaches such as Proximal Policy Optimization (PPO) (Schulman et al., 2017), learn a policy by optimizing the surrogate ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** They are designed to highlight the role of geometric structure in manipulation tasks, with a progressive increase in difficulty, from simple rigid-body manipulation with diverse ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike supervised imitation, training policies with reinforcement learning presents additional challenges, particularly due to the need for high-frequency data collection and efficient adaptation to new ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this paper, we frame manipulation problems as heterogeneous graphs.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Using Equivariant Message Passing Networks (EMPNs), they learn policies that generalize to different poses by leveraging the geometric structure of the scene.
- **p. 3 / 2 BACKGROUND - extractive body cue:** This allows leveraging symmetries to reduce the complexity of learning, potentially improving sample efficiency and generalization, as it results in a group-structured MDP homomorphism (Van ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements.
- **p. 10 / 6 CONCLUSION - extractive body cue:** This limitation could be addressed by integrating state-of-the-art computer vision techniques to extract keypoints from cameras (Tumanyan et al., 2024; Hou et al., 2024), using ...
- **Boundary to test:** Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., 2023) to utilize its GPU-based simulation engine. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Figure 4: Performance of different models on the Cloth-Hanging task across varying sample spaces. Overall, performance improves as the sample space decreases. In terms of final performance, het- erogeneous models outperform homogeneous ... | p. 8 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Failure/limitation | Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements. | p. 10 (6 CONCLUSION), p. 10 (6 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 Right: Overview of Heterogeneous Equivariant Policy (HEPi), consisting of multiple Equivariant Message Passing Networks (EMPNs) process the graph, and the outputs are aggregated to generate the final action. to reinforcement learning.를 In MDPs with symmetries, both the transition distribution P(s′/s, a) and policy distribution π(a/s) are invariant under group transformations g ∈G via left-regular representation Lg and Kg for state and action, respectively, ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To evaluate our approach and future advancements in this direction, we propose a novel suite of seven tasks, realized using NIVIDA IsaacLab (Mittal et al., 2023) to utilize its GPU-based simulation engine.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, Reinforcement Learning, SE(3) equivariance, deformable manipulation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Overall, HEPi generalizes well to unseen objects, performs consistently across resolutions, and handles noise effectively, making it suitable for real-world tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Figure 3: Evaluation curves for our seven manipulation tasks, comparing HEPi (ours), EMPN, and Transformer baselines. Results are averaged over 10 seeds, using IQM with 95% confidence intervals. HEPi consistently outperforms EMPN ....
4. Report the body metric and its denominator/aggregation: Full task details, including reward definitions, are provided in Appendix B..
5. Re-run the body-reported ablation/failure condition: Figure 23: Ablation on different k-nearest neighbors for obj-to-act edges in MPNN + VNLocal (in Section 3.3) updates, evaluated on the Rigid-Insertion task with varying message passing steps m ∈ {1, 2, ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 25 (Figure/Table caption), p. 9 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 evaluate, future, advancements mechanism이 Figure 3: Evaluation curves for our seven manipulation tasks, comparing HEPi (ours), EMPN, and Transformer baselines. ... 대비 Full task details, including reward definitions, are provided in Appendix B.을 개선하고, Limitation In our current setup, we abstract away the robot body, focusing solely on end-effector movements. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
