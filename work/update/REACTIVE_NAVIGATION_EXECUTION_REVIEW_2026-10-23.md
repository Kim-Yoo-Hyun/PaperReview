# GAP-P2 — 반응형 navigation의 공개 실행 경로와 실험 전 계약

- 검토: 2026-10-23 KST. **정적 심사 DONE / 상태 기반 진단 REVISE / native VLA HOLD**.
- 범위: 3개 repository revision·34개 source/doc(지정 구간 28·context inventory 6), 공식 dataset 문서 1건. 전체 repository 정독이나 실행 검증은 아니다.
- 질문 소유: [GAP-PLAN](../../synthesis/01_planning_control.md#gap-plan-2026). 직접 선행·보장 조건은 [GAP-P1](./REACTIVE_NAVIGATION_SAFETY_REVIEW_2026-10-23.md)을 따른다.
- 산출물: [source·구간·hash ledger](../sources/reactive_navigation_execution_review_2026-10-23.json), [실험 전 manifest](../sources/reactive_navigation_preexperiment_manifest_2026-10-23.json). Manifest는 실제 생성했지만 `executable=false`이며 실행 코드·Docker image·결과는 아직 없다.
- 외부 코드의 텍스트만 대조했다. 외부 코드 import/실행, 실험, 의존성 설치, PDF·dataset·checkpoint 다운로드, 신규 논문 등록, 사용자 읽기 상태 변경은 없었다. 공개 최신 revision과 논문에 사용한 revision의 동일성은 미확인이다.

## 1. 판정과 연구 가치

**GenSafeNav에는 로봇에 반응하는 보행자를 구성할 경로가 있다. 다만 기존 평가 스크립트를 그대로 사용하면 계획 전환 직후의 calibration·risk를 공정하게 측정하기 어렵다.** Timestamp와 track identity, predictor의 유효성, terminal/reset, oracle baseline을 먼저 분리해야 한다. 따라서 GPU를 기다릴 단계가 아니라 작은 Docker 계약 검사까지 진행할 수 있는 단계다. 일반 adaptive safety/replanning 방법의 NO-GO는 유지하며, 아래 준비가 끝났다는 사실만으로 새 연구 기여를 주장하지 않는다.

| 경로 | 이번에 확인한 것 | 허용할 결론·현재 판정 |
|---|---|---|
| GenSafeNav 상태 기반 crowd simulation | ORCA human이 ego state를 받는 분기, 0.25 s clock, GST/ACI 호출 경로 | 수정·계약 검사 후 synthetic 진단 가능. 원 논문 재현/새 방법 효과는 미검증 |
| 현재 ABot-Navigation point-goal release | 이미지→waypoint→pose 선택→정적 occupancy 선분 검사→렌더링 | 이 경로만으로 반응형 pedestrian·물리적 지연 비교 불가. Native VLA 경로 HOLD |
| THÖR-MAGNI | 실제 HRI 수집 조건, timestamp/helmet/role schema, 전처리 코드 | 기록된 반응·오차의 기술적 분석 후보. 새 ego 정책의 counterfactual 효과는 식별 불가 |

남길 조건부 질문은 **같은 predictor·관측·행동 예산에서 ego 경로 변경과 상대 반응의 상호작용이 만드는 전환 구간의 calibration/risk 변화가 단순 지연·고정 margin·wait/hysteresis 이후에도 남는가**다. 차이가 남더라도 calibration 지연이 위험의 원인이라는 매개효과까지 자동 식별하지 않는다. 그 주장은 별도 개입이 필요하다.

## 2. GenSafeNav: 실제 호출 경로와 수정 전제

검토 revision: [`01baf926a5c77c1a4ab28635658eb014ef4f1767`](https://github.com/tasl-lab/GenSafeNav/tree/01baf926a5c77c1a4ab28635658eb014ef4f1767). 아래는 코드 경로의 사실과 그로부터 도출한 검사 요건이다. 실행해서 재현한 오류 목록은 아니다.

### 설정·clock·반응

1. [`test.py` L15–63, 120–159](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/test.py)의 기본 대상은 `trained_models/Ours_GST`, `05207.pt`다. 실제 설정은 **model directory의 arguments/config**에서 import하며 root config만 고치는 것으로 충분하지 않다. `test_size=250`이 config의 500을 덮어쓴다.
2. [저장 설정 L13–176](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/trained_models/Ours_GST/configs/config.py)은 human 20, ORCA, `robot.visible=False`, holonomic action, `env.time_step=data.pred_timestep=0.25`, 예측 5 step이다. 설정상 horizon은 1.25 s지만 GST checkpoint 내부 `pred_seq_len/obs_seq_len`과 hash는 payload를 읽지 않아 미확인이다. GPU/CPU 변경도 wrapper의 `training.device`와 별개로 감사해야 한다.
3. 등록 이름은 `CrowdSimPredRealGST-v0`다. 그러나 [factory L37–151](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/networks/envs.py)는 `gym.make`가 아니라 해당 class를 직접 생성한다. 실제 경로는 `test → make_vec_envs → DummyVecEnv → VecPyTorch → VecPretextNormalize → evaluation`이다.
4. [human action L603–626](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim.py)에서 `robot.visible=True`이며 FOV 조건을 만족하면 ego의 위치·속도가 human ORCA 입력에 들어간다. [step L138–165](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred.py)는 human action을 **현재 state에서 먼저** 정하고 robot/human을 이동시킨다. 방금 선택한 ego action의 결과는 이후 state로 전달된다. 이 순서를 명시하지 않고 한 tick의 인과적 지연을 학습/추론 latency로 세면 안 된다. ORCA를 전역적으로 smooth/Lipschitz인 반응 모델로 가정하지 않는다.

### predictor → ACI → policy의 시간·identity 계약

[`VecPretextNormalize` L60–64, 130–214](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/vec_env/vec_pretext_normalize.py)는 `pred_timestep // time_step` 간격으로 history를 골라 GST를 호출한다. [`GST interface` L45–117](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/gst_updated/scripts/wrapper/crowd_nav_interface_parallel.py)는 관측 mask와 history로 상대 변위를 예측한다. 실제 time field를 반환하지 않으므로 설정의 정수 배수·예측 길이를 runtime에서 검사해야 한다.

[`evaluation.py` L52–115](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/evaluation.py)는 reset/step 후 예측을 `talk2Env`에 보내고 conformity score를 다음 policy 입력에 붙인다. 환경 step은 그 전에 이전 예측을 관측된 다음 위치와 비교한다. **관측→matured score 갱신→새 예측/반경 발행→행동**의 시간 순서를 로그로 고정해야 한다.

| 코드 사실 | 비교를 위한 요건 |
|---|---|
| [wrapper L185–204](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/vec_env/vec_pretext_normalize.py)는 `spatial_edges`를 거리순으로 정렬하고 `visible_masks`는 그대로 전달한다. [talk2Env L80–111](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred_real_gst.py)는 실제 human 거리순으로 다시 정렬해 현재 위치 차이 <0.1 m를 valid로 둔다 | positional match를 stable identity로 간주하지 않는다. `(episode, track, generation)`과 permutation/inverse를 명시하고 mask·prediction·radius가 동일 track을 가리키는지 검사한다. 특정 mask가 실제 policy에서 사용되는지는 별도 runtime 대상 |
| [`Human.update_aci` L30–51](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/utils/human.py)는 timestamp 없이 list의 뒤에서 i번째 prediction을 사용. [step L220–223](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred.py)는 valid human만 관측 목록에 추가 | 관측/예측이 끊기면 list 간격과 물리 시간 간격이 다를 수 있다. `prediction_id, issue_time, target_time, observed_time`으로 join하고 missing을 압축하지 않는다. 실제 발생 빈도·영향은 미측정 |
| [step L205–218](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred.py)는 관측 생성 뒤 goal 도달 human을 새 객체로 교체하면서 같은 id를 재사용 가능 | 초기 진단은 random/end-goal 변경과 human 수 변경을 끈다. 이후 사용 시 generation 증가와 predictor/ACI history reset을 검사 |
| [talk2Env L111](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred_real_gst.py)는 반경을 [0,1] m로 clip. [DtACI L34–66](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/dt_aci/one_step_dtai.py)는 내부 prediction으로 coverage를 기록 | 발행 시 저장한 **실제 적용 반경**으로 coverage 재계산. Raw/clip 값·saturation·미검출/fallback을 분리. 내부 평균 coverage를 배치 보장으로 승격하지 않음 |

### oracle·terminal·metric

- **ORCA baseline은 그대로 사용하지 않는다.** [step L111–123](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred.py)의 robot ORCA/social-force 분기는 `calc_human_future_traj('truth')`를 행동 입력으로 쓴다. 내부 상태/goal로 만든 lookahead이며 실제 미래 관측을 뜻하지는 않는다. 또한 [lookahead L207–230](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_var_num.py)는 human의 관측을 다른 human들로 구성한다. Reactive 실행의 ground truth로 간주할 수 없다. 공정 baseline은 다른 방법과 같은 관측·추정 속도만 사용해야 한다.
- Test의 `Danger`는 [future proxy L431–447](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_var_num.py)를 사용한다. 이 조건이 GST policy 입력으로 직접 들어간다고 확인한 것은 아니다. 하지만 실제 충돌/near-miss 지표와 별도로 이름 붙여야 한다. 상태 시점의 collision 판정만으로 tick 사이 충돌을 배제할 수도 없다.
- [`DummyVecEnv` L46–57](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/networks/dummy_vec_env.py)는 done 직후 reset observation을 반환한다. 반면 [평가 L102–119](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/evaluation.py)는 그 observation으로 `talk2Env`와 path length 갱신을 한다. Terminal pose를 별도로 보존하지 않는 경로이므로 episode 경계 혼입을 검사하고 새 진단에서는 자동 reset을 끈다.
- [평가 L146–197](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/rl/evaluation.py)의 nav time은 성공 episode 조건부다. CSV는 길이가 다른 success/collision/min-distance 목록을 같은 row 번호로 쓰므로 row를 동일 episode join으로 사용하면 안 된다.
- [reset L329–378](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_var_num.py)과 DtACI는 global NumPy RNG를 사용한다. 동일 seed만으로 분기 후 외생적 난수까지 동일하다고 보장하지 않는다. Scene 초기화·human 외생 변화·calibrator·policy RNG를 분리하고 paired branch에는 state와 RNG snapshot을 함께 복제한다.

## 3. ABot와 THÖR-MAGNI를 어디까지 쓸 수 있는가

ABot revision [`2a0aefb56f1e2d315bba924239e9e8ad9dca9d92`](https://github.com/amap-cvlab/ABot-Navigation/tree/2a0aefb56f1e2d315bba924239e9e8ad9dca9d92)의 [point-goal loop L389–505](https://github.com/amap-cvlab/ABot-Navigation/blob/2a0aefb56f1e2d315bba924239e9e8ad9dca9d92/abotn_evaluator/point_goal/evaluator.py)는 waypoint에서 pose를 골라 occupancy 충돌 검사 후 새 pose를 렌더링한다. 이 경로에는 물리적 dt, pedestrian action update, trajectory tracking controller가 연결되어 있지 않다. `step_count`를 초로 치환하거나 inference wall time 동안 인간이 이동한다고 가정할 수 없다.

구현의 [Observation/WaypointPrediction](https://github.com/amap-cvlab/ABot-Navigation/blob/2a0aefb56f1e2d315bba924239e9e8ad9dca9d92/abotn_evaluator/interface/point_goal.py#L18-L108)은 local `[front,left]` m이고 [observation 생성 L578–600](https://github.com/amap-cvlab/ABot-Navigation/blob/2a0aefb56f1e2d315bba924239e9e8ad9dca9d92/abotn_evaluator/point_goal/evaluator.py#L578-L600)도 이를 따른다. **P1의 docs 기반 `[right,front]`를 구현 계약으로 재사용하지 않는다.** Outdoor의 `success_new`는 collision count <3을 허용하므로 무충돌 성공이 아니다. [collision helper L571–626](https://github.com/amap-cvlab/ABot-Navigation/blob/2a0aefb56f1e2d315bba924239e9e8ad9dca9d92/abotn_evaluator/scene.py#L571-L626)는 occupancy/meta 부재 시 False를 반환한다. 새 adapter에서는 검사 불가능을 안전 판정과 구별해야 한다. 이는 선택한 point-goal 경로의 한계이며 전체 생태계에 동적 환경이 없다는 주장은 아니다.

[THÖR-MAGNI v2 공식 수집 문서](https://zenodo.org/records/13865754)는 scenario 3의 원격조종 이동 로봇, scenario 4의 언어/몸짓 상호작용, scenario 5의 도움 제안을 구분한다. `FILE_ID`, `BODY_NAMES/ROLES`, `Time/Frame`, 단위 header가 join의 출발점이다. QTM은 100 Hz이며 다른 센서의 frame 번호와 직접 동일시하지 않는다. `synch_info.csv`는 센서 정렬 event로, 계획 변경 annotation이 아니다. Helmet ID는 파일을 넘는 참가자 ID로 검증되지 않았다. 이 기록에는 새 정책을 배치했을 때의 matched human response가 없으므로 offline 분석만으로 policy safety 효과를 추정하지 않는다.

[도구 revision `5d804062`](https://github.com/tmralmeida/thor-magni-tools/tree/5d8040623034e4c21526792badb7b8d93e33f0ca)의 [전처리 L35–146](https://github.com/tmralmeida/thor-magni-tools/blob/5d8040623034e4c21526792badb7b8d93e33f0ca/thor_magni_tools/preprocessing/reprocess.py#L35-L146)는 linear interpolation, bin 첫 값 resampling, trailing rolling average를 제공한다. Rolling average를 centered filter라고 잘못 부르지 않는다. 다만 **linear interpolation은 gap 뒤 관측을 사용할 수 있고**, [best-marker 선택 L7–110](https://github.com/tmralmeida/thor-magni-tools/blob/5d8040623034e4c21526792badb7b8d93e33f0ca/thor_magni_tools/preprocessing/filtering.py#L7-L110)은 입력 파일 전체의 결측 수를 본다. Default는 100 frame interpolation·400 ms resampling·800 ms average다. 이 출력을 online 관측으로 사용하려면 가용 시점을 보존하는 별도 causal preprocessing이 필요하다. 데이터 payload를 읽지 않았으므로 실제 결측률·join 성공률은 모른다.

## 4. 실행 전 비교 계약

아래 값은 **새 진단을 위한 연구자 설계 초안**이며 논문 보고값·수행 결과가 아니다. 세부 값과 미결 항목은 [manifest](../sources/reactive_navigation_preexperiment_manifest_2026-10-23.json)가 소유한다.

- **1차 범위:** 상태 기반·holonomic·고정 human identity. CV predictor는 관측된 두 위치/시간으로 속도를 추정한다. GST/RL/VLA checkpoint 없이 먼저 clock/ID/평가가 맞는지 검사한다. 이 구성은 GenSafeNav의 CRL 재현이 아니다.
- **비교 축:** ego 무반응/ORCA 반응 × ego route 유지/전환 × actuator 지연 0/0.5 s. ORCA를 smooth라고 부르지 않는다. 별도 불연속 반응법칙은 구현·정의가 미완료여서 1차 범위에서 제외한다.
- **시간:** dt 0.25 s, horizon 5 step, route event 10 s, 전후 각 5 s, episode 30 s 초안. 각 reaction/delay/reference-controller 조건에서 event 직전 state·history·calibrator·RNG를 복제해 hold/switch branch를 비교한다. 고정 최종 goal·기하학적으로 대칭인 route 쌍을 사용하며 정확한 scene/waypoint 파일과 hash는 P3에서 고정한다. 반응 후의 실제 human 궤적을 동일하게 강제하지 않는다.
- **분리:** 각 method의 동일 action 후보·탐색 horizon·관측 budget·calibration source 유지. Fixed margin, timestamp-correct DtACI, rolling empirical quantile, fixed margin+stop/wait/hysteresis를 비교 후보로 고정한다. 이름만 같은 저자 baseline 재현이라고 부르지 않는다. 모든 탐색 계수·대기 threshold는 development split에서만 정한다.
- **누출 방지:** 정책 입력은 관측 시점까지의 ego state·관측 track history·현재 route만 허용. Human goal/반응 유형, 실제 미래 위치, 사후 switch 성공, calibration/test label, 미성숙 score는 analyst 전용이다. Ego의 현재 route 전환 자체는 정책이 아는 입력이다.
- **분석:** paired episode 단위로 post-window risk/progress의 `(reactive switch−hold)−(nonreactive switch−hold)`를 delay별 보고한다. Coverage는 발행한 반경과 실제 target time으로 집계한다. 같은 관측열에서 shadow calibrator 비교를 따로 수행해 predictor 오차와 calibration 차이를 먼저 구별한다. 다른 controller가 만든 궤적의 단순 비교만으로 calibration의 인과 매개효과를 주장하지 않는다.
- **metric:** 실제 swept-disc collision, 0.25 m 이하 clearance 시간, 완료/timeout/교착, 제한 시간 내 goal 거리·경로·human 진행 손실, horizon별 coverage, missing/fallback/clipping 분모. 충돌 후 조기 종료 episode를 사후 window에서 제외하지 않고 충돌 위험에는 absorbing failure로 계산한다. 성공자만의 시간·독립 frame CI는 주 결과로 쓰지 않는다.
- **split:** smoke/dev/calibration/test scene family와 seed를 분리한다. Event 이전에 종료된 scene은 event-conditioned 분석의 제외 수와 전체 실패율에 남긴다. 향후 THÖR-MAGNI는 최소 recording 단위 split이며 participant identity 연결이 미확인인 상태에서 participant holdout을 주장하지 않는다.

### 필수 로그

`episode_id, pair_id, split, scene_hash, source_revision, track_id, track_generation, physical_time_s, observation_time_s, observation_available_time_s, prediction_id, issue_time_s, target_time_s, horizon_index, prediction_valid, score_available_time_s, score_used, radius_raw_m, radius_used_m, route_id, event_time_s, command_time_s, execution_time_s, action, terminal_observation, terminal_reason, actual_clearance_m, fallback_reason`를 최소 필드로 둔다. Policy-visible/analyst-only 필드는 분리하며 missing은 0으로 채우지 않는다. 단위·필수 여부·join key는 manifest에 기록했다. 아직 이 schema로 생성된 rollout은 없다.

## 5. 진행·중단 조건과 다음 TODO

후속 [GAP-P3](../experiments/reactive_nav_contract/RESULTS.md)에서 새 상태 adapter의 Docker 계약 13/13·3개 smoke scene을 통과했다. 아래 P3 계획은 P2 당시 인계다. 계약 전용 manifest와 full research 설계를 구분하며 현재 행동은 [TODO](../../TODO.md)의 GAP-P4를 따른다.

**GAP-P3 READY — Docker 안에서 작은 계약 검사.** 먼저 scene/route·controller 후보·threshold·RNG·image digest를 고정한 뒤, 3개 smoke scene에서 timestamp join, permutation, missing/reappearance, episode reset, raw/applied radius, oracle 차단, reactive input 경로를 검사한다. 외부 GST/정책 checkpoint나 대용량 dataset을 받지 않는다. Host에는 dependency를 설치하지 않는다. 실제 실행 전 manifest의 미결 필드를 채우고 검사별 PASS/FAIL/NOT_RUN을 남긴다. 현 단계에서 Docker 실행 가능성은 검사하지 않았다.

검사를 통과하기 전 연구 효과 rollout·학습을 하지 않는다. 통과해도 곧바로 큰 sweep으로 확장하지 않고 별도의 bounded pilot 판정을 한다. 이 준비 작업은 작은 실험을 가능하게 만드는 단계이지 결과를 먼저 입증하라는 조건이 아니다.

1. **계약 실패:** timestamp/ID/reset/oracle 문제를 해결하지 못하면 실행 적합성 결과만 남기고 중단한다. 오류 때문에 생긴 차이를 연구 현상으로 발표하지 않는다.
2. **단순 대안 설명:** 정렬 수정 또는 동일 비용 fixed margin/wait/hysteresis가 차이를 제거하면 일반 방법 주장을 기각한다. 차이가 actuator delay 조건에서만 나타나면 반응 유발 calibration gap과 분리한다.
3. **조건부 진단 가치:** 무지연에서도 전환×반응 차이가 반복되고, coverage/risk/progress의 관계가 shadow 분석·단순 대안 뒤에도 남으면 held-out 장면으로 진단 pilot을 검토한다. 소수 smoke scene은 이 조건의 증거가 아니다.
4. **외적 타당성:** 한 ORCA 구현에서만 보인 효과는 해당 simulator의 조건부 관찰로 제한한다. 두 번째 반응 모델·실제 기록·native VLA 경로로 확대하려면 별도 비교 packet이 필요하다.
5. **Native 재개:** 이미지/언어가 실제 route 선택을 바꾸는 task, checkpoint·normalizer·controller·physical clock·reactive human·평가가 연결된 packet이 확보될 때만 재심사한다. ABot의 이미지 출력이나 THÖR-MAGNI의 HRI 존재만으로 이 gate를 통과시키지 않는다.

## 6. 문서 검증과 보존

Registry 1,037편, tier, active/history 읽기 입력과 기존 dirty worktree를 보존한다. 필수 generator·repository audit·diff 검사 및 이번 임시 source 삭제 결과는 [ledger](../sources/reactive_navigation_execution_review_2026-10-23.json)의 validation에 기록한다. 과거 후보의 판정과 reading evidence maturity는 변경하지 않는다. Git 게시도 이번 작업 범위에 포함하지 않는다.
