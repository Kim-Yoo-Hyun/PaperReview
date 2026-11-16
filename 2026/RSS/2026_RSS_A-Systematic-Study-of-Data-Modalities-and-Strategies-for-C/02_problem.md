# A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

이종 데이터의 종류와 섞는 학습 단계가 로봇 일반화에 어떤 차이를 만드는지 체계적으로 검토한다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

modality별 token/compute 균형·학습 단계·동일 task split·negative result의 적용 범위.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

여러 modality의 supervision → 공통 VLA 학습 → 목표 로봇 조작. Test-time context 교체와 training-data 혼합은 구분한다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p007.html) · [저자 project](https://co-training-lbm.github.io/).
