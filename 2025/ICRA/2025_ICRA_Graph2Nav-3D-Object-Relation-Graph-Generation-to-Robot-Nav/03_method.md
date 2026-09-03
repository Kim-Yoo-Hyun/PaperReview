# Method - Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2504.16782v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. GRAPH2NAV), p. 4 (IV. INTEGRATION WITH SAYNAV), p. 3 (III. GRAPH2NAV), p. 4 (IV. INTEGRATION WITH SAYNAV)): Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation graphs and 3D semantic mapping ...

## Method Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation ...
- **p. 1 / Abstract - extractive body cue:** We also evaluate the impact of Graph2Nav via integration with SayNav, a state-of-the-art planner based on large language models, on an unmanned ground robot to ...
- **p. 3 / III. GRAPH2NAV - extractive body cue:** 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is equipped on a ...
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** To accomplish SayNav in the actual physical world, we use Graph2Nav to replace the original scene graph generation module in SayNav.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** It separately models the objects and relations in the form of queries from two Transformer decoders, followed by a prompting-like relation-object matching mechanism.
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** It includes three modules: (1) Incremental Scene Graph Generation, (2) High-Level LLM-based Dynamic Planner, and (3) Low-Level Planner.
- **p. 2 / III. GRAPH2NAV - extractive body cue:** Graph2Nav (Figure 2) includes three major components: (1) A SLAM system that maps and labels 3D objects in the surrounding environment using sensors (including a ...
- **p. 1 / Abstract - extractive body cue:** This approach avoids previous training data constraints in learning 3D scene graphs directly from 3D data.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Graph2Nav (Figure 1), a novel real-time 3D object-relation graph generation framework that addresses these limitations to robot navigation.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** Note Graph2Nav is designed to support various types of pose graph-based SLAM systems, whether it is vision-based, LiDAR-based, or a tightly-coupled LiDAR-vision system.

## Source Evidence Cues

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation ...
- **p. 1 / Abstract - extractive body cue:** We also evaluate the impact of Graph2Nav via integration with SayNav, a state-of-the-art planner based on large language models, on an unmanned ground robot to ...
- **p. 3 / III. GRAPH2NAV - extractive body cue:** 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is equipped on a ...
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** To accomplish SayNav in the actual physical world, we use Graph2Nav to replace the original scene graph generation module in SayNav.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** It separately models the objects and relations in the form of queries from two Transformer decoders, followed by a prompting-like relation-object matching mechanism.
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** It includes three modules: (1) Incremental Scene Graph Generation, (2) High-Level LLM-based Dynamic Planner, and (3) Low-Level Planner.
- **p. 2 / III. GRAPH2NAV - extractive body cue:** Graph2Nav (Figure 2) includes three major components: (1) A SLAM system that maps and labels 3D objects in the surrounding environment using sensors (including a ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths ... | p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We also evaluate the impact of Graph2Nav via integration with SayNav, a state-of-the-art planner based on large language models, on an unmanned ... | p. 1 (Abstract), p. 3 (III. GRAPH2NAV) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is ... | p. 3 (III. GRAPH2NAV), p. 4 (IV. INTEGRATION WITH SAYNAV) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive body cue:** This approach avoids previous training data constraints in learning 3D scene graphs directly from 3D data.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The main advantage of a 3D scene graph over other object-based 3D scene representations is its capability also to represent semantic relationships (e.g. "beside", "in ...
- **p. 3 / III. GRAPH2NAV - extractive body cue:** Inconsistent labels and masks will be corrected and updated.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** Then, it updates the labels of voxels that are previously updated by P.
- **p. 4 / III. GRAPH2NAV - extractive body cue:** We will also update existing nodes in G using correspondent information from Gi.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 4 (III. GRAPH2NAV).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Semantic, Object, Extraction, assume, sensor, system, composed, RGBD, camera, LiDAR-camera, suite, equipped, mobile, platform | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Semantic, Object, Extraction, assume, sensor, system, composed, RGBD, camera, LiDAR-camera | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, Graph2Nav, real-time, objectrelation, graph, generation, framework | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | avoids, previous, training, data, constraints, learning, scene, graphs, directly, main | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. GRAPH2NAV - extractive body cue:** 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is equipped on a ...
- **p. 3 / III. GRAPH2NAV - extractive body cue:** The panoptic segmentation image Ii used in the real-time 3D semantic object extraction process (Section III-A) is formed by combining M and Q outputted from ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The figure also shows examples of 2D input images and the 3D point clouds generated by Graph2Nav.
- **p. 1 / Abstract - extractive body cue:** We also evaluate the impact of Graph2Nav via integration with SayNav, a state-of-the-art planner based on large language models, on an unmanned ground robot to ...
- **p. 2 / III. GRAPH2NAV - extractive body cue:** Graph2Nav (Figure 2) includes three major components: (1) A SLAM system that maps and labels 3D objects in the surrounding environment using sensors (including a ...
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** Each LLM-planned step is executed by the Low-Level Planner to generate a series of control commands for execution during navigation.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | It shows Graph2Nav reduces object localization error across a wide variety of objects from three environments, by leveraging 3D SLAM techniques to ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We propose Graph2Nav, a real-time 3D objectrelation graph generation framework, for autonomous navigation in the real world. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We use Nvidia AGX Orin as our onboard computer for Graph2Nav processing and SayNav inference.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** main, contributions, summarized, follows, Graph2Nav, real-time, objectrelation, graph, generation, framework, combines, strengths, object-relation, graphs, semantic, mapping, techniques, integrate, LLM-based, planner.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Therefore, once the robot starts the task, it will first look around to build the initial scene graph of the perceived environment ... | p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Global / local decision | We measure 3D coordinates of a set of representative 3D objects using state-of-the-art survey techniques inside these three environments. | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Motion execution / recovery | Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / V. EXPERIMENTS - extractive body cue:** It means the robot does two trials (one uses the graph without relations, and the other uses the entire graph with object relations from Graph2Nav) ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Without object-relations, the LLM generates the initial search plan based on (1) the distances to different large objects inside the environment, and (2) the likelihoods ...
- **p. 6 / VI. CONCLUSIONS AND DISCUSSION - extractive body cue:** To fulfull this goal, we propose Graph2Nav, a novel real-time 3D object-relation graph generation framework that addresses current limitations to robot navigation.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The plan can also be dynamically changed, updated, or replanned during execution, if any failure happens or any new information is received.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. GRAPH2NAV), p. 4 (IV. INTEGRATION WITH SAYNAV), p. 3 (III. GRAPH2NAV), p. 4 (IV. INTEGRATION WITH SAYNAV), objective p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 4 (III. GRAPH2NAV), temporal p. 5 (V. EXPERIMENTS), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 2 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
