# Problem — EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF의 abstract·introduction·problem/formulation 단락을 검토해 이 문제 formulation을 작성했다. tracker의 reading status/evidence는 이 migration에서 변경하지 않았다.

## Problem in One Sentence

agent가 탐색하는 동안 streaming image로 whole scene을 online reconstruct하면서 open-vocabulary semantic query를 거의 real-time으로 지원한다.

## System and Scope

- **Object / environment:** 3D scene/object와 robot coordinate frame
- **Observation / input:** RGB-D, image set, point cloud, depth와 camera pose
- **Latent state / decision variable:** geometry, map, object/relationship state
- **Output / action:** point map, pose, scene graph, affordance 또는 query result
- **Horizon / evaluation target:** geometric accuracy, semantic consistency와 planning/manipulation utility

## Formal Problem Formulation

- **State / model:** 300개 이상 streaming image와 pose를 입력으로 online sparse coefficient field가 3D Gaussians와 CLIP global codebook을 연결해 geometry, color와 semantic field를 갱신한다.
- **Objective / loss / cost:** novel-view/color/depth reconstruction과 2D·3D semantic segmentation/query consistency를 공동으로 높이며 frame-wise processing latency를 제한한다.
- **Constraints / initial-boundary-terminal conditions:** camera pose/stream alignment, incremental memory budget과 sparse semantic coefficients를 유지하면서 scene 전체를 누적해야 한다.
- **Success / guarantee:** scene exploration과 동시에 open-vocabulary 3DGS를 만들고 semantic segmentation·rendering·depth query를 downstream embodied task에 제공하는 것이다.

## Bottleneck in Prior Work

offline open-vocabulary 3DGS는 complete image set와 expensive optimization에 의존해 exploration 중 즉시 쓸 수 없고, pure 2D features는 spatial consistency가 약하다.

## What the Paper Changes

semantic 3D reconstruction을 offline post-processing이 아닌 online feed-forward embodied perception state로 reformulate한다.

## Assumptions and Failure Boundary

| Assumption | Why it is needed | Failure boundary |
|---|---|---|
| streaming view와 pose가 scene coverage를 빠르게 제공 | online reconstruction을 위해 필요 | long-tail unseen area와 pose drift는 holes/semantic misalignment |
| CLIP codebook이 robot query vocabulary를 cover | open-vocabulary indexing을 위해 필요 | fine-grained affordance·part relation은 부족 |

## Position in the Robotics Loop

streaming images/poses → online semantic 3DGS → open-vocabulary query/scene state → navigation or manipulation feedback다.

## Verification Questions

- **Evidence anchor:** 본문의 online whole-scene 3DGS, Online Sparse Coefficients Field+CLIP Global Codebook과 embodied perception objective.
- **Still to verify:** equation 번호와 exact source location, 그리고 04_evaluation의 reported protocol과 연결되는지를 확인한다.
