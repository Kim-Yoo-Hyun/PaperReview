# GAP-P4 결과 — 경로 변경 뒤 보정 실패 가설의 bounded 검증

- Completed: 2026-10-24 KST
- **결론: 현재 pilot에서 주 가설을 지지하지 못했다. 상태 기반 진단은 HOLD, 일반 adaptive safety 방법 NO-GO·native VLA HOLD를 유지한다.** 이 결과로 navigation 분야의 모든 연구 공백을 기각하지 않는다.
- Canonical question: [GAP-PLAN](../../../synthesis/01_planning_control.md#gap-plan-2026). [실행/재분석 안내](./README.md) · [동결 protocol](./PROTOCOL.json) · [기계 판정과 전체 수치](./results/verified/analysis.json).

## 1. 무엇을 실행했는가

로컬 Docker CPU에서 development12·calibration24·held-out12 scene instance를 실행했다. Held-out은 M0–M3 × 상대 반응2 × 경로 유지/변경2 × actuator 지연2로 **384 branch episodes**, 공유 prefix192개다. Pre-event 실패0개로 모든 조건에12개 paired scene이 남았다. Test의 실제 고유 simulation tick은32,890개이며, branch에 공유 prefix를 각각 포함하면40,570개다. 384개를 독립 scene384개로 해석하지 않는다.

한 ORCA crossing topology 안에서 각 split의 각도 대역·seed를 분리했다. 이는 **parameter-band holdout**이며 semantic task family·다른 simulator·실제 사람에 대한 일반화 검증이 아니다. P3의 원래 scene/controller/RVO code는 보존했다. P3 smoke의 hold도 접근 waypoint를 바꾸던 점을 고쳐, P4에서는 `(2,2)`를 계속 유지하거나10초에만 `(2,-2)`로 바꾸고 최종 goal `(12,0)`을 공유한다. 각 유지/변경 쌍은 world·calibrator·controller·FIFO·RNG를 복제한 동일 prefix에서 갈라진다.

Calibration은 성공 여부로 거르지 않은24개 reference rollout의 성숙 residual로 수행했다. Episode당 총 weight1을 주는 empirical90% quantile이며 horizon별 반경은 **0.01034, 0.02956, 0.05696, 0.09883, 0.14444m**다. 각 horizon에24개 episode가 기여했다. 이 값은 유한 표본 conformal certificate나 mission guarantee가 아니다.

- **M0:** 위 고정 반경.
- **M1:** 같은 초기 반경의 P3 timestamp-aware DtACI adapter. 원 논문 전체 구현/보장 재현을 주장하지 않는다.
- **M2:** rolling quantile; calibration episode별90% 요약24개로 warm start 후 online 갱신.
- **M3:** M0 + 기존 stop/wait/hysteresis. Threshold·33개 action·objective는 재조정하지 않았다.

## 2. 주 가설 판정

사전 조건은 M1의 **무지연** 비교에서 (a) post near-risk interaction ≥5 percentage points, (b) horizon5의 post-minus-pre miscoverage interaction ≥5pp, (c) 최소9개 paired scene, (d) 비슷한 진행량에서 단순 대안으로 설명되지 않음이었다. 이는 연구 투자용 screening 기준이며 보편적 유의성 기준이 아니다.

Interaction은 `(반응형 변경−유지)−(비반응형 변경−유지)`다. 위험은10–15초의20개 tick 중 swept clearance≤0.25m 비율이다. Collision 뒤 남은 구간은 위험1로, 조기 goal 뒤는0으로 채우되 노출 tick을 별도 기록했다. Coverage는 관측된 성숙 label만 사용하고 종료 후 미관측 label을0으로 채우지 않았다.

| M1 조건 | 위험 interaction | H5 miscoverage 변화 interaction | 진행량 interaction |
|---|---:|---:|---:|
| 지연0s | +21.25pp [13.75,30.83] | **−4.27pp** [−7.60,−0.83] | −0.354m [−0.770,−0.050] |
| 지연0.5s | +19.17pp [11.67,28.33] | **−5.76pp** [−11.39,0.80] | −0.484m [−1.016,−0.091] |

대괄호는12개 scene을 단위로1,000회 paired bootstrap한 descriptive95% interval이다. 확인적 통계 검정이나 큰 모집단의 확정적 구간으로 사용하지 않는다. **예상한 보정 악화 방향이 나타나지 않아**, 무지연·지연 모두 joint gate를 통과하지 못했다.

더 중요한 해석상 함정이 있다. 무지연 M1의 실제 위험률은 반응형에서 **유지5.42% → 변경3.75%**, 비반응형에서는 **28.75% → 5.83%**였다. 양의 interaction은 비반응형에서 감소 폭이 더 컸기 때문에 생겼다. 따라서 이를 “경로 변경이 반응형 상대에게 절대 위험을 증가시켰다”는 증거로 쓰면 틀리다. 반응형의 진행량은4.125→3.818m로 줄었다. M1의 명목상 잔여 경로는 변경 시 약0.845m(무지연),0.774m(지연) 길어졌다. 이 차이와 상대 궤적/제어 피드백 때문에 interaction만으로 calibration 매개효과를 식별할 수 없다.

## 3. 단순 대안과 실패를 함께 보면

무지연 반응형·변경 조건에서 M1 대비 M0는 위험+1.25pp·진행−0.0036m, M2는 위험+0.42pp·진행−0.0015m였다. 사전에 정한 risk2pp/progress0.5m screen 안에 들어온다. 이것은 **M1의 큰 고유 이득을 뒷받침하지 않는 결과**이며 통계적 equivalence나 단순 대안의 인과 설명 입증은 아니다. JSON의 `eliminates_joint_pattern=true`는 해당 screen 충족만 뜻한다. 주 pattern 자체가 성립하지 않았으므로 그것을 제거했다는 인과 해석은 하지 않는다.

M3는 같은 조건에서 M1보다 위험2.50pp 낮았지만 진행도0.519m 줄어 matched-progress 기준을 벗어났다. 따라서 낮은 위험을 무료 이득으로 세지 않는다. 전체384 branch에서 near-risk가 한 번이라도 있는 branch는194개, collision17개(그중 post window16개), goal342개, timeout25개였다. Collision17개는 모두 비반응형 조건이다. 원시 count는 correlated branch의 실행 inventory이며 방법별 안전 확률 추정치가 아니다. 특히 상대가 ego를 무시할 때 정지가 항상 안전한 대안은 아니라는 한계를 보였다.

Shadow는 **M0가 실제 실행한 동일 관측열**에서 네 보정기만 비교했다. 무지연 반응형·변경의 H5 post miscoverage는 M0/M3 10.00%, M1 18.02%, M2 5.21%였다. 반경과 의존 데이터가 다른 empirical 수치이며 각 방법을 실제 배치한 성공률이 아니다. M0/M3 shadow는384 trace 중 해당96개 M0 branch에서 완전히 일치했다. Shadow로 calibration→위험의 인과 매개를 주장하지 않는다.

## 4. 검증·제약·다음 결정

- P4 시작 전 episode-balanced quantile·absorbing collision·hold/switch 의미·직렬화 검사4개 PASS. P3의13개 계약은 기존 근거로 유지했다.
- 저장된384 branch에서 연속 tick/terminal 관측, 위험·진행 재집계, coverage 분모,192쌍의 동일 prefix/hash, M0/M3 shadow equality PASS. 이는 저장 clearance의 재집계이며 모든 기하 계산을 별도 물리 엔진으로 재검증했다는 뜻은 아니다.
- H5 성숙 label은 pre30,720개/post30,216개. 각 branch 끝의 미래 target40개씩 총15,360 prediction은 우측 검열로 따로 기록했다. Coverage는 종료 시점에 따라 선택되는 관측 label의 진단치이며 미관측 미래 안전을 보장하지 않는다.
- Development·calibration·held-out을 순서대로 한 번씩 실행했다. Test 결과를 본 뒤 parameter·scene·metric·기각 기준을 변경하거나 재시도하지 않았다. [동결 hash](./results/verified/TEST_FREEZE.json)와 [실행 기록](./results/verified/execution.json)을 보존한다.
- 저장 결과를 로컬 Docker에서 재분석해 원본 analysis JSON과 byte 일치를 확인했다. [재분석 증거](./results/replay_verification.json). Registry audit 오류/경고0, canonical manifest·tier·읽기 입력5개 hash와 기존 P3 artifact18개 보존을 확인했다. [유지보수/cleanup 검증](./results/maintenance_validation.json).
- 실제 human burden은 no-ego reference가 없어 **NOT_MEASURED**. 이미지·언어·학습 정책·현실 센서·다른 반응 모델은 이번 실행에 없다. 사용자 reading status와 registry tier는 변경하지 않는다.

**현재 설계의 추가 rollout/학습은 종료한다.** 이번 실패를 뒤집도록 각도나 threshold를 검색하지 않는다. 재개하려면 별도 문헌/독립 근거에서 route change 뒤 절대 위험 증가와 보정 악화가 함께 예측되는 조건을 제시하고, 진행/geometry·단순 대안과 갈리는 비교를 새 protocol로 검토해야 한다. GPU 확보만으로 재개하지 않는다.

다음 문헌 TODO는 아직 직접 충돌 심화가 남은 [GAP-DEFORM](../../../synthesis/03_manipulation_contact.md#gap-deform-2026)의 **task에 필요한 물성/고정 조건 식별**이다. JIGGLE·PGND 후속의 joint estimation/active probing과 고전 feedback·반복 보정 대안을 먼저 대조한다. VLA instruction이 probe/행동 선택을 실제 바꾸는 경우만 VLA 연결로 남기며 새 실험은 시작하지 않는다.
