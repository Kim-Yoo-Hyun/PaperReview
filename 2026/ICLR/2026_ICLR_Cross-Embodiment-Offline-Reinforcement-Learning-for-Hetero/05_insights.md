# Insights — Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10010454; PDF retrieval source: https://arxiv.org/pdf/2602.18025. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 1 INTRODUCTION - extractive body cue:** 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we propose a novel group-task update strategy based on robot embodiment information.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** To address this issue, we propose a novel mitigation strategy that groups robots according to their embodiment, thus reducing gradient conflicts.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce and analyze the new benchmark that combines offline RL with crossembodiment learning across up to 16 distinct robot platforms.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** Specifically, we encode each action with an action encoder to obtain a latent action vector, which we then concatenate with the latent representation of the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For example, implicit Q-learning (IQL) (Kostrikov et al., 2021) first fits a state value function Vψ(s) via expectile regression to capture an upper expectile of ...
- **Contribution anchor:** p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION)

### Strongest assumption and failure boundary

- **p. 3 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce the new benchmark that systematically combines offline RL with cross-embodiment learning, analyze the interactions between these paradigms, and propose ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, despite the promise of foundation models for robotics, they face a critical limitation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Since collecting large datasets for any single robot is costly, pre-training on heterogeneous robot data has become a popular strategy to improve generalization capability (Open ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** To date, applications of offline RL to robot foundation models have been rare, owing to the difficulty of learning from unlabeled interaction data; thus, a ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Collecting manipulation data is time-consuming and expensive, and each new task requires careful teleoperation, specialized hardware, and often manual labeling, making data scaling difficult.
- **p. 10 / 7 CONCLUSION - extractive body cue:** We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments.
- **p. 10 / 7 CONCLUSION - extractive body cue:** We leave this combined direction for future work.
- **Boundary to test:** We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting. | p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | From the table, EG achieves the most stable and substantial improvement on the 70% Suboptimal Forward dataset (+14.41, +38.34%). | p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Failure/limitation | We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments. | p. 10 (7 CONCLUSION), p. 10 (7 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `dataset state/observation, action, reward와 return-to-go → Q/value 또는 sequence-policy state → dataset-supported action sequence`.
- 이 논문의 재사용 가능한 지점은 3 EXPERIMENTAL SETUP 3.1 PROBLEM SETTING We study multi-embodiment offline RL, where a single policy must control multiple robot morphologies under a common state-action interface.를 Finally, the policy πϕ(a / s) is extracted via advantage-weighted BC, avoiding any need to evaluate out-of-distribution actions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 Q/value 또는 sequence-policy state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: 3.3 NETWORK ARCHITECTURE In this section, we present our approach to cross-embodiment learning in an offline RL setting.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `RL, IL, offline learning, and robot data`; tags: `Robotics, offline reinforcement learning, cross-embodiment, transfer`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the proportion of suboptimal data and the number of embodiments.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Preprint (a) Embodiment-based similarity matrix (b) Average gradient cosine similarity matrix (c) Embodiment-based similarity vs. mean gradient cosine similarity Figure 3: (a) Embodiment-based similarity matrix (1 - min-max-normalized F ....
3. Compare against the body-reported baseline or a matched simpler baseline: Compared to the IQL cross-embodiment baseline, the average improvement in the Suboptimal datasets 70% is 7.15% for PCGrad, 18.33% for SEL and 33.99% for EG..
4. Report the body metric and its denominator/aggregation: Table 7: Reward coefficients rc and curriculum length T for each robot. C DATASET DETAIL Figure 7 overlays histograms of the total reward per episode for the Forward datasets, comparing the three ....
5. Re-run the body-reported ablation/failure condition: (ii) Sensitivity to the group count M We evaluate the effect of the number of Embodiment Grouping clusters M by sweeping M over {1, 2, 4, 7, 10, 13}..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 5 (1 INTRODUCTION); the primary result is directionally consistent at p. 9 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 NETWORK, ARCHITECTURE, section mechanism이 Compared to the IQL cross-embodiment baseline, the average improvement in the Suboptimal datasets 70% is 7.15% ... 대비 Table 7: Reward coefficients rc and curriculum length T for each robot. C DATASET DETAIL Figure 7 overlays ...을 개선하고, We also identified a core failure mode, inter-robot gradient conflicts, whose incidence grows with both the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
