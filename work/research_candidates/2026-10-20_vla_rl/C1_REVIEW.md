# C1 후속 검토: 관측을 언제 생략해야 하는가

- 시작 2026-10-20, 후속 확인 2026-10-21 / [최초 후보 비교](./README.md)에서 C1을 먼저 진행
- 근거: 관련 본문·공개 interface의 정적 확인. [17개 파일의 revision/hash](./C1_SOURCE_AUDIT.json)
- 다음 판정 기준: [C1 진단 계약](./C1_PROTOCOL.md)
- Native 실행 결과는 [별도 probe 결과](../../experiments/vla_rl_active_handoff/RESULTS.md)에서 관리한다. Strict load·243 actions는 확인했지만 시간 제한으로 task competence는 미확인이다. 논문의 결과와 우리 실험을 혼합하지 않는다.

## 이번 단계의 결론

**C1을 새 RL 방법으로 바로 구현할 근거는 약해졌다.** 처음 선별에서 빠졌던 ActiveAlign과 EyeRobot 2.0을 확인했다. “잘 보이는 것이 잘 조작하는 것과 다르다”, “시선의 대상·순서를 RL로 학습한다”, “관측 뒤 조작으로 전환한다”는 각각 이미 직접 선행 연구에 있다.

남길 질문은 다음처럼 좁힌다.

> 고정된 native VLA와 물리적으로 실행 가능한 관측 행동이 주어졌을 때, 추가 관측의 **순이득이 양수인 상태만** 선택할 수 있는가? 동일 시간의 대기, 단순 접근 자세 개선, 고정 관측 규칙과 one-step outcome predictor로 설명되지 않는 이득이 남는가?

이는 아직 검증되지 않은 **조건 분석·평가 질문**이다. Frozen VLA라는 제한만으로 신규성이 생기지 않는다. Multi-step RL은 두 번 이상 관측할 때 유의미한 선택이 필요하다는 증거가 나온 후에 검토한다. 기존 데이터 적응보다 적은 비용으로 유용한 선택을 한다는 주장도 전체 데이터·학습 비용을 비교한 뒤에만 가능하다.

## 새로 확인한 직접 충돌

| 연구 / status | 확인한 내용 | C1에 반영한 수정 |
|---|---|---|
| **ActiveAlign — Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation**, arXiv 2026-10-16, venue 미검증 | [본문 III–V](https://arxiv.org/html/2610.23378v1). AP endpoint에 맞춘 alignment·replay·successful-continuation SFT. Matched-state 및 data-matched controls가 있으며 단순 camera augmentation과 구분한다. | 관측–정책 불일치의 발견과 observation-aligned SFT를 새 기여에서 제외. “기존 논문에 pose/data control이 없다”는 주장도 제외. |
| **EyeRobot 2.0**, arXiv 2026-10-02, venue 미검증 | [본문 §3–6](https://arxiv.org/html/2610.03710v1). Task-specific gaze target selector를 action-prediction reward로 RL 학습하고 gripper BC와 co-train. Fixed stereo에서 virtual fixation하며 head/neck motion은 다루지 않는다. | 시선 순서 RL과 action-loss reward는 신규성이 아님. [저자 code repository](https://github.com/kerrj/eyerobot2/tree/c5f21cc7f3fa166395bda862745de955f16932e4)는 확인 시 README만 있고 code/data는 coming soon이다. |
| **EgoReveal**, arXiv 2026-10, venue 미검증 | [본문 III–IV](https://arxiv.org/html/2610.12999). Separate camera arm, visibility convergence로 한 번 switch한 뒤 manipulation 수행. ORA는 target mask 면적의 시간 변화와 threshold를 사용한다. | Detector만 비교하지 말고 visibility-convergence handoff도 비교해야 함. 별도 camera arm의 효과를 wrist-camera 이동과 동일시하지 않음. |
| **PhysCaP**, arXiv 2026-08, venue 미검증 | [본문 §3–4](https://arxiv.org/html/2608.21031). Proprioceptive physical-property measurement와 planner/prioritizer로 탐색·종료를 결정하고 interaction/time을 평가한다. | “관측 비용에 따라 종료한다”는 일반론도 선행 연구가 있음. C1은 visual sensing과 fixed native VLA라는 구체적 설정에서 검증해야 함. |

ActiveAlign의 중요한 비교 조건: π0.5의 46.3% → 11.5% → 72.7%는 **perturbed-start** protocol의 Standard / Naive Active / ActiveAlign이다. Prescribed benchmark init에서는 96.8% / 48.0% / 96.6%다. 이를 native LIBERO 정책의 일반 성능 저하나 보편적 개선으로 옮겨 쓰지 않는다. 한 번의 pre-contact AP이며 재관측 중단 최적화의 직접 검증은 아니다. 읽은 본문·abstract에서 저자 code/checkpoint 링크를 식별하지 못했으며, 미공개라고 확정하지 않는다. [III-D, IV-A/B, V](https://arxiv.org/html/2610.23378v1).

기존 [AAWR·TVVE·SaPaVe 비교](./LITERATURE.md)도 유효하다. 추가 문헌은 새 알고리즘을 정당화하기보다 **반드시 이겨야 할 설명과 비교군**을 늘렸다.

**평가 방법 자체도 신규성에서 제외한다.** 기존 제외 후보에서 확인했던 [RESCUE, §III-A/B](https://arxiv.org/html/2610.13516)는 고정 nominal policy, state–intervention별 success, remaining budget, counterfactual branch와 replay fidelity를 이미 정의한다. 이 틀에서 intervention을 `look`으로 바꾸는 것만으로 새 평가 기여를 주장하지 않는다. C1에는 관측 행동 특유의 미해결 현상이나 일반화되는 설명이 추가로 필요하다. 이는 두 문제를 비교한 연구자 판단이며 RESCUE가 visual sensing 실험을 수행했다는 뜻은 아니다.

## Native policy를 좁힌 결과

첫 실행 전제 확인에는 SmolVLA의 **LIBERO 전용 공개 checkpoint**를 선택했다. Base/community checkpoint에 새 action head를 붙이지 않는다.

| 항목 | 정적 확인 결과 |
|---|---|
| Checkpoint | [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/6721902bc4d61e50a3bfdb11dfb4cb626f05d102), revision 고정. Weights 1,218,047,032 bytes는 Hub metadata 값이며 runtime memory가 아님 |
| Observation | Scene RGB + wrist RGB, state 8D = EEF position 3 + axis-angle 3 + 실제 gripper qpos 2 |
| Action | Native 7D relative OSC. Gripper command와 actual qpos를 구별 |
| Temporal interface | `n_obs_steps=1`, chunk 50, 실행 action 1개, flow steps 10 |
| Preprocessing | RGB channel-first [0,1] 후 LIBERO H/W flip 1회, checkpoint mean/std, policy 내부 512×512 padding. Native shape 256×256와 current CLI default 360×360를 혼동하지 않음 |
| Source | LeRobot v0.6.1 `7e241bd…`; HF LIBERO `8561c60…`. 정확한 값·URL은 source audit에 있음 |
| 실행 경계 | 현재 ARM64 Docker에 약 7.65 GiB memory. CPU inference가 필요한 설정. 실행 가능성은 source/metadata만으로 확정하지 않음 |

근거: [policy config](https://huggingface.co/HuggingFaceVLA/smolvla_libero/blob/6721902bc4d61e50a3bfdb11dfb4cb626f05d102/config.json), [policy 구현](https://github.com/huggingface/lerobot/blob/7e241bd630a3719a56157a497ce5d08f244784f1/src/lerobot/policies/smolvla/modeling_smolvla.py), [환경 processor](https://github.com/huggingface/lerobot/blob/7e241bd630a3719a56157a497ce5d08f244784f1/src/lerobot/processor/env_processor.py), [환경 wrapper](https://github.com/huggingface/lerobot/blob/7e241bd630a3719a56157a497ce5d08f244784f1/src/lerobot/envs/libero.py).

**공개 성능 근거의 한계:** 고정한 [checkpoint model card](https://huggingface.co/HuggingFaceVLA/smolvla_libero/blob/6721902bc4d61e50a3bfdb11dfb4cb626f05d102/README.md)는 `datasets: unknown`과 일반 템플릿 명령을 담고 있으며, 이 checkpoint의 task별 성공률·평가 recipe는 제공하지 않는다. [고정한 LeRobot LIBERO 안내](https://github.com/huggingface/lerobot/blob/7e241bd630a3719a56157a497ce5d08f244784f1/docs/source/libero.mdx)의 성능 표와 `n_action_steps=10` 재현 명령은 π0.5에 대한 것이다. 이를 SmolVLA의 검증된 성능이나 실행 설정으로 옮기지 않는다. 이번 probe는 checkpoint config의 `n_action_steps=1`을 유지했으며, native schema 호환과 task competence를 별도로 판정한다.

## 설계에서 제거한 잘못된 가정

1. **한 번 봤으면 VLA가 기억한다는 가정.** 확인한 SmolVLA 구현은 최신 image/state만 선택하고 action queue만 유지한다. `use_cache=true`를 episode visual memory로 해석하면 안 된다. 같은 최종 observation·state·instruction·noise로 복귀하고 policy queue도 같다면 과거 관측만 바꿔서는 해당 policy의 출력이 바뀔 경로가 없다. 이는 코드에서 도출한 조건부 결론이다.
2. **Wrist 이동을 순수 정보 수집으로 간주.** 팔 자세, 접근 경로, 남은 시간도 바뀐다. 기본 실험의 estimand는 sensing motion의 총효과다. 별도의 개입 없이 성능 차이를 정보 이득이라고 부르지 않는다.
3. **Simulator camera teleport가 물리 관측.** 같은 robot state에서 camera extrinsics만 바꾸는 검사는 진단으로 구분하고 실제 movement 결과와 합치지 않는다. ActiveAlign도 simulation IK와 physical continuous motion을 구별한다.
4. **Task seed만 같으면 paired branch.** LIBERO wrapper는 reset 때 init-state index를 증가시킨다. 각 arm의 index, model RNG, controller와 policy state를 맞춰야 한다. `set_init_state`가 모든 wrapper/controller/cache 상태를 복구한다고 가정하지 않는다.
5. **관측 후 새 episode budget 지급.** Native horizon에서 sensing에 사용한 control steps를 차감한다. MuJoCo integration step과 20 Hz control step을 혼용하지 않는다.
6. **더 좋은 branch가 존재하면 RL 필요.** 사후 최고 branch는 개선 여지의 진단일 뿐 배포 가능한 선택기가 아니다. 현재 관측에서 예측 가능한지, 단순 지도학습으로 충분한지를 따로 본다.

## 진행 판단

- **이번 작업 범위:** 기존 체크포인트의 bounded native probe, source/interface 고정, 식별 가능한 최소 비교 설계.
- **아직 미통과:** 충분한 native success, 이동 후 continuation competence, 서로 다른 상태에서 관측 순이득의 부호 변화, 관측 가능한 선택 근거.
- **보류:** 큰 branch sweep·learned selector·VLA RL fine-tuning·새 알고리즘 이름·navigation/여러 로봇 확장. 현재 근거로 C1을 top-tier 방법 연구의 주제로 채택하기는 부족하다.
- **기각할 설명:** ActiveAlign의 알려진 shift만 재현하거나 항상 같은 viewpoint가 최선이면 C1을 새 RL 방법으로 진행하지 않는다.

이 단계에서 다음 저비용 작업으로 C2의 직접 충돌 문헌 검토를 제안했다. 이후 2026-10-21 검토 결과는 [C2_REVIEW.md](./C2_REVIEW.md)에 기록했다. C1의 불확실성 때문에 C2가 자동으로 더 유망해지는 것은 아니며, C2도 방법 연구 채택은 보류했다.
