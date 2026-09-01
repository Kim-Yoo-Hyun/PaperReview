# Method - Maximum Entropy Inverse Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.cs.cmu.edu/~bziebart/publications/maximum-entropy-inverse-reinforcement-learning.html; PDF retrieval source: https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2. Recursively compute for N iterations), p. 1 (Abstract), p. 1 (Abstract), p. 3 (2. Recursively compute for N iterations), p. 4 (2. Recursively compute for N iterations), p. 2 (Abstract)): Space doesn't permit the full exposition of the incomplete (and non-convex) log-likelihood, but the intuitive expectation-maximization algorithm that results fits the maximumentropy model using initial feature expectations and then impr ...

## Method Body Digest

- **p. 3 / 2. Recursively compute for N iterations - extractive PDF cue:** Space doesn't permit the full exposition of the incomplete (and non-convex) log-likelihood, but the intuitive expectation-maximization algorithm that results fits the maximumentropy model using initial ...
- **p. 1 / Abstract - extractive PDF cue:** Background In the imitation learning setting, an agent's behavior (i.e., its trajectory or path, ζ, of states si and actions ai) in some planning space ...
- **p. 1 / Abstract - extractive PDF cue:** We apply our approach to route preference modeling using 100,000 miles of collected GPS data of taxi-cab driving, where the structure of the world (i.e., ...
- **p. 3 / 2. Recursively compute for N iterations - extractive PDF cue:** Dsi = X t Dsi,t Instead, our algorithm computes the expected state occupancy frequencies efficiently using a technique similar to the 1In contrast, margin-based and ...
- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** We model this structure for the road network surrounding Pittsburgh, Pennsylvania, as a deterministic MDP with over 300,000 states (i.e., road segments) and 900,000 actions ...
- **p. 2 / Abstract - extractive PDF cue:** They consider a class of loss functions that directly measure disagreement between an agent and a learned policy, and then efficiently learn a reward function ...
- **p. 2 / Abstract - extractive PDF cue:** We use the maximum entropy distribution of paths conditioned on the transition distribution, T, and constrained to match feature expectations (Equation 1).
- **p. 3 / Abstract - extractive PDF cue:** P(action a/θ, T) ∝ X ζ:a∈ζt=0 P(ζ/θ, T) (5) Learning from Demonstrated Behavior Maximizing the entropy of the distribution over paths subject to the feature ...

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** Our probabilistic approach enables modeling of route preferences as well as a powerful new approach to inferring destinations and routes based on partial trajectories.
- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** Each road segment's contribution to these 22 different counts is represented in the road segment's features.
- **p. 1 / Abstract - extractive PDF cue:** Our approach provides a well-defined, globally normalized distribution over decision sequences, while providing the same performance guarantees as existing methods.

## Source Evidence Cues

- **p. 3 / 2. Recursively compute for N iterations - extractive PDF cue:** Space doesn't permit the full exposition of the incomplete (and non-convex) log-likelihood, but the intuitive expectation-maximization algorithm that results fits the maximumentropy model using initial ...
- **p. 1 / Abstract - extractive PDF cue:** Background In the imitation learning setting, an agent's behavior (i.e., its trajectory or path, ζ, of states si and actions ai) in some planning space ...
- **p. 1 / Abstract - extractive PDF cue:** We apply our approach to route preference modeling using 100,000 miles of collected GPS data of taxi-cab driving, where the structure of the world (i.e., ...
- **p. 3 / 2. Recursively compute for N iterations - extractive PDF cue:** Dsi = X t Dsi,t Instead, our algorithm computes the expected state occupancy frequencies efficiently using a technique similar to the 1In contrast, margin-based and ...
- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** We model this structure for the road network surrounding Pittsburgh, Pennsylvania, as a deterministic MDP with over 300,000 states (i.e., road segments) and 900,000 actions ...
- **p. 2 / Abstract - extractive PDF cue:** They consider a class of loss functions that directly measure disagreement between an agent and a learned policy, and then efficiently learn a reward function ...
- **p. 2 / Abstract - extractive PDF cue:** We use the maximum entropy distribution of paths conditioned on the transition distribution, T, and constrained to match feature expectations (Equation 1).
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | Space doesn't permit the full exposition of the incomplete (and non-convex) log-likelihood, but the intuitive expectation-maximization algorithm that results fits the maximumentropy ... | p. 3 (2. Recursively compute for N iterations), p. 1 (Abstract) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | Background In the imitation learning setting, an agent's behavior (i.e., its trajectory or path, ζ, of states si and actions ai) in ... | p. 1 (Abstract), p. 1 (Abstract) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | We apply our approach to route preference modeling using 100,000 miles of collected GPS data of taxi-cab driving, where the structure of ... | p. 1 (Abstract), p. 3 (2. Recursively compute for N iterations) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Abstract - extractive PDF cue:** P(action a/θ, T) ∝ X ζ:a∈ζt=0 P(ζ/θ, T) (5) Learning from Demonstrated Behavior Maximizing the entropy of the distribution over paths subject to the feature ...
- **p. 3 / Abstract - extractive PDF cue:** 2 Efficient State Frequency Calculations Given the expected state frequencies, the gradient can easily be computed (Equation 6) for optimization.
- **p. 1 / Abstract - extractive PDF cue:** Under the constraint of matching the reward value of demonstrated behavior, we Copyright c⃝2008, Association for the Advancement of Artificial Intelligence (www.aaai.org).
- **p. 2 / Abstract - extractive PDF cue:** The resulting distribution over paths for deterministic MDPs is parameterized by reward weights θ (Equation 2).
- **p. 2 / Abstract - extractive PDF cue:** However, given demonstrated trajectories that are absorbed in a finite number of steps, the reward weights maximizing entropy must be convergent.
- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** We call this value a cost (i.e., a negative reward).
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 3 (Abstract), p. 3 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 4 (2. Recursively compute for N iterations).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Stochastic, Policies, distribution, over, paths, provides, policy, available, actions, state, when, partition, function, Equation | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Stochastic, Policies, distribution, over, paths, provides, policy, available, actions, state | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | probabilistic, enables, modeling, route, preferences, well, powerful, inferring, destinations, routes | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | action, Learning, Demonstrated, Behavior, Maximizing, entropy, distribution, over, paths, subject | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Abstract - extractive PDF cue:** P(ζ/θ, T) = X o∈T PT (o) eθ⊤fζ Z(θ, o)Iζ∈o (3) ≈eθ⊤fζ Z(θ, T) Y st+1,at,st∈ζ PT (st+1/at, st) (4) Stochastic Policies This distribution over ...
- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** The choice of action in any particular state is assumed to be distributed according to the future expected reward of the best policy after taking ...
- **p. 1 / Abstract - extractive PDF cue:** We discuss several additional advantages in modeling behavior that this technique has over existing approaches to inverse reinforcement learning including margin methods (Ratliff, Bagnell, & ...
- **p. 1 / Abstract - extractive PDF cue:** Background In the imitation learning setting, an agent's behavior (i.e., its trajectory or path, ζ, of states si and actions ai) in some planning space ...
- **p. 2 / Abstract - extractive PDF cue:** Non-Deterministic Path Distributions In general MDPs, actions produce non-deterministic transitions between states (Figure 1c) according to the state transition distribution, T.
- **p. 3 / Abstract - extractive PDF cue:** of action outcomes, T , and an outcome sample, o, specifying the next state for every action.
- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** These branching values yield local action probabilities (Step 3), from which state frequencies in each timestep can be computed (Steps 4 and 5) and summed ...
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value not recovered from the selected body cues. | These branching values yield local action probabilities (Step 3), from which state frequencies in each timestep can be computed (Steps 4 and ... | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Our approach provides a well-defined, globally normalized distribution over decision sequences, while providing the same performance guarantees as existing methods. | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not recovered | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / Abstract - extractive PDF cue:** We use the maximum entropy distribution of paths conditioned on the transition distribution, T, and constrained to match feature expectations (Equation 1).
- **p. 5 / A B - extractive PDF cue:** P(dest/˜ζA→B) ∝P(˜ζA→B/dest)P(dest) ∝ P ζB→dest eθ⊤fζ P ζA→dest eθ⊤fζ P(dest) These quantities can easily be computed using our inference algorithm (Algorithm 1).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Space, doesn, permit, full, exposition, incomplete, non-convex, log-likelihood, intuitive, expectation-maximization, algorithm, fits, maximumentropy, model, initial, feature, expectations, then, improves, estimates.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | We discarded roughly 30% of the trips that were too short (fewer than 10 road segments), too cyclic, or too noisy, and ... | p. 4 (2. Recursively compute for N iterations), p. 5 (A B) |
| Policy fitting | They consider a class of loss functions that directly measure disagreement between an agent and a learned policy, and then efficiently learn ... | p. 2 (Abstract), p. 5 (A B) |
| Closed-loop rollout | The authors propose a strategy of matching feature expectations (Equation 1) between an observed policy and a learner's behavior; they demonstrate that ... | p. 2 (Abstract), p. 3 (2. Recursively compute for N iterations) |

## Failure and Ablation Link

- **p. 4 / 2. Recursively compute for N iterations - extractive PDF cue:** Our algorithm is efficient (polynomial time) for both classes, but this reduction provides a significant speed up (without introducing optimization non-convexity) and limits consideration of ...
- **p. 5 / A B - extractive PDF cue:** Further, by learning a probability distribution over driver preferences, destinations, and routes the MaxEntIRL model of driver behavior can go beyond route recommendation, to new ...
- **p. 3 / 2. Recursively compute for N iterations - extractive PDF cue:** 2For stochastic MDPs we can achieve better usage of finite data by removing the variance in sample feature expectations due to the uncertainty in the ...
- **p. 2 / Abstract - extractive PDF cue:** This arises quite frequently when, for instance, the behavior demonstrated by the agent is imperfect, or the planning algorithm only captures a part of the ...
- **p. 2 / Abstract - extractive PDF cue:** We employ the principle of maximum entropy, which resolves this ambiguity by choosing the distribution that does not exhibit any additional preferences beyond matching feature ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2. Recursively compute for N iterations), p. 1 (Abstract), p. 1 (Abstract), p. 3 (2. Recursively compute for N iterations), p. 4 (2. Recursively compute for N iterations), p. 2 (Abstract), objective p. 3 (Abstract), p. 3 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 4 (2. Recursively compute for N iterations), temporal p. 4 (2. Recursively compute for N iterations), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 3 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
