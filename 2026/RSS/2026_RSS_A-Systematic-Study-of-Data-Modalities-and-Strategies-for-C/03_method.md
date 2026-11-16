# A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

vision-language 자료·robot 언어 annotation·다른 embodiment 데이터·human video·이산 action token을 여러 co-training 전략으로 비교한다.

여러 modality의 supervision → 공통 VLA 학습 → 목표 로봇 조작. Test-time context 교체와 training-data 혼합은 구분한다.

## Training vs Inference

modality별 token/compute 균형·학습 단계·동일 task split·negative result의 적용 범위을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p007.html) · [저자 project](https://co-training-lbm.github.io/).
