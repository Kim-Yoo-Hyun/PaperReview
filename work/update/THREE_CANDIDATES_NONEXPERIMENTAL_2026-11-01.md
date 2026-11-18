# 세 실험 대기 후보의 비실험 buildup 완결 검토

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- Date: 2026-11-01 KST / Task: **PRE-GPU-3**
- 범위: 현재 공개 근거로 수행할 수 있는 문헌·논리·비교·채점·분석·외부 검토 준비. **Docker 확인/실행, 모델 호출, 시뮬레이션, 패키지 설치, PDF·weights·asset 다운로드는 하지 않았다.**
- 기준: [buildup 가이드 단계 0–8](../../research/IDEA_BUILDUP_GUIDE.md#5-공백-탐색-후-문헌에서-아이디어로-넘어가는-8단계). [기존 두 후보](./PRE_GPU_BUILDUP_REVIEW_2026-10-31.md)와 [SET 검토](../research_topics/retired/README.md#object_set)의 완료 내용을 재작성하지 않고 누락·모호한 부분을 보완했다.
- [확인 source·범위](../sources/three_candidate_nonexperimental_2026-11-01.json). 현 연구 단계의 설계 문서이며 실행 manifest나 사전등록 서비스 등록본이 아니다.

## 1. 후보 수와 완료의 의미

현재 우선 실험 대기 **탐색 후보는 3개**다. REVISION 우선 재개와 HANDOFF를 유지하고 SET이 추가되었다. 과거 HOLD/NO-GO/RETIRED 후보까지 세었다는 뜻이나, 출판 가치가 검증된 연구 주제가 세 개라는 뜻은 아니다.

| 후보 | 답을 얻으면 바뀌는 결정 | 지금 가능한 비실험 결론 |
|---|---|---|
| 부분 지시 수정 | 전체 대화 재작성·규칙만으로 충분한지, 별도 예측 상태 관리가 필요한지 | 좁은 의미–행동 진단은 유지. 제약 ledger 자체의 신규 방법 주장은 더 약해짐 |
| 모바일 조작 정책 교체 | 기존 접근 조건을 재사용할지, 제한된 비용으로 다시 고를지 | 한 template에서 유한 예산의 재선택을 평가. 최적 조건 전이 손실과 구별 |
| 물체 집합·수량 지시 | 원 지시를 그대로 쓸지, 간단한 반복만 추가할지 | 처음부터 자동 물체 나열 시스템을 만들 필요 없음. 원 지시–반복 비교부터 |

**문헌·논리·분석 설계에서 현재 처리 가능한 항목은 완료했다.** 가이드 전체가 실증적으로 완료됐다는 뜻은 아니다. Native 구현·교정·효과 관측은 남아 있고, GPU와 무관한 **독립 외부 피드백도 미수신**이다. 검토용 설명·질문은 아래에 완성했으나 외부 연락을 보내거나 독립 연구자의 평가를 대신 만들어 넣지 않았다.

## 2. 가이드 단계별 누락 점검

| 단계 | 부분 지시 수정 | 모바일 조작 | 집합·수량 | 실제 완료 경계 |
|---|---|---|---|---|
| 0 공백 | Hi Robot/ReSteer와 별도로 언어 제약 철회 선행 추가 | Policy mobilization과 기존 접근 조건 재사용 구분 | Counting·직접 지시 진단 이후 단순 반복 질문 | Targeted 검색·근거 연결 완료; 부재 증명 아님 |
| 1 중요성 | 자동 의미 관리 복잡성의 필요성 | 재검증 비용을 낼 실용적 이유 | 추가 지각·분해 module 필요성 | 조건부 의사결정 문장 완료 |
| 2–3 문헌·가정 | Ledger/재작성 선행, 자동 입력/정답 분리 | 같은 navigator·정책 묶음·한 template | 자유 subset·동적 참조·학습 노출 | 기존 근거를 계승하고 바뀔 판단에만 추가 조사 |
| 4 질문 | 한 번의 수정·유지/철회, R1/R4부터 | 유한 후보의 선택 후 paired 비교 | Q2/Q4의 원 지시 대 k회 반복 | 첫 연구 범위·제외 범위 완료 |
| 5 closest work | ReBIND는 코드 생성, 물리적 시간 위반은 별도 | Mobi-π/MoTo의 알려진 개념을 새 기여로 쓰지 않음 | Spa-Bench·조합 진단 이후 추가 지식의 조건 | 넓은 방법 신규성 주장은 하지 않음 |
| 6 주장–증거 | 모델/출력/renderer·observer 수식·단순 규칙 | 추정량·선택 불능·비용 tie·결측 처리 | 반복 명세·참조 동치·최종 집합 관측 | 3개 기계 판독용 설계 계약과 결과표 완료 |
| 7 저비용 검사 | 의미 반례·부호 동치·철회 시점 | 선택 잡음·동일 정지 상태·실패 시간 | 허용 가족·순위 참조·중간/종료 조건 | 수작업 논증·문서 정합성. 모델/실행 검사는 안 함 |
| 8 비판·판단 | 아래 반대 주장과 답변 | 아래 반대 주장과 답변 | 아래 반대 주장과 답변 | 내부 자기비판·외부 질문 완료; 독립 피드백 대기 |

단계 7의 물리 검사와 단계 8의 실제 피드백까지 DONE으로 표시하지 않는다. 반대로 그 대기 때문에 같은 문헌·metadata를 반복 조사하거나 후보를 자동 폐기하지 않는다.

<a id="revision"></a>

## 3. 부분 지시 수정: 제약 상태 관리의 의미와 행동

현재 요약은 [연구 개요](../research_topics/instruction_revision/내용/README.md#overview), 세부 입력·분석 계약은 [COMPARISON_CONTRACT](../research_topics/instruction_revision/재현%20방법/COMPARISON_CONTRACT.json)이다. 기존 8개 의미 정답과 R8 P0 실행 코드는 보존했다.

### 새 문헌이 줄인 주장

[Hi Robot, ICML 2025](https://proceedings.mlr.press/v267/shi25d.html)의 계층적 피드백 해석과 [ReSteer, RSS 2026](https://roboticsproceedings.org/rss22/p143.html)의 전환 평가를 재확인했다. 추가로 [Dead Text or Binding Clause?, arXiv 2026 §3–4·6](https://arxiv.org/html/2608.12599v1)는 철회된 제약을 기록하고 활성 명세로 컴파일하는 접근을 코드 생성에서 다룬다. 따라서 **ledger·철회 기록·현재 명세 재작성 자체는 새 방법으로 제안하지 않는다.** 이 논문의 공개 실행 저장소는 확인하지 못했으며 우리의 규칙 baseline을 저자 구현 재현으로 부르지 않는다.

남는 질문은 물리적 행동이 진행되는 중 수정 전후의 유효 제약을 정확히 채점했을 때, 자동 의미 갱신의 오류와 정책 수행 실패가 어떻게 구별되는가다. 코드 생성 선행의 결과를 VLA 성능으로 옮겨 쓰지 않는다. 한 번의 수정 사례로 장기 대화 memory 우월성을 주장하지도 않는다.

### 이번에 닫은 설계 빈칸

1. **상위 모델의 첫 기준점을 지정했다.** H(전체 이력 재계산)와 S(자기 예측 상태 갱신)는 Qwen3-8B의 동일 revision·text-only·non-thinking 설정을 쓴다. [공식 model card](https://huggingface.co/Qwen/Qwen3-8B)의 권고 sampling 설정을 반영하고 config/chat-template metadata identity를 기록했다. 입력/출력 cap·실패 처리·seed도 계약에 적었다. 이것은 배포 recipe 검증이나 strongest-model 주장이 아니다. Weights는 받지 않았고 P0에 새 모델을 넣지 않았다.
2. **자동 입력을 고정했다.** 양쪽 모두 같은 원문 사용자 이력·어휘·출력 형식, S에만 자기 예측 이전 상태를 제공한다. 정답 state·case ID·simulator pose·성공 flag는 주지 않는다. 첫 범위는 명시적인 물체 이름이라 상위 VLM 이미지가 필요 없다. 같은 이력에서 만들어진 의미 출력을 여러 물리 scene에 재사용하면 새 언어 표본으로 세지 않는다.
3. **규칙 대안의 연산과 실패 범위를 적었다.** 목표 slot 교체, 제한 추가·철회, 허용과 의무의 구별, 문장 순서와 알 수 없는 표현의 처리다. Case 전체를 정답에 매핑하는 lookup은 금지한다. 수작업 문법의 적용 범위를 일반 자연어 이해로 확대하지 않는다.
4. **공통 renderer와 observer의 수학적 정의를 구체화했다.** 취소 이력은 정책 prompt에 넣지 않는다. 위치 오차는 같은 frame의 유클리드 거리, 회전 오차는 `2 acos(clip(|q·q_ref|,0,1))`이며 quaternion을 정규화한다. `q`와 `−q`는 같은 자세다. 측정 누락은 ‘위반 없음’으로 채우지 않는다. 시간 구간은 기존 action 소유권 규칙을 따른다.
5. **확정 가능한 값과 실측할 값을 분리했다.** 위 식·단위·실패 규칙은 지금 정했다. 물리 tolerance·horizon은 실제 drift/직접 작업 능력을 모르는 상태에서 임의로 채우지 않는다. 별도 dev의 정지 drift와 알려진 이동을 구별할 수 있어야 하고, H/S/R 효과를 보기 전에 숫자를 봉인하도록 절차를 정했다.

초기 주 대비는 적격 공통 prefix에서 수정 후 joint success의 S−H이며, 전체 임무 위반·O/A·규칙 대안·의미 정확도·비용을 함께 본다. 동일 전체 이력을 허용하므로 S의 이득은 예측 상태를 명시적으로 제공한 효과이며 자동으로 문맥 압축이나 기억 용량의 효과가 아니다. 초기 상위 모델이 약해서 생긴 차이라면 모델 일반화 주장도 제한한다.

### 반대 주장과 판단

- **“기존 dialogue-state tracking을 robot에 붙인 것뿐이다.”** 맞을 수 있다. 단순 규칙·전체 재명시로 충분하면 새 방법 투자를 줄인다. 유지할 기여는 시간별 의미와 물리 실패가 실제 결론을 바꾸는지에 달렸다.
- **“병이 움직이지 않았으니 제약 이해가 입증됐다.”** 제약 없는 atomic 조건도 병을 건드리지 않을 수 있다. 성공 사례는 남기되 제약 사용의 인과 증거로 읽지 않는다.
- **“정답 의미에서도 실패하니 철회가 안 됐다.”** 같은 상태의 직접 작업 능력과 oracle 복합 지시부터 구별한다. 행동 실패를 언어 오류로 자동 귀속하지 않는다.

**외부 검토용 요청:** 부분 수정 후 남는 제약을 채점하면서 재명시·예측 상태·규칙을 같은 VLA에 연결하려 한다. ReSteer/Hi Robot/언어 ledger 연구 이후 이 비교가 어떤 새로운 판단을 제공할 수 있는지, 물리적 행동 없이 드러난 설계 오류가 있는지 검토해 달라는 설명을 준비했다. 질문은 ‘단순 재명시로 충분한가’, ‘현재 모델 규모에만 생긴 효과일 수 있는가’, ‘어떤 결과라면 VLA 연구로 확대하지 말아야 하는가’다. **미발송·피드백 미수신**이다.

<a id="handoff"></a>

## 4. 모바일 조작: 재사용 손실과 재선택 이득

[연구 개요](../research_topics/retired/README.md#mobile_policy_transfer)와 [새 단일 비교 계약](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/mobile_policy_transfer/%EC%9E%AC%ED%98%84%20%EB%B0%A9%EB%B2%95/COMPARISON_CONTRACT.json)을 연결했다. 기존 10개 source·단일 template 결과는 다시 수집하지 않았고, 2/4/4의 역할과 1개 dev P0를 유지했다.

[Mobi-π](https://proceedings.mlr.press/v305/yang25b.html)와 [MoTo](https://proceedings.mlr.press/v305/wu25c.html)의 CoRL 2025 공식 metadata·문제 범위를 확인했다. Policy별 적합한 base pose와 interaction-aware docking은 이미 다루는 문제다. 이 후보는 새로운 docking 최적화법이 아니라 **같은 navigator 아래 checkpoint+normalizer 묶음 교체 시 제한된 재검증의 효용**을 묻는다.

### 추정량·선택·분모 보완

- `k̂_A, k̂_B`는 calibration에서 선택한 설정이다. 평가 표본의 `mean[Y_B(k̂_B)−Y_B(k̂_A)]`는 **관측된 재선택 이득**이며 음수일 수 있다. `max_k μ_B(k)−μ_B(k̂_A)`라는 참 최적 조건 대비 손실을 직접 측정한 것이 아니다. Test에서 가장 잘 나온 k를 고른 뒤 primary 성능으로 보고하지 않는다.
- 서로 다른 calibration 승자는 선택 잡음만으로도 생길 수 있다. A/B 평균 성공률 차이, 거리별 민감도, B의 설정 재사용/재선택을 별도로 보고한다. `k̂_A=k̂_B`이면 같은 설정 차이는 0이고 추가 선택 비용은 그대로 남는다.
- 동률의 시간 비용은 **성공한 실행만의 시간**이 아니라 후보별 예정 calibration 네 건 전체의 실제 navigation+hold+pickup tick이다. 빨리 실패한 경로가 시간 tie를 이길 수 있다는 한계도 드러낸다. All-zero·기술적 결측의 기존 fallback 규칙은 유지한다.
- Navigation 실패는 알려진 task 실패 0이고, transport/복원 오류는 미측정이다. 후자는 운영상 ‘확인된 성공 없음’으로 남기되 참 정책 결과가 0으로 관측된 것처럼 쓰지 않는다. 미완료 arm을 빼고 setting을 고르지 않는다.
- 같은 k의 A/B는 실제 navigation+공통 정지 뒤 상태를 공유한다. 서로 다른 k는 다른 전환 상태를 만드는 개입이다. 모든 k가 같은 도착 상태라는 잘못된 ‘공정성’을 요구하지 않는다. 완전 복원 목록에는 controller·assisted grasp·RNG·queue까지 넣었다.

처음 범위의 네 평가 source는 한 template이며 25%p 간격의 기술적 비교다. 새 장면 일반화·작은 이득·동등성을 확증하지 않는다. P0를 통과하기 전에 110-phase 초안을 자동 실행하지 않는다. 재선택 12회 외에 A 선택·navigation·reference·평가·실패·복원 비용도 남긴다.

### 반대 주장과 판단

- **“기존 policy mobilization이면 당연한 결과다.”** 단순히 순위가 다르다는 관찰만으로는 약하다. 정해진 비용 안에서 실제로 재사용보다 나은 선택을 했는지, 고정 0.9 m로도 충분한지가 판단을 바꿔야 한다.
- **“B가 전반적으로 더 약한 것 아닌가.”** 같은 B의 설정 대조와 reference 능력을 분리한다. Architecture·학습 데이터 크기만의 원인 효과로 쓰지 않는다.
- **“한 장면에서 4개면 연구를 못 시작한다.”** 탐색은 가능하다. 다만 표본이 허용하지 않는 population claim을 붙이지 않는다. 처음 결과로 어떤 독립 장면을 추가해야 할지 결정한다.

**외부 검토용 요청:** 같은 navigator·세 종료 거리에서 기존 정책으로 고른 조건을 새 정책에 재사용하는 경우와 제한된 재선택을 비교한다. 질문은 ‘재검증 비용이 선행 대비 무엇을 추가하는가’, ‘최적 regret가 아닌 선택 후 이득의 보고가 유용한가’, ‘고정 기준만으로 충분하면 어떤 negative result가 남는가’다. **미발송·피드백 미수신**이다.

<a id="set"></a>

## 5. 물체 집합·수량: 첫 비교를 더 단순하게

[연구 개요](../research_topics/retired/README.md#object_set)와 기존 [비교 계약 revision 2](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/object_set/%EC%9E%AC%ED%98%84%20%EB%B0%A9%EB%B2%95/COMPARISON_CONTRACT.json)를 갱신했다. 8개 추상 의미 사례와 단일 배 조작 P0는 그대로다.

기존 [ClevrSkills](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html), [Spa-Bench](https://arxiv.org/html/2610.12696v1), [순차 조합 진단](https://arxiv.org/html/2607.29687v1)의 알려진 범위를 유지한다. 이번 Spa-Bench 재확인에서도 counting·같은 장면의 직접 지시·무행동 진단이 가까운 선행이다. 단순히 ‘VLA가 수량 지시를 어려워한다’는 주장은 별도 신규성이 아니다.

### 순서·참조·채점의 누락 보완

1. **첫 후속 비교를 D 대 R로 정했다.** 익숙한 범주·빈 접시·대상 2/3개에서 EXACTLY-two(Q2/Q4)를 원 지시로 주는 조건과 원문 k만큼 한 물체 지시를 반복하는 조건이다. 별도 상위 지각 모델을 먼저 고르는 부담 없이 단순 대안의 충분성을 볼 수 있다. L/A의 나열·분해 비교는 참조가 실제로 가능한 다음 단계다. 기존 24회 D/L/A 예시는 후속 비용 예시로 남고 자동 실행하지 않는다.
2. **R이 받는 정보와 지시를 명시했다.** k·범주·목적지는 원문에서만 읽는다. ‘현재 접시 밖의 해당 범주 물체 하나를 옮기고 이미 놓인 물체는 남겨 둔다’는 고정 지시를 공통 H의 k개 slot에서 사용한다. 성공 flag로 slot을 종료하거나 각 물체에 H 전체를 다시 주지 않는다. 이 보존 조건은 보수적인 중간 전략이며 원래 terminal-only 과제의 모든 유효 경로와 동등하다고 주장하지 않는다.
3. **L/A의 같은 subset 주장을 점검했다.** 똑같은 두 물체 중 하나를 옮기면 ‘왼쪽’의 지시 대상이 달라질 수 있다. 내부 track ID가 고정돼도 VLA가 그 ID를 볼 수 있는 것은 아니다. 각 호출에서 intended track·참조 문구·모호성을 기록해야 하며, 실패한 참조를 사후 제외해서 분해 효과를 만들지 않는다.
4. **논리 불변조건을 평가 구현의 인수 조건으로 정했다.** Evaluator ID를 바꿔도 점수 불변, 두 대상에서 ALL/EXACTLY-two의 정답 가족 동일, 세 대상에서 세 쌍 모두 허용, held non-target 누락 금지, transient 성공 후 초과를 최종 성공으로 인정하지 않기다. 이는 수작업 명세이며 evaluator 실행 결과가 아니다.
5. **관측 교정의 완료 조건을 정했다.** Geometry frame/경계·support/contact·grasp·속도 단위를 별도 dev에서 확인하고 고정한다. 파지·배치 또는 내부·외부를 구별할 수 없으면 observer 미충족으로 기록한다. 물리 drift를 모르는 상태에서 수치를 발명하지 않는다.

### 반대 주장과 판단

- **“k번 반복이면 끝나는 문제다.”** 그 가능성을 첫 비교에 둔다. 실제로 충분하면 복잡한 시각 inventory·학습을 우선하지 않는다. 반복도 부족하면 기본 조작·한 물체 지시·slot 예산·참조 실패부터 구별한다.
- **“분해가 좋다는 사실은 이미 있다.”** 맞다. 선택·참조·제어 예산을 드러낸 경계 조건이 기존 지식에 무엇을 더하는지가 중요하다. 같은 결론의 재현만 남으면 독립 연구 투자를 줄인다.
- **“알려진 과일이니 OOD 일반화다.”** 전체 학습 노출은 미확인이다. 현재는 통제된 지시/목표 비교이며 training-disjoint 조합 일반화가 아니다.

**외부 검토용 요청:** 원 지시와 수량만 파싱한 반복으로 충분한 범위를 먼저 보고, 필요할 때 같은 대상을 나열·분해하는 비교로 확장하려 한다. 질문은 ‘Spa-Bench 이후 어떤 판단이 새로 바뀌는가’, ‘반복의 정보·시간 이득을 공정하게 셌는가’, ‘참조 실패를 counting 실패로 오해할 여지가 남았는가’다. **미발송·피드백 미수신**이다.

## 6. 세 후보에 공통으로 고정한 분석·재개 규칙

- 결과 행은 **관측 없음(null)**과 실패 0을 구별한다. 예정 시도·적격 수·유효 관측·기술 오류·성공 수를 함께 남긴다. 실행하지 않은 행을 실패 데이터로 생성하지 않는다.
- Pair 차이의 각 미관측 이진 결과는 `[0,1]`로 둔다. 행별 차이의 하한은 `lower(B)−upper(A)`, 상한은 `upper(B)−lower(A)`이며 모든 예정 pair에 대해 평균한다. 이는 결측에 대한 범위이지 population 신뢰구간이 아니다. 완료 pair만의 결과는 조건부로 병기한다.
- Scalar primary 대비와 선택 규칙은 위 계약을 따른다. 여러 사례·metric·threshold 중 사후 가장 좋은 것만 primary로 바꾸지 않는다. 후속 탐색을 한 경우 발견 경로를 적고 새 자료의 확증과 구분한다.
- 물리·언어·상위 module 비용을 분리한다. 동일 seed·호출 상한은 동일 정보·token 수·wall time을 보장하지 않는다. 한 ancestor scene의 paraphrase·frame·seed를 독립 장면으로 세지 않는다.
- 초안 변경은 이유·결과 열람 여부·버전을 기록한다. Image·weights·runtime hash는 실제 생성 후에만 채운다. 현재 빈 수치를 문서 완성을 위해 추정하지 않는다.

| 남은 항목 | 지금 완료한 부분 | 추가로 필요한 것 |
|---|---|---|
| 문헌·질문·단순 대안·반증 규칙 | 세 후보 모두 완료, source 경계 명시 | 실제 결과/새 직접 선행이 생길 때만 재검토 |
| 상위 의미/규칙·observer 명세 | 입력·출력·수식·조건부 숫자 동결 절차 완료 | 구현 및 실제 입력·tokenizer·물리 상태 검증 |
| 실행 준비 | 기존 세 P0 packet 보존, 후속 비교 계약 연결 | 호환 로컬 Docker에서 image/adapter·weights·CUDA/graphics·IO 확인 |
| 효과·연구 가치 | 결과별 진행/축소/중단 기준 완료 | Native 관측·작은 공정 비교·추가 독립 자료 |
| 독립 외부 비판 | 세 설명·구체 질문·반대 주장 준비 완료 | 지도교수/동료 등 실제 응답; 현재 미발송 |

현재 요청은 **비실험 문헌·논리·설계 작업의 완료**로 닫는다. GPU 확보 전 반복할 내부 문헌/문서 TODO는 새로 만들지 않는다. 외부 검토 응답이나 새로운 관련 근거가 있으면 그것을 반영할 수 있고, 자원이 준비되면 기존 P0부터 재개한다. 구현이 남았음을 ‘GPU만 꽂으면 모든 비교가 실행된다’고 바꾸지 않는다.

## 7. 검증·보존

- 비교 계약 3개와 source ledger의 JSON 구문·문서 조건을 확인했다. 실행/자동 실행 flag는 모두 false이고, HANDOFF 2/4/4 source ID는 중복 없이 10개다. SET의 첫 비교와 조건부 후속, 미관측 값을 분리했다. **모델·의미 parser·simulator를 실행한 검사는 아니다.**
- `build_reading_tiers.py`를 임시 위치에 compile한 뒤 임시 pyc를 제거했고, `python3 -B work/scripts/build_reading_tiers.py`로 생성 영역을 동기화했다. `git diff --check`를 통과했다.
- `python3 -B work/scripts/audit_repository.py`: **오류 0·경고 0**, registry **1,077편**, CORE **47** / NEXT **302** / REFERENCE **486** / ARCHIVE **242**. 표준 노트 5,385개·Markdown 5,591개·링크 11,307개를 확인했다. 신규 등록·tier 변경·reading 상태 승격은 없다.
- 시작 시 기록한 **33개 보호 파일의 SHA-256이 모두 일치**했다. Registry identity, tier/tracker, 원래 의미 사례와 세 P0 폴더의 파일을 보존했고, 기존 staged entry digest도 일치했다. 사용자의 미커밋 작업을 되돌리거나 stage/commit/push하지 않았다.
- 준비한 명세의 실제 구현, 물리 tolerance·horizon 교정, native 실행·효과, 독립 외부 피드백은 미완료다. 이 검증 통과는 연구 효과나 실행 환경 검증이 아니다.
