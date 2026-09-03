# Method - AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=NuR4lG4gKB; PDF retrieval source: https://openreview.net/pdf/fa8a077d4c454280e6633258b55a9ff0b4d204e5.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Dataset Construction), p. 5 (3.4. Dataset Construction)): Standardized data interfaces ensure compatibility with the input layers of diverse VLA models.

## Method Body Digest

- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Standardized data interfaces ensure compatibility with the input layers of diverse VLA models.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Tailored to aerial perspectives, the sensor configuration comprises: (1) a UAV front-down RGB-D camera for global bird's-eye views, (2) a manipulator wrist RGB-D camera for ...
- **p. 2 / 1. Introduction - extractive body cue:** Tailored to the unique characteristics of aerial operations, we design a multi-suite dataset rich in sensory information (RGB, depth, proprioception) and diverse language instructions, providing ...
- **p. 2 / 1. Introduction - extractive body cue:** Recently, VisionLanguage-Action (VLA) models, represented by RT-1 (Brohan et al., 2023), OpenVLA (Kim et al., 2024), and π0 (Black et al., 2026), have demonstrated exceptional ...
- **p. 3 / 1. Introduction - extractive body cue:** AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation allow a deep exploration of the performance boundaries of the models. • Comprehensive Baseline Analysis: We conduct extensive benchmarking ...
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Furthermore, LLMs are leveraged to generate natural language instructions featuring complex structures and implicit intents, ensuring dense coverage of the semantic space.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose AIR-VLA, the first VLA training and evaluation benchmark designed specifically for Aerial Manipulation Systems.

## Source Evidence Cues

- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Standardized data interfaces ensure compatibility with the input layers of diverse VLA models.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Tailored to aerial perspectives, the sensor configuration comprises: (1) a UAV front-down RGB-D camera for global bird's-eye views, (2) a manipulator wrist RGB-D camera for ...
- **Detected method headings:** 2.2. Vision-Language-Action Models (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Standardized data interfaces ensure compatibility with the input layers of diverse VLA models. | p. 5 (3.4. Dataset Construction), p. 5 (3.4. Dataset Construction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Tailored to aerial perspectives, the sensor configuration comprises: (1) a UAV front-down RGB-D camera for global bird's-eye views, (2) a manipulator wrist ... | p. 5 (3.4. Dataset Construction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Standardized data interfaces ensure compatibility with the input layers of diverse VLA models. | p. 5 (3.4. Dataset Construction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Tailored, unique, characteristics, aerial, operations, design, multi-suite, dataset, rich, sensory, information, RGB, depth, proprioception | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Tailored, unique, characteristics, aerial, operations, design, multi-suite, dataset, rich, sensory | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, Pioneering, Aerial, Manipulation, VLA, Benchmark, first | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Tailored to the unique characteristics of aerial operations, we design a multi-suite dataset rich in sensory information (RGB, depth, proprioception) and diverse language instructions, providing ...
- **p. 2 / 1. Introduction - extractive body cue:** Recently, VisionLanguage-Action (VLA) models, represented by RT-1 (Brohan et al., 2023), OpenVLA (Kim et al., 2024), and π0 (Black et al., 2026), have demonstrated exceptional ...
- **p. 3 / 1. Introduction - extractive body cue:** AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation allow a deep exploration of the performance boundaries of the models. • Comprehensive Baseline Analysis: We conduct extensive benchmarking ...
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Furthermore, LLMs are leveraged to generate natural language instructions featuring complex structures and implicit intents, ensuring dense coverage of the semantic space.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Tailored to aerial perspectives, the sensor configuration comprises: (1) a UAV front-down RGB-D camera for global bird's-eye views, (2) a manipulator wrist RGB-D camera for ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Regarding task scenarios, VLMs demonstrate excellent temporal stability; their performance in Long-Horizon tasks does not exhibit significant deterioration, standing in sharp contrast ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Tailored to AMS characteristics, the dataset features an average task length of approximately 475 time steps, significantly exceeding traditional benchmarks to reflect ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | We adopted a differentiated fine-tuning strategy based on task difficulty: 30 trajectories were used for fine-tuning simple single-step tasks with less physical ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Standardized, data, interfaces, ensure, compatibility, input, layers, diverse, VLA, models, Tailored, aerial, perspectives, sensor, configuration, comprises, UAV, front-down, RGB-D, camera.
- **Relevant PDF headings:** 2.2. Vision-Language-Action Models (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, ... | p. 4 (3.2. Evaluation Framework), p. 5 (4.1. VLA Experiments) |
| Baseline harness | Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in the AIR-VLA evaluation, outperforming traditional imitation ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 7 (4.2.2. RESULTS AND ANALYSIS) |
| Metric / failure reporting | Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS) |

## Failure and Ablation Link

- **p. 5 / 4.1.1. EXPERIMENTAL SETUP - extractive body cue:** To establish a representative benchmark, we evaluate six diverse models: π0 (Black et al., 2026) and π0.5 (Black et al., 2025), Flow Matching-based foundation models ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Notably, even under few-shot fine-tuning settings with only 30-50 demonstrations, foundation models like π0.5 rapidly adapt to aerial manipulation paradigms unseen during pretraining, achieving the ...
- **p. 6 / 4.1.1. EXPERIMENTAL SETUP - extractive body cue:** We adopted a differentiated fine-tuning strategy based on task difficulty: 30 trajectories were used for fine-tuning simple single-step tasks with less physical interaction, while 50 ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Notably, in spatial understanding tasks, the models exhibit Spatial Grounding Failure: although the correct object category is identified, the agent manipulates an identical object at ...
- **p. 7 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** In summary, VLMs hold immense potential for high-level planning in aerial manipulation, particularly in mitigating the long-horizon reasoning limitations of VLA models.
- **p. 8 / 5. Conclusion - extractive body cue:** Our findings reveal that while transferring pre-trained VLA models to aerial platforms is feasible, existing models still face severe challenges in handling floating-base dynamic coupling, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. Dataset Construction), p. 5 (3.4. Dataset Construction), objective 본문 anchor 없음, temporal p. 7 (4.2.2. RESULTS AND ANALYSIS), p. 4 (4) Long-horizon), p. 4 (3.2. Evaluation Framework), p. 5 (4.1.1. EXPERIMENTAL SETUP), p. 6 (4.1.1. EXPERIMENTAL SETUP), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
