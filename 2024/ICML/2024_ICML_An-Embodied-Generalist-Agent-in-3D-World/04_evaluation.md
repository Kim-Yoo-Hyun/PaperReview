# Evaluation - An Embodied Generalist Agent in 3D World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2311.12871; PDF retrieval source: https://arxiv.org/pdf/2311.12871. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 8 (4.5. Scaling Law Analysis), p. 8 (4.5. Scaling Law Analysis), p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption)): Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in a phrasal form, used for providing ...

## Evaluation Body Digest

- **p. 4 / 3.3. LLM-assisted 3D-language Data Generation - extractive PDF cue:** Next, we manually design some examples as seed tasks (Liu et al., 2023b), including scene and object captioning, QA, dialogue, and planning, and ask LLM ...
- **p. 4 / 3. Datasets - extractive PDF cue:** The statistics and examples of these datasets can be found in Tab.
- **p. 5 / 3.3. LLM-assisted 3D-language Data Generation - extractive PDF cue:** An Embodied Generalist Agent in 3D World Dialogue(O-CoT): Dialogue Context: high level task: organize the bedroom. low level task: check some objects.
- **p. 5 / 3.3. LLM-assisted 3D-language Data Generation - extractive PDF cue:** Thought:wardrobe2, desk-7, chair-11, bed-15 Answer: bedroom Object Scene Caption: The showcase is supported by the wall and positioned behind, close to, and to the left ...
- **p. 8 / 4.5. Scaling Law Analysis - extractive PDF cue:** We study the scaling effect (Kaplan et al., 2020; Reed et al., 2022) of data and model in LEO by tracking the instruction-tuning loss on ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Quantitative comparison with state-of-the-art models on 3D VL under- standing and embodied reasoning tasks. "C" stands for "CIDEr", "B-4" for "BLEU- 4", "M" ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 2: Answer accuracy of LLM-generated data on three types of questions. Counting Existence Non-existence 3D-LLM 56.5 96.8 40.0 Ours
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 6: Results on object navigation. † indi- cates zero-shot evaluation. MP3D-val HM3D-val Success(↑) SPL(↑) Success(↑) SPL(↑) Habitat-web (shortest) 4.4

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. Datasets (p. 4); I. Additional Results (p. 31).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in ... | p. 5 (Figure/Table caption) |
| 4.5. Scaling Law Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | 2) Scaling up LLM leads to consistent improvements. | p. 8 (4.5. Scaling Law Analysis) |
| 4.5. Scaling Law Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | In contrast, despite the consistent improvements, the gap between Aligned Vicuna-7B and Vicuna-13B appears less significant, suggesting potential saturation if we continue to scale ... | p. 8 (4.5. Scaling Law Analysis) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 6: Results on object navigation. † indi- cates zero-shot evaluation. MP3D-val HM3D-val Success(↑) SPL(↑) Success(↑) SPL(↑) Habitat-web (shortest) 4.4 | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: Answer accuracy of LLM-generated data on three types of questions. Counting Existence Non-existence 3D-LLM 56.5 96.8 40.0 Ours | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 3.3. LLM-assisted 3D-language Data Generation - extractive PDF cue:** Next, we manually design some examples as seed tasks (Liu et al., 2023b), including scene and object captioning, QA, dialogue, and planning, and ask LLM ...
- **p. 4 / 3. Datasets - extractive PDF cue:** The statistics and examples of these datasets can be found in Tab.
- **p. 5 / 3.3. LLM-assisted 3D-language Data Generation - extractive PDF cue:** An Embodied Generalist Agent in 3D World Dialogue(O-CoT): Dialogue Context: high level task: organize the bedroom. low level task: check some objects.
- **p. 5 / 3.3. LLM-assisted 3D-language Data Generation - extractive PDF cue:** Thought:wardrobe2, desk-7, chair-11, bed-15 Answer: bedroom Object Scene Caption: The showcase is supported by the wall and positioned behind, close to, and to the left ...
- **p. 8 / 4.5. Scaling Law Analysis - extractive PDF cue:** We study the scaling effect (Kaplan et al., 2020; Reed et al., 2022) of data and model in LEO by tracking the instruction-tuning loss on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The proposed embodied generalist agent LEO. It takes egocentric 2D images, 3D point clouds, and texts as input and formulates comprehensive 3D tasks ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1: Datasets statistics. We illustrate key statistics of datasets for 3D VL alignment (LEO-align) and 3D VLA instruction tuning (LEO-instruct). res. (response) denotes tokens ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 2: Answer accuracy of LLM-generated data on three types of questions. Counting Existence Non-existence 3D-LLM 56.5 96.8 40.0 Ours
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 3: The amount of examined data in
- **p. 4 / Figure/Table caption - extractive PDF cue:** Tab. 2. 3D-LLM data (Hong et al., 2023) is much less since we can only access a subset. Counting Existence Non-existence 3D-LLM 434 95 10 ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Quantitative comparison with state-of-the-art models on 3D VL under- standing and embodied reasoning tasks. "C" stands for "CIDEr", "B-4" for "BLEU- 4", "M" ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 5: Results on robot manipulation. seen indicates in-domain tasks. unseen marks OOD tasks with novel colors or objects. separating-piles packing-google -objects-seq put-blocks-in -bowls seen

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Next, we manually design some examples as seed tasks (Liu et al., 2023b), including scene and object captioning, QA, dialogue, and planning, and ask ... | embodiment, simulator version and control stack | p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 4 (3. Datasets) |
| Task/environment | The statistics and examples of these datasets can be found in Tab. | reset, timeout, object/scene variation | p. 4 (3. Datasets), p. 5 (3.3. LLM-assisted 3D-language Data Generation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (2. Model), p. 4 (2.3. Training & Inference) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (4.2. Scene-grounded Dialogue and Planning), p. 3 (2.1. Tokenization) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 4: Quantitative comparison with state-of-the-art models on 3D VL under- standing and embodied reasoning tasks. "C" stands for "CIDEr", "B-4" for "BLEU- 4", ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 2: Answer accuracy of LLM-generated data on three types of questions. Counting Existence Non-existence 3D-LLM 56.5 96.8 40.0 Ours | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 6: Results on object navigation. † indi- cates zero-shot evaluation. MP3D-val HM3D-val Success(↑) SPL(↑) Success(↑) SPL(↑) Habitat-web (shortest) 4.4 | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 9: Answer accuracy (EM) on object- existence questions. Aug: augmented data. 3RScan ScanNet (0-shot) Yes No Overall Yes | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 8: TrueSkill scores with human pref- erence. Dialg: dialogue and planning data. Answerable Unanswerable NLP w/o Dialg 24.4±1.3 23.1±1.4 23.4±1.4 | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Similar to BLIP-2 (Li et al., 2023d), we train LEO to generate captions given various 3D inputs. | definition/direction/unit from same section | p. 4 (3. Datasets) |
| Aligned Vicuna-7B shows significantly lower losses than Aligned OPT-1.3B. | definition/direction/unit from same section | p. 8 (4.5. Scaling Law Analysis) |
| In addition to the default Vicuna-7B, we incorporate two LLMs at different scales: OPT-1.3B (Zhang et al., 2022) and Vicuna-13B (Chiang et al., 2023). | definition/direction/unit from same section | p. 8 (4.5. Scaling Law Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to counterparts that utilize object boxes (Yin et al., 2023; Hong et al., 2023; Wang et al., 2023e), it offers both rich object ... | comparison identity and matched condition | p. 4 (3.3. LLM-assisted 3D-language Data Generation) |
| Table 4: Quantitative comparison with state-of-the-art models on 3D VL under- standing and embodied reasoning tasks. "C" stands for "CIDEr", "B-4" for "BLEU- 4", ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 7: Quantitative results of LEO trained with differ- ent data configurations. w/o Align: without alignment stage. ScanNet: tuned on ScanNet scenes only. w/o ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Clean the floor by sweeping to remove any dirt. | component/input/data sensitivity | p. 5 (3.3. LLM-assisted 3D-language Data Generation) |
| Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 7: Quantitative results of LEO trained with differ- ent data configurations. w/o Align: without alignment stage. ScanNet: tuned on ScanNet scenes only. w/o ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Due to the space limit, we defer details including data source and components to Appendix B.1. | component/input/data sensitivity | p. 4 (3. Datasets) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present the results of CLIPort manipulation and object navigation in Tabs. | Figure 2: Our proposed LLM-assisted 3D-language data generation pipeline and data examples.. (Top-left) Messages with 3D scene graphs, including object attributes and relations in ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 8 (4.5. Scaling Law Analysis), p. 8 (4.5. Scaling Law Analysis), p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | 2) Scaling up LLM leads to consistent improvements. | numeric claim only at cited anchor | p. 8 (4.5. Scaling Law Analysis) |

- Numeric sentences retained from the body:
- **p. 7 / 4.3. Embodied Action in 3D World - extractive PDF cue:** Answerable Unanswerable NLP w/o Dialg 24.4±1.3 23.1±1.4 23.4±1.4 w/ Dialg 25.6±1.3 26.8±1.4 26.6±1.4 Table 9: Answer accuracy (EM) on objectexistence questions.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: The proposed embodied generalist agent LEO. It takes egocentric 2D images, 3D point clouds, and texts as input and formulates comprehensive 3D ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| During training, we freeze the pretrained 3D point cloud encoder and the LLM and finetune the 2D image encoder, the Spatial Transformer, and the ... | p. 3 (2.3. Training & Inference) |
| Most of the responses are text and can be decoded directly. | p. 3 (2.2. Token Embedding & LLM) |
| Details for designing the seed tasks can be found in Appendix B.3. | p. 4 (3.3. LLM-assisted 3D-language Data Generation) |
| Next, we manually design some examples as seed tasks (Liu et al., 2023b), including scene and object captioning, QA, dialogue, and planning, and ask ... | p. 4 (3.3. LLM-assisted 3D-language Data Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: The proposed embodied generalist agent LEO. It takes egocentric 2D images, 3D point clouds, and texts as input and formulates comprehensive 3D tasks ...

- **PDF anchors reviewed:** datasets p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 4 (3. Datasets), p. 5 (3.3. LLM-assisted 3D-language Data Generation), p. 5 (3.3. LLM-assisted 3D-language Data Generation), p. 8 (4.5. Scaling Law Analysis), metrics p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (3. Datasets), baselines p. 4 (3.3. LLM-assisted 3D-language Data Generation), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 5 (Figure/Table caption), p. 8 (4.5. Scaling Law Analysis), p. 8 (4.5. Scaling Law Analysis), p. 6 (Figure/Table caption), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
