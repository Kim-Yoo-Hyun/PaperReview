# Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

- Year/Venue: 2026 / ICRA
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Robotics, Graph Reasoning, semantic
- Paper link: ./2026/ICRA/2026_ICRA_Open-Vocabulary-Spatio-Temporal-Scene-Graph-for-Robot-Perc/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The emergence of large models offers new possibilities for these limitations.
- ST-OVSG leverages LVLMs to construct open-vocabulary 3D object representations, and extends them into the temporal domain via Hungarian assignment with our temporal matching cost, yielding a unified spatio-temporal ...

## Core Idea
- To further reduce redundancy and highlight taskrelevant cues, we propose a task-oriented subgraph filtering strategy that produces compact inputs for the planner.
- To mitigate this, we introduce the Spatio-Temporal Open-Vocabulary Scene Graph (ST-OVSG), a representation that enriches openvocabulary perception with temporal dynamics and lightweight latency annotations.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that our method achieves 74% node accuracy on Replica benchmark, outperforming ConceptGraph.
- Notably, in latency-robustness experiment, the LVLM planner assisted by ST-OVSG achieved a planning success rate of 70.5%.
- These approaches have achieved 1 HI-Robot Lab, School of Automation Sc

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show that our method achieves 74% node accuracy on Replica benchmark, outperforming ConceptGraph.
- To further reduce redundancy and highlight taskrelevant cues, we propose a task-oriented subgraph filtering strategy that produces compact inputs for the planner.
- To mitigate this, we introduce the Spatio-Temporal Open-Vocabulary Scene Graph (ST-OVSG), a representation that enriches openvocabulary perception with temporal dynamics and lightweight latency annotations.

## Abstract Cue
- — Teleoperation via natural-language reduces operator workload and enhances safety in high-risk or remote settings.
