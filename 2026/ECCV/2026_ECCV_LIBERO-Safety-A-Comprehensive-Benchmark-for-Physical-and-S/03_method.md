# Method - LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.23686; PDF retrieval source: https://arxiv.org/pdf/2606.23686. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION), p. 5 (462 Hand-Object Pairs), p. 2 (462 Hand-Object Pairs)): Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance Consi ...

## Method Body Digest

- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA GR00T N1.5 GR00T ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent progress in data scaling, model architectures, and policy optimization has significantly advanced their capabilities, yielding improved task success, stronger generalization, and broader transfer across ...
- **p. 5 / 462 Hand-Object Pairs - extractive body cue:** 3 VLA Safety Benchmark To systematically evaluate the safety boundaries and robustness of VLA models, we propose a comprehensive benchmark framework.
- **p. 2 / 462 Hand-Object Pairs - extractive body cue:** We then conduct a systematic crossparadigm evaluation of eight VLA and two embodied foundation models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.
- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** To guarantee kinematic feasibility and strict adherence to safety constraints, all generated motions are subjected to a rigorous human-in-the-loop screening process, ultimately yielding a final ...

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** To systematically evaluate these challenges, we introduce a comprehensive VLA safety benchmark and develop an efficient (b) Data Generation Pipeline to synthesize 19.7K strictly collision-free ...

## Source Evidence Cues

- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA GR00T N1.5 GR00T ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent progress in data scaling, model architectures, and policy optimization has significantly advanced their capabilities, yielding improved task success, stronger generalization, and broader transfer across ...
- **p. 5 / 462 Hand-Object Pairs - extractive body cue:** 3 VLA Safety Benchmark To systematically evaluate the safety boundaries and robustness of VLA models, we propose a comprehensive benchmark framework.
- **p. 2 / 462 Hand-Object Pairs - extractive body cue:** We then conduct a systematic crossparadigm evaluation of eight VLA and two embodied foundation models.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.
- **Detected method headings:** C.1 Model Details (p. 30)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory ... | p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input ... | p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA ... | p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 462 Hand-Object Pairs - extractive body cue:** To guarantee kinematic feasibility and strict adherence to safety constraints, all generated motions are subjected to a rigorous human-in-the-loop screening process, ultimately yielding a final ...
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Despite the impressive manipulation capabilities of VisionLanguage-Action (VLA) models, their operational safety under strict constraints remains largely unverified.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Reliable deployment demands motion-level reliability and constraint satisfaction during close human-robot interaction.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** More recently, VLA-Arena [52] has introduced dynamic elements and basic safety constraints to evaluate multimodal robustness.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This infrastructure drives a fivedimensional curriculum that decouples safety into semantic reasoning and physical constraints. - Keypose-Driven Data Generation Pipeline: To overcome the inefficiency and ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we establish this evaluation framework through four core technical and empirical contributions: - Parametric Safety Benchmark and Taxonomy: We introduce the Unified Behavior ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 6 (462 Hand-Object Pairs).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Image, Input, Text, Instruction, Multi-modal, VLM, Action, Decoder, Proprioception, Tokens, World, Model, Future, State | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Image, Input, Text, Instruction, Multi-modal, VLM, Action, Decoder, Proprioception, Tokens | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | summary, establish, evaluation, framework, through, four, core, technical, empirical, contributions | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | guarantee, kinematic, feasibility, strict, adherence, safety, constraints, generated, motions, subjected | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** Image Input Text Instruction Multi-modal VLM Action Decoder Proprioception Action Tokens World Model Image Input Text Instruction Future State Action Image Input Text Instruction Sys.
- **p. 1 / 462 Hand-Object Pairs - extractive body cue:** 1 Fast, Low-Level Control High-Frequency Data Planner/ Policy Affordance-Aware Grasping Tabletop Spatial Avoidance Human-Robot Interaction Free-Space Hand-Object Avoidance OpenVLA OpenVLA-OFT VLA-JEPA UniVLA GR00T N1.5 GR00T ...
- **p. 6 / 462 Hand-Object Pairs - extractive body cue:** While the standard BDDL focuses primarily on deterministic symbolic states and logical goal satisfaction, our UBDDL extends task definitions by integrating high-fidelity stochasticity, dynamic interactive ...
- **p. 7 / 462 Hand-Object Pairs - extractive body cue:** 2(b)(5)), and finally to robustly executing safe actions despite diverse paraphrased natural language instructions (L2, Fig.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In contrast, our framework holistically assesses semantic reasoning to refuse malicious instructions, general human-robot interaction (HRI) safety for collaborative co-habitation, and uniquely introduces proximal avoidance ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Vision-Language-Action models (VLAs) have become a key direction for building general-purpose robotic intelligence [30].
- **p. 6 / 462 Hand-Object Pairs - extractive body cue:** Specifically, Csafety is instantiated as state-dependent Boolean predicates that enforce continuous physical bounds, such as maintaining a strict collision-free margin between the robot and the ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | These critical structural refinements, coupled with an expanded temporal receptive field, drastically enhance the model's capacity to denoise long-horizon continuous action sequences ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | In practice, we apply the filter in a receding-horizon manner: at each chunk boundary, the VLA predicts a nominal chunk, the chunk-level ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Hyperparameter Value Total Training Steps 30, 000 Global Batch Size 256 Peak Learning Rate 5.0 × 10-5 Warmup Steps 10, 000 Training ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our results reveal that while high-diversity training fosters safer trajectories, task success remains bottlenecked by sub-optimal trajectory synthesis and semantic misalignment.
- **p. 36 / C.2 Training Configurations - extractive body cue:** Parameter Value Optimization Steps 30, 000 Local Batch Size (per GPU) 8 Gradient Accumulation Steps 2 Constant Learning Rate 3.5 × 10-4 Image Augmentation True ...
- **p. 35 / C.2 Training Configurations - extractive body cue:** Hyperparameter Value Total Training Steps 30, 000 Global Batch Size 256 Peak Learning Rate 5.0 × 10-5 Warmup Steps 10, 000 Training Precision bfloat16 EMA ...
- **p. 35 / C.2 Training Configurations - extractive body cue:** Hyperparameter Value Total Training Steps 30, 000 Global Batch Size 32 Peak Learning Rate (η) 2.5 × 10-5 Training Precision bfloat16 Learning Rate Schedule Cosine ...
- **p. 37 / C.2 Training Configurations - extractive body cue:** Training Setting Value Total Optimization Steps 20, 000 Global Batch Size 640 Initial Learning Rate 1.0 × 10-4 Warmup Ratio 5% State Dropout (p) 0.8 ...
- **p. 37 / C.2 Training Configurations - extractive body cue:** Training Setting Value Total Optimization Steps 60, 000 Global Batch Size 1, 024 Initial Learning Rate 1.0 × 10-4 Warmup Ratio 5% GR00T N1.5 For ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Metric, Human, Teleoperation, Ours, Effort, min/task, Data, Scalability, Collision, Guarantee, Human-dependent, Planner-enforced, Spatial, Representation, World-centric, Object-centric, Trajectory, Consistency, High, variance.
- **Relevant PDF headings:** C.1 Model Details (p. 30).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | In our benchmark, the barrier function is defined by a distance-based safety margin: \la b el {e q:d i stance_barrier} h(z_t)= d(z_t,\mathcal ... | p. 40 (C.3 Additional Experimental Results), p. 14 (4 Experiment) |
| Baseline harness | Across diverse axes of visual and state stochasticity, including image noise (Noise), robot initial state (Init State), viewpoint shifts (View), and scene ... | p. 13 (4 Experiment), p. 10 (4 Experiment) |
| Metric / failure reporting | Among the evaluated standard VLAs, π0.5 achieves the highest overall success rate across all suites and difficulty levels. | p. 11 (4 Experiment), p. 10 (4 Experiment) |

## Failure and Ablation Link

- **p. 38 / C.3 Additional Experimental Results - extractive body cue:** To distinguish the safety-evaluation difficulty from the effect of training on LIBERO-Safety, we additionally evaluate two representative policies under two control settings: zero-shot inference without ...
- **p. 32 / C.1 Model Details - extractive body cue:** Functioning as a generative world model, it is pretrained on internet-scale video data to predict future visual observations from interleaved multi-modal histories, effectively deriving task-centric ...
- **p. 31 / C.1 Model Details - extractive body cue:** This architecture leverages large-scale vision-language pre-training to execute complex, language-conditioned manipulation tasks through standard text-generation pipelines. - OpenVLA-OFT [22]: A parameter-efficient variant of the base ...
- **p. 37 / C.2 Training Configurations - extractive body cue:** To effectively balance the pre-trained components with the newly initialized action head, we implement a differential learning rate strategy using the AdamW optimizer (β1 = ...
- **p. 38 / C.2 Training Configurations - extractive body cue:** Zero-shot models are evaluated without task-specific fine-tuning, while obstacle-free SFT models are fine-tuned on demonstrations without explicit safety-critical obstacle interactions.
- **p. 39 / C.3 Additional Experimental Results - extractive body cue:** Method SR (%) ↑LDLJ ↑Time (s) ↓CR (%) ↓ OpenVLA-OFT, 50 demos/task 35.3 -17.94 380.5 20.0 OpenVLA-OFT, 500 demos/task 42.7 -17.67 372.0 11.7 The embodied ...
- **p. 10 / 4 Experiment - extractive body cue:** Consequently, we use the Success Rate (SR) as our primary metric, which strictly requires goal completion without any constraint violations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION), p. 5 (462 Hand-Object Pairs), p. 2 (462 Hand-Object Pairs), objective p. 8 (462 Hand-Object Pairs), p. 1 (462 Hand-Object Pairs), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), temporal p. 33 (C.1 Model Details), p. 40 (C.3 Additional Experimental Results), p. 42 (C.3 Additional Experimental Results), p. 13 (4 Experiment), p. 13 (4 Experiment), p. 32 (C.1 Model Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (42 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Metric Human Teleoperation Ours Human Effort (min/task) 7.4 1.8 Data Scalability 1:1 1:M Collision Guarantee Human-dependent Planner-enforced Spatial Representation World-centric Object-centric Trajectory Consistency High variance Consi ... (p. 8, 462 Hand-Object Pairs).
- **Objective/update evidence:** Despite the impressive manipulation capabilities of VisionLanguage-Action (VLA) models, their operational safety under strict constraints remains largely unverified. (p. 1, 462 Hand-Object Pairs).
- **Temporal/runtime evidence:** Sparklines show L0-L2 trends from left to right with a shared 0-1 y-axis; values above/below each plot are success rate / safety violation rate. - UniVLA [8]: A universal, cross-embodiment ... (p. 32, C.1 Model Details).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
