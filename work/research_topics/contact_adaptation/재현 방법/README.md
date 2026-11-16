# 접촉 적응 후보 — 공개 구현과 재현 준비 범위

Updated: 2026-11-09 KST. **GAP-CONTACT-RL-P0-PREP 실행 자료 작성 완료 / NVIDIA native 검증 대기.** [연구 내용](../내용/README.md#n2-contract), [source·검증 원장 `contact_n1`·`contact_n2`·`contact_p0_prep`](../../../sources/vla_rl_additional_gaps_2026-11-09.json), [TODO](../../../../TODO.md)를 따른다. Docker recipe·제한된 sensor/controller probe·launcher를 작성하고 Docker stdlib16검사를 통과했다. Native image build·physics/RGB·정책 효과는 미검증이다. 아래 N2 `proposed` 값은 학습 비교의 설계값이며 P0 실행 결과가 아니다.

## 이번 실제 수행

N1/N2에서는 저자 본문과 ContactBench collector·sensor·gain 경로, RLinf π₀/Flow-SDE/PPO, Newton1.5.0을 정적으로 대조했다. 후속 P0-PREP에서는 현재 local Docker를 확인하고 재개 코드를 작성했다. 실제 결과는 [준비 이력](#preparation-history)에 구분한다. Source 문자열 열람과 Docker stdlib 검사 이외의 모델 inference·학습·simulation은 없으며 host package·PDF·weights·mesh payload를 설치/다운로드하지 않았다.

| 구현 | 고정 revision·확인 범위 | 사용할 수 있는 것·한계 |
|---|---|---|
| [ContactBench simulation](https://github.com/Michaelwyx/contactbench-sim/tree/ccd864501275112e369a71c91880adf2da28b536) | `ccd864501275112e369a71c91880adf2da28b536`; README, package metadata, charger task/variant, `Rig` 선택 구간 | asset/task/scripted baseline 출발점. 저자 README가 policy learning/evaluation pipeline 미포함을 명시. 본문 전체 task 수와 이 release의 지원 row 수는 구별 |
| [FACET](https://github.com/PINE-Lab-NTU/FACET/tree/174c33cc680a7c08130908cfbe78357a04d061c5) | `174c33cc680a7c08130908cfbe78357a04d061c5`; README, hierarchy, refinement train, adaptation policy | 접촉 post-training·관측 계약 참고. `JointPolicyHierarchy`는 두 policy; refinement는 VL backbone freeze와 trainable filter 사용. 작은 synthetic CPU 경로를 native VLA 재현으로 간주하지 않음 |
| [openpi-RLT](https://github.com/Yyshadow/openpi-RLT/tree/c1e40ac360185778c98cf20da2820e22d2d415e7) | `c1e40ac360185778c98cf20da2820e22d2d415e7`; README | TORL project에 연결돼 있으나 README는 **RLT 재현**. TORL의 stage actor 구현을 확보했다고 쓰지 않음 |
| [CompVLA](https://compvla.github.io/) | 저자 연결 `compvla/CompVLA`를 web·GitHub API로 확인, 404 | 접근 가능한 code 미확보. Drive dataset 링크 존재만 확인; payload·권한·episode 내용 미검증 |
| [TacCoRL](https://tac-corl.github.io/) / [FORGE](https://noseworm.github.io/forge/) | project outgoing link 확인 | TacCoRL의 code/checkpoint 링크 미식별, FORGE code는 Coming Soon. 논문에 등장한 RL framework를 논문 구현과 동일시하지 않음 |
| ForceRFT / CG-RL | 지정 논문 본문·출처 링크 | 이번 확인 범위에서 공식 code link 미식별. 미공개라고 단정하지 않음 |

공개 repo 전체를 검증한 것은 아니다. 원장에는 읽은 파일의 URL·SHA256·선택 구간을 남기며 단순 fetch와 내용 검토를 구분한다. 새 논문 registry 등록·읽기 status 변경은 없다.

<a id="task-interface"></a>
## Charger source에서 확인한 실행 경계

**선택 row:** `plug_in_charger_block1` 및 저항 변화 row `plug_in_charger_block1_spring_0.85mm`. `tasks/plug_insert_arm.py`는 원 insertion/extraction script이고 실제 benchmark ending은 `appendix_tasks/plug_in_charger.py`와 `plug_in_charger_blocks.py`가 교체한다. 원 script만 실행하고 논문의 삽입·손 떼기 task를 재현했다고 쓰지 않는다.

- [`ChargerBlockVariant`](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/appendix_tasks/plug_in_charger_blocks.py)의 `configure`, `should_cut`, `ending`, `_press`, `criteria`를 확인했다. 위치 보정 offset·solver `impratio=10`·settle 보정과 상단 누르기까지 동작에 영향을 준다. 이 경로를 그대로 policy action 뒤에 남기면 scripted 도움을 VLA 성능으로 셀 수 있다.
- [`ChargerVariant.criteria`](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/appendix_tasks/plug_in_charger.py)는 simulation depth/force와 phase window를 사용한다. 이는 evaluator 근거이지 robot actor가 접근 가능한 관측이라는 뜻이 아니다. 새 actor의 phase가 scripted phase와 다르면 success/ending 검사를 그대로 재사용할 수 있는지도 점검해야 한다.
- [`Rig.drive_arm`](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/rig.py#L638)은 IK 해를 joint position target에 쓴다. 이 함수에 stiffness action argument는 없다. `Rig.run`은 callback loop다. 선택 source에서 VLA용 reset/step·action-space 계약을 확보한 것은 아니다.
- [`probe_charger.py`](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/examples/force_response/probe_charger.py)는 로봇 없는 기구 force probe다. 그 결과를 robot policy 또는 wrist sensor 검증으로 재사용하지 않는다.
- [촉각 설명](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/docs/tactile.md)의 fingertip GelSight와 객체별 contact force는 wrist 6D F/T와 다르다. N2는 아래의 이상적 fingertip 3D 합력 두 개를 선택했으며 실제 tactile 장비로 재현됐다는 뜻이 아니다.

따라서 **자산 후보 확보 ≠ 학습 가능한 환경 확보**다. 첫 구현에서 controller 교체·gain 적용, 관측 분리, autonomous termination, reset/RNG/phase 상태 보존, 학습 자료 수집 및 action normalization이 필요하다. 정확한 코드 양이나 일정을 실행 전 확정하지 않는다.

<a id="n2-interface"></a>
## N2 입출력과 controller 계약

아래는 **선정한 설계**, source에서 확인한 실제 기본값, 앞으로 확인할 runtime 조건을 구분한 것이다. `contact_n2.contract`에 같은 계약의 기계 판독용 값과 미구현 상태를 기록한다.

| 항목 | 고정할 의미·shape·시점 |
|---|---|
| RGB | 실제 동역학 state에서 렌더한 base RGB 1뷰. 224×224, 동일 camera/extrinsics; 나머지 π₀ image slot은 mask=false. Camera는 초기 nominal scene에서 정해 world에 고정하고 정답 object pose를 따라 움직이지 않음. Extrinsics 수치·가시성은 P0에서 확정; 원 video frame을 timestamp 확인 없이 obs에 붙이지 않음 |
| Language | `Insert the charging block into the outlet, release it, and move the gripper away.` 고정. Spring/성공/phase 정답을 prompt에 넣지 않음 |
| State 0:9 / 9:18 | 실제 FR3 arm7+finger2 joint position / velocity. Initial `model.joint_q`가 아닌 현재 `state.joint_q/qd` |
| State 18:24 / 24:30 | left/right fingertip의 3D 접촉 합력, 현재/직전 policy 경계의 6D 값. Base frame으로 변환. 대상 object 이름으로 counterpart를 골라 actor에 주지 않음 |
| State 30 / 31 | 현재 적용 arm gain 배율 / 이력 유효 flag. 총32D. 처음에는 현재 값을 복제하되 flag0, 이후 실제 직전 값이 생기면1 |
| Sensor clock | raw force 60Hz, 각10Hz policy 시점 이전6frame의 causal mean; t+1 force를 t action 입력으로 쓰지 않음. 포화 전 raw 값은 evaluator에 별도 보존 |
| Action | 8D: base-frame TCP translation3 + rotation-vector3, symmetric finger target1, arm gain 요청1. Model 내부32D 중 나머지 좌표는 실행하지 않음 |
| Timing | network horizon50 / 실행 chunk1을 구별. 10Hz마다 관측·한 action 실행, 60Hz target interpolation/IK, physics24 substeps/frame → nominal1440Hz. 실제 속도·지연 검증 없음 |
| Bounds — proposed | translation norm≤2mm / rotation norm≤1° per policy call; finger target0–0.04m·변화≤2mm/call. 공간·joint/effort bounds는 같은 값으로 적용하고 asset에서 확정 |
| Gain — proposed | α∈[0.25,1], call당 변화≤0.1. Arm7 `Kp=12000α`, `Kd=900√α`. Finger `Kp=3000`, `Kd=40` 고정. Kd는 동반 조절값이며 critical damping/passivity 보증 아님 |
| Decoder | 목표 pose는 현재 측정 TCP에 bounded delta를 적용해 계산, 동일 IK가 관절 목표를 생성. J만 실행 gain 변경; M은 요청을 기록하고 α₀ 고정. 모든 조건에서 open/regrasp/top press 가능 |
| 입력 normalization | robot q/qd는 고정 asset bound, force는 ±100N clip/100, α는 [0.25,1]→[-1,1]. 단위·순서·mask와 bound JSON을 version/hash로 묶음. 아직 artifact 미생성 |

원 [ForceProbe](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/probes.py)는 contact resultant를 기록한다. 6D 값은 **두 개의 3D force**이며 force/torque wrench가 아니다. 손가락 합력은 압력의 총합도 아니며 접촉 힘 상쇄·가상 센서 정확도의 한계가 있다. 추가 wrist sensor가 필수라는 주장을 하지 않는다. Simulation 결과를 실물로 확장할 때 측정 가능한 대응 센서와 noise/delay 교정이 필요하다.

### 실제 gain 반영 경로와 공개 기본값

[`robot/franka.py`](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/robot/franka.py)의 arm 기본값은 Kp12000/Kd200이지만, **선택 task는 Kd900, finger Kp3000/Kd40으로 덮어쓴다.** N2는 이 task 값을 기준으로 삼았다. JSON 숫자만 바꾸고 gain이 실제 적용됐다고 쓰지 않는다.

Newton **1.5.0 / `cca3bb8a17a3620a1343df3cf12c625e4161b317`**에서 `model.joint_target_ke/kd`를 갱신한 후 `solver.notify_model_changed(newton.ModelFlags.JOINT_DOF_PROPERTIES)`가 MuJoCo actuator gain/bias를 동기화한다. 이 호출은 일부 model constants/contact cache도 갱신한다. 매 policy call 같은 위치에서 M/J 모두 호출하고 gain 반영·physics 영향·비용을 P0에서 확인한다. 최신 docs의 다른 flag를 1.5.0에 복사하지 않는다. [고정 solver source](https://github.com/newton-physics/newton/blob/cca3bb8a17a3620a1343df3cf12c625e4161b317/newton/_src/solvers/mujoco/solver_mujoco.py#L4428)

`TB_STABILIZER=0`, `TB_ARM_EFFORT` unset, MuJoCo-Warp backend, task iterations30/substeps24, charger `impratio=10`을 기록한다. 원 코드의 고정 entry trim은 adapter에서 중복 적용하지 않고 모든 조건에 동일하게 처리한다. Physics collision filters·finger mass/friction은 source 기준으로 유지한다. Gripper 접촉을 무시한 자유로운 물체/손바닥 동작으로 일반화하지 않는다. 초기 reset의 settle 이후 실제 state·gain·solver/contact buffers·RNG·history를 함께 다루어야 한다.

### π₀ / Flow-SDE / PPO 경로

**RLinf source:** `5c415fa28bb25074fab68f0d09baa73d1b67c608`. 모델은 `openpi`, `pi05=false`, `model_action_dim=32`, `action_env_dim=8`, `action_horizon=50`, `action_chunk=1`, `num_steps=4`, `noise_method=flow_sde`, `noise_level=0.5`, `train_expert_only=true`, `detach_critic_input=true`, `joint_logprob=false`를 설계값으로 선택했다. SigLIP/PaliGemma는 고정, action expert·state/action projections는 학습하며 별도 residual actor를 만들지 않는다.

공개 [`Pi0RL`](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/models/embodiment/openpi/tasks/rl.py)은 rollout의 chain/denoising index를 저장해 선택 step의 Gaussian logprob를 재계산한다. [`algorithms/utils.py`](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/algorithms/utils.py#L418)의 chunk-level 경로는 실행 chunk·action dimension을 합산한다. **M/J 모두8D scoring**을 유지하며 내부 padded32D와 executed8D를 혼동하지 않는다. 이는 선택된 denoising surrogate이고 최종 물리 action의 정확한 marginal likelihood라는 주장은 아니다. M의 사용하지 않는 gain 좌표와 shared denoising의 영향은 내용 문서의 조건부7D 비교로 점검한다.

데이터 변환·logprob rollout/recompute·정규화/물리 clipping 전후 raw/applied action이 일치하는지는 아직 native 미검증이다. Actor/critic 입력에 물체 정답·spring label이 들어가지 않아야 한다. `FrankaEEOutputs`가 기본7D만 자르므로 단순 `action_env_dim=8` 변경으로는 충분하지 않다. **ContactBench용 dataconfig/repack/input/output transform을 새로 작성**해야 한다. 기존 LIBERO·Franka output transform을 자동 fallback으로 쓰지 않는다.

**Checkpoint 원격 metadata:** [RLinf π₀ SFT](https://huggingface.co/RLinf/RLinf-Pi0-LIBERO-Spatial-Object-Goal-SFT/tree/4ec11623fba96e1432e535e2c76a634a5e0bdb96), revision `4ec11623fba96e1432e535e2c76a634a5e0bdb96`, `model.safetensors` 7,011,543,960 bytes, 게시 LFS SHA256 `66ac9332abc4a3f1c9ca15e5a80c5a44d4aecb343f0ab3de0c21da4ae2fe77f5`. Public/ungated metadata만 확인했다. Model card/license metadata가 없어 별도 사용 조건 확인이 남고, payload 다운로드·hash 대조·loader 실행은 하지 않았다. Target SFT·normalizer·tokenizer identity는 미생성이다.

### 수집·reward·평가 경계

공개 [data 문서](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/docs/data.md)는 obs[T+1]/action[T] 시간 관계를 정하지만 물체 pose도 포함하고 reward는 placeholder이며 per-step RGB를 저장하지 않는다. 따라서 수집 경로에 **동기화한 RGB·fingertip force·실제 TCP target/gain**을 추가한다. 원 joint target에서 target TCP를 복원할 경우 FK/IK 오차·trim까지 검사한다. 모든 adapter 수정 뒤 새로운 source/data hash를 기록한다.

SFT 시연은10Hz로 정렬하고 미래50개 label 중 episode 내부의 유효 timestep·실행8D만 flow-matching loss에 포함한다. Terminal 뒤의 padding을 실제 동작으로 학습하지 않는다. 이 mask·label 생성은 **추가 구현 항목**이며 기존 transform이 이미 보장한다고 쓰지 않는다. Policy/RL state·action의 물리 단위 변환을 SFT와 동일하게 사용한다.

원 reward를 그대로 사용하는 경로는 없다. N2의 reward·termination·split·예산은 [내용 계약](../내용/README.md#n2-contract)과 source 원장에 둔다. Task deadline은 유한 horizon의 실패 terminal로 처리하며, collector/예산에 의한 외부 중단은 별도 incomplete로 기록한다. 원 `ending`을 자동 실행해 성공을 만들어주지 않는다. Evaluator는 정답 geometry를 사용할 수 있으나 학습 입력으로 전달하지 않는다. Native force의 sample rate·기하 성공·무접촉 판정·contact buffer overflow 확인이 선행돼야 한다.

Release 뒤0.5초는 추가 policy action 없이 마지막 명령을 servo가 유지하는 관측 구간이다. 이 시간의 힘·재접촉·physics 비용도 포함한다. Geometry terminal success와 force-constrained evaluation success를 구분하며, reward만 높인 것을 안전 제약 충족으로 세지 않는다.

<a id="environment"></a>
## 환경 설정의 확인값과 미확정값

다음은 [upstream README](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/README.md)와 [package metadata](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/pyproject.toml)의 요구값이다. 호환성을 실행 검증한 lockfile은 아니다.

| 항목 | 확인한 요구·pin | 아직 정해야 할 것 |
|---|---|---|
| Host/컨테이너 | P0 packet은 local Linux x86-64·NVIDIA Container Toolkit/GPU allocation을 요구. 현재 Mac ARM64 allocation 실패 확인 | 호환 컴퓨터의 driver/CUDA·실제 VRAM/RAM 및 CUDA 카메라 검증. Newton 공식 안내의 driver545+/550 권장은 전체 조합의 실행 보장이 아님 |
| Python/base | P0 전용 Python3.12.12-slim-bookworm linux/amd64 digest를 [Dockerfile](./Dockerfile)에 고정 | 전체 apt/pip closure·native build 미검증. RLinf/FACET/VLA는 이 image에 설치하지 않으며 P0-B 통합은 별도 |
| Physics | `newton==1.5.0`, `warp-lang==1.16.0`, `mujoco-warp==3.11.0`, `mujoco==3.11.0` | indirect dependencies·CUDA wheels·headless renderer 실제 lock/build |
| Model/RL | 위 RLinf π₀/Flow-SDE/PPO + SFT weight revision 선택. FACET은 선행 비교용 | target SFT/data·tokenizer/normalizer·loader 검증·실제 dependency closure |
| Asset | ContactBench commit과 Newton이 고정한 FR3 revision·URDF Git blob을 [실행 계약](./P0_PLAN.json)에 기록 | `prepare`에서 Docker volume에 payload 확보·파일별 SHA256 기록; 실제 다운로드/내용·라이선스 검토는 미완료 |
| 센서/제어 | [probe](./probe.py)에 raw32D 관측·joint target hold/gain ramp·substep force·CUDA RGB 연결 작성 | Native 검증·가시성·힘 교정·N2 Cartesian8D decoder/model normalization·전체 RL 환경은 미완료 |
| 실물 확장 | robot arm/gripper, fixture·접촉 스프링, RGB·선택 force/tactile 측정, 허용 control interface 필요 | 실제 장비 접근권, calibration/동기화·reset·안전 한도·trial 비용 |

미정 GPU memory를 ‘24GB면 충분’ 같은 숫자로 채우지 않는다. 기존 ALLOC/HINDSIGHT의 image·Isaac/ManiSkill 환경을 이 Newton task에 그대로 적용하지 않는다. 나중에 설치·실행할 때는 모든 dependency와 payload를 **선택 컴퓨터의 local Docker 내부/volume**에 둔다. Host Python/MPS·원격 GPU로 대체하지 않는다.

<a id="p0-scope"></a>
## 다음 P0-A와 다른 컴퓨터에서 이어갈 지점

N2 설계에 이어 **P0-PREP 코드를 작성했다.** P0-A는 큰 VLA weights를 받기 전에 **한 nominal task의 센서·gain·clock 경로만** 확인한다. 코드는 아직 NVIDIA에서 실행되지 않았으며 import/API/build 오류를 수정해야 할 수 있다.

1. 선택 컴퓨터의 local Docker endpoint/daemon·architecture·메모리·NVIDIA/CUDA·headless graphics 조건을 재확인한다. 맞으면 아래 최소 검증, 맞지 않으면 실패 명령/결과와 다른 컴퓨터용 실행 준비를 남긴다.
2. 작성한 recipe/launcher로 image build → payload prepare → P0-A를 실행한다. Spring0.4mm·nominal dev 초기 조건1개, 최대2 resets, 총120 control frames·6,000 physics steps, 30분 process 상한이다. Pre-roll도 카운터에 포함한다. **VLA query0·weights download0·optimizer0**이다. 구현 fixture는 기존0.35초 pre-roll 뒤84frame 동안 joint target을 고정하고 α를1→0.5→1로0.1씩 바꾼다. Nominal 합계105frame/2,520physics steps이며 실제 호출 카운터를 우선한다.
3. α0.5/1 요청이 실제 MuJoCo gain/bias에 반영되는지, finger gains·effort limits·stabilizer topology가 고정인지, q/qd·force·RGB timestamp와 actor/evaluator 분리가 맞는지 기록한다. Contact force 유효성·물리 integrity가 실패하면 종료하고 학습을 시작하지 않는다. 비교 성공률을 측정하는 실험으로 보고하지 않는다.
4. P0-A 후 target 시연·normalizer·VLA IO의 P0-B를 구체화한다. N2의 RL pilot 예산은 그 후의 설계이지 지금의 실행 범위가 아니다. 예시 upstream `force-bench run`은 scripted task 명령이며 VLA/RL 재개 명령이 아니다.

환경 합력은 counterpart를 지정한 sensor의 **`force_matrix`를 합산**한다. `total_force`는 모든 counterpart의 힘을 포함하므로 pinch 제외 지표로 바로 사용하지 않는다. Actor fingertip 입력은 counterpart를 제한하지 않은 총합력을 유지한다. 이 경로의 수치 정확성과 환경 접촉이 실제 관측되는지는 native에서 확인할 항목이다. Camera는 Newton `SensorTiledCamera`의 CUDA 렌더 경로이며 이번 P0에 GUI·EGL viewer를 추가하지 않는다. [Newton 센서 source](https://github.com/newton-physics/newton/blob/cca3bb8a17a3620a1343df3cf12c625e4161b317/newton/_src/sensors/sensor_contact.py) · [공개 recorder](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/recorder.py)

<a id="resume"></a>
## 다른 컴퓨터의 실행 순서

저장소 루트에서 다음을 실행한다. Host Python은 stdlib로 Docker CLI만 조작하며 simulator/model을 import하지 않는다. 실제 설치·자산·물리 실행은 Docker image/volume 안에서만 수행한다.

```bash
python3 'work/research_topics/contact_adaptation/재현 방법/run.py' check
python3 'work/research_topics/contact_adaptation/재현 방법/run.py' build
python3 'work/research_topics/contact_adaptation/재현 방법/run.py' prepare
python3 'work/research_topics/contact_adaptation/재현 방법/run.py' p0
```

각 단계의 **exit0을 확인한 뒤 다음 단계**로 간다. `check`는 local unix endpoint·host/daemon architecture를 확인하고 호환 호스트에서 NVIDIA 할당/driver query까지 수행한다. `prepare`에서 패키지 버전·source revision·FR3 URDF Git blob·asset SHA256을 기록한다. `p0`는 network를 끄고 준비된 payload만 사용한다. Base image digest와 source pin은 확보했지만 이를 전체 dependency lock으로 부르지 않는다. 실제 build의 image ID·pip install report/freeze가 실행 identity다. CUDA runtime과 driver 호환은 Warp initialization으로 다시 확인한다. [Newton 설치·지원 조건](https://newton-physics.github.io/newton/1.5.0/guide/installation.html)

- [Dockerfile](./Dockerfile): physics-only image. [P0_PLAN.json](./P0_PLAN.json): source/asset identity·scope/caps.
- [run.py](./run.py): local endpoint 검사·fingerprint 기반 image 선택·timeout·task container 정리. [probe.py](./probe.py): asset 준비·제한된 native probe. [test_p0.py](./test_p0.py): Docker stdlib 제어 검사.
- 결과는 재현 폴더의 `runs/<시간_고유ID>/`에 생성되며 기존 결과를 덮어쓰지 않는다. 이 경로는 Git ignore다. `--output <새 디렉토리>`로 바꿀 수 있다. Packet mount는 read-only이며 결과 외에 host에 설치하지 않는다.
- 자산과 Warp/SDF cache는 Docker volume `paper-contact-p0-cache-v1`에 둔다. Packet이 바뀌어 기존 cache fingerprint가 다르면 멈춘다. 필요한 경우 **모든 단계에서 동일한** `--cache-volume paper-contact-p0-cache-v2`처럼 새 이름을 지정한다. 기존 volume/image를 자동 삭제하지 않는다.
- 결과 `launcher.json`, `prepare.json`, `p0.json`의 status·exit·image/payload hash를 확인한다. Native가 통과해도 상태는 `WIRING_CHECKS_PASS_VISUAL_REVIEW_PENDING`이며 첫/마지막 PNG의 과제 가시성과 force 교정은 별도다. 통과를 task 성공률·기본 VLA competence로 보고하지 않는다.
- 이 파일들이 포함된 revision을 다른 컴퓨터에 전달한 뒤 재개해야 한다. **현재 원격 게시·다른 컴퓨터 clone은 미확인**이다. 준비 코드의 fingerprint와 파일 해시는 [실제 준비 기록](./preparation_2026-11-09.json)에 보존했다.

<a id="preparation-history"></a>
## 2026-11-09 실제 확인과 남은 범위

[실제 명령·결과](./preparation_2026-11-09.json): Darwin ARM64·host RAM16GiB, local `desktop-linux` daemon ARM64·RAM약7.65GiB·10CPU·Docker28.3.3. NVIDIA allocation **exit125** (`could not select device driver ... [[gpu]]`), 새 launcher `check` **exit3**. 과거 실패를 재인용한 것이 아니라 이번에 확인한 결과다.

Docker ARM64 Python stdlib **16검사 통과**: remote/비호환 host 차단, reset·physics·pre-roll/time 상한, gain 범위, raw32D 관측·history·비유한 값, payload 변조·stale image fingerprint·결과 덮어쓰기 방지. Simulator·정책·학습 재현 검사가 아니다. 검사에 임시로 받은 Python image를 삭제했고 task container도 남기지 않았다. 기존 사용자 image는 보존했다.

**준비됨:** N1/N2 계약·source/base/FR3 identity, physics recipe·payload hash 기록·bounded probe/launcher·재개 명령. **실제로 확인됨:** 현재 local 환경 실패와 Docker stdlib16검사. **남음:** native image/dependency closure·payload 확보·CUDA physics/RGB·gain/force 수치·task 가시성, 이후 Cartesian actor decoder·정규화·시연/SFT·VLA IO·학습 효과·실물·독립 피드백. GPU 미지원은 연구 가설의 반증이 아니며 독립 방법 기여 미확립 판정도 바꾸지 않는다.
