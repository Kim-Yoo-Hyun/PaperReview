# Insights — Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

외관만 변할 때의 안정성과 실제 목표가 바뀔 때의 행동 전환을 구분한다.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.23650v1), §3–4, §5.1–5.3, Tables 6–7, Appendix A.2.1.

## Researcher interpretation

REVISION·FEEDBACK·residual 보정의 직접 충돌 선행. 변화에 반응하고 nuisance에 불변이라는 broad proposal의 재발명을 막는다.

개념 연결: OpenVLA/π0.5 → ReSteer·How-level diagnosis → 부분 수정 평가. 직접 citation edge 확정 아님.

- 취약 조건 점검: 연구자 점검: matched triplet의 목표 변경과 물리적 실행 가능성이 별도로 검증되어야 한다.
- 반증 가능한 질문: 다중 수정 이력에서 유지·철회 제약을 명시적으로 관리하는 이득이 완전 지시 재작성 이후에도 남는가?
- 최소 비교 제안: 같은 frozen policy에서 전체 이력 재작성·규칙 상태·정답 완전 지시를 대조하고 새 목표 성공과 옛 제약 위반을 공동 평가한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
