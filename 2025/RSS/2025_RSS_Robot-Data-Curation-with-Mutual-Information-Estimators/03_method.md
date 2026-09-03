# Method - Robot Data Curation with Mutual Information Estimators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p023.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p023.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 18 (C. Implementation Derails), p. 18 (C. Implementation Derails), p. 4 (B. Maximizing Marginal Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 4 (B. Maximizing Marginal Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy)): For action encoders and decoders, we use the same architecture as for state.

## Method Body Digest

- **p. 18 / C. Implementation Derails - extractive body cue:** For action encoders and decoders, we use the same architecture as for state.
- **p. 18 / C. Implementation Derails - extractive body cue:** For all methods using a state encoder, we use this architecture.
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Having a high marginal action entropy avoids this pitfall, forcing the learned policy to pay attention to the state when making predictions, which is desirable ...
- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** Below, we use this fact to argue why low conditional action entropy H(A / $) (term 2 in Eq, (4) leads to better BC performance ...
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Fst, we begin by earning VAES fr states and action chuaks to produce Intent representations = and Using these lateatrepreseatations, we apply the KSG A-acarest-acighbor ...
- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** r Daa (PrllPee) <7 LTE, (Da oo lne (9) Innutivey, if we can keep the policies close enough to each other at every state, then ...
- **p. 19 / C. Implementation Derails - extractive body cue:** Method Parameter ___RoboMimic State _Robotimic Image Franka ReboCrowd
- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** [6], we can bound the di tribution matching objective from Eq.

## Design Rationale

- **p. 4 / V. MetHop - extractive body cue:** come this challenge we propose Demonstration Information Estimation, which uses k-nearest-neighbor (k-NN) estimates of mutual information, Our method involves three steps - representation learning, mutual ...
- **p. 4 / V. MetHop - extractive body cue:** In this section we propose the Demonstration Information Estimation (DemInf) method for computationally estimating mutual information for demonstration data, Though mutual information is usually considered ...
- **p. 1 / Abstract - extractive body cue:** Moreover, training polices based on data filtered bby our method leads to a §-10% improvement in RoboMimic and better performance on real ALOHA and Franka ...

## Source Evidence Cues

- **p. 18 / C. Implementation Derails - extractive body cue:** For action encoders and decoders, we use the same architecture as for state.
- **p. 18 / C. Implementation Derails - extractive body cue:** For all methods using a state encoder, we use this architecture.
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Having a high marginal action entropy avoids this pitfall, forcing the learned policy to pay attention to the state when making predictions, which is desirable ...
- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** Below, we use this fact to argue why low conditional action entropy H(A / $) (term 2 in Eq, (4) leads to better BC performance ...
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Fst, we begin by earning VAES fr states and action chuaks to produce Intent representations = and Using these lateatrepreseatations, we apply the KSG A-acarest-acighbor ...
- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** r Daa (PrllPee) <7 LTE, (Da oo lne (9) Innutivey, if we can keep the policies close enough to each other at every state, then ...
- **p. 19 / C. Implementation Derails - extractive body cue:** Method Parameter ___RoboMimic State _Robotimic Image Franka ReboCrowd
- **Detected method headings:** B. Method Details (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | For action encoders and decoders, we use the same architecture as for state. | p. 18 (C. Implementation Derails), p. 18 (C. Implementation Derails) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | For all methods using a state encoder, we use this architecture. | p. 18 (C. Implementation Derails), p. 4 (B. Maximizing Marginal Action Entropy) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | Having a high marginal action entropy avoids this pitfall, forcing the learned policy to pay attention to the state when making predictions, ... | p. 4 (B. Maximizing Marginal Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** [6], we can bound the di tribution matching objective from Eq.
- **p. 3 / A. Minimizing Conditional Action Entropy - extractive body cue:** Our overall objective is to align the distribution of the learned policy with that of expert data (Eq.
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** In addition to minimizing conditional action entropy, mutual information encourages high entropy in the marginal action distribution H(A) (the frst term of Eq.
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Without considering the marginal entropy of actions H(A), the conditional entropy H(A/S) could be trivially minimized by distributions that have constant actions, e.g. taking the ...
- **p. 18 / C. Implementation Derails - extractive body cue:** For BC policies we ensemble the MLP. add dropout and use the L2 Loss function for training.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (A. Minimizing Conditional Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 18 (C. Implementation Derails).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contrast, believe, metrics, imitation, learning, should, able, measure, relative, predictability, state-action, distribution, directly, affects | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | contrast, believe, metrics, imitation, learning, should, able, measure, relative, predictability | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | come, challenge, Demonstration, Information, Estimation, uses, k-nearest-neighbor, k-NN, estimates, mutual | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | bound, tribution, matching, objective, overall, align, distribution, learned, policy, expert | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Iyrropucrion - extractive body cue:** In contrast, we believe metrics for imitation learning should be able to measure the relative predictability of the state-action distribution directly, which affects how well ...
- **p. 2 / A. Imitation Learning - extractive body cue:** Broadly, the objective of imitation learning is to learn a policy x» : S > A parameterized by 6 that is able to effectively reproduce ...
- **p. 3 / B. Demonstration Curation - extractive body cue:** In BC, we want to train a policy ‘to to predict the action a from the state s. ‘Thus the mutual information between states and ...
- **p. 4 / B. Maximizing Marginal Action Entropy - extractive body cue:** Having a high marginal action entropy avoids this pitfall, forcing the learned policy to pay attention to the state when making predictions, which is desirable ...
- **p. 1 / Abstract - extractive body cue:** Kenearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions.
- **p. 2 / A. Imitation Learning - extractive body cue:** Typically, we measure the similarity between the policy and expert using a divergence between their state visitation distributions:
- **p. 3 / B. Demonstration Curation - extractive body cue:** where $ and A represent random variables for the state and action.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | ‘Opuimizer ‘Adar Leaning Rate o0e01 1 Batch Size 256, A Training Steps 50,000 100,000 tion Chunk n 1 4 0 Image Resolution ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | (1) using the log-sum inequality in terms of the divergence between the learned policy and expert policy at each time step: | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | State-based models are trained for 50,000 steps and image based models are trained for 100,000 steps using VMs provided by a Google ... | hardware, batch and throughput |

## Training vs Inference

- **p. 19 / C. Implementation Derails - extractive body cue:** ‘Opuimizer ‘Adar Leaning Rate o0e01 1 Batch Size 256, A Training Steps 50,000 100,000 tion Chunk n 1 4 0 Image Resolution oss.
- **p. 7 / A. Experimental Setup - extractive body cue:** When training VAEs from images we use matching ResNet-18 Decoder networks for ‘each view.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** action, encoders, decoders, same, architecture, state, methods, encoder, Having, high, marginal, entropy, avoids, pitfall, forcing, learned, policy, attention, when, making.
- **Relevant PDF headings:** B. Method Details (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | The multi-human datasets from the RoboMimic benchmark [50] include 100 demonstrations from each of three robot operators for three tasks in increasing ... | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Policy fitting | 2) Baselines: We compare against a number of different data quality estimators from prior work in addition to a number of alternative ... | p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup) |
| Closed-loop rollout | Following Gandhi et al, [25], we use a measure of demonstration "compatibility" to score data. | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |

## Failure and Ablation Link

- **p. 6 / A. Experimental Setup - extractive body cue:** We additionally evaluate on versions of these datasets ("HiChew", "TootsieRoll, "HersheyKiss") where the unstructured play data has been removed, but where demonstrations still contain task-relevant ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 17. The effect of difereat values of VAE on RoboMimic Image. We find that performance is relatively robust to this parameter for RoboMimic.
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 16. The effect of diferent lateat dimension sizes for 5 and =, 0a RoboMimic Image. we fad that performance is relatively sobust to this ...
- **p. 8 / C. Mutual Information Estimators - extractive body cue:** variance across seeds, while the parametric estimators were more unstable and had one or two runs that performed far worse than the others.
- **p. 6 / A. Experimental Setup - extractive body cue:** Note that while this metric makes sense for active learning, it does not necessarily make sense in the offline setting, and in some ways may ...
- **p. 8 / C. Mutual Information Estimators - extractive body cue:** This is particularly problematic for downstream data curation, as one often does not have ground truth labels to check the quality of the scoring function,
- **p. 9 / C. Mutual Information Estimators - extractive body cue:** DemInf's performance is generally robust to this parameter, with no substantial change in performance in both HersheyKiss and Square MH.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 18 (C. Implementation Derails), p. 18 (C. Implementation Derails), p. 4 (B. Maximizing Marginal Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 4 (B. Maximizing Marginal Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), objective p. 3 (A. Minimizing Conditional Action Entropy), p. 3 (A. Minimizing Conditional Action Entropy), p. 4 (B. Maximizing Marginal Action Entropy), p. 4 (B. Maximizing Marginal Action Entropy), p. 18 (C. Implementation Derails), temporal p. 19 (C. Implementation Derails), p. 3 (A. Minimizing Conditional Action Entropy), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 18 (C. Implementation Derails).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
