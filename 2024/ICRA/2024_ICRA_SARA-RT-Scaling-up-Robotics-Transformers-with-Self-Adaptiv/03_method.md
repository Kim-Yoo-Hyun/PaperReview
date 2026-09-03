# Method - SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.01990; PDF retrieval source: https://arxiv.org/pdf/2312.01990. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 1 (Abstract), p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA)): It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterpart ...

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterpart ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models [1], the first VLA robotic policies pre-trained on ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We consider a purely zero-shot attention-based control mechanism, where the action ai of the agent corresponding to the particular target ti (i = 1, ..., ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** Learnable preprocessing corresponds here to fine-tuning matrices WQ and WK ([3]) from Transformers' attention modules, but in the linear attention context.
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We thus propose the process of the self-adaptation of their attention modules, that we refer to as up-training, which can be implemented as replacing regular ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** First we show that vision-language (VL) models can be used in a zero-shot manner for steering the agent.
- **p. 4 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** Then there exist v ∈Rm, G1, G2 ∈Rm×d, f : R → R such that the approximate attention matrix bA (implicitly) given by the mappings ...
- **p. 4 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** Denote by pϵ the probability of an event E(ϵ) = {∃i,j/bK(qi, kj) -K(qi, kj)/ > ϵK(qi, kj)}.

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** 2 (blue- and brown-border boxes), this modification enables both the ReLU and exp variants to reach their targets with no distractions and furthermore already leads ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** First we show that vision-language (VL) models can be used in a zero-shot manner for steering the agent.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterpart ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models [1], the first VLA robotic policies pre-trained on ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We consider a purely zero-shot attention-based control mechanism, where the action ai of the agent corresponding to the particular target ti (i = 1, ..., ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** Learnable preprocessing corresponds here to fine-tuning matrices WQ and WK ([3]) from Transformers' attention modules, but in the linear attention context.
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We thus propose the process of the self-adaptation of their attention modules, that we refer to as up-training, which can be implemented as replacing regular ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** First we show that vision-language (VL) models can be used in a zero-shot manner for steering the agent.
- **p. 4 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** Then there exist v ∈Rm, G1, G2 ∈Rm×d, f : R → R such that the approximate attention matrix bA (implicitly) given by the mappings ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their ... | p. 1 (Abstract), p. 1 (Abstract) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models [1], the first VLA robotic ... | p. 1 (Abstract), p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | We consider a purely zero-shot attention-based control mechanism, where the action ai of the agent corresponding to the particular target ti (i ... | p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** Denote by pϵ the probability of an event E(ϵ) = {∃i,j/bK(qi, kj) -K(qi, kj)/ > ϵK(qi, kj)}.
- **p. 4 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** Furthermore, by Theorem 4.2. from [28], the probability that / ϕSARA f,1 (xi)⊤ϕSARA f,2 (yj) m exp(r2) - K(qi, kj)/ > τϵ is at most ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | consider, purely, zero-shot, attention-based, control, mechanism, where, action, agent, corresponding, particular, target, defined, follows | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | consider, purely, zero-shot, attention-based, control, mechanism, where, action, agent, corresponding | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | present, Self-Adaptive, Robust, Attention, Robotics, Transformers, SARA-RT, paradigm, addressing, emerging | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Denote, probability, event, j/bK, Furthermore, Theorem, SARA, most | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We consider a purely zero-shot attention-based control mechanism, where the action ai of the agent corresponding to the particular target ti (i = 1, ..., ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** The manipulation policy is conditioned on the text instruction.
- **p. 1 / Body text (section not recovered) - extractive body cue:** 1: Robotics Transformer policies obtained via Self-Adaptive Robust Attention (SARA) in action for three different modalities: vision, language and point clouds and varying sequence lengths ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** The VL navigation is a convenient "macroscopic" case study, but our main targets are Transformer-architectures for Robotics, where queries for the whole images or text ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** This can be addressed algorithmically if K admits a bi-linearization, i.e. can be re-written as a linear (dot-product) kernel in the new input-space: K(x, y) ...
- **p. 2 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** Developing intuition: zero-shot navigation via VL models Consider a vision-based VR navigation agent, conditioned on the images of the target objects: t1, ..., tM or ...
- **p. 4 / III. THE MATHEMATICS OF SARA-RTS - extractive body cue:** That completes the proof, since for m defined in the statement of the theorem, pϵ < 1.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | The VLM takes a text instruction and an image (or a history of images) and produces a sequence of text tokens that ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | Finally, we combine SARA with the new tokenizer from IV-B.2 and the history of H = 3 frames. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | The VLM takes a text instruction and an image (or a history of images) and produces a sequence of text tokens that ... | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | Finally, we combine SARA with the new tokenizer from IV-B.2 and the history of H = 3 frames. | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterpart ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models [1], the first VLA robotic policies pre-trained on ...
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** Learnable preprocessing corresponds here to fine-tuning matrices WQ and WK ([3]) from Transformers' attention modules, but in the linear attention context.
- **p. 3 / II. SELF-ADAPTIVE ROBUST ATTENTION VIA - extractive body cue:** We thus propose the process of the self-adaptation of their attention modules, that we refer to as up-training, which can be implemented as replacing regular ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Reported are mean inference times (averaged over l = 10 random seeds) for PCT encoders (as well as the corresponding standard deviations; see: shaded regions) ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** 4: Training regular PCT policy as well as three variants of SARA with f ∈{ReLU, exp, sqrt} (up-training from the regular PCT checkpoint).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** converts, pre-trained, already, fine-tuned, Transformer-based, robotic, policies, quadratic, time, complexity, including, massive, billion-parameter, vision-language-action, models, VLAs, efficient, linear-attention, counterparts, maintaining.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | It consists of expert demonstrations collected with a mobile manipulation robot. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Coverage / augmentation | Thus we chose (here and for the RT-2 experiments) the simplest ReLU (that can be thought of as the tamed version of ... | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Downstream learning interface | It turns out that the resulting ViT-linear-attention hybrid RT-2 variant (third row in Table I) provides 12%+ mean accuracy improvement, excelling in ... | p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** For SARA variants (with f = ReLU and all-one vector v), up-training is conducted after the fine-tuning phase.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** A pass-through filter removes all points except for those of table top objects.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The adaptation process of the linear attention for the ReLU variant is highlighted.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We see almost immediate adaptation of the linear attention for all SARA variants.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Frames are encoded via SARA variants of the ViTs (sViT).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This self-attention block is yet another good candidate for injecting SARA variants.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VR navigation via VL attention models on Matterport environments ([21]). The top-down view of the scene is in the lower-left corner. The agent's ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 1 (Abstract), p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 3 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), p. 2 (II. SELF-ADAPTIVE ROBUST ATTENTION VIA), objective p. 4 (III. THE MATHEMATICS OF SARA-RTS), p. 4 (III. THE MATHEMATICS OF SARA-RTS), temporal p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
