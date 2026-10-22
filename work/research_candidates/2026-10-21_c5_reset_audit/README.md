# C5 buildup 결과: physical reset 아래의 VLA RL 학습 범위

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- 검토일: 2026-10-21 KST
- 단계: 문헌 충돌·공개 구현·데이터 식별 가능성 심사 완료. Policy/RL 효과 실험 전.
- **판정: 현재의 일반적인 reset/coverage 방법 주장은 NO-GO. 구체적인 VLA 현상 진단은 조건부 보류. 본격 학습 우선순위는 낮춘다.**
- 후속 요청에서는 새 reset/학습 근거가 없어 이 보류를 유지하고 [C6 심사](../2026-10-21_c6_checkpoint_audit/README.md)를 진행했다. 아래 C5 검사 결과는 그대로 보존한다.

사용자 요청에 따라 [C4](../2026-10-21_c4_reward_audit/README.md)의 재개 조건을 먼저 대조했다. 동일 정책의 RL 이력·독립 outcome 또는 native learner headroom이라는 새 근거가 없어 C4 보류를 유지하고 C5를 심사했다. C4를 재실험한 것은 아니다.

## 연구 가치 판단

| 질문 | 결과 |
|---|---|
| 중요한 문제인가? | 그렇다. 로봇이 실제로 재도달할 수 있는 장면이 다음 학습 데이터를 제한한다 |
| “reset 때문에 학습 분포가 바뀐다”가 새 문제인가? | 아니다. EARL·MEDAL의 autonomous RL formulation과 직접 겹친다 |
| “목표 시작 분포를 고정해서 평가하자”가 새 방법인가? | 아니다. 기존 deployed policy evaluation의 핵심이다 |
| “VLA의 reset 범위를 넓혀 일반화를 높이자”가 새 방법인가? | 아니다. MiDAS가 직접 다루며 simulator reset 다양성은 OmniReset도 다룬다 |
| 현재 공개 데이터로 C5의 RL 효과를 식별할 수 있는가? | 이번에 확인한 범위에서는 불충족. 아래 감사 범위를 넘어 데이터 부재를 일반화하지 않는다 |
| 지금 top-tier 방법 논문으로 채택할 만한가? | **현재안은 채택하지 않는다.** 특정한 실패 조건과 강한 단순 baseline을 넘는 증거가 먼저다 |

EARL은 비연속적인 평가용 시작 분포와 연속 학습 환경을 구분했고, MEDAL은 backward policy의 상태 분포를 학습에 유리하게 바꾼다. 따라서 학습 분포가 목표 분포와 다르다는 사실만으로 결함은 아니다. [EARL §4·6](https://arxiv.org/pdf/2112.09605), [MEDAL, ICML 2022](https://proceedings.mlr.press/v162/sharma22a.html)

MiDAS는 VLA residual RL의 position-shift 일반화에 reset curriculum을 사용한다. 이 결과를 physical reset의 비용·실패까지 검증한 것으로 확대하지 않지만, “coverage 확대”라는 기여를 다시 주장할 수도 없다. [MiDAS §6·8, App. F–G; arXiv, acceptance 미확인](https://arxiv.org/html/2608.11363v1)

## 실제로 한 검사

- 선행·최신 문헌 11편을 역할별로 대조했다. 6편은 관련 본문 구간까지, 나머지 5편은 abstract/공식 metadata 중심으로 확인했다. 전편 정독이나 exhaustive survey로 표시하지 않는다. [문헌 비교](./LITERATURE_REVIEW.md), [source ledger](./SOURCE_AUDIT.json)
- Docker에서 AutoEval·연결 logger·MEDAL·MoReFree의 **4 repository / 22개 text source**를 commit에 고정해 읽었다. Upstream package를 설치하거나 실행하지 않았다. [Code audit](./CODE_AUDIT.json)
- AutoEval 공개 export의 전체 파일 목록 **13,152개**를 확인했다. 그중 metadata 파일은 1,096개, trajectory pickle 파일은 12,054개다. **Payload는 metadata 24개와 trajectory 2개만** 검사했다. 이 수를 전체 trial 수·독립 실험 수로 해석하지 않는다. [Data audit](./DATA_AUDIT.json)
- 두 pickle은 opcode와 문자열을 정적으로 검사했으며 역직렬화·이미지 해석·성공률 산출을 하지 않았다. 총 payload 14,373,568 bytes. Sample에서 `need_human_intervention`, `num_eval_retries` 등의 흔적은 확인했으나 C5의 완전한 reset 사건 이력은 확보하지 못했다.

AutoEval은 reset 실패 시 human assistance를 부르며, 논문에서 초기 상태 분포와 수동 재검토도 다룬다. **이번 결과는 AutoEval 평가가 실제로 편향되었다는 증거가 아니다.** 해당 release는 유용한 평가 자료지만 동일 VLA의 online RL 학습 로그로 확인되지 않았다. [AutoEval §3, App. K–L](https://arxiv.org/html/2503.24278v2), [공개 데이터](https://huggingface.co/datasets/zhouzypaul/auto_eval)

## 남길 질문과 다음 한 단계

> 고정된 reset controller 아래에서 VLA의 RL update가 만드는 종료 상태의 변화는, 동일한 로봇 시간·human rescue 예산에서 다음 시작 상태의 도달 가능성을 바꾸는가? 그 변화가 **별도로 고정한 목표 분포에서 측정한 정책 개선**을 얼마나 제한하며, 단순 scene quota로 해소되는가?

이것도 아직 독창성이 입증된 기여가 아니다. Reset 가능성과 forward policy의 결합은 기존 연구에 있다. 남는 가능성은 **여러 native VLA/task에서 재현되는 조건, 실패 전에 관측 가능한 징후, 실용적인 단순 조정의 효과 또는 한계**를 규명하는 경험적 연구다. 한 로봇에서 검증하기 전에 cross-embodiment나 navigation으로 확대하지 않는다.

재검토 시 첫 작업은 **한 native VLA 환경에서 요청부터 실패·재시도·human rescue까지 빠짐없이 연결한 reset 로그를 확보하고, frozen policy로 그 기록의 완전성을 점검하는 것**이다. 현재 protocol은 [DIAGNOSTIC_PROTOCOL.md](./DIAGNOSTIC_PROTOCOL.md)에 고정했지만 환경/체크포인트/실행 manifest는 미확정이다. 학습 코드를 구현하거나 toy 결과로 이 전제를 대신하지 않았다.

Registry 974편, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242 및 사용자 읽기 이력을 유지한다. [검증·Docker 정리](./VALIDATION.md)
