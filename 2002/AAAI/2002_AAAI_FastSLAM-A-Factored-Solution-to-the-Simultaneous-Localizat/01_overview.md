# FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf.
> PDF retrieval source: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2002 / AAAI
- Authors: Michael Montemerlo, Sebastian Thrun, Daphne Koller, Ben Wegbreit
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, SLAM, particle filter, state estimation
- Official paper: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf
- Full-text retrieval: https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

FastSLAM은 로봇의 이동 궤적이 주어지면 랜드마크 위치가 조건부 독립이 된다는 성질로 SLAM 사후분포를 분해한다. [PDF 1쪽](https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The ability to simultaneously localize a robot and accurately map its surroundings is considered by many to be a key prerequisite of truly autonomous robots.
- **p. 1 / Abstract - extractive body cue:** However, few approaches to this problem scale up to handle the very large number of landmarks present in real environments.
- **p. 1 / Abstract - extractive body cue:** Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation.
- **p. 1 / Abstract - extractive body cue:** This paper presents FastSLAM, an algorithm that recursively estimates the full posterior distribution over robot pose and landmark locations, yet scales logarithmically with the number ...
- **p. 1 / Abstract - extractive body cue:** This algorithm is based on an exact factorization of the posterior into a product of conditional landmark distributions and a distribution over robot paths.
- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 1 / Abstract - extractive body cue:** A key limitation of EKF-based approaches is their computational complexity.

## Core Idea

- **p. 2 / Abstract - extractive body cue:** We also extend the FastSLAM algorithm to situations with unknown data association and unknown number of landmarks, showing that our approach can be extended to ...
- **p. 4 / Abstract - extractive body cue:** Our approach makes it possible to execute a FastSLAM iteration in O(M log K) time.
- **p. 1 / Abstract - extractive body cue:** This observation was made previously by Murphy [13], who developed an efficient particle filtering algorithm for learning grid maps.
- **p. 2 / Abstract - extractive body cue:** We develop a tree-based data structure that reduces the running time of FastSLAM to O(M log K), making it significantly faster than existing EKF-based SLAM ...
- **p. 3 / Abstract - extractive body cue:** This will allows us to silently "forget" all other pose estimates, rendering the size of each particle independent of the time index t.
- **p. 3 / Abstract - extractive body cue:** First, each particle st,[m] in St-1 is used to generate a probabilistic guess of the robot's pose at time t s[m] t ∼ p(st / ...
- **p. 1 / Abstract - extractive body cue:** Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM.
- **p. 2 / Abstract - extractive body cue:** Experimental results using a physical robot and a robot simulator illustrate that the FastSLAM algorithm can handle orders of magnitude more landmarks than present day ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation. | camera/depth stream, pose, map와 language goal | p. 1 (Abstract), p. 1 (Abstract) |
| State/latent | Kalman, filter-based, algorithms, example, require, time, quadratic, number, landmarks, incorporate, sensor, observation | robot pose, free-space/semantic map와 local goal | p. 1 (Abstract), p. 1 (Abstract), p. 3 (Abstract) |
| Output/action | Based on this observation, this paper describes an efficient SLAM algorithm called FastSLAM. | collision-free trajectory 또는 velocity command | p. 1 (Abstract), p. 3 (Abstract), p. 4 (Abstract) |
| Objective/outcome | For nt = k, we obtain p(θk / st, zt, ut, nt) (9) Bayes ∝ p(zt / θk, st, zt-1, ut, nt) p(θk / st, zt-1, ut, nt) Markov = p(zt / ... | goal reach, safety, localization error와 replanning latency | p. 3 (Abstract), p. 2 (Abstract), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- 입자로 궤적 가설을 근사하고 각 입자 안에서 개별 랜드마크의 추정치를 갱신한다. [PDF 2쪽](https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf#page=2) · [PDF 3쪽](https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf#page=3)
- 랜드마크 지도를 트리로 공유해 입자당 관측 갱신 비용을 줄이고 시뮬레이션과 실제 주행 자료로 평가한다. [PDF 4쪽](https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf#page=4) · [PDF 5쪽](https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf#page=5)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 2 (Abstract) |
| Embodiment/environment | To map its environment, the robot can sense landmarks. | hardware/simulator version and reset protocol | p. 2 (Abstract), p. 2 (Abstract) |
| Dataset/benchmark | Real-world experiments were complimented by systematic simulation experiments, to investigate the scaling abilities of the approach. | role, split, size and leakage | p. 2 (Abstract), p. 2 (Abstract), p. 5 (Abstract), p. 3 (Abstract) |
| Metric | Figure 6: Accuracy of the FastSLAM algorithm as a function of (a) the number of landmarks N, and (b) the number of particles M. Large number of landmarks reduce the robot localization ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 5 (Abstract), p. 5 (Abstract) |
| Baseline/ablation | FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map. | fair input/data/compute/action matching | p. 5 (Abstract), p. 2 (Abstract), p. 2 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Abstract - extractive body cue:** Data Association In many real-world problems, landmarks are not identifiable, and the total number of landmarks K cannot be obtained trivially-as was the case above.
- **p. 5 / Abstract - extractive body cue:** Unfortunately, the physical testbed does not allow for systematic experiments regarding the scaling properties of the approach.
- **p. 2 / Abstract - extractive body cue:** Many measurement models in the literature assume that the robot can measure range and bearing to landmarks, confounded by measurement noise.
- **p. 5 / Abstract - extractive body cue:** It has been observed frequently that false data association will make the conventional EKF approach fail catastrophically [2].

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 4 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (Abstract)이다.
