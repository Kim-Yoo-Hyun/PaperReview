# GAP-N4 — 관측 정보가 다른 selector의 선택 효과를 어떻게 구별할 것인가

- 완료: **2026-10-26 KST, 비실험 buildup DONE**. 문헌의 지정 구간 대조·수작업 식 정리·비교 설계 심사다. Docker/GPU·simulation·정책 inference·학습·저장 결과 재분석은 수행하지 않았다.
- 판정: **일반 선택 방법 NO-GO 유지; 좁은 조건 진단 REVISE/HOLD.** 추가로 확인한 선행 때문에 단순 cue masking·진단값과 성능의 상관관계는 기여에서 제외한다. 현재 상태를 새 방법 개발 GO로 올리지 않는다.
- Canonical 질문은 [DATA-TRANSFER](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026), 앞선 설계는 [N1](./PROXY_OBSERVATION_CONTRACT_REVIEW_2026-10-25.md), 실행 계약은 [N3](./PROXY_OBSERVATION_REPAIR_REVIEW_2026-10-25.md)다. 이 문서는 **후속 연구 설계의 해석을 보정**하며 검증 당시의 N3 `PROTOCOL.json`·코드·결과를 변경하지 않는다.
- [출처·판정·보존 검사](../sources/proxy_selection_identifiability_review_2026-10-26.json). 개별 논문 전체 정독·사용자 reading status 승격이나 신규 registry 등록은 아니다.

## 1. 이번에 더 확인할 가치가 있었던 부분

N2/N3는 원본 identity·시간·입력·목표 binding을 다뤘다. 그것이 맞아도 **무엇을 원인으로 해석할지, 직접 선행과 무엇이 다른지, 선택 이득을 어떤 단위로 판단할지**는 남는다. 이번에는 이 세 부분을 심사했다. 아래 §2는 논문 근거, §3–8은 그 근거와 기존 계약을 바탕으로 한 연구자 분석이다. 실제 정책 효과는 미관측이다.

## 2. 직접 충돌과 비교 기준

| 출처와 확인 범위 | 확인한 내용 | 남길 수 있는 차이 / 제외할 주장 |
|---|---|---|
| **DataMIL**, ICLR 2026 [공식 proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html), 저자 [v2 §4.2–4.3, App. C.2·C.4–C.6](https://arxiv.org/html/2505.09603v2) | **C.2에서 선택과 최종 정책 학습 양쪽의 goal state를 가린다.** 선택 단위는 trajectory/subtrajectory이며, rollout 대신 target-demo loss를 쓴다. OXE 추정 시 target data를 분할하고, 최종 학습에는 target/selected data를 혼합한다. | “goal 없는 선택은 미연구”라는 주장은 사용할 수 없다. N1은 **selector만 cue 접근을 바꾸고 최종 target은 모두 같은 history를 받는 비교**로 제한한다. v2는 2026-06-19 저자본이며 conference camera-ready와 세부 동일성을 주장하지 않는다. |
| **From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection**, [arXiv:2610.29646v1](https://arxiv.org/abs/2610.29646), 2026-10-21. [§3–6, App. A·B·H·I 지정 구간](https://arxiv.org/html/2610.29646v1) | 같은 관측에서 goal을 바꾼 demonstrator 진단으로 corpus를 선택한다. 상관·예측·선택 이득을 구별하며, 주된 증분 선택 이득은 확립되지 않았다. 단위는 whole corpus이고 counterfactual demonstrator 접근이 필요하다. | 새로 확인한 **직접 진단 선행**. 단순 paired cue 검사나 “상관≠선택 가치”를 독립 기여로 재주장하지 않는다. 여기서 검토한 history-view selector 개입과는 대상이 다르다. 공식 학회 채택 및 공개 artifact URL은 이번 확인 범위에서 식별하지 못했으므로 **preprint**로만 사용한다. |
| **ReMix**, CoRL 2024 event / PMLR 2025 [공식 abstract](https://proceedings.mlr.press/v270/hejna25a.html) | 여러 domain의 sampling weight를 DRO로 조절하며 action 정규화·discretization·early stopping을 다룬다. | Domain mixture와 episode top-k는 선택 단위가 다르다. 가중치 방법을 같은 episode 수만으로 공정 비교했다고 쓰지 않는다. 이번에는 abstract 범위이며 본문·구현 재심사를 주장하지 않는다. |
| **CUPID**, CoRL 2025 [공식 abstract](https://proceedings.mlr.press/v305/agia25a.html), 이전 [W2 지정 본문/code 감사](./GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md) | Selection용 rollout의 expected return에 대한 demonstration influence를 사용한다. DP→π₀ 전이 확인은 W2의 근거를 재사용한다. | Target-demo loss를 쓰는 비교와 rollout·평가 접근 비용을 분리한다. 이번에는 공식 metadata/abstract 재확인이며 W2 전체 code를 재검사한 것은 아니다. |

DataMIL의 [공개 repository](https://github.com/UT-Austin-RobIn/datamil)와 ReMix의 [공개 repository](https://github.com/jhejna/remix)도 확인했다. 공개되어 있다는 사실을 현재 VLA adapter의 실행 가능성으로 바꾸지 않는다. 신규 preprint의 code 링크를 확보하지 못한 것은 그 논문이 없거나 반박되었다는 뜻도 아니다. **지정 구간에서 동일 비교를 찾지 못했다는 판단은 전 문헌의 부재 증명이 아니다.**

## 3. N1 비교식의 정확한 의미

기존 표기의 `S+`, `S−`, `Sctrl`은 각각 cue 유지, cue 제거, 같은 수의 다른 history frame 제거로 학습·평가된 selector가 반환한 subset이다. 모든 subset은 같은 원본 episode pool에서 고른다. 최종 learner `B+`의 입력은 **항상 원래의 full history**이고, 초기화·학습 recipe·평가 조건을 동일하게 둔다.

`J_v = J(B+ trained on S_v)`라 쓰면 N1에서 제안한 차이 비교는

```text
(J_plus − J_minus) − (J_plus − J_ctrl)
= J_ctrl − J_minus
```

이다. **Cue 유지 arm이 상쇄되므로 독립적인 2×2 interaction이 아니다.** 같은 수의 token 제거를 비교하는 유용한 contrast지만, `selector × target memory` interaction이나 memory의 인과 효과 전체로 부를 수 없다. 같은 `J_plus` 결과를 두 번 별도로 재표집해 불확실성을 부풀리지 않고 최종 paired contrast를 직접 계산해야 한다.

후속 설계에서 구별할 양은 다음과 같다.

| 양 | 해석 | 해석할 수 없는 것 |
|---|---|---|
| `Δcue = J_ctrl − J_minus` | 특정 cue 제거와 사전 지정한 다른 frame 제거의 **선택 절차 전체 차이** | Masked frame들이 정보량 외에 완전히 교환 가능하다는 보장 |
| `Δreuse = J_plus − J_minus` | Cue 접근을 맞춘 selector 대신 cue-hidden subset을 재사용했을 때의 차이 | 최적 subset에 대한 oracle regret, 항상 양수인 손실 |
| `Δsimple = J_plus − J_bal` | 단순 층화 대비 추가적인 선택 가치 | 테스트 결과를 보고 가장 유리한 baseline만 고르는 비교 |

`J_ctrl` 대 `J_minus`는 train/validation에서 각 view에 맞게 selector를 학습하는 **절차 개입**이다. Frozen model에 새로운 mask를 한 번 넣은 반응과 구별한다. Mask 위치·시점·남는 token·동률 처리·optimizer가 함께 동결되어야 하며, 원인을 순수한 “정보량” 한 변수로 단정하지 않는다. 무관 frame의 무관성도 현재는 설계 가정이다.

2×2 target-memory interaction을 정말 묻는다면 target도 cue-visible/hidden으로 나눈 네 셀과 별도 competence gate가 필요하다. 이는 현재 질문·비용을 넓히므로 이번 후속 계획에 추가하지 않는다.

## 4. 실험 전에 제거할 논리적 비약

**선택 순위가 달라도 선택 결과가 같을 수 있다.** Top-k 밖의 순위만 달라지거나 cutoff 근처 점수가 동률이면 `S−=Sctrl`일 수 있다. 같은 원본 데이터·순서·sampler·초기화 규칙으로 최종 B를 학습한다면 두 arm의 출력 분포는 같다. 따라서 먼저 선택 ID/weight가 실제로 달라지는지를 확인해야 한다. Rank correlation 감소 자체는 선택 효과의 근거가 아니다.

**정보가 필요한 작업이라고 정보 없는 selector가 반드시 나쁜 데이터를 고르지는 않는다.** N1의 대칭적인 제곱오차 반례를 유지한다. Action label은 selector 학습에 합법적인 감독 정보이며, hidden target 색을 입력에서 뺐다고 모든 label·학습 분포에서 그 관계가 사라지는 것은 아니다. Balanced tie-break와 coverage로 충분한 경우는 연구자의 실패가 아니라 이 가설의 범위를 줄이는 결과다.

**`1/3`은 현재 로봇 성공률의 이론적 상한이 아니다.** 숨은 정답 `C`가 세 위치에 균등하고, 결정 전 모든 입력 `U`와 독립이며, 출력 `f(U)`가 한 번의 세 가지 선택이라면

```text
P(f(U)=C) = Σ_j P(f(U)=j) P(C=j) = 1/3.
```

Abstention을 실패로 포함하면 `≤1/3`이다. 이는 수작업 확률 계산이고 측정 결과가 아니다. 이후 관측·접촉·탐색·재시도가 가능하거나 입력에 cue가 남으면 전제가 깨진다. N3의 **접근 구간 진입**은 되돌릴 수 있는 보조 event이므로 이 상한이나 “불가역 첫 선택” 해석을 적용하지 않는다. Primary outcome은 검증된 native task success로 남긴다.

## 5. 선택 데이터와 최종 학습 입력을 분리하는 계약

| 자료 역할 | 허용 접근 | 금지할 혼합 |
|---|---|---|
| Selection pool `D_pool` | 같은 원본 episode ID·action label. Selector별 view만 달리 생성 | Masked cache를 최종 B의 원본 history로 덮어쓰기 |
| Selector validation `D_val` | Pool과 다른 group. 해당 selector view로 점수·tuning 판단 | 최종 test 결과로 k·mask·LR·tie-break 선택 |
| 선택 결과 `S_v` | 원본 ID 목록 또는 명시적 weight. 원본 full-history를 다시 join | Selector용 view를 그대로 B에 전달해 target 관측까지 바꾸기 |
| 선택 외 target 지원 data `D_aux` | 필요할 때만 독립 group을 추가해 모든 arm에 같은 수·비율로 제공 | 한 arm에만 추가 target demo 제공; `D_val`을 조용히 합치기 |
| Final test `D_test` | 동결된 B의 평가만. 모든 mask/permutation/retry 자식은 원 group에 종속 | Test outcome을 보고 threshold·checkpoint·제외 규칙 변경 |

N1 초안의 12/4/8 group은 각각 pool/selector-validation/test의 **미수집 상한 초안**이다. `D_aux`가 필요한 recipe를 채택하면 새 독립 split과 비용을 명시해야 한다. 기존 4개 validation group을 재사용해 DataMIL의 co-training을 구현했다고 쓰지 않는다. 원 논문 recipe를 변경하면 `DataMIL-style adaptation`으로 표시하고 공식 재현과 구분한다. Selector의 training view와 validation view도 일치시킨다.

Split 단위와 selection 단위도 다르다. 같은 group의 세 permutation은 split을 넘지 않지만, episode를 개별 선택할 수도 있고 triplet을 통째로 선택할 수도 있다. 후자는 목표 위치 균형을 자동 보존해 검증하려던 coverage 손실을 제거할 수 있다. **주 비교는 episode 단위 선택으로 설계하고**, matched triplet selection은 coverage를 강제하는 단순 대안으로 구별한다. 아직 k·전체 성공/실패 pool 기준은 미동결이다.

## 6. 강한 baseline과 비용의 범위

첫 효과 비교의 최소 arm은 `S+ / S− / Sctrl / random / Sbal`이다. Target-only/all-data는 competence와 데이터 규모의 context이며 같은 k의 방법처럼 보고하지 않는다. 같은 초기화에서 full-history target을 학습한다. `Sbal`의 task·길이·관측 가능한 action strata와 **simulator 정답 위치를 쓰는 oracle balance**는 따로 이름을 둔다. 후자는 실패 원인 진단에는 유용하지만 모든 실제 corpus에서 배포 가능한 대안은 아니다.

다음 두 비교 목적을 섞지 않는다.

1. **기제 진단:** 선택 단위·k·최종 B의 update 수·유효 action/token 노출·target data 혼합·tuning 기회를 맞춘다. Episode 길이가 달라 같은 k와 같은 token 노출을 동시에 맞출 수 없다면 무엇을 고정했는지 밝히고 길이 층화/고정 window 대안을 사전에 택한다.
2. **총비용 가치:** `수집 + selector 학습/추정 + selection rollout + tuning + 최종 학습 + 평가`를 각각 기록한다. Random은 남는 선택 비용을 추가 학습에 쓸 수 있으므로 동일 총예산 비교는 별도다. Weighting은 unique episode·노출 횟수·유효 표본 크기를 함께 기록한다. GPU 시간만으로 사람/로봇 시간을 대체하지 않는다.

CUPID나 ReMix를 현재 fixture에 즉시 이식하지 않는다. 먼저 위의 단순 대안으로 질문이 남는지 본다. 논문 전체 방식과 맞는 adaptation을 만들 때에만 별도 baseline qualification이 필요하다. 현재는 어느 방법의 wall time·VRAM·유효 비용도 측정하지 않았으므로 절감률을 제시하지 않는다.

## 7. 분석 단위·기각 규칙·미결 필드

**통계 단위:** N1의 test 8 group×3 permutation은 24개의 독립 scene이 아니다. 목표 위치가 짝지어진 group 단위 성능과 paired arm 차이를 먼저 산출한다. 학습 seed는 모든 test group을 가로지르므로 frame/episode/seed를 단순 합쳐 표본 수로 쓰지 않는다. 단일 pool은 pool 간 일반화도 검증하지 않는다. Cluster 단위 불확실성 추정·독립 학습 반복 수·최소 의미 차이 `δ`는 아직 정해야 하며, 8 group으로 충분한 검정력을 확보했다고 쓰지 않는다.

**Outcome:** Native success를 primary로 유지한다. 접근 event·subset overlap·score correlation·coverage는 별도 보조 지표다. Timeout/실패를 성공자 조건부로 제외하지 않는다. 인프라 실패는 동결된 사유/재시도 규칙으로 별도 집계하고, 실제로 결과가 없으면 성공/실패로 임의 대체하지 않는다. 두 arm 중 한쪽 trace가 빠졌을 때의 처리는 분석 전에 고정한다.

| 관찰될 경우 | 사전 해석·다음 행동 |
|---|---|
| Native equality/목표 binding/시간 정렬이 실패 | 효과 비교 중단. Fixture 또는 adapter 수정·기각 |
| History-enabled target이 독립 competence gate를 못 넘음 | Selector 가설의 반증으로 쓰지 않고 현재 측정 설계를 중단 |
| Selector 사이 top-k ID와 weight가 같음 | 해당 설정에서 선택을 통한 효과 차이를 주장하지 않음 |
| `Δcue`가 작거나 불확실함 | 이 조건에서 이득이 확인되지 않음. 동등성/정보 무용성을 자동 결론 내리지 않음 |
| 단순 balance·LR 정합으로 차이가 설명됨 | Learned 방법 기여 종료, 알려진 대안의 적용 범위로 축소 |
| `Δcue>0`지만 `Δreuse≤0` | Cue 대 무관 frame contrast는 있어도 full-history 재선택의 이득 주장은 지지되지 않음 |
| 세 contrast·competence가 일관돼도 한 fixture뿐임 | 조건부 사례. 다른 pool/task·robot의 재사용 규칙으로 확대하지 않음 |

실제 재개 전에 채워야 할 값은 **selector estimator/구현 revision, checkpoint와 pretraining 노출, encoder/normalizer, k와 sampling rule, LR/tuning budget, seed 수, `δ`, 최종 test와 종료/결측 규칙, native 허용 오차**다. 현재 값은 미결이며 실행 명세가 완성된 것으로 표시하지 않는다.

## 8. 연구 가치와 다음 단계

**한정적인 진단으로 발전시킬 여지는 남지만, 아직 주력 연구로 채택할 근거는 부족하다.** 남는 질문은 “goal 정보가 중요하다”가 아니라 **동일 target을 고정한 선택기 입력 정합의 이득이 단순 coverage·tuning 이후에도 남으며, 언제 재선택할지 사전에 예측할 수 있는가**다. 현재 한 fixture에서 contrast를 정의한 것은 이 넓은 조건 예측을 검증한 것과 다르다.

비실험으로 이번에 해소한 것은 직접 선행 누락, contrast 해석, selection→target 데이터 경계, 비교/통계 단위다. 남은 핵심 불확실성인 **실제 관측의 동등성, target의 기억·행동 능력, subset의 효과**는 문헌과 수식으로 대신 확인할 수 없다. 같은 source를 반복 조사하는 N5를 자동 생성하지 않는다.

다음 실행 항목은 기존 **N3-B의 작은 native fixture qualification**이며 자원 대기를 유지한다. 이를 통과해도 곧바로 72 episode나 selector 학습을 시작하지 않고 §7의 미결 필드와 실제 HDF5/model 연결을 먼저 고정한다. 실험을 계속 제외하는 동안에는 새 충돌 논문·새 공개 비교 packet·외부 연구자 피드백처럼 판단을 바꿀 근거가 들어올 때 재심사한다. 외부 피드백을 요청하거나 받은 적은 없다.

## 9. 저장소 검증

TODO·DATA-TRANSFER synthesis·연구/저장소 navigation·buildup guide에 이번 해석을 연결했다. `py_compile`, tier 생성, repository audit, `git diff --check`를 통과했고 audit 오류·경고는 0이다. Registry 1,072편·active 344행/history 47행·5,360개 표준 노트는 그대로다. Canonical 파일 6개와 N3의 README 외 기존 artifact 15개 hash를 보존했다. 최종 명령 결과와 변경 범위/hash 대조는 source ledger의 `validation`에 기록한다. 문서 유지보수 검사와 연구 실험을 구분한다.
