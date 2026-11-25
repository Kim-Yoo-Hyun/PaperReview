# Method - 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p067.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p067.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 6 (2) Learning efficiency. While we train all the algorithms), p. 6 (2) Learning efficiency. While we train all the algorithms)): The decision module in DP3 is formulated as a conditional denoising diffusion model [23, 10, 39] that conditions on 3D visual features v and robot poses q, then denoises a ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** The decision module in DP3 is formulated as a conditional denoising diffusion model [23, 10, 39] that conditions on 3D visual features v and robot ...
- **p. 3 / III. METHOD - extractive body cue:** To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.
- **p. 4 / III. METHOD - extractive body cue:** We use DDIM [62] as the noise scheduler and use sample prediction instead of epsilon prediction for better high-dimensional action generation, with 100 timesteps at ...
- **p. 4 / III. METHOD - extractive body cue:** (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point ...
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** We replace the visual observation and the corresponding encoder in DP3 to evaluate different 3D representations.
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** The RGBD and depth images are processed using the same image encoder as Diffusion Policy, while voxel representations employ the VoxelCNN, as implemented in [7].
- **p. 5 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** As depicted in Figure 1, DP3 achieves an inference speed marginally surpassing Diffusion Policy.
- **원문 대조:** 식 (2)는 3D visual feature v와 robot pose q에 조건화한 noise-prediction MSE를 설명한다. 같은 페이지의 구현 설명은 DDIM과 sample prediction을 사용한다고 명시하므로, 개념식과 실제 prediction parameterization을 구분해야 한다. ([PDF p. 4](https://www.roboticsproceedings.org/rss20/p067.pdf#page=4), §III-C Decision, Eq. (2) and Implementation details).

## Design Rationale

- **p. 3 / III. METHOD - extractive body cue:** To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To tackle this challenging problem, we introduce 3D Diffusion Policy (DP3), a simple yet effective visual imitation learning algorithm that integrates the strengths of 3D ...
- **p. 3 / III. METHOD - extractive body cue:** The network, termed as DP3 Encoder, is conceptually simple: it consists of a three-layer MLP, a max-pooling function as an order-equivariant operation to pool point ...

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** The decision module in DP3 is formulated as a conditional denoising diffusion model [23, 10, 39] that conditions on 3D visual features v and robot ...
- **p. 3 / III. METHOD - extractive body cue:** To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception.
- **p. 4 / III. METHOD - extractive body cue:** We use DDIM [62] as the noise scheduler and use sample prediction instead of epsilon prediction for better high-dimensional action generation, with 100 timesteps at ...
- **p. 4 / III. METHOD - extractive body cue:** (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point ...
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** We replace the visual observation and the corresponding encoder in DP3 to evaluate different 3D representations.
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** The RGBD and depth images are processed using the same image encoder as Diffusion Policy, while voxel representations employ the VoxelCNN, as implemented in [7].
- **p. 5 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** As depicted in Figure 1, DP3 achieves an inference speed marginally surpassing Diffusion Policy.
- **Detected method headings:** III. METHOD (p. 3); 2) Learning efficiency. While we train all the algorithms (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | The decision module in DP3 is formulated as a conditional denoising diffusion model [23, 10, 39] that conditions on 3D visual features ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | To this end, we introduce 3D Diffusion Policy (DP3), which mainly consists of two critical parts: (a) Perception. | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | We use DDIM [62] as the noise scheduler and use sample prediction instead of epsilon prediction for better high-dimensional action generation, with ... | p. 4 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **원문 대조:** 식 (2)는 3D visual feature v와 robot pose q에 조건화한 noise-prediction MSE를 설명한다. 같은 페이지의 구현 설명은 DDIM과 sample prediction을 사용한다고 명시하므로, 개념식과 실제 prediction parameterization을 구분해야 한다. ([PDF p. 4](https://www.roboticsproceedings.org/rss20/p067.pdf#page=4), §III-C Decision, Eq. (2) and Implementation details).
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** In contrast, Diffusion Policy exhibits a slower learning progress and achieves notably lower convergence in most tasks.
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | End-to-End, Training, Policy, Expert, Demonstrations, Evaluation, Action, Observation, Decision, Diffusion, Single-view, Point, Cloud, Crop | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | End-to-End, Training, Policy, Expert, Demonstrations, Evaluation, Action, Observation, Decision, Diffusion | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | introduce, Diffusion, Policy, DP3, mainly, consists, critical, parts, Perception, tackle | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | training, objective, predict, noise, added, original, data, MSE, where, schedule | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - extractive body cue:** (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point ...
- **p. 3 / III. METHOD - extractive body cue:** Given a small set of expert demonstrations that contain complex robot skill trajectories, we want to learn a visuomotor policy π : O 7→A that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Visual imitation learning, which takes high-dimensional visual observations such as images or depth maps, eases the need for task-specific state estimation and thus gains the ...
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** Additionally, we observe that point clouds and oracle states are very competitive, showing that point clouds might help learn an optimal policy from demonstrations.
- **p. 3 / III. METHOD - extractive body cue:** DP3 utilizes the expressive Diffusion Policy [10] as the action-making backbone, which generates action sequences conditioning on our 3D visual features.
- **p. 4 / III. METHOD - extractive body cue:** During evaluation, DP3 determines actions based on visual observations from the environment.
- **p. 6 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** We also compare with oracle states, which include object states, target goals, and robot velocity besides robot poses.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | Compared to this line of works, we endeavor to develop a universal and fast 3D policy capable of tackling 1The inference speed ... | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | We use DDIM [62] as the noise scheduler and use sample prediction instead of epsilon prediction for better high-dimensional action generation, with ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | For each seed, we evaluate 20 episodes every 200 training epochs and then compute the average of the highest 5 success rates. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - extractive body cue:** We use DDIM [62] as the noise scheduler and use sample prediction instead of epsilon prediction for better high-dimensional action generation, with 100 timesteps at ...
- **p. 4 / III. METHOD - extractive body cue:** (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point ...
- **p. 5 / 2) Learning efficiency. While we train all the algorithms - extractive body cue:** As depicted in Figure 1, DP3 achieves an inference speed marginally surpassing Diffusion Policy.
- **p. 5 / IV. SIMULATION EXPERIMENTS - extractive body cue:** For each seed, we evaluate 20 episodes every 200 training epochs and then compute the average of the highest 5 success rates.
- **p. 4 / III. METHOD - extractive body cue:** We train 1000 epochs for MetaWorld tasks due to its simplicity and 3000 epochs for other simulated and real-world tasks, with batch size 128 for ...

## Method-Specific Formal Details

- **Body-defined terms:** decision, module, DP3, formulated, conditional, denoising, diffusion, model, conditions, visual, features, robot, poses, then, denoises, random, Gaussian, noise, actions, introduce.
- **Relevant PDF headings:** III. METHOD (p. 3); 2) Learning efficiency. While we train all the algorithms (p. 5).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | Simulation Benchmark (72 Tasks) Domain Robo Object Simulator ActD #Task #Demo Adroit Shadow Rigid/Art MuJoCo 28 3 10 Bi-DexHands Shadow Rigid/Art IsaacGym ... | p. 5 (IV. SIMULATION EXPERIMENTS), p. 7 (V. REAL WORLD EXPERIMENTS) |
| Grasp / trajectory generation | To this end, our main baseline is the image-based diffusion policy [10], simply referred to as Diffusion Policy. | p. 5 (IV. SIMULATION EXPERIMENTS), p. 4 (Figure/Table caption) |
| Contact execution / correction | Fig. 2: Overview of 3D Diffusion Policy (DP3). Above: In the training phase, DP3 simultaneously trains its perception module and decision-making process ... | p. 4 (Figure/Table caption), p. 5 (IV. SIMULATION EXPERIMENTS) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Generalization in 3D space with few data. We use MetaWorld Reach as an example task, given only 5 demonstra- tions (visualized by •). ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6: Efficient scaling with demonstrations. We sample 10 simulation tasks and train DP3 and Diffusion Policy with an increasing number of demonstrations. DP3 addresses ...
- **p. 8 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** For instance, the image-based diffusion policy excels in the Drill task but fails entirely in Roll-Up.
- **p. 8 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** It is noteworthy that the depthbased diffusion policy also does not incorporate color as input.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: 3D Diffusion Policy (DP3) is a visual imitation learning algorithm that marries 3D visual representations with diffusion policies, achieving surprising effectiveness in diverse ...
- **p. 9 / 2) Dumpling. The Allegro hand first wraps the plasticine - extractive body cue:** Accurate transformation isn't necessary due to the robustness of our network.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 6 (2) Learning efficiency. While we train all the algorithms), p. 6 (2) Learning efficiency. While we train all the algorithms), objective p. 4 (III. METHOD), p. 6 (2) Learning efficiency. While we train all the algorithms), temporal p. 2 (II. RELATED WORK), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (IV. SIMULATION EXPERIMENTS).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** (a) End-to-End Training Policy Expert Demonstrations (b) Evaluation Action Observation Decision: Diffusion Policy Single-view Point Cloud Crop FPS Linear Perception: Compact 3D Representations from Point Clouds Compact 3D Repr. (p. 4, III. METHOD).
- **Objective/update evidence:** As depicted in Figure 1, DP3 achieves an inference speed marginally surpassing Diffusion Policy. (p. 5, 2) Learning efficiency. While we train all the algorithms).
- **Temporal/runtime evidence:** DP3 utilizes the expressive Diffusion Policy [10] as the action-making backbone, which generates action sequences conditioning on our 3D visual features. (p. 3, III. METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
