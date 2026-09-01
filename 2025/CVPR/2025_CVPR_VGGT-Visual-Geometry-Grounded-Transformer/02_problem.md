# Problem — VGGT: Visual Geometry Grounded Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: source PDF의 abstract·introduction·problem/formulation 단락을 검토해 이 문제 formulation을 작성했다. tracker의 reading status/evidence는 이 migration에서 변경하지 않았다.

## Problem in One Sentence

여러 장의 scene images에서 별도 iterative geometric optimization 없이 camera, depth, point map과 point track 등 3D attributes를 feed-forward로 추정한다.

## System and Scope

- **Object / environment:** 3D scene/object와 robot coordinate frame
- **Observation / input:** RGB-D, image set, point cloud, depth와 camera pose
- **Latent state / decision variable:** geometry, map, object/relationship state
- **Output / action:** point map, pose, scene graph, affordance 또는 query result
- **Horizon / evaluation target:** geometric accuracy, semantic consistency와 planning/manipulation utility

## Formal Problem Formulation

- **State / model:** image set를 sequence/tokens로 입력한 Transformer가 모든 view에 대한 camera parameters, dense point maps/depth와 cross-view tracks를 공동 출력한다.
- **Objective / loss / cost:** multi-view geometric supervision에서 camera/point/depth/track prediction error를 공동으로 최소화한다.
- **Constraints / initial-boundary-terminal conditions:** 입력 images가 충분한 overlap과 공통 scene geometry를 갖고 camera/projective ambiguity를 학습된 convention으로 해소해야 한다.
- **Success / guarantee:** 수백 image까지 한 번에 처리하며 camera estimation, depth, dense reconstruction과 tracking에서 usable한 metric geometry를 제공하는 것이다.

## Bottleneck in Prior Work

pairwise reconstruction은 image 수가 늘면 post-processing/fusion과 optimization이 필요하고, classical bundle adjustment는 latency가 크다.

## What the Paper Changes

3D-inductive optimization pipeline을 large feed-forward Transformer의 joint multi-view prediction으로 reformulate한다.

## Assumptions and Failure Boundary

| Assumption | Why it is needed | Failure boundary |
|---|---|---|
| training 3D data가 deployment camera/scene distribution을 충분히 cover | metric geometry generalization을 위해 필요 | domain shift·dynamic object는 inconsistent map |
| single forward pass의 correspondence가 geometry ambiguity를 해소 | post-processing 제거를 위해 필요 | textureless/repetitive scene은 scale/pose ambiguity |

## Position in the Robotics Loop

multi-view images → camera/point/depth/track state → mapping, localization or collision-aware planning다.

## Verification Questions

- **Evidence anchor:** 본문의 feed-forward multi-image input, camera·point map·depth·track joint output과 optimization-free 3D task formulation.
- **Still to verify:** equation 번호와 exact source location, 그리고 04_evaluation의 reported protocol과 연결되는지를 확인한다.
