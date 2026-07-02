# Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments

- Year/Venue: 2020 / ECCV
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, Robotics, Navigation, Benchmark
- Paper link: ./2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/paper.pdf
- Code/Project: https://jacobkrantz.github.io/vlnce/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a sparse set of ...
- By being situated in continuous environments, this setting lifts a number of assumptions implicit in prior work that represents environments as a sparse graph of panoramas with edges ...

## Core Idea
- We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To establish context for our results, we consider random and hand-crafted agents shown in Tab.
- We train and evaluate our models in VLN-CE.

## Limitation
- In models presented here, we took an approach where observations were mapped directly to low-level control in an end-to-end manner; however, exploring modular approaches is exciting future work.

## Contribution
- We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines.
- By being situated in continuous environments, this setting lifts a number of assumptions implicit in prior work that represents environments as a sparse graph of panoramas with edges ...

## Abstract Cue
- We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
