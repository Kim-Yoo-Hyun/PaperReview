# VLA 지시 수정·멀티모달 지시·부분 관측의 연구 공백 비교

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- 작성: 2026-10-29 KST
- 작업: GAP-S4 DONE — 문헌 기반 후보 선정과 최소 비교 초안
- 선택: **부분 지시 수정 이후 VLA의 제약 보존과 실행 일관성**. 탐색할 가치가 있는 평가·실증 질문이며, 새 방법의 필요성·효과·독립 논문 가치는 미확인이다.
- Canonical 질문: [VLA synthesis](../../synthesis/04_vla_generalist.md#gap-instruction-revision-2026). 다음 행동: [TODO](../../TODO.md)의 GAP-REVISION1.
- 근거: [source ledger](../sources/vla_gap_selection_2026-10-29.json). 실험·모델 호출·설치·PDF 저장·registry 신규 등록·사용자 읽기 상태 변경은 없다.

## 1. 범위와 이번 결정

[빌드업 단계별 기준](../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates)에 따라 중요한 질문, 가까운 선행, 강한 단순 대안, 다음 확인 항목을 비교했다. GPU가 없다는 이유로 이전 주제를 폐기하지 않는다. 이동–조작의 정책 교체와 navigation 종료 조건에 관한 [기존 연구](../research_topics/retired/README.md#mobile_policy_transfer)는 자원·구현 대기 상태를 유지한다.

Registry 1,074편의 관련 항목과 기존 후보 기록을 출발점으로, 2024–2026 외부 primary source **9편**을 이번 비교의 근거로 사용했다. 공식 venue 확인 6편(RSS 2024/2026, ICML 2025/2026, ICLR 2026, Findings of EMNLP 2025), preprint 3편이다. 이 중 6편은 지정 본문 구간까지, 3편은 abstract 중심으로 확인했다. 모든 학회의 전체 논문을 조사하거나 9편을 전부 정독한 것은 아니다. Findings를 EMNLP main으로, preprint를 채택 논문으로 표시하지 않는다.

## 2. 후보 세 개와 선택 이유

| 후보 질문 | 이미 알려진 부분 | 아직 확인할 비교와 실질적 가치 | 이번 배치 |
|---|---|---|---|
| **A. 지시 일부가 바뀔 때 무엇을 유지·수정·철회하는가?** | Hi Robot의 문맥 피드백·제약 처리, SwitchVLA/ReSteer의 실행 중 전환, How-level 진단의 온라인 수정 | 같은 실행 상태에서 부분 수정과 전체 재명시를 비교하고, 새 목표 성공과 기존 유효 제약 준수를 함께 확인. 단순 지시 재작성으로 충분한지에 따라 interface 보완과 정책 학습 투자가 달라짐 | **우선 탐색**. 문헌 차이가 확정됐다는 뜻은 아님 |
| B. 이미지와 텍스트가 다른 목표를 가리킬 때 무엇을 따르는가? | Interleave-VLA의 혼합 지시와 여러 이미지 입력, VAP의 참조 이미지 기반 개인화 | 일치·보완·불일치를 구별하고 text-only/reference-only/명시적 grounding과 비교. 참조 이미지와 goal image의 역할, 어느 지시가 우선인지 먼저 정의해야 정답이 생김 | 예비 후보. [AUTH](../../synthesis/05_world_models_safety.md#gap-authorization-2026)와 중복되는 초기 grounding을 새 방법으로 재포장하지 않음 |
| C. 목표가 안 보이는 것과 실제 없는 것을 구별하는가? | IVA의 false-premise 거절, 기존 도움 요청·불확실성 기반 행동 선택 | 같은 목표가 가려진 경우와 부재한 경우에서 재관측/질문/거절의 비용·오류 비교. 정책 능력 부족도 별도로 구별해야 함 | [C1](../../synthesis/04_vla_generalist.md#gap-selective-observation-2026)·[HRI](../../synthesis/01_planning_control.md#gap-hri-2026)의 인접 질문으로 보존. 독립 새 구현을 시작하지 않음 |

A를 고른 이유는 연구자의 언어 해석을 넘어 **실제 제약 위반과 조작 성공을 연결하는 비교**를 작게 정의할 수 있기 때문이다. B는 지시 간 우선권의 정답 계약이, C는 기존 관측·도움 요청 질문과의 분리가 먼저 필요하다. 이는 가능성의 수치 평가나 B/C의 가치 없음 판정이 아니다.

## 3. 직접 근거와 이미 답한 질문

각 행의 사실은 해당 source가 지지하는 범위다. 오른쪽 해석은 이번 후보를 위한 연구자 판단이다. 지정 arXiv 본문과 최종 proceedings PDF가 완전히 같다고 가정하지 않는다.

| 논문·공식 status | 이번 확인 범위와 논문이 지지하는 사실 | 후보에 주는 제약 |
|---|---|---|
| [Yell At Your Robot](https://roboticsproceedings.org/rss20/p025.html), RSS 2024 | 공식 abstract. 언어 수정으로 계층 정책의 고수준 제어를 지도하는 연구 | 인간의 언어 피드백을 이용한다는 동기 자체는 새롭지 않음 |
| [Hi Robot](https://proceedings.mlr.press/v267/shi25d.html), ICML 2025; registry pr-0142 | [arXiv v1](https://arxiv.org/html/2502.19417v1) §4.1–4.2, §5.1–5.2, Appendix A.1. 실행 중 피드백·negative constraint·상황별 수정과 고수준 oracle 비교를 포함 | 기존 제약 유지나 계층적 재계획이 전혀 없다는 주장은 배제. 우리 변경/유지/철회 분해와 정확히 같은 비교인지는 별도 문제 |
| [SwitchVLA](https://arxiv.org/abs/2506.03574), arXiv 2025; pr-0985 | [v1](https://arxiv.org/html/2506.03574v1) §3.4.2–4.1. 실행 상태에 따라 forward/rollback/advance를 사용하고 여러 실행 phase의 task switching 평가 | 전환·접촉 phase별 반응 자체는 선행. 새 후보에서 rollback 방법을 다시 제안하지 않음 |
| [ReSteer](https://roboticsproceedings.org/rss22/p143.html), RSS 2026 | [v1](https://arxiv.org/html/2603.17300v1) §III-A–C. 상태별 단일 task 능력과 steerability를 구분하고 전환을 평가 | 중간 상태의 실행 능력을 통제한다는 생각도 선행. Task-success indicator에 제약을 넣는 것만으로 새 지표·이론이 되지 않음 |
| [Do VLAs Really Follow Instructions?](https://arxiv.org/abs/2610.21251), arXiv 2026 | [v2](https://arxiv.org/html/2610.21251v2) §3–4.2, §5–6.1. Retry/correction/inverted correction과 온라인 개입을 비교하고, 지시만으로 주어지는 실행 조건을 평가 | “온라인 correction이 안 되는가”, “goal success만으로 instruction following을 알 수 있는가”는 이미 직접 다뤄짐. 부분 수정 후의 유효 조건 관리로 좁힘 |
| [Causeway](https://arxiv.org/abs/2609.30913), arXiv 2026 | Abstract. 앞 task가 만든 상태에서 다음 task 접근성이 낮아지는 현상과 re-entry pose를 이용한 inference intervention | 새 실패를 무조건 기억·언어 이해 문제로 해석하지 않음. 물리 상태와 정책의 continuation competence는 경쟁 설명 |
| [Interleave-VLA](https://iclr.cc/Downloads/2026), ICLR 2026; pr-0099 | 공식 목록과 [arXiv v2](https://arxiv.org/html/2505.02152v2) §4.3.2 확인. Goal image·multi-image 등 여러 지시 형식을 다룸 | 혼합 지시를 받는 것 자체는 선행. 검토 구간에서 불일치 판정이 명확하지 않다는 사실을 분야 전체의 공백으로 확대하지 않음 |
| [Bring My Cup! / VAP](https://icml.cc/Downloads/2026), ICML 2026; pr-0159 | 공식 목록과 [abstract v3](https://arxiv.org/abs/2512.20014) 확인. 참조 이미지로 개인화된 물체를 지정하고 frozen VLA를 시각 prompt로 유도 | 사용자별 instance grounding은 이미 해결 대상으로 존재. 모달리티 충돌의 정답·비용을 별도로 정의해야 함 |
| [Do What? / IVA](https://aclanthology.org/2025.findings-emnlp.635/), Findings of EMNLP 2025 | 공식 abstract 및 [arXiv v1](https://arxiv.org/html/2508.16292v1) §4·Limitations. False-premise instruction 검증·거절과 제한된 평가 범위를 설명 | 불가능한 명령 거절 자체는 새 문제가 아님. 가림·부재·능력 부족의 구분은 잠정 확장 질문. 버전 간 정량 수치를 혼합하지 않음 |

추가 registry 계보인 RT-H, RoboFollow, ExecVLA와 과거 HRI source 감사도 대조했다. 이들은 이번 9편의 새 확인 범위와 합산하지 않는다. Yell At Your Robot, ReSteer, How-level 진단, Causeway, IVA는 현재 manifest 제목·identifier 검색에서 미등록이며, 이번에는 외부 비교 근거로만 보존했다. 필요할 때 admission·중복 검토와 5개 노트를 거쳐 등록한다.

**검색의 결론:** 일반 task switching, 언어 correction, 제약 준수, 재관측·거절을 새 공백으로 주장할 수 없다. 반면 검토한 자료만으로 아래의 **선택적 지시 수정과 단순 재명시의 비교 결과**는 확정할 수 없다. 이는 탐색 진입의 근거이며 “최초 연구”의 증명은 아니다.

## 4. 선택한 질문의 최소 비교 초안

다음은 연구자 설계다. 공개 benchmark에 이미 구현됐거나 실행 가능한 manifest가 있다는 뜻이 아니다. 현재 질문의 짧은 canonical 카드는 [synthesis](../../synthesis/04_vla_generalist.md#gap-instruction-revision-2026)에 둔다.

**질문:** 단일 robot manipulation에서 사용자가 실행 중 목표의 일부를 수정하면, VLA 시스템은 새 목표를 따르면서 여전히 유효한 조건을 보존하고 명시적으로 철회된 조건을 제거하는가? 현재 유효한 전체 지시를 자동으로 다시 작성하면 충분한가?

**예시 — 연구자가 만든 설명용 사례:** “빨간 블록을 왼쪽 트레이에 넣고 파란 블록은 움직이지 마.” 실행 중 “빨간 블록은 오른쪽 트레이로 바꿔 줘.”라고 하면 목적지만 바뀌고 파란 블록 보호는 남는다. 이 사례의 실제 robot 실행 가능성·차별적 실패는 아직 확인하지 않았다.

### 관측 단위와 조건

- 동일 scene·기존 task prefix·수정 시점의 상태를 공유하는 비교를 한다. 초기 범위는 물리적으로 가능한 단일 수정이며 irreversible event·모순된 요청·긴 다중 턴·여러 embodiment는 제외한다. 실제 state branch와 타당성은 후속 Docker 단계에서 확인한다.
- 목적지/대상 교체, 조건 추가, 조건 철회와 의미가 같은 재진술 control을 분리한다. 수정하지 않은 조건이 처음부터 없었던 control도 둬서 단순 표현 민감도와 비교한다.
- “파란 블록을 움직여도 된다”는 허용이지 이동 명령이 아니다. 철회 후 안 움직였다는 사실만으로 실패 처리하지 않는다. 철회 오류를 관측하려면 수정된 목표를 수행하는 데 이전 금지 행동이 실제로 필요한 사례가 있어야 하며, 그렇지 않으면 해당 진단은 비정보적이라고 표시한다.
- 조건의 유효 시간도 명시한다. 철회 전 위반을 철회로 지우지 않고, 수정 후 새로 생긴 조건을 과거 행동에 소급 적용하지 않는다. 목표의 최종 달성과 trajectory 동안의 제약 준수를 별도로 기록한다.

### 먼저 비교할 단순 기준선

| 조건 | 역할·공정성 |
|---|---|
| 마지막 발화만 전달 | 문맥 손실 진단용 약한 대조군. 이를 이기는 것으로 기여를 주장하지 않음 |
| 전체 대화 이력 | 같은 고수준 모델·같은 frozen VLA를 쓰는 기본 baseline. 정책이 지원하는 입력 경로만 사용 |
| 목표/조건 목록을 갱신한 뒤 전체 현재 지시로 재작성 | 가장 중요한 **자동 단순 대안**. 별도 학습 없이 동일 모델·관측·호출 예산에서 비교하고 token/latency 차이를 보고 |
| 사람이 검수한 정확한 전체 현재 지시 | 의미 업데이트 오류를 구별하기 위한 oracle 정보 조건. 사람이 없는 deployable method와 같은 비용의 baseline으로 취급하지 않음 |

일차 비교에서는 고수준/저수준 구조·checkpoint를 고정하고 instruction representation만 바꾼다. Flat VLA와 더 큰 VLM을 추가한 계층 시스템의 차이를 기억 표현의 효과로 해석하지 않는다. 사람이 skill sequence까지 제공하는 추가 oracle은 전체 지시 oracle과 구별되는 별도의 능력 진단이다. 공개 skill/API 확인 전 이를 필수 실행 조건으로 고정하지 않는다.

동일 중간 상태에서 기본 skill과 정확한 전체 지시를 수행할 수 있는지 별도로 확인한다. Action queue의 비움/유지, controller 내부 상태, observation timestamp, 남은 물리 시간과 instruction 도착 시점을 맞춘다. 이러한 통제는 E2·D3에서 재사용하는 평가 원칙이며 새 기여가 아니다.

### 결과와 해석

일차 outcome은 **수정된 목표 달성 AND 유효 시간에 따른 모든 활성 제약 준수**다. 분모는 시작한 모든 비교 사례로 두며, goal-only success·제약 위반·잘못된 조건 삭제/잔존·응답 지연/비용을 함께 보고한다. 실패한 초기 task를 사후에 빼려면 별도 조건부 분석으로 표시한다. 실제 tolerance·deadline·split·seed·표본 수는 공개 evaluator 확인과 pilot 설계 때 고정한다. Frame을 독립 표본처럼 세지 않고 scene–수정 사례를 중심으로 분석한다.

| 가능한 관측 | 허용되는 해석·후속 |
|---|---|
| 자동 재명시가 oracle 수준이고 closed-loop 오류도 해소 | 우선 interface 보완으로 충분하다는 제한된 실증. 새 학습 방법 투자는 줄임. 독립 평가 논문 가치는 규모·일반화·실용적 영향에 달림 |
| 텍스트 조건 목록부터 틀리지만 oracle에서 실행 가능 | 상위 의미 업데이트 문제의 근거. Embodied 차별성이 없으면 일반 dialogue-state 문제로 범위를 축소 |
| 의미 목록은 정확하지만 전체 지시 조건에서도 행동 실패 | 의미 이해 실패로 단정하지 않음. Continuation competence·grounding·prompt distribution·control 원인을 추가 구별 |
| 수정과 무관하게 모든 조건이 실패 | 초기 task/skill 범위를 줄이고 정책 능력부터 확인. 복잡한 memory·RL 방법을 바로 만들지 않음 |
| 조건 간 차이가 관측되지 않음 | 해당 범위의 음성 결과. 전체 VLA의 동등성이나 제약 보존 문제의 부재로 확대하지 않음 |

## 5. 과거 후보와의 경계·다음 행동

- [C2](../research_candidates/summaries/C2_EXECUTION_CONSTRAINTS.md)의 static 실행 제약·label/data 문제를 자동 재개하지 않는다. 이번 차이는 **수정된 항목과 유지·철회된 항목의 구별**이며 학습 방법은 아직 없다.
- [D3](../research_candidates/summaries/D3_IRREVERSIBLE_SWITCHING.md)의 irreversible event와 continuation witness 부족 판단을 유지한다. 우선 가능한 가역적 수정만 다루며, raw metadata를 실제 행동 가능성의 증거로 쓰지 않는다.
- [E2](../research_candidates/summaries/README.md)의 timing 문제와 [AUTH](../../synthesis/05_world_models_safety.md#gap-authorization-2026)의 목표 grounding 문제를 교란 요인으로 명시한다. 이름을 바꿔 동일 실패 설계를 재개하지 않는다.

**GAP-REVISION1 — 다음 비실험 TODO:** 공개 task/instruction/evaluator interface를 제한적으로 대조하고, **6–8개 수작업 수정 사례**를 작성한다. 각 사례에는 최초 지시, 부분 수정, 정확한 전체 현재 지시, 유지/철회 조건과 유효 시간, 필요한 행동 능력, 관측 가능한 outcome, feasibility 미확인 사항을 담는다. Hi Robot/ReSteer/How-level 공개 자료에서 이미 동일 사례·비교가 있는지도 이 구체 사례 기준으로 확인한다. 단순 text-only 문제로 환원되는지와 강한 자동 baseline의 실제 입력 가능성을 검토한 뒤 좁은 진단 범위를 선택한다.

이 다음 단계의 종료점은 사례·비교 계약과 미확인의 명확화다. 새 source를 끝없이 늘리거나 환경 probe를 반복하지 않는다. 로컬 Docker가 호환되는 때에만 작은 native 검증을 하고, 현재 컴퓨터의 자원 부족으로 호스트·원격 실행으로 전환하지 않는다.

## 6. 저장소 검증

- 변경 전 repository audit: errors 0 / warnings 0, registry 1,074편.
- 변경 후 generator compile PASS(임시 경로에서 검사 후 bytecode 삭제), `build_reading_tiers.py` PASS, `git diff --check` PASS.
- 변경 후 repository audit: **errors 0 / warnings 0**, Markdown 5,561개·링크 11,082개 검사. Source ledger 9편·공식 publication 6편·지정 본문 확인 6편의 내부 count 일치.
- AGENTS·PAPER·papers manifest·registry meta·reading plan·tiers·active/history tracker의 8개 파일은 작업 전후 SHA-256이 같다. Registry 1,074편, CORE 47 / NEXT 299 / REFERENCE 486 / ARCHIVE 242, active 346 / history 47을 보존했다. 생성 queue와 사용자의 읽기 입력을 변경하지 않았다.
