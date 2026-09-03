# Method - RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (60 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.11706; PDF retrieval source: https://arxiv.org/pdf/2306.11706. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction)): Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a large set of dexterous tasks ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a ...
- **p. 4 / 1 Introduction - extractive body cue:** The VQ-GAN, similarly to a VQ-VAE (van den Oord et al., 2017), consists of an encoder that encodes an input image into a series of ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically in robotics, recent works (Brohan et al., 2022; Driess et al., 2023) have focused on bridging the gap between large pretrained language models and ...
- **p. 5 / 1 Introduction - extractive body cue:** Combining the action and observation prediction losses, at the token level, we obtain the following objective to train the model Pθ: L(θ; D) =Eˆτ∼ˆ D ...
- **p. 5 / 1 Introduction - extractive body cue:** (3) Note that, in practice, instead of conditioning on the full history of observations (as indicated by the subscript < t), we use a fixed ...
- **p. 4 / 1 Introduction - extractive body cue:** 2.1.1 Architecture and pretraining Our model is based on the transformer architecture described in Gato (Reed et al., 2022).
- **p. 6 / 1 Introduction - extractive body cue:** In each episode, we then pick a policy from this pool to be run next and record its trajectory and success.
- **p. 1 / 1 Introduction - extractive body cue:** This is because, even though the cost of task design and robot experience generation is very high, leveraging heterogeneous robot data at scale has remained ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a ...
- **p. 2 / 1 Introduction - extractive body cue:** We introduce the embodiments, tasks, and object sets that we have used in this work in Section 3.
- **p. 3 / 1 Introduction - extractive body cue:** We describe our experimental setup for both training and evaluation in Section 4, before we present our extensive experiments to support our claims in Section ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a ...
- **p. 4 / 1 Introduction - extractive body cue:** The VQ-GAN, similarly to a VQ-VAE (van den Oord et al., 2017), consists of an encoder that encodes an input image into a series of ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically in robotics, recent works (Brohan et al., 2022; Driess et al., 2023) have focused on bridging the gap between large pretrained language models and ...
- **p. 5 / 1 Introduction - extractive body cue:** Combining the action and observation prediction losses, at the token level, we obtain the following objective to train the model Pθ: L(θ; D) =Eˆτ∼ˆ D ...
- **p. 5 / 1 Introduction - extractive body cue:** (3) Note that, in practice, instead of conditioning on the full history of observations (as indicated by the subscript < t), we use a fixed ...
- **p. 4 / 1 Introduction - extractive body cue:** 2.1.1 Architecture and pretraining Our model is based on the transformer architecture described in Gato (Reed et al., 2022).
- **p. 6 / 1 Introduction - extractive body cue:** In each episode, we then pick a policy from this pool to be run next and record its trajectory and success.
- **Detected method headings:** A Model Card (p. 31)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model ... | p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | The VQ-GAN, similarly to a VQ-VAE (van den Oord et al., 2017), consists of an encoder that encodes an input image into ... | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Specifically in robotics, recent works (Brohan et al., 2022; Driess et al., 2023) have focused on bridging the gap between large pretrained ... | p. 2 (1 Introduction), p. 5 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 1 Introduction - extractive body cue:** Combining the action and observation prediction losses, at the token level, we obtain the following objective to train the model Pθ: L(θ; D) =Eˆτ∼ˆ D ...
- **p. 1 / 1 Introduction - extractive body cue:** This is because, even though the cost of task design and robot experience generation is very high, leveraging heterogeneous robot data at scale has remained ...
- **p. 2 / 1 Introduction - extractive body cue:** This significantly reduces the cost of acquiring new skills and onboarding new embodiments.
- **p. 4 / 1 Introduction - extractive body cue:** That is, for any successful episode τ i, we can select the last image of a different episode that succeeded at the same task, gi ...
- **p. 5 / 1 Introduction - extractive body cue:** For this purpose, we employ learned reward models as described in the next section.
- **p. 6 / 1 Introduction - extractive body cue:** To this end, we train vision-based reward models to detect when a task has succeeded.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | agent, handles, variations, natively, without, requiring, common, action, observation, representations, leveraging, transformer, ability, input | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | agent, handles, variations, natively, without, requiring, common, action, observation, representations | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | main, contributions, outlined, below, demonstrate, first, time, large, transformer, sequence | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Combining, action, observation, prediction, losses, token, level, obtain, following, objective | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Our agent handles these variations natively without requiring common action or observation representations, by leveraging the transformer's ability to input and output variable-length sequences based ...
- **p. 3 / 1 Introduction - extractive body cue:** Our goal-conditioned agent is represented by a policy π(at/ot, gt), where at denotes the action vector, ot = (xt, It) are the proprioceptive observation (e.g. ...
- **p. 4 / 1 Introduction - extractive body cue:** Concretely, a tokenised trajectory ˆτ ∈ˆD is represented as ˆτ =  x1:L 1 , I1:M 1 , g1:N 1 , a1:Q 1 , ..., ...
- **p. 6 / 1 Introduction - extractive body cue:** A policy pool is simply a collection of policies (or policies implicitly defined by a pool of goal images) with overlapping start and end states.
- **p. 2 / 1 Introduction - extractive body cue:** As a step towards this goal, we trained RoboCat on a very large dataset of diverse manipulation behaviours: precise and dexterous vision-based tasks, performed with ...
- **p. 4 / 1 Introduction - extractive body cue:** Note that the dimensionality of the actions and proprioception observations vary across embodiments.
- **p. 7 / 1 Introduction - extractive body cue:** The proprioception observations for Panda and Sawyer have different dimensionalities, and even for the common 7-DoF case, the physical and kinematic characteristics between the embodiments ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | (3) Note that, in practice, instead of conditioning on the full history of observations (as indicated by the subscript < t), we ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | These episodes are annotated via a crowd-sourcing interface, where annotators mark the time step after which the task is solved in each ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | (3) Note that, in practice, instead of conditioning on the full history of observations (as indicated by the subscript < t), we ... | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | To address this in a systematic and reproducible way, we employ the following evaluation protocol for each task: we first evaluate the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions in this work are outlined below: (1) we demonstrate, for the first time, that a large transformer sequence model can solve a ...
- **p. 4 / 1 Introduction - extractive body cue:** The VQ-GAN, similarly to a VQ-VAE (van den Oord et al., 2017), consists of an encoder that encodes an input image into a series of ...
- **p. 2 / 1 Introduction - extractive body cue:** Specifically in robotics, recent works (Brohan et al., 2022; Driess et al., 2023) have focused on bridging the gap between large pretrained language models and ...
- **p. 5 / 1 Introduction - extractive body cue:** Combining the action and observation prediction losses, at the token level, we obtain the following objective to train the model Pθ: L(θ; D) =Eˆτ∼ˆ D ...
- **p. 4 / 1 Introduction - extractive body cue:** 2.1.1 Architecture and pretraining Our model is based on the transformer architecture described in Gato (Reed et al., 2022).
- **p. 11 / 4.3 Evaluation - extractive body cue:** When fine-tuning a generalist to a specific real-world task, it can be difficult to determine the optimal number of fine-tuning steps, since there is no ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, outlined, below, demonstrate, first, time, large, transformer, sequence, model, solve, dexterous, tasks, multiple, real, robotic, embodiments, differing, observation.
- **Relevant PDF headings:** A Model Card (p. 31).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | All three methods were evaluated on the same Sawyer robots with identical conditions, evaluation protocol, and successful episodes visually counted. this is ... | p. 13 (5 Experiments), p. 15 (5 Experiments) |
| Coverage / augmentation | Figure 5: RoboCat compared to VFM baselines on training tasks. RoboCat performs better on the vast majority of training tasks, compared to ... | p. 12 (Figure/Table caption), p. 13 (Figure/Table caption) |
| Downstream learning interface | The results in Figure 10 show that the self-improved agent outperforms the baseline agent in all four of these tasks. | p. 17 (5 Experiments), p. 13 (5 Experiments) |

## Failure and Ablation Link

- **p. 15 / Figure/Table caption - extractive body cue:** Table 3: RoboCat-lim fine-tuning using different sources of data. Despite RoboCat-lim only being trained on agent data originally, the model can be fine-tuned with either ...
- **p. 14 / 5 Experiments - extractive body cue:** RoboCat-lim can be effectively fine-tuned, given a limited number of demonstrations, to tasks that are novel in terms of objects or task variants, and even ...
- **p. 15 / 5 Experiments - extractive body cue:** However, the model is effective at fine-tuning to this task variant with as little as 100 demonstrations.
- **p. 11 / 4.3 Evaluation - extractive body cue:** For each comparison, the VFM models are trained with the same behavioural cloning loss and the same successful episodes that the RoboCat model uses for ...
- **p. 16 / 5 Experiments - extractive body cue:** The results here are for single task variants, unlike the results in Figure 7(c).
- **p. 16 / 5 Experiments - extractive body cue:** The reported numbers are averages of task variants within each grouping. tasks, e.g. as RoboCat was trained on real-world fruit and vegetable lifting data, it ...
- **p. 18 / 5 Experiments - extractive body cue:** 5.4 Further ablations We report a number of additional ablations and evaluations in the appendix.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 4 (1 Introduction), objective p. 5 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), temporal p. 5 (1 Introduction), p. 6 (1 Introduction), p. 11 (4.3 Evaluation), p. 11 (4.3 Evaluation), p. 2 (1 Introduction), p. 4 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
