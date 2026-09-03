# Method - Learning Robust Rewards with Adversarial Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1710.11248; PDF retrieval source: https://arxiv.org/pdf/1710.11248. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 1 (ABSTRACT), p. 3 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 5 (3 BACKGROUND)): The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: π∗= arg maxπ Eτ∼π " ...

## Method Body Digest

- **p. 3 / 3 BACKGROUND - extractive body cue:** The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** Suppose IRL recovers a state-only reward r′(s) such that it produces an optimal policy in T: Q∗ r′,T (s, a) = Q∗ r,T (s, a) ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose AIRL, a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation.
- **p. 3 / 3 BACKGROUND - extractive body cue:** The dynamics or transition distribution T (s′/a, s), the initial state distribution ρ0(s), and the reward function r(s, a) are unknown in the standard reinforcement ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** Then, there exists MDP pairs M, M ′ where changing the transition model from T to T ′ breaks policy invariance on MDP M ′.
- **p. 5 / 3 BACKGROUND - extractive body cue:** If a reward function r′(s, a, s′) is disentangled for all dynamics functions, then it must be state-only. i.e.
- **p. 1 / ABSTRACT - extractive body cue:** Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features, but still require a manually specified reward function.
- **p. 5 / 3 BACKGROUND - extractive body cue:** 6: Update reward rθ,φ(s, a, s′) ←log Dθ,φ(s, a, s′) -log(1 -Dθ,φ(s, a, s′)) 7: Update π with respect to rθ,φ using any policy optimization ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose adversarial inverse reinforcement learning (AIRL), an inverse reinforcement learning algorithm based on adversarial learning.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** When compared to GAIL (Ho & Ermon, 2016), which does not attempt to directly recover rewards, our method achieves comparable results on tasks that do ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** In order to decouple the reward function from the advantage, we propose to modify the discriminator of Sec.

## Source Evidence Cues

- **p. 3 / 3 BACKGROUND - extractive body cue:** The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** Suppose IRL recovers a state-only reward r′(s) such that it produces an optimal policy in T: Q∗ r′,T (s, a) = Q∗ r,T (s, a) ...
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we propose AIRL, a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation.
- **p. 3 / 3 BACKGROUND - extractive body cue:** The dynamics or transition distribution T (s′/a, s), the initial state distribution ρ0(s), and the reward function r(s, a) are unknown in the standard reinforcement ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** Then, there exists MDP pairs M, M ′ where changing the transition model from T to T ′ breaks policy invariance on MDP M ′.
- **p. 5 / 3 BACKGROUND - extractive body cue:** If a reward function r′(s, a, s′) is disentangled for all dynamics functions, then it must be state-only. i.e.
- **p. 1 / ABSTRACT - extractive body cue:** Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features, but still require a manually specified reward function.
- **Detected method headings:** A.3 POLICY OBJECTIVE (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T ... | p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Suppose IRL recovers a state-only reward r′(s) such that it produces an optimal policy in T: Q∗ r′,T (s, a) = Q∗ ... | p. 5 (3 BACKGROUND), p. 1 (ABSTRACT) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | In this work, we propose AIRL, a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation. | p. 1 (ABSTRACT), p. 3 (3 BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 BACKGROUND - extractive body cue:** The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** 6: Update reward rθ,φ(s, a, s′) ←log Dθ,φ(s, a, s′) -log(1 -Dθ,φ(s, a, s′)) 7: Update π with respect to rθ,φ using any policy optimization ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our algorithm provides for simultaneous learning of the reward function and value function, which enables us to both make use of the efficient adversarial formulation ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** 4, h recovers the optimal value function V ∗, which serves as the reward shaping term.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** There are many scenarios where IRL may be preferred over direct imitation learning, such as re-optimizing a reward in novel environments (Finn et al., 2017) ...
- **p. 3 / 3 BACKGROUND - extractive body cue:** We can interpret the IRL problem as solving the maximum likelihood problem: max θ Eτ∼D [log pθ(τ)] , (1) Where pθ(τ) ∝p(s0) QT t=0 p(st+1/st, ...
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 5 (3 BACKGROUND).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized, discounted, reward, under, where | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | adversarial, inverse, reinforcement, learning, AIRL, algorithm, When, compared, GAIL, Ermon | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 BACKGROUND - extractive body cue:** The goal of (forward) reinforcement learning is to find the optimal policy π∗that maximizes the expected entropy-regularized discounted reward, under π, T , and ρ0: ...
- **p. 3 / 3 BACKGROUND - extractive body cue:** 4 ADVERSARIAL INVERSE REINFORCEMENT LEARNING (AIRL) In practice, using full trajectories as proposed by GAN-GCL can result in high variance estimates as compared to using ...
- **p. 5 / 3 BACKGROUND - extractive body cue:** Suppose IRL recovers a state-only reward r′(s) such that it produces an optimal policy in T: Q∗ r′,T (s, a) = Q∗ r,T (s, a) ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** 2 into the single state and action case, where: Dθ(s, a) = exp{fθ(s, a)} exp{fθ(s, a)} + π(a/s).
- **p. 4 / 3 BACKGROUND - extractive body cue:** As a simple example, consider deterministic dynamics T(s, a) →s′ and state-action rewards ˆr(s, a) = r(s, a) + γΦ(T(s, a)) -Φ(s).
- **p. 1 / ABSTRACT - extractive body cue:** Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features, but still require a manually specified reward function.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Part of the challenge is that IRL is an ill-defined problem, since there are many optimal policies that can explain a set of demonstrations, and ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | Value iteration steps are plotted on the x-axis, against returns for the policy on the y-axis. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Reinforcement learning provides a powerful and general framework for decision making and control, but its application in practice is often hindered by ... | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 7 EXPERIMENTS - extractive body cue:** We train a quadrupedal "ant" agent to run forwards, and at test time we disable and shrink two of the front legs of the ant ...
- **p. 3 / 3 BACKGROUND - extractive body cue:** They operate in a trajectory-centric formulation, where the discriminator takes on a particular form (fθ(τ) is a learned function; π(τ) is precomputed and its value ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** goal, forward, reinforcement, learning, find, optimal, policy, maximizes, expected, entropy-regularized, discounted, reward, under, where, denotes, sequence, states, actions, induced, dynamics.
- **Relevant PDF headings:** A.3 POLICY OBJECTIVE (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | (2016a), which we refer to as GAN-GCL, on standard benchmark tasks that do not evaluate transfer. | p. 6 (7 EXPERIMENTS), p. 8 (7 EXPERIMENTS) |
| Policy fitting | We find that AIRL performs on par with GAIL in a traditional imitation learning setup while vastly outperforming it in transfer learning ... | p. 6 (7 EXPERIMENTS), p. 7 (7 EXPERIMENTS) |
| Closed-loop rollout | We also show that in the transfer learning setup, under a new transition matrix T ′, the optimal policy under the state-only ... | p. 6 (7 EXPERIMENTS), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / 3 BACKGROUND - extractive body cue:** 6 LEARNING DISENTANGLED REWARDS WITH AIRL In the method presented in Section 4, we cannot learn a state-only reward function, rθ(s), meaning that we cannot ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** At test time, the agent cannot simply mimic the actions learned during training, and instead must successfully infer that the goal in the maze is ...
- **p. 4 / 3 BACKGROUND - extractive body cue:** However, we leave this direction to future work.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** (2016a) does not implement or evaluate GAN-GCL and, to our knowledge, we present the first empirical evaluation of this algorithm.
- **p. 6 / 7 EXPERIMENTS - extractive body cue:** We subtract a constant offset from all reward functions so that they share the same mean for visualization - this does not influence the optimal ...
- **p. 7 / 7 EXPERIMENTS - extractive body cue:** GAIL learns successfully in the training domain, but does not acquire a representation that is suitable for transfer to test domains.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 1 (ABSTRACT), p. 3 (3 BACKGROUND), p. 4 (3 BACKGROUND), p. 5 (3 BACKGROUND), objective p. 3 (3 BACKGROUND), p. 5 (3 BACKGROUND), p. 2 (1 INTRODUCTION), p. 5 (3 BACKGROUND), p. 1 (1 INTRODUCTION), p. 3 (3 BACKGROUND), temporal p. 7 (7 EXPERIMENTS), p. 1 (ABSTRACT), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (2 RELATED WORK), p. 3 (3 BACKGROUND).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
