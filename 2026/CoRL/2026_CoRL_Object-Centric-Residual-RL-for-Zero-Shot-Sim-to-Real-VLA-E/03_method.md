# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Policy and Learning Pipeline

Object pose·proprioception·base action을 residual 입력으로 사용하며, paired teleoperation을 통한 정렬과 simulation 학습을 결합한다.

## Observation, State, and Action

VLA의 base action과 물체 중심 상태 → 보정 행동 → 실제 조작. 학습에 사용하는 상태와 실제 배포에서 추정하는 상태를 구분해야 한다.

## Training versus Deployment

정렬된 object pose와 행동 표현이 residual 배포에 유효해야 한다. 센서 추가와 base 교체 효과를 혼동하지 않는다.

제어 주기·horizon·loss 계수 전체는 이번 노트에서 확정하지 않았다. 실제 baseline 이식 전 원문과 code 설정을 함께 대조한다.

근거: [지정 본문](https://arxiv.org/html/2606.18953v1) — §3.1–3.4/5.1–5.4/7, Appendix A.
