# C4 buildup 결과: 정책 개선을 위한 선택적 보상 검수

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- Updated: 2026-10-21 KST
- 요청: C4 buildup. 문헌 → 공개 구현 → 실제 데이터 메타데이터 → 반증 설계 → 채택 판단 순서로 진행했다.
- **판정: 현재의 새 acquisition algorithm 주장은 NO-GO. VLA에서 기존 검수법의 유효 조건을 비교하는 진단 연구는 보류한다.**
- 완료 범위: 문헌·구현·데이터 전제에 대한 1차 채택 심사. VLA 추론, reward 추론, RL 학습, robot rollout은 이번에 실행하지 않았다.
- 후속 사용자 요청: 재개 근거가 없어 이 보류를 유지하고 [C5 buildup](../2026-10-21_c5_reset_audit/README.md)을 진행했다. 아래는 C4 심사 당시의 결과다.

## 왜 판단이 바뀌었는가

이전 [C4 후보](../2026-10-21_external_search/CANDIDATES.md)는 “정책이 반복해서 이용하는 잘못된 고보상을 고치면, 불확실성만 줄이는 것보다 실제 정책 개선에 유리한가?”를 먼저 검토하도록 제안했다. 추가 조사에서 두 핵심 발상이 이미 직접 다뤄졌음을 확인했다.

1. **높게 평가된 행동을 검수해 false positive를 찾기:** ReQueST는 이 목적의 acquisition을 명시한다. 실제 rollout 대신 world model의 가상 행동을 질의한다는 차이는 있지만, 높은 보상을 우선 검수한다는 원리는 새 기여가 아니다. [ICML 2020, §2](https://proceedings.mlr.press/v119/reddy20a/reddy20a.pdf)
2. **Reward 정확도보다 정책 개선에 유용한 질문을 선택하기:** IDRL은 후보 정책 간 return 차이에 대한 정보 이득을 사용하고, policy/reward를 함께 갱신하는 deep RL 실험까지 수행한다. 따라서 기존 질문에 VLA를 붙이는 것만으로 신규성이 성립하지 않는다. [NeurIPS 2021, §3–7](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf)
3. **학습에 해로운 보상 오류를 예상해서 label 예산을 배분하기:** CARE는 LLM RLVR에서 오류 보정에 따른 advantage 변화의 예상값을 사용한다. 로봇에서의 성립을 증명한 논문은 아니지만, C4를 gradient/advantage 영향 기반으로 바꾸는 것 역시 자동으로 새 방법이 되지 않는다. [arXiv 2605.25864v1, §4–5; acceptance 미확인](https://arxiv.org/html/2605.25864v1)

PROGRESSOR·UPS·IJRR comparative-language active learning의 관련 본문과 공개 코드를 추가로 대조했다. 이들이 C4와 완전히 같은 실험을 했다는 결론은 아니다. **C4의 일반적인 동기와 선택 원리가 기존 연구에 포함되며, 남는 차이의 중요성을 아직 입증하지 못했다**는 판단이다. [비교와 확인 범위](./LITERATURE_REVIEW.md)

## 실제로 확인한 데이터

Docker Linux ARM64에서 PyArrow를 설치하고 두 공개 release의 **메타데이터 payload 20개, 총 30,198,657 bytes**를 읽었다. 영상·모델 가중치는 받지 않았다. Dataset card만 본 결과와 구분한다. [원 결과](./DATA_AUDIT.json), [검사 코드](./audit_public_data.py)

| 데이터 | 실제 읽은 범위 | C4에 대한 결론 |
|---|---|---|
| Robometer RBM OOD LeRobot export | 18,261 frame row, 571 episode, 41 task. Episode 기준 성공 233 / 실패 166 / suboptimal 172 | 실패 label은 있다. 확인한 export에는 policy checkpoint·RL update round·reward-model version·action이 없어 학습 중 보상 악용의 증가를 추적할 수 없다 |
| 같은 repository의 별도 legacy export | `train/metadata.parquet` 1,160 row 및 source별 metadata | 571개 export와 동일한 모집단이라고 가정하거나 합산하지 않는다. Source 이름의 `policy_ranking`은 시간순 checkpoint의 증거가 아니다 |
| RoboReward | train 45,072 / val 6,232 / test 2,831, 총 54,135 row | 네 필드는 `file_name`, `task`, `reward`, `gpt5_mini_check`. Policy update 이력·행동·당시 reward prediction이 없다. 정적 reward 평가에는 활용할 수 있으나 C4의 closed-loop 효과를 식별하지 못한다 |

RBM의 `timestamp`는 모든 571 episode에서 0부터 시작한다. 이는 clip 내부 시간이며 RL 학습 순서가 아니다. RoboReward test가 human-verified라는 사실은 저자 설명으로 확인했으며, 이번에 사람이 영상을 재판정한 것은 아니다. `gpt5_mini_check`는 정답 점수를 검토한 설명이므로 acquisition 입력으로 쓰면 label leakage가 생긴다. [데이터·구현 감사](./DATA_AND_CODE_REVIEW.md)

## 남길 연구 질문과 가치

질문을 남긴다면 다음 정도로 줄인다.

> **동일 VLA의 실제 RL update 전후에서, 같은 검수 비용의 기존 high-reward·uncertainty·policy-value 기반 선택법 중 무엇이 독립 성공률을 보존하는가? 실패 보정과 새로운 성공 행동의 과도한 억제가 어느 조건에서 갈리는가?**

이것은 새 selector 제안이 아니라 **기존 방법의 적용 조건을 식별할 수 있는지 묻는 진단 가설**이다. PROGRESSOR가 reach에서 과도한 push-back의 가능성을 이미 보고했으므로 “보정도 해로울 수 있다” 자체도 contribution이 아니다. 여러 VLA/task에서 재현되는 실패 조건, 이를 학습 전에 판별할 관측량, 그 관측량에 근거한 결론이 필요하다. 현재 그런 증거는 없다. [PROGRESSOR §5.1](https://arxiv.org/html/2411.17764v1)

| 항목 | 판단 |
|---|---|
| 문제의 중요성 | 높음. Learned reward로 VLA를 개선하는 실제 경로와 연결됨 |
| 현재 방법의 신규성 | 낮음. High-reward audit와 policy-aware query selection이 이미 존재 |
| 지금 가진 데이터의 식별력 | 부족. Static video/reward label로 정책 개입 효과를 복원할 수 없음 |
| 현재 컴퓨터의 실행 근거 | Metadata 감사만 성공. 공개 native VLA+reward RL 경로의 동시 실행·학습은 미검증 |
| Top-tier 연구로의 채택 | **현재안은 채택하지 않음.** 독립적인 VLA 현상 증거가 생기면 진단 연구로 재심사 |

여러 robot의 영상이 있다는 이유만으로 cross-embodiment RL 연구가 성립하지 않는다. 우선 한 native policy의 학습 이력을 검증하고, 그 결과가 성립할 때 robot별 reward 오류·검수 비용 차이로 확장한다. 이전 로봇 간 RL 전이 주제를 재개하지 않는다.

## 재개 조건

[후속 검증 계약](./DIAGNOSTIC_PROTOCOL.md)에 필요한 필드, 입력 경계, 비용, 비교군, metric, reject rule을 적었다. **가장 먼저 필요한 것은 모델 학습이 아니라, 동일 native VLA의 update 전후 rollout에 checkpoint·reward version·독립 outcome을 연결한 로그다.** 공개 release에 해당 join이 추가되거나, 현재 Docker에서 native base와 oracle-reward pilot을 검증할 실행 근거가 확보되면 재심사한다. 메타데이터 부족을 무관한 toy policy로 메우지 않는다.

현재 protocol은 **NOT IMPLEMENTATION READY**다. 환경 commit·checkpoint hash·task list·학습 예산이 확정되지 않았고, 실행 manifest나 RL 결과를 생성한 것으로 표시하지 않았다. 사용자 요청 범위인 C4를 여기까지 심사했으며 C5를 자동 착수하지 않았다.

Registry 974편과 CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242를 유지한다. 사용자 reading status를 변경하지 않았다. 실행·정리와 저장소 검증은 [VALIDATION.md](./VALIDATION.md)에 기록한다.
