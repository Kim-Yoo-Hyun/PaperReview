# A Method for Registration of 3-D Shapes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/34.121791.
> PDF retrieval source: https://doi.org/10.1109/34.121791. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1992 / IEEE Transactions on Pattern Analysis and Machine Intelligence
- Authors: P.J. Besl, Neil D. McKay
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Registration, ICP, state estimation
- Official paper: https://api.crossref.org/works/10.1109/34.121791
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; tesseract OCR fallback; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791) 기준이다.

## Why This Paper Is Here

Besl과 McKay의 ICP는 최근접점 대응과 강체 변환 추정을 반복해 두 3차원 형상을 정합한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper describes general-purpose, representation-independent method for the accurate and. computationally ‘eMicient registration of 3-D shapes Including freeform curves ‘and surfaces.
- **p. 1 / Abstract - extractive body cue:** The method handles the fll ix degrees of freedom ind is based on the iterative closest point (ICP) algorithm, Which requires only a procedure to ...
- **p. 1 / Abstract - extractive body cue:** The ICP algorithm always ‘Converges monotonically to the nearest local minimum of « mear Square distance metric, and experience shows that the rate of/ convergence ...
- **p. 1 / Abstract - extractive body cue:** Therefore, given an adequate set of intial rotations and translations for 2 particular class of objects with a certain level of "shape complexity," one can ...
- **p. 1 / Abstract - extractive body cue:** For example, a given "model" shape and a sensed "data" shape that represents 2 major portion of the model shape can be registered in minutes ...
- **p. 2 / 1) Point sets - extractive body cue:** reasonable quality curve data but has difficulty with very noisy curves because the method uses arclenath sampling of the curves to obtain corresponding point sets.
- **p. 2 / 1) Point sets - extractive body cue:** The primary limitation of this work was that it relied ‘on the probable existence of reasonably large planar regions Within a free-form shape.

## Core Idea

- **p. 4 / B. Point to Implicit Entity Distance - extractive body cue:** The SVD approach, based on the eross- ‘covariance matrix of two point distributions, does, however, ‘generalize easily ton dimensions and would be our method of ...
- **p. 2 / 1) Point sets - extractive body cue:** A recent conference proceedings [47] contains new contributions on this subject.
- **p. 2 / 1) Point sets - extractive body cue:** ‘Schwartz and Sharir [50] developed a solution to the freeform space curve matching problem without feature extraction in late 1985.
- **p. 1 / 1) Point sets - extractive body cue:** Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property.
- **p. 8 / B. Convergence Theorem - extractive body cue:** Unfortunately ifthe objective function evaluator changes the ‘values inthe state vector duting the optimization iteration, this
- **p. 2 / 1) Point sets - extractive body cue:** Then, a conventional steepest descent algorithm is used to rotate and translate the second data set so tat it minimizes the sum of the covariance-weighted ...
- **p. 2 / 1) Point sets - extractive body cue:** His method forms an attributed relational graph of fundamental surface regions for data and ‘model shapes and then performs graph matching using an inexact approach ...
- **p. 6 / B. Convergence Theorem - extractive body cue:** then there is good direction a registration state vectors: Gis de.

## Observation, State, and Output Interface

ICP는 기하 데이터의 최근접점을 찾고 강체 변환을 반복 추정해 정합 오차를 줄인다. 합성 형상과 레이저 거리 영상에서 얻은 표본으로 정합을 시험한다. 측정은 형상 정합 오차이며 로봇 제어 정책을 실행하지 않는다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=5) · [PDF 13쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=13)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | [36] also describe a method for the registration of multiple overlapping range images without distinctive feature extraction. | 최근접점 계산이 가능한 형상과 표본 점 집합 | p. 2 (1) Point sets), p. 1 (1) Point sets) |
| State/latent | describe, registration, multiple, overlapping, range, images, without, distinctive, feature, extraction, Then, iterative | 현재 강체 변환과 최근접점 대응 | p. 2 (1) Point sets), p. 1 (1) Point sets), p. 1 (1) Point sets) |
| Output/action | Then, the iterative closest point (ICP) algorithm is stated, and a theorem is proven concerning its monotonic convergence property. | 정합한 회전과 평행이동 | p. 1 (1) Point sets), p. 1 (1) Point sets), p. 2 (1) Point sets) |
| Objective/outcome | Horn and Harris [33] also addressed the problem of estimating the exact rigid-body motion of the observer given sequentially digitized range image frames of the same terrain, "They describe a range rate ... | 평균제곱거리의 수렴과 초기 정렬 영향 | p. 2 (1) Point sets), p. 3 (A. Point to Parametric Entity Distance), p. 4 (B. Point to Implicit Entity Distance) |

## Main Claims and Actual Contribution

- 최근접점 계산이 가능한 기하 표현에 알고리즘을 적용하고 평균제곱거리의 단조 감소와 국소 수렴을 분석했다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=6)
- 형상·초기 배치·관측 잡음이 달라질 때 곡선과 표면 자료에서 정합 결과를 비교했다. [PDF 10쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=10) · [PDF 11쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=11) · [PDF 12쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=12) · [PDF 13쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=121791#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 11 (A. Point Ser Matching), p. 14 (A BN) |
| Embodiment/environment | Any quoted approximate times are given for execution ona single-processor computer rated at 1.6 ‘flops on the 100 x 100 double-precision Linpack benchmark, | hardware/simulator version and reset protocol | p. 10 (VI. EXPERIMENTAL RESULTS), p. 14 (A BN) |
| Dataset/benchmark | Theorem: ‘The iterative closes point algorithm always converges monotonically toa local minimum with respect to the smean-square distance objective funetion. | role, split, size and leakage | p. 10 (VI. EXPERIMENTAL RESULTS), p. 14 (A BN), p. 6 (B. Convergence Theorem), p. 8 (B. Convergence Theorem) |
| Metric | 4d, Terminate the iteration when the change in meansquare error falls below a preset threshold > > 0 specifying the desired precision ofthe registration: dem det <7. | definition, denominator, direction and uncertainty | p. 6 (B. Point to Implicit Entity Distance), p. 7 (B. Convergence Theorem), p. 16 (A BN) |
| Baseline/ablation | The 3 range of 0.6 units is clearly visible compared withthe size ofthe object. | fair input/data/compute/action matching | p. 11 (B. Curve Matching), p. 11 (A. Point Ser Matching), p. 7 (B. Convergence Theorem) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A BN - extractive body cue:** This is a problem with almost all of the shape ‘matching algorithms in the literature For any given fixed initial set of rotations, the global ...
- **p. 6 / B. Convergence Theorem - extractive body cue:** ‘would yield a smaller mean square error than the least squares registration, which cannot possibly be the case.
- **p. 6 / B. Point to Implicit Entity Distance - extractive body cue:** 4d, Terminate the iteration when the change in meansquare error falls below a preset threshold > > 0 specifying the desired precision ofthe registration: dem ...
- **p. 7 / B. Convergence Theorem - extractive body cue:** Note the smooth character ofall the curves.
- **p. 8 / B. Convergence Theorem - extractive body cue:** The only way to be sure isto find the minimum ofall the local minima.
- **p. 8 / B. Convergence Theorem - extractive body cue:** This is an interesting accomplishment for a function where derivatives cannot be evaluated.
- **p. 10 / A. Initial States for Global Matching - extractive body cue:** Although the above methods for global shape matching will work very well for many shapes with a small probability of error, we can also state ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1) Point sets), p. 4 (B. Point to Implicit Entity Distance), p. 1 (1. Istmopuction), p. 1 (1) Point sets)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This is a problem with almost all of the shape ‘matching algorithms in the literature For any given fixed initial set of rotations, the global shape matching capability can be ... (p. 16, A BN).
- **Actual contribution:** A recent conference proceedings [47] contains new contributions on this subject. (p. 2, 1) Point sets).
- **Evaluation boundary:** To give a quantitative example comparison, the registration values, RMS error, maximum error, angular change, and cu ‘mulative are length values were recorded during 50 iterations of both the basic ... (p. 7, B. Convergence Theorem).
- **Explicit failure boundary:** allowable occlusion percentages, e-., 10% oles, We do not advocate our proposed method if feature extraction techniques will successfully solve the problem. ‘The generalization to matching deformable models with high ... (p. 16, A BN).
