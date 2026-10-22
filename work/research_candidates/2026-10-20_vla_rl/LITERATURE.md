# 새 후보의 문헌·충돌 근거

- 확인일: 2026-10-21 KST
- [판단과 우선순위](./README.md) · [후보의 검증 설계](./CANDIDATES.md)
- 아래 ID는 이번 검토용 reference다. Registry의 `paper_id`나 신규 등록을 뜻하지 않는다.
- `본문 일부 확인`은 관련 section을 확인했다는 뜻이다. 사용자 정독 tracker를 승격하지 않았다. arXiv 본문과 최종 proceedings의 모든 개정 차이를 대조한 것은 아니다.

## C1: 관측의 가치와 조작으로의 전환

| ID / 논문 / 검증 status | 확인 범위와 paper-supported 내용 | 후보에 주는 제약 |
|---|---|---|
| **P1. Real-World Reinforcement Learning of Active Perception Behaviors (AAWR)** — **NeurIPS 2025 main conference** | [공식 proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html), [본문 §3–4, App. F.2/F.4/F.5/F.7–F.9](https://arxiv.org/html/2512.01188), [code](https://github.com/penn-pal-lab/aawr). Privileged critic로 partial-observation policy를 advantage-weighted regression 학습. VLA search experiment는 detector의 연속 검출 후 π0로 전환하며 search·completion·steps와 시간 정규화도 평가한다. | 능동 탐색 RL, VLA handoff, 비용 평가 자체는 신규성이 아니다. Search reward와 handoff rule을 downstream task value와 대조해야 한다. |
| **P2. SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics** — **CVPR 2026** | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html), [본문 method, App. C.2/C.3/D](https://arxiv.org/html/2603.12193), [project](https://lmzpai.github.io/SaPaVe/). Camera/manipulation action 분리, geometry-aware execution, active manipulation. 데이터 생성에도 residual RL을 사용한다. | “camera와 arm 분리 + RL”이나 “occluder를 치운다”는 새 기여가 아니다. Pure IL-only 선행 연구로 소개하면 부정확하다. 공개 실행 code의 완전성은 이번에 검증하지 않았다. |
| **P3. ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation** — **CVPR 2026** | [공식 paper의 abstract/introduction](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.pdf). Critical region, view selection, 3D zoom-in을 다룬다. 세부 code·전체 ablation은 이번 검토 범위 밖. | Task-aware view selection이나 3D refinement 일반론은 선점되어 있다. |
| **P4. Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE)** — **CVPR 2026**, preprint 2025 | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Bai_Learning_to_See_and_Act_Task-Aware_Virtual_View_Exploration_for_CVPR_2026_paper.html), [본문 §3 및 pseudo-environment 부록](https://arxiv.org/html/2508.05186), [project](https://hcplab-sysu.github.io/TAVP/), [code](https://github.com/HCPLab-SYSU/TAVP). RGB-D로 얻은 point cloud를 virtual view로 재렌더링. PPO reward에 reference 대비 action loss 차이, entropy, view diversity를 쓴다. | “RL로 조작에 유용한 시점을 선택”도 기존 기여다. 이미 관측한 point cloud의 재렌더링과 새로운 물리 관측 획득의 차이를 분리해야 한다. |
| **P5. APPLE: Toward General Active Perception via Reinforcement Learning** — **ICLR 2026** | [공식 proceedings의 abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9e8c2895db691eaab85af37bddee75aa-Abstract-Conference.html). Perception과 decision module의 joint RL, tactile exploration 등의 평가. | “perception과 action을 함께 RL 학습”을 신규성으로 쓰지 않는다. VLA handoff의 동일 문제를 풀었다는 근거도 아니다. |
| **P6. ActiveScale: Scaling Active Perception for Robots across Model, Data, and Hardware** — **arXiv 2026, venue 미검증** | [본문 method/evaluation](https://arxiv.org/html/2609.18514), [project](https://active-scale.github.io/). History와 camera-pose supervision, human–robot mid-training, 별도 camera arm을 갖는 mobile manipulation. | Joint camera/manipulation policy나 historical views 추가만으로 차별화하지 않는다. 새 hardware/data 규모가 필요해지는 설계는 첫 후보의 자원 범위 밖. |

**P1의 지표를 잘못 읽지 않기:** Bookshelf-P의 `Search 92.4`는 finding·approaching·fixating의 **3단계 rubric 평균**이다. 독립적인 binary search 성공률이 아니다. 같은 표의 `Completion 44.4%`는 handoff 뒤 π0 grasp 성공이며 두 숫자를 빼서 실패 확률로 계산하면 안 된다. 두 지표의 차이는 proxy 검토의 동기일 뿐 handoff 개선 여지가 입증되었다는 뜻이 아니다. Complex 조건은 suboptimal/expert 데이터 결과도 구분해야 한다. [P1 App. F.2/F.7/F.8](https://arxiv.org/html/2512.01188).

**연구자 해석:** 비용과 action loss를 고려하는 기존 연구가 있으므로 C1의 공백을 “비용을 처음 고려”로 정의하지 않는다. 관측 개선, 조작 자세 변화, detector 오차, downstream competence를 분리한 조건에서 **task-outcome 기반의 sequential handoff 선택이 필요한지**가 남은 확인 사항이다. 정보 수집 행동의 가치 자체는 오래된 interactive perception 관점이다. [Bohg et al., 저자 survey](https://arxiv.org/abs/1604.03670).

### C1 우선 진행 후 추가 확인

[C1_REVIEW.md](./C1_REVIEW.md)에 **ActiveAlign, EyeRobot 2.0, EgoReveal, PhysCaP**의 관련 본문 확인 범위·직접 링크·status·비교 조건을 기록했다. 네 편은 모두 venue 미검증 preprint로 취급한다. 관측–정책 불일치, gaze sequence RL, visibility-convergence handoff, 비용을 고려한 탐색 종료까지 선행 연구가 있어 초기 C1을 새 방법으로 바로 구현할 근거는 약해졌다. 문헌별 상세 비교를 이곳에 중복 유지하지 않는다.

## C2: What과 How를 구분한 post-training

| ID / 논문 / 검증 status | 확인 범위와 paper-supported 내용 | 후보에 주는 제약 |
|---|---|---|
| **L1. LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries** — **ICML 2026** | [PMLR](https://proceedings.mlr.press/v306/lian26d.html), [본문 §3–4](https://arxiv.org/html/2601.15197), [code](https://github.com/ZGC-EmbodyAI/LangForce). Dual branch·language LLR·action loss·posterior inference를 본문과 정적 구현으로 대조. | Language-sensitive objective 자체는 신규성이 아니다. C2 matched comparison과 외부 모델 비교를 구분한다. |
| **L2. Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models** — **arXiv; ACL ARR 2026 October submission, 채택 아님** | [본문 §3–6, App. B/C](https://arxiv.org/html/2610.21251), [공식 submission](https://openreview.net/forum?id=PM8XCMAwjI), [code](https://github.com/sangwu99/how-level-vla-Arxiv). Evaluator·client·denominator까지 추가 확인. | How-level 진단·segment enrichment는 선행 기여다. Path의 instruction 변경과 물리 환경 변경을 분리해야 한다. |
| **L3. CounterAlign: Counterfactual Supervision for Vision-Language-Action Models** — **CoRL 2026 Poster** | [공식 forum](https://openreview.net/forum?id=AY4totylcx), [본문 §3–4 및 부록](https://arxiv.org/html/2608.21740), [저자 project](https://counteralign.airoa.io/). 공식 API로 status 재검증. Project는 code Coming Soon으로 표시. | Instruction alignment reward·nnPU·offline RL은 직접 충돌이다. 기존 `venue 미검증 / code 미식별` 판단을 갱신했다. |
| **L4. Stable Language Guidance for Vision–Language–Action Models** — **ACL 2026 main conference** | [공식 본문 §3–4](https://aclanthology.org/2026.acl-long.190.pdf), [code](https://github.com/Doo-mon/RSS). Instruction expansion과 conditional/unconditional steering; 공개 flow guidance도 확인. | Paraphrase robustness·language steering 자체를 새 기여로 사용하지 않는다. Native 구현 및 비용을 맞춘 비교가 필요하다. |
| **L5. VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models** — **arXiv 2026, venue 미검증** | [저자 abstract](https://arxiv.org/abs/2607.04517). Frozen VLA 앞의 language-command policy를 sparse task reward로 RL 학습한다. | Prompt rewriter RL은 별도 새 후보로 채택하지 않는다. |
| **L6. SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning** — **NeurIPS 2025** | [공식 proceedings의 abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html), [project](https://pku-safevla.github.io/). Safety-CHORES와 constrained SafeRL을 제공한다. | C2는 일반 safety penalty 또는 CMDP를 새 알고리즘이라고 주장할 수 없다. Language-specific controllability와 조합 일반화가 필요하다. |
| **L7. ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation** — **arXiv v2; ICLR 2027 submission, 채택 아님** | [본문 §3–4, App. A](https://arxiv.org/html/2603.17524v2), [공식 submission](https://openreview.net/forum?id=BCw1oqG73w). KineVLA와 동일 arXiv identity. | 고정 goal과 execution constraint 분리 자체에 직접 충돌. 독립된 두 논문으로 세지 않는다. |
| **L8. Diagnosing Compositional Generalization in Sequential Robot Tasks** — **CoRL 2026 Spotlight** | [공식 forum](https://openreview.net/forum?id=gQFYIM5dJy), [본문 §3–5, App. B](https://arxiv.org/html/2607.29687), [code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot). Dependency coverage와 sparse instruction composition을 분석. | Pair coverage의 중요성도 선행 연구다. 최신 공개 release와 논문의 평가 계약 차이를 구분한다. |
| **L9. RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents** — **CoRL 2026 Poster** | [공식 forum](https://openreview.net/forum?id=A9AQjk3dAt), [본문 §3–4, App. B](https://arxiv.org/html/2609.25636), [code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). Scene 3의 실제 task와 semantic rewrite·trajectory evaluator를 확인. | 같은 scene의 실행 제약·intent/execution 진단은 새 기여가 아니다. C2 triple holdout을 별도로 명시해야 한다. |

**L2의 진단을 그대로 재현하는 것도 새 기여는 아니다.** SIMPLER-IN의 Path는 보이지 않는 collision panel을 사용한다. 이를 일반 환경의 자연스러운 지시 이해로 바로 일반화하지 않는다. Grasp/Place의 조건도 evaluator와 base policy가 실제로 처리하는 범위를 분리해야 한다. [L2 App. C.1](https://arxiv.org/html/2610.21251).

**2026-10-21 최종 후속 판단:** [실제 데이터·Docker 검사](../../experiments/vla_rl_c2_first_pass/RESULTS.md) 후 현재 C2 설계의 1차 검증을 **NO-GO로 종료**했다. 부분 경유 supervision은 있지만 완전한 reward/coverage와 reference runtime이 미충족이며, 현재 방법 기여로서의 투자는 추천하지 않는다. [빌드업 결과](./C2_BUILDUP_RESULT.md). 문헌 claim·scope는 [C2_REVIEW.md](./C2_REVIEW.md)에 보존한다. CoRL/under-review status는 [공식 API 기록](./C2_SOURCE_AUDIT.json)으로 검증했으며 사용자 reading status는 올리지 않았다.

## 재선정하지 않은 인접 방향

| 문헌 | 확인한 범위 | 판단 |
|---|---|---|
| **RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors** — arXiv 2026 | [본문 Introduction/Related Work 및 decision-value formulation](https://arxiv.org/html/2610.13516) | State–intervention pair, remaining budget, false alarm과 reset cost까지 다룬다. 기존 RP-2를 reset cost라는 이름으로 다시 제안하지 않는다. |
| **Simple Recipe Works: Vision-Language-Action Models are Natural Continual Learners with Reinforcement Learning** — arXiv 2026, v3 | [본문 §3–4의 설정과 비교](https://arxiv.org/html/2603.11653) | Sequential LoRA/on-policy RL이 강한 조건이 있다. 모든 VLA가 안 잊는다는 보편 명제도 아니고, 단순 forgetting 방지를 새 gap으로 주장할 근거도 아니다. |
| **What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models (PAIR-VLA)** — arXiv 2026 | [abstract](https://arxiv.org/abs/2605.13105) | Task-preserving/altering visual pair와 행동 수준 regularization이 존재. “무관한 변화에 둔감하고 중요한 변화에 민감”이라는 일반 주장은 제외한다. |
| **How (and How Not) to Use Data Augmentation in VLA Post-Training** — arXiv 2026-10 | [abstract](https://arxiv.org/abs/2610.05994) | Critic/actor augmentation 분리의 직접 선행 연구. 간단한 augmentation 적용만 새 주제로 채택하지 않는다. |

## 공개 코드에서 확인한 실행 interface

아래 표는 최초 선별에서 웹으로 읽은 파일의 정적 확인이다. Revision은 2026-10-20 `git ls-remote`로 확인했다. 이후 C1에서 선택한 LeRobot·HF LIBERO·SmolVLA의 정적 확인은 [source audit](./C1_SOURCE_AUDIT.json), Docker 실행 범위는 [probe 기록](../../experiments/vla_rl_active_handoff/README.md)으로 구분한다.

| Repository / revision | 확인 파일 | 확인한 계약과 한계 |
|---|---|---|
| AAWR / `05845db6c0da25993e816c44f47c123487f20cd1` | [src/algorithm/asym_awr.py](https://github.com/penn-pal-lab/aawr/blob/05845db6c0da25993e816c44f47c123487f20cd1/src/algorithm/asym_awr.py), README | 해당 algorithm 파일에서 critic/value는 `obs['state']`, actor는 `obs['rgb']`; expectile value와 AWR extraction. 이것이 논문의 전체 Franka search stack과 같은 interface라고 가정하지 않는다. README의 toy xArm lifting 예시만으로 π0 handoff를 바로 실행할 수 있다고 할 수 없다. |
| How-Level VLA / `478fad54689126e4303bdc6bcb3c8e064e5934ab` | Evaluator·일반/π0 client·요약기·launcher | [C2 감사](./C2_DATA_AUDIT.md)로 갱신. 일반 client 경계의 image/instruction 입력은 확인; π0 downstream 전체 정보 흐름은 미검증. |
| LangForce / `ff35aab1c9c6a02b4daf73c71248350f30d22048` | README·`LangForce.py`의 LLR/forward/predict | Objective 정적 확인 완료. Checkpoint 호환성·현재 Docker runtime은 미검증. [C2 source audit](./C2_SOURCE_AUDIT.json) 참조. |
| TVVE | [repository README](https://github.com/HCPLab-SYSU/TAVP) | Stage별 학습·평가 및 checkpoint 경로 안내가 있다. 이번에 revision 고정·reward 구현 교차검증·물리 camera interface 재현은 하지 않았다. |

## 검색 경계

사용한 주요 검색 묶음은 `VLA RL active perception / handoff / task value`, `instruction following / reward / how-level / counterfactual`, `continual learning / forgetting`, `reset-free / recoverability / intervention cost`, `safety / constrained learning`이다. 저자 related work를 따라 TVVE·SaPaVe·LangForce·CounterAlign·SIMPLER-IN 등의 직접 충돌을 추가했다.

공식 NeurIPS·CVF·PMLR·ICLR·ACL 페이지로 확인한 status만 학회로 표기했다. 최신 preprint는 novelty screening에 포함하되 top-tier 채택 논문으로 세지 않았다. 일반 웹 검색은 후보 발견용이고 이 문서의 사실 근거는 위 1차 출처다. 검색 무결과는 연구 부재의 증거가 아니다. 이번 선별에서 공식 학회 논문과 최신 충돌을 확보했으나, 모든 2026 하반기 발표와 code release의 exhaustive audit를 마쳤다는 뜻은 아니다.
