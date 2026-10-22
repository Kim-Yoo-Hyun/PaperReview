# C3 문헌·공개 구현 검토

- 확인일: 2026-10-21 KST. 2024–2026 frontier와 직접적인 이전 이론을 함께 대조했다.
- 아래는 후보 조사이며 신규 registry admission·사용자 정독 완료를 의미하지 않는다.
- 주 결과: [C3 판단](./README.md) · [고정한 검증 계약](./PROTOCOL.md).

## 후보 선택에서 제외한 넓은 주장

| 검토한 방향 | 직접 근거와 읽은 범위 | 결정 |
|---|---|---|
| 성공 후 행동으로 결과를 망치지 않도록 종료 학습 | [World-Env](https://arxiv.org/html/2509.24948), §3.3/5.3, Fig.8/Table4. Success 후 지연 종료와 GT termination 없는 평가를 이미 다룸. 이 문서에서는 arXiv로 인용하며 acceptance 미확인 | 일반적인 stop/reward 설계는 새 주제로 선택하지 않음 |
| VLA RL이 여러 성공 전략을 유지하게 하기 | [Uni-TMPO](https://arxiv.org/abs/2609.34688), abstract 확인. Mode collapse와 VLA OOD strategy diversity를 직접 동기로 제시. 2026-09 preprint, venue 미확인 | 제목 차별화 수준의 diversity 제안 제외. 본문 기반 신규성 판정까지 진행한 것은 아님 |
| 사용하지 않는 padded action dimension을 RL loss에서 제거 | [RLinf GR00T 코드](https://github.com/RLinf/RLinf/blob/91a302ec50ddacd1fdabc5859b85e3661d768236/rlinf/models/embodiment/gr00t/gr00t_n1d7/gr00t_action_model.py#L973), L973–975 | 이 경로는 이미 env action dimension으로 log probabilities를 자름. Padding 버그를 발견했다고 주장하지 않음 |
| 같은 실제 gripper 명령으로 매핑되는 token의 RL update | 아래 native source chain과 기존 MPG 이론 | **현재 컴퓨터에서 mechanism 검증 가능. C3로 선택했으나 알고리즘 신규성은 별도 보류** |

## 직접 선행 연구

| 연구 | 공식 status·source | 확인 범위 / C3에 대한 함의 |
|---|---|---|
| Clipped Action Policy Gradient — Fujita & Maeda | **ICML 2018**, [PMLR](https://proceedings.mlr.press/v80/fujita18a.html), [공식 본문](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf), [저자 코드](https://github.com/pfnet-research/capg) | Abstract·문제 설정·gradient claim 확인. 실행 전 clipping을 알고 있는 unbiased, lower-variance PG는 기존 기여. 저자 코드를 실행한 것은 아님 |
| Marginal Policy Gradients — Eisenach et al. | **ICLR 2019**, [공식 PDF](https://openreview.net/pdf?id=HkgqFiAcFm), [저자 본문 v3](https://arxiv.org/html/1806.05134v3) | §4.1–4.4 및 Eq.의 기대 gradient 일치·분산 감소 확인. 일반 transform까지 포함하므로 C3의 원리는 이 연구의 적용 사례. 공식 검색 색인에서 published header 확인; OpenReview 직접 열기/API는 challenge/403이어서 본문은 arXiv HTML 사용 |
| SimpleVLA-RL | **ICLR 2026**, [공식 PDF](https://openreview.net/pdf?id=TQhSodCM4r), [저자 본문](https://arxiv.org/html/2509.09674), [공식 코드](https://github.com/PRIME-RL/SimpleVLA-RL) | §2–3.4의 token GRPO·outcome reward·KL penalty 제거 및 공개 LIBERO recipe 확인. 공식 검색 색인의 published header와 저자 repo 표기를 대조. 전체 학습/성능을 재현하지 않음 |
| ManiPhysicsBench | **arXiv 2026-10**, [본문](https://arxiv.org/html/2610.02802), [공식 코드](https://github.com/sangwu99/ManiPhysicsBench_Arxiv) | §6.1–6.2, App.F 확인. 이 평가는 wrapper binarization을 끄고 실제 joint target을 집계한다. 그 histogram은 C3 checkpoint의 conditional token logits가 아니므로 분산 이득을 계산하는 데이터로 대체할 수 없음 |
| ActionOPD | **arXiv 2026-10**, [abstract](https://arxiv.org/abs/2610.19820) | Abstract 기반. 언어 tool-use agent에서 token 대신 semantic action을 정렬하는 논문. 로봇 PPO에 대한 직접 실험은 아니지만 “token 대신 action”이라는 넓은 표현도 새 기여로 충분하지 않음 |

CAPG·MPG가 원리의 직접 충돌이다. 최신 exact gripper-class PPO 논문이 검색되지 않았다는 사실을 최초성의 증명으로 사용하지 않는다. SimpleVLA-RL과 같은 source-derived finite-function 검사가 논문 전체의 결함을 입증하지도 않는다.

## 실제 실행한 공개 코드의 연결

Revision **`7c51662df27b586f9e8a1ab35fcf849f2b8852f9`**, retrieval 2026-10-21. 아래 line은 이 고정 revision 기준이다. [파일별 SHA-256 및 metadata](../../experiments/vla_rl_c3_interface/evidence/source_audit.json)를 함께 보존했다.

1. [공개 LIBERO recipe](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/examples/run_openvla_oft_rl_libero.sh#L38): action 7차원, chunk 8, clip low 0.2/high 0.28. SFT checkpoint는 저자 collection을 가리킨다.
2. [모델 sampling/decoding](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/utils/vla_utils/openvla_oft/modeling_prismatic.py#L1729): 256-token window에서 sampling, L1742–1744에서 bin center로 decoding. 원본 decoder assignment를 AST로 실행했다. Forward는 미실행이다.
3. 같은 파일 L1421–1440의 native unnormalization. [저자 checkpoint metadata](https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero10-trajall/tree/97d6e58bc5fbc402e85bab382e4206bb8e5f0db0)의 `libero_10_no_noops`, gripper normalization mask=false를 사용했다. Metadata 확인과 checkpoint strict load는 서로 다르다.
4. [rollout L395–400](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/rollout/rob_rollout.py#L395): normalize(binarize=True) → invert → env.step. [원본 gripper utility](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/utils/libero_utils.py#L156) 두 함수를 실제 실행했다.
5. [actor L146–169](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/actor/dp_rob.py#L146): 256 logits에서 sampled token log probability를 얻는다. L499–504의 [native loss](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/trainer/ppo/core_algos.py#L271) 호출로 이어진다.

이 경로에서 256개 token을 열거하면 명령 −1에 65개, +1에 191개가 대응한다. 이는 **주어진 decoder와 metadata의 매핑 개수**다. 훈련된 정책의 열기/닫기 확률이 65:191이라는 뜻은 아니다. Utility에 `np.sign`이 있어 임의의 연속 입력이 정확히 threshold에 놓이면 0도 나올 수 있지만 검사한 256 bin center에는 해당하지 않는다.

## 해석 경계

- 물리 상태·reward가 같아도 token별 regularization이 달라질 수 있다는 가능성을 검증했다. 이것만으로 현재 training이 느리거나 실패했다고 말할 수 없다.
- 원본 raw-token score-function PG는 조건 아래 unbiased다. 실제 action을 raw density에 그대로 대입하는 잘못된 estimator와 혼동하지 않는다.
- Native model parameter의 공유 구조, action chunk 내 상관관계, 실제 advantage는 이번 유한합에 포함되지 않았다. Logit-coordinate variance 감소율을 전체 모델 gradient 감소율로 옮기지 않는다.
- ManiPhysicsBench는 연속 grip control이 필요한 경계를 보여준다. 서로 다른 force/closure command를 편의상 같은 action으로 묶으면 안 된다.
- 이 문제는 로봇 interface에 따라 존재 여부가 달라진다. Binary gripper·continuous force·sticky/hysteretic controller를 나누는 것이 multi-robot 연구의 연결점이며, 지금은 첫 interface만 검증했다.

검색어에는 `VLA reward hacking`, `post-success termination`, `VLA padding log_prob`, `VLA action equivalence`, `vision-language-action marginalization/Rao-Blackwell`, `gripper policy gradient/probability mass`를 포함했다. 검색 결과의 블로그·집계 사이트는 발견에만 쓰고 위 판단은 원문과 공식 구현으로 제한했다.
