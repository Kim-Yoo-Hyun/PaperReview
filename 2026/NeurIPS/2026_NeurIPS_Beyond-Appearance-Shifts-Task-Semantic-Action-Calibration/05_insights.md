# Insights — Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

네 가지 쉬운 목표 교체에서 보정 정책은 800회 중 옛 목표를 한 번도 실행하지 않았지만, 그중 252회는 새 목표에도 도달하지 못했다. 지시 변경을 평가하려면 새 목표 달성, 옛 목표 실행, 기타 실패를 따로 집계할 필요가 있다. [저자판 v2 표 7](https://arxiv.org/pdf/2609.23650v2#page=10) · [실물 비교와 어려운 조건](./04_evaluation.md)

행동 보정 방식과 처음 검토한 절은 방법 노트에 정리했다. [방법](./03_method.md)

## Researcher interpretation

REVISION·FEEDBACK·residual 보정의 직접 충돌 선행. 변화에 반응하고 nuisance에 불변이라는 broad proposal의 재발명을 막는다.

개념 연결: OpenVLA/π0.5 → ReSteer·How-level diagnosis → 부분 수정 평가. 직접 citation edge 확정 아님.

- 취약 조건 점검: 연구자 점검: matched triplet의 목표 변경과 물리적 실행 가능성이 별도로 검증되어야 한다.
- 반증 가능한 질문: 다중 수정 이력에서 유지·철회 제약을 명시적으로 관리하는 이득이 완전 지시 재작성 이후에도 남는가?
- 최소 비교 제안: 같은 frozen policy에서 전체 이력 재작성·규칙 상태·정답 완전 지시를 대조하고 새 목표 성공과 옛 제약 위반을 공동 평가한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
