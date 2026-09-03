# Insights — Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://iclr.cc/virtual/2026/poster/10006732; PDF retrieval source: https://arxiv.org/pdf/2601.16163. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We evaluate our method in two modes: first as a direct policy (without planning) and then with model-based planning using the future state and value ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This search process produces trajectories that are more likely to succeed at the task Our main contribution is the Cosmos Policy approach for fine-tuning pretrained ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Rather than designing new model components or making architectural modifications as done in prior works, we propose to encode additional modalities as new latent frames ...
- **p. 5 / 3 PRELIMINARIES - extractive body cue:** To encode the new modalities as latent frames, we fill each H′ ×W ′ ×C′ latent volume with normalized and duplicated copies of the robot ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** Once we have the fine-tuned checkpoint for refined world modeling and policy learning, we propose dual deployment: the original Cosmos Policy checkpoint serves as the ...
- **p. 17 / A.2.2 LIBERO TRAINING DETAILS - extractive body cue:** (Note that these are single-step training losses given varying σ (noise levels) as input, rather than losses on generations from the multi-step diffusion sampling used ...
- **p. 21 / A.4.2 COSMOS POLICY INFERENCE LATENCY - extractive body cue:** Cosmos Policy first generates N candidate action chunks with 10 denoising steps each, then generates an ensemble of 3 future state predictions per action proposal ...
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 6 (3 PRELIMINARIES), p. 17 (A.2.2 LIBERO TRAINING DETAILS)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we address these limitations with Cosmos Policy: an effective robot policy that is adapted from a pretrained video model (Cosmos-Predict2-2B (NVIDIA et ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** We aggregate these via "majority mean": we determine whether the majority predict success or failure (via a fixed threshold) and then average values within the ...
- **p. 6 / 3 PRELIMINARIES - extractive body cue:** However, training on demonstrations alone is insufficient for effective planning since the data only covers successful outcomes,‡ which means that the world model and value ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** These spatiotemporal priors hold significant value for robotics applications.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** A world model ˆT : S × A →Π(S) learns to predict the future state given current state and action, approximating the true environment dynamics.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from ...
- **p. 18 / A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS - extractive body cue:** For OOD trials, we replace the pink ziploc bag with an unseen blue ziploc bag that is filled to about 75 percent full (more than ...
- **Boundary to test:** The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from the robot's self-occlusion and highly stochastic environment ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We evaluate our method in two modes: first as a direct policy (without planning) and then with model-based planning using the future state and value predictions. | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Reported outcome | Table 1: LIBERO simulation benchmark results. Success rates (SR) across four LIBERO benchmark task suites (Liu et al., 2024). Cosmos Policy success rates are averaged over 500 trials for each suite (10 ... | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS) |
| Failure/limitation | The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from the robot's self-occlusion and highly stochastic environment ... | p. 10 (5 EXPERIMENTS), p. 18 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation, uncertainty/risk estimate와 task command → safe set, recovery state 또는 constraint margin → shielded, recovery 또는 safe action`.
- 이 논문의 재사용 가능한 지점은 It does not support robot proprioception as input, robot actions or state values as output, nor multiple camera views-all of which are desired or required for manipulation policies.를 4 COSMOS POLICY: ADAPTING VIDEO MODEL FOR CONTROL & PLANNING In this section, we discuss how to adapt Cosmos-Predict2 into a unified model that predicts actions, future states, and values.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 safe set, recovery state 또는 constraint margin가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from the robot's self-occlusion and highly stochastic environment ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We evaluate our method in two modes: first as a direct policy (without planning) and then with model-based planning using the future state and value predictions.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, world model, visuomotor control, video model`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The additional episodes are important for this task since training an accurate world model for it is particularly challenging due to low camera observability from the robot's self-occlusion and highly stochastic environment ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The LIBERO benchmark (Liu et al., 2024) consists of a variety of environments and tasks featuring a single Franka Emika Panda robot arm..
3. Compare against the body-reported baseline or a matched simpler baseline: Our method achieves highest performance overall, even outperforming fine-tuned state-of-the-art vision-language-action (VLA) models..
4. Report the body metric and its denominator/aggregation: We use score instead of success rate since a binary metric does not capture fine-grained details. • "put X on plate": 50 points for touching the correct target object..
5. Re-run the body-reported ablation/failure condition: Table 4: Cosmos Policy ablations in LIBERO. Here we report the results of two independent ablations: (1) In Section 4.2, we discussed that Cosmos Policy's policy and world model training involves additional ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 17 (A.2.2 LIBERO TRAINING DETAILS), p. 21 (A.4.2 COSMOS POLICY INFERENCE LATENCY), p. 16 (A.2.1 COSMOS POLICY NOISE DISTRIBUTION); the primary result is directionally consistent at p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 19 (A.3.2 REAL-WORLD ALOHA ROBOT EVALUATION DETAILS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 evaluate, modes, first mechanism이 Our method achieves highest performance overall, even outperforming fine-tuned state-of-the-art vision-language-action (VLA) models. 대비 We use score instead of success rate since a binary metric does not capture fine-grained details. • "put ...을 개선하고, The additional episodes are important for this task since training an accurate world model for it ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
