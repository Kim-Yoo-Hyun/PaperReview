# Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

검색한 경험을 조건으로 residual action을 내는 EFN을 RL로 학습하고, 배포 중 성공 trajectory를 경험 bank에 추가한다.

현재 관측·지시·검색 경험과 base VLA action → EFN 보정 → 실행. Base parameter 고정이 전체 시스템 무학습을 뜻하지 않는다.

## Training vs Inference

EFN 학습/배포 갱신 경계·success-only bank 편향·task filter·residual 없는 대안·동일 경험 예산을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) · [저자 project](https://dejavu2025.github.io/).
