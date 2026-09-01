# Clio: Real-time Task-Driven Open-Set 3D Scene Graphs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2404.13696.
> PDF retrieval source: https://arxiv.org/pdf/2404.13696. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 3D Vision, Graph Reasoning
- Official paper: https://arxiv.org/abs/2404.13696
- Full-text retrieval: https://arxiv.org/pdf/2404.13696
- Code/Project: https://github.com/MIT-SPARK/Clio
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the scene as well as the threshold used ...를 문제로 두고, We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.
- **p. 2 / Abstract - extractive body cue:** Our final contribution is an extensive experimental campaign showing that Clio not only allows real-time construction of compact open-set 3D scene graphs, but also improves ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our third contribution (Section V) is to include the proposed task-driven clustering algorithm into a real-time system, named Clio (Fig.
- **p. 3 / I. INTRODUCTION - extractive body cue:** Our second contribution (Section IV) is to apply the Agglomerative IB algorithm from [14] to the problem of taskdriven 3D scene understanding.
- **p. 4 / IV. TASK-DRIVEN CLUSTERING - extractive body cue:** Towards this goal, we propose an incremental version of the algorithm that can be executed online as the robot explores
- **p. 8 / VI. EXPERIMENTS - extractive body cue:** Overall, we achieve a 57% success rate for the grasps and a 71% success rate if we disregard the cases where Spot failed to actually ...
- **p. 7 / VI. EXPERIMENTS - extractive body cue:** First and second-best results are bolded and underlined, respectively. ∗Total time for Clio-batch normalized by number of images; clustering step for batch run once on ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Firstly, we observe that task-informed approaches (shaded blue rows in Table I) lead to improved open-set precision and retain a much smaller amount of objects ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 These approaches, however, leave to the user the difficult task of tuning suitable thresholds to control the number of segments that are extracted from the scene as well as the threshold used ...를 문제로 두고, We propose Clio, a novel approach for building task-driven 3D scene graphs in real-time with embedded open-set semantics.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (IV. TASK-DRIVEN CLUSTERING), p. 2 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
