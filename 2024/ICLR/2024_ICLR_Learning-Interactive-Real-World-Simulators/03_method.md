# Method - Learning Interactive Real-World Simulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/c4d66eae503694424123b93ac0fbaf17-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2310.06114. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 7 (1. Put cup 2. Pen 3. Apple), p. 7 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple)): The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction by combining diverse datasets rich in along different ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction by combining diverse ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We then formulate the universal simulator as an observation prediction model that predicts observations conditioned on actions and previous observations as shown in Figure 2.
- **p. 1 / ABSTRACT - extractive body cue:** We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps the ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** The simulator can simulate video trajectories from the initial real observation, from which robot actions are recovered using an inverse dynamics model and executed on ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** REINFORCE algorithm (Williams, 1992) to optimize the VLA policy, treating the rollouts from the simulator as the on-policy rollouts from the real environment and use ...
- **p. 1 / ABSTRACT - extractive body cue:** We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** One advantage of this observation prediction model is that the simulator stays the same across all tasks and can be used in combination with any ...

## Design Rationale

- **p. 1 / 1 INTRODUCTION - extractive body cue:** In this work, we propose to combine a wealth of data in a conditional video generation framework to instantiate a universal simulator (UniSim)1.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Nevertheless, we propose specific strategies for processing each type of data to unify the action space and align videos of variable lengths to actions in ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Under a unified action-in-video-out interface, the simulator enables rich interaction through fine-grained motion control of otherwise static scenes and objects.

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction by combining diverse ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We then formulate the universal simulator as an observation prediction model that predicts observations conditioned on actions and previous observations as shown in Figure 2.
- **p. 1 / ABSTRACT - extractive body cue:** We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps the ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** The simulator can simulate video trajectories from the initial real observation, from which robot actions are recovered using an inverse dynamics model and executed on ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** REINFORCE algorithm (Williams, 1992) to optimize the VLA policy, treating the rollouts from the simulator as the on-policy rollouts from the real environment and use ...
- **p. 1 / ABSTRACT - extractive body cue:** We first make the important observation that natural datasets available for learning a real-world simulator are often rich along different dimensions (e.g., abundant objects in ...
- **Detected method headings:** A.2 ADDITIONAL REAL-ROBOT RESULTS FOR LONG-HORIZON LANGUAGE POLICY (p. 16); A.3 ADDITIONAL RESULTS ON LEARNING RL POLICY IN UNISIM (p. 17); C ARCHITECTURE AND TRAINING (p. 20)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction ... | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | We then formulate the universal simulator as an observation prediction model that predicts observations conditioned on actions and previous observations as shown ... | p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in ... | p. 1 (ABSTRACT), p. 7 (1. Put cup 2. Pen 3. Apple) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1 INTRODUCTION - extractive body cue:** One advantage of this observation prediction model is that the simulator stays the same across all tasks and can be used in combination with any ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** The learned reward function can then be used to optimize policies π(at/ht) using existing decision making algorithms such as planning and RL, as we will ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** REINFORCE algorithm (Williams, 1992) to optimize the VLA policy, treating the rollouts from the simulator as the on-policy rollouts from the real environment and use ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps the ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** Reduction in distance to goal (RDG) defined in Equation 3 across 5 evaluation runs of VLM trained using simulated long-horizon data (bottom row) compared to ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** Finetuning only on simulated data has a large advantage over no finetuning and transfers better to other tasks than finetuning on true data.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 7 (1. Put cup 2. Pen 3. Apple).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | LEARNING, INTERACTIVE, REAL-WORLD, SIMULATOR, define, real, world, model, given, some, state, image, frame, take | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | LEARNING, INTERACTIVE, REAL-WORLD, SIMULATOR, define, real, world, model, given, some | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | combine, wealth, data, conditional, video, generation, framework, instantiate, universal, simulator | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | One, advantage, observation, prediction, model, simulator, stays, same, across, tasks | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2 LEARNING AN INTERACTIVE REAL-WORLD SIMULATOR We define a simulator of the real world as a model that, given some state of the world (e.g., ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** In addition to testing the language instructions and simulated video by converting video trajectory into robot actions executed on the real robot, we also conduct ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** Simulator-RL improves the overall performance, especially in pointing-based tasks which contain limited expert demonstrations. final frame from each long-horizon rollout as a goal input and ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** UniSim is a video diffusion model trained to predict the next (variable length) set of observation frames (ot) given observations from the past (e.g., ot-1) ...
- **p. 6 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** During each evaluation run, we set the long-horizon goal by modifying the location of 3-4 blocks, and measure the blocks' distance to their goal states ...
- **p. 6 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We train an image-goal conditioned VLM policy to predict language instructions and the motor controls from the start and goal images using the PALM-E architecture ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To support long-horizon repeated interactions, we formulate the simulator as an observation 1Note that by "universal", we mean the model can simulate through the unified ...
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | At a specific interactive step t, an agent, having observed a set of history frames ht-1 ∈O, decides on some temporally extended ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | The main contributions can be summarized as follows: • We take the first step toward building a universal simulator of real-world interaction ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | At a specific interactive step t, an agent, having observed a set of history frames ht-1 ∈O, decides on some temporally extended ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / ABSTRACT - extractive body cue:** We use the simulator to train both high-level vision-language policies and low-level reinforcement learning policies, each of which can be deployed in the real world ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps the ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** REINFORCE algorithm (Williams, 1992) to optimize the VLA policy, treating the rollouts from the simulator as the on-policy rollouts from the real environment and use ...
- **p. 7 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** To acquire reward information, we use the number of steps-to-completion from the training data as a proxy reward to train a model that maps the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, summarized, follows, take, first, step, toward, building, universal, simulator, real-world, interaction, combining, diverse, datasets, rich, along, different, dimensions.
- **Relevant PDF headings:** A.2 ADDITIONAL REAL-ROBOT RESULTS FOR LONG-HORIZON LANGUAGE POLICY (p. 16); A.3 ADDITIONAL RESULTS ON LEARNING RL POLICY IN UNISIM (p. 17); C ARCHITECTURE AND TRAINING (p. 20).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | [Bottom] Real-robot execution of an RL policy trained in simulation and zero-shot onto the real Language Table task. | p. 8 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple) |
| Filtering / recovery | Table 2: Evaluation of long-horizon actions. Re- duction in distance to goal (RDG) defined in Equa- tion 3 across 5 evaluation runs ... | p. 7 (Figure/Table caption), p. 8 (1. Put cup 2. Pen 3. Apple) |
| Monitoring / re-entry | Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity ... | p. 22 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We compare PaLI-X finetuned on purely generated videos to pretrained PaLI-X without finetuning and PaLI-X finetuned on original ActivityNet Captions in Table 4.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Ablations of history conditioning using FVD, FID, and Inception score, and CLIP score on Ego4D. Conditioning on multiple frames is better than on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Evaluation of RL policy. Percentage of successful simulated rollouts (out of 48 tasks) using the VLA policy with and without RL finetuning on ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 8: Ablations of datasets using FVD and CLIP score on the held-out test split. Including internet data and diverse human activity and robot data ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 13: Failed environment simulation from the action "uncover bottle" without training on broad data as in UniSim. Top two videos are generated from only ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: Simulations of low-data domains using the Habitat object navigation using HM3D dataset (Ra- makrishnan et al., 2021) with only 700 training exam- ples. ...
- **p. 8 / 1. Put cup 2. Pen 3. Apple - extractive body cue:** We finetune PaLI-X (Chen et al., 2023), a VLM with 55B parameters pretrained on a broad set of image, video, and language tasks, to caption ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 7 (1. Put cup 2. Pen 3. Apple), p. 7 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple), objective p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 8 (1. Put cup 2. Pen 3. Apple), p. 7 (1. Put cup 2. Pen 3. Apple), p. 7 (1. Put cup 2. Pen 3. Apple), p. 8 (1. Put cup 2. Pen 3. Apple), temporal p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 7 (1. Put cup 2. Pen 3. Apple), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 2 LEARNING AN INTERACTIVE REAL-WORLD SIMULATOR We define a simulator of the real world as a model that, given some state of the world (e.g., an image frame), can take ... (p. 2, 1 INTRODUCTION).
- **Objective/update evidence:** The learned reward function can then be used to optimize policies π(at/ht) using existing decision making algorithms such as planning and RL, as we will illustrate in Section 4.1 and ... (p. 4, 1 INTRODUCTION).
- **Temporal/runtime evidence:** At a specific interactive step t, an agent, having observed a set of history frames ht-1 ∈O, decides on some temporally extended action at-1 ∈A, which can be resolved into ... (p. 3, 1 INTRODUCTION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
