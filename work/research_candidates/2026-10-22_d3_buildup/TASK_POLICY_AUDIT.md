# D3-L1 — 조리 task·정책·관측·평가 경로 자격 심사

> **후속 D3-R1 완료:** [추가 공개 근거](./R1_REVIEW.md)에서 원자료 파일 identity와 평가 수치의 실제 task/대상 범위를 확인했다. Gate NOT_MET, 연구 REVISE·실험 HOLD 유지. 아래는 L1 당시 기록이며 현재 다음 gate는 [R1 증거 명세](./R1_EVIDENCE_REQUIREMENTS.json)에 따른 D3-R2다.

- 확인일: 2026-10-22 KST. [D3 계약 §7](./TASK_CONTRACT.md#7-다음-비실험-작업의-완료-기준--d3-l1)의 네 항목을 비실험으로 검토했다.
- **작업 판정: D3-L1 DONE / 실행 자격 PARTIAL.** Task와 언어 입력을 받는 model 후보를 찾았다. 현재 공개 server/evaluator를 그대로 연결하는 비교는 D3의 언어 변경을 검증하지 못한다.
- **연구 판정: REVISE 유지.** 관측 가능한 사건 이후 목표 가능성 진단은 남기되, cooking full-task 비교·새 학습은 HOLD다. 이 판정은 D3 효과의 실험적 반증이 아니다.
- [Source/metadata ledger](./qualification_sources_2026-10-22.json), [비실행 interface 명세](./QUALIFICATION_SPEC.json), [유지보수 검증](VALIDATION.md#stage-1).

## 1. 이전 단계에서 달라진 점

| 이전 미확인 항목 | 이번 확인 | 의미 |
|---|---|---|
| Cooking용 공개 checkpoint | Task 45 전용 checkpoint와 cooking을 포함한 언어 LL 모델 발견 | ‘조리 모델을 찾지 못했다’는 이전 경계를 갱신한다. 각각의 interface/competence는 별도 심사 |
| 실제 demo coverage | 공식 2026 task 45 주석 200개를 모두 확인 | 원래 task의 기술 분해는 확인. 목표 변경 시연이나 Cooked event label 확보는 아님 |
| 지시 변경 경로 | evaluator는 task ID, 언어 LL server는 ID→고정 문장 사용 | 문자열을 보내기만 하는 실험은 무효. Model의 언어 경로와 serving interface를 구별해야 함 |
| 목표 평가 | 원래 BDDL goal·termination·Q-score가 고정되어 있음 | 지시만 바꿔도 평가 goal은 바뀌지 않는다. 별도 goal evaluator가 필요 |
| 관측 cue | RGB·proprio 경로와 texture state의 시각화 연결 확인 | 실제 camera에서 사건 전후 구별 가능성은 여전히 미검증 |

새 논문을 추가한 작업이 아니라 공개 자산과 source의 자격 심사다. Third-party checkpoint의 model card를 top-tier 논문의 결과로 사용하지 않는다. 사용자의 정독 상태도 올리지 않는다.

## 2. Task와 공개 데이터의 연결

공식 challenge task catalog에서 `cook_hot_dogs`는 두 hotdog를 fridge에서 꺼내 microwave로 조리하는 작업이며 scene model은 `house_single_floor`다. 공식 dataset metadata는 R1Pro, 30 Hz, 61차원 observation state, 23차원 action, head/양쪽 wrist의 RGB·depth를 명시한다. `chunk-045`의 data·episode metadata·video 파일 목록과 `annotations/task-0045/`를 확인했다. 실제 action/state Parquet·영상·HDF5는 읽거나 저장하지 않았다. [공식 task catalog](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/docs/challenge/task_data.json), [dataset schema](https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/blob/4f50b44796641a4d526a19d9aeadc8aa51e2f2c2/meta/info.json).

### 200개 annotation의 정적 감사

성능 측정이 아니라 공개 주석의 구조와 기술 coverage를 집계했다. 대상 200개, 읽기 성공 200개, 오류 0, skill segment 총 2,599개다.

| Annotation의 skill description | Segment 수 | 해당 skill을 포함한 episode 수 |
|---|---:|---:|
| move to | 400 | 200 |
| open door | 400 | 200 |
| pick up from | 600 | 200 |
| close door | 399 | 200 |
| place on | 200 | 200 |
| place in | 400 | 200 |
| turn on switch | 200 | 200 |

200개 모두 마지막 skill label은 `turn on switch`다. `turn off` label은 없었다. Fridge를 destination으로 적은 `place in`은 1개였지만, 그 주석만으로 복귀 동작의 실제 성공이나 cooked 이후 continuation을 인정하지 않았다. [해당 annotation](https://huggingface.co/datasets/behavior-1k/2026-challenge-demos/blob/4f50b44796641a4d526a19d9aeadc8aa51e2f2c2/annotations/task-0045/episode_00450220.json).

**이 집계가 지지하지 않는 것:** 주석의 마지막 동작 이후 물리 시간이 전혀 흐르지 않았다는 주장, 모든 시연이 실패했다는 주장, 전체 100개 task에 turn-off 기술이 없다는 주장, 조리 임계 시점의 label. Skill annotation은 object ID·frame interval·동작 이름을 주지만 Cooked 전이의 ground-truth timestamp를 주지 않는다. `turn on`의 시작/끝 frame을 `t_event`로 대체하면 안 된다. 200개 파일의 identity와 집계 범위는 ledger에 보존했다.

예시 annotation에는 `hotdog_207/208`, `fridge_dszchb_0`, `microwave_abzvij_0`가 나타난다. 이를 모든 instance의 같은 물체 ID로 일반화하지 않는다. 또한 annotation 파일명의 `00450010`을 dataset의 `episode_index`로 바로 해석하지 않는다. Namespace mapping은 독립 확인 대상이다.

### Scene instance와 version 경계

- 2025 공개 task-instance repo에는 `house_single_floor`의 해당 task template/instance 파일 목록이 있다. 이는 **2025 자산의 존재**이며 2026 evaluator와의 호환성 증거가 아니다. [2025 asset repo](https://huggingface.co/datasets/behavior-1k/2025-challenge-task-instances/tree/316fa44817dadc4798b61d0f262e69bdd0e3d93a).
- 현재 source는 `2026-challenge-task-instances/metadata/B100_task_misc.csv`를 요구한다. 해당 2026 repo의 익명 API 요청은 401을 반환해 metadata/instance manifest를 확인하지 못했다. 존재하지 않는다는 결론이나 2025 자료로의 대체를 하지 않았다. [loader](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/eval/utils/eval_utils.py#L60).
- 공식 baseline 안내의 `v3.9.3` ref는 이번 API 조회에서 해결되지 않았고 `v3.9.3-post1/post2` tag는 확인됐다. `post2=a8247a8…`에서도 Cooked/MaxTemperature 의미는 유지된다. 그러나 현재 main의 evaluator 경로, 2025 winner submodule, 2026 model을 한 호환 runtime으로 합쳤다고 주장하지 않는다. [안내](https://behavior.stanford.edu/challenge/baselines.html), [공개 tags](https://github.com/StanfordVL/BEHAVIOR-1K/tags).

## 3. 공개 정책 후보의 자격

| 후보 | 확인한 근거 | D3에서의 역할 / 판정 |
|---|---|---|
| P1: `Rena-Tian/b1k-2026-task45-ft1` | 공개 model card·파일 목록, revision `4658b90…`; task 45용. 저자는 task-ID embedding과 no-language-prompt 구조를 명시 | **자연어 변경 B0로 FAIL.** 원래 cooking competence의 참고 후보이나 우리 실행은 없음. 별도 symbolic skill executor 역할도 재자격 필요 |
| P2: `hanbin5/pi07-ll-b1k-200k` | 공개 card/config, revision `c4c6946…`; π0.5 기반 third-party LL, cooking 포함 18 task. Text token→VLM prefix→action expert 경로 source 확인 | **후속 interface 후보로 PARTIAL.** Model은 언어를 받지만 stock server가 외부 수정 문장을 처리하지 않으며 full-task competence는 미확보 |
| P3: `0Corvid0/pi05-b1k-eval-checkpoints` | 공개 card·API metadata, revision `7ecd470…`, cooking 포함 25 task, access gate 있음 | **보조 discovery 후보.** 조건 동의나 파일 접근은 하지 않았다. Card의 cooking 100%는 이 모델의 성능이 아니라 Ilias-expert baseline 값임 |
| 공식 2026 π0.5/GR00T baseline | 공개 recipe 및 checkpoint 표 | 안내된 checkpoint는 radio용. Cooking용 native competence로 대체하지 않음 |

근거: [P1 model card](https://huggingface.co/Rena-Tian/b1k-2026-task45-ft1/blob/4658b90b189ec5824579cf12bf53834c1409150f/README.md), [P2 model card](https://huggingface.co/hanbin5/pi07-ll-b1k-200k/blob/c4c6946a9e61a9826616977a037a7e28526fcb6b/README.md), [P2 config](https://huggingface.co/hanbin5/pi07-ll-b1k-200k/blob/c4c6946a9e61a9826616977a037a7e28526fcb6b/config.json), [P3 card](https://huggingface.co/0Corvid0/pi05-b1k-eval-checkpoints), [공식 baseline](https://behavior.stanford.edu/challenge/baselines.html).

P1 저자는 public instance 10개에서 `q=0.6`을 보고한다. 이는 독립 재현이 아니고 변경 지시 성공률도 아니다. 기반 winner source의 `tokenized_prompt`라는 이름은 자연어를 뜻하지 않는다. `embed_prefix()`가 첫 두 값을 task ID와 stage로 읽는다. Adapter가 `prompt` 필드를 보존한다는 사실만으로 language conditioning을 인정하면 안 된다. Rena의 수정 training pipeline 전체를 확보한 것은 아니므로 기반 코드와 model-card 주장을 구분한다. [winner prefix](https://github.com/IliaLarchenko/behavior-1k-solution/blob/ca556f74a455cef7987a2be4537b5ac85cc56dd7/src/b1k/models/pi_behavior.py#L520).

P2는 action expert만 공개하며 frozen VLM/base는 별도다. 저자가 보고한 검증은 open-loop action error와 제한된 skill 수행이다. Full-task 성공률은 미측정이라고 명시되어 있다. Skill 평가도 demo start로 복원한 상태와 정답 subtask, 조건에 맞는 segment만 사용하므로 D3 continuation competence의 증거가 아니다. 이를 실패한 정책으로 확정하지도 않는다. 공식 π0.7 release로 부르지 않는다.

## 4. 언어·action의 실제 source 경로

P2의 공개 source revision은 `inner-king/policy@ec298b7…`다. 다음 구분은 실행 없이 확인한 데이터 흐름이다.

| 경로 | 확인 | D3에 필요한 변화 |
|---|---|---|
| evaluator → policy | `_preprocess_obs`는 `task_id`를 붙임. 기본 task observation은 `include_obs=false` | 외부 `instruction`과 버전을 별도로 보내는 protocol 필요. Simulator predicate 정답을 함께 보내면 안 됨 |
| server `_parse` → `act` | RGB/proprio/task ID를 읽고 local index의 `task_by_id`에서 고정 `instr`를 꺼냄 | 새 요청 문장을 받는 경로가 없음. Dictionary에 prompt key를 추가하는 것만으로는 효과 없음 |
| `pi07_prompt` → `LLPolicy.tokenize/encode_prefix` | 실제 text token이 VLM에 들어가 action sampling의 KV cache에 연결됨 | model 차원의 language 경로는 있음. 외부 지시 반영 효과·사용 능력은 미측정 |
| server action queue | LL chunk에서 앞 25개 action을 queue에 저장. 내장 HL의 subtask 변경 때 queue를 비움 | 외부 지시 변경에도 동일한 stale-chunk 취소와 새 inference를 적용해야 함 |
| evaluator client queue | 옵션으로 server chunk를 받아 cache. Cache가 남으면 새 obs를 송신하지 않고 action 반환 | client와 server 양쪽 queue를 무효화해야 함. 한쪽만 비우면 지연 교란이 남음 |

근거: [evaluator L576](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/eval/evaluator.py#L576), [P2 server L182–250](https://github.com/inner-king/policy/blob/ec298b7ebe46880abe4264032db9c98b1988485c/pi07/src/pi07/serve_pi07.py#L182), [model L127–213](https://github.com/inner-king/policy/blob/ec298b7ebe46880abe4264032db9c98b1988485c/pi07/src/pi07/models.py#L127), [client cache L113](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/eval/utils/network_utils.py#L113).

P2 server는 local `B1KIndex`에 의존하며 model card도 원 setup 밖에서 그대로 실행되지 않는다고 명시한다. Unknown task ID를 다른 task로 fallback하는 경로도 있다. D3에서는 명시적 오류로 다뤄야 하며 silently 다른 task를 실행한 결과를 사용할 수 없다. 공개된 high-level/WM 코드가 있다고 해당 weights도 공개된 것으로 간주하지 않는다.

**중단 행동도 수정해야 한다.** 현재 R1Pro 설정의 arm/trunk는 absolute-position JointController다. 23차원 zero action은 일반적인 ‘현재 자세 유지’가 아니다. Hold는 base velocity 0, 현재 arm/trunk command와 gripper 상태를 유지하는 controller 의미로 정의하고, 열원 차단은 별도 mitigation으로 다뤄야 한다. 실제 안정성은 미검증이다. [robot/controller config](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/eval/r1pro.yaml).

## 5. 관측 가능성과 목표 평가

### 관측: PARTIAL

DefaultWrapper는 224×224 RGB이며 RGBD full-resolution wrapper와 다르다. P2는 RGB 세 view와 proprio를 사용한다. Depth를 추가한 system과 같은 조건으로 비교했다고 부르면 안 된다. `USDObject`는 활성 visual state 중 우선순위에 따라 texture change를 적용한다. 따라서 Cooked 함수의 존재에서 실제 camera cue까지 가려면 state 활성화, visual priority, occlusion, rendering timestamp를 확인해야 한다. [DefaultWrapper](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/eval/wrappers/default_wrapper.py), [visual update](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/objects/usd_object.py#L845).

공식 ontology의 hotdog는 cookable/heatable 상태를 지원하지만, 이것만으로 microwave 문이 닫힌 상태에서도 Cooked를 식별할 수 있다는 결론은 나오지 않는다. [공식 object taxonomy](https://behavior.stanford.edu/knowledgebase/synsets/hotdog.n.02.html). RGB 구분이 불가능하면 history/inspection이 허용된 조건으로 수정하거나 해당 case를 제외해야 한다. 사건 정답을 숨긴 채 oracle처럼 행동하라고 요구하지 않는다.

### Goal/termination: 현재 runner는 D3 변경 평가로 FAIL, 수정 지점은 확인

`BehaviorTask`는 compiled BDDL goal을 `PredicateGoal`과 Q-score의 기준으로 사용한다. `update_activity()`는 scope·compiled task를 재구성하는 경로이며 안전한 mid-episode goal 교체 API로 자격화하지 않았다. `show_instruction()`은 표시 기능으로, model 입력이나 goal 교체 기능과 다르다. [task source](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/tasks/behavior_task.py#L353).

`PredicateGoal`은 기존 goal이 참이면 종료하고, env는 설정에 따라 자동 reset할 수 있다. 성공 시점 이후의 상태를 조사하려면 D3 runner가 world state를 유지하면서 원래 task 종료와 새 goal 종료를 분리해야 한다. 현재 loop 그대로는 모든 post-event continuation을 측정할 수 있다고 볼 수 없다. [termination](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/termination_conditions/predicate_goal.py#L38), [env step](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/envs/env_base.py#L775).

현재 Q-score는 episode 시작 때와 종료 때의 **같은 goal predicate**를 비교한다. Goal을 교체하고 initial mask를 그대로 쓰면 분모·predicate 대응이 달라질 수 있다. D3는 switch 시점의 새 goal·독립 만족 여부·추가 위반을 별도로 기록하고 원 challenge Q-score와 섞지 않는다. [metric source](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/metrics/task_metric.py).

## 6. 공정 비교를 위한 최소 수정 계약

[QUALIFICATION_SPEC](./QUALIFICATION_SPEC.json)은 **미구현 contract**이며 실행 manifest가 아니다. 다음 수정은 baseline/평가를 유효하게 만드는 작업으로, 새로운 연구 기여로 주장하지 않는다.

1. 요청에 episode ID·instruction version·새 문장을 넣고 응답에 적용 version을 남긴다. Model prompt까지 값이 전달되는지 확인한다. 환경 task ID는 goal 변경의 대용물이 아니다.
2. 지시 변경 시 client/server의 pending action과 stale subgoal을 함께 무효화한다. Observation/event history는 보존 여부를 모든 baseline에 동일하게 적용한다. Episode reset으로 세계를 되돌리지 않는다.
3. 기존 BDDL scope를 고정하고 **evaluator 전용** 새 goal predicate를 별도 관리한다. Object replacement·Cooked setter·state restore를 online action으로 사용하지 않는다.
4. 모든 비교가 같은 controller·hold·inspection·mitigation option을 쓴다. 시간을 멈춰 판단하거나 queue 시간을 제외한 이득을 허용하지 않는다.
5. `t_request`, `t_ack`, `t_event`, 첫 새 action과 goal outcome을 구분한다. Latency 통제 후에도 효과가 남는지를 묻는다.

| 비교 | 현재 자격 | 이유 |
|---|---|---|
| B0: native VLA + 변경 지시 | PARTIAL | P2 model 경로는 있지만 stock serving/competence 미자격 |
| B1: 항상 hold/report | PARTIAL | Controller 의미는 확인. 안전 hold·열원 mitigation 실행은 미검증 |
| B2: VLM planner + 같은 LL | PARTIAL | 같은 P2를 쓰는 설계 가능; planner·tool·정보·runtime 고정 전 |
| B3: 추정 predicate + 단순 planner | PARTIAL | Goal check는 구체화 가능; 사건의 policy-visible cue 미자격 |
| B4: oracle predicate 진단 | PARTIAL | Source invariant/goal 경로 확인; 실제 event snapshot와 witness 없음 |

## 7. 연구 가치와 다음 판단

**가능성을 높인 근거:** 실제 task·200개 annotated demonstration·language-capable model path가 있어, 전혀 새 환경과 정책을 처음부터 만들 필요는 없을 수 있다. **본격 실험을 아직 추천하지 않는 이유:** 외부 지시 전달·목표 evaluator가 현재 runner에 없고, 관측 가능한 사건 시점과 수정 후 행동 competence를 확보하지 못했다. 자원만의 문제가 아니다.

남는 질문은 여전히 ‘같은 관측과 시간에서 상태 기반 단순 재계획 이후에도 VLA의 행동 전환 문제가 남는가’다. Source wiring을 고친 이득, 정답 상태를 더 준 이득, 약한 base policy를 교체한 이득은 D3의 신규성을 입증하지 않는다. 단순 rule `Cooked=true ∧ same-object-uncooked-goal → 불가능` 자체도 새로운 방법이 아니다.

**D3-R1 재개 근거를 다음 gate로 둔다.** (a) 동일 instance에서 event 전후를 연결하는 공개 관측/상태 근거, (b) 공개 language LL의 필요한 continuation/mitigation을 지지하는 source·기존 결과 또는 향후 허용된 competence 검증, (c) 수정 protocol 아래 같은 task를 수행하는 공정 비교가 필요하다. 모든 효과를 실험 전에 입증하라는 뜻은 아니다. 비실험으로 확인 가능한 공개 자료는 계속 검토할 수 있지만 같은 recipe·문서만 반복해 GO로 올리지 않는다.

현재 full-task 설계와 D3-E1은 HOLD_RESEARCH, D3-R1은 WAITING_EVIDENCE다. 작은 adapter가 필요하다는 사실만으로 연구를 기각한 것이 아니며, 실행 자격과 진단 질문의 과학적 가치를 분리했다. 실제 외부 피드백은 미완료다. D1/D2/C1–C6를 재개하지 않았다.
