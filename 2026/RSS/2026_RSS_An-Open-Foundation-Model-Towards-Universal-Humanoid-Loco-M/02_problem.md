# Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·공식 project/code 및 arXiv v1 §III–IV, Appendix IX–X의 지정 내용 확인. RSS 최종본문 전체 대조·사용자 정독·실험을 의미하지 않는다.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Target Problem

인간 영상의 손/손목 궤적과 humanoid의 관절·균형 제약을 하나의 학습 target으로 다루기 어렵다. 표현 학습과 로봇 제어 학습을 분리하는 것이 논문의 접근이다. [§III](https://arxiv.org/html/2603.12263v1#S3).

## Assumptions and Closed Loop

정렬된 관측·행동 데이터, 로봇별 변환, 유효한 하위 제어기가 필요하다. 실패가 의미 이해·action expert·하위 제어 중 어디에서 발생하는지 구분해야 한다.

## Formulation Boundary

단계별 supervised pre/post-training과 하위 RL 제어의 조합이다. 연구 해석상 end-to-end 배포 경로가 있다고 해서 VLA backbone까지 reward로 공동 갱신한 것은 아니다.
