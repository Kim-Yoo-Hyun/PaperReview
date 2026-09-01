# Method - Training language models to follow instructions with human feedback

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (68 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.02155; PDF retrieval source: https://arxiv.org/pdf/2203.02155. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction)): We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- **p. 2 / 1 Introduction - extractive PDF cue:** We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our ...
- **p. 4 / 1 Introduction - extractive PDF cue:** To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from ...
- **p. 1 / Abstract - extractive PDF cue:** Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model ...
- **p. 3 / 1 Introduction - extractive PDF cue:** InstructGPT models generate about 25% fewer toxic outputs than GPT-3 when prompted to be respectful.
- **p. 3 / 1 Introduction - extractive PDF cue:** InstructGPT models also generate more appropriate outputs according to our labelers, and more reliably follow explicit constraints in the instruction.
- **p. 2 / 1 Introduction - extractive PDF cue:** Finally, we use this RM as a reward function and fine-tune our supervised learning baseline to maximize this reward using the PPO algorithm (Schulman et ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** See Section 3 for more details on our method. sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture.
- **p. 4 / 1 Introduction - extractive PDF cue:** The rest of this paper is structured as follows: We first detail related work in Section 2, before diving into our method and experiment details ...
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- **p. 2 / 1 Introduction - extractive PDF cue:** We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our ...
- **p. 4 / 1 Introduction - extractive PDF cue:** To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from ...
- **p. 1 / Abstract - extractive PDF cue:** Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model ...
- **p. 3 / 1 Introduction - extractive PDF cue:** InstructGPT models generate about 25% fewer toxic outputs than GPT-3 when prompted to be respectful.
- **p. 3 / 1 Introduction - extractive PDF cue:** InstructGPT models also generate more appropriate outputs according to our labelers, and more reliably follow explicit constraints in the instruction.
- **Detected method headings:** C Additional model details (p. 40); C.3 Details of the initialization models for RLHF (p. 42); C.5 FLAN and T0 models (p. 42)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Input representation | source-defined input을 learnable representation으로 바꾼다 | paper-specific image/text/sequence input | encoder, tokenization, normalization 또는 feature extraction을 수행 | latent feature/state | We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Core objective / transformation | source task의 prediction·generation 목표를 최적화한다 | representation, target/condition | paper-specific model, loss, decoder 또는 generative process를 적용 | prediction/embedding/sample | We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Downstream transfer boundary | 결과를 후속 task 또는 embodied system에 전달한다 | output와 query/task context | task head, retrieval, grounding 또는 adapter를 적용 | task cue/representation | Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); ... | p. 2 (1 Introduction), p. 4 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** Finally, we use this RM as a reward function and fine-tune our supervised learning baseline to maximize this reward using the PPO algorithm (Schulman et ...
- **p. 1 / 1 Introduction - extractive PDF cue:** This is because the language modeling objective ∗Primary authors.
- **p. 2 / 1 Introduction - extractive PDF cue:** Thus, we say that the language modeling objective is misaligned.
- **p. 3 / 1 Introduction - extractive PDF cue:** This is an example of an "alignment tax" since our alignment procedure comes at the cost of 3
- **p. 3 / 1 Introduction - extractive PDF cue:** We can minimize performance regressions on public NLP datasets by modifying our RLHF fine-tuning procedure.
- **p. 4 / 1 Introduction - extractive PDF cue:** We can greatly reduce the performance regressions on these datasets by mixing PPO updates with updates that increase the log likelihood of the pretraining distribution ...
- **Formal bridge:** source-defined input o -> prediction/embedding/sample ŷ -> paper-specific objective -> source task metric; robot link not established.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | then, collect, dataset, rankings, model, outputs, further, fine-tune, supervised, reinforcement, learning, human, feedback, Specifically | 논문이 명시한 observation과 task input | body cue; exact tensor/frame verify |
| State/latent | then, collect, dataset, rankings, model, outputs, further, fine-tune, supervised, reinforcement | task state 또는 decision variable | body cue; notation verify |
| Action/output | See, Section, more, details, sizes, parameters, models, GPT-3, architecture, rest | paper-specific output/action | body cue; unit/decoder verify |
| Objective/constraint | Finally, reward, function, fine-tune, supervised, learning, baseline, maximize, PPO, algorithm | paper-specific objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- **p. 2 / 1 Introduction - extractive PDF cue:** Specifically, we use reinforcement learning from human feedback (RLHF; Christiano et al., 2017; Stiennon et al., 2020) to fine-tune GPT-3 to follow a broad class ...
- **p. 3 / 1 Introduction - extractive PDF cue:** InstructGPT models also generate more appropriate outputs according to our labelers, and more reliably follow explicit constraints in the instruction.
- **p. 3 / 1 Introduction - extractive PDF cue:** On "closed-domain" tasks from our API prompt distribution, where the output should not contain information that is not present in the input (e.g. summarization and ...
- **p. 1 / Abstract - extractive PDF cue:** For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user.
- **p. 4 / 1 Introduction - extractive PDF cue:** These datasets consist of a variety of NLP tasks, combined with natural language instructions for each task.
- **p. 4 / 1 Introduction - extractive PDF cue:** We qualitatively probe InstructGPT's capabilities, and find that it is able to follow instructions for summarizing code, answer questions about code, and sometimes follows instructions ...
- **Normalized interface:** observation=논문이 명시한 observation과 task input; state=task state 또는 decision variable; output/action=paper-specific output/action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | More practically, for the purpose of our language tasks, we use a framework similar to Askell et al. | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | In Step 2, boxes A-D are samples from our models that get ranked by labelers. | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive PDF cue:** We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.
- **p. 2 / 1 Introduction - extractive PDF cue:** We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our ...
- **p. 4 / 1 Introduction - extractive PDF cue:** To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from ...
- **p. 1 / Abstract - extractive PDF cue:** Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model ...
- **p. 3 / 1 Introduction - extractive PDF cue:** InstructGPT models also generate more appropriate outputs according to our labelers, and more reliably follow explicit constraints in the instruction.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** then, collect, dataset, rankings, model, outputs, further, fine-tune, supervised, reinforcement, learning, human, feedback, mainly, evaluate, models, having, labelers, rate, quality.
- **Relevant PDF headings:** C Additional model details (p. 40); C.3 Details of the initialization models for RLHF (p. 42); C.5 FLAN and T0 models (p. 42).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Input representation | Second, it can be difficult for public NLP datasets to obtain a very high diversity of inputs (at least, on the kinds ... | p. 13 (4 Results), p. 12 (4 Results) |
| Core objective / transformation | Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred ... | p. 2 (Figure/Table caption), p. 12 (4 Results) |
| Downstream transfer boundary | When evaluated only on prompts that were not adversarially selected against GPT-3, our PPO models are still significantly more truthful and informative ... | p. 13 (4 Results), p. 12 (4 Results) |

## Failure and Ablation Link

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from ...
- **p. 58 / Figure/Table caption - extractive PDF cue:** Figure 38: Human evaluation metrics as a function of learning rates. E.9 Learning rate optimization for PPO models For both 1.3B and 6B models, we ...
- **p. 14 / 4 Results - extractive PDF cue:** This advantage disappears when the respectful prompt is removed ("no prompt").
- **p. 14 / 4 Results - extractive PDF cue:** A total of 1,729 prompts were labeled for three different 175B models, both with and without "respectful" instructions.
- **p. 63 / Figure/Table caption - extractive PDF cue:** Figure 43: Model samples on a prompt cherry-picked to show instruction following behavior in other languages, along with random samples from the GPT-3 175B and ...
- **p. 15 / 4 Results - extractive PDF cue:** In Figure 29 we show that adding pretraining updates to our PPO fine-tuning (PPO-ptx) mitigates these performance regressions on all datasets, and even surpasses GPT-3 ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 8: Examples of generalization in the 175B PPO-ptx model (InstructGPT 175B) compared to GPT-3 175B with no additional prefixing. Prompts are cherry-picked to illustrate ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), objective p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), temporal p. 10 (3.6 Evaluation), p. 3 (1 Introduction), p. 6 (2 Related work), p. 6 (2 Related work), p. 9 (3.2 Dataset), p. 11 (4 Results).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
