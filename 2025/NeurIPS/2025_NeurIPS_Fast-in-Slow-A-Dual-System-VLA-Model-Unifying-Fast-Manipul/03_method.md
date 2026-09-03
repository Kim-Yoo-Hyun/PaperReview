# Method - Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=4asFznbzJg; PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/8cf3760422b9d4505589a97c8f9569e7-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction)): Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action (a) Previous Dual-system VLA (b) ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 1 / Abstract - extractive body cue:** To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's ...
- **p. 3 / 1 Introduction - extractive body cue:** Our model demonstrates SOTA performance in both single-arm simulation and dual-arm real-world experiments, while maintaining a high execution frequency.
- **p. 2 / 1 Introduction - extractive body cue:** For the multimodal comprehension component (System 2), we exploit an autoregressive next-token prediction objective to maintain its discrete action generation or high-level language planning capabilities ...
- **p. 1 / 1 Introduction - extractive body cue:** The undamental objective of robotic manipulation learning [3, 4, 5, 6] is to convert real-world sensory data and human instructions into precise control signals.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 2 / 1 Introduction - extractive body cue:** To jointly optimize the reasoning and execution components in FiS-VLA, we introduce a dualaware co-training strategy.
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 1 / Abstract - extractive body cue:** To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's ...
- **p. 3 / 1 Introduction - extractive body cue:** Our model demonstrates SOTA performance in both single-arm simulation and dual-arm real-world experiments, while maintaining a high execution frequency.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy ... | p. 2 (1 Introduction), p. 1 (Abstract) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** For the multimodal comprehension component (System 2), we exploit an autoregressive next-token prediction objective to maintain its discrete action generation or high-level language planning capabilities ...
- **p. 1 / 1 Introduction - extractive body cue:** The undamental objective of robotic manipulation learning [3, 4, 5, 6] is to convert real-world sensory data and human instructions into precise control signals.
- **p. 2 / 1 Introduction - extractive body cue:** To jointly optimize the reasoning and execution components in FiS-VLA, we introduce a dualaware co-training strategy.
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 2 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Block, LLM, Lowfrequency, Highfrequency, Separate, Policy, Model, Feature, Action, Previous, Dual-system, VLA, Fast-in-Slow, Different | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Block, LLM, Lowfrequency, Highfrequency, Separate, Policy, Model, Feature, Action, Previous | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, Fast-in-Slow, FiS, unified, dual-system, VLA, model, embeds | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | multimodal, comprehension, component, System, exploit, autoregressive, next-token, prediction, objective, maintain | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 2 / 1 Introduction - extractive body cue:** Most recent end-to-end approaches [22, 23, 24] leverage VLM as System 2 for high-level feature extraction, while appending an additional policy head as System 1 ...
- **p. 1 / Abstract - extractive body cue:** For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in realworld tasks in terms of average success rate, while achieving a ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 3 / 1 Introduction - extractive body cue:** With a 1:4 operating frequency ratio between System 2 and System 1, FiS-VLA achieves a 117.7 Hz control frequency on an NVIDIA 4090 GPU with ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Building on previous action chunking methods [39, 3], the instruction and scene observation at time step t can provide guidance for a ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | In terms of control frequency, FiS-VLA operates at 21.9 Hz, over 2× faster than CogACT (9.8 Hz) and more than 1.6× faster ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | In terms of control frequency, FiS-VLA operates at 21.9 Hz, over 2× faster than CogACT (9.8 Hz) and more than 1.6× faster ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 2 / 1 Introduction - extractive body cue:** Considering these limitations, and motivated by the functional abstraction of Kahneman's dual-system theory, we raise a question: "If a VLM model serves as the central ...
- **p. 3 / 1 Introduction - extractive body cue:** In summary, our contributions are as follows: • We propose Fast-in-Slow (FiS), a unified dual-system VLA model that embeds System 1 execution within a pretrained ...
- **p. 1 / Abstract - extractive body cue:** To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's ...
- **p. 2 / 1 Introduction - extractive body cue:** Block 1 Block 2 Block 3 LLM Lowfrequency Highfrequency Block n-1 Block 1 Block 2 LLM Block n Lowfrequency Highfrequency Separate Policy Model Feature Action ...
- **p. 7 / 4 Experiments - extractive body cue:** FiS-VLA model is trained for 300 epochs using the AdamW optimizer [74] on 8 NVIDIA A800 GPUs, with mixed-precision training employed.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Block, LLM, Lowfrequency, Highfrequency, Separate, Policy, Model, Feature, Action, Previous, Dual-system, VLA, Fast-in-Slow, Different, Robot, Control, Encoder, Place, wine, rack.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Models Agilex Dual-Arm Robot Task AlphaBot Dual-Arm Robot Task Pick Lift ball Place bottles Wipe Mean Pick bowl and Handover Pour water ... | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Action / skill decoding | Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA ... | p. 9 (Figure/Table caption), p. 7 (4 Experiments) |
| Receding execution / feedback | Figure 4: Visualization of real-world experiments with Agilex and AlphaBot dual-arm robots. Quantitative and qualitative results. As shown in Table 2, FiS-VLA ... | p. 9 (Figure/Table caption), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 29 / Figure/Table caption - extractive body cue:** Figure 7: Ablation studies on action chunk size and input variants of FiS-VLA. (Left) Impact of different action chunk sizes on success rate and inference ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Ablation Study To analyze the impact of each component on overall performance within the FiS-VLA, we conduct ablation experiments on 10 RLBench tasks using ...
- **p. 7 / 4 Experiments - extractive body cue:** The effectiveness of each component is evaluated in Section 4.2 and Appendix B.
- **p. 8 / 4 Experiments - extractive body cue:** More ablation experiments can be found in Appendix B.
- **p. 8 / 4 Experiments - extractive body cue:** If Lslow is removed during training, manipulation performance drops from 69% to 62%.
- **p. 9 / 4 Experiments - extractive body cue:** These results demonstrate that under the proposed FiS-VLA dual-system paradigm, embedding the System 1 execution module within the VLM-based System 2 allows it to better ...
- **p. 31 / Figure/Table caption - extractive body cue:** Table 12: Results of different input variants of FiS-VLA on RLBench. The results in this table correspond to the second subplot of Figure 7 in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 5 (2 Related Work), p. 7 (4 Experiments), p. 5 (2 Related Work), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
