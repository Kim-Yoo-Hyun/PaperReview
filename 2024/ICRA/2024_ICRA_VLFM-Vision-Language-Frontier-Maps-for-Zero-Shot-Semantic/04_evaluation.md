# Evaluation - VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2312.03275; PDF retrieval source: https://arxiv.org/pdf/2312.03275. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption)): For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31].

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world environments; Gibson [6], ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** HM3D's validation split contains 2000 episodes across 20 scenes and 6 object categories.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31].
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** SPL scores the efficiency of an agent's path by comparing it to the length of the shortest path from the start position to the closest ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Left: Visualization of how the confidence score of a pixel within the robot's FOV is determined based on its location relative to the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: VLFM iteratively constructs value maps for target-driven navigation by using BLIP-2 to compute the cosine similarity between a text prompt incorporating the target ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. It ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: VLFM constructs an occupancy map of the scene identifying frontiers of explored space as well as a value map of the likelihood of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTAL SETUP (p. 5); VI. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31]. | p. 5 (V. EXPERIMENTAL SETUP) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. ... | p. 1 (Figure/Table caption) |
| V. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method outperforms previous zero-shot methods and performs competitively against methods directly trained on the Object Navigation task. | p. 5 (V. EXPERIMENTAL SETUP) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 3: Left: Visualization of how the confidence score of a pixel within the robot's FOV is determined based on its location relative to ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 4: VLFM iteratively constructs value maps for target-driven navigation by using BLIP-2 to compute the cosine similarity between a text prompt incorporating the ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world environments; Gibson [6], ...
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** HM3D's validation split contains 2000 episodes across 20 scenes and 6 object categories.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. It ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: VLFM constructs an occupancy map of the scene identifying frontiers of explored space as well as a value map of the likelihood of ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Left: Visualization of how the confidence score of a pixel within the robot's FOV is determined based on its location relative to the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: VLFM iteratively constructs value maps for target-driven navigation by using BLIP-2 to compute the cosine similarity between a text prompt incorporating the target ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world environments; Gibson ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP) |
| Task/environment | HM3D's validation split contains 2000 episodes across 20 scenes and 6 object categories. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTAL SETUP) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 2 (III. PROBLEM FORMULATION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31]. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL SETUP) |
| SPL scores the efficiency of an agent's path by comparing it to the length of the shortest path from the start position to the ... | definition/direction/unit from same section | p. 5 (V. EXPERIMENTAL SETUP) |
| Fig. 3: Left: Visualization of how the confidence score of a pixel within the robot's FOV is determined based on its location relative to ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 4: VLFM iteratively constructs value maps for target-driven navigation by using BLIP-2 to compute the cosine similarity between a text prompt incorporating the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: VLFM constructs an occupancy map of the scene identifying frontiers of explored space as well as a value map of the likelihood ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate VLFM by comparing it to several state-of-the-art (SOTA) techniques for zero-shot object navigation: CLIP on Wheels (CoW) [1], ESC [2], SemUtil [3], ... | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL SETUP) |
| Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Our method outperforms previous zero-shot methods and performs competitively against methods directly trained on the Object Navigation task. | comparison identity and matched condition | p. 5 (V. EXPERIMENTAL SETUP) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Approach Semantic Nav Gibson HM3D MP3D Training SPL↑SR↑SPL↑SR↑SPL↑SR↑ PONI [19] ObjectNav 41.0 73.6 - - 12.1 31.8 PIRLNav [15] ObjectNav - - 27.1 64.1 ... | component/input/data sensitivity | p. 5 (V. EXPERIMENTAL SETUP) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we propose Vision-Language Frontier Maps (VLFM), a zero-shot approach for target-driven semantic navigation to an unseen object in a novel environment. | For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31]. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Fig. 1: VLFM achieves state-of-the-art semantic Object Goal Navigation performance in unfamiliar environments, without task-specific training, pre-built maps, or prior knowledge of the surroundings. ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** We use the ObjectNav validation split for Gibson developed in SemExp [16] which contains 1000 episodes across 5 scenes.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** HM3D's validation split contains 2000 episodes across 20 scenes and 6 object categories.
- **p. 5 / V. EXPERIMENTAL SETUP - extractive body cue:** MP3D's validation split contains 2195 episodes across 11 scenes and 21 object categories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | VLFM has a number of limitations that could be addressed by future work. | p. 6 (VII. CONCLUSION) |
| body limitation/failure cue | So, we cannot leverage this map in sequentially executed semantic navigation tasks to different objects or in executing other navigation tasks requiring targets specified ... | p. 6 (VII. CONCLUSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| An episode is defined as successfully completed if STOP is called within 1 m of any instance of the target object in 500 or ... | p. 2 (III. PROBLEM FORMULATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VII. CONCLUSION - extractive body cue:** VLFM has a number of limitations that could be addressed by future work.
- **p. 6 / VII. CONCLUSION - extractive body cue:** So, we cannot leverage this map in sequentially executed semantic navigation tasks to different objects or in executing other navigation tasks requiring targets specified by ...

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), metrics p. 5 (V. EXPERIMENTAL SETUP), p. 5 (V. EXPERIMENTAL SETUP), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), results p. 5 (V. EXPERIMENTAL SETUP), p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTAL SETUP), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We evaluate our approach using the Habitat [5] simulator on the validation splits of three different datasets of 3D scans of real-world environments; Gibson [6], HM3D [8], and MP3D [7]. (p. 5, V. EXPERIMENTAL SETUP).
- **Metric evidence:** For all approaches, we report success rate (SR) and Success weighted by inverse Path Length (SPL) [31]. (p. 5, V. EXPERIMENTAL SETUP).
- **Baseline/ablation evidence:** Our method outperforms previous zero-shot methods and performs competitively against methods directly trained on the Object Navigation task. (p. 5, V. EXPERIMENTAL SETUP).
- **Failure/negative evidence:** VLFM has a number of limitations that could be addressed by future work. (p. 6, VII. CONCLUSION).
