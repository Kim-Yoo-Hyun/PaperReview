# Evaluation - SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (41 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=EyOtIOmMUh; PDF retrieval source: https://arxiv.org/pdf/2512.10046. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Abstract)): After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics.

## Evaluation Body Digest

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike existing robot navigation benchmarks, we evaluate multiple robot capacities necessary for real-world urban navigation jointly, including robust 3D visual perception, grounding multimodal instructions to ...
- **p. 3 / 1 Introduction - extractive body cue:** To address this gap, we introduce SimWorld-20K, a large-scale dataset for benchmarking multimodal robot navigation in photo-realistic urban environments.
- **p. 2 / 1 Introduction - extractive body cue:** Compared to indoor scenarios, robotics in outdoor environments, in particular, large urban environments, introduces additional challenges, such as (1) 3D perception, spatial reasoning and grounding ...
- **p. 1 / Abstract - extractive body cue:** With these key features, we build two challenging robot benchmarks: (1) a multimodal instruction-following task, where a robot must follow vision-language navigation instructions to reach ...
- **p. 1 / Abstract - extractive body cue:** Unlike existing benchmarks, these two new benchmarks comprehensively evaluate a wide range of critical robot capacities in realistic scenarios, including (1) multimodal instructions grounding, (2) ...
- **p. 3 / 1 Introduction - extractive body cue:** After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics.
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 16: Qualitative result key-step VLM outputs from the finetuned model successfully completing the task However, finetuning also exhibits certain limitations. First, when the target ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4.2 Results (p. 8); 5.2 Results (p. 10); B Benchmark Comparison (p. 20); B.1 Comparing SimWorld-MMNav with Prior Vision-Language Navigation Benchmarks (p. 20); C.6 More Quantitative Results (p. 27); 4. Experimental result reproducibility (p. 37); 7. Experiment statistical significance (p. 38); 8. Experiments compute resources (p. 39).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics. | p. 3 (1 Introduction) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks. | p. 3 (1 Introduction) |
| 1 Introduction | EMPIRICAL / REAL-ROBOT OR HARDWARE | More recent city simulators, such as MetaDrive [29], MetaUrban [56], significantly improve the scalability. | p. 2 (1 Introduction) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2: Experimental results on the SIMWORLD-MMNAV benchmark (easy task set). The numbers in parentheses indicate the improvement after finetuning. Models SR%↑ Subtask SR% ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 3 / 1 Introduction - extractive body cue:** In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic urban ...
- **p. 2 / 1 Introduction - extractive body cue:** Unlike existing robot navigation benchmarks, we evaluate multiple robot capacities necessary for real-world urban navigation jointly, including robust 3D visual perception, grounding multimodal instructions to ...
- **p. 3 / 1 Introduction - extractive body cue:** To address this gap, we introduce SimWorld-20K, a large-scale dataset for benchmarking multimodal robot navigation in photo-realistic urban environments.
- **p. 2 / 1 Introduction - extractive body cue:** Compared to indoor scenarios, robotics in outdoor environments, in particular, large urban environments, introduces additional challenges, such as (1) 3D perception, spatial reasoning and grounding ...
- **p. 1 / Abstract - extractive body cue:** With these key features, we build two challenging robot benchmarks: (1) a multimodal instruction-following task, where a robot must follow vision-language navigation instructions to reach ...
- **p. 1 / Abstract - extractive body cue:** Unlike existing benchmarks, these two new benchmarks comprehensively evaluate a wide range of critical robot capacities in realistic scenarios, including (1) multimodal instructions grounding, (2) ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of SimWorld Robotics (SWR). Built upon Unreal Engine 5, SWR is a simulation platform for large-scale, photorealistic, and dynamic urban environments. It ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Simulator Comparison Top: Our simulator demonstrates key features including dynamic lighting (e.g., sunrise), realistic weather (e.g., rain), diverse high-fidelity buildings, and rich pedestrian ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison of outdoor simulation platforms across key features. The Scenes section includessupport for Procedural Generation (✓: supported, ×: not supported), and level of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Procedural City Generation. SWR receives a user's specification and modularizes the process into road, building, details, and traffic elements generation. network through a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Illustration of a multimodal robot navigation task. Action Space. SWR supports three types of continuous vehicle control: acceleration, braking, and steering. Each action ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Experimental results on the SIMWORLD-MMNAV benchmark (easy task set). The numbers in parentheses indicate the improvement after finetuning. Models SR%↑ Subtask SR% ↑ ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Experimental results on the SIMWORLD-MMNAV benchmark (hard task set). Models SR%↑Stat. Coll. ↓Dyn. Coll.↓Red Light Viol.↓Subtask SR%↑Distance Progress%↑ GPT-4o 2.08 1.92 10.37 3.02
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Most common failure modes in SIMWORLD-MMNAV. Subtask Failure Mode Frequency (%) Moving to Intersection Misestimate the distance to the intersection 53.33 Fail to ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic ... | embodiment, simulator version and control stack | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Task/environment | Unlike existing robot navigation benchmarks, we evaluate multiple robot capacities necessary for real-world urban navigation jointly, including robust 3D visual perception, grounding multimodal instructions ... | reset, timeout, object/scene variation | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 1 (Abstract) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics. | definition/direction/unit from same section | p. 3 (1 Introduction) |
| Figure 16: Qualitative result key-step VLM outputs from the finetuned model successfully completing the task However, finetuning also exhibits certain limitations. First, when the ... | definition/direction/unit from same section | p. 34 (Figure/Table caption) |
| Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks. | definition/direction/unit from same section | p. 3 (1 Introduction) |
| Figure 3: Procedural City Generation. SWR receives a user's specification and modularizes the process into road, building, details, and traffic elements generation. network through ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 12: Experimental results on the SimWorld-MMNav benchmark (easy task set) with confidence intervals Models SR%↑ Subtask SR% ↑ Distance Progress% ↑ Proprietary Models ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| Figure 13: Qualitative result - lack of distance grounding Spatial Reasoning The VLM exhibits limitations in reasoning about spatial relationships, particularly in estimating distance, ... | definition/direction/unit from same section | p. 32 (Figure/Table caption) |
| Our experimental results demonstrate that stateof-the-art models, including vision-language models (VLMs), struggle with our tasks, lacking robust perception, reasoning, and planning abilities necessary for ... | definition/direction/unit from same section | p. 1 (Abstract) |
| Training these models requires a large amount of data, much of which can be generated in high-fidelity embodied simulators, such as Habitat 3 [40], ... | definition/direction/unit from same section | p. 1 (1 Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 11: Example communication for ROCO baseline Baseline 2 - ROCO The ROCO-based [33] setting extends the oracle setup by introducing collaborative planning and ... | comparison identity and matched condition | p. 30 (Figure/Table caption) |
| After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics. | comparison identity and matched condition | p. 3 (1 Introduction) |
| Compared to indoor scenarios, robotics in outdoor environments, in particular, large urban environments, introduces additional challenges, such as (1) 3D perception, spatial reasoning and ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| Figure 1: Overview of SimWorld Robotics (SWR). Built upon Unreal Engine 5, SWR is a simulation platform for large-scale, photorealistic, and dynamic urban environments. ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks. | comparison identity and matched condition | p. 3 (1 Introduction) |
| Table 1: Comparison of outdoor simulation platforms across key features. The Scenes section includessupport for Procedural Generation (✓: supported, ×: not supported), and level ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 11: Ablation study with key components. Configuration Explicit Reason Separate Perceive/Act Depth Segment | component/input/data sensitivity | p. 27 (Figure/Table caption) |
| After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics. | component/input/data sensitivity | p. 3 (1 Introduction) |
| Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In sum, our key contributions include: (1) a new embodied AI simulator, SimWorld-Robotics (SWR), that supports the creation and simulation of photorealistic and dynamic ... | After fine-tuning on SimWorld-20K, QwenVL2.5-7B achieves a non-zero success rate on the test set and outperforms SOTA proprietary models across several key metrics. | PDF body cue; verify exact table/figure and matched conditions | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Abstract) |
| Primary metric/result | Our experimental results demonstrate that existing models, including state-of-the-art vision-language models (VLMs), fail to achieve meaningful success on our benchmarks. | numeric claim only at cited anchor | p. 3 (1 Introduction) |

- Numeric sentences retained from the body:
- **p. 3 / 1 Introduction - extractive body cue:** The dataset contains 20K training steps sampled from 200 episodes, each averaging 500 m in length, across 100 procedurally generated city environments with an average ...
- **p. 3 / 1 Introduction - extractive body cue:** Compared to MetaUrban [56], the most recent urban simulator supporting procedural city generation, SWR offers environments that are 100× larger in area and episodes that ...
- **p. 3 / 1 Introduction - extractive body cue:** The dataset contains 20K training steps sampled from 200 episodes, each averaging 500 m in length, across 100 procedurally generated city environments with an average ...
- **p. 3 / 1 Introduction - extractive body cue:** Compared to MetaUrban [56], the most recent urban simulator supporting procedural city generation, SWR offers environments that are 100× larger in area and episodes that ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 13: Qualitative result - lack of distance grounding Spatial Reasoning The VLM exhibits limitations in reasoning about spatial relationships, particularly in estimating distance, ... | p. 32 (Figure/Table caption) |
| body limitation/failure cue | Figure 15: Qualitative result - lack of perspective-adaptive matching These limitations also manifest when matching buildings from different perspectives. The target building is provided ... | p. 33 (Figure/Table caption) |
| body limitation/failure cue | Table 4: Most common failure modes in SIMWORLD-MMNAV. Subtask Failure Mode Frequency (%) Moving to Intersection Misestimate the distance to the intersection 53.33 Fail ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 14: Qualitative result - lack of embodied reasoning Given a working memory, an embodied agent would robustly infer that it has aligned accordingly. ... | p. 33 (Figure/Table caption) |
| body limitation/failure cue | Figure 16: Qualitative result key-step VLM outputs from the finetuned model successfully completing the task However, finetuning also exhibits certain limitations. First, when the ... | p. 34 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The dataset contains 20K training steps sampled from 200 episodes, each averaging 500 m in length, across 100 procedurally generated city environments with an ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 32 / Figure/Table caption - extractive body cue:** Figure 13: Qualitative result - lack of distance grounding Spatial Reasoning The VLM exhibits limitations in reasoning about spatial relationships, particularly in estimating distance, maintaining ...
- **p. 33 / Figure/Table caption - extractive body cue:** Figure 15: Qualitative result - lack of perspective-adaptive matching These limitations also manifest when matching buildings from different perspectives. The target building is provided as ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Most common failure modes in SIMWORLD-MMNAV. Subtask Failure Mode Frequency (%) Moving to Intersection Misestimate the distance to the intersection 53.33 Fail to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of a multi-robot search task. Hard Setting. We further evaluated realistic obstacle avoidance and traffic rule obedience on models that performed relatively ...
- **p. 33 / Figure/Table caption - extractive body cue:** Figure 14: Qualitative result - lack of embodied reasoning Given a working memory, an embodied agent would robustly infer that it has aligned accordingly. However, ...
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 16: Qualitative result key-step VLM outputs from the finetuned model successfully completing the task However, finetuning also exhibits certain limitations. First, when the target ...

- **Evidence anchors reviewed:** datasets p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract), metrics p. 3 (1 Introduction), p. 34 (Figure/Table caption), p. 3 (1 Introduction), p. 5 (Figure/Table caption), p. 28 (Figure/Table caption), p. 32 (Figure/Table caption), baselines p. 30 (Figure/Table caption), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (Figure/Table caption), p. 3 (1 Introduction), p. 4 (Figure/Table caption), results p. 3 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Abstract).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
