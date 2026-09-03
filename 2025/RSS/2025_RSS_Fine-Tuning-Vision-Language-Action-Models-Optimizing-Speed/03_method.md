# Method - Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p017.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p017.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 7 (3) LI regression objective), p. 14 (A. Model Architecture Details), p. 7 (3) LI regression objective), p. 8 (3) LI regression objective)): LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.

## Method Body Digest

- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** For Diffusion Policy training, we use the DROID implementation [22], which conditions action predictions on DistilBERT [42] language embeddings of the task description, We list ...
- **p. 7 / 3) LI regression objective - extractive body cue:** Given that the alternative fine-tuning formulation, along with additional model inputs and outputs, induces a distri bution shift between the base VLA's pretraining and finetuning, ...
- **p. 14 / A. Model Architecture Details - extractive body cue:** These projected features are concatenated with language ‘embeddings along the sequence dimension before being pro- ‘cessed by the Llama-2 decoder to output a 7-limensional robot, ...
- **p. 7 / 3) LI regression objective - extractive body cue:** In this section, we use an augmented version of our VLA fine-tuning recipe (OFT+) that additionally includes feature- ‘wise linear modulation (FiLM) for enhanced language ...
- **p. 8 / 3) LI regression objective - extractive body cue:** We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** DDINOv2 ['s] vision transformers in OpenVLA\s fuse vision backbone, The average tsk description embedling modules visual features throvgh sale and shift operations at each transformer ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate decay ...

## Design Rationale

- **p. 3 / 1. Iyrropucrion - extractive body cue:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.
- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, ...

## Source Evidence Cues

- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** For Diffusion Policy training, we use the DROID implementation [22], which conditions action predictions on DistilBERT [42] language embeddings of the task description, We list ...
- **p. 7 / 3) LI regression objective - extractive body cue:** Given that the alternative fine-tuning formulation, along with additional model inputs and outputs, induces a distri bution shift between the base VLA's pretraining and finetuning, ...
- **p. 14 / A. Model Architecture Details - extractive body cue:** These projected features are concatenated with language ‘embeddings along the sequence dimension before being pro- ‘cessed by the Llama-2 decoder to output a 7-limensional robot, ...
- **p. 7 / 3) LI regression objective - extractive body cue:** In this section, we use an augmented version of our VLA fine-tuning recipe (OFT+) that additionally includes feature- ‘wise linear modulation (FiLM) for enhanced language ...
- **p. 8 / 3) LI regression objective - extractive body cue:** We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** DDINOv2 ['s] vision transformers in OpenVLA\s fuse vision backbone, The average tsk description embedling modules visual features throvgh sale and shift operations at each transformer ...
- **Detected method headings:** 2) How does each design decision affect model inference (p. 5); B. Methods in Comparison (p. 8); A. Model Architecture Details (p. 14); 1) Single OpenVLA-OFT Policy for All LIBERO Task Suites (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to ... | p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | For Diffusion Policy training, we use the DROID implementation [22], which conditions action predictions on DistilBERT [42] language embeddings of the task ... | p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 7 (3) LI regression objective) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Given that the alternative fine-tuning formulation, along with additional model inputs and outputs, induces a distri bution shift between the base VLA's ... | p. 7 (3) LI regression objective), p. 14 (A. Model Architecture Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate decay ...
- **p. 8 / 3) LI regression objective - extractive body cue:** We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size ...
- **p. 14 / B. Implementation Details - extractive body cue:** On the other hhand, with a continuous action representation, the VLA can directly model the action distribution without lossy discretization
- **p. 14 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** [37], we multiply F by (1 +7) instead of 7 since + and 9 are near zero at initialization. ‘This helps preserve the visual encoder's ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** For faster convergence, we decay the leaming rate from Se-4 to Se-S after 100K gradient steps.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (3) LI regression objective), p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | decoding, action, chunking, conti, simple, regression-based, ference, efficiency, policy, performance, flex, inthe, rodel, input-output | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | decoding, action, chunking, conti, simple, regression-based, ference, efficiency, policy, performance | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | next, section, present, parallel, generation, scheme, enables, efficient, action, chunking | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | maintain, same, convergence, criterion, LIBERO, experiments, training, until, mean, normalized | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** ‘decoding, action chunking, a conti and a simple L1 regression-based lea ference efficiency, policy performance, and flex inthe rodel's input-output opecicatios.
- **p. 7 / 3) LI regression objective - extractive body cue:** This setup differs significantly from OpenVLA's pretraining, which includes single-arm robot data only, a single camera viewpoint from 4 third-person camera, no robot state inputs, ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, ...
- **p. 4 / B. Implementing Alternative Design Components - extractive body cue:** First, similar to Zhao et al, [56], we implement LI regression by replacing the decoder's output embedding layer with an MLP action head that directly ...
- **p. 4 / B. Implementing Alternative Design Components - extractive body cue:** During training, policies may learn to latch conto such spurious correlations when predicting actions, rather than properly attending to the language instructions, resulting in poor ...
- **p. 14 / A. Model Architecture Details - extractive body cue:** These projected features are concatenated with language ‘embeddings along the sequence dimension before being pro- ‘cessed by the Llama-2 decoder to output a 7-limensional robot, ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Our parallel decoding approach, when paired with action chunking, achieves significantly greater speedups: 26x to 43% throughput with much lower latency (0.07 ms for single-arm ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | With 25-timestep action ‘chunks, OpenVLA-OFT+ achieves 43% faster throughput than base OpenVLA, demonstrating that our new fine-tuning recipe ‘enables real-time robot control ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Ress include policies finetuned from retained base models (Octo, DIT Policy, Seer xo), models trained from scratch (Diffusion Policy, Seer (rach), MDT), ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Ress include policies finetuned from retained base models (Octo, DIT Policy, Seer xo), models trained from scratch (Diffusion Policy, Seer (rach), MDT), ... | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** For Diffusion Policy training, we use the DROID implementation [22], which conditions action predictions on DistilBERT [42] language embeddings of the task description, We list ...
- **p. 7 / 3) LI regression objective - extractive body cue:** Given that the alternative fine-tuning formulation, along with additional model inputs and outputs, induces a distri bution shift between the base VLA's pretraining and finetuning, ...
- **p. 7 / 3) LI regression objective - extractive body cue:** In this section, we use an augmented version of our VLA fine-tuning recipe (OFT+) that additionally includes feature- ‘wise linear modulation (FiLM) for enhanced language ...
- **p. 8 / 3) LI regression objective - extractive body cue:** We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size ...
- **p. 8 / 3) LI regression objective - extractive body cue:** We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** We maintain the same convergence criterion as in the LIBERO experiments (training until mean normalized LI loss falls below 0.01) and similar learning rate decay ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** regression, MLP, action, head, consists, layers, ReLU, activation, mapping, final, Llama-2, decoder, layer, hidden, states, directly, continuous, actions, Diffusion, Policy.
- **Relevant PDF headings:** 2) How does each design decision affect model inference (p. 5); B. Methods in Comparison (p. 8); A. Model Architecture Details (p. 14); 1) Single OpenVLA-OFT Policy for All LIBERO Task Suites (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, ... | p. 5 (A. LIBERO Experimental Setup), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation) |
| Action / skill decoding | Fine-tuned VLA pol cies generally outperform the from-scratch baselines in both task execution and language following, consistent with prior findings (27, 3]. | p. 8 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup) |
| Receding execution / feedback | Finally, OpenVLA-OFT+ achieves the highest performance across both task execution and language following (see Figure 7 for examples of successful task rollouts). | p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup) |

## Failure and Ablation Link

- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** Note that we do not use FILM for LIBERO ‘experiments since the fine-tuned policies without it already demonstrate good language grounding.
- **p. 14 / B. Implementation Details - extractive body cue:** On the other hhand, with a continuous action representation, the VLA can directly model the action distribution without lossy discretization
- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** Note that Seer uses additional LIBERO90 pretraining data
- **p. 5 / A. LIBERO Experimental Setup - extractive body cue:** Our primary baseline in this study is the base OpenVLA ‘model fine-tuned using the original fine-tuning recipe.
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** datasets (6K episodes and 8K hours of bimanual data, respec tively). ‘This suggests that the fine-tuning technique can be more crucial than pretraining data coverage ...
- **p. 14 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** [37], we multiply F by (1 +7) instead of 7 since + and 9 are near zero at initialization. ‘This helps preserve the visual encoder's ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: OpenVLA-OFT+ on the bimanual ALOHA robot. Our Optimized Fine-Tuning (OFT) recipe enhances fnesuned OpeaVLA pic and inpt-outptfeibliy. The resulting OpeaVLA-OFT+ policies execute diverse ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 7 (3) LI regression objective), p. 14 (A. Model Architecture Details), p. 7 (3) LI regression objective), p. 8 (3) LI regression objective), objective p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 8 (3) LI regression objective), p. 14 (B. Implementation Details), p. 14 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), temporal p. 2 (1. Iyrropucrion), p. 6 (C. LIBERO Inference Efficiency), p. 1 (1. Iyrropucrion), p. 14 (B. Implementation Details), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, and an LI regression objective ... (p. 1, 1. Iyrropucrion).
- **Objective/update evidence:** We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size IK ~ 2 At inference ... (p. 8, 3) LI regression objective).
- **Temporal/runtime evidence:** for non-diffusion methods and 100-250K steps for diffusion methods (which converge slower), using a batch size of 64-128 across 8 A100/H100 GPUs. (p. 5, A. LIBERO Experimental Setup).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
