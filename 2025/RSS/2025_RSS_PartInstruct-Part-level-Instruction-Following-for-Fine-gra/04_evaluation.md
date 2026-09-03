# Evaluation - PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p148.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p148.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (C. Dataset), p. 6 (C. Dataset), p. 1 (Figure/Table caption)): Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated ...

## Evaluation Body Digest

- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts.
- **p. 5 / C. Dataset - extractive body cue:** Each episode contains an observation set with different modslities, an expert action trajectory, a natural language description of the overall task, referred to as the ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** These benchmarks typically involve tasks such as object placement, scene arrangement, and basic interaction with objects in their entirety.
- **p. 6 / C. Dataset - extractive body cue:** For example, consider the task, "Rotate [part] of the object on the table So that it points to the opposite direction" Here, instead of explicitly ...
- **p. 5 / C. Dataset - extractive body cue:** Partinsiruct includes 10,000 demonstrations for training and over 1,800 annotated episodes for evaluation.
- **p. 6 / C. Dataset - extractive body cue:** For instance, "Push the object toward [direction] while touching [part] lift the object by holding {part}, then rotate [part] to face [direction]." Another focus is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of a ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** A. Instruction Following Benchmarks for Table-Top Robot (p. 2); C. Dataset (p. 5); B. Partinstruct Benchmark Details (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error ... | p. 7 (Figure/Table caption) |
| C. Dataset | BENCHMARK / DATASET | 11, 13, 5, 49) and (2) bi level planning that first generates high-level plans (typically subgoals), then compute and execute the low-level action plans ... | p. 6 (C. Dataset) |
| C. Dataset | BENCHMARK / DATASET | To achieve general-purpose robot manipulation, there have been two common types of approaches: (1) end-to-end policy learning that directly maps observation and instruction 10 ... | p. 6 (C. Dataset) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 1: An example fine-grained robot manipulation task in Partlnstruet, To successfully perform the task described in the instruction | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts.
- **p. 5 / C. Dataset - extractive body cue:** Each episode contains an observation set with different modslities, an expert action trajectory, a natural language description of the overall task, referred to as the ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** These benchmarks typically involve tasks such as object placement, scene arrangement, and basic interaction with objects in their entirety.
- **p. 6 / C. Dataset - extractive body cue:** For example, consider the task, "Rotate [part] of the object on the table So that it points to the opposite direction" Here, instead of explicitly ...
- **p. 5 / C. Dataset - extractive body cue:** Partinsiruct includes 10,000 demonstrations for training and over 1,800 annotated episodes for evaluation.
- **p. 6 / C. Dataset - extractive body cue:** For instance, "Push the object toward [direction] while touching [part] lift the object by holding {part}, then rotate [part] to face [direction]." Another focus is ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: An example fine-grained robot manipulation task in Partlnstruet, To successfully perform the task described in the instruction
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Example tasks and expert demonstrations in the dataset. Each task is defined by a task instruction, Each demonstration is annotated with a chain ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: PartGym supports multimodal observations, including RGB images, depth maps, and scene point clouds (PCDs), It also provides object and part annotations, including object ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Annotated parts grouped by object categories. The
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Number of object instances in each object category.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6: Representative object assets from Partlnstruct.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7: Overview of the bi-level planning framework. ‘The Hi
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. | embodiment, simulator version and control stack | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 5 (C. Dataset) |
| Task/environment | Each episode contains an observation set with different modslities, an expert action trajectory, a natural language description of the overall task, referred to as ... | reset, timeout, object/scene variation | p. 5 (C. Dataset), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 7 (1 Actions .ow-Level Action), p. 6 (A. End-to-End Policy Learning) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 7 (1 Actions .ow-Level Action), p. 8 (B. Bi-level Planning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. | definition/direction/unit from same section | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |
| For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of ... | definition/direction/unit from same section | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |
| 4) Evaluation Prorocol: As defined in Section III-C, each part-level skill has a binary success criterion, A completion of the entire task means the ... | definition/direction/unit from same section | p. 6 (C. Dataset) |
| Figure 1: An example fine-grained robot manipulation task in Partlnstruet, To successfully perform the task described in the instruction | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| For example, there are 7 types of part compositions for bottles, including "(body, closure, neck)", "(body, handle, lid, neck)", "(body, handle, mouth)", Leveraging the ... | definition/direction/unit from same section | p. 5 (C. Dataset) |
| For each base skill, we follow the template in Table X to generate skill instructions. | definition/direction/unit from same section | p. 6 (C. Dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 3) Demonstration Generation: Each demonstration is. a sequential execution of oracle high-level plans of base skills defined in Table X, To generate the trajectories ... | comparison identity and matched condition | p. 6 (C. Dataset) |
| Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. | comparison identity and matched condition | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. | component/input/data sensitivity | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |
| This yields between 3 -8 natural-language variants per template, greatly increasing the language diversity Of the dataset. | component/input/data sensitivity | p. 6 (C. Dataset) |
| For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of ... | component/input/data sensitivity | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Specifically, the bi-level planner consists of two modules: (1) a high-level task planner and (2) a low-level action policy. | Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (C. Dataset), p. 6 (C. Dataset), p. 1 (Figure/Table caption) |
| Primary metric/result | 11, 13, 5, 49) and (2) bi level planning that first generates high-level plans (typically subgoals), then compute and execute the low-level action plans ... | numeric claim only at cited anchor | p. 6 (C. Dataset) |

- Numeric sentences retained from the body:
- **p. 5 / C. Dataset - extractive body cue:** In total, there are 513 object instances and 4,653 part labels Figure 5 shows the object instance distribution across object categories.
- **p. 5 / C. Dataset - extractive body cue:** 2) Task Categories: Partinstruct has 16 task categories, including 10 seen categories for training, and 6 unseen categories for testing.
- **p. 7 / 1 Actions .ow-Level Action - extractive body cue:** Specit= ically, we select the top two checkpoints for each baseline and conduct approximately 20 rollouts per object class across all test splits, resulting in ...
- **p. 9 / B. Bi-level Planning - extractive body cue:** Fiasetines 0S Or TOC asin oso 0a Gemin-I3 Fish 20411807 Toa) 0.15 20231705 DP Gat Tad 16.57 008 God 828 Gemini20 Flash 27.73 25.94 26.75 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ... | p. 9 (V. Discussion) |
| body limitation/failure cue | While they can follow simple part-based instructions such as "grasp" or "touch? instructions Tike "touch the left part" introduce fine-grained spatial reasoning that these ... | p. 9 (V. Discussion) |
| body limitation/failure cue | For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of ... | p. 2 (A. Instruction Following Benchmarks for Table-Top Robot) |
| body limitation/failure cue | However, VLM-based planners can still fail during task planning, particularly in tasks that require a long chain of, skill instructions (e.., tasks in Test ... | p. 10 (V. Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This modified point cloud is encoded using an MLP, following the approach described in the original implementation [49]. | p. 8 (B. Bi-level Planning) |
| 11, 13, 5, 49) and (2) bi level planning that first generates high-level plans (typically subgoals), then compute and execute the low-level action plans ... | p. 6 (C. Dataset) |
| Specifically, We use a pre-trained TS language encoder to get the language ‘embedding [31]. | p. 7 (1 Actions .ow-Level Action) |
| updates the skill instruction once every n steps, while the low-level action policy updates the action at every step. | p. 7 (1 Actions .ow-Level Action) |
| CaP leverages an LLM to compose API calls to generate robot policy code. | p. 8 (B. Bi-level Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / V. Discussion - extractive body cue:** Our experimental results demonstrate that the part-level instruction following tasks in our Partinstruct benchmark remains extremely difficult for state-of-the-art end-to-end vision-language policy learning ‘methods. ‘There ...
- **p. 9 / V. Discussion - extractive body cue:** While they can follow simple part-based instructions such as "grasp" or "touch? instructions Tike "touch the left part" introduce fine-grained spatial reasoning that these models ...
- **p. 2 / A. Instruction Following Benchmarks for Table-Top Robot - extractive body cue:** For instance, CALVIN incorporates spatial semantics but lacks explicit partlevel semantics, treating components like a "door handle as standalone objects rather than parts of a ...
- **p. 10 / V. Discussion - extractive body cue:** However, VLM-based planners can still fail during task planning, particularly in tasks that require a long chain of, skill instructions (e.., tasks in Test 4).

- **Evidence anchors reviewed:** datasets p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 5 (C. Dataset), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 6 (C. Dataset), p. 5 (C. Dataset), p. 6 (C. Dataset), metrics p. 7 (Figure/Table caption), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), p. 6 (C. Dataset), p. 1 (Figure/Table caption), p. 5 (C. Dataset), baselines p. 6 (C. Dataset), p. 7 (Figure/Table caption), p. 2 (A. Instruction Following Benchmarks for Table-Top Robot), results p. 7 (Figure/Table caption), p. 6 (C. Dataset), p. 6 (C. Dataset), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 8: Success Rates of all baselines. The left group represents end-to-end learning policies, while the right group corresponds to bi-level planning models. Error bars denote the standard errors calculated ... (p. 7, Figure/Table caption).
- **Metric evidence:** Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. (p. 2, A. Instruction Following Benchmarks for Table-Top Robot).
- **Baseline/ablation evidence:** Early benchmarks in robot manipulation primarily concentrated on object-level and object-scene interactions without delving into the manipulation of specific object parts. (p. 2, A. Instruction Following Benchmarks for Table-Top Robot).
- **Failure/negative evidence:** The Failure Cause was calculated by dividing the number of times a skill chain failed because of a specific skill or part by the total number of skill chain failures. (p. 21, C. Skill and Object Part Impact Study).
