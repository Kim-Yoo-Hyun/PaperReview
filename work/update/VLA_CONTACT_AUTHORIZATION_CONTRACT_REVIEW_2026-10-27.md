# GAP-AUTH3 — checkpoint·attention·접촉 계측의 비실험 계약

- 완료: 2026-10-27 KST. **Source/인터페이스 계약 검토 DONE, 비교 packet PARTIAL, 연구 진단 REVISE, native·정책 효과 NOT_MET.**
- 범위: [AUTH2](./VLA_CONTACT_AUTHORIZATION_SOURCE_REVIEW_2026-10-27.md)의 두 SafeLIBERO 과제를 유지하고 공개 checkpoint, 실제 선택 backend, 정규화, attention 출력, 접촉 dependency를 확인했다. [기계 판독 계약·source ledger](../sources/vla_contact_authorization_contract_review_2026-10-27.json)는 **실행 manifest가 아니며 `executable=false`**다.
- 조사량: 공식 OpenPI 고정 revision의 source/doc 12파일 지정 구간 + 변환 script 1파일 context, PyPI robosuite 1.4.1 배포본의 source/metadata 7파일 지정 구간, checkpoint 객체 목록 16건과 작은 metadata JSON 3개. AUTH2의 AEGIS 25파일은 이전 근거로 재사용했다.
- 실험·Docker/GPU probe·모델/API 호출·dependency 설치 없음. PDF·가중치·초기 상태 payload 다운로드 없음. 공개 source와 작은 정규화/구조 metadata만 읽었다. 신규 등록·tier·사용자 읽기 상태 변경 없음.

## 1. 이번 단계의 결론

**자산 이름의 모호함과 계측 위치는 줄였지만 연구 효과를 판단할 증거는 아직 없다.** 실제 비교 기준으로 사용할 공개 JAX checkpoint를 지정했고, AEGIS에 적힌 경로 문자열을 그 논문의 실제 weights라고 간주하지 않았다. Attention을 꺼내는 인터페이스 변경과 독립 contact evaluator가 필요하며, 공통 지각 모듈과 단순 관계 baseline의 구체 구현은 남아 있다.

가장 중요한 수정은 두 가지다. `observation/state`가 입력에 있다고 해서 정책이 그 값을 행동 생성에 쓰는 것은 아니다. 또 control tick 마지막의 contact bool만으로 physics substep 사이의 오접촉을 검증할 수 없다. 두 경우 모두 필드 이름 대신 실제 계산 경로를 기준으로 계약을 바꿨다.

현재 후보의 가치는 **“정책의 잘못된 물체 선택이 보호 제외 오류로 함께 전파되는 조건”을 분리해 진단하는 것**이다. 새 CBF·독립 guard 자체는 기여가 아니다. 독립 판단의 이득이 초기 목표 고정, confidence threshold 또는 같은 지각 정보의 단순 관계 규칙으로 설명되면 learned method로 발전시키지 않는다.

## 2. 공개 checkpoint와 정규화

| 항목 | 선택한 기준 / 확인 범위 |
|---|---|
| 공식 source | `Physical-Intelligence/openpi@215abfb217dbac7d5f1273282331b9b1866c0479` |
| Checkpoint | `gs://openpi-assets/checkpoints/pi05_libero`; 공식 LIBERO README가 이 checkpoint와 `pi05_libero` config를 연결 |
| Backend | 공개 목록에 `params/` Orbax/OCDBT 구조가 있고 `model.safetensors`가 없음. **이 공개 bundle을 쓰는 로컬 비교의 기준은 JAX** |
| Config | `pi05=True`, horizon 10, action_dim 32, max_token_len 200, `discrete_state_input=False`, bfloat16 |
| 실제 반환 action | 정규화 복원 뒤 앞 7차원. Runner는 앞 5개를 실행하고 새 query |
| Norm asset | `assets/physical-intelligence/libero/norm_stats.json`, generation `1757354341826612`, 1,914 bytes |
| 확인한 norm hash | SHA256 `b3a44bb2810436fb62917decaea58bd4d9110255df527dea21e8fd40c960bd84`; 제공 MD5와 읽은 byte도 일치 |
| Norm schema | state의 mean/std/q01/q99 각각 8차원, actions 각각 7차원; PI05는 quantile normalization 사용 |
| 미확인 | 전체 weights byte/hash·실제 load·native action·AEGIS 저자 실행 weights와의 동일성 |

근거: [공식 LIBERO README L64–71](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/libero/README.md#L64), [config L743–763](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L743), [loader L45–64](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/policies/policy_config.py#L45). Generation·size·MD5/CRC는 원격 listing 값이며 모든 weights를 직접 검증했다는 뜻이 아니다. 16개 객체를 ledger에 남겼다. 작은 `_METADATA`와 `array_metadatas/process_0`는 구조만 확인했으며 `write_shape`를 전체 tensor shape로 해석하지 않았다.

Normalization은 `(x-q01)/(q99-q01+1e-6)*2-1`이고 역변환도 대응되는 quantile 식이다. 일반 z-score나 별도 추정 norm으로 대체하지 않는다. LIBERO의 delta action에 추가 delta transform을 적용하지 않는다. [Transform L141–181](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/transforms.py#L141), [LIBERO data config L315–343](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L315).

### 입력 state의 실질적 사용 경계

API는 EEF pose·gripper의 8차원 state를 받고 normalize/pad한다. 그러나 이 config는 discrete state token을 끄고, PI05 suffix에는 PI0의 continuous state token이 없다. 선택한 경로의 행동 예측은 **RGB·language·sampling noise에 의존하며 state 값은 정책 conditioning으로 들어가지 않는다는 정적 추론**이 가능하다. State shape의 batch 처리, output 변환, controller가 읽는 EEF 정보는 별개다. “proprioception을 사용하는 정책”으로 단정했던 포괄 표현을 이 기준에는 적용하지 않는다. 실행 중 state를 바꾸어 확인한 결과는 아니다. [TokenizePrompt L248–266](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/transforms.py#L248), [suffix L148–186](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/pi0.py#L148).

## 3. Attention 계약: 실제 계산과 연구자가 정한 readout

### 확인한 계산 경로

JAX는 prefix KV cache를 만든 뒤 기본 10회 denoising을 `lax.while_loop`로 수행한다. Gemma의 18개 layer, 8 query heads / 1 KV head, head_dim 256에서 RoPE와 scaling을 적용한 Q/K로 masked full-key softmax를 계산한다. 현재 반환은 action뿐이다. Layer scan, model sampler, `Policy.infer`, 최종 transform의 경계를 모두 통과해야 runner가 readout을 받을 수 있다. Python hook 하나를 붙이면 JIT/scan 밖으로 자동 전달된다고 가정하지 않는다. [Sampler L216–279](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/pi0.py#L216), [attention L158–249 및 scan L350–411](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/gemma.py#L158).

**두 정규화를 구별한다.** 전체 유효 key의 softmax에서 camera 부분을 자른 값은 camera-only softmax와 다르다. 같은 query/head의 camera slice를 그 camera 질량으로 다시 나누면 조건부 분포와 수학적으로 같지만, 작은 bfloat16 값의 underflow가 있으면 raw logits에서 float32 camera softmax를 다시 계산해야 한다. Base/wrist별 token span과 mask를 기록하며 빈 right-wrist camera는 제외한다. Camera span은 실제 embedding 길이에서 얻고 고정 offset을 추측하지 않는다.

[KNOWS §3.3–3.4·Appendix 7.2](https://arxiv.org/html/2606.09749v1#S3.SS3)는 특정 head의 camera-only 재계산, 면적 정규화와 confidence fallback을 사용한다. 이 계약이 그 논문의 head 선택·시간 집계·전체 구현을 재현했다고 주장하지 않는다. 보고된 layer/head 번호만 가져와 검증된 intent 신호로 취급하지 않는다.

### 고정한 v0 계측 규칙과 아직 필요한 calibration

| 항목 | 최소 계약 |
|---|---|
| 계측 보존성 | 기존 weights·noise·action 계산을 바꾸지 않는 별도 auxiliary 출력. 동일 입력/noise의 원 sampler 대 수정 sampler action 일치 확인은 미래 native gate |
| Primary readout | 최종 denoising evaluation에서 실행 예정 action row 0–4의 agent-camera 조건부 attention. 18×8 head/layer를 동일 가중 평균하는 **선택 없는 진단 proxy** |
| Secondary | Full-key camera mass, wrist map, head별 요약. 특정 head 선택 비교는 별도 dev selection을 동결한 뒤에만 가능; primary proxy 실패로 KNOWS를 반박하지 않음 |
| 시간 집계 | v0는 K=1 unique query. 하나의 map을 5번 재사용해 표본 수를 늘리지 않음. 미래 K>1 분석도 서로 다른 query와 각 query 당시 mask를 연결 |
| 물체 점수 | patch fractional coverage를 이용한 mass / mask pixel area; area 단위와 image transform을 고정. 없는/겹침이 불명확한 track은 invalid |
| Confidence | top1–top2 density gap이며 calibrated probability가 아님. threshold δ는 test 결과로 선택하지 않음 |
| δ 결정 | dev 분할에서 coverage–오허용–정상 진행 trade-off를 보고 하나를 동결; 그 전에는 `delta=null`, executable=false. Threshold-only baseline에도 같은 calibration 자료/예산 |
| Export | `sample_actions`의 aux를 scan/loop에서 명시적으로 전달하고, `LiberoOutputs`가 action만 반환한 **뒤** `Policy.infer`가 `authorization_trace`로 붙임 |
| 결측 | 빈 map·NaN·mask 미정·query 불일치·오래된 trace이면 보호 제외 없음. 명목 action으로 몰래 우회하지 않음 |

이 v0는 구현 전 오류를 분리하기 위한 로컬 선택이다. 좋은 target estimator라는 근거가 아니며, 약한 평균 readout만 상대하여 독립 guard 우월성을 주장할 수 없다. 유효한 single-head/readout 대안도 비교해야 방법 수준 주장을 심사할 수 있다. 현재 계측 코드와 action equivalence report는 없다.

## 4. robosuite 1.4.1과 접촉 시점

GitHub tag를 유사한 다른 버전으로 대체하지 않고 [공식 PyPI 1.4.1 release](https://pypi.org/project/robosuite/1.4.1/)를 확인했다. 전체 wheel은 약 193.5 MB이므로 저장·설치하지 않았다. HTTP Range 24회로 ZIP index와 필요한 텍스트 7개만 읽었다(전송 137,220 bytes). 개별 entry CRC와 SHA256을 확인했다. PyPI가 제공한 전체 wheel SHA256은 ledger에 기록하되 **전체 archive hash 검증 완료로 표시하지 않았다.**

| 연결 | 실제 source 구간 / 결론 |
|---|---|
| Control→physics | `robosuite/environments/base.py:364–407`: `int(control_timestep/model_timestep)`회 forward → pre_action → step → observables |
| Simulation 호출 | `utils/binding_utils.py:1082–1092`: forward는 `mj_forward`, step은 `mj_step` |
| 기본 주기 | macros의 0.002초와 AUTH2의 20 Hz라면 control당 25 substep. 실제 model.opt.timestep·private override·integrator와 일치하는지는 미확인 |
| 기존 contact helper | `utils/sim_utils.py:8–40`: geom pair를 검사하며 distance·exclude 조건은 검사하지 않음 |
| 이름 연결 | `models/base.py:274–295,580–625`: prefix를 반영한 contact_geoms/important_geoms 사용. Panda finger/pad 이름은 `panda_gripper.py:28–35` |
| Dependency | 배포 metadata의 MuJoCo 하한은 >=2.3.0. AUTH2 client의 3.2.3 pin과 문서 대조는 했으나 설치 호환성을 검증하지 않음 |

### Recorder 위치와 event 정의

- **기본 sample:** 각 substep의 기존 `sim.forward()` 직후, `_pre_action` 이전. 그때의 `data.time`·qpos identity·contact pair를 함께 기록한다.
- **Step 직후 보조 sample:** 필요하면 transition 기록으로 별도 저장한다. `mj_step` 뒤 contact를 새 qpos 시점의 contact라고 다시 붙이지 않는다. MuJoCo는 step이 state를 갱신한 직후 derived quantity의 시점이 다를 수 있음을 명시한다. [공식 consistency 설명](https://mujoco.readthedocs.io/en/3.2.3/computation/index.html#consistency-in-mjdata).
- **마지막 boundary:** 다음 기존 forward가 없는 terminal/horizon에서는 별도 복제 data의 position/contact 갱신으로 마지막 경계를 감사한다는 계약을 둔다. 원 simulator에 추가 forward를 끼워 넣지 않는다. 이 read-only 복제 경로도 미구현이며, 없으면 last-boundary coverage를 INCOMPLETE로 표시한다.
- **Primary event:** gripper의 실제 contact geom 집합과 다른 그릇 geom 집합 사이에서 finite `dist<=0`인 pair가 존재하는가. 순서를 뒤집어도 같다. `exclude`, `efc_address`, raw distance는 보존하고 active-constraint event를 secondary로 분리한다. [mjContact 정의](https://mujoco.readthedocs.io/en/3.2.3/APIreference/APItypes.html#mjcontact).
- Finger/pad만 검사했다면 결과 이름도 finger/pad로 제한한다. 전체 gripper event에는 `gripper.contact_geoms`를 사용하고 actual body descendants·collision flags와 대조한다. 누락 geom을 빈 집합으로 허용하지 않는다. Compiled ID는 reset 후 evaluator가 확인하며 guard 입력에 포함하지 않는다.
- 20 settling tick 뒤 이미 contact가 있는 case는 초기 부적합으로 기록한다. 첫 목표 접촉과 같은 physics timestamp의 다른 그릇 접촉도 오류다. 목표 접촉은 **평가 구간의 종료 규칙만** 바꾸며 guard에 oracle phase 신호를 주지 않는다.
- Discrete physics boundary 관측이 substep 사이의 연속 충돌, grasp, 충격량 또는 damage를 보장하지 않는다. 이 범위에서는 기하 접촉 진단이라고 부른다.

## 5. 최소 변경 계약과 누출 방지

다음은 만들어진 코드 목록이 아니라 **구현 시 요구하는 인터페이스**다. JSON의 각 항목은 `implemented=false`다.

| 경계 | 필수 내용 | 금지되는 우회 |
|---|---|---|
| Query packet | case/branch/query ID, control tick·sim time, RGB hash·transform, prompt hash, checkpoint/norm identity, noise identity, camera token spans, nominal chunk, aux score provenance | 실제 instruction target/body ID를 policy/guard packet에 첨부 |
| Perception packet | 같은 RGB-D의 visual track ID, mask·area·camera frame·calibration, object geometry·timestamp·validity, track history | segmentation ID나 simulator object pose를 perceived geometry로 바꿔 부름 |
| Authorization packet | 선택/보호할 **visual track** 집합, readout/rule version, gap·δ, reason·fallback; 입력 packet hash | task index로 `bowl_1`을 고정하거나 evaluator phase를 사용 |
| Filter packet | nominal action, 동일 controller units·limits, 모든 보호 track의 constraint, solver status·residual, output action, fallback, wall time | 첫 bbox만 보호, infeasible/empty cloud를 무필터 success로 처리 |
| Evaluator packet | 전용 truth body/geom mapping, substep 시간, contact raw fields, native success, diagnostic event, 종료·예외 사유 | truth mapping을 guard의 cache/로그 API로 역전달 |

공유 prefix의 한 decision을 비교할 때 nominal chunk·noise·geometry·controller·시점을 동일하게 고정한다. 보호 제외 집합만 바꾸어 잘못된 허용이 filter 결과에 전파되는지를 본다. Branch가 갈린 뒤에는 각자의 관측으로 같은 지각 알고리즘을 다시 실행해야 한다. 다른 branch의 미래 geometry나 attention trace를 강제로 재생하면 closed-loop 인과 비교가 아니다.

### 공통 filter와 fallback

하나의 bbox/ellipsoid/constraint인 AEGIS 원 경로를 그대로 둔 비교는 사용하지 않는다. v0 수정은 모든 **유효한 보호 track**의 같은 형식 constraint를 하나의 QP에 넣고, pose/normalization/controller unit·solver tolerance·warm-start 규칙을 arm 간 동일하게 두는 것이다. Gradient·margin·controller scaling의 실제 수치 manifest는 지각/제어 연결 심사 뒤 확정한다. 이 문서로 그 값까지 이미 검증했다고 표시하지 않는다.

- 유효 geometry와 불확실한 authorization: 아무 물체도 제외하지 않고 모두 보호.
- geometry 결측·NaN·solver 실패·시간 초과: 명목 action을 통과시키지 않고 비교 run을 `INVALID_FILTER`로 종료. Simulator 연구용 실패 처리이며 물리 로봇 emergency-stop 보장이 아니다.
- B0 무필터도 계측 실패는 invalid로 집계. B5 전부 보호와 명시적 정지 비교는 안전을 높이는 대신 진행을 막을 수 있으므로 완료·방해율을 함께 제시.
- Error/exception/invalid episode를 제거한 뒤 성공률을 다시 계산하지 않는다. 전체 예정 case 분모와 유효 case 조건부 결과를 모두 기록.

B1 내부 score+fallback, B2 threshold-only, B3 초기 예측 목표 고정, B4 원 지시+perceived relation, B5 전부 보호/정지, B6 oracle 허용 진단의 역할은 AUTH2대로 유지한다. **B4의 로컬 지각 model과 relation rule은 아직 특정하지 못했다.** 독립 grounding이 “별도 코드”라는 이유만으로 오류 독립성을 갖는 것도 아니다. 공통 detector/geometry 오류는 모든 arm에 함께 작용할 수 있다.

## 6. 예산·판정·환경 경계

- 기존 qualification 상한: 두 task의 초기 상태 index 후보 0·1, 총 4 reset packet. 실제 index 유효성은 아직 모른다. 이 네 case는 wiring/동일성 점검용이며 효과 추정·head 선택·test를 모두 겸하지 않는다.
- 동일 prefix 단일 decision은 horizon 10개 중 5개 실행 계약, 20 Hz control, 기본 10 denoising. Closed-loop 후속은 AUTH2의 최대 300 control tick과 20 settling을 보존하되 실행 승인을 의미하지 않는다.
- 비용 단위: policy query 수, control tick/substep 수, 지각 호출 수, 초기화/steady-state wall ms, device-synchronized model ms, QP/serialization ms, annotation/GT 사용량. Episode·reset을 독립 단위로 삼고 head·query·substep을 독립 trial로 세지 않는다.
- 20 Hz의 50 ms는 제어 간격이다. inference latency를 5로 나눈 평균만으로 deadline 충족을 주장하지 않는다. Cold start와 query 경계 stall, attention export, perception, solver를 분리해야 한다. 원 `Policy.infer`의 JAX timing은 host 변환 전 측정하므로 동기화 없는 측정값을 device 완료 시간으로 쓰지 않는다.
- Head/calibration/test 분리, δ·geometry margin·solver tolerance·지각 checkpoint, 실제 hardware/lock/digest는 미확정이다. 이것이 **packet PARTIAL**인 구체 이유이며, null을 임의 숫자로 채우지 않는다.
- 추후 환경 기준은 local Docker 내부의 server(JAX/OpenPI)와 client(SafeLIBERO/MuJoCo/robosuite)를 분리한다. 공식 OpenPI README는 Ubuntu 22.04와 inference >8 GB NVIDIA GPU를 안내한다. 이것은 attention 계측을 포함한 이번 구성의 VRAM 실측/보증이 아니다. Host 설치, 자동 PyTorch 변환, cloud VLM으로 우회하지 않는다. [공식 requirements](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/README.md#L22).

| 관측/미충족 조건 | 판단 |
|---|---|
| 동일 noise인데 계측 전후 action 달라짐, ID/시간 누출, native timestep 불일치 | 계측/비교 계약 실패. 연구 효과 해석 중단 |
| 공통 지각에서 두 그릇을 구분하지 못함 | 지각 실패와 authorization 오류를 분리할 수 없음; oracle 결과로 실사용 개선 주장 불가 |
| 평균 proxy만 실패하고 적절한 head baseline은 미검증 | 선택한 readout에 대한 결과로 제한; 내부 attention 계열 일반 반박 불가 |
| 높은 gap의 자연 오선택/오허용 사례가 없음 | 이 두 과제의 조건부 기제는 미관측. 주입 반례로 자연 발생 빈도 주장 불가 |
| Threshold 조정·초기 목표 고정·간단 관계 규칙으로 이득 설명 | 새 learned guard/방법 주장 중단; 진단 가치만 다시 심사 |
| 접촉 감소가 정지/invalid 증가·정상 작업 실패로 설명 | 유용한 안전 개선으로 채택하지 않음 |
| 동일 geometry에서 오허용은 줄지만 physical contact 차이가 없음 | authorization 진단까지만 지지; 정책 safety 효과는 미입증 |

## 7. 다음 TODO와 완료 경계

**GAP-AUTH4 — 비실험 지각·단순 대안 충분성 심사**만 다음에 진행한다. Cloud VLM 없이 두 그릇·plate/ramekin/stove의 visual identity와 관계를 제공할 공개 로컬 자산을 하나로 좁히고, 같은 지각 정보를 쓰는 B3/B4가 질문을 이미 해결하는지 검토한다. 정확한 checkpoint/license·mask/track/depth interface·frame/clock 연결, privilege와 calibration 비용, 기각 기준이 결과다. 후보 목록을 계속 늘리거나 지금 모델을 실행하는 작업이 아니다.

그 단계에서도 공정한 단순 baseline 또는 남는 차별적 예측을 확보하지 못하면 **현재 설계를 HOLD로 종료**한다. GPU를 구하거나 문서를 더 썼다는 이유로 연구 GO로 바꾸지 않는다. 실제 자연 오선택·진행 보존·접촉 이득은 추후 별도의 local Docker native 검증이 있어야 알 수 있다.

## 8. 문서·registry 검증

- `py_compile`, tier generator, `git diff --check` 통과. Repository audit **오류 0·경고 0**. 수정 문서의 local link 618개에서 깨진 경로 0개.
- Registry 1,072편·CORE 47/NEXT 297/REFERENCE 486/ARCHIVE 242·active tracker 344/history 47·표준 note 5,360개 유지. Registry/manifest/meta/tier/tracker 6파일의 작업 전후 hash 동일.
- 작업 전 dirty 639파일 중 이번 수동 수정 7파일 외 **632파일**을 byte 단위 보존했고, 기존 missing 10경로도 유지했다. Source 20파일의 SHA256·읽기 구간과 작은 metadata 3개의 hash를 확인했다. 임시 source/metadata 29파일은 삭제했다.
- 이 검사는 문서·registry 유지보수다. 연구 구현 테스트, native contact 재현 또는 정책 효과 검증으로 기록하지 않는다.
