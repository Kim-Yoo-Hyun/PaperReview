# D3 buildup — 비가역 상태 변화 뒤의 지시 수정

> **최신 후속: D3-R1 공개 심사 완료 / 재개 gate NOT_MET.** [추가 결과](./R1_REVIEW.md)에서 raw/annotation 200쌍의 파일 identity를 연결했지만 사건–RGB pair와 조리 후 continuation 능력은 확보하지 못했다. P2 평가에는 hotdog가 없고, 별도 P4는 조리 전 placement 보고다. **연구 REVISE / full-task 실험·학습 HOLD 유지.** [증거 명세](./R1_EVIDENCE_REQUIREMENTS.json)에 맞는 새 자료를 받으면 D3-R2에서 심사한다. 같은 문서 재조사·adapter 구현을 자동 진행하지 않는다. [R1 검증](VALIDATION.md#stage-2), [L1 기록](./TASK_POLICY_AUDIT.md). 아래 1–8은 B1 당시의 역사적 심사이며 다음 행동은 이 후속 판단을 따른다.

- 검토일: 2026-10-22 KST
- 절차: [기존 8단계 buildup](../../../research/IDEA_BUILDUP_GUIDE.md#5-문헌에서-아이디어로-넘어가는-8단계)
- **판정: REVISE — 구체적인 VLA 진단 후보로 비실험 검토를 이어갈 가치가 있다.** 일반적인 interruption·rollback·재계획을 새 방법으로 채택하는 것은 NO-GO다. 새 학습과 native 실험은 HOLD다.
- 완료 범위: 1–6의 문헌·분석·비교 설계, 7의 정적 source/해석적 점검, 8의 내부 투자 판단. 실제 정책 효과와 외부 연구자 피드백은 미완료다.
- 산출물: [문헌·공개 interface 비교](./CLOSEST_WORK.md), [task·주장·기각 계약](./TASK_CONTRACT.md), [source identity](./sources_2026-10-22.json), [유지보수 검증](./VALIDATION.md).

## 0. D2에서 전환한 이유

[D2의 재개 조건](../2026-10-22_d2_buildup/README.md#8-내부-반박과-다음-판단)은 공개 task/executor, 기존 대안과 예측이 갈리는 조건, 공정한 비교다. 추가 확인한 MoManipVLA 제목의 저장소는 `eb987d1…`에서 README와 그림의 두 파일뿐이었다. [공식 project](https://gary3410.github.io/momanipVLA/)의 code 공개 안내와 이 [제목 일치 repo](https://github.com/CyanChew/MomanipVLA/tree/eb987d1b4de40f6215c883bca9b365eca7c54774)를 구분했다. 해당 repo를 공식 실행 구현으로 인정하지 않았다.

코드 부족만으로 D2의 가치를 부정한 것은 아니다. 기존 planner·supervised ranking·foresight 계열과 구별되는 구체적인 예측도 새로 확보하지 못했다. 이번 bounded 점검에서는 D2 HOLD를 유지하고, 사용자의 조건부 지시에 따라 D3로 전환했다. D1과 C1–C6의 기존 판단도 유지한다.

## 1. 해결되면 달라질 일

**VLA가 물체를 익히거나 자른 뒤 지시를 수정받았을 때, 이미 바뀐 물체 상태를 인정하고 가능한 새 목표로 전환하며, 불가능해진 요구는 추가 손상 없이 구분할 수 있는가?** 로봇의 팔을 이전 자세로 옮기는 것과 세계의 상태를 복원하는 것은 다르다. 그런데 기존 목표의 성공 여부만 측정하면 불가능한 요구를 계속 시도하는 행동과, 가능한 요구까지 모두 거부하는 행동을 구별하기 어렵다.

첫 범위는 단일 로봇의 manipulation이다. 다양한 로봇으로 확장할 수 있는 평가 개념이지만 cross-embodiment 전이 효과를 주장하지 않는다. RL도 전제가 아니다. 실제 VLA에서 이 문제가 얼마나 자주 생기고, 기존 계층형 정책이 얼마나 잘 처리하는지는 미측정이다.

## 2. 판단에 필요한 문헌 집합

| 역할 | 핵심 문헌 | 이 검토에서 묻는 것 |
|---|---|---|
| 직접 task switching | SwitchVLA | contact phase와 역방향 action이 물체의 상태 변화까지 다루는가 |
| 강한 언어 피드백 대안 | Hi Robot, VoLo | 관측 기반 지시 수정·중단·재계획만으로 충분한가 |
| safety·rollback | SafeLoop | 위험 회피와 이미 발생한 사건 이후 목표 가능성은 어떻게 다른가 |
| 반대 설명 | RePlan-Bot, RSA | 전제조건을 보완하는 재계획 또는 비가역 상태 회피로 설명되는가 |
| task·평가 | BEHAVIOR-1K, OopsieVerse | 실제 상태 전이가 있는가, 단지 damage score만 감소하는가 |

ICML 2025·NeurIPS 2025·RSS 2026 공식 출처를 확인했다. RePlan-Bot은 **CVPR Workshops**다. SafeLoop의 IROS 2026과 VoLo의 CoRL 2026 표기는 저자 발표와 공식 venue 검증을 분리했다. 2024–2026의 관련 연구를 탐색하되 BEHAVIOR-1K의 2022 foundation과 최신 공개 source를 함께 사용했다. 전수조사나 독창성 보증은 아니다. 8편 중 기존 registry 4편을 재사용했고 외부 4편은 dossier에만 기록했다.

## 3. 가정과 interface에서 확인한 것

- SwitchVLA의 rollback 학습은 과거 joint-action sequence의 역방향 사용이다. 이를 물체의 익힘·절단을 복원하는 기능으로 해석할 수 없다. 다만 해당 논문이 D3 task에서 실패했다는 실험 증거도 없다. [§3.4](https://arxiv.org/html/2506.03574v1).
- Hi Robot은 사용자 개입 시 상위 VLM을 다시 호출하며 관측에 맞는 명령·언어 응답을 생성한다. 따라서 ‘변경된 지시에 응답한다’는 broad contribution은 이미 존재한다. [§4.1–4.2](https://arxiv.org/html/2502.19417v1).
- SafeLoop는 비가역 변화를 되돌릴 수 없다는 한계를 본문에서 인정한다. 공개 실행 코드에는 **kinematic qpos 수정·PD 실행·선택적 state restore**가 공존한다. D3에서는 이들을 동일한 물리적 rollback으로 묶지 않는다. [본문 §III-C](https://arxiv.org/html/2609.26313v1), [executor source](https://github.com/Loule0-0/SafeLoop/blob/3980d6dd3ec324b974d5f9c7d65a9b5115f4a7ba/safety_guard/libero_motion.py#L297).
- BEHAVIOR의 Cooked는 최고 온도의 이력에 의존한다. 정상 물리 update에서는 최고 온도가 감소하지 않지만 관리자 setter/reset으로는 바꿀 수 있다. **허용된 로봇 행동에 상대적인 비가역성**으로 정의해야 한다. [Cooked](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/object_states/cooked.py), [MaxTemperature](https://github.com/StanfordVL/BEHAVIOR-1K/blob/7d6718cb8ac5f249bb3c610c23713627d97da1ef/OmniGibson/omnigibson/object_states/max_temperature.py).

## 4. 남길 질문과 경쟁 설명

**같은 관측·이력·행동·시간 예산에서, VLA 시스템은 비가역 사건 이후의 ‘가능한 새 목표’와 ‘불가능한 새 목표’를 구분하는가? 상태 predicate를 사용하는 단순 재계획 이후에도 설명되지 않는 행동 차이가 남는가?**

| 가설 | 구별할 관찰 / 분석 | 경쟁 설명 |
|---|---|---|
| H0: 지시 전달 또는 stale chunk 문제다 | 동일 queue flush·latency를 적용하면 차이가 사라짐 | 언어 갱신·controller timing만 고치면 됨 |
| H1: 현재 물체 상태를 잘못 추정한다 | 같은 planner에서 추정 predicate와 oracle predicate의 판단이 갈림 | perception·event memory 문제 |
| H2: 상태는 알지만 새 목표의 가능성을 잘못 판단한다 | 같은 predicate에서 goal check 유무에 따라 선택이 갈림 | symbolic precondition/reachability check로 충분 |
| H3: 가능성 판단은 맞지만 실행을 전환하지 못한다 | goal과 witness가 있으나 native VLA가 continuation에 실패 | competence·훈련 분포·실행 지연 문제 |

이는 경쟁 가설이며 어느 것도 확인된 VLA 현상이 아니다. H2가 남는다고 즉시 RL을 도입하지 않는다. 전체 상태가 충분한 Markov state이면 과거 이력 자체가 별도의 정보를 추가하지 않는다는 점도 계약에 반영했다.

## 5. 신규성 심사

| 주장 후보 | 판단 |
|---|---|
| VLA가 지시 변경에 반응한다 | Hi Robot·SwitchVLA와 직접 충돌 |
| 위험을 감지해 rollback하고 다시 계획한다 | SafeLoop·VoLo 및 기존 재계획과 직접 충돌 |
| 비가역 상태를 피하도록 RL한다 | RSA 등과 인접/직접 충돌. D3의 별도 기여로 채택하지 않음 |
| 사건 전후 목표 가능성·관측·실행을 분리하면 기존 task-switching 평가의 결론이 달라진다 | **검증할 가치가 있는 잠정 진단 질문**. 현상 크기·일반성·기존 benchmark와의 추가 차별성은 미확보 |

‘이 문제를 다룬 논문을 찾지 못했다’는 이유로 신규성을 확정하지 않는다. 이미 익은 물체를 다시 생것으로 만들 수 없다는 사실도 새로운 결과가 아니다. 논문으로 발전하려면 기존 VLA/계층형 정책에 대해 **어떤 정보와 비교 조건이 행동 평가의 결론을 바꾸는지** 보여야 한다.

## 6. 주장–증거 계약

[TASK_CONTRACT](./TASK_CONTRACT.md)에 다음을 고정했다.

1. 로봇 자세·물체 상태·목표 도달 가능성을 분리하고 동일 물체 identity를 유지한다.
2. Cooked 전후의 지시 수정, 가역적인 위치 이동, 수정 없는 원래 작업을 각각 비교한다. 실제 reachable witness가 없는 사례는 ‘가능’ 정답으로 확정하지 않는다.
3. 고정 VLA, 동일 지시 갱신/queue flush, 강한 관측 기반 VLM planner, 추정 predicate + 단순 planner, oracle 진단을 비교한다.
4. 가능한 목표의 완료율, 불가능한 목표에 대한 근거 있는 중단, 가능 목표의 오거부, 추가 손상·시간을 분리한다. 모두 거부하는 baseline도 둔다.
5. 단순 planner가 충분하면 새 learned method를 중단한다. 관측 불가능·native competence 부재·정보 누출이면 먼저 task/평가를 수정한다.

이 문서는 설계 계약이다. Scene instance, asset parameter, checkpoint, seed, time budget, sample size와 실행 manifest는 아직 확정하지 않았다.

## 7. 가장 약한 연결의 비실험 점검

**Task의 실체는 확인했다.** `cook_hot_dogs/problem0.bddl`에는 조리 전 hotdog와 조리 완료 goal이 있다. `slicing_vegetables/problem0.bddl`은 원래 물체가 사라지고 diced 물질이 생성되는 goal을 사용한다. 후자는 transition-rule source와 연결되지만 identity·particle goal의 복잡성이 있어 2차 후보로 둔다. 새 지시·switch wrapper는 우리가 제안한 평가 확장이며 기존 benchmark가 제공하는 실험으로 표시하지 않는다.

**Damage score와 물리적 변화를 구분했다.** OopsieVerse의 health 감소는 유용한 독립 평가 신호지만, 감사한 health update만으로 fracture topology나 새 goal의 불가능성을 입증하지 못한다. 따라서 primary는 상태 전이가 있는 BEHAVIOR task, OopsieVerse는 보조 metric 후보로 둔다.

**실행 baseline은 아직 자격 미충족이다.** 공식 BEHAVIOR baseline 문서가 연결하는 π0/OpenVLA-OFT recipe를 확인했다. 감사한 π0 문서의 공개 checkpoint는 radio/trash task용이며 cooking/cutting competence를 보장하지 않는다. 레시피가 있다는 사실을 D3용 native policy 확보로 해석하지 않는다. [공식 baseline recipe](https://github.com/StanfordVL/b1k-baselines/blob/59cee351ea84733b04629cf5879ac5b1d538c04f/tutorials/openpi.md).

총 23개 공개 text 파일의 revision/hash를 확인했다. Source를 import하거나 실행하지 않았다. 가시성·반응 시간·실제 전이 발생·정책 성공률은 미측정이다.

## 8. 내부 반박과 투자 판단

| 내부 반박 | 현재 답과 판단 |
|---|---|
| “그냥 상태 기반 재계획 아닌가?” | 맞을 수 있다. 이것을 가장 강한 단순 baseline으로 두며, 충분하면 방법 주장은 종료한다. |
| “불가능한 명령을 일부러 주는 trivia인가?” | 가능한 수정·불가능한 수정·가역 control을 함께 비교하고 실제 행동/추가 손상까지 달라져야 연구 가치가 있다. |
| “멈추기만 하면 되는가?” | 가능 목표의 오거부를 측정한다. 열원이 작동 중이면 팔의 정지는 열 발생의 정지가 아니므로 별도 mitigation 행동도 필요하다. |
| “왜 VLA/RL이어야 하는가?” | VLA executor의 상태별 continuation 차이는 질문이 될 수 있으나 현재 필수성은 없다. RL은 단순 planner·supervised 대안 이후 순차 효과가 남을 때만 검토한다. |
| “지금 본격 연구로 추천할 수 있는가?” | **좁힌 진단 후보의 추가 buildup은 추천한다. 새 학습 투자나 top-tier 논문 가능성 확정은 추천하지 않는다.** |

다음은 **D3-L1: cooking task의 native policy·공개 demonstration coverage·관측 cue·goal 변경 평가 경로를 정적으로 연결하는 작업**이다. 구체적인 source 근거를 확인하는 일이므로 GPU 없이 가능하다. 한 task family를 먼저 자격화하고, 충족되지 않으면 대규모 이식/학습 없이 HOLD로 전환한다. [TODO](../../../TODO.md)에 범위와 완료 조건을 남겼다.

실제 외부 피드백은 받지 않았다. 문헌/interface는 `READING-SUPPORTED`, D3 정책 현상·효과는 `CURATION-HYPOTHESIS`다. Native episode·실험·패키지 설치·모델/데이터/PDF 저장은 없고 registry tier·사용자 reading status도 변경하지 않았다.
