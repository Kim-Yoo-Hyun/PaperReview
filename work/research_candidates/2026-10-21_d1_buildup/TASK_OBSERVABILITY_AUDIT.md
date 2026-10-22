# D1-L3 — 실제 task·관측 경로 적합성 감사

- 후속 [N3 반대 심사](./NONEXPERIMENTAL_REVIEW.md#3-d1-n3--현재-task의-적합성-반대-심사): 아래 task는 operator 진단 후보이며 핵심 novelty의 자격을 얻은 task가 아니다. Source 사실은 유지하며 현재 method NO-GO·진단 HOLD, 재개 gate는 R2다.
- 검토일: 2026-10-22 KST. [TODO](../../../TODO.md)의 D1-L3 완료 산출물.
- Evidence: 공식 공개 source의 task definition·선택한 코드 경로를 정적으로 검토했다. Policy 추론·simulator·학습·upstream code import는 수행하지 않았다.
- 원자료: [source identity와 40개 task의 goal 추출](./task_sources_2026-10-22.json), [실행 불가능한 후보 명세](./TASK_CANDIDATES.json).
- 절차: [기존 buildup 가이드](../../../research/IDEA_BUILDUP_GUIDE.md)의 가정/interface 비교 → 경쟁 가설 → 주장/증거 → 내부 반박. 실험·외부 피드백 완료를 뜻하지 않는다.

## 1. 이번 결정

**기존 primary `pi05_libero`는 state 값만 보정하는 D1 비교에서 제외한다.** 입력 packet에 state가 있어도 확인한 native config의 action 계산에는 그 값이 연결되지 않는다. 앞선 dossier가 입력 interface의 존재를 근거로 이 모델을 primary로 선정한 것은 충분하지 않았다. 이번에 value path를 확인하여 수정했다.

**OpenVLA-OFT의 proprio-enabled LIBERO-Goal variant를 후속 primary 후보로 변경한다.** State token 경로와 공개 asset 위치는 확인했지만 clean competence·state의 실제 유용성은 미검증이다. 실행 준비 완료로 승격하지 않는다.

Task는 `libero_goal`의 **0: 중간 서랍 열기, 8: 그릇을 접시에 놓기**를 1차 후보로, **1: 그릇을 스토브에 놓기**를 goal contrast로, **7: 스토브 켜기**를 보조 후보로 정한다. 모두 `task_order_index=0` 기준이다. 이 task들이 D1의 신규 현상을 입증한다는 뜻은 아니다.

## 2. Native state 경로 — 가장 중요한 전제 수정

### π0.5 LIBERO: packet의 state와 모델이 쓰는 state 구분

아래는 openpi commit `215abfb217dbac7d5f1273282331b9b1866c0479`의 **지정 config**에 한정한 dataflow 판단이다.

| 연결 | 확인 사실 | 근거 |
|---|---|---|
| Client → packet | RGB 2개, language, 8D state를 전송 | [LIBERO client L130–141](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/libero/main.py#L130) |
| Config → tokenizer | `pi05=True`, `discrete_state_input=False`; tokenizer에 state를 넣지 않음 | [config L744–749](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L744), [TokenizePrompt](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/transforms.py#L248) |
| State → continuous suffix | JAX/PyTorch 모두 continuous state embedding은 `not pi05` 조건 안에 있음 | [JAX L151](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/pi0.py#L151), [PyTorch L244](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models_pytorch/pi0_pytorch.py#L244) |
| Output → action | `extra_delta_transform=False`; state를 action에 다시 더하는 변환도 없음 | [config](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L336), [policy transform 조립](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/policies/policy_config.py#L75) |

**연구자 도출:** 같은 유한 shape, RGB·prompt·noise/RNG, 수정하지 않은 경로라면 state **값만** 바꾸어 action이 달라질 경로가 없다. State shape은 batching에 사용되므로 “state 필드 자체가 필요 없다”는 주장은 아니다. Runtime parity나 rollout 성공률을 측정한 것도 아니다.

따라서 G-PSMR M2 같은 state-value-only wrapper의 이득을 이 variant에서 기다리는 것은 부적절하다. 이는 checkpoint의 전반적 성능 실패나 모든 π0.5 모델의 한계가 아니다. Physical robot/controller 변화는 RGB·실제 운동을 바꿀 수 있어 여전히 영향을 줄 수 있다. 단순히 config의 state flag를 켜는 것은 기존 checkpoint의 native 재현을 유지하는 해결책이 아니다.

### OpenVLA-OFT: 경로 존재와 유용성 분리

OFT commit `e4287e94541f459edc4feabc4e181f537cd569a8`의 기본 L1-head·`use_proprio=True` 경로에서는 state를 normalize하고 proprio projector로 embedding한 뒤 vision token에 붙여 action을 예측한다. [Eval config](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/libero/run_libero_eval.py#L97), [inference 전달](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/openvla_utils.py#L772), [model token 경로](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/prismatic/extern/hf/modeling_prismatic.py#L1005).

공식 [LIBERO recipe](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/LIBERO.md#L65)의 Goal asset은 `moojink/openvla-7b-oft-finetuned-libero-goal`이다. [Model repository revision](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal/tree/c2d0f9fbbd82674683b397ff923168a12f6a307b)은 `c2d0f9fbbd82674683b397ff923168a12f6a307b`; 목록에 50,000-step action head·proprio projector가 있다. 이전 Spatial asset의 150,000-step sidecar와 혼용하지 않는다. Weight·normalizer payload는 읽거나 내려받지 않았다.

State 경로가 존재해도 학습된 policy가 이를 유용하게 쓰는지는 G1에서 확인해야 한다. π0.5와 OFT의 차이를 state 유무의 공정한 ablation으로 사용하지 않는다. 서로 다른 backbone·training·timing이다.

## 3. Task identity와 성공 조건

Openpi의 실제 LIBERO gitlink는 `f78abd68ee283de9f9be3c8f7e2a9ad60246e95c`다. 조사 시 최신 upstream `8f1084…`를 발견했지만 native source 판정은 gitlink 기준으로 다시 했다. [gitlink](https://github.com/Physical-Intelligence/openpi/tree/215abfb217dbac7d5f1273282331b9b1866c0479/third_party), [suite map](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/benchmark/libero_suite_task_map.py), [task order·prompt 생성](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/benchmark/__init__.py#L44).

OFT recipe는 LIBERO를 clone하지만 commit을 고정하지 않는다. 위 commit은 **이번 task-definition 기준 및 후속 공통 환경 후보**다. OFT 원 실험의 환경 commit으로 확인된 것이 아니며 아직 runtime freeze가 아니다. Openpi client lock과 OFT requirements 모두 robosuite 1.4.1을 지정하는 것은 확인했다.

| Suite / ID / 역할 | 정확한 slug와 goal | 성공 판정의 의미 | D1 적합성 |
|---|---|---|---|
| `libero_goal` / 0 / articulated primary | `open_the_middle_drawer_of_the_cabinet`; Open(middle region) | 해당 drawer slide joint가 open threshold를 넘는지 | Contact/상태 진행 검사 후보. 절대 EEF orientation 목표는 아님 |
| `libero_goal` / 8 / placement primary | `put_the_bowl_on_the_plate`; On(bowl, plate) | Contact, bowl 높이와 두 object 중심의 xy 관계 | 움직인 target에 맞게 행동하는지 검사 후보. 필요 보정 방향이 다르다는 증거는 아직 없음 |
| `libero_goal` / 1 / goal contrast | `put_the_bowl_on_the_stove`; On(bowl, cook region) | Site 영역·높이와 parent stove contact | Task 8과 같은 bowl·다른 목표. Language utility 검사 후보 |
| `libero_goal` / 7 / 보조 | `turn_on_the_stove`; Turnon(stove) | Stove hinge joint threshold와 연결된 상태 | Visual-progress/affordance 대조. 명확한 시각 cue로 너무 쉬울 가능성도 검사 |

직접 BDDL: [0](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/open_the_middle_drawer_of_the_cabinet.bddl), [8](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/put_the_bowl_on_the_plate.bddl), [1](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/put_the_bowl_on_the_stove.bddl), [7](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/bddl_files/libero_goal/turn_on_the_stove.bddl).

Predicate → object state → object implementation까지 확인했다. Drawer는 `q < −0.14`인 slide, stove는 `q ≥ 0.5`인 hinge 조건이다. Object–object On은 contact·높이와 xy 중심 거리 0.03 미만을 검사한다. 이는 grasp 해제·안정 유지 시간을 별도로 요구하는 성공 규칙이 아니다. [Object state 판정](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/object_states/base_object_states.py#L78), [articulation threshold](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/objects/articulated_objects.py#L173), [site 판정](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/objects/site_object.py).

**이름만으로 정의하지 않는다:** Native prompt는 filename에서 만들어진다. Task 0의 BDDL language는 native prompt와 다르다. Task 3의 이름에는 drawer를 여는 행동이 있지만 최종 goal은 bowl의 In predicate이며 별도 Open conjunct가 없다. Task 6의 이름은 “in the bowl”이지만 실제 goal은 On이다. 이는 오류라고 단정할 근거가 아니라 language·경로·종료 조건을 분리해야 할 이유다.

## 4. 목표 대조의 가능성과 한계

Spatial/Object/Goal/10의 **40개 BDDL**에서 terminal goal을 구조적으로 읽었다. Atomic predicate 출현은 On 24, In 20, Open 1, Turnon 3, Close 2개다. Compound goal 때문에 합계는 task 수와 다르다. 이 goal들에는 절대 EEF orientation을 직접 요구하는 predicate가 없다. LIBERO-90의 전체 task까지 조사한 결과는 아니다.

따라서 이전에 검토하려던 **“absolute EEF orientation 필수 task 대 relative-goal task” 대조는 이 범위에서 확보하지 못했다.** Orientation이 grasp/contact/control에 중요하지 않다는 뜻은 아니다. 물체 간 상대 목표도 gravity·collision·reachable workspace 때문에 임의 SO(3) 변환에 invariant하지 않다.

Goal 10개는 regions·fixtures·objects·symbolic init 구조 hash가 모두 같다. Task 8↔1은 같은 source scene 구조에서 목표를 바꾸기 좋은 후보지만, `.pruned_init`의 binary state와 렌더링이 같은지는 확인하지 않았다. Task마다 같은 숫자의 initial-state index를 쓰는 것만으로 paired scene이 되지 않는다. Shared physical reset과 두 predicate의 initial truth, instruction 전환 뒤 evaluator goal을 함께 검증해야 한다.

**질문 수정:** 절대 자세 목표의 일반적 반례를 이미 갖췄다는 주장을 내려놓고, **report 오류 보정이 실제 목표 변화에 대한 반응을 훼손하는지**를 task별로 검사한다. Simple residual·causal 재보정·task reference가 충분하면 새 방법은 필요하지 않다.

## 5. Policy-visible / controller / evaluator 경계

| 경로 | Source에서 확인한 조건 | 실험 설계에 주는 제한 |
|---|---|---|
| Images | Agentview와 eye-in-hand RGB; native client의 180° 회전·resize/crop 적용 | Native image transform 유지. Extra view/depth·render segmentation은 추가 정보 |
| State | EEF position 3 + quaternion→axis-angle 3 + gripper qpos 2 | Object pose·drawer joint·fault label을 이 8D에 넣지 않음 |
| Orientation frame | Report quaternion은 EEF body, controller orientation은 grip site에서 읽음 | 두 회전의 고정 transform을 확인하지 않고 residual에 직접 대입하지 않음 |
| Action | OSC_POSE의 delta position·axis-angle rotation 6 + gripper 1 | Absolute pose command로 해석 금지. Action scale/rotation composition 유지 |
| Controller feedback | Simulator site pose·joint/dynamics를 직접 읽음 | Policy packet만 수정한 오류는 controller feedback fault가 아님 |
| Evaluator | Sim object pose/contact/joint로 goal predicate 계산 | Success·true pose·fault onset은 method 입력으로 전달하지 않음 |
| Extra observation keys | Environment는 object state 등을 포함할 수 있지만 native packet은 선택한 필드만 전달 | `obs` 전체를 estimator에 넘기면 privileged leakage가 생길 수 있음 |

기준 source: [native wrapper](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/f78abd68ee283de9f9be3c8f7e2a9ad60246e95c/libero/libero/envs/env_wrapper.py#L12), [robot sensor·controller 연결](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/robots/single_arm.py#L304), [controller feedback](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/controllers/base_controller.py#L139), [OFT action mapping](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/libero/run_libero_eval.py#L265).

Robosuite 1.4.1의 default OSC는 input을 ±1로 clip하고 position 축별 ±0.05 m, rotation 축별 ±0.5 rad로 scale한다. Translation은 현재 world position에 더하며, nonzero rotation update는 delta rotation matrix를 현재 orientation에 왼쪽 곱한다. Zero rotation command에서 orientation goal을 갱신하지 않는 분기도 있으므로 매번 현재 자세를 그대로 목표로 삼는다고 가정하지 않는다. 이는 최종 실제 이동량 보장이 아니다. [OSC config](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/controllers/config/osc_pose.json), [goal 구성](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/utils/control_utils.py#L150), [zero-update 분기](https://github.com/ARISE-Initiative/robosuite/blob/c848ca848020d0c4ccdd10c5056bd06f2a195ba2/robosuite/controllers/osc.py#L257).

**설계 해석:** 실제 자세 교란에서 기존 low-level controller가 복원하는 효과도 baseline에 포함된다. Controller의 과거 goal·filter 상태를 누락한 reset이나 policy state만 본 해석으로 learned correction의 필요성을 주장하지 않는다.

Default environment는 20 Hz action step이다. Openpi는 10-step 예측 중 5개를 실행하고 OFT는 기본 8개를 실행한다. 따라서 nominal simulation 시간의 재관측 간격은 각각 0.25 s/0.40 s다. 실제 wall-clock latency는 측정하지 않았다. Policy 없는 chunk 중간에 새 RGB를 읽는 wrapper는 관측 예산이 늘어난 것이다. Primary OFT와 그 wrapper는 같은 queue를 유지해야 한다.

OFT state normalization은 bounds/quantile scaling 후 clipping한다. Corruption·correction은 raw pose/rotation 표현에서 정의하고 변환·normalization 순서를 고정해야 한다. 큰 오류가 clipping으로 같아진 경우를 원인 식별 불능과 혼동하지 않는다. [Normalizer](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/openvla_utils.py#L649).

## 6. 관측 가능성은 아직 조건부다

아래는 source 기반 설계 해석이다. 실제 rendered visibility·pose-estimator error·identifiability를 측정한 결과가 아니다.

| Intervention 후보 | 무엇이 바뀌는가 | 가능한 cue / 실패할 수 있는 조건 | 판단 |
|---|---|---|---|
| Policy report-only pose bias | Packet의 state 값; scene/진짜 controller는 유지 | RGB와 proprio의 불일치. Occlusion·gripper 대칭·미지 calibration이면 구별이 어려움 | OFT에서 검토 가능. 관측 가능성 보장 없음 |
| 실제 robot pose 변화 | Physics, controller, RGB·wrist view·state가 함께 변화 | 일관된 visual/kinematic 변화 | Joint range·collision·contact·velocity를 만족하는 perturbation 계약 필요. qpos teleport만으로 현실적 외력을 주장하지 않음 |
| Target plate 이동 | 목표 위치/영상 변화; robot state 자체는 같을 수 있음 | Goal 8에서는 target, Goal 1에서는 비목표 물체 | 후자도 장애물이 될 수 있으므로 “완전 무관”이라고 가정하지 않음. Robot-state 오류의 동일 matched cause pair도 아님 |
| Drawer/stove 진행 변화 | Object articulation·시각 cue | Native 8D에 object joint는 없음 | Progress control. Simulator joint를 method에 주면 누출 |
| Camera 오류 | RGB와 image geometry; controller state는 유지 | Fixed scene cue가 있을 수 있음 | Camera calibration/pose를 oracle로 주지 않음. 별도 fault axis |

실제 물리 변화와 report 오류가 **동일한 full policy history**를 만드는지, 각 조건에서 최선의 행동이 다른지는 아직 미확인이다. Task source만으로 그 두 조건을 증명했다고 말하지 않는다. 식별이 안 되면 cause label 정확도를 요구하지 않고 보수적 행동·보류의 utility로 수정한다.

## 7. Buildup 판정과 다음 TODO

- **완료:** Task 40개의 goal 구조 감사, 후보 4개 ID/goal 고정, native packet부터 모델·controller까지 경계 확인, 이전 primary의 state-value 전제 실패 발견, 대체 후보의 경로 확인.
- **이번 제외:** `pi05_libero`의 state 보정 primary 역할. 별도 vision-language reference로는 남길 수 있지만 OFT의 matched vision-only baseline은 아니다. 모든 π0.5·전체 D1을 기각한 것은 아니다.
- **남은 연구 가치:** Target/진행 변화와 잘못된 report에 대한 task utility를 통제하는 조건부 진단은 검토 가능하다. Strict absolute-orientation claim과 새 cause-conditioned 학습 방법의 필요성은 지지하지 못했다. 큰 학습은 계속 HOLD다.
- **후속 D1-L4 완료:** 선택한 OFT/task의 perturbation 위치·물리 타당성 gate·shared reset·split·관측/계산 예산은 [비실험 계약](./PRE_EXPERIMENT_CONTRACT.md)과 [설계 spec](./PILOT_SPEC.json)에 기록했다. 실제 물리 validity·run artifact·payload hash는 미검증/unchecked/null로 유지한다. 다음은 D1-E1 G0/G1이다.

실험 제약 외에도 **정책 경로와 task formulation 자체의 부적합**이 있었다. 자원이 생기면 바로 기존 π0.5 pilot을 실행하는 계획은 철회한다. OFT의 G0/G1을 통과하고 단순 baseline 이후 잔여 gap이 있어야 방법 구현을 검토한다.
