# Clio: Real-time Task-Driven Open-Set 3D Scene Graphs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2404.13696.
> PDF retrieval source: https://arxiv.org/pdf/2404.13696. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RA-L
- Authors: Dominic Maggio, Yun Chang, Nathan Hughes, Matthew Trang, Dan Griffith, Carlyn Dougherty, Eric Cristofalo, Lukas Schmid, Luca Carlone
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 3D Vision, Graph Reasoning
- Official paper: https://arxiv.org/abs/2404.13696
- Full-text retrieval: https://arxiv.org/pdf/2404.13696
- Code/Project: https://github.com/MIT-SPARK/Clio
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Clio는 자연어로 주어진 작업에 필요한 물체와 공간만 충분한 세분도로 남기는 온라인 3차원 장면 그래프를 만든다. [PDF 2쪽](https://arxiv.org/pdf/2404.13696#page=2)

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** Modern tools for class-agnostic image segmentation (e.g., SegmentAnything) and open-set semantic understanding (e.g., CLIP) provide unprecedented opportunities for robot perception and mapping.
- **p. 2 / Abstract - extractive body cue:** While traditional closed-set metricsemantic maps were restricted to tens or hundreds of semantic classes, we can now build maps with a plethora of objects and ...
- **p. 2 / Abstract - extractive body cue:** This leaves us with a fundamental question: what is the right granularity for the objects (and, more generally, for the semantic concepts) the robot has ...
- **p. 2 / Abstract - extractive body cue:** While related work implicitly chooses a level of granularity by tuning thresholds for object detection, we argue that such a choice is intrinsically task-dependent.
- **p. 2 / Abstract - extractive body cue:** The first contribution of this paper is to propose a task-driven 3D scene understanding problem, where the robot is given a list of tasks in ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** This problem can be naturally formulated using the classical Information Bottleneck (IB) [13] theory, which also provides algorithmic approaches for task-driven clustering.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.
- **p. 2 / Abstract - extractive body cue:** Our final contribution is an extensive experimental campaign showing that Clio not only allows real-time construction of compact open-set 3D scene graphs, but also improves ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our third contribution (Section V) is to include the proposed task-driven clustering algorithm into a real-time system, named Clio (Fig.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our second contribution (Section IV) is to apply the Agglomerative IB algorithm from [14] to the problem of taskdriven 3D scene understanding.
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** In this section, we first provide relevant background on the Agglomerative IB, then present an incremental version of the Agglomerative IB algorithm to support real-time ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These approaches use a class-agnostic segmentation network [10] (SegmentAnything or SAM) to generate fine-grained segments of the image and then apply a foundation model [11] ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of tasks, specified in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our key observation is that if the graph of primitives in input to the algorithm has multiple connected components (e.g., 3D object segments in different rooms), then the clustering can we performed ... | camera/depth stream, pose, map와 language goal | p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION) |
| State/latent | observation, graph, primitives, input, algorithm, multiple, connected, components, object, segments, different, rooms | robot pose, free-space/semantic map와 local goal | p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING) |
| Output/action | Our first contribution (Section III) is to state the task-driven 3D scene understanding problem, where the robot is given a list of tasks, specified in natural language, and is required to build ... | collision-free trajectory 또는 velocity command | p. 3 (I. INTRODUCTION), p. 5 (IV. TASK-DRIVEN CLUSTERING), p. 2 (Abstract) |
| Objective/outcome | As suggested in [14], at each iteration k, we also compute δ(k) = I( ˜Xk; Y ) -I( ˜Xk-1; Y ) I(X; Y ) (3) as a measure of the fractional loss ... | goal reach, safety, localization error와 replanning latency | p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 3 (I. INTRODUCTION), p. 4 (IV. TASK-DRIVEN CLUSTERING) |

## Main Claims and Actual Contribution

- 정보 병목 원리를 적용해 작업 구분에 필요한 정보를 보존하면서 물체 조각들을 묶는다. [PDF 4쪽](https://arxiv.org/pdf/2404.13696#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2404.13696#page=5)
- 센서 관측을 받으며 계층 그래프를 갱신하고, 실제 장면과 로봇에서 그래프 크기·작업 관련성·구축 비용을 평가했다. [PDF 7쪽](https://arxiv.org/pdf/2404.13696#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2404.13696#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |
| Embodiment/environment | During the experiments, the robot constructs a map with Clio in real-time while exploring a scene, and then is tasked to navigate to and pick up objects matching a provided natural language ... | hardware/simulator version and reset protocol | p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Dataset/benchmark | Closed-set semantic segmentation experiments on 8 scenes from the Replica [17] dataset. | role, split, size and leakage | p. 8 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Metric | We report the F1 score as the harmonic mean of osR and osP and include average IOU of the top n most relevant estimated objects, total number of estimated objects (Objs), and ... | definition, denominator, direction and uncertainty | p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS), p. 8 (VI. EXPERIMENTS) |
| Baseline/ablation | In particular, in some cases Clio retains an order of magnitude less objects compared to taskagnostic baselines (cf. with the number of objects in ClioPrim, which is essentially Clio without the Information ... | fair input/data/compute/action matching | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 7 (VI. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / VII. LIMITATIONS - extractive body cue:** Despite the encouraging experimental results, our approach has multiple limitations.
- **p. 8 / VII. LIMITATIONS - extractive body cue:** First, while our method is zero-shot and is not bound to any particular foundation model, it does inherit some limitations from the foundation models used ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** Closed-Set Object Evaluation While Clio is designed for open-set detection, we include results on the closed-set Replica [17] dataset using the evaluation method performed by ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (IV. TASK-DRIVEN CLUSTERING)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the scene as well as the ... (p. 2, I. INTRODUCTION).
- **Actual contribution:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once on entire graph takes approximately 30 ... (p. 7, VI. EXPERIMENTS).
- **Explicit failure boundary:** Notably, Clio was only unable to select the correct target object in the scene graph once (i.e., the "Wrong Object" failure category). (p. 8, VI. EXPERIMENTS).

## 배포 범위 대조

- 코드 — 저자 구현 파일 · clio/src/object_update_functor.cpp [배포 파일](https://raw.githubusercontent.com/MIT-SPARK/Clio/f912b7c08fb0e029d80fd6b05eccee5009199ce4/clio/src/object_update_functor.cpp)
- 데이터 — 저자 저장소에서 평가 장면의 좌표 변환을 확인했다. 별도 배포한 Office·Apartment·Cubicle·Building 원시 RGB-D 묶음은 저자 안내에서 식별했다. [배포 파일](https://raw.githubusercontent.com/MIT-SPARK/Clio/f912b7c08fb0e029d80fd6b05eccee5009199ce4/clio_eval/scene_transforms.yaml)
