# Problem — Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

외관만 변할 때의 안정성과 실제 목표가 바뀔 때의 행동 전환을 구분한다.

## Robotics Loop

RGB·지시·기존 행동 → 작은 action residual; 선택적 보조 경로는 canonicalized 관측의 추가 policy query를 사용한다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: matched triplet의 목표 변경과 물리적 실행 가능성이 별도로 검증되어야 한다.

개념 연결: OpenVLA/π0.5 → ReSteer·How-level diagnosis → 부분 수정 평가. 직접 citation edge 확정 아님.

## Boundary

Break 열은 옛 목표 성공률이므로 낮다고 새 목표 성공이 아니다. Margin 분리만으로 물리적 성공이 보장되지 않는다. 최종 proceedings와 읽은 v1의 동일성·공개 구현은 미확인.

근거: [확인한 원문](https://arxiv.org/html/2609.23650v1), §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1.
