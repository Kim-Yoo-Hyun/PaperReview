# VLA 업데이트 이후 residual reinforcement learning의 재사용과 적응

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)의 VLA+RL 대안이다. 교체 후 과거 보정의 비용상 가치라는 질문은 조건부 유망하지만, A residual 구축과 B 적응을 모두 검증해야 한다. 최근의 단일 모델 선호에서는 UNIFIED 뒤에 둔다. 아래 11/05의 “주 탐색”은 당시 권고다.

현행 비실험 상태 검토: **2026-11-06** · [7단계 상태·기여 가설·판단 분기](#buildup-status). 기존 문헌/계약/결과를 대조한 보강이며 새 효과 관측은 없다.

**11/05 통합 판단:** 기존 6개와 새 2개를 함께 봐도 VLA+RL 주 탐색으로 유지한다. FIRe의 동일 residual 이식과 BAS-VLA의 frozen-policy calibration을 넘어서, 독립적으로 갱신된 B에서 과거 residual 경험이 같은 추가 interaction의 fresh residual·gain·성공 BC/return-weighted imitation보다 가치가 있는지를 묻는다. Base B 단독 성능과 A 학습을 포함한 총비용도 별도로 보고한다. 새 방법 GO나 native 유용성 입증은 아니다. [11/06 N2 비교](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md#integrated-n2)를 완료했으며 기존 P0 자원/구현 대기는 유지한다.

**11/06 식별 범위 보완:** 현재 F/W/U/Z/G/P는 모두 `D_A`를 받으므로 비교는 공통 과거 데이터 아래 초기화/anchor의 가치다. 과거 데이터 접근 자체의 효과를 입증하지 않는다. 공개 A/B의 exact parent SHA와 B의 우월성도 아직 확인되지 않았다. FEEDBACK은 다른 robot·single-action·normalizer를 쓰므로 실행 adapter와 경험 데이터를 직접 합치지 않는다. 원 단일 비교 계약·P0 상한은 변경하지 않았다.

근거·전체 상대 비교: [기존 6개+새 2개 공백 검토](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md). 신규 paper별 확인 절과 status는 [등록 원장](../../../sources/registry_admissions_2026-11-05.json)에 통합한다. 기존 실행 계약·원시 결과·과거 source 날짜는 보존한다.

Updated: 2026-11-03 KST. **내부 비실험 buildup 완료 · 탐색 후보 유지 · native 효과 미검증**.

## 1. 연구 질문과 현재 판단

**VLA를 새 checkpoint로 교체했을 때, 이전 VLA에서 학습한 행동 보정을 그대로 쓰거나 적은 상호작용으로 적응시키는 편이 다시 학습하는 것보다 유리한가?** 새 base가 이미 해결한 오류에는 보정이 불필요할 수 있고, 공통으로 남은 오류에는 이전 보정이 도움이 될 수 있다는 **가설**이다. 실제로 그런 일이 발생했거나 보정 필요성을 예측할 수 있다는 결과는 아직 없다.

목표는 VLA의 성능 개선과 현장별 RL 적응을 함께 쓰는 시스템에서 **base 교체 뒤 다시 수집해야 할 데이터와 성능 손실**을 줄이는 판단 근거다. 첫 범위는 같은 Panda·같은 task·두 checkpoint이며 로봇 간 전이가 아니다. 원래 로봇 간 RL 전이 후보의 RETIRED 판단을 재개하지 않는다.

**연구 가치 판단:** 작은 현상·비용 비교를 할 가치가 있다. 독립적인 방법의 신규성은 미확정이다. Q-filter·residual regularization 자체는 선행이며, 새 benchmark에서 이 조합을 실행한 성능표만으로 top-tier 기여를 주장하기 어렵다. 재사용이 유리하거나 불리한 조건과 그에 따른 적응 선택이 여러 업데이트에서 반복되면 실증·방법·시스템 기여로 발전할 수 있다. 이는 연구자 판단이며 채택 예측이 아니다.

11/05 재확인에서도 macOS ARM64 Docker의 NVIDIA CUDA 조건을 충족하지 못했다. **GPU만 있으면 검증이 끝나는 상태는 아니다:** P0 launcher·native adapter·image recipe 초안은 작성했지만 실제 build·package closure·asset·CUDA/EGL·모델 IO는 미검증이다. 제어·중단 장치 9개 Docker 검사는 정책 실행이 아니다. [재현 방법](../재현%20방법/README.md)과 [환경·재개 명세](../재현%20방법/RESUME_PLAN.json)에 작성/검증 범위를 분리했다. Residual 학습·효과 비교는 여전히 후속이다.

- 근거 원장: [42편 survey 및 source별 확인 깊이](../../../sources/vla_rl_gap_review_2026-11-03.json). 41편은 2024–2026, 1편은 2018 Q-filter foundation이다. 전체 registry 정독이나 venue 전수조사가 아니다.
- Canonical 비교 계약: 같은 원장의 `r2_review.comparison_contract`. 아래 설명은 그 계약을 사람이 읽도록 정리한 것이다.
- 전체 gap 탐색 이력과 예비 후보: [공통 survey](../../../update/VLA_RL_GAP_REVIEW_2026-11-03.md).
- 단계 기준: [buildup guide](../../../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates). 실제 독립 피드백은 미수신이다.

## 2. 가장 가까운 선행이 이미 답한 것

| 선행·확인 위치 | Base·residual 관계와 확인된 전이 | 이 질문에 주는 제약 / 미확정 |
|---|---|---|
| [Object-Centric Residual RL, CoRL 2026 accepted](https://www.corl.org/program/accepted-papers), [arXiv §3·5.4, 부록 A.1–A.4·A.7](https://arxiv.org/html/2606.18953v1) | 같은 시연 행동으로 sim/real base를 정렬하고 sim에서 학습한 residual을 real base에 연결한다. Residual 학습 중 base는 고정. 별도로 rollout을 이용한 base SFT도 보고 | **같은 residual의 base 교체는 이미 존재.** GR00T↔π0.5 동일 가중치 및 SFT된 base에 이전 residual을 다시 붙인 결과는 확인 범위에서 미확정. 저자 페이지에서 공식 training code 미식별 |
| [PLD, ICLR 2026](https://iclr.cc/virtual/2026/poster/10008318), [§3, 부록 B·C](https://arxiv.org/html/2511.00091v1) | Frozen base의 task별 residual → hybrid 수집 → generalist SFT. 배포는 개선된 generalist | Residual을 데이터 생성에 쓰는 경로가 선행. Actor–learner update frequency는 base 버전 전이 실험이 아니다. 최종 conference 본문 접근 제한; author v1과 동일하다고 가정하지 않음. 검색되는 `stpark7/pld`는 custom implementation이며 공식 release가 아님 |
| [VLaRL, 2026 preprint](https://arxiv.org/html/2609.30868v1), III-D·IV, VI-C | VLA와 latent mapper를 단계적으로 고정한 뒤 residual 학습. VI-C는 mapper의 backbone별 구성, residual의 task-category별 학습을 명시 | 여러 backbone의 평가를 단일 residual 가중치 전이로 읽을 수 없음. 잠재표현까지 바꾸면 action shift 외의 혼란 변수가 추가됨. 공유 residual은 해당 논문의 향후 방향이며 신규성 보증이 아님 |
| [EXPO, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d56a652ad743308b24b6c4d0e6411dd7-Abstract-Conference.html), [§4·Algorithm 1](https://arxiv.org/html/2507.07986v3) | Base는 replay imitation, edit policy는 Q 최대화로 함께 갱신. Base/edited action 중 Q로 선택 | **Base가 바뀔 때 editor도 적응하는 구조와 Q 선택은 기존 방법.** 독립 배포된 새 checkpoint에 동결 editor를 이식하는 프로토콜과 구분 |
| [EXPO-FT, CoRL 2026 accepted](https://openreview.net/forum?id=U3Nmrhun8B), [§4.2–4.3·부록 C](https://arxiv.org/html/2605.25477v1) | VLA action chunk와 editor를 함께 학습하고 human intervention 사용. Base image encoder 고정은 전체 VLA 고정과 다름 | [공식 code](https://github.com/pd-perry/expo-ft/blob/21fe3d3b7d913c80836496817965932f49e0aedf/expo_ft/agents/alg/expo_ft.py#L734)의 `update_actor`→`actor.train_step`, `_update_jit` 호출도 확인. 공동 적응 baseline이며 현재 π0.5/DROID 통합을 LIBERO에 바로 실행할 수 있다고 가정하지 않음 |
| [Policy Decorator, ICLR 2025 최종 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf), §4.1–4.3·부록 B.5 | Frozen BeT/DP 위 SAC residual, bounded correction·controlled exploration | Model-agnostic **방법 적용**과 같은 residual 가중치 이식은 구분. 독립 base 업데이트 후 재사용 실험은 확인한 절에 없음; 모든 후속 연구의 부재를 뜻하지 않음 |
| [FIRe 저자 project](https://rcilab.khu.ac.kr/FIRe/), Methodology·RQ5 | **같은 residual policy**가 GR00T·π0.5·OpenVLA에 전이한다고 명시. Force/proprio/상대 pose를 쓰는 contact correction | RA-L **submitted**, acceptance 미확인. Paper/code coming soon, 링크된 PDF는 404. 체크포인트와 학습 provenance는 미확인이나 단순 ‘VLA 간 residual 전이’ 신규성에 직접 충돌하므로 제외할 수 없음 |

공식 acceptance와 읽은 본문 버전을 분리했다. PLD/Object-Centric의 최종 conference PDF와 전체 training source를 모두 확인했다는 뜻은 아니다. EXPO/EXPO-FT의 공개 code는 읽기만 했고 실행하지 않았다. EXPO의 `expo_learner.py`도 `update_actor`와 `update_edit_actor`를 같은 update에서 호출한다. FIRe의 제출 상태·공개 미완료를 이유로 이미 공개된 아이디어를 없는 것으로 취급하지 않는다.

## 3. 적응 규칙을 정하며 확인한 선행

| 근거 | 이번 결정에 쓰는 내용 | 신규성·source 경계 |
|---|---|---|
| [Accelerating Residual RL, RA-L 2026 issue](https://doi.org/10.1109/LRA.2025.3636808), [본문 IV-B·V-D](https://arxiv.org/html/2506.17564v2) | Critic에 residual 단독이 아닌 합성 행동을 넣는 방식. [공식 code](https://github.com/lakshitadodeja/uncertainty_aware_residual_rl/blob/8125f33dcf490d4cf93d57a27d3e1963a47f52ea/serl_launcher/serl_launcher/agents/continuous/assymetric_sac.py#L134)도 실제 합성 행동을 사용 | 기존 방법으로 채택. 이를 base-update를 위한 새 critic으로 주장하지 않음. IEEE 페이지는 JS 제한; 저자 accepted 표기·publisher-deposited Crossref의 2026/01 issue를 구분 |
| [Nair et al., Q-Filter 절·식 (8)](https://arxiv.org/pdf/1709.10089), [ICRA 2018 DOI](https://doi.org/10.1109/ICRA.2018.8463162) | Demonstration이 현재 actor보다 높은 Q를 가질 때만 BC를 적용 | 2018 foundation이며 최신 trend로 세지 않음. 유용한 과거 행동만 모방한다는 원리 자체는 신규성이 아님 |
| [DICE-RL, ICML 2026](https://proceedings.mlr.press/v306/sun26al.html), [v2 §4](https://arxiv.org/html/2603.10263v2) | Frozen prior·chunk critic·선택적 행동 정규화·value-based selection. [공식 image learner](https://github.com/zhanyisun/dice-rl/blob/98d936e52523878f0172e606ea32403176497100/model/rl/distill_residual_rl_img.py)에서 Q 및 Monte-Carlo 기반 filter 확인 | ‘유용한 residual만 허용’도 이미 다룸. 아래 TD3/Q-filter 비교는 이 논문 전체 재현이 아니며 원래 stochastic prior·MC filter·데이터 구성과 다름 |
| [MiDAS v3, 2026-10-21](https://arxiv.org/html/2608.11363v3), §4·6, 부록 E·I.4·J | Few-demo base의 residual 학습, representation·success replay·filtered imitation 비교. DICE와 공유 원리도 명시 | 초기 v1의 다른 title/부록 번호와 구분. [CoRL R2RL workshop 목록](https://r2rl-workshop.github.io/)은 main-track acceptance가 아님. 작은 residual과 적은 시연을 결합한다는 발상도 선행 범위 |

**판단:** Q-filter와 두 reference를 조합하는 것만의 신규성은 약하다. 남겨 둔 것은 *독립적인 base 업데이트 후 어떤 과거 보정이 아직 유효한가*와 그 재사용 비용이다. 같은 선행을 다른 benchmark에 이식한 성능표만 남으면 독립 기여로 올리지 않는다. 위 논문들의 모든 결과·code를 재현했다는 뜻은 아니다.

## 4. 고정하는 task·관측·행동

- **Task:** LIBERO-10의 `STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy`. [고정 task BDDL](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/bddl_files/libero_10/STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy.bddl)의 `In black_book_1 desk_caddy_1_back_contain_region`만 성공으로 쓴다. 단일 물체 배치를 골라 다중 물체 순서 효과를 줄였으며 성능을 보고 고른 task가 아니다. 임의 release/dwell 조건을 추가하지 않는다.
- **Robot/controller:** pinned LIBERO의 Panda·OSC_POSE·20 Hz. [wrapper 기본값](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/env_wrapper.py) 확인. 실제 package/controller 설정·asset hash·EGL은 P0에서 검증한다. 한 episode는 warmup 뒤 최대 520 control steps. `H=C=8`: 8-step chunk 전체를 실행 후 다시 관측한다. Sim time 기준 0.4초이며 실시간 지연 연구가 아니다.
- **VLA A/B:** [재현 문서](../재현%20방법/README.md#checkpoints)의 revision·normalizer를 그대로 참조. 동일 단일 RGB·원 instruction·결정적 discrete decode. 모델 자체의 proprio 입력은 꺼 둔다. 양쪽 모두 같은 dtype/processor를 명시하고 load·precision 영향은 P0에서 구분한다.
- **Residual 관측 `x`:** 최근 두 chunk 경계의 RGB를 **A의 동결 vision backbone+projector**로 각각 처리한 patch mean, 두 시점의 EEF position/axis-angle/gripper qpos(8차원), 직전 실행 command(7차원), 남은 시간 비율. RGB는 원 224 입력 전처리, proprio는 A의 공통 q01/q99 통계를 사용한다. 첫 history는 현재 관측을 복제한다. [공식 `_process_vision_features`](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/utils/vla_utils/openvla_oft/modeling_prismatic.py#L467)의 vision→projector 경로만 재사용하며 language hidden state·B의 갱신된 encoder를 섞지 않는다. Feature 차원 `d`는 loader 출력에서 확인하고 `dim(x)=2d+24`로 구성한다. 이 encoder도 실제 사용 검증 전이다.
- **입력 경계:** actor는 `x`와 현재 base의 normalized 8×7 chunk를 받는다. Critic은 `x`와 합성된 환경 command chunk를 받는다. Hidden object pose·goal predicate·force·privileged critic은 사용하지 않는다. Goal predicate는 reward/evaluator 전용이다. 고정 지시 한 개이므로 language generalization의 근거는 만들지 못한다. 두 frame도 완전한 Markov state를 보장하지 않는다.
- **보정 행동:** `uθ∈[-1,1]^(8×6)`, scale `α=0.1`. Base의 normalized translation/rotation 6좌표에 `αuθ`를 더하고 [-1,1]로 clip한 뒤 **원 normalizer→gripper binarize/invert→controller command clip** 순서를 적용한다. Gripper는 base 것을 그대로 쓴다. α는 meter/radian 단위가 아니다. `C_v(x,u)`를 이 전체 합성 연산으로 정의한다. `C_v(x,0)`이 원 VLA 환경 명령과 같은지 P0에서 검증한다. Gripper 오류·지원 밖 큰 이동은 이 제한된 residual로 고칠 수 없다.

Frozen A encoder를 선택한 것은 표현 변화와 행동 변화를 처음부터 섞지 않기 위해서다. 그것이 critic 학습에 충분한 표현인지는 별도 가정이다. 이 경로가 실패하면 residual 전이 전체의 불가능으로 해석하지 않는다. Extra proprio·encoder 비용은 모든 residual/IL 비교군에 동일하게 제공하고, VLA 단독의 비용과 구분해 기록한다.

## 5. 선택한 한 가지 적응 규칙

**규칙: 가치 비교로 기존 residual 또는 새 base를 선택적으로 모방하는 TD3 적응.** 설명용 이름이며 신규 알고리즘 이름을 붙이지 않는다. A에서 학습한 actor `uA`는 별도 동결 사본으로 남기고 B의 현재 chunk를 입력해 `u_old=uA(x,b_B(x))`를 얻는다. 적응 actor `uθ`는 A 가중치로 시작한다. B에서는 A의 critic·target critic·optimizer를 이어받지 않는다.

두 target critic을 `Q̄1,Q̄2`, 세 command 후보를 `c_old=C_B(x,u_old)`, `c_0=C_B(x,0)`, `c_θ=C_B(x,uθ)`라 하자. 두 critic 모두 같은 reference를 다른 두 후보보다 높게 평가할 때만 다음 mask를 켠다.

```text
w_old = 1[for both critics: Qbar(c_old) > max(Qbar(c_0), Qbar(c_theta))]
w_0   = 1[for both critics: Qbar(c_0)   > max(Qbar(c_old), Qbar(c_theta))]
L_actor = E[-Q1(x, C_B(x, u_theta))
            + 0.1 * (w_old * mean((u_theta - stopgrad(u_old))^2)
                     + w_0 * mean(u_theta^2))]
```

Mask는 gradient를 통과시키지 않으며 strict tie·critic 불일치이면 둘 다 0이다. 현재 actor가 더 좋은 경우에도 과거 행동으로 당기지 않는다. `w_old`와 `w_0`는 동시에 1이 될 수 없다. 이는 **estimated value에 따른 정규화**이지 보정의 인과적 필요성·성공 보존 보증이 아니다. 두 critic의 동의도 보정된 신뢰구간이 아니다. Q 오차로 잘못된 행동을 유지하거나 좋은 보정을 버릴 수 있다.

Critic은 원 데이터의 합성 command를 입력받는다. 성공 직전 `k≤8` step만 실행되면 실제 prefix의 reward 합과 `k`를 저장한다. Target은 `R_k + 0.99^k (1-done) min_i Q̄_i(x', C_B(x', u_target+noise))`다. Task 성공·520-step deadline은 terminal, 수집 예산으로 끊긴 episode는 censored이며 성공/실패 label로 확정하지 않는다. Future reward를 사용해 action 입력 mask를 바꾸지 않는다.

기본 actor/critic은 256–256 ReLU MLP, Adam 3e-4, batch 256, target τ=0.005, critic update/decision=1, actor delay=2다. Target residual noise σ=0.2·clip 0.5, 수집 residual noise σ=0.1, 평가 noise=0으로 고정한다. Noise는 `u` 좌표에서 넣고 [-1,1]로 clip한다. A 초기 actor는 마지막 층을 0으로 두고 처음 100 decision은 수집만 한다. 성공 보상은 첫 native success에 1, 나머지 0이며 dense reward·새 demonstration을 추가하지 않는다. 소예산 sparse RL 실패 가능성을 명시한다.

**Replay 이전:** A의 raw transition `D_A`는 모든 적응군에 동일하게 준다. B가 같은 과거 관측에서 내는 action은 결정적 query로 새로 계산·cache하고 비용을 기록한다. 과거 reward/next observation/실제 command는 바꾸지 않는다. `r_old`를 B 행동에 그대로 더한 가상 transition으로 relabel하지 않는다. Critic은 공통 `D_A: D_B = 1:1` batch, actor와 anchor는 B-stage 관측만 사용한다. 물리 transition의 재사용 가능성과 Q값의 불변성은 다르다. B continuation이 바뀌므로 critic을 다시 학습한다.

공통 B probe 250 decision에서 B 또는 B+동결 residual을 episode 단위 1/2 확률로 선택해 데이터를 모은다. 같은 reset/수집 seed의 이 자료와 `D_A`로 **B 단독 continuation**의 critic을 500회 warmup하여 모든 군에 복제한다. 이후 각 군은 자기 continuation으로 같은 budget의 TD3를 수행한다. Actor별 optimizer와 actor target은 각각 초기 actor에서 새로 시작하고, critic optimizer도 복제 후 같은 초기 상태로 맞춘다. 모든 군이 과거 data에 접근하므로 fresh는 *actor 가중치만 fresh*이며 tabula-rasa baseline이 아니다.

## 6. 비교군과 비용을 혼동하지 않는 규칙

| 군 | 이전/적응 방식 | 무엇을 구분하는가 |
|---|---|---|
| Static | A, A+rA, B, B+rA, calibration으로 고른 B+λrA | 원 보정 이득·base 자체 변화·zero-shot 재사용. λ={0,.25,.5,1}; λ=0/1은 B/B+rA와 재사용, tie는 작은 λ |
| F | Fresh actor, 같은 old data·공통 초기 critic, λ_anchor=0 | 과거 actor 가중치의 가치 |
| W | A actor warm-start, anchor 없음 | 단순 재학습 이후 추가 가치 |
| U | A actor warm-start, 항상 기존 u_old로 anchor | 과거 보정을 무조건 유지하는 효과 |
| Z | A actor warm-start, 두 critic에서 base가 현재 actor보다 좋을 때만 0으로 anchor | 기존 Q-filter를 새 base 보호에 적용한 강한 대조. DICE 전체 재현이라고 부르지 않음 |
| G | A actor warm-start, 두 critic에서 old가 현재 actor보다 좋을 때만 old로 anchor | 표준 teacher Q-filter; 새 base와의 비교를 추가할 이유가 있는가 |
| P | §5의 두 reference 규칙 | ‘old냐 base냐’를 추가로 비교하는 것이 필요한가 |
| IL-S / IL-R | W와 같은 D_A·공통 probe·W 수집 데이터를 사용해 success-only / return-weighted imitation, 각 500 actor updates | RL의 목적함수가 같은 데이터 선택/모방보다 주는 이득. 데이터 수집 비용은 W 비용을 그대로 부과 |
| Q-select | 공통 warmup critic의 min-Q로 B와 B+rA 중 선택, tie는 B | EXPO식 두 후보 선택만으로 충분한가. 동일 common-probe 비용, 추가 Q 비용 포함. EXPO/EXPO-FT 전체 재현 아님 |

모든 적응군의 actor/critic 크기·추가 interaction·update cap·sensor·residual bound는 동일하다. U/Z/G/P의 anchor 계수도 0.1로 같다. 같은 데이터를 쓴다는 뜻은 F–P가 같은 **online trajectory**를 갖는다는 뜻이 아니다. 각 군의 수집은 정책에 따라 달라진다. 따라서 P–W 차이만으로 mask의 인과 효과가 입증되지는 않는다. 후속 동일 replay 학습 비교가 필요하며 이번에는 자동 실행하지 않는다.

IL은 raw residual label을 복사하지 않고 **합성 command의 6개 연속 좌표 MSE**를 최소화한다. B의 제한된 보정 범위 밖 target, gripper 불일치 비율을 보고한다. 성공 episode가 없으면 IL-S는 `NO_SUCCESS_TARGETS`로 표시하며 성능 0으로 꾸미지 않는다. IL-R은 완결 episode의 실제 return-to-go `G`에 `exp((G-Gmax)/0.1)`을 적용해 minibatch 평균 1로 정규화한다. Censored trajectory는 return label에서 제외한다. 두 IL군은 W와 같은 A actor 초기화·B data 접근을 사용한다. 이 비교는 residual adapter의 RL 대 imitation이며 full-VLA SFT 비교가 아니다.

`r_keep=c_A-b_B`는 A+rA의 합성 행동을 그대로 복원하는 항등식이다. 별도 유료 학습군으로 만들지 않고 A+rA static row로 대표하며 새로운 B 이득을 보존했다는 증거로 쓰지 않는다. 원 DICE-RL·EXPO-FT의 완전하고 공정한 native 재현은 **새 방법 우수성 주장 전 필요**하지만 첫 IO/현상 탐색의 진입 조건은 아니다.

## 7. Split·예산·판정

**Split:** 공개 init-state ID 0–29는 학습, 30–39는 calibration, 40–49는 최종 평가다. 최소 50개 존재·ID와 state hash·중복 여부를 P0 준비에서 확인해야 하며 아직 payload를 열지 않았다. 50개 미만이면 임의 재사용하지 않고 계약을 수정한다. 공개 base의 학습 중 해당 장면 노출은 미확정이므로 OOD 또는 base의 미관측 test를 주장하지 않는다. 동일 task의 residual-stage reset 분할이다. 평가 단위는 **서로 다른 init state 10개**이며 frame·chunk·반복 query를 독립 trial로 세지 않는다.

Seeds는 A actor=101, B probe/reset sampling=303, 공통 critic=202, 적응 update RNG=404로 고정한다. Environment는 공식 helper처럼 `seed(0)`을 고정하고 init-state ID가 reset 차이를 만든다. 각 군은 같은 ID 순서를 사용한다. 학습 seed 한 개의 탐색이며 여러 seed의 robustness 주장은 금지한다. 최초 buffer/weight 선택은 마지막 고정 update를 쓰고 평가 성공률로 고르지 않는다.

| 단계 | 상한 / 실행 순서 | 현재 상태 |
|---|---|---|
| P0 IO | 1 dev init state(ID 0), A/B 각 1 query·1 chunk, 각 reset의 10 warmup 포함 **최대 36 env steps·VLA query 2회**, vision feature call 최대 4회. Zero residual·norm·gripper·shape·same reset 확인 | 다음 실행 준비 대상. 전체 task success/전이 판정 아님 |
| P1 A residual 학습 | 최대 4,000 chunk decisions·32,000 policy steps·reset 160회. 같은 cap에서 자동 연장 안 함 | P0 통과 뒤 별도 단계. rA checkpoint 현재 없음 |
| P1 static/calibration | A/A+rA/B/B+rA/λ=.25/λ=.5, 각 10 calibration states: 최대 60 episodes·31,200 policy steps | A 보정 이득과 B의 개선 여지 탐색. 모든 결과 공개 |
| P2 공통 probe·적응 | Probe 250 decisions·2,000 steps·reset 40회. F/W/U/Z/G/P 각각 **1,000 decisions·8,000 steps·reset 60회**, actor updates 500·critic updates 1,000. 초기 critic warmup 500회는 별도 공통 비용 | 조건부 연구 예산이며 다음 TODO의 자동 학습 범위 아님 |
| Held-out 평가 | Static 5군×10, 적응 6군×{0,500,1000 decisions}×10, IL 2군+Q-select×10 = 최대 **260 episodes·135,200 policy steps**. 모든 checkpoint 보고, 선택/튜닝 금지 | 이 비교 전체는 미실행. 작은 평가 표본의 탐색 범위 |

전체 후속을 모두 수행할 경우 policy steps 상한은 **248,416**(P0의 16 포함), warmup까지 포함한 env-step 상한은 **257,236**이다. 평가 비용도 작지 않다. Rollout VLA query 상한은 31,052회, 별도 old-state B cache는 최대 8,000회다. CPU bookkeeping을 제외한 GPU-hour·encoder/query 비용·reset·학습과 평가 비용을 모두 따로 보고한다. 이 수치는 실행 시간/필요 VRAM 실측이 아니며 P0 예산과 혼동하지 않는다.

Decision·step·reset cap 중 하나라도 먼저 도달하면 해당 수집을 멈춘다. 같은 cap이 실제 사용량까지 같다는 뜻은 아니다. 실제 도달한 공통 decision 지점에서 비교하고, 미도달한 500/1000 checkpoint를 복제하거나 결측 성능을 채우지 않는다. Update 수도 실제 수집량에 따라 줄어들 수 있으므로 위 표의 값은 상한으로 기록한다.

**Primary 관측:** `ΔA=J(A+rA)-J(A)`, `ΔB=J(B+rA)-J(B)`, 고정 추가 budget의 `J(P)-J(W/F/Z/G)`와 B 대비 퇴행. 성공률뿐 아니라 같은 초기 상태의 win/loss/tie, 완료 steps, correction/clip 빈도, mask 선택률, 성공 데이터 수를 남긴다. 0/500/1000 decision 세 점은 거친 탐색 곡선이며 sample complexity나 유의한 SOTA를 입증하지 않는다. B가 성공했던 reset의 실패 전환과 그 반대도 기술하되, 관측 결과로 만든 subgroup을 새로운 독립 검정 집합처럼 쓰지 않는다.

**진행·수정 규칙:**

1. P0 실패는 실행 실패로 기록한다. A/B·zero-residual·frame/normalizer가 정합하지 않으면 학습을 시작하지 않는다.
2. Calibration에서 A+rA의 이득이 보이지 않거나 모든 rollout이 실패하면 해당 cap의 residual bootstrap이 미확인이다. 전이 불가능의 반증으로 쓰지 않고, 큰 학습으로 자동 연장하지 않는다. B가 이미 전부 성공하고 retained correction도 필요 없어 보이면 이 pair는 방법 발전에 정보가 부족하다.
3. 동결 residual·gain·W·G/Z가 충분하면 그 결과를 받아들인다. P를 무조건 이기게 할 perturbation·task·threshold를 사후 추가하지 않는다. 반대로 작지만 재현 가능한 교체 효과가 있으면 다음 탐색을 허용하며 통계적 확증을 입장 조건으로 요구하지 않는다.
4. P가 우세해도 ‘Q-filter 조합의 신규성’으로 승격하지 않는다. 독립적인 추가 update/task·seed, 원 DICE/EXPO 계열의 공정 비교, 비용/representation/replay 통제가 있어야 더 넓은 기여를 평가할 수 있다. 평가 10개와 training seed 하나만으로 top-tier 가치 확정은 불가다.

<a id="nonexperimental-completion"></a>

## 8. 추가 비실험 점검 — 대안 설명과 주장 범위

| 설명·위험 | 결과를 구분할 비교/기록 | 현재 판단 |
|---|---|---|
| B 자체가 좋아진 효과 | A 대 B와 각각 residual의 추가 이득을 따로 기록 | ΔB−ΔA는 조건별 효과 차이의 기술값이며 RL 업데이트의 인과 효과가 아님. Exact A→B lineage도 미확정 |
| 보정 크기만 너무 큼 | Calibration의 λ=0/.25/.5/1, 동일 clip·비용 | Gain으로 충분할 수 있다. 미리 실패를 가정하지 않음 |
| Actor 입력의 base action 분포가 바뀜 | 같은 관측에서 A/B chunk 차이와 입력 support·clip 빈도를 기록 | 고정 encoder는 representation drift만 줄인다. `uA(x,bB)`의 입력 변화까지 제거하지 않으므로 ‘B가 오류를 이미 고침’만으로 원인을 단정할 수 없음 |
| 과거 데이터나 warm-start만 도움이 됨 | F/W/U/Z/G/P의 공통 D_A·초기 critic·cap, IL-S/IL-R | Fresh는 actor만 fresh. P–W의 online trajectory도 달라 mask의 인과 효과까지 분리한 실험은 아님 |
| Critic의 과대추정으로 잘못된 anchor 선택 | Twin Q·분산/불일치·mask 빈도·실제 성공을 따로 기록 | 두 critic은 독립적인 진실 판정기가 아님. [DICE §4 식 (6)](https://arxiv.org/html/2603.10263v2#S4)는 Monte-Carlo consistency까지 사용한다. 현재 규칙에는 그 보정이 없어 알려진 약점으로 남김 |
| α=.1·gripper 고정·8-step feedback이 필요한 보정을 막음 | Bound/clip·gripper mismatch·첫 실패 위치 기록 | P 실패가 residual 재사용 일반 불가능의 증거가 아님. 평가 뒤 bound를 몰래 늘리지 않고 수정 설계로 기록 |
| 단일 task의 높은 B 성공률 또는 낮은 A competence | A/B 및 A+rA calibration 결과를 먼저 공개 | 효과가 드러나지 않는 pair일 수 있다. 사후 실패 task/perturbation 검색을 자동 진행하지 않음 |
| Two-frame state가 충분하지 않음 | History·controller/queue 초기화와 입력 사용 경로를 검증 | 부분 관측 상태의 Q approximation이며 정확한 Markov/Bellman 보장을 주장하지 않음 |

**수작업 반례·계약 점검 결과:**

1. 같은 additive 좌표에서 `r_keep=c_A−b_B`는 과거 합성 행동을 복원할 뿐 새 base의 이득을 활용했다는 증거가 아니다. 실제 clip·gripper·controller를 포함한 composition을 비교해야 한다.
2. `u=0`이면 원 base 경로와 같아야 한다. 이를 실수 연산상 항등식으로 검토했지만 실제 dtype·normalizer·controller IO의 일치는 아직 확인하지 않았다.
3. Strict Q 순위는 old/base mask의 동시 활성화를 막는다. 모든 Q가 틀렸거나 같으면 이 성질만으로 좋은 행동을 고르지 못한다.
4. 실제 old command·reward·다음 관측의 재사용은 가능하지만, B를 붙인 반사실 transition으로 바꾸거나 old Q를 불변값으로 쓸 수는 없다.
5. A residual 학습은 anchor 없는 TD3로 A continuation을 쓴다. R2의 old/base anchor는 학습된 rA가 생긴 뒤 B 적응에만 적용한다. A target에 B를 넣는 구현을 막기 위해 계약에 명시했다.
6. 성공 보상의 discounted return과 episode success는 다르다. Reward-to-go에서 빠른 성공을 선호해도 최종 보고의 primary는 native success와 비용이며 둘을 같은 수치로 쓰지 않는다.
7. Censored episode는 success/failure 또는 imitation return label로 채우지 않는다. Terminal 직전 chunk는 실제 실행 길이 k를 기록하고, 수집 cap으로 끊는 경우 그 지점의 다음 관측/시간을 보존한다.

위 점검은 문헌·수식·정적 source 검토이며 합성 실험이나 정책 관측이 아니다. Normalizer metadata의 action 7차원·proprio 8차원도 대조했으나 환경의 실제 필드 순서는 P0에서 확인한다.

## 9. 주장과 필요한 증거

| 잠정 주장 | 관측되면 남길 결과 | 줄이거나 버릴 조건 | 현재 |
|---|---|---|---|
| Base 교체 후 residual 재사용에 중요한 비용/성능 차이가 있음 | ΔA·ΔB·gain·paired 성공 전환·추가 데이터 비용 | 단순 재사용으로 충분하거나 차이가 중요하지 않음 | 미실험 |
| 과거 actor 가중치가 새 data에서 가치가 있음 | 같은 old data·공통 critic의 W 대 F | Fresh와 차이가 없거나 warm-start가 나쁨 | 미실험 |
| 두 reference 선택이 단순 대안보다 유용함 | P 대 W/U/Z/G·gain·Q-select·IL, 비용 포함 | Gain/단일 anchor/같은 데이터 imitation으로 설명 | 미실험 |
| 다른 업데이트에도 재사용 가능한 원리임 | 별도 update·task·학습 seed에서 예측이 유지 | 한 pair의 우연·representation/예산 차이만 남음 | 첫 pilot 이후 조건부 연구 |
| 실물 deployment 비용을 줄임 | 실제 robot의 재수집·reset·latency와 실패 비용 | 시뮬레이터 결과만 있음 | 주장하지 않음 |

결과표는 `arm / training seed / init-state ID / native success / terminal reason / executed steps / base queries / encoder calls / new interactions / updates / elapsed time / peak VRAM / correction-clip-mask statistics`를 가진 episode 단위 행으로 만든다. 숫자는 아직 채우지 않는다. 동일 init state의 win/loss/tie와 각 정책의 성공 개수를 함께 제시하고, 10개 편의 표본·학습 seed 1개에서 population 신뢰구간이나 유의한 SOTA를 주장하지 않는다.

논문의 중심 이야기는 “두 Q-filter를 합쳤다”가 아니라 **base 업데이트 이후 local RL 지식을 재사용하는 선택이 언제 비용을 줄이는가**다. 결과가 모두 예상대로여도 한 pair뿐이면 탐색 결과다. 필요한 후속 원 논문 baseline·update/task 확장은 이미 §6–7에 적었으며 첫 P0의 진입 조건으로 앞당기지 않는다.

<a id="buildup-status"></a>

## 10. 비실험 buildup 현행 상태 — 2026-11-05

**판정: 탐색 유지 · 내부 비실험 검토 정리 · native IO/학습된 residual/효과 미검증.** [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 기존 문헌·논리·계약에 적용해 정리했다. 아래 상태는 새 실험 결과나 11/04 신규 문헌 전수조사가 아니다.

**한 문단 기여 가설:** VLA 교체 때 현장별로 학습한 보정을 버릴지 재사용할지 결정할 근거가 필요하다. 기여 후보는 **독립적인 base 업데이트 후 과거 보정 가중치가 추가 상호작용 비용을 줄이는 조건**이다. 이미 알려진 Q-filter 조합의 성능 개선만으로 독립 방법 기여를 세우지 않는다.

| 비실험 단계 | 상태 | 현재 근거·완료 경계 |
|---|---|---|
| 1 문제·독자 | 정리됨 | §1: VLA 배포·적응 연구자가 base 교체 후 재수집/재학습을 선택하는 문제. 현장 빈도·실제 비용은 미측정 |
| 2 가까운 선행 | 지정 범위 확인 | §2–3 및 42편 source 원장: 공동 적응, sim-to-real, 여러 backbone 적용과 독립 checkpoint 교체를 구분. 일부 최종본/code는 미확인 |
| 3 질문·대안 | 정리됨 | §8: gain, base-action 입력 변화, critic 오류, old data, warm-start·모방을 대조. Exact A-parent 불명은 RL 업데이트의 인과 주장 범위를 제한 |
| 4 기여 서술 | 가설 초안 | 위 중심 기여와 §9 주장–증거 표. 비용 절감·방법 우월성·다른 로봇 전이는 결과 칸을 비워 둠 |
| 5 최소 비교 | 설계됨·미실행 | §6–7 및 원장의 r2_review.comparison_contract. 먼저 2 query/36 env-step IO; 이후 A residual이 유용한지부터 확인 |
| 6 실행 부담 | P0 코드·recipe 초안 작성, native 검증 대기 | [재개 명세](../재현%20방법/RESUME_PLAN.json): host 중단 확인·제어 검사 9개 통과. Native image/의존성 closure·실제 reset/asset·rA는 미확보. P0와 후속 학습 비용 구분 |
| 7 외부 비판 | 질문 준비·미수신 | §11의 직접 선행·가중치 가치·총비용 질문. 실제 발송/응답 없음; 내부 자기비판은 독립 검토가 아님 |

**결과에 따른 판단 — 아직 관측하지 않은 분기 포함**

| 다음 증거 | 바뀌는 판단 | 이 증거만으로 하지 않을 주장 |
|---|---|---|
| A에서 residual 이득부터 확인할 수 없음 | 해당 bootstrap/예산의 실현 가능성부터 수정 | Residual 전이 일반 불가능이라는 결론 |
| Gain·warm-start·동일 데이터 모방으로 충분함 | 저렴한 재사용 조건을 실증 결과로 남기고 새 규칙 개발 투자를 줄임 | 복잡한 규칙의 필요성을 사후 가정 |
| 여러 교체에서 단순 대안 이후 재사용 이득이 반복됨 | 추가 update/task에서 조건 예측과 공정 원 논문 baseline 비교를 검토 | 첫 pair의 우위를 곧바로 새로운 알고리즘·cross-embodiment 성과로 승격 |

**비용을 두 관점으로 적는다.** 기존 rA가 이미 있는 운영자는 교체 이후 추가 수집·학습·검증 비용을 본다. 처음 도입하는 운영자는 A residual 구축 비용까지 본다. 과거 비용을 모든 비교에서 숨기거나 이중 부과하지 않는다. 실행 시간/VRAM은 미측정이며 전체 후속 sweep은 P0 승인 범위가 아니다.

**외부 검토 준비:** 가장 강한 외부 질문은 “EXPO/DICE류의 알려진 적응을 적용한 뒤에도, 이 교체 조건에서 재사용 결정을 바꾸는 새 지식이 남는가?”다. 검토자는 §1·§2–3·§6–9를 읽고 직접 선행 또는 가장 싼 반례를 지적할 수 있다. 실제 응답·반영이 생기면 내용과 source 위치를 기록한다. 미수신은 작은 탐색을 금지하는 진입 조건이 아니다.

**다음 확인과 문서 종료점:** 다음 판단은 같은 문헌 집계가 아니라 기존 P0와 A residual의 유용성, 또는 직접 선행을 특정한 외부 반론이다. 첫 구현 주에는 A/B action 의미·zero-residual·reset 연결의 실제 trace와 미완료 항목을 검토한다. 완료 기간 추정이 아니며 다른 학습/평가를 자동 실행하지 않는다. 새로운 직접 선행·자료·반례·피드백 없이 같은 문서 검토를 반복할 내부 과제로 만들지 않는다. 실행 범위·상한은 기존 계약과 [재현 안내](../재현%20방법/README.md)가 관리한다.

## 11. 독립 검토를 받을 때 보여 줄 질문

검토용 brief는 §1, closest-work는 §2–3, 반증 가능한 비교는 §6–9다. 외부로 전송하지 않았으며 아래 질문을 준비했다.

- EXPO의 공동 적응·DICE의 선택적 regularization을 독립 checkpoint 교체에 적용하면 질문이 대부분 해결되는가? 그렇더라도 재사용 비용에 남는 중요한 경험적 지식은 무엇인가?
- 동일 로봇·한 task의 교체 효과가 현장에서 반복되는 문제인지, 단순 input shift를 새 문제처럼 포장한 것인지 어떤 추가 근거가 필요한가?
- Fresh에도 D_A를 주는 actor-weight 비교가 주장을 제대로 겨냥하는가? 실제 사용자 총비용은 A residual의 과거 비용까지 포함해 별도로 보고해야 한다는 구분에 동의하는가?
- Gain·W·G/Z·IL 중 가장 싼 반례는 무엇인가? 결과가 모두 긍정적이어도 새 지식이 약한 부분은 무엇인가?

**다음 실질적 행동:** 호환 NVIDIA 컴퓨터에서 [재개 안내](../재현%20방법/README.md#resume)의 `check → build → prepare → p0`를 수행하고 실제 실패가 있으면 해당 의존성/adapter를 수정한다. P0만 검증하며 그 전에는 새 학습·효과 검증 완료로 상태를 올리지 않는다.
