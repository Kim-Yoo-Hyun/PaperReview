# GAP-AUTH1 — VLA 목표 추정과 접촉 허용 판단의 결합 오류

- 작성: 2026-10-27 KST. 조사: 2026-10-26–27.
- 판정: **새로운 좁은 진단 질문으로 후속 검토할 가치 있음. 방법 채택·효과 입증은 미완료.**
- 범위: 문헌 비교, 공개 source 정적 대조, 수작업 반례와 비교 설계. 실험·모델 호출·설치·PDF 다운로드 0.
- 근거: [source ledger](../sources/vla_contact_authorization_review_2026-10-27.json), [canonical 질문](../../synthesis/05_world_models_safety.md#gap-authorization-2026), [다음 행동](../../TODO.md).
- 적용 절차: [buildup guide](../../research/IDEA_BUILDUP_GUIDE.md)의 공백 탐색 → 직접 선행 → 경쟁 설명 → 약한 고리 → 진행/기각 판단. 사용자 읽기 상태와 가설 성숙도는 올리지 않는다.

## 1. 왜 다른 주제로 이동하는가

기존 DATA-TRANSFER는 [GAP-N4](./PROXY_SELECTION_IDENTIFIABILITY_REVIEW_2026-10-26.md)에서 넓은 방법 주장의 직접 충돌과 좁은 진단의 미충족 조건을 확인했다. 같은 문헌을 반복하는 것보다 새로운 공백을 비교하는 편이 현재 비실험 작업에 적합하다. 기존 가설 전체가 반증됐다는 뜻은 아니다. N3 PARTIAL·native/model/연구 gate NOT_MET, N3-B 자원 대기와 이전 후보의 판단은 보존한다.

새 질문은 **“VLA가 잘못된 물체를 향할 때, 그 정책의 의도를 읽는 안전 필터도 같은 물체를 접촉 허용 대상으로 잘못 제외하는가?”**다. 첫 조작 대상 선택에 범위를 제한한다. 같은 geometry·tracking·controller·계산 조건에서 허용 판단의 출처만 바꿔야 한다.

이 질문의 가치 후보는 새 CBF나 별도 VLM의 존재가 아니다. **어떤 조건에서 정책 내부 신호를 보호 대상 설정에 재사용해도 되는지**, 언제 간단한 지시 기반 판단이 충분한지를 밝히는 것이다. 실제 동반 오류의 빈도와 단순 대안 이후의 새 지식은 아직 없다.

## 2. 공백부터 비교한 네 방향

2024–2026 문헌 15건을 역할별로 비교했다. 공식 proceedings 또는 IEEE가 제출한 DOI metadata로 출판을 확인한 7건과, 공식 main-track 출판을 확인하지 못한 preprint 8건을 구별한다. 모든 venue·모든 논문을 망라한 systematic review는 아니다. 최근 직접 경쟁 preprint를 top-tier 논문 수로 합산하지 않는다. 각 문헌의 실제 읽기 깊이는 ledger에 기록했다.

| 방향 | 이미 있는 근거 | 이번 판단 |
|---|---|---|
| 조작 종료·성공 후 안정성 | VLA-SCT의 correction/termination, SafeStage의 전·중·후 평가 | 일반 종료 모듈·후속 안정성 평가는 새 공백으로 채택하지 않음. E2의 timing 문제도 재명명하지 않음 |
| 비대상 물체 보존·damage 평가 | VLA-Arena, SafeVLA-Bench, ManiPhysicsBench | 성공과 부수 피해 분리 자체는 선행. 측정 항목 추가만으로 새 benchmark를 제안하지 않음 |
| Navigation–manipulation 연결 | Mobi-π의 이동과 manipulation-policy 연결 | 넓은 base/view 선택은 선행 및 D1/D2와 겹침. 현재 새 조건 예측 없음 |
| 정책 의도에 의존하는 접촉 허용 판단 | KNOWS, VLSA/AEGIS, semantic safeguards, RoboGuard | **선정:** 높은 신뢰도의 잘못된 목표에 대한 보호 제외를 분리하는 좁은 진단. 독립 guard 추가 자체는 선행 |

Scouting 근거: [VLA-SCT](https://arxiv.org/abs/2602.01811), [SafeStage](https://arxiv.org/abs/2609.21223), [ManiPhysicsBench](https://arxiv.org/abs/2610.02802), [Mobi-π, CoRL 2025](https://proceedings.mlr.press/v305/yang25b.html). 앞 세 건은 abstract 수준으로 후보 경계를 확인했으며 방법 전체를 비교했다고 주장하지 않는다.

## 3. 직접 선행이 이미 해결한 것

| 논문·확인한 출판 상태 | 이번에 확인한 근거 | 새 주장에 주는 제약 |
|---|---|---|
| [ReKep, CoRL 2024](https://proceedings.mlr.press/v270/huang25g.html), proceedings 2025 | 공식 abstract | 지시를 공간·시간 제약으로 바꾸는 접근 자체는 선행 |
| [Semantically Safe Robot Manipulation, RA-L 2025](https://doi.org/10.1109/LRA.2025.3553046) | [IEEE 제출 DOI metadata](https://api.crossref.org/works/10.1109/LRA.2025.3553046), [저자 abstract](https://arxiv.org/abs/2410.15185) | 기하 충돌을 넘어 의미 제약을 motion safeguard로 연결하는 넓은 주장 배제. 본문 세부는 미확인 |
| [SafeVLA, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html) | 공식 abstract | VLA safety alignment·constrained learning 자체는 신규성이 아님 |
| [SAFE, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html) | 공식 abstract | VLA 내부 feature로 실패를 예측하는 것과 접촉 허용의 정당성은 다른 비교 대상 |
| [VLA-Arena, ICML 2026](https://proceedings.mlr.press/v306/zhang26cp.html) | 공식 abstract·지정 code/BDDL | 안전·distractor·언어/시각 변화 평가가 존재. Suite 이름만으로 특정 violation label을 추론하면 안 됨 |
| [RoboGuard / Safety Guardrails for LLM-Enabled Robots, RA-L 2026](https://doi.org/10.1109/LRA.2026.3667488) | [IEEE 제출 metadata](https://api.crossref.org/works/10.1109/LRA.2026.3667488), [v2 III-A–B·V](https://arxiv.org/html/2503.07885v2) | 독립적인 trust module·환경 의미 기반 사양·plan repair가 이미 있음. 정확한 world model 가정의 한계도 명시됨 |
| [KNOWS, arXiv v1](https://arxiv.org/html/2606.09749v1) | §3–5 지정 본문 | Attention으로 목표를 추정해 장애물 집합에서 제외. 신뢰도 차이가 작으면 전부 보호하는 fallback이 있음. 새 비교는 **높은 신뢰도의 오선택**이어야 함 |
| [VLSA/AEGIS, arXiv v2](https://arxiv.org/html/2512.11891v2) | III–IV·V-C·VI 지정 본문, 공개 code | 외부 VLM의 지시 기반 장애물 선택과 CBF가 이미 있음. 안전 개입에 따른 OOD 실패도 선행이 논의 |
| [SafeVLA-Bench, arXiv v3](https://arxiv.org/html/2606.00773v3) | §3.1–3.3·App C 지정 구간 | Task별 적용 조건과 non-target displacement·접촉 관련 신호가 있음. 평가 정의를 새 기여로 포장하지 않음 |
| [VLPSA, arXiv v1](https://arxiv.org/html/2609.22462v1) | abstract·서론 | Whole-body/held-object safety 확장 자체도 선행. 이번 질문에서는 geometry 범위를 동일하게 고정 |

가장 가까운 KNOWS의 비교는 per-step 재위치 추정과 목표 제외를 함께 바꾸며, Naive는 초기 한 장애물의 고정 geometry다. 따라서 보고된 차이를 허용 판단 출처의 효과로 해석할 수 없다. §4.4의 내부 신호–성공 상관도 허용 집합 교체의 인과 비교는 아니다. 이는 **읽은 구간에서 해당 분리 비교를 확인하지 못했다**는 뜻이지, 관련 연구 전체에 없다는 증명은 아니다.

또한 [Initiation Safety v2](https://arxiv.org/abs/2607.07420)는 행동 시작 전 허용이라는 개념적 경계를 다룬다. 저자 workshop 표기를 RSS main-track으로 세지 않는다. “의도/자신감과 허용은 다르다”는 문장 자체는 새 기여가 아니다.

## 4. 기존 후보와 구별되는 주장

- C2는 경로·방향 등 수행 제약을 정책이 학습·준수하는 문제였다. 여기서는 **고정 정책을 감싸는 필터가 어떤 대상을 보호에서 제외하는지**가 처치다. 새로운 RL/SFT selector를 학습하지 않는다.
- D1/D2의 관측 보정·grasp/transport나 D3의 진행 중 목표 변경이 아니다. 첫 pre-grasp 구간의 지시와 목표를 고정한다.
- E2의 timing/관측 갱신, GAP-P의 navigation 보장, DATA-TRANSFER의 데이터 선택과 다른 질문이다. 이들의 실험 결과를 새 가설의 증거로 가져오지 않는다.
- 자연적인 정책 grounding 오류를 대상으로 한다. 공격이나 사람의 동의를 새로운 task family로 추가하지 않는다. “허용되지 않은 접촉”은 미리 선언한 task contract 위반이며 자동으로 물리적 손상을 뜻하지 않는다.

**Primary question:** 관측 가능한 목표 혼동 조건에서, 동일 안전 필터의 허용 집합을 정책 의도에서 얻을 때와 원 지시에서 독립적으로 얻을 때, task-contract 위반과 정상 작업 방해의 균형이 달라지는가?

## 5. 수작업 반례 — 필터의 적용 범위 확인

첫 접근 단계의 물체 집합을 O, 실제 task가 gripper 접촉을 허용한 대상을 A, 필터가 장애물에서 제외한 대상을 E라고 하자. 필터가 O \ E에 대해서만 분리를 강제한다고 가정한다. 보호해야 할 물체 b가 E \ A에 들어가면 b에 대한 제약은 없다. 따라서 모든 **설정된** 제약을 만족하면서 b와 접촉하는 행동이 허용될 수 있다.

예를 들어 지시는 왼쪽 컵 a를 집는 것이고 오른쪽 컵 b는 접촉 금지라고 미리 정한다. 정책 의도가 b를 가리켜 E={b}가 되면, a를 피하며 b에 접근하는 경로는 설정된 장애물 제약과 모순되지 않는다. 지시 기반 E={a}는 같은 b 접근을 차단할 수 있다. 차단이 a를 성공적으로 집는 행동을 만들어 준다는 보장은 없다.

이는 새 정리나 CBF 이론의 반증이 아니다. 제약 생성이 틀리면 그 제약의 보장이 원래 task에 충분하지 않다는 **범위 반례**다. 실제 VLA에서 이런 오류가 나타나는지, 기존 confidence fallback이 얼마나 막는지는 미측정이다. A는 원칙적으로 robot link–object–phase 관계다. 첫 설계는 gripper의 첫 접근으로 제한하며 물체 전체의 모든 접촉을 허용하는 해석을 피한다.

## 6. 경쟁 설명과 갈리는 예측

| 설명 | 맞을 때의 예측 | 구별할 비교 |
|---|---|---|
| H1: 정책 목표 오류와 보호 제외가 함께 틀림 | Geometry를 맞춰도 높은 신뢰도의 오선택에서 잘못된 제외가 남고, 허용 판단 교체에 민감 | 같은 상태·nominal action·geometry에서 제외 대상만 변경. 별도 자연 오류 평가 필요 |
| H0: 기존 confidence fallback이면 충분 | 오선택이 대부분 낮은 신뢰도에 모이고, 정상 작업 방해를 맞추면 독립 판단 이득이 사라짐 | 원 fallback과 threshold 보정 baseline을 반드시 포함 |
| H2: 원인은 geometry/identity tracking/latency | 허용 집합이 같아도 tracking·지연을 바꾸면 차이가 설명됨 | 같은 tracked instances·형상·갱신 시점, 별도 oracle-geometry 진단 |
| H3: 단순 고정 목표가 충분 | 초기 지시 grounding으로 정한 목표를 유지하는 것만으로 개선됨 | 동적 learned selector 없이 frozen initial target과 비교 |
| H4: 외부 판단도 같은 시각 오류를 공유 | 정책과 별도 모델을 써도 같은 b를 허용함 | Grounder별 오류 일치·불일치와 자연 분모 기록. 모듈 분리는 통계적 독립의 증거가 아님 |

H1의 후보 가치는 “나쁜 내부 feature”라는 결론이 아니다. 합리적인 저비용 신호가 어느 오류 조건에서 보호 목적에 불충분한지를 밝히는 것이다. H0/H3가 설명하면 복잡한 방법은 중단한다. 단순 대안이 충분하다는 결과도 다양한 task/model에 재현될 때 설계 지침이 될 수 있지만, 한 예시만으로 top-tier 기여를 주장하지 않는다.

## 7. 최소 비교 계약 초안

| 항목 | 고정할 내용·미결 경계 |
|---|---|
| Task | 두 혼동 가능한 물체 중 하나의 첫 접근/집기. 보호 물체와 허용 접촉 관계를 행동 전에 명시. 예시는 설계일 뿐 실행 가능한 scene은 아직 없음 |
| Policy input | 원 지시·RGB·proprio; 모든 비교에서 같은 checkpoint와 action interface. Simulator object ID·평가용 A는 정책에 노출 금지 |
| Guard input | 공통 tracker/geometry. 내부 신호 branch만 attention 사용; 독립 branch는 동일 시점 원 지시와 영상 사용. 추가 계산·메모리·지연은 비용에 포함 |
| Intervention | 같은 상태의 정책 nominal action, 공통 QP/하위 controller를 유지하고 E의 생성 경로만 변경. 물체 수·추적 갱신·형상·action chunk·fallback을 동시에 바꾸지 않음 |
| Timing | 첫 허용 판단 시점, 판단 refresh, 관측 age, 실행 deadline을 모두 기록. 초기 grounding 고정 branch와 매-step branch를 별도 비교 |
| Baselines | 무필터, 원 attention+confidence fallback, threshold만 조정한 같은 방법, 초기 지시 기반 목표 고정, 독립 지시 grounding, 전부 보호/정지, 평가용 정답 허용 집합 |
| Oracle 역할 | 정답 A·정답 geometry는 오류 분해용. 실용 방법이나 같은 입력 예산 baseline으로 집계하지 않음 |
| 측정 | 모든 rollout의 task-contract 위반·정상 완료·정상 접촉 차단·timeout·소요 시간. 성공+무위반도 함께 집계. 움직임 없는 접촉과 displacement를 구분 |
| 단위 | Scene/task와 초기 상태·policy noise seed를 묶은 paired episode. 여러 frame을 독립 표본으로 세지 않음. 학습 seed나 모델 간 일반화는 아직 없음 |
| 예산 | 동일 deadline/추가 연산 예산 비교와 각 방법 native latency 비교를 분리. 대기 시간을 숨긴 score만 비교하지 않음 |
| Split | Head/threshold/grounder 선택은 development에서만. Scene/object arrangement holdout과 test lock을 실험 전에 확정 |

**평가자의 허용 집합은 guard 예측과 독립적으로 고정한다.** 필터가 선택한 물체를 평가에서도 target으로 바꾸면 잘못된 제외 자체가 지워진다. Success 조건부 비율만으로 결론내리지 않고 전체 episode를 분모로 둔다. 아무것도 하지 않는 방법의 무위반을 작업 개선으로 세지 않는다.

자연 오류와 주입 오류를 분리한다. 고정 상태의 nominal direction 정상/오류 × 허용 집합 정상/오류 2×2는 원리 진단으로 유용하지만 인위적 오류가 현실 빈도를 증명하지 않는다. 자연 오류 strata는 개입 전 공통 관측·nominal action/목표 readout으로 정의해야 한다. 필터 실행 후 실패한 사례만 뽑는 post-selection은 금지한다. Rollout 전체와 사전 지정 strata의 결과를 함께 보고한다.

기각에 쓸 최소 효과 크기·허용 성공률 감소·task별 표본 수·checkpoint revision은 **미결**이다. 공개 source의 접속만으로 값을 만들어 동결하지 않았다. 다음 비교 packet에서 test를 보기 전에 정하며, 이 문서는 실행 manifest가 아니다.

## 8. 공개 구현을 대조한 결과

두 repository revision에서 문서/source/BDDL **10파일의 지정 구간**을 정적으로 읽었다. 실행·dependency 설치·weights/data payload 확보는 하지 않았다. Hash·구간은 ledger에 있다.

1. **AEGIS의 장애물 판단:** [utils.py L447–499](https://github.com/THU-RCSCT/vlsa-aegis/blob/ce5683c069983baef4e66025aef9da30d9d67ca2/main/utils.py#L447)는 image+instruction으로 한 장애물을 고르고 GLM-4.5V API를 호출한다. 현재 그대로는 완전 로컬 baseline이 아니다. Local 모델로 대체하면 수정 baseline임을 밝혀야 한다. API는 호출하지 않았다.
2. **AEGIS의 metric:** [main_aegis.py L367–373](https://github.com/THU-RCSCT/vlsa-aegis/blob/ce5683c069983baef4e66025aef9da30d9d67ca2/main/main_aegis.py#L367)는 선택한 added obstacle의 위치 변화 합을 0.001과 비교한다. 이 코드 경로는 모든 물체와의 직접 contact를 검사하는 평가자가 아니다. 이를 그대로 새 가설의 ground truth로 쓰지 않는다.
3. **VLA-Arena의 분리 가능성:** [환경 L1137–1180](https://github.com/PKU-Alignment/VLA-Arena/blob/babe582ebffc82b979b77964a7e56417d02f63a4/vla_arena/vla_arena/envs/bddl_base_domain.py#L1137)는 goal과 cost predicate를 구분한다. [timeout helper](https://github.com/PKU-Alignment/VLA-Arena/blob/babe582ebffc82b979b77964a7e56417d02f63a4/vla_arena/vla_arena/utils/eval_cost.py#L16)에는 final-cost 경로와 fallback이 있다. 실제 wrapper 호출·종료 처리까지 연결했다는 뜻은 아니다.
4. **Suite 이름과 실제 task는 다르다:** 읽은 state-preservation L0 blue-mug BDDL은 조작 물체 하나와 goal만, L1 black-bowl BDDL은 water balls와 `Spilled` cost를 정의한다. 이 두 task는 두 목표의 혼동·비대상 접촉을 직접 시험하는 packet이 아니다. 전체 suite에 적합한 task가 없다는 주장도 하지 않는다. Predicate 파일의 contact wrapper만으로 원하는 평가가 자동 구성되지는 않는다.
5. **KNOWS 재현 경계:** 확인한 공식 abstract/HTML과 제목 검색에서 저자 code URL을 식별하지 못했다. 논문의 방법 존재와 code 확보를 구별한다. Paper를 참고한 새 구현을 저자 공개 구현 재현으로 쓰지 않는다.

## 9. Claim–evidence와 진행·기각 기준

| 주장 | 지금의 근거 | 판정 |
|---|---|---|
| 정책이 추정한 목표가 안전 제약의 적용 대상을 바꾸는 방법이 존재 | KNOWS 지정 본문 | 문헌으로 확인 |
| 잘못된 제외는 원래 task contract 보장과 어긋날 수 있음 | §5 수작업 범위 반례 | 논리적 가능성만 확인 |
| 실제 frozen VLA에 높은 신뢰도의 자연 오선택이 충분히 존재 | 없음 | 미검증 |
| 그 오선택이 조건부 contact violation 증가를 일으킴 | 없음 | 미검증 |
| 독립 판단이 동일 비용의 fallback/초기 고정 목표보다 낫다 | 없음 | 미검증 |
| 공식 baseline·task·평가자가 새 비교에 바로 연결된다 | 선택한 code/BDDL만 감사 | 미충족; 문서/배포 존재는 실행 준비가 아님 |
| 일반izable한 새 연구 기여가 있다 | 조건부 질문과 경쟁 예측 | 아직 채택 불가; 외부 피드백 없음 |

**후속 검토 진행:** 기존 연구가 한 번에 바꾸던 target selection·tracking·geometry를 분리하는 질문과 그 질문을 틀리게 만들 수 있는 대안이 구체적이다. 실험 전 task/평가자/정책 readout의 source-level 연결을 한 단계 더 확인할 가치가 있다.

**수정:** 자연 오류가 드물거나 attention readout이 목표 방향과 관계없으면 빈도를 과장하지 않고 관찰 질문으로 축소한다. 첫 접근에서 차이가 없다고 phase transition으로 사후 이동하지 않는다. Phase-dependent specification은 별도 선행과 새 사전 설계가 필요하다.

**방법 중단:** 같은 tracking/latency로 맞춘 confidence fallback 또는 초기 고정 목표가 이득을 설명하면 새 learned guard 개발을 중단한다. 차이가 displacement/target 재정의 오류로만 생기면 metric을 고친 뒤 기존 결과를 폐기한다. Oracle 허용 집합조차 해당 오류를 줄이지 못하면 현재 진단도 다시 설계한다.

**논문 수준의 가치 조건:** 자연 발생 빈도, 같은 geometry에서의 개입 효과, 단순 대안과의 정확한 경계가 여러 task/model에서 이어져야 한다. “기존 구현 하나의 버그”, 수작업 컵 반례, 임의로 만든 오류만으로는 부족하다. 독립 판단이 항상 낫다고 미리 결론내리지 않는다.

## 10. Buildup 단계 완료 범위와 다음 TODO

| 단계 | 이번 결과 | 남은 것 |
|---|---|---|
| 0 공백 우선 탐색 | 네 방향 비교·기존 후보 중복 배제 | 넓은 신규성의 완전 증명은 아님 |
| 1 가치/결정 | 내부 신호 재사용의 조건과 단순 대안 충분성으로 좁힘 | 실제 효과 크기 |
| 2 문헌 지도 | 공식 출판 7·preprint 8, 깊이별 provenance | Abstract-only 논문의 본문은 필요한 주장에 한해 후속 |
| 3 비교/가정 | Intent·permission·geometry·metric 분리 | 실제 source 연결 |
| 4 경쟁 가설 | H0–H4와 판별 비교 작성 | 자연 오류와 paired outcome |
| 5 closest work | KNOWS·AEGIS·RoboGuard·기존 benchmark 대조 | 코드 미확보 부분과 최종 출판본 동일성 |
| 6 claim–evidence | 확인·추론·미검증을 분리 | Native 효과 |
| 7 가장 약한 고리 | 수작업 반례·10파일 정적 대조; 부적합 BDDL 식별 | 최소 실험 미실시, 실행 계약 미완료 |
| 8 외부 검토 | 미실시 | 실제 연구자 피드백; 자동 리뷰로 대체 안 함 |

**GAP-AUTH1 DONE**은 이 비실험 buildup의 완료다. 가설 입증이나 연구 GO가 아니다. 다음 **GAP-AUTH2 READY — 비실험 비교 packet 심사**는 정확한 task 2개에 대해 원 지시→target identity, 보호 관계→독립 predicate, 공통 geometry→filter 제외, policy readout→시각/time 연결을 source로 확인한다. 기존 task에 부족한 보호 사양을 추가하면 원 benchmark와 수정 진단을 구별하고, 허용 spec을 evaluator에서 policy로 누출하지 않는다. 원 baseline과 가능한 로컬 대체의 차이·미결 예산을 고정한 뒤 가장 작은 Docker pilot의 필요성을 판단한다. 적합한 자산이 없으면 추가 대형 framework 이식 대신 제한을 기록한다.

학습·GPU 실험은 자동 시작하지 않는다. 실험이 필요해지는 후속 단계에서는 사용자 선택 컴퓨터의 로컬 Docker 경로를 따르며 host 설치나 cloud API로 우회하지 않는다. 환경 image/checkpoint/정확한 자원값은 아직 선택하지 않았으므로 실행 가능하다고 표시하지 않는다.

## 11. 저장소 검증

Generator·읽기 입력/기존 변경 보존·registry audit·link·diff 검증 결과는 아래와 ledger에 기록했다. Registry 등록·tier 조정·사용자 reading status 승격은 이번 범위에 없다.

- `py_compile`, tier generator, `git diff --check` 통과. Repository audit **오류 0·경고 0**, 수정 문서 local link 617개 확인·깨짐 0.
- Registry **1,072편**, CORE 47·NEXT 297·REFERENCE 486·ARCHIVE 242, active tracker 344·history 47, 표준 note 5,360개 유지.
- Registry/manifest/meta/tier/active·history tracker 6파일은 작업 전 SHA256과 동일. Reading plan은 generator의 갱신일 한 줄만 변경됐고 이전 날짜를 대입하면 원 hash와 일치한다.
- 기존 dirty 635파일 중 수동 변경 7파일·generator 날짜 변경 1파일을 제외한 **627파일** 보존, 기존 missing 10경로 복원/추가 삭제 없음. Source text 임시 사본 10개는 hash를 남기고 삭제했다. 실험 결과는 생성하지 않았다.
