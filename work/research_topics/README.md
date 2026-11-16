# 현재 연구 주제 — 내용과 재현 방법

Updated: 2026-11-16 KST. **11개 주제: 기존 8개 + hindsight 목표 선택·과제 배분·접촉 적응 탐색**을 두 폴더 구조로 관리한다. [기존 8개 우선순위·가능성 판정](#candidate-priority)과 [HINDSIGHT 초기 판정](#hindsight-exploration)·[과제 배분 초기 판정](#additional-gaps-2026-11-09)은 이 문서가, 선택한 다음 행동·자원 대기는 [TODO](../../TODO.md)가 관리한다. 논문 읽기 tier는 별도 [READING_PLAN](../../research/READING_PLAN.md)의 영역이다. 기존 6개의 [비실험 상태 감사](#nonexperimental-process-audit)는 당시 범위로 보존한다. 과거 보류·종료 후보는 자동 재개하지 않는다.

**현재 선택 후속:** [지시별 행동 보존 분석](./unified_vla_rl/내용/README.md#langret-n2)을 UNIFIED에 통합했다. N1/N2·P0 실행 준비를 마쳤으며, 실제 검증과 다음 명령은 [재현 문서](./unified_vla_rl/재현%20방법/README.md#langret-p0-preparation)·[TODO](../../TODO.md)가 소유한다. 아래11개는 문서 주제 수이며 실행 가능한 실험 수가 아니다. [REG-R14](../update/REGISTRY_MAINTENANCE_2026-11-12.md)의 선행 등록으로 기존 순위나 연구 gate를 바꾸지 않았다.

**11/16 게시 인계:** 실행 준비 자료를 포함한 registry snapshot을 GitHub에 게시하고 현재 Mac에서 새 원격 clone의 구조·링크·재현 자료236개 bytes를 확인했다(내용 commit `f04a8579`). 이전 날짜별 문서/JSON의 원격 게시 미확인은 당시 기록이다. 호환 NVIDIA 호스트의 clone·image build·native 실험은 새로 확인하지 않았으며 과학적 gate와 자원/구현 대기는 유지한다. 현재 전달 상태는 [REG-R16 게시 기록](../update/REGISTRY_ACCURACY_PSI0_2026-11-16.md#github-반영)을 따른다.

**11/07 기존 8개 내부 비교 보존:** **UNIFIED → VRL → REVISION → FEEDBACK → HANDOFF → SET → RETRIEVAL → CODEC1**. 이는 사용자의 VLA+RL·통합 정책 선호를 반영한 연구 투자 순서이며 논문 채택 확률이나 동시에 실행할 queue가 아니다. UNIFIED의 최소 검증은 자원·구현 대기, VRL·REVISION은 대안이다. **11/07 HINDSIGHT-N2의 내부 비실험 연구 설계·P0 실행 자료 작성을 마쳤으며 native 검증 대기**다. 문서 설계 완료만으로 기존 8개 대비 숫자 순위를 부여하지 않는다. FEEDBACK은 관련 진단에 재사용할 수 있으나 다른 학습 계보·action adapter를 무조건 합치지 않는다.

| 주제 | 내용 | 재현 방법 | 실제 완료·남은 범위 |
|---|---|---|---|
| 접촉 조작에서 VLA RL과 가변 임피던스 제어 | [N1/N2·판정](./contact_adaptation/내용/README.md) | [Docker 재개·실제 확인](./contact_adaptation/재현%20방법/README.md#resume) | 내부 비실험 설계·P0-PREP 완료. Physics recipe·bounded gain/sensor probe·launcher 작성·Docker stdlib16검사 통과. Mac NVIDIA allocation 실패; native image/payload·physics/RGB/gain·VLA 효과는 미검증. 전체 학습 환경/normalizer는 별도. Broad 조합 기여 제외·좁은 탐색 유지 |
| 계산 예산과 배포 목표를 고려한 다중 과제 VLA RL | [N2-R1 비실험 보완](./task_allocation/내용/README.md#nonexperimental-review) | [Docker 재개·확인 범위](./task_allocation/재현%20방법/README.md) | N2-R1·P0-PREP 완료·예비 분석으로 보존. 상태별 GRPO 신호 반례·weight/optimizer 해석·calibration/통계 보완. Recipe·sampler/actor-facing sidecar·loss fixture·launcher 작성·Docker 제어24검사 통과. Mac NVIDIA 조건 미충족. Native image/payload·tensor/IO/gradient·전체 worker 연결·정책 효과는 미검증 |
| 원 과제 전이를 고려한 VLA RL의 hindsight 목표 선택 | [공백·N2 계약](./hindsight_transfer/내용/README.md#n2-contract) | [source·구현 경계](./hindsight_transfer/재현%20방법/README.md#n2-learning-contract) | N2 내부 비실험 설계 완료·좁은 분석 후보 유지. 일반 adaptive weighting은 선행 중복. A/B split·paired 비교·공통 loss/상한 고정. P0 recipe/adapter·launcher 작성·CPU 제어15검사 통과. Mac NVIDIA 조건 미충족; image/payload·witness/native 실행·효과 미확인 |
| 단일 VLA의 RL 공동 학습·지시별 행동 보존 | [U1 판단·LANGRET 비교 설계](./unified_vla_rl/내용/README.md#langret-n2) | [LANGRET 전용 재개](./unified_vla_rl/재현%20방법/README.md#langret-p0-preparation) · [기존 U1](./unified_vla_rl/재현%20방법/README.md#resume) | 두 질문의 내부 검토·실행 자료 작성. LANGRET11/12 제어22검사, U1의 기존15검사는 서로 다른 준비 기록이다. Native build/payload·IO/gradient·초기 능력·효과 미검증. 현재 선택은 LANGRET-P0이며 U1 코드/상한은 보존. 독립 기여·외부 피드백 미확인 |
| VLA 업데이트 후 residual RL 재사용·적응 | [비실험 buildup·판단](./vla_residual_update/내용/README.md) | [현재 자원·재개 명령](./vla_residual_update/재현%20방법/README.md#resume) | 내부 비실험 검토 완료·탐색 유지. 11/05 P0 코드·recipe 초안 작성·제어 검사 9개 통과. Mac NVIDIA 조건 미충족, native build/IO·residual 학습·효과·외부 피드백 미완료 |
| 부분 지시 수정과 제약 유지·철회 | [통합 문서](./instruction_revision/내용/README.md) | [환경·명령](./instruction_revision/재현%20방법/README.md) | 내부 비실험 설계·P0 준비 코드 작성; native image/정책 실행·updater/observer 미검증. VLA 단독 대안 우선 |
| 강화학습 후학습과 시각 피드백 활용 | [기여 후보·7단계 상태](./visual_feedback/내용/README.md) | [P0 환경·재개 명령](./visual_feedback/재현%20방법/README.md#resume) | 비교 진단 유지. 11/06 P0 준비·Docker CPU 제어 검사 9개 통과. Native build/IO·전체 상태 분기 복원·효과·외부 피드백 미확인 |
| 모바일 조작 정책 교체와 종료 조건 전이 | [통합 문서](./mobile_policy_transfer/내용/README.md) | [환경·미구현 항목](./mobile_policy_transfer/재현%20방법/README.md) | 비실험 설계 완료; native image·transport·동일 상태 분기 미구현 |
| 물체 집합 선택·수량 지시 | [통합 문서](./object_set/내용/README.md) | [환경·명령](./object_set/재현%20방법/README.md) | 비실험 설계·준비 코드 완료; native 실행 대기. P0 후 D/R 비교 우선 |
| 시연 저장소 확장과 기존 과제 성능 보존 | [통합 문서](./context_retrieval/내용/README.md) | [CPU 자산 감사](./context_retrieval/재현%20방법/README.md) | 비실험 검토·자산 감사 완료; 정책 실행 packet 없음 |
| 행동 토큰화의 실행 구간 복원 | [통합 문서·추가 비실험 검토](./action_tokenization/내용/README.md#nonexperimental-followup) | [기존 CPU 진단 재현](./action_tokenization/재현%20방법/README.md) | 20 episode·101 window 진단과 추가 문헌/논리 검토 완료. 독립 방법 GO 근거 부족; learned/native 비교 미실행 |

```text
주제/
├── 내용/
│   ├── README.md      # 질문·선행·핵심 결과·한계·다음 판단을 통합
│   └── sources.json   # 확인 범위·revision·출처 기록
└── 재현 방법/
    ├── README.md      # 환경·실행 명령·완료/미구현 범위
    └── ...            # 꼭 필요한 코드·계약·설정·원시 결과
```

문서 보완은 각 README에 누적하고 날짜별 유사 보고서를 새로 만들지 않는다. 실행에 필요한 JSON·코드·원시 결과를 문서 수를 줄이려고 억지로 한 파일에 합치지 않는다. Runtime 결과와 hash는 당시 증거이며 과거 명령의 경로는 [이동·병합 대응표](./ORGANIZATION.json)로 현재 위치를 찾는다. 새 경로에는 공백이 있어 shell에서 반드시 따옴표로 감싼다.

기존 5개 정리 당시에는 71개 관련 파일을 58개, 주제별 Markdown을 **19개에서 10개**로 줄였다. 그 수량은 새 VRL의 3개 파일을 포함하지 않는 당시 기록이다. VRL은 공통 survey의 R1/R2 본문을 주제 문서 2개와 재개 JSON 1개로 통합했고 42편 source/단일 비교 계약은 공통 원장을 참조한다. Source·실제 결과·실행 코드·hash를 보존하며, 여러 주제의 공통 검토·registry 로그는 공용 이력에 둔다. 기존 이관 대응표는 위 파일이 소유하고 날짜별 유사 문서를 늘리지 않는다.

기존 5개 이관 당시 검증은 repository audit 오류·경고 0, 이동 관련 링크·fragment 1,075개, 준비 코드 검사 10개 Docker 통과였다. 논문 노트 5,450개·canonical registry/읽기 기록·staged 항목과 실행 코드/설정/원시 결과 27개를 보존한 당시 기록이다. VRL은 11/05 `재현 방법/`에 P0 재개 코드·recipe를 추가했다. 제어·중단 장치 9개는 기존 image의 임시 CPU container에서 검사했지만 native 정책 실행은 0이다. 다른 컴퓨터의 실제 실행은 미검증이다.

<a id="additional-gaps-2026-11-09"></a>

## 추가 공백에서 선택한 초기 buildup

**아래는 Robotics 중심 재선정 이전의 선택 이력이다.** [11/09 외부 문헌·기존 질문 대조](../update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md)로 추가한 두 질문 중, 동일 simulator·단일 정책에서 시작할 수 있는 **과제 배분을 먼저 선택해 N1→N2의 내부 비교 설계를 완료**했다. 기존 8개 투자 순위와 HINDSIGHT-P0 계약은 유지한다. 10개는 준비 수준이 다른 문서 주제 수이며 실행 가능한 실험 수가 아니다.

| 검토 순서 | 질문·canonical 내용 | 현재 판단 |
|---|---|---|
| 1 | [계산 예산과 배포 목표를 고려한 다중 과제 VLA RL](./task_allocation/내용/README.md) | N2 내부 설계 완료·예비 분석으로 보존. 일반 sampling/weighting 신규성은 제외. 고정 q·native reducer·분할/비용 계약과 P0 실행 자료 작성. 다음 GAP-ALLOC-P0는 호환 local NVIDIA 자원 및 native 구현 검증 대기 |
| 2 | [VLA RL 업데이트와 접촉·동역학 일반화](../../synthesis/05_world_models_safety.md#gap-physics-2026) | CURATION-HYPOTHESIS·예비 탐색. Broad 진단은 예비; 행동 학습으로 좁힌 CONTACT-RL 분기의 비실험 검토 우선 |

과제 배분의 남은 질문은 고정 배포 목적 아래 실제 계산 비용을 맞췄을 때의 효과와 조건이다. [N2-R1](./task_allocation/내용/README.md#nonexperimental-review)은 task 평균 성공률과 초기 상태별 group 신호의 차이·단순 coverage 대안·weighting 해석을 보완했다. Prism/VSR 같은 직접 선행 뒤에도 중요한 실증 차이가 남는지는 미확인이다. 비용 차이·효과·독립 기여는 미측정이므로 새 방법 GO 또는 기존 후보보다 높은 채택 가능성을 주장하지 않는다. 사람 개입 시점·기준 질문은 RLIF의 직접 비교로 제외한 판단을 유지한다.

<a id="hindsight-exploration"></a>

## 신규 탐색: 원 과제 전이를 고려한 hindsight 목표 선택

**GAP-HINDSIGHT-N0→N2 / 2026-11-07:** [선행 대조·비교 계약](./hindsight_transfer/내용/README.md#n2-contract) 후, 같은 실패의 여러 참인 목표 중 원 과제 전이를 비교하는 **좁은 분석 후보로 유지**한다. 일반 weighting은 선행과 겹치며 객체 일치 이후 이득은 미측정이다. N2는 공개 A/B와 확장 예약 C/D, 적응 단계 split, 3 seed의 fixed-pool U/O/G 비교·학습/비용 계약을 마무리했다. **방법 GO·기존 후보보다 높은 출판 가능성은 미판정**이다. P0 실행 자료를 작성했고 native 검증 대기; 자연 witness와 native 효과는 아직 없다. 기존 8개 판정·실행 자료는 유지한다.

<a id="nonexperimental-process-audit"></a>

## 6개 후보의 비실험 buildup 상태 — 2026-11-04

11/03에는 공통 절차를 대조했고, 이번에는 **각 주제의 기존 내용 문서에 7단계 상태·기여 가설·결과별 판단·구현 비용·외부 검토 질문을 보강**했다. 기존 단계별 종료 표 3개는 현행 표로 통합했으며 별도 주제 보고서는 만들지 않았다.

아래의 **정리됨**은 문헌·논리·설계의 기록이고 **검증됨**은 실제 해당 자료/실행의 증거를 뜻한다. 설계가 정리되어도 아직 자료를 못 얻었거나 구현을 하지 않았다면 그 의존성은 열린 상태로 남긴다. 완료율·문서 수로 주제 가치나 논문 채택 가능성을 점수화하지 않는다. 기준은 [비실험 절차](../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)다.

| 후보별 현행 상태 | 보강한 기여·대안 판단 | 다음 판단에 필요한 구체 증거 |
|---|---|---|
| [VLA residual 재사용](./vla_residual_update/내용/README.md#buildup-status) — 탐색 유지 | 독립 base 교체 후 과거 가중치의 비용상 가치. 구축 총비용과 교체 이후 추가 비용을 구분 | Native A/B IO → A residual 유용성. Gain/warm-start/동일 데이터 모방 이후에도 남는 이득은 미측정 |
| [부분 지시 수정](./instruction_revision/내용/README.md#buildup-status) — 좁은 평가 후보 유지 | 의미 갱신 오류와 올바른 지시의 행동 이행 오류를 구분. H·규칙·정답 지시·atomic 대조의 역할 명시 | Renderer/observer·분기 교정, O/A 능력과 H/S의 공동 목표·제약 결과 |
| [모바일 정책 교체](./mobile_policy_transfer/내용/README.md#buildup-status) — 조건부 평가 후보 유지 | 재사용 손실·유한 재선택 이득·정책 전반 능력을 구분. 선택이 같으면 같은 결과를 공유하고 비용은 보고 | 실제 도착→정지→같은 상태 A/B 분기. 현재 한 template의 작은 비교를 넘어서는 근거는 별도 |
| [물체 집합·수량](./object_set/내용/README.md#buildup-status) — 제한된 탐색 유지 | D/R의 충분성과 수량·선택·참조·실행의 설명을 구분. 중간 보존 전략과 원 terminal-only 의미의 차이 명시 | 다중 물체 능력·집합 observer·반복 wrapper, 이후 Q2/Q4 비교 |
| [시연 저장소 확장](./context_retrieval/내용/README.md#buildup-status) — 제한된 reference 입력 진단 유지 | H 불변성은 구현 대조이며 새 기여가 아님. 성공 donor 확대 주장에는 원 자료 연결이 필요 | 현재 reference의 native 입력/선택/행동. 성공·평가 독립성을 주장하려면 원 trajectory↔payload↔episode 근거 추가 |
| [행동 토큰화](./action_tokenization/내용/README.md#buildup-status) — 평가 자료 보존·독립 방법 투자 보류 | 알려진 양자화 성질과 실제 설정 선택의 가치를 구분. 평균 순위 역전만을 필수 기준으로 강제하지 않음 | 지원 codec/checkpoint·H/rate/단위 일치. 그 뒤 선택 또는 사전 제어 기준을 바꾸는지 확인; GPU만으로 해소되지 않음 |

**공통 현황:** 문제·가까운 선행·대안·기여 초안·작은 비교의 설계는 각 범위에서 정리됐다. 실행 가능성은 의존성 목록까지 작성됐으며 실제 구현/교정은 미완료다. 시연 검색의 source provenance와 토큰화의 후속 codec 조건은 추가로 남는다. 과거 CPU 증거는 시연 자산 감사와 offline codec 진단에만 적용된다. **6개 모두 독립 외부 피드백은 기록상 미수신**이며 검토 질문 준비와 구별했다.

구현을 선택한 뒤 첫 주에는 각 문서의 첫 산출물과 미완료 의존성을 재평가한다. 이는 소요 기간 예측·자동 실행 승인·새 연구 gate가 아니다. 수행 시간·마감이 정해지지 않아 총 공수는 미정이다. 새로운 자료·반례·독립 반론 없이 같은 문헌 요약을 반복하지 않는다. 이 상태 보강 당시 VLA+RL 탐색은 VRL이었으며 11/05의 새 공백 탐색은 상단 링크를 따른다. 기존 3개 정책 packet의 우선 재개는 REVISION이며 과거 HOLD/NO-GO를 자동 변경하지 않는다.

<a id="masters-publication-comparison"></a>
<a id="candidate-priority"></a>

## 기존 8개 후보의 우선순위와 연구 발전 가능성

**판정일: 2026-11-07 / CANDIDATES-PRIORITY-R1, HINDSIGHT-N0 이전 비교.** 기존 8개 주제의 buildup·실제 결과·실행 대기를 같은 기준으로 비교했다. 2024–2026 직접 선행의 기존 지정 본문/code 검토와 당시 공식 페이지·저자 abstract 재확인을 사용했다. 아래 가능성은 **연구자 판단**이며 실험으로 관측한 성과나 채택 확률이 아니다. 새 HINDSIGHT는 위 N2 판정과 P0 native 검증 대기를 따르며 아직 이 숫자 순위에 넣지 않았다.

기준은 **기여의 명확성·중요성 → 현재 VLA+RL 및 단일 정책 선호와의 적합성 → 반론을 구별할 수 있는가 → 석사 기간의 구현/데이터/검증 부담**이다. 단일 모델이라는 형태만으로 신규성 점수를 주지 않는다. 문서 수·최근성·현재 GPU 부재·Docker 제어 검사 통과를 연구 가치의 근거로 쓰지 않는다. 자원·기간이 미정이므로 부담은 상대적인 판단이며 소요 개월 수를 추정하지 않았다.

### 종합 투자 순위

| 순위 | 후보·현재 역할 | 논문으로 발전시킬 가능성·중심 기여 | 방향 적합성 / 검증 부담 | 가장 큰 위험 |
|---|---|---|---|---|
| **1** | **UNIFIED — 우선 탐색** | **조건부 유망, 실증·분석 우선.** 같은 VLA에서 value supervision이 목표 선택을 돕거나 방해하는 조건과 학습 선택 기준 | VLA+RL·단일 배포 정책에 가장 직접적 / **중상**: 실제 gradient·두 목표 능력·반복 학습 필요 | 일반 actor–critic 간섭·초기 critic 오차·loss/lr 조정의 재현에 그칠 수 있음. 새 방법 기여는 아직 약함 |
| **2** | **VRL — VLA+RL 대안** | **조건부 유망, 비용·적응 원리 중심.** Base 교체 후 과거 보정 가중치가 새 interaction 비용을 줄이는 조건 | VLA+RL 직접적, residual 파이프라인이라 최근 통합 선호와는 거리 / **높음**: A residual 학습 후 B 적응까지 필요 | Gain·warm-start·같은 데이터 모방이면 충분할 수 있음. A→B 계보와 B 우월성도 미확정 |
| **3** | **REVISION — VLA 단독 대안 우선** | **조건부 유망, 문제와 평가가 비교적 선명.** 부분 수정에서 남는 제약/철회된 제약의 이행과 의미·행동 오류 분해 | VLA interaction에 직접적, RL은 현재 필수 아님 / **중간**: 상태 분기·updater·제약 observer 필요 | 전체 이력 재작성/규칙만으로 해결되거나 정답 지시도 실행 못 할 수 있음 |
| **4** | **FEEDBACK — 보조 진단·독립 분석 예비** | **제한적 가능성.** 물리 변화 후 새 관측의 행동상 가치와 후학습 checkpoint 차이의 해석 | VLA+RL 현상 분석과 맞음 / 시작은 **중간**, RL 인과 주장까지는 추가 학습 비용 큼 | 공개 RL/SFT의 데이터·normalizer 차이. Fresh/stale 차이가 성공 회복을 뜻하지 않음 |
| **5** | **HANDOFF — 인프라 조건부 시스템 후보** | **조건부 가능성.** 조작 정책 교체 시 기존 접근 조건 재사용과 적은 재선택의 가치 | Manipulation+navigation 연결은 가장 넓음, RL/단일 모델 중심은 아님 / **매우 높음**: mobile stack·transport·복원·새 환경 | 한 template·거리 재조정에 그치거나 기존 policy mobilization 결과 반복 |
| **6** | **SET — 제한된 평가 예비** | **제한적 가능성.** 수량/집합 실패의 원인이 의미·참조·진행 추적·운동 중 어디인지 설명 | VLA에 직접적, RL 필요성 없음 / **중간**: 다중 물체 생성·observer·반복 wrapper | Counting/분해 선행과 중복; k회 반복이나 counter로 충분할 가능성 |
| **7** | **RETRIEVAL — 낮은 우선의 조건부 진단** | **현재 가능성 낮음.** 목표별 분리의 안정성과 다른 과제 reference 재사용의 이득이 갈리는 조건 | ICL VLA에 한정, 현재 RL 축과 간접적 / **중상**: 원 시연 provenance·native 연결 추가 | Goal partition으로 충분하거나 donor의 성공/평가 독립성을 확인하지 못함 |
| **8** | **CODEC1 — 평가 자료 보존, 독립 방법 투자 보류** | **현재 독립 논문 근거 약함.** 실행 구간 metric이 실제 설정 선택·행동을 바꾸는지라는 좁은 평가만 남음 | VLA action interface에 직접적, RL과 간접적 / native/learned codec 확장은 **중상** | 기존 CPU 결과가 알려진 변환/양자화로 설명됨. 단순 GPU 확보로 기여 부족이 해소되지 않음 |

**1위는 가장 높은 채택 확률을 뜻하지 않는다.** UNIFIED는 최신 방향 적합성과 작게 구별할 비교가 있어 먼저 선택했으며, 선행 대비 방법 신규성이 가장 강하다는 판단은 아니다. 방향 제한 없이 좁은 VLA 논문을 완주하는 것이 최우선이면 REVISION을 더 먼저 검토할 이유가 있다. VLA+RL은 유지하되 파이프라인도 허용하면 VRL이 주요 대안이다. Mobile manipulation 인프라와 실물 플랫폼이 이미 있으면 HANDOFF가 올라갈 수 있다. 신규 training 예산이 없으면 FEEDBACK의 동결 정책 진단이 상대적으로 가벼우나, RL 원인의 입증까지 저렴해지는 것은 아니다.

### 선행 대비 남는 기여를 판단한 이유

- **UNIFIED:** [VLAC, ICML 2026](https://proceedings.mlr.press/v306/zhang26if.html)의 통합 구조와 [ICLR 2025 표현 연구](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html)의 actor/critic 전문화가 이미 있다. [RL4VLA, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html)는 일반화 자체도 다룬다. 따라서 기여는 공유 구조·detach가 아니라 **단순 대안 뒤에도 남는 목표별 행동의 조건부 설명**이어야 한다. [N2](./unified_vla_rl/내용/README.md#nonexperimental-completion)의 8개 대안과 결과 분기를 유지한다.
- **VRL:** [Object-Centric Residual RL](https://arxiv.org/html/2606.18953v1), [PLD](https://arxiv.org/html/2511.00091v1), [Dejavu](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html)는 residual 활용·학습·경험 재사용의 강한 선행이다. 독립적인 base 교체 후 **동일 과거 데이터 아래 가중치 재사용의 추가 비용상 가치**로 좁혀야 한다. 그 질문은 유용할 여지가 있지만 rA 구축·B 적응의 두 학습 단계가 부담이다.
- **REVISION / FEEDBACK:** [ReSteer, RSS 2026](https://roboticsproceedings.org/rss22/p143.html)는 지시 변경 실패와 개선을 이미 보여 주며, [BAS-VLA](https://arxiv.org/abs/2609.23650)는 의미 변화에 따른 행동 교정을 다룬다. REVISION의 남는 제약/철회 공동 기준은 질문이 비교적 선명하다. FEEDBACK의 정보 개입은 유용한 분석이 될 수 있으나 공개 checkpoint 차이만으로 RL 목적함수의 효과라고 할 수 없어 독립 주력 순위를 낮췄다.
- **HANDOFF:** [Mobi-π](https://proceedings.mlr.press/v305/yang25b.html)와 [MoTo](https://proceedings.mlr.press/v305/wu25c.html), CoRL 2025, 이후 좋은 접근 위치나 navigation/manipulation 연결 자체는 기여가 아니다. **정책 교체에 따른 재검증/재선택 비용**이 남는 질문이지만 현재의 한 scene template와 미완성 transport로 일반적 주장을 검증하기는 어렵다.
- **SET / RETRIEVAL / CODEC1:** [ClevrSkills, NeurIPS 2024 D&B](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html)와 [Spa-Bench](https://arxiv.org/abs/2610.12696)는 조합·counting 평가를, [When Does Retrieval Help?](https://arxiv.org/abs/2610.05492)는 retrieval 방식과 cross-task 도움을, [ProAct](https://arxiv.org/abs/2610.09170)는 복원 이외의 token 예측/해독과 행동 성능을 다룬다. 각각 단순 반복·goal partition·알려진 양자화 이후 남는 가치가 좁다. 마지막 세 arXiv 자료는 이번 조사만으로 main-conference 채택을 새로 확정하지 않았다.

### 무엇이 가능성 판정을 바꾸는가

| 후보 | 우선 얻을 증거 | 계속 투자할 조건 | 축소·중단 판단 |
|---|---|---|---|
| UNIFIED | 기존 P0의 실제 gradient/IO → 목표 쌍 feasibility·기초 능력 | 같은 초기화의 행동 차이가 단순 scale/lr/초기화 대조 뒤 남고 새 조건을 예측 | 일반 optimizer 효과만 남으면 recipe/재현으로 축소; 무학습·넓은 불확실성을 반증으로 쓰지 않음 |
| VRL | A/B native IO → A residual의 실제 유용성 | 같은 old data와 추가 예산에서 weights 재사용 이득, 교체를 늘려도 유지 | Gain/모방/평범한 warm-start로 충분하면 새 규칙 투자 축소 |
| REVISION | 정답 완전 지시·atomic 능력과 joint 제약 evaluator | H/R 이후에도 의미 갱신 또는 행동 이행의 구별 가능한 병목 | O부터 실패하면 updater 연구보다 actor 능력/조건을 수정 |
| FEEDBACK | 동일 상태 fork와 네 조건 성공률 | 단순 능력 차이와 구별되는 정보 활용 패턴이 별도 task에서도 반복 | 출력만 달라지고 회복 효과가 없으면 IO 진단 수준으로 보존 |
| HANDOFF | 실제 도착→정지→동일 상태 A/B 실행 | 전반 능력·geometry 이상으로 재선택 결정을 바꾸는 조건 | 같은 선택 또는 거리 calibration만으로 충분하면 시스템 사례로 축소 |
| SET | Q2/Q4의 D 대 k회 반복 R와 다중 물체 능력 | 단순 반복 이후 남는 참조/진행 병목이 행동과 연결 | 반복/외부 counter로 충분하면 새 방법 필요성 낮춤 |
| RETRIEVAL | Native reference 입력과 donor identity/성공 근거 | Partition이 잃는 다른 목표의 실질 이득과 공정 비용 비교 | Partition이면 충분하거나 source 정합성 불명확하면 제한된 입력 진단만 |
| CODEC1 | 호환 codec의 같은 H/rate 비교와 native 행동 | Prefix 지표가 설정/제어 결정을 바꾸는 추가 증거 | 같은 FAST 집계·재구성 성질 반복이면 새 학습 투자 안 함 |

실험 실패와 가치 부족을 구별한다. 현재 UNIFIED·VRL·REVISION·FEEDBACK·HANDOFF·SET의 핵심 행동 가설은 **미검증**이다. RETRIEVAL에는 원 자료 연결 문제도 남고, CODEC1에는 **기존 결과의 설명력이 좁다는 내용상의 약점**이 있다. 8개 모두 실제 독립 연구자 피드백은 미수신이다. 작은 pilot의 착수와 top-tier 수준의 주장 확정은 별개이며, 지금 모든 확장·baseline을 첫 실행의 선결 조건으로 요구하지 않는다.

### 예비 질문과 과거 후보의 처리

**아래 예비 질문은 별도 실행 주제로 늘리지 않는다.** 새로 선택한 HINDSIGHT의 비실험 탐색은 상단에 별도로 기록한다.

| 예비 질문 | 현재 가능성·선택 조건 |
|---|---|
| [UNIFIED-U2: 행동·progress의 동일 가중치 공동 적응](./unified_vla_rl/내용/README.md) | 통합 선호에는 매우 맞지만 VLAC 이후 단순 통합만으로 부족. 독립 성공 evaluator와 reward drift를 구분할 구체 사례가 있어야 우선순위를 다시 판단 |
| [CROSSPLAY: 독립 VLA partner 협력](../update/VLA_RL_NEW_GAP_SCAN_2026-11-05.md#cross-play) | VLA+RL 전략 후보. MARL 선행 이후 남는 호환성 질문·2-robot task·기본 능력·학습 비용이 미구체화되어 기존 8개와 같은 실행 순위를 부여하지 않음 |
| [VRL-2: reward reference coverage](../update/VLA_RL_GAP_REVIEW_2026-11-03.md#counterfactual-coverage) | CounterAlign과 구별되는 coverage/label 효과를 보여 줄 자료가 생길 때 재검토 |
| [UNIFIED-U3: 실행 horizon의 credit](./unified_vla_rl/내용/README.md) | RLinf-VLA·TemporalGRPO·AtomicRL과 중복이 커 낮은 우선 유지 |

과거 [16개 요약](../research_candidates/summaries/README.md)의 NO-GO/HOLD/RETIRED와 D3/E1 재개 gate는 그대로다. 현재 순위 변경은 초기 cross-robot RL 전이나 기존 지연·관측 후보의 자동 재개가 아니다. 새 증거가 없는 상태에서 예전 주제를 다시 순위표에 넣어 유망 후보 수를 늘리지 않았다.

### 반영 범위와 다음 행동

**현재 과제 배분의 GAP-ALLOC-P0-PREP는 완료했고, 선택한 다음 행동은 호환 local NVIDIA에서 GAP-ALLOC-P0의 check → build → prepare → p0다.** Docker 제어24검사는 native 검증이 아니며 전체 worker 연결도 남아 있다. 기존 HINDSIGHT-P0 실행 대기는 해당 계약대로 보존한다. 사용자의 새 공백 탐색 요청에 따른 변경이며 UNIFIED의 과학적 강등이 아니다. UNIFIED-P0는 호환 NVIDIA 로컬 Docker에서 기존 계약대로 check → build → prepare → p0를 검증할 대기 상태로 보존한다. U1의 과학적 구분 가능성이 낮아지면 VRL 또는 REVISION의 적합성을 다시 선택한다. FEEDBACK은 U1의 의미/시각 문제와 겹치는 진단만 필요할 때 참고하며 서로 다른 checkpoint·normalizer·action 계약을 합치지 않는다. 외부 피드백은 준비된 질문으로 받을 수 있지만 이번에 전송하지 않았다.

**웹 재확인 범위:** 공식 VLAC·ICLR 표현 연구·ReSteer·RL4VLA·Mobi-π·MoTo·ClevrSkills 페이지와 BAS-VLA v2/Spa-Bench/retrieval/ProAct abstract를 확인했다. 기존 dossier의 selected full-text/code 검토를 전부 새로 수행했다고 표시하지 않는다. Dejavu CVF page는 직접 open 403, PLD 공식 program은 접근 제한이어서 기존 공식 확인 기록을 보존했다. FIRe project와 새로 검색된 [저장소 후보](https://github.com/RCILab/FIRe)는 직접 open/API 404여서 현재 code 공개 여부를 재확인하지 못했다. 검색 snippet만으로 실행 가능·채택 상태를 갱신하지 않았다.

추가 검색의 [Say the Same, Act Differently](https://arxiv.org/abs/2611.04166)는 reasoning text/action의 분리와 adversarial perturbation을 다루는 **abstract 확인 후보**다. PPO value-loss routing의 동일 실험으로 간주하지 않았으며 저자 NeurIPS 채택 표기는 공식 exact entry를 확보하지 못해 이번 paper registry에 신규 등록하지 않았다. 검색 무결과나 페이지 접근 실패는 연구 공백의 부재/존재 증명이 아니다. 전체 venue·1,112편의 게재 상태 전수 조사는 아니며 새 논문 수를 채우는 추가·tier 변경·reading status 승격은 없다.

**과거 비교의 보존:** 11/03의 5개 순위는 REVISION → HANDOFF → SET → RETRIEVAL → CODEC1이었다. 11/05의 VRL 우선·FEEDBACK 진단 권고는 [통합 검토](../update/INTEGRATED_GAP_REVIEW_2026-11-05.md)의 당시 범위다. 이 문서의 중복된 5개 상세 비교는 각 주제 문서의 선행/판단과 위 8개 표로 통합했다. 해당 시점의 실제 결과·실행 계약은 바꾸지 않았다.
