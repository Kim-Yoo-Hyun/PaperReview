# Problem — Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF의 abstract·introduction·problem/formulation 단락을 검토해 이 문제 formulation을 작성했다. tracker의 reading status/evidence는 이 migration에서 변경하지 않았다.

## Problem in One Sentence

point cloud에서 고정 label set에 없는 object와 관계까지 query 가능한 open-vocabulary 3D scene graph를 예측한다.

## System and Scope

- **Object / environment:** 3D scene/object와 robot coordinate frame
- **Observation / input:** RGB-D, image set, point cloud, depth와 camera pose
- **Latent state / decision variable:** geometry, map, object/relationship state
- **Output / action:** point map, pose, scene graph, affordance 또는 query result
- **Horizon / evaluation target:** geometric accuracy, semantic consistency와 planning/manipulation utility

## Formal Problem Formulation

- **State / model:** 3D scene을 object node와 directed relation edge로 표현하고, point-cloud geometry와 open-vocabulary semantic embedding을 사용해 node class와 spatial/supportive/semantic relation을 생성한다.
- **Objective / loss / cost:** object·relation prediction이 known class에 overfit되지 않으면서 graph query에 필요한 node identity와 edge consistency를 높인다.
- **Constraints / initial-boundary-terminal conditions:** point cloud segmentation/instance grouping이 안정적이고, open-vocabulary embedding과 relation predicate가 동일 scene coordinate에서 해석되어야 한다.
- **Success / guarantee:** scene-graph annotation 없이도 arbitrary object class와 open-set inter-object relationship을 복원해 planning·place recognition query를 지원하는 것이다.

## Bottleneck in Prior Work

기존 3D scene graph predictor는 labeled dataset과 fixed object/relation categories에 의존해 novel household object와 관계를 표현하지 못한다.

## What the Paper Changes

closed-set supervised graph prediction을 open-vocabulary point-cloud graph construction으로 바꾸고, queryable node/edge를 출력 대상으로 둔다.

## Assumptions and Failure Boundary

| Assumption | Why it is needed | Failure boundary |
|---|---|---|
| foundation semantic feature가 novel object/relation 의미를 보존 | open-set prediction을 위해 필요 | domain-specific geometry/contact relation은 semantic prior만으로 혼동 |
| point cloud가 object boundary와 relative geometry를 보존 | graph edge를 위해 필요 | occlusion·sparse scan은 missing node/edge |

## Position in the Robotics Loop

3D scan → object/relationship scene graph → language/spatial query → planning or perception decision다.

## Verification Questions

- **Evidence anchor:** 본문의 fixed-category 3D scene graph bottleneck, open-vocabulary node/edge prediction과 queryable graph formulation.
- **Still to verify:** equation 번호와 exact source location, 그리고 04_evaluation의 reported protocol과 연결되는지를 확인한다.
