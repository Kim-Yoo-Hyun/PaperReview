# GAP-CF2 — 공개 로봇 자료가 숨은 정보와 행동 부족을 구별할 수 있는가?

- 검토일: 2026-10-23 KST. [CF1 문헌 심사](./CAUSAL_INFORMATION_COVERAGE_REVIEW_2026-10-23.md)의 후속 자료 충분성 검토.
- 작업: **GAP-CF2 DONE**. 판정: **현재 공개 자료만 쓰는 CF 설계 종료, 문헌 진단으로 보존**. 일반 deconfounding/단순 cue-versus-demo 방법 NO-GO는 유지한다.
- Canonical 질문: [GAP-CAUSAL](../../synthesis/02_rl_il_offline.md#gap-causal-2026). [Source·revision·구간·보존 hash](../sources/causal_data_sufficiency_review_2026-10-23.json).
- Raw episode·영상·음성·survey·checkpoint를 받거나 열지 않았다. 외부 코드는 임시 텍스트 열람만 했고 import·실행·설치는 하지 않았다.

## 1. 결과

**DROID·Bridge·OXE·CIVIL의 확인한 공개 경로에는 CF1 질문을 곧바로 시험할 완결된 비교 자료가 없다.** DROID/Bridge의 언어 주석은 행동 이후 작성된 설명이며 시연자의 행동 전 정보와 같지 않다. OXE의 형식 통일은 원래 없던 시연자 정보·반사실 행동 결과를 추가하지 않는다. CIVIL은 가장 가까운 수집/평가 선행이지만, 공개 경로에서 전체 participant–cue–비용–학습 subset–native 결과의 연결을 확인하지 못했다. 이는 아래 명시한 문헌·schema·code 범위의 판단이며, 모든 비공개 자료에도 해당 정보가 없다는 주장이 아니다. [DROID §III-B](https://arxiv.org/html/2403.12945v2#S3.SS2), [Bridge §3.2](https://arxiv.org/html/2308.12952v2#S3.SS2), [OXE §IV-A](https://arxiv.org/html/2310.08864v9#S4.SS1), [CIVIL 공개 경로](https://civil2025.github.io/).

GPU가 없는 것보다 **자료의 의미와 비교 설계가 아직 맞지 않는 것**이 현재 제한이다. 같은 episode를 더 많이 받거나 embedding coverage를 계산해도 hidden condition별 행동 support·추가 cue의 수집 비용·대안 정책의 성공을 복원하지 못한다. 기존 로그로 가능한 IL 학습/representation ablation과 CF1의 원인 분리·정책 선택 검증은 다른 작업이다.

이는 causal robot learning 전체의 과학적 가치가 없다는 판정이 아니다. 현실에서 재사용할 조건 예측이 생긴다면 가치가 있지만, 현재 자료로는 단순 관측 정렬·history BC·표적 시연 수집과 구별되는 새 결론을 검증할 근거가 부족하다. **CF3를 만들어 같은 자료 조사를 반복하지 않는다.** 새로운 비교 자료가 확보될 때만 재심사한다.

## 2. 조사 범위와 버전

| 자료 | Registry / 공식 status | 확인 범위 |
|---|---|---|
| DROID | pr-0732, [RSS 2024](https://roboticsproceedings.org/rss20/p120.html) | arXiv v2 §III·App B/E, 공식 dataset/collection/teleoperation 문서, 수집·저장·policy loader 코드 |
| BridgeData V2 | pr-0733, [CoRL 2023](https://proceedings.mlr.press/v229/walke23a.html) | arXiv v2 §3.1–3.2, 공식 project/release index, raw 변환·공식 README가 연결한 RLDS builder·OpenVLA transform |
| Open X-Embodiment | pr-0024, [ICRA 2024 공식 목록](https://2024.ieee-icra.org/awards-and-finalists/) | arXiv v9 §III-A·IV-A, 공식 README·RLDS 계약, 위 두 source dataset의 소비 경로. OXE 전체 구성 dataset 전수 감사 아님 |
| CIVIL | 외부 선행, [Autonomous Robots 2026](https://link.springer.com/article/10.1007/s10514-026-10266-3) | Publisher §6–7·Data Availability, 공식 project→repository tree, 수집·전처리·config·CALVIN 평가 경로 |

Bridge는 지정 baseline이라 2023 자료도 포함했다. PMLR abstract는 trajectory 53,896개를, project/arXiv v2는 60,096개를 보고한다. 이번에는 어느 release의 실제 payload 수인지 재집계하지 않았으므로 두 수를 동일 버전의 검증된 크기로 합치지 않는다. CIVIL의 2025 공개 code commit은 2026 journal 모든 평가의 실제 실행 revision이라는 증거가 아니다. OXE v9와 DROID v2 역시 최초 proceedings 이후 수정 본문이다.

7개 repository revision에서 source/doc/config **27개**를 임시 확보했다. 20개는 지정 구간/README 계약을 읽었고 7개는 경로·symbol 탐색용 context다. Payload가 아니라 code가 값을 저장하도록 작성됐다는 수준의 확인이다. 완전한 source listing의 `truncated=false`도 외부 링크·비공개 저장소·실제 release 완전성을 보장하지 않는다.

## 3. 자료별 정보·시각·식별 충분성

| 자료 | Demonstrator와 policy 정보 | 시점·action·episode join | 비용·outcome·평가 | CF1에 대한 판단 |
|---|---|---|---|---|
| DROID | GUI의 사전 task와 camera feed 접근은 문서화. Raw에는 task/collector/scene metadata, RLDS에는 영상·proprio·사후 언어. 실제 정책 입력은 loader가 선택한 카메라/상태에 달림 | 수집 code는 관측→controller→command와 시간 필드를 저장. Raw UUID/path·RLDS 원본 path가 연결 단서이나 실제 join은 미실행 | Collector success label과 실패 episode의 존재를 논문이 명시. 예제 학습기는 success 경로·언어 유무로 필터링. 수집 준비/주석/폐기까지 포함한 allocation 비용과 대안 정책 rollout은 별도 | 기술적 정렬·분포 진단에는 유용. 시연자의 전체 정보, 알려진 latent별 support, 비용 대조는 미충족 |
| Bridge 계열 | VR teleop와 scripted 수집을 혼합. 언어는 trajectory 후 crowdsourcing으로 작성. 추가 camera/depth가 모든 episode에 있다고 가정 불가 | Raw converter는 `time_stamp`를 읽음. 현재 연결된 RLDS builder는 원본 path·modality flag, 날짜별 latency shift·마지막 dummy action을 사용 | 원래 recipe별 reward/terminal 의미가 다르며 native 성공 label로 치환 불가. 공식 평가 안내는 WidowX hardware 재실행 경로 | 사후 language·reached-state action으로 시연 전 원인을 판단하면 대상이 달라짐. Scripted data도 동일 조건의 randomized causal 비교가 아님 |
| OXE | Source별 관측과 collection protocol을 보존하는 통합 형식. RT-X의 한 canonical camera 입력과 source 전체 센서가 다름 | 7D라는 동일 shape에도 좌표계·absolute/delta/velocity가 다름. Source/version/normalizer와 terminal convention이 필요 | Data inference 예제는 기록된 action 예측이며 새 정책의 실제 성공 evaluator가 아님. 모든 source에 공통된 비용/인과 실험 metadata는 통일 계약에 없음 | 통합만으로 hidden-information 문제를 해결하지 않음. Source별 검사 없이 pooled causal conclusion 불가 |
| CIVIL | 학습용 marker/언어 supervision은 직접 선행. 공개 수집 code에 timestamp와 cue 관련 경로가 있음 | Raw user/mode/demo path와 비용 필드는 존재. 확인한 학습 HDF5 writer는 `demo_i`로 재번호화하며 해당 비용·timestamp·raw path를 쓰지 않음 | Paper에는 동일 시간 비교가 있음. 공개 tree에는 demo sample 1개와 survey 경로, user study config에는 저자 로컬 path. CALVIN 평가 code도 있으나 사용자 연구의 대응 결과 묶음은 미확인 | 가장 가까운 부분 경로. 전체 paired 비교 packet·공정 수집 예산·새 조건 예측 부족. 기존 연구 결과가 없다는 뜻은 아님 |

행별 근거는 다음 지정 code 구간과 공식 문서에 연결한다. `없음`과 `미확인`을 구별한다. 특정 writer에 필드가 없는 것은 확인할 수 있지만, 모든 원본 episode가 그 writer로 생성됐는지는 확인하지 않았다.

## 4. 판단을 바꾼 구체적 근거

### DROID: 사전 task, 사후 설명, 성공 선택을 분리한다

[공식 collection 문서](https://droid-dataset.github.io/droid/example-workflows/data-collection.html)는 task 입력/선택과 camera feed 접근을 설명한다. [Dataset 문서](https://droid-dataset.github.io/droid/the-droid-dataset.html)는 raw metadata/HDF5/video와 RLDS 필드를 구분한다. Controller가 robot observation을 인자로 받는다는 사실은 사람이 그 observation만 봤다는 증거가 아니다.

- [수집 loop](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/droid/trajectory_utils/misc.py#L69-L129): `step_start/policy_start/control_start/step_end`, `skip_action`, 관측과 command dict 저장. [Robot observation](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/droid/robot_env.py#L108-L133)은 camera/robot timestamp를 따로 받는다. 실제 clock 오차·release 누락은 측정하지 않았다.
- [Metadata schema](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/droid/postprocessing/schema.py#L97-L143)는 UUID·user·scene·success·current_task를 제공하는 경로다. 이를 crowdsourced instruction과 섞어 하나의 contemporaneous cue로 만들지 않는다.
- [예제 loader](https://github.com/droid-dataset/droid_policy_learning/blob/9a29c832b4c81bf38401111f5e4cdddaca217581/examples/droid_dataloader.py#L20-L66)와 [success filter](https://github.com/droid-dataset/droid_policy_learning/blob/9a29c832b4c81bf38401111f5e4cdddaca217581/robomimic/utils/rlds_utils.py#L8-L38)는 `/success/` 경로와 language 유무를 사용한다. 데이터 전체에 실패가 없다는 결론이나 불편향한 outcome sample이라는 결론 모두 부적절하다.
- Dataset 문서의 flat action 설명에는 `6x joint velocities`라는 표기가 있으나 action_dict의 Cartesian/joint 차원 및 loader 계약과 구별해야 한다. 확인한 policy transform은 Cartesian absolute position→rotation6D+gripper를, OpenVLA는 Cartesian velocity+gripper를 선택한다. 문서 한 줄로 실험 action 의미를 고정하지 않는다.

### Bridge: label, command, 도달 상태의 차이가 중요하다

[공식 프로젝트](https://rail-berkeley.github.io/bridgedata/)의 다양한 시연은 학습용으로 유용하지만, 환경을 매번 동일 상태로 reset하지 않는 수집은 paired intervention의 자동 증거가 아니다. [논문 §3.2](https://arxiv.org/html/2308.12952v2#S3.SS2)는 사후 task labeling과 scripted rollout을 구별한다.

- [Raw→NumPy](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/data_processing/bridgedata_raw_to_numpy.py#L117-L137)는 원래 state/time/command를 읽는다. 같은 파일의 [L175–228](https://github.com/rail-berkeley/bridge_data_v2/blob/bc60a35b701a12021c8c95e9d8601274d3acd928/data_processing/bridgedata_raw_to_numpy.py#L175-L228)은 terminal을 0으로 만들고 `labeled_rew`의 마지막 두 값에 1을 둔다. 이 배열은 독립적인 실물 성공 판정의 근거가 아니다.
- 공식 README가 연결한 [현재 RLDS builder](https://github.com/kvablack/dlimp/blob/92e3eca97af3b14d0b6aa15182c0dc240407698d/rlds_converters/bridge_dataset/bridge_dataset_dataset_builder.py#L145-L205)의 step schema에는 reward/is_terminal이 없으며, [L224–237](https://github.com/kvablack/dlimp/blob/92e3eca97af3b14d0b6aa15182c0dc240407698d/rlds_converters/bridge_dataset/bridge_dataset_dataset_builder.py#L224-L237)은 2021-07-23 이전 수집분을 shift하고 마지막 dummy action을 붙인다. 이것을 모든 배포 Bridge RLDS 버전의 동일 schema로 일반화하지 않는다.
- [OpenVLA 변환](https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/prismatic/vla/datasets/rlds/oxe/transforms.py#L31-L86)은 첫 step 제거 후 [relabel 함수](https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/prismatic/vla/datasets/rlds/utils/data_utils.py#L166-L172)로 다음 state−현재 state를 movement action으로 쓴다. 도달 상태 기반 supervision은 유용할 수 있지만 commanded action의 인과 효과와 같은 estimand가 아니다.

### OXE: 형식 일치는 causal 의미 일치가 아니다

[OXE §IV-A](https://arxiv.org/html/2310.08864v9#S4.SS1)는 좌표계를 통일하지 않고 absolute/relative/velocity를 허용한다고 명시한다. [공식 README](https://github.com/google-deepmind/open_x_embodiment/blob/9eeb68b989efbcf474e8fb9019e01d02b962a604/README.md#L23-L37)의 inference overlay를 native policy 성공 평가로 세지 않는다. [RLDS 규칙](https://github.com/google-research/rlds#dataset-format)에서 마지막 observation의 `is_last=true` step은 후속 action/reward/discount가 invalid다. Padding과 terminal 처리를 확인하지 않은 action coverage 집계는 이 단계의 목표를 달성하지 못한다.

### CIVIL: 비용 기록 코드는 있지만 공개 비교 자료는 아직 불완전하다

[수집 code](https://github.com/CIVIL2025/Implementation/blob/785be3450b39232364fb16caf84ceeccae05dfb3/user_study.py#L87-L190)는 `timestamp`, `marker_placing_time`, `demo_time`을 저장한다. 따라서 “비용 기록이 없다”는 주장은 틀리다. 다만 [L201–278](https://github.com/CIVIL2025/Implementation/blob/785be3450b39232364fb16caf84ceeccae05dfb3/user_study.py#L201-L278)의 budget counter는 저장된 demonstration 반환 시간으로 증가하며 폐기 demo는 0을 반환한다. 이것이 실제 journal 실험의 총 wall-clock 비용을 정확히 재현하는지는 미확인이다.

[전처리 writer](https://github.com/CIVIL2025/Implementation/blob/785be3450b39232364fb16caf84ceeccae05dfb3/preprocess_data_civil.py#L166-L199)는 obs/action/num_samples를 저장하지만 위 비용·시각·원본 participant path를 쓰지 않는다. 따라서 raw-to-processed mapping을 따로 보존해야 한다. [User-study config](https://github.com/CIVIL2025/Implementation/blob/785be3450b39232364fb16caf84ceeccae05dfb3/conf/dataset/user_study.yaml)는 저자 로컬 디렉토리를 가리킨다. 공개 tree에서 확인한 payload 경로는 `panda_data_example/demo_sample.pkl` 한 개와 `data/subjective_survey.csv`이며 **내용은 열지 않았다**. Publisher Data Availability→project→code 경로에서는 완전한 participant/subset/outcome release를 확인하지 못했다.

[CALVIN 생성](https://github.com/CIVIL2025/Implementation/blob/785be3450b39232364fb16caf84ceeccae05dfb3/data_generation/generate_calvin.py#L77-L105)은 `scene_obs`를 beacon state로 사용하고, [평가](https://github.com/CIVIL2025/Implementation/blob/785be3450b39232364fb16caf84ceeccae05dfb3/test_calvin.py#L68-L133)는 state reset→policy action→task oracle 경로를 갖는다. **합성된 privileged cue 비교를 구성할 가능성은 있다.** 그러나 인간 cue의 수집 비용/오류를 검증하는 자료가 되지는 않으며 현재 VLA checkpoint·동일 budget baseline·실행 환경도 qualification하지 않았다. 이를 우회로 삼아 학습을 시작하지 않는다.

## 5. 주장–증거 심사

| 필요한 증거 | 현재 도달 수준 | 미충족이 의미하는 것 |
|---|---|---|
| 행동 전 시연자 정보와 고정 policy input의 관계 | Sensor·GUI·cue code를 부분 확인 | 전체 human information/known hidden variable의 증거는 아님. 사후 언어·미래 outcome을 대체 변수로 쓰면 안 됨 |
| 조건별 action support와 검증할 effect | Command/state·episode 기록 계약 존재 | 관측 marginal coverage로 숨은 조건의 support를 검증할 수 없음. 명시적 가정·통제 비교가 필요 |
| 동일 비용의 cue-only/support-only/both 비교 | CIVIL에 가장 가까운 실제 선행과 수집 코드 존재 | 전체 조건별 데이터/모델/평가 연결과 새 예측을 확보하지 못함 |
| Source episode·사용자·cost·가공 subset join | DROID/Bridge 원본 path, CIVIL raw path 단서 | Payload join 검사는 하지 않았고 일부 가공 writer는 metadata를 보존하지 않음 |
| Held-out 정책의 native outcome | 실물 평가 절차 및 CALVIN code 경로 존재 | 기존 기록만으로 새 정책 결과를 얻을 수 없음. 실제 평가 또는 식별 가능한 설계가 별도 필요 |
| 가장 강한 대안 이후의 새 지식 | CF1 baseline/reject 초안 | 단순 관측 복원·history·추가 데이터와 갈리는 구체적 예측 미확정 |

이 표의 부족은 모든 causal 추정에 paired counterfactual outcome이 필수라는 정리가 아니다. 유효한 IV·구조적 가정·partial bounds로 다른 질문을 풀 수 있지만, 그 가정을 실제 자료가 만족하는지와 CF1의 **정책 선택 개선**을 평가할 증거는 따로 필요하다. “로그가 크다”는 이유로 그 단계를 생략하지 않는다.

## 6. 종료와 재검토 조건

현재 설계를 문헌 진단으로 종료한다. Buildup 0–6은 문제·직접 선행·반례·비교 계약까지, 7은 입력 가용성/공개 interface 정적 심사까지 수행했다. 8의 외부 연구자 피드백은 받지 않았고 native 효과·실행 성공·신규성을 입증하지 않았다. C1/C2, 초기 RL 전이, D1–D3, E1/E2의 기존 판정도 바꾸지 않는다.

재검토에는 다음과 같은 구체적인 변화가 필요하다.

1. 행동 전 cue의 출처/시각, operator-visible/robot-visible 정보, command와 실제 상태, episode/participant ID, 실패·폐기·주석·reset 비용, 정책별 평가 결과가 연결된 자료를 확보한다. 또는 같은 식별 질문을 평가할 명시적 생성 모형과 정당화된 검증 설계를 제시한다.
2. Cue-only·support-only·both를 같은 수집 비용에서 구별하고 CIVIL/단순 BC·history/targeted collection과 다른 **조건 예측**을 정한다. 추가 camera를 test에도 주는 센서 향상과 train-only cue의 이득을 분리한다.
3. 실제 실행이 필요한 경우에만 사용자 컴퓨터의 로컬 Docker에서 runtime·base competence를 먼저 확인한다. GPU 확보는 위 두 항목의 대체물이 아니다.

다음 TODO는 **GAP-P1**이다. 아직 지정 본문 심화가 남은 [GAP-PLAN](../../synthesis/01_planning_control.md#gap-plan-2026)의 반응하는 상대·모드 전환·안전과 진행의 trade-off를 2024–2026 직접 선행으로 검토한다. VLA navigation과 연결하되 high-level 목표와 low-level 안전 보장을 분리한다. 이 문서에서는 새 PLAN 가설을 검증하거나 실험을 시작하지 않았다.

## 7. 검증과 보존

- 변경 전 audit: registry 1,037편, 표준 노트 5,185개, 오류·경고 0.
- 신규 등록·tier·사용자 읽기 상태 변경 없음. 기존 registry의 DROID/Bridge/OXE 3편을 source로 연결했으며 DROID-SLAM/BridgeVLA와 혼동하지 않았다.
- `py_compile`, reading-tier 생성, repository audit, `git diff --check` 통과. CORE 47/NEXT 275, active/history tracker 322/47 유지. Markdown 5,337개·링크 10,174개 검사, 오류 0·경고 0.
- 기존 dirty/untracked 358개 중 관련 문서 8개만 갱신하고 나머지 350개 hash를 보존했다. Manifest·registry meta·tier·active/history tracker hash도 그대로다. 신규 파일은 이 report와 source ledger 2개다.
- 임시 source/doc/config 27개는 hash 확인 후 tree metadata·보존 snapshot과 함께 삭제했다. 기존 논문·PDF·실험 artifact는 삭제하지 않았다. 상세 결과는 ledger에 기록했다.
