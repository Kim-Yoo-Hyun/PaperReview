# D3 — 직접 문헌과 공개 interface

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다. VoLo의 CoRL 2026 Poster도 추가 확인했다.

- 확인일: 2026-10-22 KST. Registry 4편 + 외부 비교 4편. 신규 등록·정독 상태 승격은 수행하지 않았다.
- ‘본문 확인’은 아래 관련 절을 읽었다는 뜻이며 전체 논문·부록·모든 code를 정독/재현했다는 뜻이 아니다.
- 판단의 경계: [결과](./README.md), [source identity](./sources_2026-10-22.json). 2024–2026 중심 탐색이며 전수조사가 아니다.

## 1. 정확한 identity와 읽은 범위

| ID / 등록 | Title / year / status | 직접 근거와 확인 범위 | 역할·D3와의 관계 |
|---|---|---|---|
| D3-P01 / pr-0985 | **SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models** / 2025 / arXiv, 공식 venue 미확인 | [2506.03574v1](https://arxiv.org/html/2506.03574v1), §3.4·4.1·limitations; [project](https://switchvla.github.io/). 공식 task-switching 구현 release는 이번 탐색에서 식별하지 못함 | 직접 충돌. contact phase 기반 forward/rollback/advance; 역방향 joint action과 세계 상태 복원은 별개. 물질 상태 변화 후 feasible/infeasible goal 대조를 확인하지 못했으며 실패를 입증한 것은 아님 |
| D3-P02 / pr-0142 | **Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models** / 2025 / **ICML** | [PMLR 공식 출판](https://proceedings.mlr.press/v267/shi25d.html), [원문 v1 §4.1–4.2·학습 개요](https://arxiv.org/html/2502.19417v1), [project](https://www.pi.website/research/hirobot). 해당 system의 공개 training/runtime 구현은 미감사 | 직접 강한 대안. 상위 VLM의 시각·언어 해석과 하위 π0, 사용자 개입에 따른 명령/언어 응답. 단순 instruction rewriting baseline보다 강하게 비교해야 함 |
| D3-P03 / 외부 | **SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation** / 2026 / arXiv; **IROS 2026 accepted는 저자 보고, 공식 program 미검증** | [arXiv metadata](https://arxiv.org/abs/2609.26313), [v1 §III–IV](https://arxiv.org/html/2609.26313v1); [공개 release source](https://github.com/Loule0-0/SafeLoop/tree/3980d6dd3ec324b974d5f9c7d65a9b5115f4a7ba). README, memory/controller/executor/eval entrypoint 확인 | 직접 safety/rollback 대안. Frozen VLA 위 risk predictor, BC warm-start/PPO decider, noop/record/rollback. Training critic의 privileged 정보와 actor 입력을 구분. 본문도 irreversible change 복원 한계를 인정 |
| D3-P04 / 외부 | **VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation** / 2026 / arXiv; **CoRL 2026은 저자 project 표기, 공식 acceptance 미검증** | [v1 §4·API/평가 개요](https://arxiv.org/html/2606.07723v1), [project](https://chicychen.github.io/VoLo/), [VoLoAgent](https://github.com/NVlabs/VoLoAgent/tree/b4e623079ca8498a16bcd5016920d71f76c44d30), [RoboLab adapter](https://github.com/NVlabs/RoboLab/blob/b6cfcf6ccd2113c4cd1216d35b33024a7d5691da/policies/volo/README.md). README/adapter 문서, proxy text 탐색; 전체 control 경로 감사 아님 | 직접 orchestration 대안. VLA 외 perception/grasp/place tools, monitor–halt–redirect. 추가 tool·depth·GT를 섞으면 동일 VLA의 representation 비교가 아님 |
| D3-P05 / pr-0970 | **OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation** / 2026 / **RSS** | [RSS 공식 proceedings](https://roboticsproceedings.org/rss22/p098.html), [v1 §III](https://arxiv.org/html/2606.31993v1), [health/env source](https://github.com/UT-Austin-RobIn/oopsieverse/tree/a739f99e94f32c3229ae6932299e2e0e8c065480/damagesim/core). 모든 benchmark task와 native VLA 실행은 미감사 | 평가 신호. 누적 damage와 goal completion을 분리하는 근거. Health 감소만으로 비가역 geometry transition을 추정하지 않음 |
| D3-P06 / 외부 | **Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments** / 2025 / **NeurIPS main** | [공식 proceedings/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html), [원문](https://openreview.net/pdf?id=dAAz7afWJR). Abstract/introduction 범위, 세부 objective/code 미감사 | 반대 설명·인접 RL. Forward/reset 학습에서 curriculum·행동 기반 irreversible state 회피. 사용자 지시 변경의 VLA 평가를 해결했다고 일반화하지 않음. C5 reset 연구를 재개하지 않음 |
| D3-P07 / 외부 | **RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following** / 2026 / **CVPR Workshops, GRAIL-V** | [CVF 공식 workshop 출판](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html), [v1 §3.1·4.5·limitations](https://arxiv.org/html/2605.25851v1). 공식 구현 미감사 | 상태 기반 계획의 강한 반대 설명. ALFRED의 전제조건·검색·action 보정. §4.5 tabletop 예시는 privileged low-level policy를 공유하므로 native VLA switching 증거로 보지 않음 |
| D3-P08 / pr-0730 | **BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation** / 2022 / **CoRL** | [공식 project/docs](https://behavior.stanford.edu/), [현재 source commit](https://github.com/StanfordVL/BEHAVIOR-1K/tree/7d6718cb8ac5f249bb3c610c23713627d97da1ef), [2025 challenge](https://behavior.stanford.edu/challenge/archive/2025/index.html). BDDL 2개, Cooked/Burnt/MaxTemperature/열 전달/transition source, baseline 안내 확인 | Foundation + task 자산. 2022 논문과 2026 현재 source를 같은 구현 version으로 취급하지 않음. BDDL과 simulator state가 D3의 구체적 평가 후보를 제공 |

## 2. 비교를 바꾸는 interface 경계

| 방법 | 관측·state | 결정·행동 | 공정 비교에서 유지할 것 |
|---|---|---|---|
| SwitchVLA | 이미지·기존/변경 지시·contact 추정 | chunk 단위 action과 forward/rollback/advance | base competence, 동일 변경 시점·chunk 취소; contact label을 사건/goal 정답으로 대체하지 않음 |
| Hi Robot | 상위: 이미지·사용자 상호작용; 하위: 이미지·명령·proprio | 주기적/개입 시 상위 갱신, atomic command와 언어 응답 | 같은 low-level executor·언어 입력·추론/대기 예산; 원 system 미재현이면 ‘Hi Robot-style’로 표시 |
| SafeLoop | predicted risk·joint history; 학습 critic은 추가 GT | 위험 예측에 따른 waypoint 저장/후퇴 | world restore 금지, 정상 actuator 실행, rollback 동안 물리 시간과 추가 손상 포함 |
| VoLo | 이미지·memory, tool별 depth/calibration; GT monitor 경로도 존재 | 비동기 tool 중단·다른 tool 또는 계획으로 전환 | action/tool menu 동일화, GT와 deployable 분리. Tool-chain이 VLA 없이 동작하는 경로를 VLA 개선으로 보고하지 않음 |
| Predicate planner | 같은 observation에서 추정한 사건 상태·object identity·새 goal | 전제조건 검사 후 재계획/mitigation/report | 상태 추정 비용과 planner의 사전 지식 공개. Oracle predicate는 별도 진단이며 learned policy의 공정 baseline으로 혼합하지 않음 |

SafeLoop source의 `motion_execution_mode`와 eval CLI 기본값은 `kinematic`이다. 해당 경로는 qpos/qvel을 직접 바꾸고 `sim.forward()`를 호출한다. `pd` 경로와 state-restore fallback은 별도다. 따라서 **source에 physical control 경로가 있다는 사실도, kinematic default가 있다는 사실도 논문의 모든 reported rollout 설정을 확정하지 않는다**. 본 검토는 수치 재현/오류 판정이 아니다. D3 baseline 자격 심사에서 mode·flag·시간 계측을 반드시 고정해야 한다. [executor L267–390](https://github.com/Loule0-0/SafeLoop/blob/3980d6dd3ec324b974d5f9c7d65a9b5115f4a7ba/safety_guard/libero_motion.py#L267), [eval entrypoint L167](https://github.com/Loule0-0/SafeLoop/blob/3980d6dd3ec324b974d5f9c7d65a9b5115f4a7ba/scripts/evaluate_pi0_safeguard_closed_loop.py#L167).

VoLo 공개 안내는 depth 기반 grasp/place와 GT failure-monitor 옵션을 구분한다. 이를 제거했을 때 같은 system 성능이 유지된다는 증거는 없다. 같은 입력에서 비교할 수 없다면 full-system 결과와 통제된 component 비교를 별도로 보고해야 한다. [VoLoAgent README](https://github.com/NVlabs/VoLoAgent/blob/b4e623079ca8498a16bcd5016920d71f76c44d30/README.md).

## 3. 현재 탐색으로 말할 수 있는 범위

- 일반적인 feedback·interruption·rollback·replanning은 신규성이 아니다.
- 감사한 source에는 joint pose와 material/event state의 구분을 강제할 task 의미가 있다. 이것은 **평가 후보의 근거**다.
- 지시 수정 전후 도달 가능성을 통제한 VLA 비교가 기존 결과를 바꾸는지, 이 후보가 충분한 독창성을 갖는지는 아직 모른다.
- 새 학습 전에는 누락된 직접 연구와 최신 version/release를 다시 확인한다. 코드 미확보를 기존 방법이 약하다는 근거로 쓰지 않는다.
