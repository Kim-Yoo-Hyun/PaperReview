# Method - Towards Physically Executable 3D Gaussian for Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HB6KvsqcAn; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/246616. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 7. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## DOC-QA3 — PS의 원문·구현 계약

**원문 근거:** PDF p. 7 §3.3의 식은 `1 − mean min(abs(Δθ)/π, 1)`이다. 본문에서 부르는 variance와 식도 구분한다.

**공식 코드 근거:** `PathSmoothness`는 XY 위치 차분 중 norm > 1e-6인 벡터만 남기고, 그 연속 차이 norm의 평균 a에 대해 `1/(1+10a)`를 반환한다. 유효 변위가 2개 미만이면 1이다. heading이나 π clipping, dt 나눗셈을 사용하지 않는다. 따라서 코드의 velocity/acceleration 변수는 시간 정규화된 물리량으로 읽지 않는다.

`default_measures`/`nogoal_measures` → benchmark의 manager 생성 → command 전후 update → episode log의 dump까지 연결했다. **연구자 해석:** 샘플링·이동 간격·좌표 단위가 다른 실행의 PS를 동일한 metric으로 합칠 수 없다. 정지/제자리 회전 조건의 높은 값은 코드에서 도출되는 경계이지 실제 정책 실패를 측정한 결과가 아니다.

대조 근거: [원문](https://arxiv.org/html/2510.21307v2#S3.SS3) · [공식 구현 69e60c2123ac](https://github.com/Galery23/SAGE-3D_Official/blob/69e60c2123aca55ff2ad96d66a80a9bac5a7912d/Code/benchmark/environment_evaluation/measures.py#L338-L381) · [전체 호출 경로·파일 hash](../../../work/sources/paper_code_formula_review_2026-10-23.json). 검토일 2026-10-23. 지정 구간을 정적으로 읽었으며 코드 실행·의존성 설치는 하지 않았다. 논문 실험과 이 commit의 동일성 및 저자 확인 정오표는 미확인이다. 사용자 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS)): The training data did not include any VLN-CE R2R or RxR samples.

## Method Body Digest

- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We run A*-based shortest-path search to generate trajectories with a cost function that integrates free-space distance, narrow-passage penalties, and area preferences to ensure both obstacle ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex indoor spaces (Wei ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For data, we provide a hierarchical instruction scheme that combines high-level semantic goals (especially task-causal ones like "I'm thirsty, get water from the table") with ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, we design a 2D semantic top-down map derived from 3DGS to support instruction generation and path planning.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** To diversify the dataset, start-end pairs are sampled across different rooms, functional areas, and object instances, and a minimum safety distance is enforced to avoid ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a 3DGS-Mesh Hybrid Representation: starting from our mesh scene data, we extract collision bodies for each object as the physics layer, while using ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we present SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a paradigm that upgrades 3DGS from a purely perceptual scene ...

## Source Evidence Cues

- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **Detected method headings:** B DETAILED SAMPLING METHOD OF INTERIORGS (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The training data did not include any VLN-CE R2R or RxR samples. | p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set. | p. 15 (A IMPLEMENTATION DETAILS) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The training data did not include any VLN-CE R2R or RxR samples. | p. 15 (A IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We run A*-based shortest-path search to generate trajectories with a cost function that integrates free-space distance, narrow-passage penalties, and area preferences to ensure both obstacle ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling, them, follow, natural, language | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Vision-and-Language, Navigation, VLN, core, capability, Vision-Language, Action, VLA, models, enabling | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | introduce, DGS-Mesh, Hybrid, Representation, starting, mesh, scene, data, extract, collision | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | shortest-path, search, generate, trajectories, cost, function, integrates, free-space, distance, narrow-passage | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 INTRODUCTION - extractive body cue:** Vision-and-Language Navigation (VLN) is a core capability for Vision-Language Action (VLA) models, enabling them to follow natural language instructions and navigate complex indoor spaces (Wei ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For data, we provide a hierarchical instruction scheme that combines high-level semantic goals (especially task-causal ones like "I'm thirsty, get water from the table") with ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, we design a 2D semantic top-down map derived from 3DGS to support instruction generation and path planning.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** We selected 500k "trajectory-instruction" pairs from SAGE-Bench, with no overlap with the test set.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** To diversify the dataset, start-end pairs are sampled across different rooms, functional areas, and object instances, and a minimum safety distance is enforced to avoid ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 ... | episode/sequence/action-chunk boundary |
| Path smoothness metric | PS = 1 − meanₜ min(abs(Δθₜ)/π,1), t=2,…,T. | PDF p. 7 §3.3의 heading-change metric; 본문의 variance 표현과 달리 식은 clipped absolute-change 평균 | 원문 식이며 공개 구현과 다름; 위 DOC-QA3 참조. Hz/latency 근거가 아님 |
| Memory | map/scene graph, pose history와 current local goal. | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The results show that 3DGS scene data achieves a perframe rendering time of 6.2 ms and an average memory usage of 220 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The training data did not include any VLN-CE R2R or RxR samples.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** Training was carried out on 8 NVIDIA Tesla H20 GPUs with a batch size of 256 and a learning rate of 2 × 10-5.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We randomly selected 10k training samples and 1k validation samples from both traditional scanned mesh data and our 3DGS data, and conducted experiments with the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, data, include, VLN-CE, R2R, RxR, samples, selected, trajectory-instruction, pairs, SAGE-Bench, overlap, test, shortest-path, search, generate, trajectories, cost, function, integrates.
- **Relevant PDF headings:** B DETAILED SAMPLING METHOD OF INTERIORGS (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Data in # Train SAGE-Bench VLN #Scenes #Samples SR ↑ OSR ↑ SPL ↑ CSR ↑ ICP ↓ PS ↑ 800 240k ... | p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Global / local decision | 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines. | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Motion execution / recovery | Even the recent SOTA model NaVILA achieves only a 0.39 success rate on high-level instructions, significantly lower than its 0.56 success rate ... | p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4, models trained entirely on SAGE-Bench data (without any VLN-CE data) achieved clear performance improvements over their respective baselines.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We trained two models on this subset: one based on NaVILA's pre-trained model navila-siglip-llama3-8b-v1.5-pretrain (denoted as NaVILA-base), producing NaVILA-SAGE; and the other based on Navid's ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overview of SAGE-Bench. SAGE-Bench includes a hierarchical instruction generation scheme, two major task types, two episode complexity categories, and three newly designed natural ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4 corroborate this finding: the NaVILA model (blue trajectory) exhibits unsmooth movement and persistent collisions that conventional metrics fail to reveal.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Traditional 3DGS vs. Our work. Compared with traditional 3DGS, our InteriorGS pro- vides object-level 3DGS annotations across diverse indoor and outdoor scenes, including ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Overview of SAGE-3D, which consists of two key components: (1) Object-Level Semantic Grounding, 3DGS data is annotated by expect at the object level, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 15 (A IMPLEMENTATION DETAILS), p. 15 (A IMPLEMENTATION DETAILS), objective p. 15 (A IMPLEMENTATION DETAILS), temporal p. 8 (4 EXPERIMENTS), p. 7 (3) Path Smoothness), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
