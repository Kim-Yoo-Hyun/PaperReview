# GAP-N2 — 관측 정보 비교의 source 계약 심사

- 완료: 2026-10-25 KST. **작업 DONE; 현재 자산 설계 REVISE/HOLD; 연구 채택·수집·학습 HOLD; `executable=false`.**
- 범위: [GAP-N1 설계](./PROXY_OBSERVATION_CONTRACT_REVIEW_2026-10-25.md)의 네 연결을 공개 source에서 추적했다. RoboMME 두 고정 revision, source/config 35개 중 지정 구간 31개·context 4개다. 전체 repository 정독·현재 HEAD 감사·논문 실험 재현이 아니다.
- 근거: [파일별 URL/hash·검토 구간·수정 계약·검증 ledger](../sources/proxy_observation_qualification_review_2026-10-25.json). Source text만 임시로 가져왔으며 연구 코드를 실행하지 않았다. PDF·HDF5·checkpoint·패키지 다운로드, Docker 변경, rollout·inference·학습은 없다.
- Canonical 질문: [DATA-TRANSFER](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026). 새로운 gap/priority 목록을 만들지 않는다.

## 1. 결론과 판단의 범위

**현재 공개 경로를 그대로 이어서는 N1의 비교를 해석할 수 없다.** 원본 episode와 전처리 ID의 대응표가 없고, 관측/action 시점과 목표 변경 계약을 추가해야 한다. 반면 선택한 FrameSamp 경로의 과거 index 제한과 perceptual 입력에서 subgoal 문자열을 제거하는 연결은 source에서 확인했다. 네 항목을 모두 실패로 처리하거나 RoboMME 전체의 결함으로 확대하지 않는다.

| 연결 | source에서 확인한 것 | 이번 판정 |
|---|---|---|
| 원본 episode·split | 파일별 raw ID가 실행 순서에 따른 global ID로 바뀜. 그룹 split·원본 대응표를 builder/sample loader가 보존하지 않음 | N1의 paired 비교에 필요한 계약 **미충족** |
| Memory cutoff·mask·시간 | FrameSamp 요청 index는 현재까지. Mask가 train/inference의 memory attention까지 전달됨. 기록·평가의 물리 시점 및 encoder weight 동일성은 미확인 | index/mask 연결 **조건부 확인**, end-to-end 동등성 **HOLD** |
| 실제 model input | 선택한 perceptual 구성은 정답 subgoal을 tokenize하지 않음. Action label은 별도 학습 target | 문자열 누설 경로 **조건부 차단 확인**, 실제 tensor/checkpoint 검증은 미실행 |
| Paired goal–planner–evaluator | task dictionary와 별도 language-goal 함수가 모두 첫 bin/색에 결합. Native pickup 판정은 높이 threshold | 수정 지점 특정, paired fixture·독립 선택 metric **미구현** |

연구 질문은 **제한적인 진단 후보**로 보존한다. 정보 부족이 해로운 선택을 보장하지 않는 N1 반례, 같은 target B·같은 예산·단순 층화/tuning 대안은 그대로 적용한다. 지금은 top-tier 기여나 native 효과를 입증한 단계가 아니다. 일반 전이 방법 NO-GO와 기존 C1–C6/D1–D3/E1/E2·MEMORY·CAUSAL 판정도 바꾸지 않는다.

## 2. 원본 episode → 전처리 sample → split

`scripts/build_dataset.py → DatasetProcessor.run → _process_episode → SampleDataset → RoboMMEDataset → DataLoaderImpl`을 확인했다. [Builder L165–223](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/dataset_builder/build_robomme_dataset.py#L165)은 raw directory를 정렬하지 않은 `os.listdir`로 순회하고, 각 파일 안에서는 `episode_N`을 정렬한다. 모든 파일에 걸쳐 증가하는 `global_episode_idx`를 feature directory와 frame의 `epis_idx`에 사용한다. Raw filename/episode ID의 대응표나 group/split을 frame·stats에 저장하지 않는다. 기존 출력 directory를 삭제하는 초기화도 있으므로 향후 builder 실행은 별도 출력 경로가 필요하다. 이번에는 실행하지 않았다.

[Frame 저장 L242–318](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/dataset_builder/build_robomme_dataset.py#L242)은 video feature도 저장하되 실행 구간만 PKL sample로 쓴다. Episode 종료 시 memory buffer를 비운다. [SampleDataset L26–39](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/dataset.py#L26)는 stats에 적힌 sample 수와 정수 PKL 이름을 읽으며 그룹 split을 적용하지 않는다. 따라서 같은 raw pool을 다른 순서/부분집합으로 다시 전처리할 때 global ID를 stable identity로 쓰면 안 된다. 기존 배포 데이터의 ID가 실제로 잘못됐거나 복구 불가능하다는 뜻은 아니다. 외부에서 input directory를 분리하는 방법은 가능하지만 그 대응 증거가 이번 설계에는 없다.

Native replay의 [episode dataset resolver](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/env_record_wrapper/episode_dataset_resolver.py#L77)는 raw `episode_N`의 non-demo timestep을 따로 모은다. 평가의 [BenchmarkEnvBuilder L136–205](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/env_record_wrapper/episode_config_resolver.py#L136)는 metadata에서 task/episode의 seed·difficulty를 읽어 환경을 만든다. 이 두 경로와 global PKL ID 사이의 join이 자동 제공된다고 볼 수 없다.

**수정 계약:** source file digest/raw episode key → stable episode ID → fixture group·view·split → global index·sample ID를 모두 보존한다. 색 permutation 세 개와 모든 mask/retry 파생본은 같은 group split에 둔다. 목록 순서·재전처리로 split이 바뀌면 중단한다. Seed만으로 join하지 않으며 기존 train/test 데이터와 새 fixture의 provenance도 분리한다. 성공만 저장하는 [RecordWrapper L1151–1167](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/env_record_wrapper/RecordWrapper.py#L1151) 외부에 실패/retry/시간 attempt log가 필요하다.

## 3. Memory의 인과적 범위와 train/eval 연결

대상은 [perceptual-framesamp-modul.yaml](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/models/config/robomme/perceptual-framesamp-modul.yaml): 512 tokens, frame당 16 tokens, front view 1개, positional embedding 사용, historical state embedding 미사용이다. Current front/wrist/state는 별도로 들어간다. Recurrent/TokenDrop/symbolic variant까지 이번 결론을 확장하지 않는다.

[Training dataset L132–138](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/dataset.py#L132)과 [online policy L142–159](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/policies/policy.py#L142)는 같은 frame-sampling helper를 호출한다. [Indices/padding L8–68](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/shared/data_utils.py#L8)는 `0..t` 또는 그 구간의 linspace, 부족분의 false mask를 만든다. **이 branch의 index 규칙은 미래 frame을 요청하지 않는다.** 현재 frame은 포함한다.

Mask는 [train L616 이후](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/models/integration/history_pi0.py#L616), [inference L738–747](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/models/integration/history_pi0.py#L738)의 modulation 경로를 거쳐 [MemoryAttention L94–100](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/models/integration/history_gemma.py#L94)에 전달된다. 여기서는 masked logit을 같은 유한한 음수로 바꾼 뒤 softmax한다. **모두 false이면 memory가 0이 된다고 보장하지 않는다**: 유한 상수가 그대로 유지되는 연산에서는 균등 attention이 되는 구조다. 이는 코드에 근거한 해석이며 실행 결과가 아니다. N1 cue 제거는 최소 한 유효한 비-cue token을 남기고, 별도 null-memory 비교는 명시적인 zero-output 처리와 검증 없이는 사용하지 않는다.

같은 helper를 쓴다는 사실만으로 시간·feature 동일성이 보장되지는 않는다.

- **관측/action 정렬:** [RecordWrapper L823–845](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/env_record_wrapper/RecordWrapper.py#L823)는 `env.step(action)` 뒤 관측을 저장하고 같은 action을 row에 기록한다(L1033–1055). [Chunk builder L46–59](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/dataset_builder/build_robomme_dataset.py#L46)는 그 row의 action부터 target을 만든다. 따라서 기본 row를 곧바로 “행동 전 관측→다음 action”으로 부르면 안 된다. 실제 배포 HDF5의 생성 revision·의도한 offset은 미확인이다. 정책 성능 오류나 미래 누설을 확인한 것으로 해석하지 않는다.
- **Reset/시간축:** [DemonstrationWrapper L146–245](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/env_record_wrapper/DemonstrationWrapper.py#L146)는 demo에 초기 action 한 step을 덧붙이고 `NO RECORD` frame을 거른다. [Eval L80–140](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/examples/robomme/eval.py#L80)과 [policy L111–121](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/policies/policy.py#L111)는 수신된 frame의 순서로 online index를 부여한다. Raw timestep·filtered index·physics step·첫 decision의 대응표가 필요하다. 일반적인 video resampling이 발견됐다고 주장하지 않는다.
- **Feature provenance:** offline [SigLipTokenizer L13–35](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/shared/siglip_tokenizer.py#L13)는 별도 `siglip_params.pkl`을, online [vision_encode L771–783](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/models/integration/history_pi0.py#L771)는 policy의 image encoder를 사용한다. 두 weights가 다르다고 단정하지 않지만 hash/freeze/provenance 대조는 아직 없다.

**수정 계약:** 공통 decision cutoff와 raw time→feature slot 대응을 먼저 고정한다. Cue 제거로 frame을 압축·재번호화하지 않고 동일한 slot/position/mask 길이를 유지한다. 같은 수의 비-cue slot을 제거하는 control을 두고, 그룹 구성원 사이 mask 위치가 정답을 인코딩하지 않게 한다. Cue가 실제 sampled history에 들어가는지, 제거 후 current image/state·남은 history로 색이 드러나지 않는지도 확인해야 한다. 관측 equality를 전체 행동 이후까지 요구하지 않는다. 비교 기준 시점은 행동이 갈라지기 전이다.

## 4. Subgoal·정답이 실제 입력으로 들어가는가?

Builder가 저장한 네 subgoal 문자열 중 online 두 필드는 [dataset L190–217](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/dataset.py#L190)에서 제거된다. 남은 두 필드는 [RoboMMEInputs L43–86](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/policies/robomme_policy.py#L43)를 거치지만, [PI05 transform L170–210·L232–256](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/config.py#L170)은 perceptual 설정에서 이를 pop하고 prompt/state만 tokenize한다. [Training loader L19–30](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/dataloader.py#L19)는 `HistAugObservation`과 `actions`를 분리해 반환한다. Flow-matching 학습이 target action으로 noisy action을 만드는 것은 학습 objective이며 평가 시 정답을 제공하는 경로와 구별한다.

Eval은 oracle/Gemini/Qwen/MemER를 선택하지 않으면 [NullSubgoalPredictor L81–83·L245–258](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/examples/robomme/subgoal_predictor.py#L81)를 사용한다. [Eval L195–215](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/examples/robomme/eval.py#L195)는 current RGB/state/prompt와 별도 history buffer를 보낸다. Raw segmentation, choice labels, evaluator result, actor identity가 이 확인된 입력 whitelist에 포함되는 경로는 찾지 못했다.

**조건부 결론:** 선택한 perceptual 경로의 정답 subgoal 문자열 누설은 source 수준에서 차단된다. 하지만 [policy_config L31–53](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/policies/policy_config.py#L31)가 checkpoint 상위의 `history_config.txt`로 설정을 덮어쓰고, 파일이 없으면 history를 끌 수 있다. CLI 이름만으로 perceptual 경로를 보증할 수 없다. Resolved config·transform·norm stats·weight hash와 train/eval 최종 입력 key/tensor 검사가 재개 packet에 필요하다. Prompt의 목표 색은 허용 입력이지만 모든 matched group member에서 같아야 하며 목표 위치/actor ID는 제공하지 않는다.

## 5. Paired fixture: 함께 바꿔야 하는 지점

[VideoUnmask L160–234](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/VideoUnmask.py#L160)는 같은 seed generator로 bin 배치와 색 permutation을 만든다. Seed만 바꾸면 배치도 달라질 수 있다. **고정 scene/pose와 독립적인 색 permutation**을 명시적으로 전달해야 한다. [L387–405](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/VideoUnmask.py#L387)의 bin lift/drop cue와 demo 종료 뒤 첫 decision을 연결하되 렌더·접촉·그림자에 의한 current 관측 차이는 runtime에서 확인해야 한다.

| 수정 위치 | 필요한 동일 목표 계약 |
|---|---|
| `VideoUnmask._load_scene`의 색/actor 배정 | `target_color`는 group 내 상수, `target_bin_index`는 그 색의 실제 위치로 결정. Pose/camera/robot state 고정 |
| [Task dictionary L251–260](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/VideoUnmask.py#L251) | `func`, `failure_func`의 제외 집합, `solve(obj=...)`, `segment`, `name/subgoal_segment`를 같은 target actor로 연결 |
| [별도 `task_goal.py` L98–105](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/utils/task_goal.py#L98) | 현재 `color_names[0]` 사용. Task dictionary만 고쳐서는 안 됨. 저장 setup와 eval prompt가 고정 target color를 함께 사용 |
| [`solve_pickup_bin` L1090–1156](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/utils/subgoal_planner_func.py#L1090) | 전달된 `obj`의 pose/OBB로 경로 생성. 새로운 planner를 만드는 것보다 호출 target의 일치를 먼저 확인 |
| [`evaluate` L315–345](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/VideoUnmask.py#L315)와 [pickup 함수 L415–425](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/utils/subgoal_evaluate_func.py#L415) | 같은 task list로 성공/실패 판정. 실제 pickup 구현은 `z > 0.15`; 주석의 다른 높이·grasp 설명을 metric 정의로 사용하지 않음 |
| Metadata→builder | 기존 builder가 읽는 seed/difficulty만으로 새 permutation·target을 복원하지 못함. Fixture 설정/hash와 실행 경로를 함께 확장 |

N1의 **“첫 올바른 container 선택”은 아직 별도 metric이 아니다.** Easy task는 한 번의 pickup이며, 첫 lift와 native success를 같은 것으로 기록하면 독립적인 선택 진단이 되지 않는다. Grasp attempt/선택 확정 event의 관측 기준, 모호한 경우·동시 접촉·무선택 timeout 처리와 event 시점을 미리 정해야 한다. 평가 전용 privileged state는 허용할 수 있지만 policy input과 분리한다. 그 정의 없이 성공률을 두 이름으로 보고하지 않는다.

## 6. 재개에 필요한 구체 artifact와 기각 규칙

다음은 [ledger의 `repair_contract`](../sources/proxy_observation_qualification_review_2026-10-25.json)에 필드·검사·현재 미구현 상태로 기록했다. 실행 manifest나 구현 완료 schema를 만들어 낸 것으로 표시하지 않는다.

1. **Identity/split manifest:** raw digest/key, stable episode/group/variant/attempt ID, split, global/sample ID, 생성 revision. Pair/retry/view의 split 교집합 0 및 완전한 join 검증.
2. **Time/feature contract:** raw row·physics step·관측의 pre/post-action 구분·target action offset·첫 decision·cue span·선택 frame/slot·valid mask. Offline/online encoder 및 normalizer provenance.
3. **Resolved policy-input contract:** 실제 history config, front/wrist/state/prompt/history key·shape·mask, forbidden answer fields 없음. All-masked memory 처리 및 동일 수 비-cue 제거 control. Null-memory OOD 실패와 조건별 학습 selector 비교 분리.
4. **Fixture revision/metric contract:** 고정 scene와 독립 permutation, 동일 목표를 쓰는 language goal/planner/evaluator, 별도 첫 선택 event, 실패/retry/cost log. Action 이전 paired observation equality는 **Docker qualification의 목적**이며 문서만으로 통과시키지 않는다.

**GAP-N3 `WAITING_EVIDENCE`: 수정된 source/fixture와 위 계약이 포함된 새 packet을 받을 때 재심사.** 같은 revision의 목록 재조회나 GPU 확보만으로 자동 재개하지 않는다. 먼저 corrected source와 계약을 검토하고, 통과한 경우에만 resource/runtime/checkpoint/budget을 채워 사용자 선택 컴퓨터의 로컬 Docker에서 작은 qualification을 제안한다. 정책 이득을 실험 전에 입증하라는 gate는 아니다. Native effect는 이후 pilot의 질문이다.

원본 ID를 연결할 수 없거나, cue 제거가 시간/목표/예산까지 바꾸거나, target이 prompt/planner/evaluator에서 다르거나, 정답이 입력에 남으면 현재 비교를 중단한다. 계약을 고친 뒤에도 단순 층화·정상 정렬·동일 tuning으로 차이가 설명되면 새 선택 방법 주장을 기각한다. 별도 비자명한 조건 예측 없이 더 큰 학습으로 넘어가지 않는다. N1의 **72 episode는 미실행 수집 상한 초안(수집 0)**이며 실행 승인·검정력 보장이 아니다. 외부 연구자 피드백도 미확보다.

## 7. 저장소 검증

TODO·DATA-TRANSFER와 memory cross-link·navigation·당일 기록을 갱신한다. Registry 신규 등록, tier 및 사용자 reading 상태, 과거 보고서/실험 결과는 보존한다. 필수 유지보수 명령, canonical hash와 기존 dirty 변경 보존, 임시 source 정리의 실제 결과는 [ledger validation](../sources/proxy_observation_qualification_review_2026-10-25.json)에 기록한다. 이 검증은 문서/registry 무결성이며 연구 코드의 실행 결과가 아니다.
