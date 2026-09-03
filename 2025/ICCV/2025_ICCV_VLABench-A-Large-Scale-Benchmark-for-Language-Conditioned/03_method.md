# Method - VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (Model), p. 7 (4.2. Zero-shot Ability of Agent), p. 8 (4.2. Zero-shot Ability of Agent), p. 6 (3.4. Dataset Construction), p. 8 (4.2. Zero-shot Ability of Agent), p. 6 (3.4. Dataset Construction)): We also discuss in detail the potential issues with current VLAs, such as multimodal data co-training and model architecture designs.

## Method Body Digest

- **p. 7 / Model - extractive body cue:** We also discuss in detail the potential issues with current VLAs, such as multimodal data co-training and model architecture designs.
- **p. 7 / 4.2. Zero-shot Ability of Agent - extractive body cue:** For our evaluation of foundation model-based algorithms, we reviewed two state-of-the-art frameworks, Voxposer [25] and CoPA [24], and the comparison results are shown in Figure ...
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** The reason why only GLM-4V-9B is evaluated in a zero-shot setting is that it does not support multigraph inference, which is required for the other ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** Voxposer w uses GPT-4V as the visual perception module.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** The data collection framework includes multiple task-specific motion planners.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** The final trajectory is smoothed using a Bezier curve to optimize path quality.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** These motion planners call upon the skills in the skill library based on the current task progress and determine parameters by incorporating prior information.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** We summarize contributions as follows: • We propose VLABench, the first benchmark designed to comprehensively evaluate the capabilities of VLAs and VLMs in robotics manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To better define the types of language-conditioned manipulation tasks suited for foundation models and provide a standardized evaluation suite to advance robotics research, we introduce ...
- **p. 8 / 4.3. Comprehensive Ability of VLMs - extractive body cue:** This dataset consists of a complex set of tasks designed to assess the VLM's ability to perceive visual stimuli and comprehend verbal instructions.

## Source Evidence Cues

- **p. 7 / Model - extractive body cue:** We also discuss in detail the potential issues with current VLAs, such as multimodal data co-training and model architecture designs.
- **p. 7 / 4.2. Zero-shot Ability of Agent - extractive body cue:** For our evaluation of foundation model-based algorithms, we reviewed two state-of-the-art frameworks, Voxposer [25] and CoPA [24], and the comparison results are shown in Figure ...
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** The reason why only GLM-4V-9B is evaluated in a zero-shot setting is that it does not support multigraph inference, which is required for the other ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** Voxposer w uses GPT-4V as the visual perception module.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** The data collection framework includes multiple task-specific motion planners.
- **Detected method headings:** Model (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We also discuss in detail the potential issues with current VLAs, such as multimodal data co-training and model architecture designs. | p. 7 (Model), p. 7 (4.2. Zero-shot Ability of Agent) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | For our evaluation of foundation model-based algorithms, we reviewed two state-of-the-art frameworks, Voxposer [25] and CoPA [24], and the comparison results are ... | p. 7 (4.2. Zero-shot Ability of Agent), p. 8 (4.2. Zero-shot Ability of Agent) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The reason why only GLM-4V-9B is evaluated in a zero-shot setting is that it does not support multigraph inference, which is required ... | p. 8 (4.2. Zero-shot Ability of Agent), p. 6 (3.4. Dataset Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.4. Dataset Construction - extractive body cue:** The final trajectory is smoothed using a Bezier curve to optimize path quality.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** These motion planners call upon the skills in the skill library based on the current task progress and determine parameters by incorporating prior information.
- **p. 7 / Model - extractive body cue:** Among these, the performance decline is more pronounced in models based on non-VLM architectures: RDT's progress score decreases by 45.2% while OpenVLA and π0 only ...
- **p. 7 / 4.2. Zero-shot Ability of Agent - extractive body cue:** While Voxposer performed adequately on basic tasks and achieved the Progress Scores of 30-40, its reliance on LLMdriven motion planning often led to grasping failures ...
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** Evaluation progress score for Voxposer and CoPA.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | strong, generalization, capabilities, inspired, main, approaches, language-conditioned, manipulation, pre-training, visionlanguage-action, models, large-scale, robotics, data | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | strong, generalization, capabilities, inspired, main, approaches, language-conditioned, manipulation, pre-training, visionlanguage-action | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | summarize, contributions, follows, VLABench, first, benchmark, designed, comprehensively, evaluate, capabilities | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | final, trajectory, smoothed, Bezier, curve, optimize, path, quality, motion, planners | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** The strong generalization capabilities has inspired two main approaches in language-conditioned manipulation: pre-training visionlanguage-action models using large-scale robotics data, as demonstrated by RT-2 and Palm-E ...
- **p. 2 / 1. Introduction - extractive body cue:** Such tasks require agents to master multiple capabilities: interpreting natural language instructions, understanding complex environments, making decisions, formulating plans, and executing precise actions.
- **p. 8 / 4.3. Comprehensive Ability of VLMs - extractive body cue:** Besides, performance declines significantly when linguistic instructions transition from direct semantics to abstract meanings, as shown in the 3As GLM-4V-9B does not support multiple image ...
- **p. 7 / 4.2. Zero-shot Ability of Agent - extractive body cue:** The lack of closed-loop feedback limits these models' ability to perform physical reasoning tasks, particularly those involving dynamic interactions, leading to lower scores in this ...
- **p. 7 / 4.2. Zero-shot Ability of Agent - extractive body cue:** For our evaluation of foundation model-based algorithms, we reviewed two state-of-the-art frameworks, Voxposer [25] and CoPA [24], and the comparison results are shown in Figure ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** Section 8.4 provides more details of the instruction generation.
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** We use GPT-4o [1] to generate descriptions that incorporate target-specific characteristics and interactive instructions that encompass a variety of contexts and intentions.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Composite tasks have a significantly longer trajectory horizon, with an average episode length exceeding 500 timesteps-considerably more than the average of 120 ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | VLABench stands out from previous benchmarks in four key aspects: 1) tasks requiring world knowledge and common sense transfer, 2) natural language ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks Shiduo Zhang1, Zhe Xu1, Peiju Liu1*, Xiaopeng Yu1*, Yuan Li1, ... | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | We then assessed the models across 50 episodes for each task, resulting in a total of 250 trials per track. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / Model - extractive body cue:** We also discuss in detail the potential issues with current VLAs, such as multimodal data co-training and model architecture designs.
- **p. 8 / 4.2. Zero-shot Ability of Agent - extractive body cue:** The reason why only GLM-4V-9B is evaluated in a zero-shot setting is that it does not support multigraph inference, which is required for the other ...
- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** discuss, detail, potential, issues, current, VLAs, multimodal, data, co-training, model, architecture, designs, evaluation, foundation, model-based, algorithms, reviewed, state-of-the-art, frameworks, Voxposer.
- **Relevant PDF headings:** Model (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Following the approach of previous benchmarks built on Mujoco [38, 47], the dataset is stored in the same format, with similar visual ... | p. 6 (3.4. Dataset Construction), p. 5 (3.3. Benchmark) |
| Baseline harness | The progress score refers to the completion level of subtasks in a long-horizon task and serves as a softer process supervision metric ... | p. 6 (3.3. Benchmark), p. 3 (Figure/Table caption) |
| Metric / failure reporting | In addition to the success rate (SR), considering the long-horizon nature and high difficulty level of our tasks, we introduce the intention ... | p. 5 (3.3. Benchmark), p. 6 (3.3. Benchmark) |

## Failure and Ablation Link

- **p. 6 / 3.4. Dataset Construction - extractive body cue:** During the data construction process, we introduced diverse task variants and domain randomization across different episodes of the same task to ensure the diversity of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Evaluation progress score for Voxposer and CoPA. Vox- poser w/o refers to the version without visual perception, where ground truth labels are directly ...
- **p. 6 / 4.1. Generalization Ability of VLAs - extractive body cue:** Pretrained VLAs are expected to possess robust generalization and versatility similar to LLMs.
- **p. 4 / 3.3. Benchmark - extractive body cue:** VLABench organizes evaluations into three categories: assessments of pretrained or fine-tuned visionlanguage-action (VLA) models, heuristic workflows that integrate foundation models with various algorithms, and multi-dimensional ...
- **p. 5 / 3.3. Benchmark - extractive body cue:** Building upon Track 1, replace the instructions with unseen and more complex ones. - Track 5: Cross-domain behavior transferability.
- **p. 5 / 3.3. Benchmark - extractive body cue:** The evaluation tasks are replaced with ones that differ from those in the training set, but require similar actions. - Track 6: Long-horizon task learning.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Overall experiment result of 6 evaluation tracks of fine-tuned VLAs. The detailed result of each task is reported in Table 9. above, we ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (Model), p. 7 (4.2. Zero-shot Ability of Agent), p. 8 (4.2. Zero-shot Ability of Agent), p. 6 (3.4. Dataset Construction), p. 8 (4.2. Zero-shot Ability of Agent), p. 6 (3.4. Dataset Construction), objective p. 6 (3.4. Dataset Construction), p. 6 (3.4. Dataset Construction), p. 7 (Model), p. 7 (4.2. Zero-shot Ability of Agent), p. 8 (4.2. Zero-shot Ability of Agent), temporal p. 4 (3.1. Task Description), p. 1 (Abstract), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.1. Generalization Ability of VLAs).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
