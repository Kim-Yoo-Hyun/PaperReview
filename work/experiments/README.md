# 실험 근거와 재개 범위

- Updated: 2026-10-23 KST

실행 당시 driver·raw evidence·source/hash·runtime manifest는 보존한다. 최신 실행 절차는 [Docker 재개 안내](./portable/README.md)를 사용한다. 과거 manifest의 절대 경로·컨테이너 이름을 새 컴퓨터의 현재 환경으로 취급하지 않는다.

| 실험/진단 | 실제 수행 범위 | 현재 재개 판단 |
|---|---|---|
| [초기 로봇 간 RL 전이](./vla_rl_cross_embodiment/RESULTS.md) | 기본 정책 qualification 실패; RL 대 imitation 전이 비교 미실행 | RETIRED. 핵심 결과만 보존하며 과거 실행 자산은 삭제됨 |
| [C1 native probe](./vla_rl_active_handoff/RESULTS.md) | SmolVLA strict load·LIBERO 243 control steps; 시간 예산 종료 | HOLD. 완결된 episode·base competence·active perception 효과 미확인 |
| [C2 첫 검증](./vla_rl_c2_first_pass/RESULTS.md) | 실제 데이터·경유 판정·의존성 probe | 현재 설계 NO-GO. 완전한 label/coverage·native runtime 미충족 |
| [C3 mechanism](./vla_rl_c3_interface/RESULTS.md) | Synthetic 분포·native decoder/loss의 수치 검사 | 메커니즘 근거. RL 업데이트 효과 아님 |
| [C3 실제 checkpoint](./vla_rl_c3_logits/RESULTS.md) | 실제 16개 관측·3 forward batch·head/autograd 진단 | 본격 학습 비추천. 저장 수치는 portable Docker에서 재분석 가능 |
| [D1 formulation](../research_candidates/2026-10-21_d1_buildup/RESULTS.md) | 합성 반례·Docker source 감사 | 관측 가능성과 보정 필요성 구별. Native VLA 효과 미검증 |
| [D1-E1 preflight](./vla_d1_e1_preflight/RESULTS.md) | Docker 자원·GPU allocation 실패·source/normalizer 감사 | G0 전체 미충족·G1 미실행. 자원 외 D1-R2 연구 gate도 미충족 |

D2/D3/E1/E2의 문헌·정적 데이터 감사는 [후보 요약](../research_candidates/summaries/README.md)에서 찾는다. 실행 계획 JSON의 존재는 native 실험 수행을 뜻하지 않는다. 현재 새 policy rollout·training을 즉시 재개할 자격을 갖춘 후보는 없다.

[C3 portable replay](./portable/README.md)는 checkpoint·dataset을 다시 다운로드하지 않고 저장 NPZ의 score/alias 지표를 재계산한다. 결과는 stdout으로 출력하며 기존 evidence를 덮어쓰지 않는다. 자동 삭제되는 container와 필요 시 제거할 전용 image를 사용한다. 다른 이미지·volume에는 손대지 않는다.

실험 결과로 사용자 읽기 상태·논문 tier를 자동 승격하지 않는다. 문헌 주장, 정적 source 경로, 수치 검사, 실제 closed-loop 효과를 서로 대체하지 않는다.
