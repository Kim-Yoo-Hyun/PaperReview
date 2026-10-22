# C3 후속: 실제 checkpoint 분포 검사 계약

- 작성: 2026-10-21, 실제 logits 관측 전 고정.
- 사용자 요청: C3 다음 단계. [기존 mechanism 검사](./PROTOCOL.md)에 이은 별도 검사이며 policy 성능 실험은 아니다.

## 목표와 입력

실제 pretrained policy의 gripper 확률이 class별 한 token에 이미 집중되는지를 먼저 측정한다. 그 경우 synthetic diffuse-distribution 결과만으로 큰 학습 효과를 예상할 수 없다.

- Checkpoint: `Haozhan72/Openvla-oft-SFT-libero10-trajall`, revision `97d6e58bc5fbc402e85bab382e4206bb8e5f0db0`.
- Code: `PRIME-RL/SimpleVLA-RL`, commit `7c51662df27b586f9e8a1ab35fcf849f2b8852f9`의 OpenVLA-OFT path. 원본 sampling/actor 입력의 action masking과 position을 확인한다.
- 데이터 후보: `lerobot/libero`, revision `a1aaacb7f6cd6ee5fb43120f673cebb0cfea7dd4`. Metadata에서 LIBERO-10 지시를 식별하고 실제 payload를 확인한 뒤 선택 manifest를 동결한다. 이름만 보고 suite를 추정하지 않는다.
- 예정 표본: 최초로 식별되는 native-suite 2개 task × 최초 2개 episode × 길이의 10/30/60/90% frame = 최대 16개 고유 관측. Dataset에 필요한 suite가 없으면 공식 LIBERO 원본의 소규모 payload로 교체하고 logits를 보기 전에 이유·revision을 기록한다.
- 독립 표본의 단위는 관측/episode다. Chunk의 8개 gripper position을 독립 robot episode로 세지 않는다. Demonstration-state 진단이며 on-policy visitation은 아니다.

## 실행 계약

- 현재 Linux ARM64 Docker에서만 실행. Container 7 GiB·6 CPU. Host dependency 설치, remote inference, MPS 사용 없음.
- 15GB급 원 가중치를 CPU/disk offload로 읽는다. 압축/양자화 checkpoint로 바꾸지 않는다. FP32 연산 시 원 BF16 weight 값의 exact cast이며 reference BF16 GPU와의 수치 동등성은 별도 미검증으로 기록한다.
- 최대 임시 disk 48 GiB, 준비/추론 합계 90분의 bounded probe. 한 관측 확인 후 예상 비용이 초과하면 실제 완료한 표본만 보고한다. 실제 forward가 실패하면 logits를 만들지 않는다.
- Strict key/shape coverage, frozen/eval mode, image orientation/resize/crop, prompt, action slots, normalization stats 확인이 선행 조건이다.
- 원본 forward와 memory offload가 계산 순서만 바꾸는지 확인한다. CPU compatibility 수정이 필요하면 diff·범위를 기록한다.
- 산출물: source/weight/data provenance, 실제 256-way action logits와 위치, input hash, 계산 설정, finite 검사와 분석 JSON. 모델·원 데이터·패키지 cache는 Docker 내부에만 두고 종료 시 정리한다.

## 지표와 판정

1. Temperature 1.0과 공개 training recipe의 temperature에서 class mass, token entropy, class entropy, class-conditional top-1 mass, effective alias count, `1 − Σ_class max_token p(token)` 측정.
2. 실제 분포에서 raw/class score covariance trace를 정확히 계산한다. 필요하면 기존 binary reward 조건부 예시를 명시적으로 붙이되 실제 rollout advantage로 부르지 않는다.
3. 같은 실제 logits에 고정한 class-preserving perturbation을 넣은 clipping 진단은 **counterfactual stress test**다. 실제 old/new RL update가 없는 상황에서 관측된 학습 clipping으로 보고하지 않는다.
4. Native model의 마지막 linear head까지 Jacobian을 적용할 수 있으면 범위를 분리하여 기록한다. 전체 backbone gradient나 actual policy-gradient variance를 대신하지 않는다.
5. 실제 분포가 집중되어 potential effect가 작으면 C3 투자 우선순위를 낮춘다. 효과가 남아도 policy 실험 GO를 자동 선언하지 않는다. Actual advantage·matched rollout·strong MPG/binary-head baseline 비교가 남는다.
6. NaN, source/key mismatch, incorrect input, unverified substitute logits는 증거에서 제외한다. 시간·메모리 실패는 가설의 반증과 구분한다.

## 입력 확인 후, logits 관측 전 고정한 세부 사항

- [선택 manifest](../../experiments/vla_rl_c3_logits/evidence/observation_manifest.json): task ID 0의 episode 0·18, task ID 1의 episode 1·4. 각 episode에서 4개 frame, 총 16개다. 공식 LIBERO-10 task-name mapping과 정확한 instruction을 대조했다. 첫 task는 white/yellow mug를 두 plate에 놓기, 두 번째는 white mug와 chocolate pudding 배치다.
- 공개 recipe는 `temperature=1.6`, `num_images_in_input=1`, `use_proprio=False`, `center_crop=True`, 8×7 action chunk다.
- LeRobot의 video copy는 원 LIBERO simulator 대비 이미 180도 회전되어 있다. 추가 회전 없이 공개 `resize_image`의 JPEG encode/decode·Lanczos3 224 resize와 `center_crop_image`의 TensorFlow crop을 실행한다. AV1 압축으로 원 RGB와 동일하지는 않다. [공식 데이터 설명](https://github.com/huggingface/lerobot/blob/afbf3f14a13bdad3e5990e2bed629c6539605658/docs/source/libero.mdx), [공식 orientation 설명](https://github.com/huggingface/lerobot/blob/afbf3f14a13bdad3e5990e2bed629c6539605658/docs/source/env_processor.mdx).
- CPU path는 원본 `forward`를 그대로 호출하고 module pre/post hook에서 BF16 weight를 FP32로 load/release한다. 양자화나 network block 교체는 없다. 첫 decoder layer의 resident/streamed 결과와 native rollout token-position extraction을 별도로 대조한다.
- Native recipe의 asymmetric PPO clip은 `[0.8, 1.28]`다. Counterfactual에서는 class 안에서 token 순서대로 ×0.4/×1.6을 적용한 뒤 원 class mass로 재정규화한다. Advantage는 가상의 `close reward − expected close reward`다. 이는 **실제 gripper advantage·실제 PPO update가 아니다**.
- Score covariance는 실제 확률에서의 `∇log π`를 측정한다. 마지막 linear head의 값은 해당 관측 hidden-state norm을 적용한 조건부 score covariance이며, 전체 backbone 또는 reward-weighted policy gradient의 분산 감소율로 해석하지 않는다.
- 추가 scope 확인: gripper 8개 위치의 감소량뿐 아니라 전체 56개 token의 조건부 score trace에서 차지하는 비중도 기록한다. 이 구현은 sampled token을 다음 slot의 입력으로 넣지 않고 parallel factorized sampling을 하므로, fixed observation에서 final head의 joint score trace를 slot별로 합산할 수 있다. Actual return을 곱하면 이 합산만으로 policy-gradient variance를 알 수 없다.
