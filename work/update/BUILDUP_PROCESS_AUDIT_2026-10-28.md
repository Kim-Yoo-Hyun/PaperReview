# GAP-PROC1 — 연구 공백 탐색 절차의 엄격성 검토

- 확인일: 2026-10-28 KST / **비실험 검토 DONE**
- 사용자 질문: 현재 절차가 너무 엄격해서 연구 주제 확보를 어렵게 만드는가?
- 판단: **그럴 가능성이 높다. 특히 초기 탐색에 확증·구현 단계의 요구를 앞당긴 운용을 수정해야 한다.** 기존 가이드 전체가 잘못됐거나 과거 후보들이 모두 유망했다는 결론은 아니다.
- 수행 범위: 가이드·TODO·후보 요약과 TERM1/AUTH4/N4/P4의 지정 판단 구간, 공식 지침·저자 자료 8건을 대조했다. [Source/검증 기록](../sources/buildup_process_audit_2026-10-28.json).
- 실제 후보 성과를 비교하는 실험이 아니므로 절차가 실패의 유일한 원인인지, 얼마나 개선될지는 측정하지 못했다. 기존 native 효과·외부 연구자 피드백도 새로 확보하지 않았다.

## 1. 결론의 근거: 원칙보다 적용 단계가 문제였다

기존 [가이드](../../research/IDEA_BUILDUP_GUIDE.md)는 이미 결과의 부호를 미정으로 두고, 모든 검사를 수행할 필요가 없으며, 문헌과 작은 검사를 왕복하라고 했다. 그래서 단순히 “엄격한 항목을 모두 삭제”하는 처방은 맞지 않는다. 반면 실제 최근 심사에서는 **단순 대안 이후 남는 사전 조건부 설명, 자연 사례, 동일 관측·행동 packet**이 충분히 갖춰지지 않았다는 이유로 현재 후보를 미채택하고 다음 주제로 이동했다.

그 항목들은 인과 주장·native 비교에는 중요하다. 하지만 아직 현상을 관찰하며 질문을 만드는 단계에서는 바로 그 정보가 **탐색으로 얻을 대상**이다. 이를 탐색 자격으로 요구하면 “확인하려면 먼저 확인 근거가 있어야 하는” 순환이 생길 수 있다. “추가 관측이 어떤 판단을 바꿀 것인가”와 “기제를 사전에 얼마나 완성했는가”를 구별해야 한다.

이번 판단은 목적 표집한 네 사례의 문서 감사와 외부 원칙의 비교다. 전체 후보 기각률이나 거짓 음성률을 계산한 연구가 아니다. 최근 미채택이 반복됐다는 사실만으로 과잉 엄격성을 입증하지 않았으며, 아래 구체적인 요구의 위치와 논리로 판단했다.

## 2. 외부 근거는 무엇을 요구하는가

| 출처 / 확인 깊이 | 직접 지지하는 내용 | 우리 운영에 대한 해석 |
|---|---|---|
| [NeurIPS 2026 Reviewer Guidelines](https://neurips.cc/Conferences/2026/ReviewerGuidelines), General·Use-Inspired·Concept/Negative Results 지정 구간 | 신규성은 새 알고리즘만이 아니며 기존 방법의 새 이해·유의미한 조합도 포함한다. Concept와 negative result도 근거·중요성 요구가 높다. | “새 learned method를 만들 이유가 약함”과 “연구 질문이 무가치함”을 분리한다. 유형 이름으로 낮은 증거를 정당화하지 않는다. |
| [NeurIPS 2026 E&D](https://neurips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines), Benchmark Analysis·Evaluation Methodology·Auditing | 평가 가정에 따라 과학적 결론이 달라짐을 보이는 것도 기여이며 baseline 능가는 필수가 아니다. 체계적·타당한 검증은 요구한다. | 평가/실증 후보에 새 기제나 성능 개선을 공통 필수 조건으로 두지 않는다. 단순 metric 재명명과 실제 새 평가 지식은 구별한다. |
| [ECCV 2026 Contribution Types](https://eccv.ecva.net/Conferences/2026/ReviewerContributionTypes), 서론·Applied/Systems·Concept & Feasibility | 단일 엄격 checklist를 피하고 기여 유형에 맞춰 심사한다. 개념 연구에는 의미 있는 작은 feasibility 검증이 가능하다. | 모든 초기 질문에 큰 real-robot 평가·전체 ablation을 먼저 요구할 근거가 없다. 작은 예제도 그 범위 안에서는 유용하다. |
| [ICLR 2026 Reviewer Guide](https://iclr.cc/Conferences/2026/ReviewerGuide), 평가·FAQ | SOTA는 필수가 아니며 새로운 유용한 지식이 중요하다. 이 연도의 동시기/미출판 작업 비교 정책도 별도로 정한다. | 최신 preprint는 투자 판단상 확인하되, 존재 자체를 모든 후속 연구의 기각 사유나 모든 venue의 강제 규칙으로 쓰지 않는다. |
| [Torralba·Isola·Freeman, How to Do Research](https://visionbook.mit.edu/how_to_do_research.html), §52.2 | 작은 toy로 직관을 만들고, 실패를 분해하며, 초기 제안 주변을 수정해 배운다. 가까운 문헌을 알아야 한다는 조언도 있다. | 최소한의 탐색과 문헌을 왕복한다. 첫 구상에 불확실성이 많다는 이유만으로 바로 버리거나 모든 확인을 나중으로 미루지 않는다. |
| [Nosek et al., The preregistration revolution, PNAS 2018](https://doi.org/10.1073/pnas.1708274114), 공식 검색 노출 abstract·Program of Research 구간 | 기존 관측에서 가설을 생성하는 탐색과 새 관측으로 검증하는 확증은 구별된다. 둘을 반복하되 사후 발견을 사전 예측으로 포장하지 않는다. | 탐색에는 미리 정한 효과 방향이 없어도 된다. 가설이 생긴 뒤 별도 검증을 설계한다. 모든 작업에 preregistration을 의무화하자는 결론은 아니다. |
| [Uri Alon, How To Choose a Good Scientific Problem, Molecular Cell 2009](https://www.weizmann.ac.il/mcb/alon/sites/mcb.UriAlon/files/uploads/nurturing/howtochoosegoodproblem.pdf), 저자 공개본의 검색 노출 지정 구간 | 흥미/새 지식과 실행 가능성을 별도 축으로 보고 연구자의 상황에 맞게 문제를 선택한다. | 완벽한 신규성 확신 대신 기대 학습 가치와 다음 단계 비용을 함께 평가한다. 자원 부족이 과학적 가치 없음은 아니다. |
| [Karpathy, A Survival Guide to a PhD](https://karpathy.github.io/2016/09/07/phd/), Research topics | 문제 선택 능력은 연습·도제 학습으로 발전하고, 중요한 문제에는 접근할 출발점도 필요하다. | 후보마다 확실한 성공을 요구하는 대신 배울 수 있는 공격 지점 하나를 찾는다. 흥미만 있고 접근 경로가 없는 무제한 탐색도 피한다. |

학회 문서는 **완성된 제출물의 평가 기준**이지 초기 아이디어의 통과 규정이 아니다. 연구자의 조언과 방법론 논문도 특정 절차가 논문 채택률을 높인다는 인과 증거는 아니다. 위 표의 마지막 열은 이 저장소에 적용한 해석이다. PNAS 직접 열기는 403/접근 확인 화면, Alon PDF web 열기는 timeout이어서 primary 검색 노출 구간만 사용했고 로컬 PDF는 받지 않았다.

## 3. 최근 판단에서 유지할 것과 수정할 것

| 사례 | 타당했던 제한 | 과도하게 일반화하지 말아야 할 것 |
|---|---|---|
| [TERM1](./VLA_TERMINATION_CONTRACT_REVIEW_2026-10-27.md) | First-hit/terminal 개념과 단순 종료 선행, task/controller 차이를 확인한 것은 유용하다. 순위 항등식을 새 이론으로 주장할 수 없다. | **평가 가정 변경이 중요한 정책 선택을 어떻게 바꾸는지**는 기제 설명 없이도 탐색할 수 있다. 항등식이 자명하다는 사실은 실제 현상의 빈도·규모·범위까지 자명하게 만들지 않는다. P12 미확인을 완전 중복이나 novelty의 증거로 삼지 않는다. |
| [AUTH4](./VLA_CONTACT_AUTHORIZATION_BASELINE_REVIEW_2026-10-27.md) | 올바른 초기 grounding과 지속적인 identity tracking이 주어지면 R-init으로 잘못된 보호 제외가 없다는 조건부 논증은 맞다. 그 조건에서 더 복잡한 방법을 강제할 이유가 약하다. | 그 가정이 자연 조건에서 얼마나 성립하는지는 미측정이다. **단순 대안이 존재함**과 **실제로 충분함**은 다르다. 반대로 실제 perception 실패가 있더라도 곧바로 새 authorization 방법의 필요성을 입증하지 않는다. |
| [N4](./PROXY_SELECTION_IDENTIFIABILITY_REVIEW_2026-10-26.md) | DataMIL의 goal masking 등 실제 직접 선행 확인으로 “그 비교가 없다”는 좁은 novelty 주장을 제외한 것은 타당하다. | 방법 family가 있다는 사실만으로 다른 질문·사용 조건의 실증적 가치를 지우지 않는다. 관측/선택/최종 학습의 차이는 질문을 구체화하는 데 쓴다. |
| [P4](../experiments/reactive_nav_pilot/RESULTS.md) | 실제 bounded pilot에서 사전 joint gate를 통과하지 못했다. 테스트 뒤 좋은 조건만 찾아 같은 주장을 살리지 않은 판단은 유지한다. | 이 pilot의 부정 결과를 다른 task나 분야 전체로 확대하지 않는다. 새 탐색이 필요하면 이전 결과와 분리하고 새 검증을 명시해야 한다. 이번에는 재개하지 않는다. |

**과거 기록과 후보 상태는 유지했다.** 이 감사는 후보 재심사나 효과 재현이 아니다. 특히 “기준을 완화했으니 TERM/AUTH를 GO로 바꾸자”는 결론이 아니다. 향후 질문을 같은 이유만으로 조기 탈락시키지 않도록 판단 범위를 교정했다.

## 4. 수정한 운영 방식

가이드의 [단계별 요구 수준](../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates)을 canonical 절차로 갱신했다.

1. **탐색 후보:** 중요성·가까운 선행·미확인 질문·답의 활용·다음 확인 한 가지로 선정한다. 완성된 원인 설명, 효과 방향, baseline의 실측 실패, 전체 runtime packet은 없어도 된다.
2. **탐색적 진단:** 현상 또는 비교 질문과 강한 baseline, 관측 단위, 비용/범위/중단점을 정한다. 탐색으로 설명을 만들 수 있다. 실제 실행 전에는 그 작은 검사에 필요한 계약과 Docker 제약을 충족한다.
3. **확증·본격 구현:** 새로 정한 주장과 baseline·metric·split·budget을 고정하고, 해당 기여 유형에 맞게 검증한다. 탐색 결과를 사전 예측인 것처럼 쓰지 않는다.

기각 근거도 **직접 중복 / 논리 모순 / 해당 조건의 부정 결과 / 현재 투자 우선순위 / 미확인 / 실행 대기**로 구별한다. 새 상태 시스템이나 registry를 만들지 않고 기존 문서의 이유 필드와 TODO 상태를 사용한다. 자원·자료 문제로 보류할 수는 있어도 그것을 현상 부재나 가치 없음으로 번역하지 않는다.

초기 카드는 한 페이지를 운영상 기본으로 삼고, source 목록보다 **다음에 배울 것**을 남긴다. 모든 칸을 채우기 위한 추가 source 감사는 하지 않는다. 외부 연구자에게 반박을 받는 것은 여전히 유용한 다음 행동이지만 아직 수행하지 않았고, 메시지를 대신 보내거나 확보한 피드백처럼 기록하지 않았다.

## 5. 현재 비실험 상황에서의 다음 행동

다음 TODO **GAP-S3**는 유지한다. 다만 탐색 후보를 선정할 때 이미 조건부 기제를 설명해야 한다는 요구를 낮추고, VLA navigation·mobile manipulation에서 중요한 질문과 가까운 선행의 실제 범위를 먼저 비교한다. 방법·평가/실증·system을 구분하고 가장 강한 단순 대안을 함께 적는다. 질문의 답은 미정이어도 된다.

한 질문을 보존할 이유가 있으면 그 질문의 다음 관측을 구체화한다. 더 이상의 문헌 작업으로 해결되지 않는 부분은 `실험 필요·미확인`으로 남길 수 있다. 모든 후보가 GO일 필요도, 반드시 0개여야 할 이유도 없다. 현재 과학적 중요성과 다음 확인의 정보 가치가 우선이다.

이번 변경은 사용자의 비실험 요청, Docker-only 실행 규칙, 기존 후보별 재개 gate를 완화하지 않는다. 낮춘 것은 **탐색에 들어갈 때 요구하던 완성도**이며, 실제 결과를 주장할 때의 증거 기준은 유지한다.

## 6. 검증

`py_compile`, reading generator, `git diff --check`, repository audit를 완료했고 오류·경고는 0개다. Registry 1,072편, tier 47/297/486/242, active/history 읽기 기록 344/47을 유지한다. Markdown 5,538개·상대 링크 10,930개 검사 통과.

AGENTS·PAPER·manifest/meta·tier CSV·active/history CSV 7개는 작업 전과 byte-identical이다. Generator가 `READING_PLAN.md`의 날짜만 10-28로 갱신했으며 날짜를 정규화하면 작업 전 hash와 같다. 작업 전 dirty 647개 중 수동 수정 6개와 생성 날짜 변경 1개 외 **640개**, 기존 삭제 10개를 보존했다. 신규 파일은 보고서와 source 기록 2개다. 신규 등록·읽기 승격·후보 재개·실험·설치·GPU probe·git commit/push는 수행하지 않았다.
