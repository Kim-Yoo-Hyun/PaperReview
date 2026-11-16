# Method — Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

실패 초기조건 중심 데이터 수집, agent별 positive-advantage filtering, 동결 VLA의 latent-noise RL을 순차 적용한다.

## Observation, State and Action

각 agent wrist RGB·proprio + 모든 agent가 공유하는 third-person RGB·지시 → 개별 action.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.36588v1), §4.2–4.3, §5, Appendix C.1.
