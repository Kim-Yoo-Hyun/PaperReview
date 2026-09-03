# Evaluation - DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p075.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p075.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. ANALYSIS AND RI), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (B. Evaluation Tasks), p. 7 (Figure/Table caption)): In our evaluations, we seek to investigate the following key questions: 1) How effectively does DexWild leverage human data to achieve strong in-the-wild performance?

## Evaluation Body Digest

- **p. 6 / C. Evaluation Environments - extractive body cue:** We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present in ...
- **p. 6 / B. Evaluation Tasks - extractive body cue:** Finally, in Bimanual Clothes Folding, the robot uses both hands to fold a clothing item, assessing manipulation of deformable objects.
- **p. 6 / B. Evaluation Tasks - extractive body cue:** Success requires the policy to adapt to varying object properties, environmental conditions,
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Using DexWild-System, humans can effortlessly collect accurate data with their own in any robot hand to perform dexterous manipulation in a human-like way ...
- **p. 6 / V. ANALYSIS AND RI - extractive body cue:** In our evaluations, we seek to investigate the following key questions: 1) How effectively does DexWild leverage human data to achieve strong in-the-wild performance?
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: How does co-training help with scaling up in the wild performance? We evaluate our policy across three scenarios: (a) In-Domain
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Left: Cross-Task Performance - Evaluating DexWild on the Cross-Embodiment Performance ~ Testing DexWild policy on the Orig = Demonstrating improved DexWild performance as ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DexWild enables dexterous policies to generalize to new objects, scenes, and embodiments. This is achieved by leveraging large-scale, real-world human embodiment data collected ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** B. Evaluation Tasks (p. 6); C. Evaluation Environments (p. 6); 1. Cotraining Extended Results (p. 14); experiments (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. ANALYSIS AND RI | EMPIRICAL / REAL-ROBOT OR HARDWARE | In our evaluations, we seek to investigate the following key questions: 1) How effectively does DexWild leverage human data to achieve strong in-the-wild performance? | p. 6 (V. ANALYSIS AND RI) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Left: Cross-Task Performance - Evaluating DexWild on the Cross-Embodiment Performance ~ Testing DexWild policy on the Orig = Demonstrating improved DexWild performance ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: DexWild enables dexterous policies to generalize to new objects, scenes, and embodiments. This is achieved by leveraging large-scale, real-world human embodiment data ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 8: DexWild-System offers 4.6% improvement over robot data collection speed and nearly matches the human bare hands data collection speed. | p. 8 (Figure/Table caption) |
| B. Evaluation Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success requires the policy to adapt to varying object properties, environmental conditions, | p. 6 (B. Evaluation Tasks) |

## Dataset / Benchmark Role

- **p. 6 / C. Evaluation Environments - extractive body cue:** We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present in ...
- **p. 6 / B. Evaluation Tasks - extractive body cue:** Finally, in Bimanual Clothes Folding, the robot uses both hands to fold a clothing item, assessing manipulation of deformable objects.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: DexWild enables dexterous policies to generalize to new objects, scenes, and embodiments. This is achieved by leveraging large-scale, real-world human embodiment data collected ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Left: DexWild efficiently capture
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: DexWild aligns the visual observations between humans and robots to bridge the embodiment gap. This incentivizes the model to Team a task-centric rather ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Using DexWild-System, humans can effortlessly collect accurate data with their own in any robot hand to perform dexterous manipulation in a human-like way ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: We collect data using a diverse set of objects across 9 Test; Pour Task - 35 Train, 5 Test; Florist Task ~ 6 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: How does co-training help with scaling up in the wild performance? We evaluate our policy across three scenarios: (a) In-Domain
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Left: Cross-Task Performance - Evaluating DexWild on the Cross-Embodiment Performance ~ Testing DexWild policy on the Orig = Demonstrating improved DexWild performance as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: DexWild-System offers 4.6% improvement over robot data collection speed and nearly matches the human bare hands data collection speed.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present ... | embodiment, simulator version and control stack | p. 6 (C. Evaluation Environments), p. 6 (B. Evaluation Tasks) |
| Task/environment | Finally, in Bimanual Clothes Folding, the robot uses both hands to fold a clothing item, assessing manipulation of deformable objects. | reset, timeout, object/scene variation | p. 6 (B. Evaluation Tasks) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 3 (A. Data Collection System), p. 4 (A. Data Collection System) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 2 (B. Data Generation for Robot Manipulation), p. 4 (A. Data Collection System) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success requires the policy to adapt to varying object properties, environmental conditions, | definition/direction/unit from same section | p. 6 (B. Evaluation Tasks) |
| Fig. 4: Using DexWild-System, humans can effortlessly collect accurate data with their own in any robot hand to perform dexterous manipulation in a human-like ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| In our evaluations, we seek to investigate the following key questions: 1) How effectively does DexWild leverage human data to achieve strong in-the-wild performance? | definition/direction/unit from same section | p. 6 (V. ANALYSIS AND RI) |
| Fig. 6: How does co-training help with scaling up in the wild performance? We evaluate our policy across three scenarios: (a) In-Domain | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 7: Left: Cross-Task Performance - Evaluating DexWild on the Cross-Embodiment Performance ~ Testing DexWild policy on the Orig = Demonstrating improved DexWild performance ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present DexWild, a system that enables effective learning of robust dexterous manipulation policies through co-training on human and robot demonstrations. | In our evaluations, we seek to investigate the following key questions: 1) How effectively does DexWild leverage human data to achieve strong in-the-wild performance? | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. ANALYSIS AND RI), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (B. Evaluation Tasks), p. 7 (Figure/Table caption) |
| Primary metric/result | Fig. 7: Left: Cross-Task Performance - Evaluating DexWild on the Cross-Embodiment Performance ~ Testing DexWild policy on the Orig = Demonstrating improved DexWild performance ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Next, because humans typically perform these tasks successfully their demonstrations seldom include error recovery-causing trained policies to struggle to recover from unexpected failures. | p. 8 (06 06 06 _) |
| body limitation/failure cue | DexWild policies achieve a strong 68.1% average success rate, compared to just 13% for the robot ‘only baseline, Even when failures occur, DexWild policies ... | p. 7 (3) Does policy performance scale effectively with increasing) |
| body limitation/failure cue | We identify three key limitations of Gello-based collection that our system overcomes | p. 8 (06 06 06 _) |
| body limitation/failure cue | This 36-point performance drop suggests that robot-only policies overft to environment-specitic features and fail to develop robust, transferable representations. | p. 6 (3) Does policy performance scale effectively with increasing) |
| body limitation/failure cue | dlomain settings (64.7% success rate) but degrade significantly in more challenging scenarios-in-the-wild (28.5%) and inthe-wild extreme (22.0%). | p. 6 (3) Does policy performance scale effectively with increasing) |
| body limitation/failure cue | 1:5) degrades performance (54.5% in-domain, 50.9% in-thewild), indicating that robot data remains essential for grounding fine-grained control, | p. 7 (3) Does policy performance scale effectively with increasing) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Ni: Compute difision toss £p = I ~ el | p. 5 (B. Training Data Modalities and Preprocessing) |
| 1: niilize poicy x» with ViT encoder dye | p. 5 (B. Training Data Modalities and Preprocessing) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 06 06 06 _ - extractive body cue:** Next, because humans typically perform these tasks successfully their demonstrations seldom include error recovery-causing trained policies to struggle to recover from unexpected failures.
- **p. 7 / 3) Does policy performance scale effectively with increasing - extractive body cue:** DexWild policies achieve a strong 68.1% average success rate, compared to just 13% for the robot ‘only baseline, Even when failures occur, DexWild policies exhibit ...
- **p. 8 / 06 06 06 _ - extractive body cue:** We identify three key limitations of Gello-based collection that our system overcomes
- **p. 6 / 3) Does policy performance scale effectively with increasing - extractive body cue:** This 36-point performance drop suggests that robot-only policies overft to environment-specitic features and fail to develop robust, transferable representations.
- **p. 6 / 3) Does policy performance scale effectively with increasing - extractive body cue:** dlomain settings (64.7% success rate) but degrade significantly in more challenging scenarios-in-the-wild (28.5%) and inthe-wild extreme (22.0%).
- **p. 7 / 3) Does policy performance scale effectively with increasing - extractive body cue:** 1:5) degrades performance (54.5% in-domain, 50.9% in-thewild), indicating that robot data remains essential for grounding fine-grained control,

- **Evidence anchors reviewed:** datasets p. 6 (C. Evaluation Environments), p. 6 (B. Evaluation Tasks), metrics p. 6 (B. Evaluation Tasks), p. 5 (Figure/Table caption), p. 6 (V. ANALYSIS AND RI), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines 본문 anchor 없음, results p. 6 (V. ANALYSIS AND RI), p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (B. Evaluation Tasks), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We evaluate our approach across three scenarios: 1) In-Domain: Environments where robot training data was collected, testing with novel objects 2) In-the-Wild: Environments present in DexWild but absent from robot ... (p. 6, C. Evaluation Environments).
- **Metric evidence:** Success requires the policy to adapt to varying object properties, environmental conditions, (p. 6, B. Evaluation Tasks).
- **Baseline/ablation evidence:** Success requires the policy to adapt to varying object properties, environmental conditions, (p. 6, B. Evaluation Tasks).
- **Failure/negative evidence:** This avoids the fragility of SLAMLbased wrist tracking, which often fails in feature-sparse environments or during occlusion-heavy tasks (e.g., drawer opening). (p. 4, A. Data Collection System).
