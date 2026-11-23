# 시각 피드백

**현행 투자 판단 — 2026-11-17:** [유지 3개·예비 1개](../../README.md#candidate-priority) 중 **신뢰성·실패 원인의 문헌 탐색을 우선**한다. 기존 관측 지연 진단은 보존하되 새 monitor/복구 방법이 구현된 것으로 바꾸지 않는다. 공개 RL/SFT 차이는 학습 목적함수의 인과효과가 아니다. 추가한 [직접 선행·탐색 범위](#reliability-scout-2026)와 기존 P0의 수행 범위를 구분한다.

- Updated: 2026-11-06 KST
- 상태: **비교 진단 후보 유지; 최소 입출력 검증 준비, native 실행 미확인**. 내부 작업 ID는 FEEDBACK이다. 새 방법의 기여나 RL 효과가 입증된 상태가 아니다.
- [재현 방법](../재현%20방법/README.md) · [공통 선행·학습 계보·비교 계약](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/INTEGRATED_GAP_REVIEW_2026-11-05.md#integrated-n2) · [공통 source 원장의 integrated_n2_review](../../../sources/vla_rl_new_gap_scan_2026-11-05.json)

## 연구 질문과 기여 후보

작업 도중 물체가 움직이면 로봇은 새로운 영상을 활용해 행동을 수정해야 한다. VLA를 강화학습으로 후학습했을 때 나타나는 일반화 성능이 **새 시각 정보를 이용한 회복**, 기존 조작 능력, 배경 변화에 대한 불변성 중 무엇과 연결되는지 구분한다. 답을 얻으면 후학습 데이터와 평가 조건을 선택하는 근거가 된다.

질문은 “같은 정책에서 물리 변화 직후 한 번의 관측을 지연하면 성공에 어떤 영향이 생기며, 그 영향은 후학습 checkpoint 사이에서 어떻게 달라지는가?”다. 기여 후보는 정보 개입을 통한 행동 진단이다. 기존 방법에 RL이나 관측 선택기를 추가했다는 사실을 기여로 삼지 않는다.

## 선행이 해결한 것과 남은 비교

| 직접 근거 | 이미 다루는 것 | 이번에 좁힌 비교·해석 경계 |
|---|---|---|
| [RL4VLA 저자 v4 §3–5·A](https://arxiv.org/html/2505.19789v4) | VLA의 SFT/RL 후학습과 여러 일반화 조건 | 정책을 동결한 뒤 관측 가용성에 개입한다. 공개 RL/SFT는 데이터와 normalizer가 달라 목적함수만의 대조가 아님 |
| [BAS-VLA 저자판 v2, 표 5–7](https://arxiv.org/pdf/2609.23650v2#page=9) | 무관한 변화에서의 행동 유지, 목표·공간 관계 변경 후 새 과제 성공 | 이 후보는 물체 이동 직후 한 관측을 지연했을 때의 회복 차이를 후학습 정책별로 비교한다 |
| [RobustVLA Algorithm 1](https://arxiv.org/html/2511.01331v2) | Reference policy 대비 행동 변화의 제약 | 낮은 시각 민감도를 좋은 회복으로 간주하지 않음. 행동 차이와 실제 성공을 분리 |

위 source와 공개 code의 확인 범위·hash는 공통 원장에 보존한다. 읽은 절에서 좁은 비교를 확인하지 못했다는 뜻이며 문헌 전체에서 부재를 입증한 것은 아니다. 사용자 읽기 상태는 변경하지 않았다.

## 주장과 필요한 증거

Checkpoint `m`의 고정 deadline 성공률을 `Y_m(p,v)`로 둔다. `p`는 물리 변화 유무, `v`는 fresh 영상 또는 **한 query만 직전 영상으로 대체**하는 stale 조건이다.

`I_m = [Y_m(1,F) − Y_m(1,S)] − [Y_m(0,F) − Y_m(0,S)]`

이 상호작용은 정상 조건의 지연 손실을 제외한 추가 관측 가치를 나타내는 설계다. 네 조건의 성공률과 완료 시간을 함께 봐야 한다. 큰 값은 fresh에서 잘 회복하거나 stale에서 크게 실패한 결과일 수 있다. 전체 RGB 지연은 로봇 자세 정보도 늦추므로 물체 위치 정보만의 효과라고 해석하지 않는다.

`I_RL − I_SFT`는 공개 checkpoint 간 연관이다. **RL 목적함수의 인과효과**를 주장하려면 공통 초기 weights·학습 데이터·normalizer·augmentation·update 예산과 성공 데이터 선택/return-weighted imitation 대조가 별도로 필요하다. 현재 공개 weights만으로 충족하지 못한다. Native normalizer를 임의 통일하는 것도 공정한 대조가 아니다.

이번 P0는 RL checkpoint 하나의 동일한 post-event 물리 상태에서 stale/fresh/repeat-fresh 입력을 질의한다. 측정 대상은 행동 반응성, 반복성, 관측 시각과 명령 형식이다. **성공률·위 상호작용·SFT 대조·기본 조작 능력은 측정하지 않는다.** 전체 상태 분기 복원도 아직 구현·교정하지 않았다. 관측 이미지의 행동 차이만으로 유용한 회복이라고 주장하지 않는다.

## 비실험 buildup 상태

기준은 [7단계 비실험 절차](../../../../research/RESEARCH_GUIDE.md#nonexperimental-workflow)다.

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

<a id="reliability-scout-2026"></a>

## 신뢰성·실패 원인·복구로 연결하는 탐색 — 2026-11-17

사용자가 강조한 VLA + RL + Computer Vision + Robotics에 맞춰 기존 시각 피드백 진단을 새 문제의 출발점으로 남긴다. **아래는 문헌 기반 탐색 가설이며 기존 FEEDBACK 실험의 완료나 새 독립 방법의 확정이 아니다.** 실패를 예측하는 점수, 실패 원인을 설명하는 분류, 현재 상태에서 특정 복구 행동이 도움이 될 가능성은 서로 다른 대상이다. 이를 분리했다는 사실만으로 새 기여가 생기지는 않는다.

### 직접 선행이 이미 다룬 것

| 근거·확인 범위 | 이미 제공하는 것 | 새 질문에서 조심할 경계 |
|---|---|---|
| [Sentinel, CoRL 2024](https://proceedings.mlr.press/v270/agia25a.html), 공식 초록 | 생성 정책의 시간적 행동 일관성과 task progress를 이용한 runtime monitoring | 일반 실패 탐지·진행 감시를 공백으로 주장하지 않음. Proceedings 발행 연도 2025와 개최 연도 구분 |
| [SAFE, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html), 공식 초록 | VLA 내부 특징으로 실패 위험을 탐지하고 conformal 절차로 판단 | Hidden-state probe+calibration 자체는 신규성이 아님. 오류 원인의 인과적 식별과는 다름 |
| [AHA, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/70a06501001e1820fd1eb9ee821302d2-Abstract-Conference.html), 공식 초록 | 로봇 실패 설명과 합성 실패 데이터, 계획·검증·보상 활용 | 실패를 설명해 RL/recovery에 쓰는 일반 연결도 기존 연구에 있음 |
| [FAIL-Detect, RSS 2025](https://www.roboticsproceedings.org/rss21/p073.html), 공식 초록 | 성공 데이터에서 불확실성 기반 실패 탐지 | 실패 데이터 없이 탐지한다는 주장만으로 차별화 불가 |
| [SFF, arXiv 2026](https://arxiv.org/html/2611.11688v1), 초록·§3–4·§7 및 관련 부록 | 배포 후 episode 결과로 head/threshold를 갱신하며 task·policy-version 변화와 개입을 평가 | 일반 정책 업데이트 후 재보정은 직접 중복. 실제 로봇 자료는 replay이며 live 실행이 아님. 조기 탐지는 비가역 실패 전 탐지와 같지 않음. 부록에 stopped/censored label 검토도 있어 이를 모두 미해결로 쓰지 않음 |
| [SAFECAST](https://arxiv.org/abs/2608.04246)·[VLA-Tug](https://arxiv.org/abs/2611.08425), arXiv 2026 초록 | 배포 변화에서 위험 보정, 잠재 특징의 실패 예측·유형 분류 | 단순 OOD probe나 failure-type classifier 추가를 독립 기여로 삼지 않음. 본문·code 대조는 다음 단계 |
| [AHEAD, arXiv 2026 §6.1](https://arxiv.org/html/2606.02486v1), 지정 한계 절 | Optical-flow 조건의 미래 latent로 동적 조작을 보완 | 단일 motion 추정의 불확실성 전파·명시적 깊이·충돌 후 운동이 한계로 제시됨. 3D/uncertainty/RL 조합 전체의 부재를 뜻하지 않음 |
| [B2FF, arXiv 2026 §5](https://arxiv.org/html/2606.09258v1), 지정 한계 절 | 미리 생성한 milestone을 선택하는 VLA 실패 복구 | 관측·도달 가능하고 기본 skill이 있는 회복 가능한 이탈 범위. 잘못된 grounding·심한 지각 실패·사라진 물체·비가역 변화까지 해결한 것으로 일반화하지 않음 |

2026 preprint들의 본 학회 게재는 이번 확인 범위에서 검증하지 못했다. SFF의 workshop 표기를 CoRL 본 학회로 승격하지 않는다. [No Free Checker](https://arxiv.org/abs/2609.09250)는 verifier의 판단 비용·시점·신뢰도 용어를 정리하는 survey로만 사용하며 공백의 부재/존재를 입증하는 근거로 쓰지 않는다. 확인 범위와 이전 dossier 근거의 구별은 [원장](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/sources/candidate_triage_2026-11-17.json)이 소유한다.

### 먼저 확인할 연구 질문

1. **실패 원인과 유용한 개입의 관계 — 우선 문헌 대조.** 같은 물리 상태에서 시각 추정을 갱신하면 회복되는 오류와, 올바른 관측을 주어도 정책이 실행하지 못하는 오류를 구별할 수 있는가? 이 구별이 같은 비용의 재관측·고정 재시도·재계획보다 최종 성공과 안전한 중단에 유용한가? AHA의 설명과 B2FF의 복구 범위를 넘는 차이가 있는지 먼저 확인한다. Pose estimator를 쓰지 않는 VLA에 인위적으로 pose bottleneck을 넣지 않는다.
2. **시각 운동 추정의 불확실성과 행동 위험 — 예비 연결.** Occlusion/깊이/추적 모호성이 미래 예측과 행동 오차에 어떻게 전달되는가? 단일 optical flow의 오차와 world model의 불확실성을 분리해 추정했을 때 단순 재관측이나 속도 제한보다 유용한 행동 결정을 만드는가? AHEAD의 한계가 출발점이지만 동적 로봇·state ground truth·calibration 부담이 커 후속으로 둔다. 영상 예측 오차 감소만을 로봇 기여로 세지 않는다.
3. **RL 업데이트 후 monitor 변화 — 대조 항목.** SFF/SAFECAST/VLA-Tug가 직접 경쟁 연구다. 일반 online recalibration을 새 방법으로 선택하지 않는다. 위험 순위·false alarm·실제 복구 가능 시점·개입 후 성공을 구분하고 무엇이 이미 평가됐는지 확인한다.

현재는 **1번을 선택해 본문·공개 interface를 추가 대조할 가치가 있다**는 판단이다. 새로운 틈이 확정됐다는 뜻은 아니다. RL은 결국 로봇 행동을 개선하는 학습 대상·신호·비교군으로 구체화해야 하며 monitor 뒤에 붙였다는 이유만으로 기여를 주장하지 않는다. 신뢰성 분석 결과만으로도 중요한 지식이 남는다면 그 기여를 별도로 평가한다.

### 기존 설계와의 연결·남은 확인

기존 fresh/stale 실험은 새 영상의 **정보 가치**를 보는 작은 진단이다. 전체 RGB 지연은 물체 정보뿐 아니라 로봇 자세·카메라 정보까지 늦춘다. 따라서 이를 그대로 순수 perception failure와 policy failure의 원인 분해라고 부를 수 없다. 새 주장에는 동일 상태 분기·관측/추정만의 개입·올바른 관측 하의 기본 능력 대조가 필요하며 아직 구현하지 않았다. 정답 상태는 진단 상한용으로만 사용하고 실제 정책에 허용되는 입력과 구별한다.

다음 산출물은 기존 이 절 안에 **가까운 선행 3–5편의 입력·예측 대상·개입·평가 범위 비교, 하나의 구별 가능한 질문, 강한 단순 대안, 작은 로봇 사례**를 보완하는 것이다. 과거 D1의 관측 가능성/보정 필요성 NO-GO를 단어만 바꾸어 재개하지 않는다. 새 사례에서 기존 결론과 무엇이 다른지 설명하지 못하면 질문을 수정하거나 종료한다. 기존 FEEDBACK P0·Docker 상한·runtime 파일은 이번 정리로 변경하지 않았으며 실제 실험은 수행하지 않았다.
