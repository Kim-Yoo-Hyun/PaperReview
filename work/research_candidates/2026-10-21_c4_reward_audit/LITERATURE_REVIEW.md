# C4: 가장 가까운 연구와 신규성 경계

- Checked: 2026-10-21 KST
- 기존 E ID는 [외부 탐색 ledger](../2026-10-21_external_search/SEARCH_AUDIT.json), 이번 추가 N ID는 [SOURCE_AUDIT.json](./SOURCE_AUDIT.json)을 따른다.
- 관련 section을 읽은 범위를 명시한다. 사용자 정독 tracker와 별개이며 모든 theorem·실험·supplement를 전부 검증한 기록이 아니다.

## 기존 후보의 직접 충돌 재검토

| 근거 / 확인 범위 | 논문이 이미 한 일 | C4와 남는 차이 및 주의점 |
|---|---|---|
| E01 Robometer — RSS 2026. §IV-Q3, V, Appendix E-2; 이번에는 reward finetune·policy wrapper code | Failure/preference reward와 downstream VLA 기반 online RL. Reward prediction을 성공 종료에도 사용 | Label acquisition을 바꾸는 효과와 reward 모델·종료 규칙 교체 효과를 분리해야 함. LIBERO 특화 모델을 LIBERO 미학습 모델로 취급하면 안 됨. [공식](https://www.roboticsproceedings.org/rss22/p140.html), [본문](https://arxiv.org/html/2603.02115v2) |
| E02 RoboReward — arXiv, 최종 acceptance 미확인. 기존 §3, 5.3, 6 + 이번 실제 metadata | Synthetic negatives·실제 실패를 함께 이용하고 reward 평가와 downstream RL 관계도 분석 | “정적 정확도가 행동을 전혀 설명하지 못한다”는 강한 전제는 부적절. 특정 policy shift에서 선택법 비교가 필요. [본문](https://arxiv.org/html/2601.00675v2) |
| E04 PROGRESSOR — ICCV 2025. 이번 §4.1–4.2, Algorithm 1, §5.1, §7.2 + `online_update` | Expert progress 학습과 최근 non-expert replay의 adversarial push-back을 함께 수행. 사람 label 없이 online reward 수정 | 제한된 human audit 선택은 다르지만 online correction 자체는 기존 기여. Goal image/expert video를 쓰므로 language-conditioned reward와 정보 조건이 다름. [공식](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html), [확인 본문 v1](https://arxiv.org/html/2411.17764v1) |
| E07 UPS — RSS 2026. 이번 §III–V, Appendix A-F + 공개 wrapper/README | Calibrated verifier로 실행·언어 clarification·action intervention을 고름. 같은 intervention trajectory 수로 residual learning 비교 | Residual의 MSE imitation이며 reward-model audit 기반 RL과 동일하지 않음. “uncertainty로 human feedback을 아끼자”는 범위에서는 충돌. [공식](https://www.roboticsproceedings.org/rss22/p142.html), [본문](https://arxiv.org/html/2602.22474v1) |
| E15 Active reward learning … comparative language feedback — IJRR, first online 2025 / issue 2026. 이번 pp.4–8, 10–12 + `next_traj.py`, `info.py` | Reward parameter와 comparative language response의 mutual information을 최대화. BALD/QBC와 비교하며 실제 사람의 시간 비용도 평가 | 고정 trajectory set과 language feedback 문제. 새로운 VLA rollout을 만드는 RL loop와 구분해야 함. [Publisher](https://journals.sagepub.com/doi/abs/10.1177/02783649251394742), [저자 본문](https://liralab.usc.edu/comparative-language-feedback/static/pdfs/journal.pdf) |

PROGRESSOR의 수식은 `stop_gradient(N(βμ, 1/(g−i)²))`를 목표로 하는 KL이다. 공개 commit의 `DrM/metaworld_env.py:401–424`는 detached predicted scale을 유지하고 non-expert KL에 `0.01`을 곱한다. 논문식과 이 구현 선택을 동일한 것으로 기록하지 않는다. 코드에서는 expert loss와 replay loss가 함께 최적화되고, `train_mw.py:287–288`이 online update를 호출한다. 단순 reward 값 곱셈을 이 논문의 재현이라고 부를 수 없다. [Pinned source](https://github.com/ripl/progressor/blob/1482845dab2b55816708633494b4a52163f44c91/DrM/metaworld_env.py#L401)

UPS의 feedback은 action correction이며, IJRR 논문의 feedback은 comparative language다. Binary outcome audit와 모두 “1 label”로 맞추면 정보량·시간·비용이 달라진다. 이들은 직접 재현 또는 interface adaptation 여부를 밝혀야 하는 비교군이지, 이름만 붙여 결과표에 넣을 baseline이 아니다.

## 추가한 acquisition 계보

| ID / status / 확인 범위 | 이미 확보된 기여 | C4에 주는 판단 |
|---|---|---|
| N01 Active Reward Learning with a Novel Acquisition Function — Autonomous Robots 2015. Publisher abstract, 저자 원고 §4·6의 EPD 관련 부분 | Expected policy divergence: reward query가 현재 정책을 바꾸는 정도를 고려 | “정책 영향 기반 검수”라는 일반 발상은 오래된 계보. [Publisher](https://link.springer.com/article/10.1007/s10514-015-9454-z), [저자 원고](https://www.ias.informatik.tu-darmstadt.de/uploads/Team/ChristianDaniel/ActiveRewardLearning.pdf) |
| N02 Learning Human Objectives by Evaluating Hypothetical Behavior (ReQueST) — ICML 2020. §2, acquisition definitions | 모델에서 가상 행동을 만들어 uncertainty·high reward·low reward·novelty로 query. High-reward 질의의 목적에 false positive 검출을 명시 | High-reward audit 자체는 새로운 selector가 아님. 실제 current-policy pool은 차이지만 그 차이만으로 연구적 이득은 미입증. [공식](https://proceedings.mlr.press/v119/reddy20a.html), [본문](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf) |
| N03 PEBBLE — ICML 2021. Algorithm/feedback sampling/relabeling 관련 본문 | Policy와 reward의 교대 학습, replay reward 재계산, feedback-efficient sampling | Frozen reward만 상대하는 비교는 약함. 같은 replay relabel·update 조건의 uniform/entropy/disagreement baseline 필요. [공식](https://proceedings.mlr.press/v139/lee21i.html), [본문](https://proceedings.mlr.press/v139/lee21i/lee21i.pdf) |
| N04 Information Directed Reward Learning for Reinforcement Learning (IDRL) — NeurIPS 2021. §3–7, Algorithm 1 | 후보 정책의 return 차이에 대한 information gain. 후보 정책/쿼리 pool 갱신과 deep RL까지 평가 | C4의 가장 강한 개념 충돌. Reward error 최소화와 정책 개선의 차이, 정책에 따른 query 변경 모두 이미 다룸. 추가 정책 최적화 비용까지 맞춰 비교해야 함. [공식](https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html), [본문](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf) |
| N05 A Generalized Acquisition Function for Preference-based Reward Learning — ICRA 2024, 저자 기관 출판목록 확인; IEEE page 접근 제한. §I, V–VI | Reward parameter 정확도 대신 downstream 행동 동치성·ranking 등으로 reward 유사성을 정의한 acquisition | “행동에 중요한 reward 차이를 보자”도 기존 문제 설정. [저자 기관의 venue 기록](https://aima.eecs.berkeley.edu/~russell/publications.html), [본문](https://arxiv.org/html/2403.06003v1), [IEEE DOI](https://doi.org/10.1109/ICRA57147.2024.10611472) |
| N06 STAIR — NeurIPS 2025. §3–4 및 공식 abstract | Policy 변화에 적응하는 temporal-distance stage 추정과 같은 stage의 preference query 선택 | Multi-stage/task-conditioned sampling도 이미 다뤄짐. Stage 구분만 추가하는 C4 확장은 불충분. 정리의 전체 proof는 이번 감사 범위 밖. [공식](https://proceedings.neurips.cc/paper_files/paper/2025/hash/07fbde96bee50f4e09303fd4f877c2f3-Abstract-Conference.html), [본문](https://papers.neurips.cc/paper_files/paper/2025/file/07fbde96bee50f4e09303fd4f877c2f3-Paper-Conference.pdf) |
| N07 When Self-Belief Misleads … (CARE) — arXiv 2026, acceptance 미확인. §4–5, §7 baseline; 공개 README | Ground-truth/pseudo-label의 advantage 차이를 oracle로 정의하고, reliability·expected correction value를 예측해 query/drop/retain 결정 | Robotics 증거는 아니지만 예상 gradient/advantage 영향에 따른 보정 선택과 직접 가까움. CAG의 GRPO·answer-cluster 전제를 SAC/연속 행동에 그대로 옮길 수 없음. [본문](https://arxiv.org/html/2605.25864v1), [코드](https://github.com/Lumina04/CARE) |

N01은 일반 robotics journal의 foundational collision으로 포함하며 top-tier 최신 논문으로 세지 않는다. N05는 IEEE 본문 접근이 제한되어 공식 page를 읽었다고 표시하지 않는다. N07은 preprint다. 이 7편은 추가 비교 문헌이며 registry admission을 수행하지 않았다.

## 차별화 문장 검토

| 제안 문장 | 판단 |
|---|---|
| 실패 data로 reward model을 고친다 | E01/E02/E03와 중복 |
| Online policy의 OOD reward를 교정한다 | E04와 중복 |
| 높은 reward를 받은 실패 후보를 검수한다 | N02와 직접 충돌 |
| Reward accuracy 대신 policy improvement를 위한 label을 고른다 | N01/N04/N05와 직접 충돌 |
| 정책의 stage 변화에 맞춰 query한다 | N06까지 비교해야 함 |
| 예상 advantage 오류를 줄이는 label을 고른다 | N07과 기전상 가까움. Robotics 적용만으로 충분하지 않음 |
| 기존 선택법의 한계가 native VLA RL에서 어떤 조건에 따라 달라지는가 | 진단 질문으로 가능하지만, 현재 데이터로 관측하지 못했고 새 현상·설명을 입증해야 함 |

검색 범위는 active reward learning, policy divergence, information-directed acquisition, reward hacking audit, active label correction, temporal preference selection과 VLA reward refinement였다. 기존 [21편의 최신 탐색](../2026-10-21_external_search/LITERATURE.md)에 이 계보를 추가했다. 전 분야의 부재 증명이 아니며, 이번 NO-GO는 “문제가 해결됐다”가 아니라 **현재 제안에 독립적인 기여와 검증 자료가 부족하다**는 판단이다.
