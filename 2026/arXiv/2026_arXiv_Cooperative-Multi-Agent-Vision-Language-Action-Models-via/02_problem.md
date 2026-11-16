# Problem — Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

단일 로봇 사전학습 VLA에 협력 기술을 부여하고 시연 이상의 성능으로 개선한다.

## Robotics Loop

각 agent wrist RGB·proprio + 모든 agent가 공유하는 third-person RGB·지시 → 개별 action.

## Assumptions to Check — Researcher Interpretation

연구자 점검: 팀 전체 성공과 agent별 credit 추정을 동일시하지 않는다.

개념 연결: CHORUS·latent-space RL → cooperative RFT → independent partner compatibility.

## Boundary

CHORUS의 local-only 입력과 같지 않다. 읽은 평가에서 독립 학습 partner 교체의 순수 효과는 분리되지 않는다. Anonymous code 링크는 논문에 있으나 실행·내용 확인은 미완료.

근거: [확인한 원문](https://arxiv.org/html/2609.36588v1), §4.2–4.3, §5, Appendix C.1.
