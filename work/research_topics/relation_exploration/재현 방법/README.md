# 접촉 관계 탐색 재현

Updated: 2026-11-17 KST. **P0-PREP 코드·재개 문서 작성 완료, native 검증 전.** [내용·방법·비교 설계](../내용/README.md) · [공통 원장](../../../sources/new_field_scout_2026-11-17.json)의 `relation_n1`(선행/자산), `relation_n2`(계약), `relation_p0_preparation`(현재 준비/확인 범위). Portable launcher·Dockerfile·bounded adapter를 작성했다. 현재 launcher check는 **BLOCKED_DAEMON / exit3**이며 native image build·Docker 제어 검사·정책 실행·학습은 모두 미실행이다. 학습용 rollout/PPO trainer와 전체 task event evaluator는 구현 범위에 없다.

## 실제 확인 범위

공개 GitHub API/raw source와 Hugging Face의 소형 metadata/normalizer JSON을 읽었다. 외부 코드를 import/실행하지 않았고 패키지·weights·simulator assets·PDF를 설치/다운로드하지 않았다. 임시 source cache는 SHA256/검토 위치를 원장에 남긴 뒤 삭제한다. Source hash는 파일 확인 증거이며 실행·성능 재현 증거가 아니다.

| 자료 | 고정 revision | 확인한 의미와 제한 |
|---|---|---|
| [RLinf](https://github.com/RLinf/RLinf/tree/461104f2e5a106f38add2c794c19b7aa269e31a3) | `461104f2e5a106f38add2c794c19b7aa269e31a3` | Robotwin wrapper·OpenPI RL sampler/dataconfig·π₀.₅ recipe. Apache-2.0 metadata. Default model config는 `model/pi0_5.yaml`; 오래된 주석의 `openpi_pi05` 이름으로 파일을 추정하지 않음 |
| [RoboTwin, RLinf_support](https://github.com/RoboTwin-Platform/RoboTwin/tree/dca9ec682688821c42944eacd7f5dd9bfb15396f) | `dca9ec682688821c42944eacd7f5dd9bfb15396f` | RLinf 문서가 지정한 branch. Task·robot·base·vector env·config·asset downloader를 확인. Default branch와 섞지 않음 |
| [RoboTwin default branch](https://github.com/RoboTwin-Platform/RoboTwin/tree/ea8b21121ebb3cd201ff5b3fe361944ac94eda3f) | `ea8b21121ebb3cd201ff5b3fe361944ac94eda3f` | 최초 발견 경로. `scripts/`와 `RLinf_support`의 `script/`도 다름. 기본 branch의 MIT 표기를 별도 branch/배포 asset 전체의 license 확인으로 확대하지 않음 |
| [OpenPI](https://github.com/Physical-Intelligence/openpi/tree/215abfb217dbac7d5f1273282331b9b1866c0479) | `215abfb217dbac7d5f1273282331b9b1866c0479` | P0의 재구성 loader 기준. Aloha transform·tokenizer·PyTorch ODE를 확인. Motus의 실제 학습 fork라는 뜻은 아님 |
| [Motus](https://github.com/thu-ml/Motus/tree/88f6fe30c62af033874b0a2e48ad1cbdaf12cfdf) | `88f6fe30c62af033874b0a2e48ad1cbdaf12cfdf` | Tree·README·INFERENCE·RoboTwin guide 확인. 공개 guide는 Motus/Wan/Qwen 경로이며 π₀.₅ baseline recipe로 대체할 수 없음 |
| [Lattice](https://github.com/amathislab/lattice/tree/846d02fa993b9b80ce5ecb806463e0a05711bad3) | `846d02fa993b9b80ce5ecb806463e0a05711bad3` | MIT. Distribution·PPO policy를 읽음. Native VLA drop-in adapter는 아님 |
| [SOE](https://github.com/EricJin2002/SOE/tree/9b5be5a7be16c39e8aa5314aad4bff29c6c81261) | `9b5be5a7be16c39e8aa5314aad4bff29c6c81261` | DPExt/transport config/success-filter loop. 루트 license 파일·API license는 식별하지 못함. 코드를 이 저장소에 vendor하지 않았음 |

StructRL의 [저자 project](https://flyfaerss.github.io/structrl/)는 직접 HTTP로 읽을 수 있었지만 코드 링크를 식별하지 못했다. 동명의 Amazon StructRL을 대체 구현으로 사용하지 않는다. RL-SCT도 paper의 함수/interface를 대조했으나 공식 독립 코드 위치는 미확인이다.

## Task·관측·제어에서 확인한 함정

- **Task 세 가지:** [lift_pot](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/lift_pot.py#L54)는 height/pose/TCP 거리 성공 조건, [handover_block](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/handover_block.py#L114)은 최종 위치·right gripper open, [pick_dual_bottles](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/pick_dual_bottles.py#L150)는 두 병의 위치·높이를 본다. Scripted expert의 순서를 정책이 실제 수행했다고 간주하지 않는다.
- **Command와 measurement:** [`get_obs` L509–519](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/_base_task.py#L509)는 `get_*_arm_jointState`를 쓰고, [robot L528–557](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/robot/robot.py#L528)는 drive target과 actual qpos를 별도 함수로 제공한다. `real_jointState`도 마지막 gripper 값은 기존 helper를 호출하므로 전체 14D를 전부 실제 센서값이라고 이름 붙이지 않는다. 기하 계산에는 실제 arm 12D만 별도 export하는 계획이다.
- **Action:** `[left6,left_gripper,right6,right_gripper]`의 14D joint target. [Aloha dataconfig](https://github.com/RLinf/RLinf/blob/461104f2e5a106f38add2c794c19b7aa269e31a3/rlinf/models/embodiment/openpi/dataconfig/robotwin_aloha_dataconfig.py#L79)는 arm delta·gripper absolute를 구분한다. Joint sign flip·gripper 비선형 변환·normalizer가 모두 맞아야 하며 14D가 같다는 사실로 호환을 판정하지 않는다.
- **실제 RL 호출 경로:** [`SubEnv.step_with_full_obs` L141–166](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/robotwin/envs/vector_env.py#L141) → [`gen_sparse_reward_data` L1747–2023](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/_base_task.py#L1747)를 기준으로 한다. N1의 `take_action` 설명만으로 이 경로를 대신하지 않는다. TOPP 1/250 간격·50-step 실패 fallback 외에 **compress_path의 정지 경로 잡음(표준편차 2e-4), 최대500-point downsampling**이 있다([L444–460](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/_base_task.py#L444)). 원 경로/축약 경로/실제 scene.step 수를 각각 기록한다. TOPP duration을 실행 물리 시간으로 대신하지 않는다.
- **성공/종료:** `eval_success` 이후 action을 건너뛰는 경로가 있다. Final success와 contact 전환의 witness를 별도 기록하고, 안정된 배치/손 해제를 평가하려면 종료 조건과 관측 시점을 따로 설계한다. 단순히 추가 hold를 실행했다고 native metric과 동등하다고 쓰지 않는다.
- **Contact:** Annotation의 `get_contact_point`는 실제 물리 contact가 아니다. `scene.get_contacts()`와 body/link identity·impulse를 evaluator에 제한해서 사용한다. `get_scene_contact()`에는 debugger 호출이 있으므로 그대로 실행 경로에 넣지 않는다. 임계값·지속 시간은 아직 미교정이다.
- **Reset:** Vector env의 setup 실패 retry가 seed를 바꾸는 경로를 확인했다. 진단에서는 실패를 기록하고 총 시도 상한을 적용할 계획이다. 반환된 최종 seed와 의도한 seed를 함께 저장해야 한다.

## Checkpoint와 asset — payload 실행은 미확인

| 후보 | metadata에서 확인한 것 | 판정 |
|---|---|---|
| [motus-robotics/pi0.5_robotwin2](https://huggingface.co/motus-robotics/pi0.5_robotwin2/tree/effc6e1a99bd4d0edf9447e8ba313def67649cfe) | Revision `effc6e1a99bd4d0edf9447e8ba313def67649cfe`. 저자 card: 50-task clean/randomized SFT, model horizon32, adapt_to_pi·delta joint. 실제 file의 norm asset ID는 `pi0.5_clean_randomize_joint_training`; state/action stats 각각14D. Weight LFS SHA256 `de8e03a445f3e0af417a9d61a903d342fca5b6a5b4fdc6f20445e14ad25692eb` | **범위상 우선 후보, loader/기본 능력 미검증.** Card의 예시 asset ID와 실제 파일명이 다르다. Model config 파일·정확한 학습 fork·명시적인 model license는 확보하지 못함. 공개 사용자 [issue #45](https://github.com/thu-ml/Motus/issues/45)도 recipe를 요청하지만 이것을 저자 확인으로 세지 않음 |
| [RLinf π₀.₅ adjust_bottle](https://huggingface.co/RLinf/RLinf-Pi05-RoboTwin-SFT-adjust_bottle/tree/fa8df6ed103db0f5549c122f3a17c00ba6426c98) | Revision `fa8df6ed103db0f5549c122f3a17c00ba6426c98`, metadata/file 목록. RLinf recipe는 3 images·14 action·horizon/chunk50·5 denoise steps | **Interface 참고용**. 선택한 세 task에 적합한 multitask checkpoint로 간주하지 않음. Normalizer payload는 이 후보에서는 미검토 |
| [RoboTwin assets](https://huggingface.co/datasets/TianxingChen/RoboTwin2.0/tree/3dc3b798668feb99ac61cc9086d84cbcc3d79186) | Revision `3dc3b798668feb99ac61cc9086d84cbcc3d79186`; dataset card MIT. `embodiments.zip`·`objects.zip`·`background_texture.zip`의 upstream LFS hash/크기를 원장에 기록 | Archive 내부 URDF·TCP/frame·object mesh는 아직 열지 않음. 기본 downloader는 세 zip을 모두 받으므로 지금 실행하지 않음. 나중에도 asset별 권리/실제 payload hash를 확인 |

Upstream LFS hash는 서버 metadata에서 읽은 값이다. Weight/zip의 로컬 계산 hash가 아니며 정상 로드·내용 일치를 검증했다고 표시하지 않는다. Norm stats의 소형 JSON만 실제 읽고 SHA256을 계산했다. RLinf의 선택 model config는 padded32D, 실행14D를 구별한다. Motus payload의 실제 tensor shape는 아직 읽지 않았다.

<a id="n2-interface"></a>
## N2 — loader 결정과 관측·행동 계약

**결정:** 첫 loader는 위 OpenPI pin에서 저자 card의 `pi05=True, action_horizon=32, adapt_to_pi=True, use_delta_joint_actions=True`를 재구성한다. RLinf의 horizon50/adjust_bottle config에 weight만 교체하지 않는다. 이는 **우리의 재구성 baseline**이며 Motus 논문 결과 재현으로 부르지 않는다. 아래의 source 확정과 호환 가설을 분리한다.

| 항목 | 결정·근거 | 아직 남은 검증 |
|---|---|---|
| 모델 구성 | Card 명시 H32. OpenPI 기본은 action_dim32, Gemma2B/300M expert, π₀.₅ max_token_len200·discrete state([config L19–41](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/pi0_config.py#L19)). 이 기본값을 재구성 설정으로 선택 | 원 fork·변환 이력·tensor key/shape는 미확정. H32는 card 근거이며 tensor shape로 입증한 값 아님 |
| Weight loader | [`load_pytorch` L243–247](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/model.py#L243)의 PI0Pytorch/safetensors 경로. P0에서는 strict load와 누락/초과 key·shape 기록을 요구 | 실로드 전. `strict=False`, key 삭제, 임의 reshape로 성공을 만들지 않음 |
| Normalizer | 위 실제 파일/해시를 명시적으로 전달. [`policy_config` L58–88](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/policies/policy_config.py#L58)의 입력/출력 transform 순서 사용 | π₀.₅ 기본 **quantile** 경로를 선택([factory L179–188](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L179)); Motus 원 fork에서도 같았다는 독립 증거는 없음 |
| 저자 recipe | Motus guide는 `mp_rank_00_model_states.pt`·Wan/Qwen을 요구한다. π₀.₅ `model.safetensors` loader와 다름. [issue45](https://github.com/thu-ml/Motus/issues/45)는 확인 당시 open·댓글0 | 사용자 issue를 저자 답변으로 사용하지 않음. 저장소 tree/지정 guide 확인이며 모든 파일의 의미적 전수검토는 아님 |
| 공통 SFT | **지금 자동 시작하지 않음.** 먼저 재구성 loader의 구조/IO를 판정한다. 호환되지 않으면 공개 baseline 사용을 중단하고, 문서화된 OpenPI base에서 모든 비교군 공통 SFT를 만드는 경로로 변경 | 성공한 strict load도 의미적 호환·grasp 능력을 보장하지 않음. 후속 full-start pilot에서 기본 능력 부족이면 공통 SFT/data 검토. 데이터 split·훈련비·normalizer 재계산 전에는 SFT 준비 완료가 아님 |

**입력 순서:** 같은 물리 tick에서 세 camera의 RGB(HWC,uint8), `joint_action.vector`14D, actual arm qpos12D를 읽는다. Adapter가 RGB를 CHW로 바꿔 `images/cam_high,cam_left_wrist,cam_right_wrist`에 넣으면 AlohaInputs가 다시 HWC로 복원한다. P0에는 세 camera 모두 필수로 두며 missing-camera black-mask fallback을 통과로 세지 않는다. Default goal을 조용히 주입하지 않고 실제 prompt·생성 seed·token/hash·truncation 여부를 저장한다.

`AlohaInputs → Normalize(quantile) → ResizeWithPad(224²) → TokenizePrompt(state 포함) → Pad32` 순서다. State는 arm sign flip과 gripper 상태 전용 비선형 변환 후 정규화한다. **정규화된 14D 상태를 먼저 토큰화하고 이후 32D pad**한다. Pad된 32D나 actual qpos를 checkpoint의 state token에 넣지 않는다. [`ModelTransformFactory` L126–137](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py#L126), [`tokenizer` L22–46](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models/tokenizer.py#L22). Tokenizer 파일도 Docker cache에서 hash를 기록해야 한다.

**출력 순서:** full ODE의 `(1,32,32)` 예측에서 첫 시점·첫14D를 평균으로 사용한다. Endpoint raw `u`14D를 샘플/저장 → quantile inverse → **관측 시점의 복원된 command state**를 arm12축에 더함 → Aloha output sign/gripper 변환 → `gen_sparse_reward_data(command[None,:],collect_obs=True)`로 K1 실행한다. Horizon32는 보존하고 suffix31개와 padding18축은 실행 likelihood에서 제외한다. 출력 unnormalizer는 action뿐 아니라 state를 복원한 뒤 AbsoluteActions를 호출한다([transforms L149–181,226–242](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/transforms.py#L149)).

Arm 축 `I=(0…5,7…12)`에서 `aπ=(u+1)(q99−q01+1e−6)/2+q01`, `command_I=F_I·(aπ_I+sπ_I)`다. `F=[1,−1,−1,1,1,1,1,1,−1,−1,1,1,1]`. 따라서 raw→arm command의 미분은 `D=diag(F_I·(q99_I−q01_I+1e−6)/2)`다. Gripper 두 축은 delta를 더하지 않고 `_gripper_from_angular`를 적용한다. 상태용 `_gripper_to_angular`와 action용 함수는 서로의 단순 역함수가 아니다([Aloha L104–201](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/policies/aloha_policy.py#L104)).

이후 RoboTwin `set_gripper`는 [L662–693](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/robot/robot.py#L662)에서 [0,1] clipping·이전 drive target 기반 opening 제한·mimic joint 변환을 추가한다. `raw_u`, requested command, clipped gripper, 실제 각 substep drive target, 측정 qpos를 구별한다. 명령값 round-trip과 실제 추종 오차는 다른 검사다.

**기구학 계약:** `get_*_tcp_pose()`는 world-frame EE pose에 embodiment의 `global_trans_matrix·delta_matrix` 회전과 x축 `gripper_bias`를 적용한다([robot L598–637](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/robot/robot.py#L598)). `T_rel=T_world_left⁻¹ T_world_right`; `J_rel`은 `Log(T_rel(q)⁻¹ T_rel(q+dq))`의 body-frame 미분, 행은 translation3/rotation3, 열은 actual joint L6/R6로 고정한다. Quaternion은 해당 source의 wxyz convention을 사용하며 두 robot base frame을 바로 빼지 않는다. `W=diag(1/0.1m ×3,1/1rad ×3)`는 첫 진단용 공학적 선택이며 검증된 최적값이 아니다. 모든 군에 같은 geometry 제공. URDF·joint-name 순서·TCP offset payload hash와 FK 대조는 아직 미확인이라 numerical Jacobian을 확보했다고 표시하지 않는다. `D`는 명령 감도이지 접촉 중 실제 joint displacement의 Jacobian이 아니다.

## 학습 구현에서 필요한 수정

[OpenPI sample_actions L376–420](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models_pytorch/pi0_pytorch.py#L376)는 `@torch.no_grad()`이며 [`Policy.infer` L97–102](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/policies/policy.py#L97)는 detach/NumPy로 변환한다. 학습에 그대로 사용하지 않는다. [RLinf Pi0RL](https://github.com/RLinf/RLinf/blob/461104f2e5a106f38add2c794c19b7aa269e31a3/rlinf/models/embodiment/openpi/tasks/rl.py#L181)의 denoising-chain density도 endpoint Gaussian density를 대신하지 않는다.

구현할 지점은 **별도 differentiable full-ODE sampler와 마지막 Euler vector-field 평가의 `suffix_out[:,0,:]` 추출**([denoise_step L450–462](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/models_pytorch/pi0_pytorch.py#L450))이다. 이 feature는 최종 action 자체나 t=0의 추가 forward가 아니다. P0는 명시적으로 Euler10회·H32·K1·compile off·eval mode를 사용한다. 10회는 선택한 OpenPI 기본과 맞춘 진단 설정이며 Motus 원 평가 설정으로 주장하지 않는다.

학습 허용 집합은 `gemma_expert`, action input/output projection, π₀.₅ time-conditioning MLP, 새 λ head다. PaliGemma vision/language와 tokenizer는 고정한다. 실제 parameter 이름·개수·dtype·gradient를 출력해 이 whitelist와 대조한다. Critic은 별도이며 actor로의 value gradient를 차단한다. Raw `(ξ,u)`를 detach해 rollout 상수로 저장하고 **같은 raw 값**의 log-probability를 재계산한다. 새 sample의 reparameterization 경로로 PPO score를 계산하지 않는다. Cholesky/log-density는 FP32 이상, `(ξ,u)` augmented policy라는 해석을 유지한다.

`compress_path`의 추가 잡음은 actor covariance와 별개다. P0에서는 upstream 동작/RNG를 그대로 기록한다. **이후 방법 비교에서는 모든 군에 공통으로 random perturbation을 제거한 동일 controller**를 적용하고, zero-length는 정확한 중복점으로 보내 기존 TOPP 실패/hold fallback을 기록한다. 이 변경은 별도 patch/hash와 compatibility 검사를 요구한다. Downsampling·gripper 제한·prefix는 군별로 바꾸지 않으며 원 논문 점수와 직접 동등 비교하지 않는다. 학습 controller가 준비되었다는 뜻은 아니다.

<a id="n2-events"></a>
## N2 — 접촉 사건·시간·기록 계약

접촉은 evaluator 전용이다. SAPIEN3의 `PhysxContact.bodies/points`와 impulse/normal/separation을 사용한다([공식 API](https://sapien-sim.github.io/docs/api/sapien.pysapien.physx.html)). Contact entry 존재만으로 접촉이라고 세지 않는다([공식 설명, 2.2 API 경계](https://sapien.ucsd.edu/docs/latest/tutorial/basic/contact.html)). 선택3.x에서 실제 field/API와 단위를 P0에서 대조해야 한다. Actor에는 object identity·pose·event·정답 contact를 전달하지 않는다.

두 finger link와 task object의 **실제 entity identity**를 setup 시 mapping한다. `is_in_hand`의 이름 문자열/count를 그대로 정답으로 쓰지 않는다. 각 물리 step 뒤 pair별 impulse norm 합과 separation을 저장하고, distinct finger 양쪽의 임계값 초과·연속 지속시간으로 `contact_supported_grasp`를 판정한다. 이것도 force closure 증명이 아니다. 시작 진단값은 force-equivalent 0.05N, separation≤1mm, 지속≥0.04s다. Simulator/asset에 대해 미교정이며 P0 통과 조건이나 최종 지표 threshold가 아니다. 이후 dev에서 RGB·실제 finger qpos·분리 장면과 대조해 고정하고 raw trace는 보존한다. API/mapping이 틀리면 event=unknown으로 기록하고 false로 채우지 않는다.

| Task | Native success와 별도 evaluator witness | 미관측/해석 경계 |
|---|---|---|
| lift_pot | 같은 pot에 양손 supported contact가 성립한 시작 tick, 양손 지속 구간, pot 상승·table support 변화, 최초 한쪽 이탈. 양손 구간의 λ·상대 TCP 이동·실제 joint 이동 | Native height/pose/TCP-distance 성공은 접촉 증명이 아님. 양손 구간 미도달도 full-start 분모에 남김 |
| handover_block | 동일 block의 left-only→both→right-only 순서와 각 지속시간. 주는 손 open **command**와 actual finger 분리, 받는 손 contact 유지, table contact/no-table 구간을 별도 기록 | 최종 배치 성공만으로 handover라 하지 않음. 보조 handover witness는 right-only·table 미접촉의 지속 구간을 요구. 종료 전에 못 보면 not_observed 또는 right_censored; 관측 길이 부족을 곧 실패로 세지 않음 |
| pick_dual_bottles | left/right object의 별개 identity와 각 손–물체 contact, 서로 다른 물체 동시 유지, 잘못된 object 접촉·놓침 | 서로 다른 task 사이 λ 차이만으로 causal benefit이나 language grounding을 주장하지 않음 |

P0의 한 command로 위 전체 사건을 확보하려 하지 않는다. P0는 contact API/empty-contact 처리·identity mapping만 검증한다. 실제 positive grasp/release trace의 교정은 후속 competence pilot에 남긴다. Task expert를 정책 중간에 호출하지 않는다. 별도 scripted evaluator 교정이 필요하면 그것을 시연/추가 비용으로 명시한다.

**시간과 종료:** 생성된 target 수, 부분 실행을 포함한 실행 prefix, physics step 수, simulated seconds, 추론/학습 wall time을 따로 기록한다. 기본 dt=0.004s를 명시하고 runtime 값을 assert한다. TOPP 시간을 downsample 뒤의 scene 시간으로 복사하지 않는다. setup 안정화 자체가 2,000+500 step([L163–194](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/_base_task.py#L163))이므로 rollout 외 비용도 센다. Setup/retry·warmup·control 전체 `scene.step()`에 counter를 걸어 budget 전에 차단한다.

성공은 substep 후 검사되므로 contact를 **같은 substep의 성공 검사/return보다 먼저** 수집한다. Raw last observation, `terminated`, `truncated`, 예외, budget stop을 구분하고 성공 이후 추가 hold를 하지 않는다. `collect_obs`가 채운 suffix 반복 frame은 `executed_action_count`/중간 종료 tick과 함께 해석한다. K1도 일부만 실행되면 partial flag를 남긴다. 성공 이전에 종료된 event window는 censored다. 임의의 미래 frame은 actor 입력에 들어가지 않는다.

**필수 로그 그룹:** `run/source/image/checkpoint/normalizer/tokenizer/asset hashes`; `task/requested_seed/actual_seed/reset_attempt/prompt`; `obs_tick/3RGB hashes/command_state14/q_measured12/TCP`; `ξ/raw_u/μ/λ/Σ/logp_old/logp_replay`; `requested_command/applied_substep_targets/gripper_limits/TOPP flags/path lengths/controller RNG`; `body-object map/contact point trace/event timestamps`; `physics_setup/physics_control/dt/model_evaluations/wall time/peak VRAM/termination`. P0 adapter는 raw 관측·action NPZ, 명령/실제 qpos·finger/TCP·object/table pose/contact JSONL, controller/종료 정보를 기록하도록 작성했다. 전체 사건 timestamps는 `null + 미구현 사유`이며 raw trace를 검증된 grasp/handover label로 승격하지 않는다. 구현된 로그도 native 실행 전에는 확보된 결과가 아니다.

<a id="n2-p0"></a>
## N2 — 최초 native P0 범위

| 단계 | 상한과 통과 기준 | 실패 시 |
|---|---|---|
| Loader/자산 | 모델1회 strict load. Pin/hash·14D stats·H32/pad32·tokenizer·URDF/FK mapping 검증. 누락/초과 key·shape 불일치는 실패 | 모델 호환 문제로 기록. 자동 다른 checkpoint나 SFT를 실행하지 않음 |
| Scene/관측 | demo_clean의 세 task 각각 requested seed0, 실패 시 seed1 한 번만 허용: **총 setup≤6, 유효 scene≤3**. 각 시도 physics≤5,000. Instruction은 실제 유효 episode metadata로 생성·저장하고 별도 metadata scene을 만들지 않음 | 원래 seed/실패를 기록. 무한 retry/조용한 seed 변경 금지 |
| Query/command | 성공한 scene당 관측1개에서 policy query1회, **총 query≤3**. H32/K1. Model/transform 값이 finite이고 arm target이 URDF limit 안, 현재 command 대비 ≤0.05rad일 때만 command1회. 그 외는 command budget 미사용으로 종료 | 이 0.05는 진단 상한이지 method 성능 기준이 아님. 통과를 위해 임의 축소하거나 hold를 정책 action으로 바꾸지 않음 |
| Physics/contact | command당 physics≤1,000, 총 control≤3,000; setup 포함 **전체≤33,000**. Counter/identity/contact API와 requested/applied action trace 확보 | 한 command로 task 성공·handover/evaluator 의미 타당성 확보를 주장하지 않음 |
| 재채점 | 관측별 고정 ξ/u 재계산1회, **총≤3**. 동일 가중치/입력에서 finite SPD·logp 일치. 우선 FP32 density abs tolerance1e-4, BF16 차이는 기록하고 자동 완화 금지 | inference drift와 density 오류를 구별. 조건 차이를 숨긴 tolerance 변경 금지 |
| 선택적 gradient | 위 IO 통과 후 관측1개에서 **전체 ODE backward≤1, optimizer step=0**. 실제 raw sample 고정, expert/λ-head gradient 유무·finite 확인, frozen backbone 변화0 확인 | OOM/끊긴 gradient를 정책 가설 반증으로 세지 않음. 학습/sweep으로 확대하지 않음 |

Full ODE forward는 query3+replay3+gradient용1로 **최대7회**, 각 Euler10회다. 관계 head/SPD 진단의 초기값은 `λ_max=10, η=0.05, σ_arm=0.1, σ_gripper=0.1`로 명시하되 최적값·학습 설정으로 승격하지 않는다. P0용 policy/module seed0. **P0-PREP 명세 명확화:** N2의 `24 FK + 기준1`은 관측당 relative FK 평가 수다. 세 관측에서 최대75회이며 각 relative 평가가 두 TCP를 계산한다. 기존 원장의 모호한 total25 기록은 역사로 보존하고 실행 전 [PLAN](./PLAN.json)에 수정 이유를 남겼다. Physics/query 상한은 늘리지 않았다. 수식 self-consistency 통과를 contact 보존 효과로 해석하지 않는다.

<a id="p0-preparation"></a>
## P0-PREP — 구현·환경·확인 경계

| 파일 | 역할 | 현재 확인 |
|---|---|---|
| [PLAN.json](./PLAN.json) | Source/image/checkpoint/asset pin, 자원 설정, N2 실행 상한 | JSON·source metadata 대조. 실제 설치 환경 아님 |
| [Dockerfile](./Dockerfile) / [.dockerignore](./.dockerignore) | 필요한 소스만 image에 복사. OpenPI frozen upstream lock과 simulator 환경을 분리 | Recipe 작성, **build 미실행** |
| [resume.py](./resume.py) | Host stdlib로 로컬 endpoint·daemon·GPU 조건 확인, image/build/cache·bounded container orchestration | 현재 host의 차단 경로 실행: BLOCKED_DAEMON, exit3 |
| [actor.py](./actor.py) | Strict loader, 14D state-token/행동 변환, full Euler10, λ/공분산, raw 재채점, 선택적 backward | Python 정적 컴파일 통과. Native import/weight load/gradient 미실행 |
| [probe.py](./probe.py) | Docker 내부 payload hash, CUDA/graphics, task setup·FK·physics budget·contact/명령 로그 | Python 정적 컴파일 통과. FK/physics/graphics 미실행 |
| [test_contract.py](./test_contract.py) | Docker CPU의 budget·archive·공분산/밀도·upstream transform·source 계측 검사9개 | 코드 작성·정적 컴파일만 완료. **9개 검사 미실행**, 통과로 세지 않음 |

**현재 실제 환경 확인:** Darwin/arm64, Docker CLI 존재, context `desktop-linux`, 로컬 Unix socket. 직접 `docker info`와 새 launcher의 `check` 모두 daemon 연결 실패를 반환했다. Server architecture·메모리·NVIDIA 할당/CUDA/graphics는 **미확인**이다. 오류 응답의 빈/0 필드는 hardware 측정이 아니다. 이번 작업이 만든 container/image/volume·host dependency·weight/asset 다운로드는 0이다. 생성하지 않은 Docker 자산을 정리한다며 기존 사용자 자산을 삭제하지 않았다.

### 고정한 환경과 구현 선택

- Linux x86-64 호스트의 **로컬 Docker Engine**, NVIDIA Container Toolkit, 선택 GPU의 CUDA/BF16와 SAPIEN graphics가 필요하다. Unix context라도 host/daemon architecture·GPU allocation을 다시 검사한다. Docker/builder override 환경변수나 원격 endpoint는 차단한다. 현재 launcher는 Windows/WSL 경로를 검증하지 않는다.
- Base는 `rlinf/rlinf:agentic-rlinf0.4-robotwin`의 **linux/amd64 child digest `sha256:e3952705e6d38d9b5cb6235aaf2661d5e4112ede95fdf61a69c46beb7d14cf3c`**다. Docker Registry manifest/config metadata로 확인했으며 image layer는 받지 않았다. Config의 CUDA는12.8.1, compressed layers 합계 약13.65GiB다. 실제 package inventory/import 성공을 확인한 것은 아니다. Driver는 이 CUDA image를 지원해야 하며 실제 allocation/BF16/render 검사로 판정한다. [NVIDIA GPU·graphics 설정](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html).
- Simulator는 image의 `/opt/venv/openpi/bin/python`, actor는 별도로 고정한 OpenPI source/`uv.lock`을 `uv sync --frozen --no-dev --python 3.11`로 설치하는 `/opt/relation-openpi/bin/python`이다. Upstream 요구 torch2.7.1·transformers4.53.2 및 transformers replacement를 simulator 환경에 덮어쓰지 않는다. Image build 중 import/pip 정합성과 두 package 목록을 저장한다. **Frozen upstream lock을 사용한 recipe이지, 검증을 마친 우리 환경 lock은 아니다.**
- 동일 container 안에서 두 Python 환경은 JSON/NPZ로 소통한다. 이는 의존성 분리이며 연구 방법을 계층형 정책으로 바꾸는 것이 아니다. Actor는 RGB·prompt·command-state·actual q/J만 읽고 object/contact 정답은 받지 않는다. 단일 actor의 action expert와 λ-head를 함께 미분하는 경로다.
- 준비용 자원 하한은 daemon RAM32GiB, 선택 GPU **남은 VRAM24GiB**, Docker storage 여유100GiB, container memory32GiB/shm2GiB다. 이는 측정한 최소 사양이 아니며 여유 VRAM 조건상 명목24GB GPU는 차단될 수 있다. Full ODE backward는 더 큰 메모리가 필요할 수 있다. Resource 값을 바꾸면 PLAN·packet hash도 달라지며 image를 다시 build한다. [Docker 자원 제한](https://docs.docker.com/engine/containers/resource_constraints/).
- Source는 `/opt/relation-src`, 실행용 계측 복사본은 `/tmp/relation-robotwin`, payload는 Docker **named volume**의 `/cache`, 결과만 host에서 지정한 새 경로를 `/results`로 mount한다. 특정 사용자의 절대 경로가 재개 조건은 아니다. GPU는 host index로 선택하고 실제 UUID를 container에서 재확인한다.
- `demo_clean`이므로 background texture zip은 받지 않는다. 고정한 두 asset zip과 model/norm만 내부 download/hash 확인한다. 압축 내부 root·mesh/URDF 구조는 아직 미확인이며 예상 구조와 다르면 중단한다. Cache의 extraction marker는 archive hash 확인 이력이지 모든 추출 파일의 무결성 증명이 아니다. 실제 사용 URDF·tokenizer hash는 실행 때 저장한다.
- Planner는 지원 source의 `mplib`, camera near는0.01로 선택했다. 원본 checkout은 유지하고 임시 source 사본에서 명시적 `scene.step()`을 계측한다. Model mean은 upstream Euler와 같은10단계로 재구성했다. Native mean parity·strict key 호환·state 의미 호환은 아직 검증 전이다.
- FK는 `*_ee`가 joint인 점을 반영해 **child-link FK × joint pose-in-child**를 거쳐 TCP offset을 적용한다. Actual TCP와 위치1e-4m/회전1e-3rad 범위에서 일치해야 한다. 고정 base pose/축/normalizer scale이 틀리면 중단한다. [RoboTwin joint 정의](https://github.com/RoboTwin-Platform/RoboTwin/blob/dca9ec682688821c42944eacd7f5dd9bfb15396f/envs/robot/robot.py#L175) · [SAPIEN3 joint API](https://sapien-sim.github.io/docs/api/sapien.pysapien.physx.html).
- P0는 기존 TOPP 정지 잡음·downsampling을 유지하며 RNG/입출력·실제 physics 수를 기록한다. 향후 학습 비교에서 추가 정지 잡음을 제거하는 **모든 군 공통 deterministic controller 변경은 아직 미구현**이다. P0 trace를 완성된 학습 환경으로 취급하지 않는다.

<a id="resume"></a>
## Clone 후 재개 명령

저장소 root에서 실행한다. `check`는 host stdlib와 read-only system 명령만 사용하며 실험 dependency를 import하지 않는다. 모든 package/weight/asset 확보와 native 실행은 아래 launcher가 만든 **로컬 Docker 안**에서만 수행한다. `--results`는 매 호출 새 디렉토리여야 한다.

```bash
python3 "work/research_topics/relation_exploration/재현 방법/resume.py" check   --results "work/research_topics/relation_exploration/재현 방법/runs/local-check"

python3 "work/research_topics/relation_exploration/재현 방법/resume.py" run   --gpu 0 --results "work/research_topics/relation_exploration/재현 방법/runs/p0-first"
```

`run`은 조건 충족 시 allocation → image build → Docker CPU contract checks → CUDA/BF16/render → payload 준비 → bounded P0 순서로 수행한다. 자원 조건 불충족이면 exit3에서 끝나며 image/payload를 받지 않는다. 위 P0에는 optimizer가 없고 backward도 기본 꺼져 있다. 같은 첫 실행에 선택적 단 한 번의 gradient 진단까지 포함하려면 `run`에 `--backward`를 붙인다. 이 선택은 RL 학습 실행이 아니다. 새로운 P0 반복/상한 증가로 실패를 덮지 말고 이전 실패 원인부터 검토한다.

단계를 나눌 때도 동일 launcher의 `build`, `control`, `prepare`, `p0`를 사용한다. `build` 후 고정 image는 packet hash tag로 재사용하고, payload volume은 model/asset revision 조합으로 재사용한다. 각 호출에 다른 결과 디렉토리를 지정한다. `p0` 단독 재개는 같은 image의 `control` 결과와 payload 준비가 확인된 뒤 사용하며, 새 run의 native 최소 검증 상한을 적용한다. Image나 payload가 없거나 hash가 다르면 자동 다른 버전을 선택하지 않는다.

Run 결과에는 `local_check.json`, `launcher.json`, container/build logs, `control.json`, `environment.json`, `graphics.json`, `payload.json`, `loader.json`, `source_instrumentation.json`, task별 observation/action NPZ·contact JSONL·case JSON, `p0.json`이 단계별로 생긴다. 앞 단계에서 실패하면 뒤 파일이 없는 것이 정상이다. 대용량 결과는 `runs/` gitignore 아래 두며 이후 검토한 요약/필수 증거만 선별 보존한다. Container는 `--rm`이며 오류 시 이번 launcher가 소유한 고유 이름만 정리한다. Image와 named cache volume은 재개에 필요하므로 유지하며, 폐기 시 `launcher.json`의 정확한 ID/owner label을 확인해 개별 삭제한다. `docker system prune`은 사용하지 않는다.

<a id="다음-n2의-종료-산출물"></a>
## 현재 종료와 다음 판단

**P0-PREP 준비 코드/문서 완료, P0 native 검증 대기**다. 현재 확인한 것은 public source/image metadata, 코드 정적 컴파일, host launcher의 daemon 실패 차단뿐이다. Container 제어 검사9개·dependency 정합·image build·payload 내부 구조·checkpoint key/의미 호환·FK/RGB/contact·raw likelihood/gradient는 검증되지 않았다. 성공률·학습 효과·full-start competence도 미측정이다.

다음 TODO는 **GAP-RELATION-EXPLORE-P0 — NATIVE_RESOURCE_WAIT**다. 호환 NVIDIA 컴퓨터의 로컬 Docker에서 위 최소 실행을 먼저 판정한다. Strict loader/IO 실패 시 자동 key 변경·다른 checkpoint/SFT로 넘어가지 않는다. IO만 통과하면 그 결과로 기본 능력·positive event 교정 pilot의 예산을 다음에 정한다. 학습 trainer·critic·실험 split/비교군과 전체 event evaluator는 그 이후이며, 준비 자료 완성을 독립 방법의 가치 입증으로 해석하지 않는다.
