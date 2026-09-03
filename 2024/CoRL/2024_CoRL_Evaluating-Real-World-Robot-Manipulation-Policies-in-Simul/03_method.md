# Method - Evaluating Real-World Robot Manipulation Policies in Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=LZh48DTg71; PDF retrieval source: https://openreview.net/pdf?id=LZh48DTg71. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We address the challenges inherent in ...

## Method Body Digest

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We ...
- **p. 1 / Abstract - extractive body cue:** We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As such, SIMPLER is a first step towards using simulated evaluation as a tool for reliable, scalable, and reproducible manipulation policy evaluation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These advances are underpinned by large-scale datasets [11, 66] and expressive models [1, 6, 29].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Remarkable progress has been made in recent years towards building generalist real-world robot manipulation policies [6, 50], i.e., policies that can perform a wide range ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Simulated Manipulation Policy Evaluation for Real Robot Setups SIMPLER Pick Coke Can Move Near Open/Close Drawer Put Object in Drawer Google Robot Put Carrot on ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We then propose and evaluate approaches for mitigating these differences based on offline system identification, "green-screening" simulation observations using realworld backgrounds, and object texture baking ...
- **p. 1 / Abstract - extractive body cue:** Additionally, we find that SIMPLER evaluations accurately reflect real-world policy behavior modes such as sensitivity to various distribution shifts.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose simulated evaluation as a possible answer, in which manipulation policies trained on real data are evaluated in purpose-built simulated environments ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: We introduce SIMPLER, a suite of open-source simulated evaluation environments for common real robot manipulation setups, namely the Google Robot evaluations from the RT-series ...

## Source Evidence Cues

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation setups. • We ...
- **p. 1 / Abstract - extractive body cue:** We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As such, SIMPLER is a first step towards using simulated evaluation as a tool for reliable, scalable, and reproducible manipulation policy evaluation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** These advances are underpinned by large-scale datasets [11, 66] and expressive models [1, 6, 29].
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | In summary, our contributions are as follows: • We introduce SIMPLER, a suite of simulated evaluation environments for commonly-used real robot manipulation ... | p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups. | p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | As such, SIMPLER is a first step towards using simulated evaluation as a tool for reliable, scalable, and reproducible manipulation policy evaluation. | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / I. INTRODUCTION - extractive body cue:** Remarkable progress has been made in recent years towards building generalist real-world robot manipulation policies [6, 50], i.e., policies that can perform a wide range ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Simulated, Manipulation, Policy, Evaluation, Real, Robot, Setups, SIMPLER, Pick, Coke, Move, Near, Open/Close, Drawer | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Simulated, Manipulation, Policy, Evaluation, Real, Robot, Setups, SIMPLER, Pick, Coke | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, SIMPLER, suite, simulated, evaluation, environments, commonly-used | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Remarkable, progress, been, made, recent, years, towards, building, generalist, real-world | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Simulated Manipulation Policy Evaluation for Real Robot Setups SIMPLER Pick Coke Can Move Near Open/Close Drawer Put Object in Drawer Google Robot Put Carrot on ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We then propose and evaluate approaches for mitigating these differences based on offline system identification, "green-screening" simulation observations using realworld backgrounds, and object texture baking ...
- **p. 1 / Abstract - extractive body cue:** Additionally, we find that SIMPLER evaluations accurately reflect real-world policy behavior modes such as sensitivity to various distribution shifts.
- **p. 1 / Abstract - extractive body cue:** We then employ these approaches to create SIMPLER, a collection of simulated environments for manipulation policy evaluation on common real robot setups.
- **p. 3 / I. INTRODUCTION - extractive body cue:** • We open-source our workflow for constructing SIMPLER environments to facilitate research on general-purpose manipulation policies and simulated evaluation frameworks.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | For the WidowX environments, given the consistent black color of the arm and gripper across videos, we skip this step. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Additionally, for Google Robot simulated evaluations, we average results over four versions of robot arm and gripper colors to account for changes ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** For evaluations in the Google Robot environments, we additionally use a number of RT-1 [6] checkpoints at various stages of training: RT-1 trained to convergence ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Additionally, we open-source policy inference code for real-to-sim evaluation of common generalist robot policies (RT-1 [6], RT-1-X [11], and Octo [50]), and we provide detailed ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, contributions, follows, introduce, SIMPLER, suite, simulated, evaluation, environments, commonly-used, real, robot, manipulation, setups, address, challenges, inherent, policy, proposing, approaches.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Models that obtain low real-world performance, such as RT1 (Begin) on Google Robot tasks and RT-1-X on BridgeData V2 tasks, similarly have ... | p. 8 (2) Can simulated evaluations not only capture the perfor), p. 9 (2) Can simulated evaluations not only capture the perfor) |
| Baseline harness | Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg). | p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor) |
| Metric / failure reporting | Thus, the approaches we introduced in Section IV-B for narrowing the visual gap between simulated and real scene can significantly improve real-andsim ... | p. 10 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Change in success rate under various distribution shifts for two RT-1 policies trained without and with data augmentation. Success rates are averaged across ...
- **p. 9 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Ablation Studies We ablate the effect of the approaches we introduced in Section IV for closing the control and visual gaps between simulation and real-world ...
- **p. 7 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** mance relationships across different policies, but also accurately reproduce real-world policy behavior modes within the same policy, like sensitivity to various visual distribution shifts?
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Furthermore, "Visual Matching" (VisMatch) outperforms "Variant Aggregation" (VarAgg).
- **p. 8 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** These issues are exacerbated under Variant Aggregation, which has much larger visual distribution shifts to the real world (Fig.
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Sensitivity to physical property gap.
- **p. 10 / 2) Can simulated evaluations not only capture the perfor - extractive body cue:** Sensitivity to choice of physics simulator.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective p. 1 (I. INTRODUCTION), temporal p. 7 (2) Can simulated evaluations not only capture the perfor), p. 7 (2) Can simulated evaluations not only capture the perfor), p. 8 (2) Can simulated evaluations not only capture the perfor), p. 10 (2) Can simulated evaluations not only capture the perfor), p. 6 (II. RELATED WORK), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (22 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Simulated Manipulation Policy Evaluation for Real Robot Setups SIMPLER Pick Coke Can Move Near Open/Close Drawer Put Object in Drawer Google Robot Put Carrot on Plate Stack Cubes Put Eggplant ... (p. 2, I. INTRODUCTION).
- **Objective/update evidence:** These advances are underpinned by large-scale datasets [11, 66] and expressive models [1, 6, 29]. (p. 1, I. INTRODUCTION).
- **Temporal/runtime evidence:** For the WidowX environments, given the consistent black color of the arm and gripper across videos, we skip this step. (p. 7, 2) Can simulated evaluations not only capture the perfor).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
