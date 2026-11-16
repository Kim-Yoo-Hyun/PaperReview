# 강화학습 후학습과 시각 피드백 활용

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)의 보조 진단·독립 분석 예비다. 동결 정책으로 시작할 수 있다는 장점은 있지만 공개 RL/SFT 차이만으로 학습 목적함수의 인과효과를 말할 수 없다. UNIFIED에 참고할 평가 원리는 있어도 동일 연구·동일 adapter로 합치지 않는다.

- Updated: 2026-11-06 KST
- 상태: **비교 진단 후보 유지; 최소 입출력 검증 준비, native 실행 미확인**. 내부 작업 ID는 FEEDBACK이다. 새 방법의 기여나 RL 효과가 입증된 상태가 아니다.
- [재현 방법](../재현%20방법/README.md) · [공통 선행·학습 계보·비교 계약](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md#integrated-n2) · [공통 source 원장의 integrated_n2_review](../../../sources/vla_rl_new_gap_scan_2026-11-05.json)

## 연구 질문과 기여 후보

작업 도중 물체가 움직이면 로봇은 새로운 영상을 활용해 행동을 수정해야 한다. VLA를 강화학습으로 후학습했을 때 나타나는 일반화 성능이 **새 시각 정보를 이용한 회복**, 기존 조작 능력, 배경 변화에 대한 불변성 중 무엇과 연결되는지 구분한다. 답을 얻으면 후학습 데이터와 평가 조건을 선택하는 근거가 된다.

질문은 “같은 정책에서 물리 변화 직후 한 번의 관측을 지연하면 성공에 어떤 영향이 생기며, 그 영향은 후학습 checkpoint 사이에서 어떻게 달라지는가?”다. 기여 후보는 정보 개입을 통한 행동 진단이다. 기존 방법에 RL이나 관측 선택기를 추가했다는 사실을 기여로 삼지 않는다.

## 선행이 해결한 것과 남은 비교

| 직접 근거 | 이미 다루는 것 | 이번에 좁힌 비교·해석 경계 |
|---|---|---|
| [RL4VLA 저자 v4 §3–5·A](https://arxiv.org/html/2505.19789v4) | VLA의 SFT/RL 후학습과 여러 일반화 조건 | 정책을 동결한 뒤 관측 가용성에 개입한다. 공개 RL/SFT는 데이터와 normalizer가 달라 목적함수만의 대조가 아님 |
| [BAS-VLA §4–5·A.2.1](https://arxiv.org/html/2609.23650v1) | 무관한 변화의 불변성과 의미 변화에 대한 행동 수정 | “변화에 반응한다”는 넓은 동기는 중복. 학습 계보별 정보 개입의 효과로 한정 |
| [RobustVLA Algorithm 1](https://arxiv.org/html/2511.01331v2) | Reference policy 대비 행동 변화의 제약 | 낮은 시각 민감도를 좋은 회복으로 간주하지 않음. 행동 차이와 실제 성공을 분리 |

위 source와 공개 code의 확인 범위·hash는 공통 원장에 보존한다. 읽은 절에서 좁은 비교를 확인하지 못했다는 뜻이며 문헌 전체에서 부재를 입증한 것은 아니다. 사용자 읽기 상태는 변경하지 않았다.

## 주장과 필요한 증거

Checkpoint `m`의 고정 deadline 성공률을 `Y_m(p,v)`로 둔다. `p`는 물리 변화 유무, `v`는 fresh 영상 또는 **한 query만 직전 영상으로 대체**하는 stale 조건이다.

`I_m = [Y_m(1,F) − Y_m(1,S)] − [Y_m(0,F) − Y_m(0,S)]`

이 상호작용은 정상 조건의 지연 손실을 제외한 추가 관측 가치를 나타내는 설계다. 네 조건의 성공률과 완료 시간을 함께 봐야 한다. 큰 값은 fresh에서 잘 회복하거나 stale에서 크게 실패한 결과일 수 있다. 전체 RGB 지연은 로봇 자세 정보도 늦추므로 물체 위치 정보만의 효과라고 해석하지 않는다.

`I_RL − I_SFT`는 공개 checkpoint 간 연관이다. **RL 목적함수의 인과효과**를 주장하려면 공통 초기 weights·학습 데이터·normalizer·augmentation·update 예산과 성공 데이터 선택/return-weighted imitation 대조가 별도로 필요하다. 현재 공개 weights만으로 충족하지 못한다. Native normalizer를 임의 통일하는 것도 공정한 대조가 아니다.

이번 P0는 RL checkpoint 하나의 동일한 post-event 물리 상태에서 stale/fresh/repeat-fresh 입력을 질의한다. 측정 대상은 행동 반응성, 반복성, 관측 시각과 명령 형식이다. **성공률·위 상호작용·SFT 대조·기본 조작 능력은 측정하지 않는다.** 전체 상태 분기 복원도 아직 구현·교정하지 않았다. 관측 이미지의 행동 차이만으로 유용한 회복이라고 주장하지 않는다.

## 비실험 buildup 상태

기준은 [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)다.

| 단계 | 현재 확보한 내용 | 남은 증거 |
|---|---|---|
| 1. 문제와 독자 | 물리 변화 후 정보 활용과 후학습 평가의 결정 연결 | 실제 배포 빈도·영향 크기는 미측정 |
| 2. 가까운 선행 | 위 본문·공개 source·checkpoint 계보 검토 | 전체 release/학습 run의 동등성 미확인 |
| 3. 질문과 대안 | Clean competence, nuisance augmentation, 데이터 선택, normalizer 차이 분리 | 무엇이 현상을 설명하는지는 실험 필요 |
| 4. 짧은 논문 이야기 | 정보 개입 기반 행동 진단의 기여 가설과 주장 경계 | 결과·독립 출판 가치는 미확인 |
| 5. 최소 비교 설계 | Four-cell 후속 설계와 그 전 단계인 bounded IO 계약 | 실제 분기 복원·rollout 비교·독립 task/seed 미실행 |
| 6. 실행 부담 | Code/weight/asset pin, Docker recipe·adapter 초안, CPU 제어 검사 9개 | NVIDIA build/전체 dependency closure·CUDA/Vulkan·native IO 교정; 공수 미정 |
| 7. 외부 비판과 반복 | 아래 검토 질문 준비 | 독립 연구자 응답 미수신; 내부 검토까지만 완료 |

외부 검토 질문은 “기존 RL 일반화 평가와 구별되는 정보 개입이 유용한가?”, “공통 상태 생성 정책과 task phase 편향을 어떻게 제한할 것인가?”, “어떤 결과가 단순 능력 차이보다 강한 설명을 요구하는가?”다. 외부에 메시지를 발송하지 않았다. 미수신은 작은 탐색의 금지 조건이 아니다.

## 결과별 다음 판단과 비용

- IO 실패: dependency·loader·renderer·관측 순서를 수정한다. 연구 질문을 반증한 것으로 기록하지 않는다.
- 반복 fresh 출력 불일치: 먼저 decode 재현성을 교정한다. 관측 민감도와 stochastic variation을 섞지 않는다.
- Fresh/stale 명령 차이 없음: 해당 한 상태의 무반응을 기록한다. 긍정 결과를 얻으려고 task·변화 크기·query 수를 자동으로 늘리지 않는다.
- 차이 있음: 반응성만 기록한다. 같은 상태에서의 네 조건 분기와 기본 능력을 검증한 뒤 회복 효과를 판단한다.
- 후속에서 clean 능력·augmentation·동일 데이터 모방이 충분히 설명: RL 전용 방법 주장을 줄인다. 남는 반복 가능한 차이가 있으면 별도 task/seed·matched-data 대조로 확장한다.

첫 구현 산출물은 [P0 trace 명세](../재현%20방법/RESUME_PLAN.json)다. 실제 비용은 reset·model query·control step·physics step을 분리한다. 준비 build/download 시간과 평가 실행 시간을 합쳐 숨기지 않는다. P0 상한은 **reset 2, query 3, control 6, event 1, physics 2,000**이며 학습은 없다. Native 실행이 가능해진 첫 점검에서 관측/행동 연결을 판단하고, 그 결과 없이 전체 비교 구현을 계속 늘리지 않는다.

VRL을 주 탐색으로 두었던 11/05 권고는 당시 이력이며 현행 선택은 상단의 전체 후보 비교를 따른다. FEEDBACK과 VRL은 robot·action·control rate가 달라 adapter와 경험 데이터를 직접 공유하지 않는다. 과거 C1·D1의 보류 판단을 자동 해제하지 않는다. 현재 결론은 **작은 비교 진단을 수행할 이유는 있으나, 독립 방법 연구나 top-tier 논문 기여로 확정할 증거는 아직 부족하다**는 것이다.
