# Stable Language Guidance for Vision–Language–Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

시각 prior가 언어의 의도를 압도하고 표현 변화에 정책이 민감해지는 문제를 다룬다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

semantic prior 제거 방식·추가 decode 비용·paraphrase 정답 정보·평가 instruction 분리.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

시각 관측·언어 표현들의 분포 → 의미/affordance 분리 추론 → VLA 행동. 검색한 demo를 바꾸는 개입과 현재 지시를 바꾸는 개입은 다르다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://aclanthology.org/2026.acl-long.190/) · [저자 project](https://github.com/Doo-mon/RSS).
