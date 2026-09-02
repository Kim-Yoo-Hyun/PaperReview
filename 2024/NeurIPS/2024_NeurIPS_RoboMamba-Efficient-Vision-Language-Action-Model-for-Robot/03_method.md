# Method - RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (1.1 Hz), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1.1 Hz), p. 3 (1.1 Hz)): In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, which possesses visual common sense ...

## Method Body Digest

- **p. 3 / 1.1 Hz - extractive body cue:** In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, ...
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba Language Model Tokenizer ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 3 / 1.1 Hz - extractive body cue:** Moreover, RoboMamba achieves an inference speed that is 3 times faster than previous robotic VLA models [29, 15].
- **p. 1 / Abstract - extractive body cue:** A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions.
- **p. 1 / Abstract - extractive body cue:** Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability ...

## Design Rationale

- **p. 3 / 1.1 Hz - extractive body cue:** In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, ...
- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 2 / 1.1 Hz - extractive body cue:** Subsequently, we introduce an efficient fine-tuning strategy to equip RoboMamba with pose prediction abilities, requiring a few dozen minutes to fine-tune a simple policy head ...

## Source Evidence Cues

- **p. 3 / 1.1 Hz - extractive body cue:** In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, ...
- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba Language Model Tokenizer ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 3 / 1.1 Hz - extractive body cue:** Moreover, RoboMamba achieves an inference speed that is 3 times faster than previous robotic VLA models [29, 15].
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the ... | p. 3 (1.1 Hz), p. 1 (Abstract) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba ... | p. 2 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions.
- **p. 1 / Abstract - extractive body cue:** Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability ...
- **p. 2 / 1.1 Hz - extractive body cue:** Second, fine-tuning MLLMs and using them to generate robot manipulation actions incurs higher computational costs due to their expensive attention-based LLMs [20, 21].
- **p. 2 / 1.1 Hz - extractive body cue:** Drawing inspiration from this, we raise a question: "Can we develop an efficient robotic VLA model that possesses strong reasoning capabilities while also acquiring robot ...
- **p. 3 / 1.1 Hz - extractive body cue:** We find that once RoboMamba achieves sufficient reasoning capabilities, it can acquire pose prediction skills with minimal cost. • In our extensive experiments, RoboMamba excels ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 1 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision, encoder, linear-complexity, Mamba, LLM | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | fundamental, objective, robot, manipulation, enable, models, comprehend, visual, scenes, execute | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1.1 Hz - extractive body cue:** In summary, our contributions are as follows: • We introduce RoboMamba, an efficient VLA model that integrates a vision encoder with the linear-complexity Mamba LLM, ...
- **p. 3 / 1.1 Hz - extractive body cue:** With its strong reasoning abilities, RoboMamba achieves state-of-the-art (SOTA) manipulation performance in the SAPIEN simulation [28], requiring only a 7MB policy head and a few ...
- **p. 1 / 1 Introduction - extractive body cue:** On the other hand, Vision-Language-Action (VLA) models [13-15] leverage the inherent capabilities of MLLMs, empowering them with the ability to predict low-level SE(3) poses. ∗Project ...
- **p. 2 / 1.1 Hz - extractive body cue:** In this way, RoboMamba can simultaneously generate robot reasoning using language responses and predict end-effector poses via the policy head.
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba Language Model Tokenizer ...
- **p. 1 / Abstract - extractive body cue:** The recently proposed state space model (SSM) known as Mamba demonstrates promising capabilities in non-trivial sequence modeling with linear inference complexity.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Notably, we also directly evaluate RoboMamba's robotic-related reasoning abilities on the 18k validation dataset of RoboVQA, covering robotic tasks such as long-horizon ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Meanwhile, our proposed RoboMamba VLA framework and training strategy can also be adapted to other, more advanced linear-complexity LLM models. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient ...
- **p. 2 / 1 Introduction - extractive body cue:** Manipulation Q: Given <image> Predict the contact point and orientation for pulling the {object} Question: Predict the contact point … RoboMamba Mamba Language Model Tokenizer ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and ...
- **p. 3 / 1.1 Hz - extractive body cue:** Moreover, RoboMamba achieves an inference speed that is 3 times faster than previous robotic VLA models [29, 15].
- **p. 7 / 4 Experiment - extractive body cue:** Implementation details Before training, RoboMamba loads a pre-trained CLIP/SigLIP ViT-Large [26, 70] as the visual encoder, and the 2.8/1.4B Mamba [1] model as the language ...
- **p. 8 / 4 Experiment - extractive body cue:** For a fair comparison, we load the pre-trained parameters of both LLaMAAdapterV2 and TinyLLaVA and fine-tuned the baseline models on the RoboVQA training set for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summary, contributions, follows, introduce, RoboMamba, efficient, VLA, model, integrates, vision, encoder, linear-complexity, Mamba, LLM, possesses, visual, common, sense, robotic-related, reasoning.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Datasets (Stage 2) For the dataset used in the robot manipulation fine-tuning stage, we follow the data collection process of previous works ... | p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Action / skill decoding | We choose LLaMA-AdapterV2 as a baseline because it serves as the base model for the current state-of-the-art (SOTA) robot MLLM, ManipLLM [15]. | p. 8 (4 Experiment), p. 7 (4 Experiment) |
| Receding execution / feedback | As shown in Table 2, our RoboMamba achieves a 7.0% improvement on seen tasks and a 2.0% improvement on unseen tasks compared ... | p. 8 (4 Experiment), p. 9 (4 Experiment) |

## Failure and Ablation Link

- **p. 7 / 4 Experiment - extractive body cue:** validate the effectiveness of each method design, we perform an ablation study in Section 4.4.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of RoboMamba. RoboMamba is an efficient robotic VLA model that combines reasoning and manipulation capabilities. First, we integrate and align a vision ...
- **p. 9 / 4 Experiment - extractive body cue:** 4.4 Ablation study The impact of LLM on reasoning abilities.
- **p. 9 / 4 Experiment - extractive body cue:** Additionally, we present more ablation studies in Appendix C, including explorations of different vision encoders, training datasets, and policy head design.
- **p. 10 / 4 Experiment - extractive body cue:** This finding reveals how to efficiently equip an VLA model with manipulation abilities without compromising its inherent reasoning capabilities.
- **p. 19 / Figure/Table caption - extractive body cue:** Table 6: Ablation study of policy head design on manipulation dataset.
- **p. 19 / Figure/Table caption - extractive body cue:** Table 5: Ablation study of training strategies on MLLM reasoning benchmarks. LLaVA 1.5 ShareGPT4V-SFT LLaVA-Next Robo-300k GQA POPE RoboVQA4

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (1.1 Hz), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1.1 Hz), p. 3 (1.1 Hz), objective p. 1 (Abstract), p. 1 (Abstract), p. 2 (1.1 Hz), p. 2 (1.1 Hz), p. 3 (1.1 Hz), temporal p. 7 (4 Experiment), p. 9 (4 Experiment), p. 10 (4 Experiment), p. 10 (4 Experiment), p. 1 (Abstract), p. 2 (1.1 Hz).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
