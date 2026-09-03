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

- **Paper-specific interface:** By coupling the VLA policy with the learned Q-function, RFT allows the VLA model to refine its behavior based on trial-and-error interactions and task-specific feedback. (p. 2, III. PROBLEM SETUP AND PRELIMINARIES).
- **Paper-specific mechanism:** Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency ... (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective and stable policy improvement with a ... (p. 8, V. EXPERIMENT AND RESULTS); the relevant task/metric cue is As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, improving the success rates across multiple robotic tasks. (p. 8, V. EXPERIMENT AND RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain. (p. 8, VI. LIMITATIONS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `VLA, Reinforcement Learning, human interventions, consistency policy, real-world manipulation, fine-tuning`.
- **Reading predecessor in the generated track queue:** NaVILA: Legged Robot Vision-Language-Action Model for Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: By coupling the VLA policy with the learned Q-function, RFT allows the VLA model to refine its behavior based on trial-and-error interactions and task-specific feedback. (p. 2, III. PROBLEM SETUP AND PRELIMINARIES); preserve the objective/update rule: Motivated by combining the BC loss with Q guidance under a consistency-based objective [18], we introduce Cal-ConRFT in the offline stage. (p. 3, IV. METHOD).
2. Use the paper-reported task/data/environment cue: This figure presents the success rates, intervention rates, and episode lengths for HIL-SERL [20], HG-DAgger [19], PA-RL [14] and our method across five representative real-world tasks, displayed as a running ... (p. 6, V. EXPERIMENT AND RESULTS).
3. Compare against the reported or matched baseline: For the online stage, we compared HIL-ConRFT with multiple baselines, including HG-DAgger [19] that incorporates human corrections to fine-tune the policy through supervised learning, PA-RL [14] that optimized actions through ... (p. 6, V. EXPERIMENT AND RESULTS).
4. Report the body metric with its denominator and aggregation: As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, improving the success rates across multiple robotic tasks. (p. 8, V. EXPERIMENT AND RESULTS).
5. Re-run the reported ablation or stress/failure condition: PA-RL is implemented without human intervention. (p. 6, V. EXPERIMENT AND RESULTS); if none is reported, design one around: Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain. (p. 8, VI. LIMITATIONS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 8 (V. EXPERIMENT AND RESULTS), p. 7 (V. EXPERIMENT AND RESULTS), p. 8 (V. EXPERIMENT AND RESULTS), and measure the boundary at p. 8 (VI. LIMITATIONS), p. 6 (V. EXPERIMENT AND RESULTS).

## Falsifiable research question

Under the paper's stated interface (By coupling the VLA policy with the learned Q-function, RFT allows the VLA model to refine its behavior based on trial-and-error interactions ...), does the paper-specific mechanism (Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage ...) retain the reported evaluation outcome (As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, ...) when tested against the paper's strongest explicit boundary (Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (As shown in Table IV, the results indicate that ConRFT can effectively enhance the performance of various VLAs, ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Motivated by insights from CPQL [18], we propose a unified training objective that integrates supervised learning with Qlearning in the offline stage and further fine-tunes the VLA model via consistency ... (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** This suggests that Cal-ConRFT enables quicker adaptation of the online learning process by leveraging the Q loss during the offline stage, allowing more effective and stable policy improvement with a ... (p. 8, V. EXPERIMENT AND RESULTS).
- **Strongest explicit boundary:** Although our approach demonstrates strong performance and sample efficiency for fine-tuning VLA models in realworld manipulation tasks, several limitations remain. (p. 8, VI. LIMITATIONS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
