# Method - Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html; PDF retrieval source: https://proceedings.iclr.cc/paper_files/paper/2024/file/430894999584d0bd358611e2ecf00b15-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 19 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.2 SOCIAL REARRANGEMENT)): We use a long short-term memory networks (LSTM) (Hochreiter & Schmidhuber, 1997) policy with ResNet18 as the visual backbone and two recurrent layers, resulting nearly 8517k parameters.

## Method Body Digest

- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** We use a long short-term memory networks (LSTM) (Hochreiter & Schmidhuber, 1997) policy with ResNet18 as the visual backbone and two recurrent layers, resulting nearly ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** When using learned skills, we use the same 2-layer policy architecture, except use learned navigation, and learned pick/place skills, which operate entirely using robot depth ...
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The LSTM output is then set to an action and value prediction network.
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The visual embedding is then concatenated with the state sensor values and passed through a 2-layer LSTM network with hidden dimension 512.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** This results in reactive behaviors, like the high-level policy commanding the robot to move backwards to give way to the humanoid in narrow corridors, or ...
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 2 PPO minibatches and 1 epoch per update, an entropy loss of 1e-4, and clip the gradient norm to 0.2.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Social tasks - Aiming at reproducible and standardized benchmarking, we present two collaborative human-robot interaction tasks and a suite of baselines for each.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we introduce Habitat 3.0 - a simulator that supports both humanoid avatars and robots for the study of collaborative human-robot tasks in ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework is open-sourced, for more details see Appendix A.

## Source Evidence Cues

- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** We use a long short-term memory networks (LSTM) (Hochreiter & Schmidhuber, 1997) policy with ResNet18 as the visual backbone and two recurrent layers, resulting nearly ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects or placing an ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** When using learned skills, we use the same 2-layer policy architecture, except use learned navigation, and learned pick/place skills, which operate entirely using robot depth ...
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The LSTM output is then set to an action and value prediction network.
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The visual embedding is then concatenated with the state sensor values and passed through a 2-layer LSTM network with hidden dimension 512.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** This results in reactive behaviors, like the high-level policy commanding the robot to move backwards to give way to the humanoid in narrow corridors, or ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We use a long short-term memory networks (LSTM) (Hochreiter & Schmidhuber, 1997) policy with ResNet18 as the visual backbone and two recurrent ... | p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at ... | p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects ... | p. 18 (A.2 SOCIAL REARRANGEMENT), p. 19 (A.2 SOCIAL REARRANGEMENT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We use 2 PPO minibatches and 1 epoch per update, an entropy loss of 1e-4, and clip the gradient norm to 0.2.
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** We see that the agent is able to improve the reward while minimizing the distance to the humanoid for finding and following the humanoid over ...
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** We use a learning rate of 1 × 10-4 and the maximum gradient norm of 0.2.
- **p. 16 / A.1 SOCIAL NAVIGATION - extractive body cue:** In addition, a slack reward of -0.1 is given to encourage the agent to find the humanoid as soon as possible.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We plot the training success and reward for the social rearrangement baselines (top) and ablations (bottom).
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 17 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | policy, uses, ResNet-18, visual, encoder, embed, depth, input, image, dimension, embedding, generate, realistic, body | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | policy, uses, ResNet-18, visual, encoder, embed, depth, input, image, dimension | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | Social, tasks, Aiming, reproducible, standardized, benchmarking, present, collaborative, human-robot, interaction | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | PPO, minibatches, epoch, update, entropy, loss, clip, gradient, norm, agent | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The policy uses a ResNet-18 (He et al., 2016) visual encoder to embed the 256 × 256 depth input image into a 512 dimension embedding.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (2019)) to generate realistic body shapes and poses, (4) a library of avatars made from 12 base models with multiple gender representations, body shapes, and ...
- **p. 17 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The LSTM output is then set to an action and value prediction network.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** Additionally, we provide 4 ‘primitive' actions to the high-level policy that move the robot forward/backward or turn it left/right by a fixed amount.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** The action space of the learned high-level policy consists of discrete selections from all possible combinations of skills and objects/receptacles allowed at each step.
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** If the robot approaches the humanoid within a short distance (< 1.5m) while executing a skill, the current skill is aborted, and the high-level policy ...
- **p. 19 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** If the high-level policy chooses to execute an infeasible low-level action, such as attempting to pick an object that is out of reach (based on ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | During evaluation, the total episode length is 1500 steps and the episode terminates if there is a collision between the humanoid and ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | We use 3 seeds for each model. overall task, +5 for completing any subgoal consisting of picking one of the target objects ... | hardware, batch and throughput |

## Training vs Inference

- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** We present the overall task success as well as the training reward for all approaches, averaged over 3 seeds.
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** All baselines are trained with three different random seeds, and results are reported averaged across those seeds.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** long, short-term, memory, networks, LSTM, Hochreiter, Schmidhuber, policy, ResNet18, visual, backbone, recurrent, layers, resulting, nearly, parameters, action, space, learned, high-level.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | In all episodes, to make sure that the robot learns to find the humanoid, the robot location is initialized at least 3m ... | p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION) |
| Baseline harness | Figure 5: Social Navigation training curves. We plot the training average distance to the humanoid and reward for the social navigation baselines ... | p. 17 (Figure/Table caption), p. 18 (A.2 SOCIAL REARRANGEMENT) |
| Metric / failure reporting | Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different ... | p. 7 (Figure/Table caption), p. 25 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** Among the ablations, removing the sensors used in original training make learning slower, with primitive actions having the most effect.
- **p. 28 / Figure/Table caption - extractive body cue:** Figure 12: Benchmark results in Habitat 3.0. We study the effect of varying scene size, number of objects, type of agents and single or multi-agent. ...
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** We plot the training average distance to the humanoid and reward for the social navigation baselines and ablations.
- **p. 17 / A.1 SOCIAL NAVIGATION - extractive body cue:** 5 shows the average distance between the humanoid and the robot and reward learning curve over the number of simulation steps for the end-to-end RL ...
- **p. 18 / A.2 SOCIAL REARRANGEMENT - extractive body cue:** 6 shows learning curves for all baselines and ablations on the social rearrangement task.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Social Navigation. Overview of the Social Navigation task and sensors used (left). Baseline Results (right). The bottom rows show different variations of removing ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Human-in-the-Loop Coordination Results. We report estimated mean and 95% confidence intervals (CI) across 30 participants. drop in performance. Removing the humanoid-GPS results in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 19 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.2 SOCIAL REARRANGEMENT), objective p. 17 (A.2 SOCIAL REARRANGEMENT), p. 17 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 18 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT), temporal p. 18 (A.2 SOCIAL REARRANGEMENT), p. 16 (A.1 SOCIAL NAVIGATION), p. 16 (A.1 SOCIAL NAVIGATION), p. 17 (A.1 SOCIAL NAVIGATION), p. 17 (A.2 SOCIAL REARRANGEMENT), p. 18 (A.2 SOCIAL REARRANGEMENT).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
