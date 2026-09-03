# Method - Offline Imitation Learning Through Graph Search and Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p054.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p054.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING)): To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation.

## Method Body Digest

- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** Implementation and Time Complexity We use R3M [33] as pretrained feature since it is pretrained with a contrastive objective, which we find can represent fine-grained ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** We use 3 workspace cameras with 256 × 256 RGB observation, highlighting the challenge in perception especially for our considered precise manipulation tasks. the appendix.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Overview For simplicity, let us first consider the problem of defining w(o, a) in a tabular case where we want the agent to reach a ...
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Obviously, for any observation o, the agent should pick an action a whose resulting next observation (more
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Here, the cost function is the number of steps taken to reach og.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To specify the task objective conveniently, we also add a "virtual" goal vertex g to V.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** As a direct approach that uses graph search rather than deep RL, our method enjoys high time efficiency.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We also provide various quantitative and qualitative analyses to show that our method is capable of identifying good behaviors in the dataset.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** We introduce the implementation details in the remaining sections.

## Source Evidence Cues

- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** Implementation and Time Complexity We use R3M [33] as pretrained feature since it is pretrained with a contrastive objective, which we find can represent fine-grained ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** We use 3 workspace cameras with 256 × 256 RGB observation, highlighting the challenge in perception especially for our considered precise manipulation tasks. the appendix.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Overview For simplicity, let us first consider the problem of defining w(o, a) in a tabular case where we want the agent to reach a ...
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Obviously, for any observation o, the agent should pick an action a whose resulting next observation (more
- **Detected method headings:** IV. POLICY LEARNING (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Fixed-data support | 온라인 탐색 없이 transition/action 분포를 정의한다 | offline trajectories와 metadata | dataset support, behavior distribution과 task return을 정리 | training batch/support | To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation. | p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING) |
| Value / uncertainty update | dataset 밖 action의 과대추정을 억제한다 | batch transition과 value parameters | conservative, implicit, uncertainty 또는 behavior-regularized update를 수행 | Q/V/uncertainty estimate | Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set ... | p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING) |
| Policy extraction / deployment | 학습된 value를 실행 action으로 변환한다 | value와 behavior support | argmax, advantage weighting, sequence decoding 또는 constraint filtering을 적용 | dataset-supported action | Implementation and Time Complexity We use R3M [33] as pretrained feature since it is pretrained with a contrastive objective, which we find ... | p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Here, the cost function is the number of steps taken to reach og.
- **p. 3 / IV. POLICY LEARNING - extractive body cue:** Overview For simplicity, let us first consider the problem of defining w(o, a) in a tabular case where we want the agent to reach a ...
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To specify the task objective conveniently, we also add a "virtual" goal vertex g to V.
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** We perform finetuning with a time-contrastive learning objective in simulated experiments and find that it improves the robustness to the selection of hyperparameters.
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** Implementation and Time Complexity We use R3M [33] as pretrained feature since it is pretrained with a contrastive objective, which we find can represent fine-grained ...
- **Formal bridge:** dataset transition (s,a,r,s′) -> dataset-supported policy action -> offline value with OOD control -> offline return and deployment safety.
- **Equation/algorithm anchors:** p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | define, where, advantage, taking, action, observation, corresponds, policy, extraction, objective, Advantage-Weighted, Regression, AWR, Implicit | dataset state/observation, action, reward와 return-to-go | body cue; exact tensor/frame verify |
| State/latent | define, where, advantage, taking, action, observation, corresponds, policy, extraction, objective | Q/value 또는 sequence-policy state | body cue; notation verify |
| Action/output | direct, uses, graph, search, rather, deep, enjoys, high, time, efficiency | dataset-supported action sequence | body cue; unit/decoder verify |
| Objective/constraint | Algorithm, GSR, Optional, Finetune, pretrained, Build, graph, procedure, Section, IV-B | offline value with OOD control | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PRELIMINARIES - extractive body cue:** If we define w(o, a) = exp(A(o, a)) where A is the advantage of taking action a at observation o, this corresponds to the policy ...
- **p. 3 / III. PRELIMINARIES - extractive body cue:** Each trajectory τ is a sequence of observations o0:T and corresponding actions a0:T , i.e., τ = (o0, a0, o1, a1, ..., oT , aT ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In the experiments, we test our method in both simulation and real-world robotic manipulation tasks of various visual and physical complexities, involving high-resolution, multiview camera ...
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** For the real-world continuous control problem, each encountered observation is unique in the human demonstration dataset D, and we have the following two problems: (1) ...
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The desired learning algorithm should be able to pick up those good segments and recover this desired policy, which is also known as trajectory stitching ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** With this function, we bias the action toward the better ones for each v.
- **Normalized interface:** observation=dataset state/observation, action, reward와 return-to-go; state=Q/value 또는 sequence-policy state; output/action=dataset-supported action sequence.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | offline trajectory/discounted return horizon; deployment horizon과 분리한다. | This task features both precise manipulation and long-horizon control. | episode/sequence/action-chunk boundary |
| Rate / latency | training은 batch update, inference는 environment control tick; exact values 확인 필요. | We use the following two dataset setup: Worse-Okay50 and WorseBetter50. • Transport This is a long-horizon dual arm manipulation task. | Hz/fps, inference time and control rate |
| Memory | fixed dataset, value/policy parameters와 optional context/history. | not recovered | window and reset |
| Compute | dataset size, conservative/value update와 sequence/action decoding이 비용을 결정한다. | Each checkpoint evaluation takes 30 trials. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / IV. POLICY LEARNING - extractive body cue:** To identify similar states, we use the off-shelf pretrained vision models to compute features for similarity computation.
- **p. 4 / IV. POLICY LEARNING - extractive body cue:** Algorithm 1: GSR 1 [Optional] Finetune pretrained fθ on D; 2 Build graph G(V, E) using procedure in Section IV-B; 3 Set w[v] = 0 ...
- **p. 5 / IV. POLICY LEARNING - extractive body cue:** Implementation and Time Complexity We use R3M [33] as pretrained feature since it is pretrained with a contrastive objective, which we find can represent fine-grained ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** 3) Evaluation Metric: To evaluate the performance of a trained policy, we use the following metrics. • Success rate (SR) is defined as the number ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** identify, similar, states, off-shelf, pretrained, vision, models, compute, features, similarity, computation, Algorithm, GSR, Optional, Finetune, Build, graph, procedure, Section, IV-B.
- **Relevant PDF headings:** IV. POLICY LEARNING (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Fixed-data support | Bottom: Our real-world tasks. and Worse-Better20 (the whole worse-human dataset with 20% data of the better-human dataset). • Nut Assembly In this ... | p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Value / uncertainty update | We first study how much performance gain our method can achieve compared to the state-of-the-art imitation learning baseline. | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Policy extraction / deployment | We find that our method can achieve a success rate greater than 80% in the considered task and outperform all baselines in ... | p. 7 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / V. EXPERIMENTS - extractive body cue:** Hyperparameter Analysis Having known that our method indeed strengthened desired behavior, in this section, we further study the effect of the main hyperparameters in our ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Specifically, in the simulation experiment, the last average pooling layer of ResNet-18 is replaced by a spatial softmax [15] as in previous works [30, 8].
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Identifying connectivity. Augmented edge: We add a bidirectional edge between two nodes u and v if they both lie in the tolerance range ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** However, in many cases, they will get stuck or go out of distribution, leading to a complete failure.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Interestingly, we have the following findings: (1) All the temporal segments that lead to the failures are weakened and have low weights.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The robot is required to push a blue cylinder toward a green cube on the table. • Spoon Scooping In this task, the robot is ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** This task highlights the challenge of robust perception against partial occlusion and fine-grained manipulation. • Tweezer Manipulation In this task, the robot needs to first ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING), objective p. 4 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING), p. 3 (IV. POLICY LEARNING), p. 4 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), p. 5 (IV. POLICY LEARNING), temporal p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), p. 4 (IV. POLICY LEARNING).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
