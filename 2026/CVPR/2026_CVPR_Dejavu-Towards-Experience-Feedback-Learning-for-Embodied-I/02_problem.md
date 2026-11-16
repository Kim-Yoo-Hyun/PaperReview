# Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

고정 VLA가 배포 후 쌓이는 경험을 행동 개선에 사용하는 경로를 다룬다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

EFN 학습/배포 갱신 경계·success-only bank 편향·task filter·residual 없는 대안·동일 경험 예산.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

현재 관측·지시·검색 경험과 base VLA action → EFN 보정 → 실행. Base parameter 고정이 전체 시스템 무학습을 뜻하지 않는다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) · [저자 project](https://dejavu2025.github.io/).
