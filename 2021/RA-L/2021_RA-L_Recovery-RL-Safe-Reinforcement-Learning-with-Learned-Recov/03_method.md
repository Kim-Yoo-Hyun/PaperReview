# Method - Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.15920; PDF retrieval source: https://arxiv.org/pdf/2010.15920. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (IV. RECOVERY RL), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 4 (IV. RECOVERY RL), p. 4 (IV. RECOVERY RL), p. 3 (III. PROBLEM STATEMENT)): [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics model.

## Method Body Digest

- **p. 5 / IV. RECOVERY RL - extractive body cue:** [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics model.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, the inherent objective conflict between exploring to learn new tasks and limiting exploration to avoid constraint violations can lead to suboptimalities in policy optimization.
- **p. 4 / IV. RECOVERY RL - extractive body cue:** If the task policy πtask proposes an action aπtask at state s such that (s,aπtask)̸ ∈T π safe, then a recovery action sampled from πrec ...
- **p. 4 / IV. RECOVERY RL - extractive body cue:** Then π selects actions as follows: at = ( aπtask t (st,aπtask t ) ∈T π safe aπrec t (st,aπtask t ) ∈T π rec ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Stochastic dynamics model P : S ×A×S →[0,1] maps a state and action to a probability distribution over subsequent states, γ ∈[0,1] is a discount ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 4 / IV. RECOVERY RL - extractive body cue:** We train ˆQπ φ,risk by minimizing the following MSE loss with respect to the target (RHS of equation IV.1).

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Thus, endowing RL agents with the ability to satisfy constraints during learning not only enables robots to interact safely, but also allows them to more ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We present Recovery RL, a new algorithm for safe robotic RL.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...

## Source Evidence Cues

- **p. 5 / IV. RECOVERY RL - extractive body cue:** [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics model.
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, the inherent objective conflict between exploring to learn new tasks and limiting exploration to avoid constraint violations can lead to suboptimalities in policy optimization.
- **p. 4 / IV. RECOVERY RL - extractive body cue:** If the task policy πtask proposes an action aπtask at state s such that (s,aπtask)̸ ∈T π safe, then a recovery action sampled from πrec ...
- **p. 4 / IV. RECOVERY RL - extractive body cue:** Then π selects actions as follows: at = ( aπtask t (st,aπtask t ) ∈T π safe aπrec t (st,aπtask t ) ∈T π rec ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** Stochastic dynamics model P : S ×A×S →[0,1] maps a state and action to a probability distribution over subsequent states, γ ∈[0,1] is a discount ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | [8] to plan over a learned stochastic dynamics model, while for tasks with visual observations, we use a VAE based latent dynamics ... | p. 5 (IV. RECOVERY RL), p. 1 (Abstract) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before ... | p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | First, the inherent objective conflict between exploring to learn new tasks and limiting exploration to avoid constraint violations can lead to suboptimalities ... | p. 2 (I. INTRODUCTION), p. 4 (IV. RECOVERY RL) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. RECOVERY RL - extractive body cue:** We train ˆQπ φ,risk by minimizing the following MSE loss with respect to the target (RHS of equation IV.1).
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We augment the MDP with an extra constraint cost function C : S →{0,1} which indicates whether a state is constraint violating and associated discount ...
- **p. 4 / IV. RECOVERY RL - extractive body cue:** Note we do not assume access to the true constraint cost function C.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We consider a RL formulation subject to constraints on the probability of unsafe future behavior and design an algorithm that can balance the often conflicting ...
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, the inherent objective conflict between exploring to learn new tasks and limiting exploration to avoid constraint violations can lead to suboptimalities in policy optimization.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | present, algorithm, optimize, equation, III, utilizing, pair, policies, task, policy, trained, maximize, over, recovery | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | present, algorithm, optimize, equation, III, utilizing, pair, policies, task, policy | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | Thus, endowing, agents, ability, satisfy, constraints, during, learning, only, enables | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | train, risk, minimizing, following, MSE, loss, respect, target, RHS, equation | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 4 / IV. RECOVERY RL - extractive body cue:** If the task policy πtask proposes an action aπtask at state s such that (s,aπtask)̸ ∈T π safe, then a recovery action sampled from πrec ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Safe exploration poses a tradeoff: learning new skills through environmental interaction requires exploring a wide range of possible behaviors, but learning safely forces the agent ...
- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We leverage Doffline to constrain exploration of the task policy to reduce the probability of constraint violation during environment interaction.
- **p. 4 / IV. RECOVERY RL - extractive body cue:** Then π selects actions as follows: at = ( aπtask t (st,aπtask t ) ∈T π safe aπrec t (st,aπtask t ) ∈T π rec ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Instead of modifying the policy optimization procedure to encourage constraint satisfaction, which can introduce suboptimality in the learned task policy [26], the recovery policy can ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | We do not report reward per episode, as episodes terminate on task completion or constraint violation. | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | All experiments involve policy learning under state space constraints, in which a constraint violation terminates the current episode. | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** First, the inherent objective conflict between exploring to learn new tasks and limiting exploration to avoid constraint violations can lead to suboptimalities in policy optimization.
- **p. 4 / IV. RECOVERY RL - extractive body cue:** Then π selects actions as follows: at = ( aπtask t (st,aπtask t ) ∈T π safe aπrec t (st,aπtask t ) ∈T π rec ...
- **p. 3 / III. PROBLEM STATEMENT - extractive body cue:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Figure 5: Sensitivity Experiments: We report the final number of task ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** plan, over, learned, stochastic, dynamics, model, while, tasks, visual, observations, VAE, latent, Recovery, algorithm, navigates, tradeoff, leveraging, offline, data, learn.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | Domains: We evaluate Recovery RL on a set of 6 simulation domains (Figure 3) and an image-based obstacle avoidance task on a ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Filtering / recovery | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation ... | p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Monitoring / re-entry | Results suggest that Recovery RL with both model-free and modelbased recovery mechanisms significantly outperform prior algorithms across all 3 2D pointmass navigation ... | p. 6 (V. EXPERIMENTS), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Ablations: We ablate different components of Recovery RL and study the sensitivity of Recovery RL to the number of transitions in Doffline for the Object ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Ablations: We first study the affect of different algorithmic components of Recovery RL (left). Results suggest that offline pretraining of πrec and ˆQπ ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** We then evaluate Recovery RL on an image-based obstacle avoidance task on the da Vinci Research Kit (dVRK) [20] where the robot must guide its ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In the object extraction environments, the goals is to extract the red block without toppling any blocks, and in the case of Object Extraction (Dynamic ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In both object extraction environments, the objective is to grasp and lift the red block without toppling any of the blocks or colliding with the ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In Navigation 1 and 2, the goal is to navigate from the start set to the goal set without colliding into the obstacles (red) while ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** In all navigation tasks, we find that Recovery RL significantly outperforms prior methods with both model-free and model-based recovery policies, while for the object extraction ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (IV. RECOVERY RL), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 4 (IV. RECOVERY RL), p. 4 (IV. RECOVERY RL), p. 3 (III. PROBLEM STATEMENT), objective p. 4 (IV. RECOVERY RL), p. 3 (III. PROBLEM STATEMENT), p. 4 (IV. RECOVERY RL), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), temporal p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 3 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** We present an algorithm to optimize equation (III.1) by utilizing a pair of policies, a task policy πtask, which is trained to maximize Rπ over πtask ∈Π and a recovery ... (p. 3, III. PROBLEM STATEMENT).
- **Objective/update evidence:** We propose Recovery RL, an algorithm which navigates this tradeoff by (1) leveraging offline data to learn about constraint violating zones before policy learning and (2) separating the goals of ... (p. 1, Abstract).
- **Temporal/runtime evidence:** We do not report reward per episode, as episodes terminate on task completion or constraint violation. (p. 5, V. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
