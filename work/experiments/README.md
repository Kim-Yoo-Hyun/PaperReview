# 실험 근거와 재개 범위

- Updated: 2026-11-06 KST

현재 8개 주제의 준비·실제 실행/미구현 상태는 [주제별 `내용/`·`재현 방법/`](../research_topics/README.md)에 통합했다. UNIFIED는 P0 실행 코드·recipe를 작성했고 실제 native build·IO/gradient 검증을 기다린다. 이 디렉토리는 과거 실행 근거를 보존한다. 아래 새 준비 2개와 기존 3개 정책 준비는 연구 효과가 확인된 실험 수를 뜻하지 않는다.

실행 당시 driver·raw evidence·source/hash·runtime manifest는 보존한다. C3는 [portable replay](./portable/README.md), GAP-P3는 [계약 검사 재개 안내](./reactive_nav_contract/README.md)를 사용한다. 과거 manifest의 절대 경로·컨테이너 이름을 새 컴퓨터의 현재 환경으로 취급하지 않는다.

| 실험/진단 | 실제 수행 범위 | 현재 재개 판단 |
|---|---|---|
| [FEEDBACK P0 준비](../research_topics/visual_feedback/재현%20방법/README.md#resume) | 11/06 local Mac ARM 조건에서 exit 3, Docker CPU 제어 검사 9개 통과; native 실행 0 | 단일 모델·reset 2·query 3·control 6·physics 2,000 이내 IO 초안. 호환 NVIDIA build/closure·CUDA/Vulkan·실제 IO·상태 분기 교정 대기 |
| [VRL P0 준비](../research_topics/vla_residual_update/재현%20방법/README.md#resume) | 11/05 local Mac ARM 조건에서 exit 3, Docker CPU 제어 검사 9개 통과; native 실행 0 | A/B 2 queries·warmup 포함 36 env steps 이내 IO 초안. Native image/IO·residual 학습·효과는 미확인 |
| [물체 집합·수량 P0 준비](../research_topics/object_set/재현%20방법/README.md#execution) | 2026-11-01 local Docker ARM64·GPU allocation 실패(exit 125), launcher 차단 확인. Native 실행 0 | 새 미빌드 packet. 공개 π0/config·normalizer·seen-category dev 고정, Docker recipe·bounded adapter 작성. 호환 환경에서 1 rollout·최대 200 control step/40 inference. Image/dependency·asset·CUDA/EGL·native 능력은 미확인; 집합/수량 task와 효과 비교 미구현 |
| [지시 전환 P0 준비](../research_topics/instruction_revision/재현%20방법/README.md#execution) | 2026-10-31 Docker ARM64·GPU allocation 실패(exit 125), portable launcher 차단 확인. Native 정책 실행 0 | 기존 REVISION/HANDOFF/SET 묶음 내 우선. 고정 source/checkpoint·Dockerfile·R8 단일 IO probe 작성, image 미빌드. 호환 컴퓨터에서 단계별 실행 후 실제 runtime manifest 확보. R1/R4 제약 observer·paired branch·H/S updater 미구현 |
| [HANDOFF P0 준비](../research_topics/mobile_policy_transfer/재현%20방법/README.md#execution) | 2026-10-28 Docker ARM64·GPU allocation 실패와 resource script 점검. Native 정책 실행 0 | 자원 대기 보존. 호환 로컬 Docker에서 check → gpu 후 sim/server 환경·transport/handoff adapter를 완성해 최소 IO/1 dev 확인. Image·adapter·최종 split/seed/runtime manifest 미완료 |
| [GAP-N3-A 관측 정보 계약](./proxy_observation_contract/README.md) | ARM64 Docker source/합성 계약 17/17, 수정 patch 적용/hash 확인. Native·VLA·학습 0 | 계약 재실행 가능. 전체 N3 PARTIAL; N3-B native qualification은 local Docker 자원 대기. [환경 설정](./proxy_observation_contract/ENVIRONMENT.md) 작성 완료, native image/실제 데이터/model adapter·연구 gate 미충족 |
| [GAP-P3 reactive navigation](./reactive_nav_contract/RESULTS.md) | ARM64 Docker CPU 계약 13/13·3개 scene/150 tick, 저장 trace 시간/ID/FIFO 재결합 | 계약 검사 재실행 가능. 후속 bounded 비교는 GAP-P4로 완료; native VLA HOLD |
| [GAP-P4 bounded navigation](./reactive_nav_pilot/RESULTS.md) | Dev12/cal24/test12·384 branch·192 paired prefix. 주 가설 joint gate 실패·저장 trace 검증 PASS | 현재 진단 HOLD·일반 방법 NO-GO·native VLA HOLD. [Docker 저장 결과 재분석](./reactive_nav_pilot/README.md) 가능; 추가 rollout/학습은 새 조건 예측 전 보류 |
| [초기 로봇 간 RL 전이](./vla_rl_cross_embodiment/RESULTS.md) | 기본 정책 qualification 실패; RL 대 imitation 전이 비교 미실행 | RETIRED. 핵심 결과만 보존하며 과거 실행 자산은 삭제됨 |
| [C1 native probe](./vla_rl_active_handoff/RESULTS.md) | SmolVLA strict load·LIBERO 243 control steps; 시간 예산 종료 | HOLD. 완결된 episode·base competence·active perception 효과 미확인 |
| [C2 첫 검증](./vla_rl_c2_first_pass/RESULTS.md) | 실제 데이터·경유 판정·의존성 probe | 현재 설계 NO-GO. 완전한 label/coverage·native runtime 미충족 |
| [C3 mechanism](./vla_rl_c3_interface/RESULTS.md) | Synthetic 분포·native decoder/loss의 수치 검사 | 메커니즘 근거. RL 업데이트 효과 아님 |
| [C3 실제 checkpoint](./vla_rl_c3_logits/RESULTS.md) | 실제 16개 관측·3 forward batch·head/autograd 진단 | 본격 학습 비추천. 저장 수치는 portable Docker에서 재분석 가능 |
| [D1 formulation](../research_candidates/2026-10-21_d1_buildup/RESULTS.md) | 합성 반례·Docker source 감사 | 관측 가능성과 보정 필요성 구별. Native VLA 효과 미검증 |
| [D1-E1 preflight](./vla_d1_e1_preflight/RESULTS.md) | Docker 자원·GPU allocation 실패·source/normalizer 감사 | G0 전체 미충족·G1 미실행. 자원 외 D1-R2 연구 gate도 미충족 |

D2/D3/E1/E2의 문헌·정적 데이터 감사는 [후보 요약](../research_candidates/summaries/README.md)에서 찾는다. 실행 계획 JSON의 존재는 native 실험 수행을 뜻하지 않는다. Native VLA rollout·training의 기존 재개 gate는 유지하며, GAP-P3의 상태 기반 계약 검사와 후속 bounded pilot은 별도 범위다.

[C3 portable replay](./portable/README.md)는 checkpoint·dataset을 다시 다운로드하지 않고 저장 NPZ의 score/alias 지표를 재계산한다. 결과는 stdout으로 출력하며 기존 evidence를 덮어쓰지 않는다. 자동 삭제되는 container와 필요 시 제거할 전용 image를 사용한다. 다른 이미지·volume에는 손대지 않는다.

실험 결과로 사용자 읽기 상태·논문 tier를 자동 승격하지 않는다. 문헌 주장, 정적 source 경로, 수치 검사, 실제 closed-loop 효과를 서로 대체하지 않는다.
