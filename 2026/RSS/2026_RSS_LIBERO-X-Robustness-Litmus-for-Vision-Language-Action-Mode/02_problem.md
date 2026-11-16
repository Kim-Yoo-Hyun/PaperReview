# LIBERO-X: Robustness Litmus for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

단일 교란이나 균질한 장면만으로 평가하면 VLA의 공간·물체·지시 일반화 한계를 가릴 수 있다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

train/evaluation scene 중복·difficulty별 sample 수·실제 init state 공개 범위·predicate 정의.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

공간 배치·물체 속성·지시 표현을 바꾼 관측과 task → VLA 행동 → 다차원 label별 평가.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p097.html) · [저자 project](https://meituan.github.io/LIBERO-X/).
