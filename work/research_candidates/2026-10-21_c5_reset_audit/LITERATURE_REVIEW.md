# C5 문헌 대조

- Date: 2026-10-21 KST
- 기준: 2024–2026 frontier와 필수 autonomous/reset-free RL 계보. 최신 여부와 foundation 역할을 분리한다.
- 아래는 candidate bibliography다. Registry 등록·사용자 reading status 승격이 아니다. 정확한 title·URL·확인 범위는 [SOURCE_AUDIT.json](./SOURCE_AUDIT.json)을 따른다.

## 기존 contribution과 C5의 경계

| ID / 논문 | 확인 범위·status | 이미 다룬 것 | C5에 대한 영향 |
|---|---|---|---|
| S01 Leave No Trace | ICLR 2018 accepted manuscript의 abstract/공식 검색 결과. Forum 직접 열기는 challenge | Forward/reset policy를 함께 학습하고 자율성과 안전을 고려 | “forward 실패와 reset 가능성을 함께 보자” 자체는 새롭지 않음 |
| S02 EARL | ICLR 2022 accepted manuscript §4, §6.2–6.3 | Autonomous training과 deployed/continuing evaluation 구분; 방문 분포 분석 | 고정 목표 시작 분포의 별도 평가를 새 contribution으로 주장하지 않음 |
| S03 MEDAL | ICML 2022, §1–3, §5의 평가 정의; 공개 code | Backward policy로 demonstration 상태 분포를 맞춰 학습을 도움 | Physical reset을 통해 학습 분포를 조절한다는 넓은 주장이 충돌 |
| S04 ARIEL | CoRL 2022, PMLR 발행 2023; abstract | Prior offline data로 새 task와 reset을 학습 | 사전학습 데이터를 reset에 활용하는 것만으로 차별화 안 됨 |
| S05 PAINT | NeurIPS 2022; abstract | Irreversible state 감지·회피, 필요한 human intervention 요청 | Rescue 배분을 method로 바꾸려면 직접 본문/구현 대조를 더 해야 함 |
| S06 GEAR | CoRL 2023; abstract/project | Reachability를 고려한 자율 exploration과 비동기 human feedback | “도달 가능한 목표를 고르자”는 일반 원리가 이미 존재 |
| S07 So You Think You Can Scale Up Autonomous Robot Data Collection? | CoRL 2024, PMLR 발행 2025; §3, App. A.3–A.4 | 자율 수집의 환경 설계·reset·human data 비용 한계 | 전체 시간과 human-assisted baseline을 포함해야 함. Autonomous IL 결과를 VLA RL 효과로 바꾸지 않음 |
| S08 AutoEval | CoRL 2025; arXiv v2 §3, App. G–L; 공개 code | Generalist policy의 자동 평가·reset·human assistance; 초기 상태 분포 확인 | 단순 평가 분모 점검은 새 system이 아님. 본문은 arXiv판이며 camera-ready 전체 diff는 미확인 |
| S09 MoReFree | TMLR 2025; 공식 indexed PDF/저자 code, arXiv v3 §3–4; 공개 code | 초기·평가 목표와 exploratory goal을 섞어 task-relevant 학습 | Coverage와 exploration의 균형 자체도 선행 방법. VLA native 실행 구현은 아님 |
| S10 OmniReset | ICLR 2026 proceedings/abstract | Simulator에서 다양한 reset 상태를 생성하여 dexterous RL coverage 확대 | Simulator state 설정을 physical reset 수행의 증거로 쓰지 않음 |
| S11 MiDAS | arXiv 2026, acceptance 미확인; §6·8, App. F–G·I | VLA residual RL의 reset curriculum과 state-shift robustness | “VLA + RL + reset 다양성”은 contribution에서 제외 |

직접 근거: [S01](https://openreview.net/pdf?id=S1vuO-bCW), [S02](https://arxiv.org/pdf/2112.09605), [S03](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf), [S04](https://proceedings.mlr.press/v205/walke23a.html), [S05](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6bf82cc56a5fa0287c438baa8be65a70-Abstract.html), [S06](https://proceedings.mlr.press/v229/balsells23a.html), [S07](https://arxiv.org/html/2411.01813v1), [S08](https://arxiv.org/html/2503.24278v2), [S09](https://arxiv.org/html/2408.09807v3), [S10](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html), [S11](https://arxiv.org/html/2608.11363v1).

## Paper-supported conclusion

1. Autonomous training 후 독립적인 시작 분포에서 정책을 평가하는 틀은 이미 확립돼 있다. EARL §4.1은 이를 continuing performance와 구분하고, MEDAL §5는 별도 evaluation rollout을 learner에 주지 않는다. 두 문제를 구분하는 것 자체는 novelty가 아니다. [EARL](https://arxiv.org/pdf/2112.09605), [MEDAL](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf)
2. AutoEval Algorithm 1은 reset 불능 시 human 도움을 요구한다. App. K는 3개 run의 시작 위치를 비교하고, App. L은 reset 실패 run의 사후 검토를 다룬다. 기존 논문이 reset 분포를 전혀 고려하지 않았다는 전제는 틀리다. [AutoEval](https://arxiv.org/html/2503.24278v2)
3. MiDAS App. F의 확대 reset은 simulator에서 위치 범위를 단계적으로 넓히는 설정이다. App. I의 실제 물체 재배치는 demonstration 주변으로 기술되어 있지만, 이번 확인 구간만으로 모든 reset attempt의 비용·실패 provenance가 공개됐다고 말할 수 없다. [MiDAS](https://arxiv.org/html/2608.11363v1)

## Researcher interpretation

- **학습 coverage 감소 / 평가 selection / 운영 throughput**은 별개의 결과다. 더 쉬운 장면에서 평가했다는 관찰로 정책의 학습 효과가 나빠졌다고 결론 내릴 수 없다.
- Training distribution을 target distribution과 강제로 같게 하는 것도 항상 좋지 않다. Curriculum의 이득과 reset 비용을 함께 비교해야 한다.
- VLA가 실패 후 도달하는 상태가 reset 학습 범위를 벗어나는 사례를 관측하더라도, 일반적인 reset-policy OOD일 수 있다. 단순 reset retraining·quota·human placement와 구별되는 반복 가능한 구조가 있어야 후속 연구 가치가 생긴다.
- 이 검토는 “C5와 완전히 같은 논문은 세상에 없다”는 증명이 아니다. 현재안의 넓은 주장을 새 기여로 채택하기에 선행 충돌이 충분히 강하다는 판단이다.

Baseline 선정 참고인 S01·S04·S05·S06·S10은 abstract 범위다. 이후 이 방법 자체를 구현·비교하게 되면 해당 full method와 공개 interface를 먼저 확인해야 한다. 지금은 baseline을 재현했다고 표시하지 않는다. 이전 FLARE 기반 retry/reset selector나 종료된 로봇 간 전이 프로젝트를 다시 활성화하지 않는다.
