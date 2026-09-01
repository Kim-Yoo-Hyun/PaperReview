# Method - Generative Adversarial Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1606.03476; PDF retrieval source: https://arxiv.org/pdf/1606.03476. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 4 (2 Background), p. 6 (2. Form a gradient estimate with Eq. (12) with c∗), p. 2 (2 Background), p. 4 (2 Background), p. 3 (2 Background)): networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our algorithm harnesses generative adversarial training to fit distributions ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our algorithm harnesses generative ...
- **p. 4 / 2 Background - extractive body cue:** For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing ...
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** We propose the following new cost regularizer that combines the best of both worlds, as we will show in the coming sections: ψGA(c) ≜ EπE[g(c(s, ...
- **p. 2 / 2 Background - extractive body cue:** Section 3 will work with finite state and action spaces S and A to avoid technical machinery out of the scope of this paper (concerning ...
- **p. 4 / 2 Background - extractive body cue:** In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy ...
- **p. 3 / 2 Background - extractive body cue:** A basic result [21] is that the set of valid occupancy measures D ≜{ρπ : π ∈Π} can be written as a feasible set of ...
- **p. 1 / Abstract - extractive body cue:** We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- **p. 5 / 2 Background - extractive body cue:** With the indicator function δC : RS×A →R, defined by δC(c) = 0 if c ∈C and +∞otherwise, we can write the apprenticeship learning objective ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** We show that a certain instantiation of our framework draws an analogy between imitation learning and generative adversarial networks, from which we derive a model-free ...
- **p. 1 / 1 Introduction - extractive body cue:** Then, we instantiate our framework in Sections 4 and 5 with a new model-free imitation learning algorithm.
- **p. 3 / 2 Background - extractive body cue:** We explore such algorithms in Sections 4 and 5, where we show that certain settings of ψ lead to both existing algorithms and a novel ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our algorithm harnesses generative ...
- **p. 4 / 2 Background - extractive body cue:** For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing ...
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** We propose the following new cost regularizer that combines the best of both worlds, as we will show in the coming sections: ψGA(c) ≜ EπE[g(c(s, ...
- **p. 2 / 2 Background - extractive body cue:** Section 3 will work with finite state and action spaces S and A to avoid technical machinery out of the scope of this paper (concerning ...
- **p. 4 / 2 Background - extractive body cue:** In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy ...
- **p. 3 / 2 Background - extractive body cue:** A basic result [21] is that the set of valid occupancy measures D ≜{ρπ : π ∈Π} can be written as a feasible set of ...
- **p. 1 / Abstract - extractive body cue:** We propose a new general framework for directly extracting a policy from data, as if it were obtained by reinforcement learning following inverse reinforcement learning.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our ... | p. 2 (1 Introduction), p. 4 (2 Background) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across ... | p. 4 (2 Background), p. 6 (2. Form a gradient estimate with Eq. (12) with c∗) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We propose the following new cost regularizer that combines the best of both worlds, as we will show in the coming sections: ... | p. 6 (2. Form a gradient estimate with Eq. (12) with c∗), p. 2 (2 Background) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2 Background - extractive body cue:** For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing ...
- **p. 5 / 2 Background - extractive body cue:** With the indicator function δC : RS×A →R, defined by δC(c) = 0 if c ∈C and +∞otherwise, we can write the apprenticeship learning objective ...
- **p. 2 / 2 Background - extractive body cue:** Maximum causal entropy IRL looks for a cost function c ∈C that assigns low cost to the expert policy and high cost to other policies, ...
- **p. 2 / 2 Background - extractive body cue:** For the remainder of this paper, we will adopt maximum causal entropy IRL [31, 32], which fits a cost function from a family of functions ...
- **p. 4 / 2 Background - extractive body cue:** This is the dual of the optimization problem minimize ρ∈D -¯H(ρ) subject to ρ(s, a) = ρE(s, a) ∀s ∈S, a ∈A (7) with Lagrangian ...
- **p. 5 / 2 Background - extractive body cue:** (12) is the policy gradient for a reinforcement learning objective with cost c∗, Ho et al. propose an algorithm that alternates between two steps: 1.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 5 (2 Background), p. 5 (2 Background), p. 6 (2. Form a gradient estimate with Eq. (12) with c∗), p. 4 (2 Background), p. 7 (2. Form a gradient estimate with Eq. (12) with c∗), p. 3 (2 Background).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | There, main, approaches, suitable, setting, behavioral, cloning, learns, policy, supervised, learning, problem, over, state-action | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | There, main, approaches, suitable, setting, behavioral, cloning, learns, policy, supervised | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | certain, instantiation, framework, draws, analogy, between, imitation, learning, generative, adversarial | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | class, cost, functions, apprenticeship, learning, algorithm, finds, policy, performs, better | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** There are two main approaches suitable for this setting: behavioral cloning [20], which learns a policy as a supervised learning problem over state-action pairs from ...
- **p. 4 / 2 Background - extractive body cue:** In reality, the expert trajectory distribution will be provided only as a finite set of samples, so in large environments, most of the expert's occupancy ...
- **p. 3 / 2 Background - extractive body cue:** The occupancy measure can be interpreted as the distribution of state-action pairs that an agent encounters when navigating the environment with policy π, and it ...
- **p. 4 / 2 Background - extractive body cue:** For a class of cost functions C ⊂RS×A, an apprenticeship learning algorithm finds a policy that performs better than the expert across C, by optimizing ...
- **p. 5 / 2 Background - extractive body cue:** Pros of apprenticeship learning While restrictive cost classes C may not lead to exact imitation, apprenticeship learning with such C can scale to large state ...
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** The discriminator network can be interpreted as a local cost function providing learning signal to the policy-specifically, taking a policy step that decreases expected cost ...
- **p. 1 / Abstract - extractive body cue:** Consider learning a policy from example expert behavior, without interaction with the expert or access to reinforcement signal.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Our characterization introduces a framework for directly learning policies from data, bypassing any intermediate IRL step. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Inverse reinforcement learning (IRL), on the other hand, learns a cost function that prioritizes entire trajectories over others, so compounding error, a ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** networks [9], a technique from the deep learning community that has led to recent successes in modeling distributions of natural images: our algorithm harnesses generative ...
- **p. 3 / 2 Background - extractive body cue:** A basic result [21] is that the set of valid occupancy measures D ≜{ρπ : π ∈Π} can be written as a feasible set of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** networks, technique, deep, learning, community, recent, successes, modeling, distributions, natural, images, algorithm, harnesses, generative, adversarial, training, states, actions, defining, expert.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | We found that on the classic control tasks (cartpole, acrobot, and mountain car), behavioral cloning suffered in expert data efficiency compared to ... | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Policy fitting | We tested Algorithm 1 against three baselines: 1. | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Closed-loop rollout | Our algorithm almost always achieved at least 70% of expert performance for all dataset 7 | p. 7 (6 Experiments), p. 7 (6 Experiments) |

## Failure and Ablation Link

- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** When D cannot distinguish data generated by G from the true data, then G has successfully matched the true data.
- **p. 6 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** The indicator regularizers δC, used by the linear apprenticeship learning algorithms described in Section 4, are always fixed, and cannot adapt to data as ψGA ...
- **p. 5 / 2. Form a gradient estimate with Eq. (12) with c∗ - extractive body cue:** This carefully constructed step scheme ensures that divergence does not occur due to high noise in estimating the gradient (12).
- **p. 5 / 2 Background - extractive body cue:** If C does not include a cost function that explains expert behavior well, then attempting to recover a policy from such an encoding will not ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 4 (2 Background), p. 6 (2. Form a gradient estimate with Eq. (12) with c∗), p. 2 (2 Background), p. 4 (2 Background), p. 3 (2 Background), objective p. 4 (2 Background), p. 5 (2 Background), p. 2 (2 Background), p. 2 (2 Background), p. 4 (2 Background), p. 5 (2 Background), temporal p. 1 (1 Introduction), p. 1 (1 Introduction), p. 7 (6 Experiments), p. 2 (2 Background), p. 2 (2 Background), p. 5 (2. Form a gradient estimate with Eq. (12) with c∗).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
