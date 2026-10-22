# E2 buildup — VLA의 시간 표현과 feedback 효과를 구분할 수 있는가

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- 검토일: **2026-10-22 KST**. [TODO](../../../TODO.md) · [기존 8단계 절차](../../../research/IDEA_BUILDUP_GUIDE.md)
- 요청: E1을 계속하거나 다음 연구 주제를 buildup. E1의 [직전 R1](../2026-10-22_e1_buildup/R1_REVIEW.md)에서 미충족인 비교 packet을 해소할 새 근거가 없어 HOLD를 유지하고, 이번 조건부 요청에 따라 [예비 후보 E2](../2026-10-22_vla_rescout/README.md)를 심사했다. E1을 새 실험으로 기각한 것은 아니다.
- **결론: 일반적인 frequency-adaptive VLA·adaptive chunking 신규 방법은 현재 설계 NO-GO. 시간·feedback·controller를 분리하는 진단으로 REVISE하되, 주력 연구 채택은 보류한다.** 중요성은 있지만 가까운 연구가 이미 많고, 통제 후 기존 판단을 바꿀 현상과 일관된 실행 packet은 아직 확보하지 못했다.
- **E2-B1 비실험 심사 DONE**: 단계 1–6 문헌/설계, 7 해석적·source 검사, 8 내부 반박까지. Native 성능·실제 외부 피드백은 미완료. 사용자 정독 상태와 논문 evidence maturity를 승격하지 않는다.

## 1. 중요성과 문제 한 문장

**“VLA를 다른 주기로 실행할 때 얻는 이득은 시간 표현의 이득인가, 최신 관측을 반영하는 빈도·controller 변경의 이득인가?”** 서로 다른 로봇으로 옮길 때 action label의 시간 간격, 명령 수신 주기, servo와 센서 주기가 일치하지 않을 수 있다. 이 구분은 어떤 모델·실행 설정에 투자할지에 영향을 준다.

다만 “고주파가 좋다”, “chunk가 길면 반응이 느리다”는 새 질문이 아니다. [RTC / NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html), [SAIL / CoRL 2025](https://proceedings.mlr.press/v305/arachchige25a.html), [RTR / ICML 2026](https://proceedings.mlr.press/v306/wang26lj.html)부터 직접 경쟁 기준으로 둔다. 이번 범위는 manipulation이다. Navigation·다른 embodiment로의 일반성은 주장하지 않는다. RL은 필요 조건이 아니다.

## 2. 문헌 집합과 반대 근거

[CLOSEST_WORK.md](./CLOSEST_WORK.md)에 직접 비교 9편을 남겼다. 공식 proceedings 확인 4편과 최신 preprint 5편을 구분한다. 기존 FAST·RDT는 foundation 연결이며 이번 신규 정독으로 세지 않는다.

- RTC: 지연을 견디는 비동기 chunk 연결이 이미 있다.
- SAIL·SPACE: 시간 재조정과 controller의 역할을 이미 다룬다.
- RTR·Vela·PaceVLA: 고주파 latent 표현, 연속 action curve, 적응형 시간 양자화가 이미 있다.
- AAC·A2C2: 실행 길이 선택과 chunk 중간의 fresh-observation 보정이 이미 있다.
- Stability Assumption 논문: 같은 상태에서 open-loop와 closed-loop 분기의 안정성을 진단하는 접근도 이미 있다.

따라서 단순한 “연속 곡선 + 짧은 feedback”, entropy 기반 horizon, frozen VLA 위 residual, perturbation 후 open/closed-loop 비교를 신규 기여로 제안하지 않는다. Preprint도 novelty 검토에서 제외하지 않는다.

## 3. 가정·interface·증거 비교

[SOURCE_INTERFACE_AUDIT.md](./SOURCE_INTERFACE_AUDIT.md)는 README 유무에서 멈추지 않고 pinned 코드의 관측→선택→명령 경로를 확인한다.

| 확인한 사실 | 연구 해석과 경계 |
|---|---|
| RTR의 공개 π0.5 15/60 Hz recipe는 horizon 12/48, non-servo/servo 설정이 함께 다름 | 단순 주파수 한 변수의 비교로 읽을 수 없다. 저자가 의도한 시스템 설계일 수 있으며 논문 결과가 틀렸다는 증거가 아님 |
| 두 recipe의 `control_hz=60`, `execute_hz=50` 설정이 같음 | 파일명의 Hz를 실제 측정된 actuator 주기로 사용하지 않는다. 실제 timestamp는 미확보 |
| AAC client는 여러 candidate의 entropy로 길이를 고른 뒤 그 길이만큼 `env.step` 수행 | 예측 다양성·재관측 간격·계산량이 관련됨. 벽시계 지연을 반영한 실시간 평가와 동일하지 않음 |
| A2C2는 지연과 실행 길이를 분리하고 매 step 최신 관측으로 residual 계산 | E2의 넓은 feedback 질문을 선점한다. 공개 eval의 model 경로는 placeholder이며 실행 자격은 미완료 |

코드 존재, 논문 저자 보고, 우리 정책 실행을 분리했다. 현재 컴퓨터의 Docker나 모델 성능을 이번에 측정하지 않았다.

## 4. 남길 수 있는 반증 가능한 질문

**동일한 VLA와 task에서 기준 궤적의 물리적 시간, 정보의 나이, 저수준 controller·제약, 계산 예산을 명시하면, 실행 방식의 상대 순위 또는 권장 설정이 달라지는가?** 차이가 난다면 어떤 task 조건에서 재현되는가?

이는 잠정적인 진단 질문이다. 모든 요인을 한 번에 고정할 수 있다는 뜻이 아니다. [비교 계약](./CLAIM_CONTRACT.md)은 표현/시간 재조정/feedback/제어기 개입을 별도 arm으로 나누고, 통제 가능한 공통 영역에서만 비교한다. Reference 경로를 맞추는 것과 실제 robot trajectory를 동일하게 만드는 것은 다르다.

경쟁 설명은 세 가지다. 표현만으로 충분할 수 있고, 정보 갱신이 설명할 수 있으며, controller·실행 budget이 설명할 수도 있다. 하나가 기각되었다고 다른 하나를 자동 채택하지 않는다. Contact에서 feedback이 항상 유리하다는 방향도 미리 정하지 않는다.

## 5. 가장 가까운 선행 이후의 차이

남은 후보 기여는 새 scheduler가 아니라 **비교 조건을 통제했을 때 기존 설계 선택을 바꾸는 재현 가능한 경계**다. 그러나 SAIL은 이미 다중 주기 시스템을 명시하고, A2C2는 delay/horizon을 나누며, Vela는 horizon-matched 대조를 보고한다. 기존 연구가 이 문제를 전혀 고려하지 않았다는 novelty 문장은 철회한다.

독립 연구로 발전하려면 다음이 필요하다.

1. 특정 구현 오류 하나를 고친 수준을 넘어 기존 설명으로 예상하기 어려운 현상 또는 선택의 변화가 있어야 한다.
2. 강한 fixed-horizon·단순 보간·gain-only 대조와 적합한 기존 방법 이후에도 설명할 것이 남아야 한다.
3. 적어도 다른 task 조건에서 재검증해야 하며, cross-embodiment를 주장하려면 두 번째 로봇의 native 경로도 별도로 확보해야 한다.

현재는 이 세 가지의 효과 evidence가 없다. 따라서 top-tier 신규성이나 채택 가능성이 높다고 평가하지 않는다.

## 6. 주장–증거와 baseline 계약

[CLAIM_CONTRACT.md](./CLAIM_CONTRACT.md)에 구별할 intervention, 측정 단위, baseline 공정성, 중단 규칙을 작성했다. 실행 명세의 빈칸은 [QUALIFICATION_SPEC.json](./QUALIFICATION_SPEC.json)에 `null`로 남겼다.

기본 비교는 frozen native VLA의 여러 fixed horizon과 시간 의미를 보존한 단순 resampling이다. RTC/AAC는 호환 backbone에서 비교하고, A2C2는 추가 학습·입력을 별도 계정으로 둔다. RTR·SAIL의 다른 모델·hardware 수치를 같은 leaderboard에 합치지 않는다. Success와 실패를 포함한 시간 예산을 함께 보며, 매 step jerk를 물리적 시간 단위 없이 비교하지 않는다.

## 7. 가장 약한 연결 검사 결과

해석적으로 확인한 것은 다음이다. 실험·새 정리·VLA 효과 증명이 아니다.

- 같은 H를 더 빠른 주기로 실행하면 open-loop 시간도 달라진다. 이를 표현만의 효과로 귀속할 수 없다.
- 같은 경로를 더 빨리 실행하는 retiming은 속도·가속도를 바꾸므로 단순한 sample 수 변경과 다르다.
- 병합한 delta가 endpoint를 보존해도 rotation·gripper·contact의 중간 과정까지 보존하지 않는다.
- 잠시 멈추는 lockstep simulator에서 추론 wall time을 재는 것만으로 실제 지연 robustness를 검증할 수 없다.

정적 코드 검사로는 RTR의 controller mode 동시 변경, AAC의 재계획 시점, A2C2의 discrete-delay queue를 확인했다. 실제 timestamp·성공률·ranking 변화는 미측정이다. 이 결과는 넓은 attribution 주장의 전제 부족을 보여주며 E2 가설의 실험적 반증은 아니다.

## 8. 내부 반박, 투자 판단, 다음 행동

| 반박 | 현재 답 |
|---|---|
| 기존 control 지식과 A2C2/SAIL의 반복 아닌가? | 상당 부분 그렇다. 기존 방법이 예측하지 못하는 결과가 없으면 독립 주제로 종료 |
| source 설정 차이를 논문 오류로 오해하는가? | 차이는 확인했지만 영향은 측정하지 않았다. 원 논문의 full-system 목적을 인정하고 attribution만 제한 |
| GPU만 있으면 진행할 수 있는가? | 아니다. 동일 task의 checkpoint·normalizer·시간/제어기·평가 경로가 먼저 필요 |
| 공정성을 위해 장점을 없애는가? | 맞춘 조건의 causal 비교와 각 방법의 최선 시스템 비교를 별도 보고해야 함 |
| 실패해도 새 지식이 남는가? | 비교 결론을 바꾸지 못하면 재사용 가능한 감사 메모는 남지만 독립 top-tier 기여 근거는 약함 |

**현재 권고:** E2를 주력 신규 방법으로 채택하지 않는다. 진단은 조건부 보존하되 큰 학습·환경 이식은 하지 않는다. **E2-R1은 WAITING_EVIDENCE**이며 아래 한 packet이 생겼을 때만 재심사한다.

- 하나의 task–checkpoint–normalizer–controller–evaluator 연결과 재현 가능한 시간 정의.
- 기존 fixed-horizon/RTC/AAC/A2C2 비교로 곧바로 환원되지 않는 구체적인 차별적 예측.
- 성능을 미리 입증할 필요는 없지만, competing explanation을 구별할 개입과 비용을 명시.

같은 문헌 재조회나 추가 checklist 작성을 자동 후속 작업으로 반복하지 않는다. E1-R2는 별도 보류 gate로 유지한다. 실제 외부 비판은 E2-F1 / NOT_STARTED이며 이 내부 심사로 대체하지 않았다. [검증 기록](./VALIDATION.md)은 문서·registry 보존 검사다.
