# Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf.
> PDF retrieval source: https://arxiv.org/pdf/2504.16782v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Navigation, Graph Reasoning
- Official paper: https://www.proceedings.com/content/081/081087webtoc.pdf
- Full-text retrieval: https://arxiv.org/pdf/2504.16782v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, there are two major limitations in current 3D scene graph generation methods which hinder the growth of this field.를 문제로 두고, Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation graphs and 3D semantic mapping techniques. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose Graph2Nav, a real-time 3D objectrelation graph generation framework, for autonomous navigation in the real world.
- **p. 1 / Abstract - extractive body cue:** Our framework fully generates and exploits both 3D objects and a rich set of semantic relationships among objects in a 3D layered scene graph, which ...
- **p. 1 / Abstract - extractive body cue:** It learns to generate 3D semantic relations among objects, by leveraging and advancing state-of-the-art 2D panoptic scene graph works into the 3D world via 3D ...
- **p. 1 / Abstract - extractive body cue:** This approach avoids previous training data constraints in learning 3D scene graphs directly from 3D data.
- **p. 1 / Abstract - extractive body cue:** We conduct experiments to validate the accuracy in locating 3D objects and labeling objectrelations in our 3D scene graphs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, there are two major limitations in current 3D scene graph generation methods which hinder the growth of this field.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Graph2Nav (Figure 1), a novel real-time 3D object-relation graph generation framework that addresses these limitations to robot navigation.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Graph2Nav (Figure 1), a novel real-time 3D object-relation graph generation framework that addresses these limitations to robot navigation.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** Note Graph2Nav is designed to support various types of pose graph-based SLAM systems, whether it is vision-based, LiDAR-based, or a tightly-coupled LiDAR-vision system.
- **p. 1 / Abstract - extractive body cue:** We also evaluate the impact of Graph2Nav via integration with SayNav, a state-of-the-art planner based on large language models, on an unmanned ground robot to ...
- **p. 3 / III. GRAPH2NAV - extractive body cue:** 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is equipped on a ...
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** To accomplish SayNav in the actual physical world, we use Graph2Nav to replace the original scene graph generation module in SayNav.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** It separately models the objects and relations in the form of queries from two Transformer decoders, followed by a prompting-like relation-object matching mechanism.
- **p. 4 / IV. INTEGRATION WITH SAYNAV - extractive body cue:** It includes three modules: (1) Incremental Scene Graph Generation, (2) High-Level LLM-based Dynamic Planner, and (3) Low-Level Planner.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3D Semantic Object Extraction We assume that a sensor system, which is composed of an RGBD camera or a LiDAR-camera suite, is equipped on a mobile platform (a UGV in our case) ... | camera/depth stream, pose, map와 language goal | p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV) |
| State/latent | Semantic, Object, Extraction, assume, sensor, system, composed, RGBD, camera, LiDAR-camera, suite, equipped | robot pose, free-space/semantic map와 local goal | p. 3 (III. GRAPH2NAV), p. 3 (III. GRAPH2NAV), p. 1 (I. INTRODUCTION) |
| Output/action | The panoptic segmentation image Ii used in the real-time 3D semantic object extraction process (Section III-A) is formed by combining M and Q outputted from our PSGFormer. | collision-free trajectory 또는 velocity command | p. 3 (III. GRAPH2NAV), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective/outcome | This approach avoids previous training data constraints in learning 3D scene graphs directly from 3D data. | goal reach, safety, localization error와 replanning latency | p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (III. GRAPH2NAV) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Graph2Nav (Figure 1), a novel real-time 3D object-relation graph generation framework that addresses these limitations to robot navigation.
- **p. 3 / III. GRAPH2NAV - extractive body cue:** Note Graph2Nav is designed to support various types of pose graph-based SLAM systems, whether it is vision-based, LiDAR-based, or a tightly-coupled LiDAR-vision system.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Clearly, Graph2Nav greatly improves the capability in detecting correct relationships among the objects, compared to 2D-based method.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** First, we validate the accuracy of our generated 3D scene graphs for both indoor and outdoor scenes in the real world.
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Note the accuracy of our mapped 3D point cloud and the estimated platform pose relies on the underlying SLAM system (LIO-SAM [23] in our case), ...
- **p. 6 / V. EXPERIMENTS - extractive body cue:** From the results, we found that the LLM is able to utilize the object-relations to design more efficient plans to search objects.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Embodiment/environment | Therefore, once the robot starts the task, it will first look around to build the initial scene graph of the perceived environment using Graph2Nav. | hardware/simulator version and reset protocol | p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Dataset/benchmark | The robot then will set up and execute a search plan for finding the target object based on LLM's knowledge of the perceived environment. | role, split, size and leakage | p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Metric | First, we validate the accuracy of our generated 3D scene graphs for both indoor and outdoor scenes in the real world. | definition, denominator, direction and uncertainty | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Baseline/ablation | We measure 3D coordinates of a set of representative 3D objects using state-of-the-art survey techniques inside these three environments. | fair input/data/compute/action matching | p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. CONCLUSIONS AND DISCUSSION - extractive body cue:** To fulfull this goal, we propose Graph2Nav, a novel real-time 3D object-relation graph generation framework that addresses current limitations to robot navigation.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** The plan can also be dynamically changed, updated, or replanned during execution, if any failure happens or any new information is received.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Combining observations from different 2D images shall improve the robustness and accuracy in depicting the actual relationships among 3D objects in the real world.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, there are two major limitations in current 3D scene graph generation methods which hinder the growth of this field.를 문제로 두고, Our main contributions are summarized as follows: • We propose Graph2Nav, a new real-time 3D objectrelation graph generation framework that combines strengths of 2D object-relation graphs and 3D semantic mapping techniques. • ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 3 (III. GRAPH2NAV), p. 4 (IV. INTEGRATION WITH SAYNAV) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
