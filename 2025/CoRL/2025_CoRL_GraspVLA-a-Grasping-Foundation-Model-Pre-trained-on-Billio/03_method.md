# Method - GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/deng25a.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction), p. 7 (5 Hz)): In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data acquisition burden, ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 7 / 5 Hz - extractive body cue:** We benchmark GraspVLA against AnyGrasp [14], a state-of-the-art grasp detection model specialized in grasping.
- **p. 7 / 5 Hz - extractive body cue:** 5.5 Efficient Post-Training A defining characteristic of foundation models is their ability to adapt to new tasks.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 2 / 1 Introduction - extractive body cue:** To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 7 / 5 Hz - extractive body cue:** We benchmark GraspVLA against AnyGrasp [14], a state-of-the-art grasp detection model specialized in grasping.
- **p. 7 / 5 Hz - extractive body cue:** 5.5 Efficient Post-Training A defining characteristic of foundation models is their ability to adapt to new tasks.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into ... | p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data. | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect.
- **p. 2 / 1 Introduction - extractive body cue:** However, gathering real-world data at a large scale is both labor-intensive and costly, requiring a large number of robots and human operators, as well as ...
- **p. 2 / 1 Introduction - extractive body cue:** PAG treats perception tasks, i.e., visual grounding and grasping pose prediction, as intermediate steps in action generation, forming a CoT process that causally infers actions.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Compared, AnyGrasp, state-of-the-art, traditional, grasping, detection, algorithms, GraspVLA, supports, natural, language, instructions, delivers, robust | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Compared, AnyGrasp, state-of-the-art, traditional, grasping, detection, algorithms, GraspVLA, supports, natural | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, novel, pretraining, paradigm, relies, entirely, synthetic | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Synthetic, data, offers, cost-effective, alternative, potential, remains, largely, underexplored, However | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Compared to AnyGrasp [14], the state-of-the-art in traditional grasping detection algorithms, GraspVLA supports natural language instructions and delivers a robust closed-loop grasping policy.
- **p. 2 / 1 Introduction - extractive body cue:** These models process robotic visual observations and human instructions to directly generate robot actions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 7 / 5 Hz - extractive body cue:** In the language-conditioned test set, both model achieve similar performance, with GraspVLA slightly outperforming AnyGrasp in grounding ability, due to its comprehensive multiview observation.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks.
- **p. 7 / 5 Hz - extractive body cue:** We benchmark GraspVLA against AnyGrasp [14], a state-of-the-art grasp detection model specialized in grasping.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | The action expert is supervised with flow matching loss on chunked end-effector delta actions: LS1 = ∥vt(At, x, ybbox, ygrasp) -ut(At / ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To facilitate accurate 3D sensing, the proprioceptions from the latest two timesteps are tokenized and inserted before generating grasp pose. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | High-quality meshes are often large, leading to lengthy loading times and significant memory usage. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | In other words, we test each method for 15 × 2 × 5 × 2 = 300 trials in total. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** To bridge this gap, we explore the feasibility of training Vision-Language-Action (VLA) models entirely with large-scale synthetic action data.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Abstract: Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
- **p. 3 / 1 Introduction - extractive body cue:** scale globally, c) we propose Progressive Action Generation to co-train synthetic actions with Internet data, extending GraspVLA's skills to novel object categories, and d) extensive ...
- **p. 7 / 5 Hz - extractive body cue:** 5.5 Efficient Post-Training A defining characteristic of foundation models is their ability to adapt to new tasks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, contributions, follows, introduce, novel, pretraining, paradigm, relies, entirely, synthetic, action, data, significantly, reducing, real, world, acquisition, burden, curate, billion-frame.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We define synthetic categories as those present in our SynGrasp-1B dataset, while web categories refer to those exclusively present in Internet grounding ... | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Action / skill decoding | Additionally, the SPL metric reveals that GraspVLA grasps objects with shorter path lengths compared to π0 baselines which often exhibit hesitation. | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Receding execution / feedback | Table 14: Impact of number of input views. Comparison of GraspVLA with different numbers of input views. The results demonstrate that while ... | p. 24 (Figure/Table caption), p. 6 (5 Experiments) |

## Failure and Ablation Link

- **p. 6 / 5 Experiments - extractive body cue:** Additionally, to assess the effectiveness of pre-training on SynGrasp-1B, we report results of direct fine-tuning π0 from its VLM weights [77], without its cross-embodiment robotic ...
- **p. 6 / 5 Experiments - extractive body cue:** Interestingly, the π0 baseline without cross-embodiment pre-training performs better than its pre-trained counterpart, suggesting 6
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 10: Scaling laws different training regimes. (a) Performance scaling with number of train- ing frames in both simulation and real-world environments. (b) Impact of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Efficient post-training. GraspVLA shows superior adaptability to novel tasks, surpassing the model without pre- training and all baselines. As shown in Table 4, ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 13: Impact of instruction format. Fine-tuned baselines exhibit performance drops when the original instructions are simplified. H Details about Comparison with AnyGrasp Setup. To ...
- **p. 7 / 5 Experiments - extractive body cue:** It surpasses π0 and OpenVLA fine-tuned on the LIBERO dataset, demonstrating strong generalizability.
- **p. 7 / 5 Experiments - extractive body cue:** The zero-shot performance of GraspVLA surpasses the fine-tuned performance of strong baselines π0 and OpenVLA.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (1 Introduction), p. 7 (5 Hz), objective p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 5 (2 Related Work), p. 5 (2 Related Work), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Compared to AnyGrasp [14], the state-of-the-art in traditional grasping detection algorithms, GraspVLA supports natural language instructions and delivers a robust closed-loop grasping policy. (p. 2, 1 Introduction).
- **Objective/update evidence:** Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. (p. 1, Body text (section boundary not confidently recovered)).
- **Temporal/runtime evidence:** In other words, we test each method for 15 × 2 × 5 × 2 = 300 trials in total. (p. 6, 5 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
