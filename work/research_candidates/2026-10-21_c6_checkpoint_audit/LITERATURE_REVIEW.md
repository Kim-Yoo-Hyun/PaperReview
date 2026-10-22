# C6 문헌 비교와 신규성 경계

- 2026-10-21 KST. 최신 창 2024–2026에 foundation을 보충했다.
- 아래 내용은 저자 측 주장/실험을 비교한 것이다. 우리의 재현 결과가 아니다.
- Publication metadata는 proceedings를 우선했다. 본문 확인은 명시한 버전의 관련 구간이며 theorem 전체 검증이나 사용자 정독 완료가 아니다.

## 직접 충돌과 필요한 baseline

| ID | 논문 / 확인된 status | 확인 범위 | C6에 주는 제약 |
|---|---|---|---|
| S01 | **Active Offline Policy Selection** — [NeurIPS 2021](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html) | [본문](https://papers.nips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf) §2–4·limitations; 공개 selector/kernel | OPE prior, policy similarity, active online allocation과 simple regret가 이미 있다. MPG는 simulated Jaco이며 실제 로봇 실험으로 쓰지 않는다 |
| S02 | **Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection** — [CoRL 2025](https://proceedings.mlr.press/v305/anwar25a.html) | [arXiv v1](https://arxiv.org/html/2502.09829v1) §III–VII; 최종판의 code link는 검색된 OpenReview PDF text | Policy–task 선택과 setup cost를 다룸. MetaWorld checkpoint 실험도 있으므로 checkpoint라는 단어 자체가 차별점이 아니다. Mean estimation과 full-distribution fit의 결과를 구분해야 한다 |
| S03 | **Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping** — [RSS 2025](https://roboticsproceedings.org/rss21/p077.html) | [v4](https://arxiv.org/html/2503.10966v4) §II–IV, comparison extension | STEP은 binary outcome의 순차 비교와 다중 비교 확장을 다룬다. Fixed target의 i.i.d. trial 가정이 있으며, 단순 “중간에 멈추는 검정”은 신규 기여가 아니다 |
| S04 | **Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison** — [RSS 2026](https://roboticsproceedings.org/rss22/p076.html) | [v1](https://arxiv.org/html/2603.13616v1) §III–V·VI-C·VII·App. C; N-SCORE code | Bounded progress/reward, multi-policy ranking, RL baseline 비교도 다룬다. Anytime-validity가 test data 재사용에 의한 policy 설계나 무제한 후보 탐색까지 자동 보장하지 않는다 |
| S05 | **Leveraging Correlation Across Test Platforms for Variance-Reduced Metric Estimation** — [CoRL 2025](https://proceedings.mlr.press/v305/luo25a.html) | 공식 abstract; Sim2Val preprint와 title 관계 확인 | Paired auxiliary/real data의 control variate 계보. “값싼 평가를 실측으로 보정”만으로는 신규성이 없다. 구체적 guarantee 적용은 본문 추가 확인 필요 |
| S06 | **Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators** — [arXiv 2025](https://arxiv.org/abs/2510.04354); 저자 [ICRA 2026 표기](https://abadithela.github.io/), 공식 venue 확인은 미완료 | [v1](https://arxiv.org/html/2510.04354v1) §7·App.13의 가정; [SureSim project](https://suresim-robot-eval.github.io/)·공개 data interface | PPI로 simulator bias를 보정한다. Paired prediction의 연관성과 같은 환경 분포가 필요하다. VLA에 보정항을 추가하는 것도 직접 비교가 필요 |
| S07 | **RACE: Calibrated Cumulative Scoring for Rollout-Free Checkpoint Selection** — [저자 project](https://changyeon.site/race/) | [본문](https://changyeon.site/race/assets/paper.pdf) §3–5, 실제 공개 JSON | 성공 reference의 action deviation·시간 누적으로 checkpoint ranking. 실험은 BC/fine-tuning 계열로 RL 이력의 증거가 아니다. 저자 표기: NeurIPS 2026 Robot Learning Workshop accepted / ICRA 2027 under review; 공식 acceptance 독립 확인 전 |
| S08 | **Scaling Robot Policy Evaluation via Discrete Diffusion World Model** — [ICML 2026](https://proceedings.mlr.press/v306/li26hi.html) | 관련 [dWorldEval v1](https://arxiv.org/html/2604.22152v1) §4.2–4.3; project source | Action controllability와 success-based ranking, 늦은 checkpoint의 성능 하락 추적을 이미 다룸. World model hallucination을 처음 발견했다고 할 수 없다 |
| S09 | **Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation** — [RSS 2026](https://www.roboticsproceedings.org/rss22/p154.html) | [v1](https://arxiv.org/html/2605.11479v1) §IV–V·VI–VIII; dataset loader | Truncation·recovery를 반영하는 state value다. 학습된 행동 데이터의 progress 평가를 arbitrary target-policy checkpoint return estimator로 바꾸어 해석하지 않는다 |
| S10 | **ALOE: Action-Level Off-Policy Evaluation for Vision-Language-Action Model Post-Training** — [arXiv 2026](https://arxiv.org/abs/2602.12691), acceptance 미확인 | [v3](https://arxiv.org/html/2602.12691v3) §3–5.3; project repository | Mixed replay에서 current-policy Q와 action ranking을 다룬다. Action critic의 calibration은 checkpoint 전체의 독립 배포 성능 보장과 다르다 |
| S11 | **World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy** — [arXiv 2026](https://arxiv.org/abs/2602.06508), acceptance 미확인 | [v2](https://arxiv.org/html/2602.06508v2) §3.3·4.5; 공식 repository | RL 중 simulator 오차를 이용하는 사례와 실패 데이터 feedback을 이미 보고한다. “VLA에서도 reward hacking 발생”만으로는 충분하지 않다 |
| S12 | **Scaling Laws for Reward Model Overoptimization** — [ICML 2023](https://proceedings.mlr.press/v202/gao23h.html) | 공식 abstract | Proxy 최적화와 독립 reference의 불일치는 기존 일반 원리. 이 논문의 gold reward도 합성 설정의 모델이므로 물리적 진실과 동일시하지 않는다 |

S08의 proceedings title/author list와 project·arXiv title/author list는 차이가 있다. 이번에는 공식 출판 metadata와 preprint 본문의 근거를 따로 기록했다. 같은 계열이라는 판단으로 registry identity를 합치거나 변경하지 않았다. RACE workshop status 역시 main-conference 검증 수에 넣지 않는다.

## 핵심 합성

**Paper-supported:** S01–S06은 평가의 allocation·comparison·bias correction을 이미 제공한다. S07–S10은 robot/VLA score와 value를 구체화한다. S11–S12는 최적화와 평가의 결합에서 생기는 오차의 위험을 뒷받침한다.

**Researcher interpretation:** C6가 남으려면 위 방법을 VLA에 이식하는 수준을 넘는, 재현 가능한 조건과 그에 대한 설명이 필요하다. 현재의 질문은 이 조건을 특정하지 못했고 공개 자료의 provenance도 부족하다. Importance와 novelty를 분리하면 “필요한 검증 문제”이지만 “지금 착수할 새 방법 논문”은 아니다.

## 제안에서 제거한 우회 주장

- Confidence interval이나 abstention을 추가하면 새로워진다 → STEP/N-SCORE/SureSim 대조 없이는 성립하지 않는다.
- Ranking correlation이 높으면 안전하게 고를 수 있다 → 근소한 top checkpoint 차이·reference의 유한 표본·task mixture를 따로 봐야 한다.
- 여러 robot에서 측정하면 새로워진다 → 범위 확장만으로 기여가 되지 않는다. 먼저 한 native VLA에서 RL 고유의 조건을 확인해야 한다.
- 정적 ranking 오류가 관측되면 reward exploitation이다 → 분포 이동·측정 잡음·모델 부정확성과 구분하는 개입이 필요하다.
- 실패를 발견하지 못하면 비열등성이 증명된다 → 작은 budget의 미결정과 개선/비열등성의 증거를 구분한다.

조사는 전 venue의 exhaustive novelty proof가 아니다. Source의 공개 상태·버전 차이·미검사 payload를 [자료 심사](./DATA_AND_CODE_REVIEW.md)에 명시한다.
