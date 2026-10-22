# USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

실제 robot online learning은 cheap reset·대규모 병렬화가 불가능하고 이기종 장비·통신·장기 학습 관리가 필요하다.

## Bottleneck and Changed Formulation

Robot/GPU 추상화, adaptive communication 및 persistent buffer를 갖춘 asynchronous learning system을 제안한다.

## System and Robotics Loop

Robot observation/action/reward stream ↔ edge/cloud rollout·training workers ↔ policy weight synchronization.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Weight version tagging, replay consistency, crash recovery와 실제 robot 시간 비용.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RSS abstract는 simulation과 실제 multi-robot·heterogeneous manipulator·edge-cloud·장기 비동기 학습 사례를 명시한다.

## Evidence Anchor

[공식 paper/abstract](https://roboticsproceedings.org/rss22/p037.html) · [저자 project/code](https://github.com/RLinf/RLinf/blob/main/docs/source-zh/rst_source/resources/release_v0.3.rst). Exact objective, constraints, success definition은 본문 수동 확인 필요.
