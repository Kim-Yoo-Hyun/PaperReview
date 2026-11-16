# Method — Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

동결 VLA 행동에 instruction-conditioned residual을 더한다. Clean/control 모방·일관성과 semantic-break margin을 함께 학습하고 preserving 보조 경로는 evidence gate로 제한한다.

## Observation, State and Action

RGB·지시·기존 행동 → 작은 action residual; 선택적 보조 경로는 canonicalized 관측의 추가 policy query를 사용한다.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.23650v1), §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1.
