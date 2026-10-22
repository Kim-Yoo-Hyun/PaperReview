# 외부 문헌 대조와 근거 범위

- Checked: 2026-10-21 KST
- 대상: Registry 외부의 직접 선행·반증·비교 기준 21편. 검색 결과 전체를 세거나 venue별 quota를 채운 목록이 아니다.
- **15편의 공식 학회·저널 출판 확인**, **6편은 arXiv/status unverified**로 유지한다.
- 아래 `관련 본문`은 표시한 section을 확인했다는 의미다. 전편 정독, code 재현, 사용자 reading status의 승격을 뜻하지 않는다.
- 세 후보의 가설은 [CANDIDATES.md](./CANDIDATES.md), machine-readable source ledger는 [SEARCH_AUDIT.json](./SEARCH_AUDIT.json)에 있다.
- **후속 갱신:** 아래 표는 최초 탐색 당시의 확인 범위다. 이후 E04·E07·E15의 관련 본문/code와 E01/E02의 실제 metadata를 확인하고 acquisition 계보 7편을 추가했다. 최신 C4 판정·근거는 [buildup 문헌 검토](../2026-10-21_c4_reward_audit/LITERATURE_REVIEW.md)를 따른다.
- **C5 후속 갱신:** E08·E09·E16 관련 본문과 autonomous RL 계보를 대조한 [C5 문헌 검토](../2026-10-21_c5_reset_audit/LITERATURE_REVIEW.md)를 추가했다. AutoEval 공개 payload와 code 감사는 그 폴더에서 별도로 관리한다.
- **C6 후속 갱신:** E11–E13·E18을 확장하고 A-OPS·STEP·N-SCORE·RACE 등을 대조한 [C6 문헌 검토](../2026-10-21_c6_checkpoint_audit/LITERATURE_REVIEW.md)를 추가했다. 기존 21편 표를 소급해 정독 완료로 바꾸지 않는다.

## 보상 학습과 정책 개선

| ID | 정확한 title / 공식 status | 확인 범위 | 이번 판단에 주는 제약 |
|---|---|---|---|
| E01 | **Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons** — [RSS 2026 proceedings](https://www.roboticsproceedings.org/rss22/p140.html) | [본문 v2](https://arxiv.org/html/2603.02115v2), IV-Q3, V, Appendix E-2; [reward code](https://github.com/robometer/robometer), [policy code](https://github.com/robometer/robometer-policy-learning) README/interface | Progress와 trajectory preference, 실제/합성 실패를 함께 쓰며 VLA 기반 RL도 평가한다. 실패 데이터 활용·online RL 결합 자체는 이미 존재 |
| E02 | **RoboReward: General-Purpose Vision-Language Reward Models for Robotics** — [arXiv, 2026](https://arxiv.org/abs/2601.00675), acceptance 미확인 | [본문 v2](https://arxiv.org/html/2601.00675v2), §3, §5.3, §6; [공개 dataset card](https://huggingface.co/datasets/teetone/RoboReward) | Counterfactual/temporal negatives와 reward accuracy→RL 효과를 이미 평가. C4를 이 상관관계의 최초 연구라고 부를 수 없음 |
| E03 | **Position: Good Embodied Reward Models Need Bad Behavior Data** — [ICML 2026, position paper](https://proceedings.mlr.press/v306/tian26o.html) | [본문](https://arxiv.org/html/2606.01036v1), §3–4 | 실제 나쁜 행동에 대한 과대 보상과 negative example 보정을 제시. 중요성의 근거이면서 broad novelty의 직접 충돌 |
| E04 | **PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement** — [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html) | 공식 abstract·[paper의 공개 텍스트](https://openaccess.thecvf.com/content/ICCV2025/papers/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.pdf) 도입부 | Goal-conditioned reward를 online adversarial refinement. C4는 OOD reward correction을 새 개념으로 주장하지 않음. Update식·공개 code 상세 대조는 다음 gate |
| E05 | **General Process Reward Modeling for Robotic Reinforcement Learning** — [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) | 공식 metadata·abstract | General process reward와 downstream robot RL의 비교 기준. Robo-Dopamine이라는 project/preprint 명칭과 별도 논문으로 중복 취급하지 않음 |
| E06 | **Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement** — [RSS 2026](https://www.roboticsproceedings.org/rss22/p079.html) | [본문](https://arxiv.org/html/2606.18247v1), §6.1의 policy·baseline, 실험 질문 | VERITAS의 verifier-guided rollout/SFT가 있으므로 reward가 좋은 trajectory를 골랐다는 효과와 RL 최적화 효과를 구별해야 함 |
| E07 | **When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering** — [RSS 2026](https://www.roboticsproceedings.org/rss22/p142.html) | 공식 abstract | Semantic uncertainty와 policy feasibility를 구분하고 act/clarify/intervention을 선택. C4를 generic ask-or-learn supervisor로 만들면 직접 충돌. Full method/code 확인 필요 |
| E15 | **Active reward learning and iterative trajectory improvement from comparative language feedback** — [IJRR, Vol.45 Issue 9](https://journals.sagepub.com/doi/abs/10.1177/02783649251394742) | Publisher metadata·abstract; [저자 project](https://liralab.usc.edu/comparative-language-feedback/) 링크 확인 | Active reward querying 자체는 선행 연구. First online 2025-11-12와 2026 issue를 구별. 현재 full method 확인 전이므로 acquisition novelty를 확정하지 않음 |

### C4에 가장 직접적인 관찰

Robometer Appendix E-2는 frozen π0 위 DSRL을 사용하며, reward model의 점수를 reward와 success detection에 함께 쓴다. 같은 절에서 잘못된 목표의 조작이나 near-miss를 성공으로 판정하는 문제가 online learning을 해치는 사례를 보고한다. 본문의 저자 측 결과이며 우리가 재현한 현상이 아니다. [관련 본문, Appendix E-2](https://arxiv.org/html/2603.02115v2)

이 근거는 **“reward false positive가 실제 학습 문제일 수 있다”**를 지지한다. **“우리 acquisition rule이 낫다”**, **“static 정확도는 무의미하다”**, **“Robometer도 같은 실패를 보인다”**는 결론은 지지하지 않는다. 서로 다른 reward model의 비교를 label 선택의 인과 효과로 바꾸어 읽지 않는다.

공개 repository는 per-frame progress/success와 trajectory preference inference를 안내한다. 또한 LIBERO용 별도 checkpoint의 training에 LIBERO suite와 failure data를 사용했다고 명시한다. 따라서 같은 suite를 자동으로 held-out으로 두지 않는다. [Reward README](https://github.com/robometer/robometer), [OOD dataset card](https://huggingface.co/datasets/robometer/rbm-1m-ood). 데이터 payload·checkpoint·native 실행은 검사하지 않았다. Project의 RBM-1M 전체 데이터 release 표기와 실제 배포 범위도 후속 데이터 gate에서 구분해야 한다.

## 자율 데이터 수집과 reset

| ID | 정확한 title / 공식 status | 확인 범위 | 이번 판단에 주는 제약 |
|---|---|---|---|
| E08 | **AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World** — [CoRL 2025](https://proceedings.mlr.press/v305/zhou25a.html) | [본문](https://arxiv.org/html/2503.24278), reset 설계와 Appendix G–H; [code](https://github.com/zhouzypaul/auto_eval) 링크 확인 | 자동 reset·success/invalid detection이 실제 시스템 요소다. C5의 편향은 이 논문이 실패했다는 결론이 아니라 후속 검증 가설 |
| E09 | **So You Think You Can Scale Up Autonomous Robot Data Collection?** — [CoRL 2024, PMLR publication 2025](https://proceedings.mlr.press/v270/mirchandani25a.html) | 공식 abstract; [volume의 개최 연도](https://proceedings.mlr.press/v270/) 대조 | 자율 수집이 인간 데이터보다 항상 효율적이지 않다는 negative result. 새로운 자율 수집 시스템도 human-cost baseline이 필요 |
| E10 | **Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning** — [ICLR 2026 Poster](https://openreview.net/forum?id=nAO9LcV7nE) | 공식 OpenReview metadata·abstract; [OmniReset project](https://omnireset.github.io) 링크 확인 | 다양하고 구조화된 reset 자체는 이미 강한 RL 연구 방향. C5는 physical reset이 유도하는 selection과 비용으로 좁힘 |
| E16 | **Adaptation of Generalist Robot Policies with Minimal Data** — [arXiv, 2026](https://arxiv.org/abs/2608.11363), acceptance 미확인 | [본문 v1](https://arxiv.org/html/2608.11363v1), §6·8, Appendix F–G | MiDAS는 reset curriculum으로 position robustness를 넓히고 behavioral support의 한계를 논한다. “VLA RL에 reset curriculum 추가”를 제외 |

C5의 구분점은 curriculum의 목표 분포를 선언하는 것보다 **실제로 그 시작 상태를 만들 수 있는가, 못 만든 sample을 어떻게 계수하는가**에 있다. Fixed target 평가·물리 reset 비용을 분리하지 않으면 독립 기여가 약하다. 현재 자료로 reset-induced collapse가 실제 존재한다고 판정하지 않았다.

## 평가·critic 및 넓은 후보의 직접 충돌

| ID | 정확한 title / 공식 status | 확인 범위 | 이번 판단에 주는 제약 |
|---|---|---|---|
| E11 | **Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection** — [CoRL 2025](https://proceedings.mlr.press/v305/anwar25a.html) | [본문](https://arxiv.org/html/2502.09829), formulation·cost·§VI–VII | Policy–task outcome distribution과 active testing을 이미 제안. 본문에서 일부 EIG 전략이 random-task보다 효율적이지 않았다는 결과도 확인. Learned selection의 우월성을 가정하지 않음 |
| E12 | **Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation** — [RSS 2026](https://www.roboticsproceedings.org/rss22/p154.html) | [본문 v1](https://arxiv.org/html/2605.11479v1), §IV–V·VII–VIII | Timeout, recovery, value optimism을 직접 다룸. Perceptually similar state의 잘못된 연결과 OOD 한계를 저자가 명시. Arbitrary new-policy OPE 보장으로 확대하지 않음 |
| E13 | **Scaling Robot Policy Evaluation via Discrete Diffusion World Model** — [ICML 2026](https://proceedings.mlr.press/v306/li26hi.html) | 공식 abstract | dWorldEval은 action-causal world model과 policy ranking을 다룸. World-model evaluator 추가 자체를 후보에서 제외 |
| E14 | **Informed Asymmetric Actor-Critic: Leveraging Privileged Signals Beyond Full-State Access** — [ICML 2026](https://proceedings.mlr.press/v306/ebi26a.html) | 공식 abstract | Privileged signal 선택·informativeness 기준까지 선행 연구. VLA에 privileged critic을 붙이는 broad proposal 제외; theorem assumptions 전체 검증은 하지 않음 |
| E21 | **RL's Razor: Why Online Reinforcement Learning Forgets Less** — [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) | 공식 abstract | Robotic foundation model에서 RL/SFT의 forgetting과 policy divergence를 비교. Generic RL retention 주제를 재시작하지 않음 |

## 최신 preprint의 충돌 검사

Top-tier 출판이 확인되지 않았더라도 같은 질문을 먼저 다루는 preprint를 신규성 검토에서 제외하지 않는다. 아래는 acceptance를 주장하지 않는 비교 문헌이다.

| ID | 정확한 title / 출처 | 확인 범위 | 후보와의 관계 |
|---|---|---|---|
| E17 | **ARS: Agentic Reward System for Robot Learning** — [arXiv 2609.34484](https://arxiv.org/abs/2609.34484) | [본문 v1](https://arxiv.org/html/2609.34484v1), §2·5; [code](https://github.com/midea-ai/ars) 링크 확인 | Explicit verification·offline curation이 이미 존재. 저자는 later observation을 사용하는 방식과 causal online reward를 구분함. C4를 여러 agent의 영상 검수로 바꾸는 것만으로는 부족 |
| E18 | **ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training** — [arXiv 2602.12691](https://arxiv.org/abs/2602.12691) | Abstract·[저자 project repository](https://github.com/AgibotTech/aloe) | Mixed-policy experience에서 chunk-level TD/value learning을 이미 다룸. 이 GitHub는 project webpage이며 학습 코드 공개 증거가 아님 |
| E19 | **ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning** — [arXiv 2512.16861](https://arxiv.org/abs/2512.16861) | [본문 v1](https://arxiv.org/html/2512.16861v1), §4.2–4.3; [project](https://reinforcegen.github.io/) | Termination false positive filtering과 학습/배포 termination 차이를 다룸. Detector를 더 잘 만들자는 주장은 신규성이 없음 |
| E20 | **World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training** — [arXiv 2509.24948](https://arxiv.org/abs/2509.24948) | [본문](https://arxiv.org/html/2509.24948), §4.2–4.3·5.3, Algorithm 1 | Reward와 종료를 결합하며 post-success action 문제를 다룸. 이전 C3 탐색 때 제외한 stopping 방향을 다시 후보화하지 않음 |

## 검색·해석의 경계

검색은 공식 RSS 2026 proceedings에서 출발해 CoRL/PMLR, ICLR/OpenReview, CVF ICCV/CVPR, IJRR publisher로 넓혔다. Reward·reset·active evaluation·privileged critic을 나누어 검색하고 최신 arXiv를 직접 충돌 필터로 사용했다. Awesome-Progress-Reward-Model·Awesome-Robot-Verifier는 후보 발견에만 사용했으며 최종 status·method 근거는 위 primary source다. 논문 저자의 GitHub README도 실행 성공이나 reproducibility의 증거는 아니다.

이는 전 venue의 systematic review나 “동일 연구가 전혀 없다”는 증명이 아니다. 최초 탐색에서 남겼던 E04·E07·E15의 관련 method/code와 active reward learning 계보 대조는 후속 C4 buildup에서 수행했다. 넓은 acquisition 주장은 기존 연구와 충돌하며 정책 효과는 아직 측정하지 않았다. RoboReward의 공식 OpenReview forum/API는 최초 접근에서 verification/403 응답으로 final status를 확인하지 못해 arXiv로 유지했다. Peer-review가 없다고 단정한 것이 아니다.

현재 registry의 IQL·SERL·ConRFT·DSRL·SimpleVLA-RL은 actor update와 native runtime을 선택할 때의 기존 기반이다. 이번 외부 논문들은 그 위에서 **reward feedback, 실제 수집 분포, 평가 선택**이라는 별도의 문제 설정을 비교하도록 추가한 검토 자료다. 신규 paper admission·CORE/NEXT 승격이나 사용자 정독 완료는 하지 않았다.
