# Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Evidence maturity: `ABSTRACT_CHECKED`.
> Analysis basis: official ICML proceedings page (abstract only; public PDF unavailable) checked on 2026-09-02 (1 source page(s); official ICML proceedings page (abstract only; public PDF unavailable)); canonical paper source: https://kakigo.github.io/VLA-FixBench/.
> Body source: https://icml.cc/virtual/2026/poster/64203. Reading tracker status/evidence was not changed.

> Evidence boundary: abstract/source-page only; method details, exact metrics, limitations and failure cases require full-text review.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, failure diagnosis, recovery, Benchmark, LIBERO, real robot
- Official paper: https://kakigo.github.io/VLA-FixBench/
- Full-text retrieval: https://icml.cc/virtual/2026/poster/64203
- Code/Project: https://kakigo.github.io/VLA-FixBench/
- Paper type: benchmark_or_dataset
- Source audit: official ICML proceedings page (abstract only; public PDF unavailable) checked on 2026-09-02 (1 source page(s); official ICML proceedings page (abstract only; public PDF unavailable))

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 benchmark 문제를 이해하기 위해 읽는다. 본문은 We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.를 문제로 두고, We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** While VLMs offer strong explanatory capabilities, their effectiveness in assisting VLAs is limited by their unclear role in diagnostics and inadequate collaboration mechanisms.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We further propose FaultEval, a static-to-dynamic-to-real evaluation framework that benchmarks 20 VLMs across multiple fault-related dimensions.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Building on these insights, we design a VLM-VLA collaboration mechanism that localizes spatiotemporal deviations and rolls back task execution to enable targeted recovery.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.

## Core Idea

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and apply a corrective ...

## Observation, State, and Output Interface

| Role | abstract/source-page evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on these findings, we design a robot recovery mechanism that can stop execution, roll back to an earlier safe step, and apply a corrective action. | standardized observation, action, task state와 evaluation split | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| State/latent | findings, design, robot, recovery, mechanism, stop, execution, roll, back, earlier, safe, step | benchmark state/goal와 method decision | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Output/action | Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success. | policy/controller trajectory 또는 measured result | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Objective/outcome | success metric, robustness, generalization과 reproducibility | success metric, robustness, generalization과 reproducibility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Embodiment/environment | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on real-world robots. | hardware/simulator version and reset protocol | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Dataset/benchmark | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on real-world robots. | role, split, size and leakage | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Metric | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on real-world robots. | definition, denominator, direction and uncertainty | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Baseline/ablation | not recovered | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We also build an evaluation framework to test how well different vision-language models can detect failures, locate when and where they happen, and provide useful ...

## Why Read It

World models, safety, uncertainty, and recovery의 benchmark 문제를 이해하기 위해 읽는다. 본문은 We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.를 문제로 두고, We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
