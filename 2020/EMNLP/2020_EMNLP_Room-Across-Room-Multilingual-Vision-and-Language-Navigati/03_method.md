# Method - Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://aclanthology.org/2020.emnlp-main.356/; PDF retrieval source: https://aclanthology.org/2020.emnlp-main.356.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.
- **p. 1 / 1 Introduction - extractive body cue:** We provide monolingual and multilingual baseline experiments using a variant of the Reinforced Cross-Modal Matching agent (Wang et al., 2019).
- **p. 1 / Abstract - extractive body cue:** We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended to in human ...
- **p. 2 / 1 Introduction - extractive body cue:** This especially matters for VLN, as different languages encode spatial and temporal information in idiosyncratic ways-e.g., how contact/support relationships are expressed (Munnich et al., 2001), ...
- **p. 3 / 1 Introduction - extractive body cue:** Preliminaries Movement in the simulator is based on a navigation graph.
- **p. 4 / 1 Introduction - extractive body cue:** The next selected action is indicated in red and unseen pixels in the equirectangular panoramic images are faded.
- **p. 4 / 1 Introduction - extractive body cue:** Guide Task Like R2R, our simulator has camera controls allowing continuous heading and elevation changes and movement between panoramas.
- **p. 1 / 1 Introduction - extractive body cue:** Datasets have been collected for both indoor (Anderson et al., 2018b; Thomason et al., 2019b; Qi et al., 2020) and outdoor (Chen et al., 2019; ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** We introduce Room-across-Room (RxR), a VLN dataset that addresses gaps in existing ones by (1) ∗First two.
- **p. 1 / Abstract - extractive body cue:** We introduce Room-Across-Room (RxR), a new Vision-and-Language Navigation (VLN) dataset.
- **p. 2 / 1 Introduction - extractive body cue:** In addition to verifying instruction quality, this allows us to collect a play-by-play account of how a human interpreted the instructions, represented as a pose ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.
- **p. 1 / 1 Introduction - extractive body cue:** We provide monolingual and multilingual baseline experiments using a variant of the Reinforced Cross-Modal Matching agent (Wang et al., 2019).
- **p. 1 / Abstract - extractive body cue:** We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended to in human ...
- **p. 2 / 1 Introduction - extractive body cue:** This especially matters for VLN, as different languages encode spatial and temporal information in idiosyncratic ways-e.g., how contact/support relationships are expressed (Munnich et al., 2001), ...
- **p. 3 / 1 Introduction - extractive body cue:** Preliminaries Movement in the simulator is based on a navigation graph.
- **p. 4 / 1 Introduction - extractive body cue:** The next selected action is indicated in red and unseen pixels in the equirectangular panoramic images are faded.
- **p. 4 / 1 Introduction - extractive body cue:** Guide Task Like R2R, our simulator has camera controls allowing continuous heading and elevation changes and movement between panoramas.
- **Detected method headings:** A method (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | We provide monolingual and multilingual baseline experiments using a variant of the Reinforced Cross-Modal Matching agent (Wang et al., 2019). | p. 1 (1 Introduction), p. 1 (Abstract) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We also provide results for a model that learns from synchronized pose traces by focusing only on portions of the panorama attended ... | p. 1 (Abstract), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** Datasets have been collected for both indoor (Anderson et al., 2018b; Thomason et al., 2019b; Qi et al., 2020) and outdoor (Chen et al., 2019; ...
- **p. 3 / 1 Introduction - extractive body cue:** Uniform coverage of environment viewpoints, to maximize the diversity of references to visual landmarks and objects over all paths.
- **p. 5 / 1 Introduction - extractive body cue:** The Follower tasks objectively validate the quality of Guide instructions based on whether the Follower can succeed (i.e., reaching within 3m of the last panorama ...
- **p. 1 / 1 Introduction - extractive body cue:** These VLN tasks fall in the Goldilocks zone: they can be tackled - but not solved - with current methods, and progress on them makes ...
- **p. 2 / 1 Introduction - extractive body cue:** To enable multilingual progress on VLN, RxR includes instructions for three typologically diverse languages: English (en), Hindi (hi), and Telugu (te).
- **p. 3 / 1 Introduction - extractive body cue:** P[ri] is the subgraph of P induced by room annotation ri and C returns a graph's connected components.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Guide, Follower, pose, traces, provide, dense, spatiotemporal, alignments, between, instructions, visual, percepts, actions, perspectives | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Guide, Follower, pose, traces, provide, dense, spatiotemporal, alignments, between, instructions | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | introduce, Room-across-Room, RxR, VLN, dataset, addresses, gaps, existing, ones, First | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | Datasets, have, been, collected, indoor, Anderson, Thomason, outdoor, Chen, Mehta | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.
- **p. 5 / 1 Introduction - extractive body cue:** The output of the Guide task is an audio file, a tokenized, timestamped, manually-transcribed instruction, and a pose trace (a series of timestamped 6-DOF camera ...
- **p. 6 / 29. US English instructions are the longest on av - extractive body cue:** Inputs that the Guide / Tourist have not observed cannot influence their utterances / actions, so pose traces offer rich opportunities for agent supervision.
- **p. 5 / 29. US English instructions are the longest on av - extractive body cue:** RxR also includes a far higher proportion of allocentric relations and state verification compared to R2R, and matches Touchdown (navigation instructions).
- **p. 1 / Abstract - extractive body cue:** Furthermore, each word in an instruction is time-aligned to the virtual poses of instruction creators and validators.
- **p. 2 / 1 Introduction - extractive body cue:** To enable multilingual progress on VLN, RxR includes instructions for three typologically diverse languages: English (en), Hindi (hi), and Telugu (te).
- **p. 3 / 1 Introduction - extractive body cue:** These matter both for generalization to new environments and fidelity to the descriptions given in the instruction-otherwise, strong performance might be achieved by agents that ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Grounding Supervision To incorporate spatiotemporal groundings into agent training, for each Guide path (G-path) and Follower path (F-path) we convert the corresponding ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | At each time step t, the agent receives a panoptic encoding of its viewpoint vt ∈Rk×d (where k = 36 is the ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Guide and Follower pose traces provide dense spatiotemporal alignments between instructions, visual percepts and actions - and both perspectives are useful for agent training.
- **p. 7 / 5 Experiments - extractive body cue:** All agents are trained with Adam (Kingma and Ba, 2014) to convergence (100K iterations with batch size of 32 and initial learning rate of 1e-4).
- **p. 8 / 5 Experiments - extractive body cue:** 7) is trained without data augmentation from model-generated instructions (Fried et al., 2018; Tan et al., 2019) and with hyperparameters tuned for RxR.
- **p. 6 / 3. Given correct first step then go straight - extractive body cue:** Each simple baseline requires a stopping criteria; we choose to stop after N steps where N is the average number of steps in the train ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Guide, Follower, pose, traces, provide, dense, spatiotemporal, alignments, between, instructions, visual, percepts, actions, perspectives, useful, agent, training, monolingual, multilingual, baseline.
- **Relevant PDF headings:** A method (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | Monolingual Results Table 5 provides results on the val-unseen split for several training settings, as well as human performance from Follower annotations. | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Baseline harness | 1 and 2), monolingual outperforms multilingual (exp. | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Metric / failure reporting | Applying the same approach to textual attention did not improve performance. | p. 8 (5 Experiments), p. 9 (5 Experiments) |

## Failure and Ablation Link

- **p. 8 / 5 Experiments - extractive body cue:** 7) is trained without data augmentation from model-generated instructions (Fried et al., 2018; Tan et al., 2019) and with hyperparameters tuned for RxR.
- **p. 9 / 5 Experiments - extractive body cue:** In contrast, the vision-only model has no access to the instructions, without which the paths are highly random.
- **p. 9 / 5 Experiments - extractive body cue:** This is likely because even without vision, parts of the instructions such as ‘turn left‘ and ‘go upstairs‘ still have meaning in the context of ...
- **p. 7 / 5 Experiments - extractive body cue:** (2020), we pretrain the CNN in an image-text dual encoder setting using the Conceptual Captions dataset (Sharma et al., 2018).
- **p. 7 / 5 Experiments - extractive body cue:** However, since RxR instructions are much longer than R2R, we replace the bidirectional LSTM instruction encoder with a more parallelizable CNN encoder.
- **p. 8 / 5 Experiments - extractive body cue:** Although RxR and R2R share the same underlying environments, we note that RxR →R2R cannot exploit R2R's
- **p. 8 / 5 Experiments - extractive body cue:** This is consistent with results in multilingual machine translation (MT) and automatic speech recognition (ASR) where adding more languages can also lead to degradation for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), objective p. 1 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), temporal p. 7 (5 Experiments), p. 7 (5 Experiments), p. 2 (1 Introduction), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 6 (29. US English instructions are the longest on av).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
