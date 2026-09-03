# Method - SAFE: Multitask Failure Detection for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (4 Method), p. 4 (4 Method), p. 4 (4 Method)): Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 𝒆1 LSTM 𝑠1 𝒆2 LSTM ...

## Method Body Digest

- **p. 5 / 4 Method - extractive body cue:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 ...
- **p. 4 / 4 Method - extractive body cue:** 4.1 Visual Analysis on VLA Latent Space VLAs process multi-modal inputs and extract rich semantic information in their internal feature space.
- **p. 4 / 4 Method - extractive body cue:** We study this hypothesis by visualizing the VLA features in Fig.
- **p. 4 / 4 Method - extractive body cue:** 1(c) further illustrates how VLA's features evolve in the feature space when VLA progresses temporally.
- **p. 4 / 4 Method - extractive body cue:** 1(c), we can see that failure rollout initially stays out of the "failure zone" when it progresses normally, and when the robot mistakenly drops the ...
- **p. 1 / 1 Introduction - extractive body cue:** Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions ...
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and ...
- **p. 4 / 4 Method - extractive body cue:** 1(b), we can further see that although the features are extracted from different tasks with various instructions, objects and environments, when the VLA fails, its ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and ...
- **p. 2 / 1 Introduction - extractive body cue:** Based on this insight, we introduce SAFE, a ScAlable Failure Estimation method that scales across diverse tasks for generalist policies like VLAs.
- **p. 1 / 1 Introduction - extractive body cue:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.

## Source Evidence Cues

- **p. 5 / 4 Method - extractive body cue:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 ...
- **p. 4 / 4 Method - extractive body cue:** 4.1 Visual Analysis on VLA Latent Space VLAs process multi-modal inputs and extract rich semantic information in their internal feature space.
- **p. 4 / 4 Method - extractive body cue:** We study this hypothesis by visualizing the VLA features in Fig.
- **Detected method headings:** 4 Method (p. 4); B.1 Vision-Language-Action Models (p. 23)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 ... | p. 5 (4 Method), p. 4 (4 Method) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | 4.1 Visual Analysis on VLA Latent Space VLAs process multi-modal inputs and extract rich semantic information in their internal feature space. | p. 4 (4 Method), p. 4 (4 Method) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | We study this hypothesis by visualizing the VLA features in Fig. | p. 4 (4 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4 Method - extractive body cue:** 1(c) further illustrates how VLA's features evolve in the feature space when VLA progresses temporally.
- **p. 4 / 4 Method - extractive body cue:** 1(c), we can see that failure rollout initially stays out of the "failure zone" when it progresses normally, and when the robot mistakenly drops the ...
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Encoder, Decoder, Action, Observation, Instruction, VLA, Model, SAFE-MLP, SAFE-LSTM, MLP, LSTM, Recently, scaling, robot | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | Encoder, Decoder, Action, Observation, Instruction, VLA, Model, SAFE-MLP, SAFE-LSTM, MLP | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | contributions, summarized, follows, analyze, VLA, feature, space, across, different, task | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | further, illustrates, VLA, features, evolve, feature, space, when, progresses, temporally | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4 Method - extractive body cue:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 ...
- **p. 1 / 1 Introduction - extractive body cue:** Recently, scaling up robot manipulation datasets has enabled the development of large visionlanguage-action (VLA) models, which are generalist manipulation policies that can follow language instructions ...
- **p. 2 / 1 Introduction - extractive body cue:** The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions and ...
- **p. 4 / 4 Method - extractive body cue:** 4.1 Visual Analysis on VLA Latent Space VLAs process multi-modal inputs and extract rich semantic information in their internal feature space.
- **p. 4 / 4 Method - extractive body cue:** 1(b), we can further see that although the features are extracted from different tasks with various instructions, objects and environments, when the VLA fails, its ...
- **p. 1 / 1 Introduction - extractive body cue:** VLAs are designed to accomplish diverse tasks and may frequently encounter novel task instructions and unseen environments during deployment.
- **p. 2 / 1 Introduction - extractive body cue:** Experiments show that SAFE outperforms baselines and achieves state-of-the-art (SOTA) performance.
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | 1(c), we can see that failure rollout initially stays out of the "failure zone" when it progresses normally, and when the robot ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | At timestep t, a VLA is given an input observation ot, consisting of RGB images, natural language instruction, and current robot state, ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | For instance, pi0 has 3.3 billion parameters and an inference time of 149 ms. | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / 6 Results - extractive body cue:** For instance, pi0 has 3.3 billion parameters and an inference time of 149 ms.
- **p. 10 / 6 Results - extractive body cue:** For example, SAFE-LSTM contains 2.3 million parameters and introduces an additional 0.73 ms of inference time.
- **p. 4 / 4 Method - extractive body cue:** 1(c), we can see that failure rollout initially stays out of the "failure zone" when it progresses normally, and when the robot mistakenly drops the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Encoder, Decoder, Action, Observation, Instruction, VLA, Model, SAFE-MLP, SAFE-LSTM, MLP, LSTM, Visual, Analysis, Latent, Space, VLAs, process, multi-modal, inputs, extract.
- **Relevant PDF headings:** 4 Method (p. 4); B.1 Vision-Language-Action Models (p. 23).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator ... | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Filtering / recovery | Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still ... | p. 9 (6 Results), p. 27 (Figure/Table caption) |
| Monitoring / re-entry | 75.54 53.93 82.37 70.00 Euclid. k-NN 80.35 60.27 72.01 53.64 Cosine k-NN 80.23 59.51 74.76 65.88 PCA-KMeans 49.98 51.03 75.62 47.22 RND ... | p. 10 (6 Results), p. 10 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 5 Experiments - extractive body cue:** On SimplerEnv, we test pretrained π0 models from a reproduction [64], which we denote as π∗ 0 in this paper.
- **p. 6 / 5 Experiments - extractive body cue:** Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our lab.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: The proposed failure detector, SAFE, has three major components: (1) SAFE extracts the latent feature from the last layer of a VLA model; ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding camera observations from simulation experiments. The blue-shaded ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that the failure detection method does not apply. ...
- **p. 5 / 3. Calibrate failure detection - extractive body cue:** Inspired by this observation, we design SAFE, which uses the internal features of VLAs for failure detection.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (4 Method), p. 4 (4 Method), p. 4 (4 Method), objective p. 4 (4 Method), p. 4 (4 Method), temporal p. 4 (4 Method), p. 3 (2 Related Work), p. 4 (2 Related Work), p. 5 (3. Calibrate failure detection), p. 8 (0 SimplerEnv), p. 9 (0 SimplerEnv).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ǁ𝑠𝑇 𝒆1 LSTM 𝑠1 𝒆2 LSTM ... (p. 5, 4 Method).
- **Objective/update evidence:** We study this hypothesis by visualizing the VLA features in Fig. (p. 4, 4 Method).
- **Temporal/runtime evidence:** 1(c), we can see that failure rollout initially stays out of the "failure zone" when it progresses normally, and when the robot mistakenly drops the pot in the middle of ... (p. 4, 4 Method).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
