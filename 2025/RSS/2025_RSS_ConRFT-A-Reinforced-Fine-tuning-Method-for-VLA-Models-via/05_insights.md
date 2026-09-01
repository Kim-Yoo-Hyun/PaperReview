# Insights — ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p019.html; PDF retrieval source: https://arxiv.org/pdf/2502.05450. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To leverage the benefits of RL-based techniques for efficiently fine-tuning VLA models with online interaction data, we propose a reinforced fine-tuning (RFT) approach consisting of ...
- **p. 2 / IV. METHOD - extractive body cue:** The proposed pipline ConRFT consists of two stages: offline fine-tuning followed by online fine-tuning to optimize robotic policies, as shown in Fig.
- **p. 3 / IV. METHOD - extractive body cue:** To address this issue, we propose augmenting the offline training process by incorporating a BC loss.
- **p. 3 / IV. METHOD - extractive body cue:** Motivated by combining the BC loss with Q guidance under a consistency-based objective [18], we introduce Cal-ConRFT in the offline stage.
- **p. 4 / IV. METHOD - extractive body cue:** As a result, we use a standard Q loss for online critic updating: Lonline Q (θ) = E(s,a,s′)∼(D∪R)[(Qθ(s, a) -BπQ(s, a))2] (4) The consistency-based training ...
- **p. 4 / IV. METHOD - extractive body cue:** The consistency policy is a diffusion-model-based policy [46] that learns to map random actions sampled from the unit Gaussian to generate actions drawn from the ...
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, extending these insights to VLA models presents unique challenges because, unlike LLMs, VLA models necessitate direct physical interaction in real-world robotic tasks.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In the subsequent online stage, we solve two challenges of sample efficiency and real-world safety requirements by exploiting task-specific rewards with CPQL [18] under human ...
- **p. 8 / VI. LIMITATIONS - extractive body cue:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.
- **p. 6 / V. EXPERIMENT AND RESULTS - extractive body cue:** While HG-DAgger leverages human corrections to fine-tune the VLA model through supervised learning, it fails to achieve significant policy improvement and even experiences a performance ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing ...
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** They also show the limitations of supervised methods in handling sub-optimal data and efficient policy exploration.
- **p. 7 / V. EXPERIMENT AND RESULTS - extractive body cue:** However, it fails to improve the policy performance in contact-rich tasks that require precise, careful manipulation, such as Insert Wheel.
- **Boundary to test:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency policy through ... | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Figure 3. Our approach, ConRFT, achieves the highest average success rate of 96.3% after 45 to 90 minutes of real-world training across all tasks, representing a 144% improvement over the supervised baseline. ... | p. 6 (Figure/Table caption), p. 8 (V. EXPERIMENT AND RESULTS) |
| Failure/limitation | Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain. | p. 8 (VI. LIMITATIONS), p. 6 (V. EXPERIMENT AND RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 To address these issues, we formulate each robotic task as a Markov Decision Process (MDP), where the goal of RL is to find the optimal policy in the MDP, M = (S, ...를 The consistency policy is a diffusion-model-based policy [46] that learns to map random actions sampled from the unit Gaussian to generate actions drawn from the expert action distribution conditioned on the current ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency policy through ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Reinforcement Learning, human interventions, consistency policy, real-world manipulation, fine-tuning`.
- **Reading predecessor in the generated track queue:** NaVILA: Legged Robot Vision-Language-Action Model for Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative real-world tasks, displayed as a running average over ....
3. Compare against the body-reported baseline or a matched simpler baseline: For the online stage, we compared HIL-ConRFT with multiple baselines, including HG-DAgger [19] that incorporates human corrections to fine-tune the policy through supervised learning, PA-RL [14] that optimized actions through a policy-a ....
4. Report the body metric and its denominator/aggregation: This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective and stable policy improvement with a small set ....
5. Re-run the body-reported ablation/failure condition: This ability to fine-tune the action generation while leveraging the pretrained visual components underscores the broad applicability of ConRFT..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. METHOD), p. 3 (IV. METHOD), p. 3 (IV. METHOD); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 8 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Motivated, insights, CPQL mechanism이 For the online stage, we compared HIL-ConRFT with multiple baselines, including HG-DAgger [19] that incorporates human ... 대비 This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during ...을 개선하고, Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
