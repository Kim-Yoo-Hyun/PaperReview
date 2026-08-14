# Method

- Year/Venue: 2024 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, bimanual manipulation, motion planning, inverse kinematics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://tommycohn.com/Bimanual-Web/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- D ISCUSSION We presented a novel parametrization of the constrained configuration space that arises in bimanual manipulation, which can be leveraged by both sampling-based planners and trajectory optimizers ...
- We use the multi-query PRM algorithm , initialized with nodes from multiple BiRRTs to ensure connectivity, as in [8, §C].
- We use GCS-planner with 19 regions, constructed from hand-selected seed points.

## 원리적 동기
- We leverage an analytic solution to the inverse kinematics problem to parametrize the configuration space, resulting in a lower-dimensional representation where the set of valid configurations has positive ...
- In the case of certain bimanual planning problems, there is additional structure that
- D ISCUSSION We presented a novel parametrization of the constrained configuration space that arises in bimanual manipulation, which can be leveraged by both sampling-based planners and trajectory optimizers ...

## 핵심 방법론
- D ISCUSSION We presented a novel parametrization of the constrained configuration space that arises in bimanual manipulation, which can be leveraged by both sampling-based planners and trajectory optimizers ...
- We use the multi-query PRM algorithm , initialized with nodes from multiple BiRRTs to ensure connectivity, as in [8, §C].
- We use GCS-planner with 19 regions, constructed from hand-selected seed points.
- For sampling-based planners, we use the single-query Atlas-BiRRT and multiquery Atlas-PRM algorithms , as implemented in the Open Motion Planning Library .
- For both the BiRRT and PRM plans, we use short-cutting to post-process the paths .
