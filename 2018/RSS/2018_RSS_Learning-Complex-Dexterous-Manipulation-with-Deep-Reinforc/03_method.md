# Method - Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p49.html; PDF retrieval source: https://arxiv.org/pdf/1709.10087. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG))): We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to incorporate demonstrations.

## Method Body Digest

- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to incorporate demonstrations.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ log πθ(ai t/si ...
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** In policy gradient methods, the parameters of the policy are directly optimized to maximize the objective, η(θ), using local search methods such as gradient ascent.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** R : S × A →R is the reward function which measures task progress.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, this versatility comes at the price of high dimensional observation and action spaces, complex and discontinuous contact patterns, and under-actuation during nonprehensile manipulation.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** S ∈Rn and A ∈Rm represent the state and actions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the current benchmarks are typically quite limited both in the dimensionality of the tasks and the complexity of the interactions.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- **p. 2 / I. INTRODUCTION - extractive body cue:** We attribute this to human priors in the demonstrations which bias the learning towards more robust strategies. • We propose a set of dexterous hand ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Indeed, model-free methods have been used for acquiring manipulation skills [52], [13], but so far have been limited to simpler behaviors with 2-3 finger hands ...

## Source Evidence Cues

- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to incorporate demonstrations.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ log πθ(ai t/si ...
- **Detected method headings:** IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) (p. 5); 2) How does DAPG compare to other model-free methods (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to ... | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ ... | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We first present some RL preliminaries, followed by the base RL algorithm we use for learning, and finally describe our procedure to ... | p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** In policy gradient methods, the parameters of the policy are directly optimized to maximize the objective, η(θ), using local search methods such as gradient ascent.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** R : S × A →R is the reward function which measures task progress.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | However, versatility, comes, price, high, dimensional, observation, action, spaces, complex, discontinuous, contact, patterns, under-actuation | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | However, versatility, comes, price, high, dimensional, observation, action, spaces, complex | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | overcome, challenge, augment, policy, search, process, small, number, human, demonstrations | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | policy, gradient, methods, parameters, directly, optimized, maximize, objective, local, search | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, this versatility comes at the price of high dimensional observation and action spaces, complex and discontinuous contact patterns, and under-actuation during nonprehensile manipulation.
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** S ∈Rn and A ∈Rm represent the state and actions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To overcome this challenge, we propose to augment the policy search process with a small number of human demonstrations collected in virtual reality (VR).
- **p. 5 / IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) - extractive body cue:** First, NPG computes the vanilla policy gradient, or REINFORCE [54] gradient: g = 1 NT N X i=1 T X t=1 ∇θ log πθ(ai t/si ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the current benchmarks are typically quite limited both in the dimensionality of the tasks and the complexity of the interactions.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In particular, we find that pre-training a policy with behavior cloning, and subsequent fine-tuning with policy gradient along with an augmented loss to stay close ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | timestep so that the policy can better capture relevant statistics about the data. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Using expressive function approximators allow for complex, nonlinear ways to use sensory feedback, making them wellsuited to dexterous manipulation. | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** (b/c) unnatural grasp for hammer (d) unnatural use of wrist for unlatching the door. be useful for training on the physical hardware.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, present, some, preliminaries, followed, base, algorithm, learning, finally, describe, procedure, incorporate, demonstrations, NPG, computes, vanilla, policy, gradient, REINFORCE, t/si.
- **Relevant PDF headings:** IV. DEMO AUGMENTED POLICY GRADIENT (DAPG) (p. 5); 2) How does DAPG compare to other model-free methods (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | In order to benchmark the capabilities of DRL with regard to the dexterous manipulation tasks outlined in Section III, we evaluate the ... | p. 6 (2) Do the resulting policies exhibit desirable properties like), p. 7 (2) Do the resulting policies exhibit desirable properties like) |
| Policy fitting | Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance ... | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Closed-loop rollout | Figure 10: Performance of RL with demonstrations methods - DAPG(ours) and DDPGfD. DAPG significantly outperforms DDPGfD. For DAPG, we plot the performance ... | p. 8 (Figure/Table caption), p. 6 (2) Do the resulting policies exhibit desirable properties like) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 9: Robustness of trained policies to variations in the envi- ronment. The top two figures are trained on a single instance of the environment ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** Subsequently, we demonstrate the benefits of incorporating human demonstrations with regard to faster learning, increased robustness of trained policies, and ability to cope with sparse ...
- **p. 6 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** robustness to variations in the environment?
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** The mental models of solution strategies that humans have for these tasks are indeed quite robust.
- **p. 7 / 2) Do the resulting policies exhibit desirable properties like - extractive body cue:** Furthermore, we take the additional step of analyzing the robustness of these policies to variations in environments that were not experienced during training.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), objective p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), temporal p. 5 (2) In-hand Manipulation - Repositioning a pen (Figure), p. 3 (II. RELATED WORK), p. 4 (2) In-hand Manipulation - Repositioning a pen (Figure), p. 4 (2) In-hand Manipulation - Repositioning a pen (Figure), p. 5 (IV. DEMO AUGMENTED POLICY GRADIENT (DAPG)), p. 6 (2) While RL eventually solves the task with appropriate).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
