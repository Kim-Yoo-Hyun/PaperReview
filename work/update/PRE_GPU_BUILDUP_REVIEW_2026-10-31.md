# 두 연구 후보의 GPU 전 비실험 buildup 검토

- 검토일: 2026-10-31 KST / registry 정리에서 두 보고서를 병합했다.
- [부분 지시 수정](#instruction-revision) · [모바일 조작 정책 교체](#mobile-policy-transfer)
- 주제별 판단·표·source·미구현 범위는 보존했다. 원래 경로·SHA256은 [정리 ledger](../sources/registry_maintenance_2026-10-31.json)에 기록한다.
- 아래 “이번 검토”와 검증 수치는 각 원래 비실험 검토 당시 범위다. 병합 이후 registry 등록과 구분한다.
- 후속 사용자 요청의 비실험 잔여 검토는 [마지막 절](#remaining-work-review)에 추가했다. 이전 검토의 범위·수치를 소급 변경하지 않는다.

<a id="instruction-revision"></a>

## 부분 지시 수정: GPU 확보 전 buildup 보완

- 작성: 2026-10-31 KST / 비실험 검토 완료, 탐색 유지.
- 대상: [연구 개요](../research_topics/instruction_revision/내용/README.md#overview), [사례집](../research_topics/instruction_revision/내용/README.md#cases), [기존 source 검토](../research_topics/instruction_revision/내용/README.md#source-review), [buildup 가이드](../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates).
- 이번 범위: 문헌 지정 구간·비교 계약·수작업 논리 대조. Model 호출, simulator, Docker/GPU probe, dependency 설치는 하지 않았다. [출처·범위](../sources/pre_gpu_buildup_review_2026-10-31.json).

### 1. 감사 결과와 선행연구 경계

연구 질문과 공개 실행 경로는 있으나 **제약 준수의 정보성, 의미 갱신 baseline의 입력 공정성, 오류 분류·평가 분모**가 충분히 구체적이지 않았다. 이는 GPU 없이 보완할 수 있다. 아래는 다음 비교의 설계 보완이며 실제 정책 효과나 모든 구현의 완료를 뜻하지 않는다. 현재 R8 단일 IO용 실행 예산은 변경하지 않는다.

| 직접 선행과 확인 구간 | 이미 알려진 내용 | 이번 질문의 남은 경계 |
|---|---|---|
| [Hi Robot §4.1–4.2, A.1](https://arxiv.org/html/2502.19417v1) | 사용자 개입·부정 지시·문맥 조건을 계층적으로 해석한다 | 목표/제약 상태 관리 자체는 신규 방법이 아니다. 전체 이력 재해석을 강한 자동 대안으로 둔다 |
| [ReSteer, RSS 2026](https://roboticsproceedings.org/rss22/p143.html) 및 기존에 읽은 rollout 코드 | 상태에 따른 작업 전환 능력, 새 prompt와 행동 큐 교체 | 기본 switching이나 queue reset을 새 기여로 삼지 않는다 |
| [Causeway §III, V-A, VII; 2026 preprint](https://arxiv.org/html/2609.30913v1) | 이전 행동으로 바뀐 상태의 접근 가능성, 복귀 개입 및 그 제약을 다룬다 | 정확한 의미라도 행동이 실패할 수 있다. 실패를 기억/철회 오류로 바로 분류하지 않는다. 이 논문의 별도 복귀 제어를 본 비교에 몰래 추가하지 않는다 |
| [How-level 진단 §B.3–B.4; 2026 preprint](https://arxiv.org/html/2610.21251v2) | 중립 문장 대조, 지시 반응과 성공의 구별을 이미 평가한다 | 문장 길이·표현 변화와 의미 내용의 효과를 구별한다. 제약 준수/목표 성공을 나누는 것 자체도 새 기여가 아니다 |

잠정 기여는 **선택적 수정 뒤의 의미 오류와 물리적 실행 실패를 구별하고, 단순 자동 재명시가 충분한 조건을 보여 주는 평가 근거**다. 해당 조합이 독립 논문으로 충분한지는 미확인이다. 이번 targeted 검색은 같은 비교를 식별하지 못한 범위만 뜻하며 미존재 증명이 아니다. 새 학습·RL·memory architecture는 채택하지 않았다.

### 2. 제약을 이해하지 않아도 통과하는 경우를 분리

R1에서 병이 그릇 운반 경로와 멀면 병 금지를 무시한 정책도 목표와 제약을 모두 만족할 수 있다. 따라서 joint success만으로 지시 이해를 주장하지 않는다. 동일 상태의 **제약 없는 목표 지시**를 반드시 함께 기록한다. 두 조건 모두 위반하지 않으면 그 사례는 성공 결과로 보존하되 제약의 행동 효과에는 비정보적일 수 있다고 해석한다. 결과가 마음에 들지 않는다는 이유로 test에서 제거하지 않는다.

R4는 병이 이미 랙에 있지 않고, 새 목표를 수행하려면 실제 이동이 필요한 사례로 정의한다. 허용만 바뀐 R5에서는 병을 움직이지 않는 행동도 정답이다. R1/R4의 물리적 가능성·정책 능력은 native 확인 대상으로 남긴다. 인위적으로 충돌을 강제한 장면을 자연 발생 사례로 표시하지 않는다.

단순 목적지 전환 R8, 의미가 같은 재진술 R7, 제약 없는 목표 지시를 이용해 먼저 필요한 차이를 구별한다. 중립 부가 문장 대조는 표현 길이 문제가 실제로 관찰될 때 같은 상태·재질의 규칙으로 추가할 수 있다. 이 추가 대조를 P0의 자동 실행 범위로 넣지는 않는다.

### 3. 의미 갱신의 공통 입출력 계약

자동 두 조건은 같은 상위 모델·version·decoding 설정·공개 물체 이름·사용자 대화 이력·허용 관측을 사용한다. 첫 비교는 명시적 물체 이름의 지시로 한정한다. 전체 재명시는 매번 이력에서 현재 조건을 다시 도출하고, 상태 갱신은 **자신이 이전에 예측한 상태**를 수정한다. 둘 다 정답 상태·case ID별 정답표·simulator pose·성공 여부를 입력받지 않는다. 이전 상태를 사용하는 차이가 개입이며, 상태 갱신 쪽에 정답 memory를 주지 않는다.

두 조건 모두 아래 의미 구조를 출력하고 **같은 deterministic renderer**가 최종 VLA 문장을 만든다. 자유로운 문장 생성 능력 차이를 상태 관리 효과에 섞지 않는다. 아래는 구현 계약 초안이며 실행 schema·parser가 생성됐다는 뜻은 아니다.

| 필드 | 허용 의미 |
|---|---|
| `goals` | 현재 활성 목표의 대상·관계·목적지. 취소된 목표를 실행 지시에 남기지 않음 |
| `constraints` | 대상·관계 또는 이동 금지·기준 시점·유효 시작·종료 이벤트 |
| `cancelled_goals` / `revoked_constraints` | 의미 채점·감사용 과거 이력. 현재 행동 명령과 분리 |
| `event_id` | 순서가 고정된 최초/수정 발화 ID. 실제 robot tick은 evaluator에서 연결 |

각 최초/수정 발화마다 한 번의 상위 호출을 기본으로 하고 입력·출력 token, 호출 수, 지연을 기록한다. 같은 호출 상한이 같은 실제 비용을 의미하지는 않는다. Parse 실패·알 수 없는 대상·상충된 출력은 의미 실패로 기록하고 해당 비교를 중단한다. 정답으로 자동 수선하거나 성공할 때까지 재시도하지 않는다. 이전 지시를 계속 실행하는 fallback을 선택하려면 별도 조건으로 정의해야 한다.

**가장 단순한 대안도 포함한다.** 현재 8개 사례처럼 명시적인 이름·교체/추가/철회 표현으로 제한하면, 결과를 보기 전에 고정한 문법 parser와 slot overwrite가 충분할 수 있다. 이 규칙형 baseline은 원문 문자열만 읽으며 정답 편집 연산을 받지 않는다. 지원하지 않는 문장은 명시적으로 실패 처리하고 적용 범위를 보고한다. 정답 edit를 입력받는 규칙기는 자동 baseline이 아니라 oracle이다. 이 계약은 작성했지만 parser 실행·LLM 정확도 검증은 하지 않았다.

Oracle 전체 지시는 같은 renderer를 사용하되 의미 정답을 가진 **진단 조건**으로 구분한다. 원자 작업 지시는 실제 continuation 능력 비교다. Oracle이 항상 더 높은 성공을 보장하지 않으므로 수학적 성능 상한으로 표시하지 않는다.

### 4. 시간 의미·관측 경계의 수작업 검수

아래는 가상 경우의 논리 대조이며 모델/정책 test 결과가 아니다.

| 경우 | 올바른 채점 | 잘못된 해석 |
|---|---|---|
| 목적지만 변경, 병 제한 언급 없음 | 기존 병 제한 유지 | 최신 발화에 없으니 제한 삭제 |
| 병 금지 철회 + 병→랙 목표 | 철회 전 위반은 유지, 이후 이동 허용·목표 수행 필요 | 병을 안 움직였으니 무조건 제약 준수 성공 |
| 병 이동 허용만 추가 | 병 이동 의무 없음 | 병을 움직이지 않았으니 철회 실패 |
| 수정 전 병이 움직였다가 원위치 | 기존 구간 위반을 보존 | 최종 pose가 같으니 항상 준수 |
| 수정 시 새 금지 추가 | 그 시점 pose·이후 구간을 기준으로 측정 | 과거 이동을 새 제약 위반으로 소급 |
| 의미가 같은 재진술 | 목표·제약 정답은 동일 | queue reset으로 생긴 차이를 의미 갱신 능력으로 해석 |

평가용 기준 pose와 policy-visible input을 구분한다. 현재 native VLA는 현 RGB/proprio/prompt만 받으며 최초 RGB나 수치 pose reference가 자동으로 추가되지 않는다. 따라서 `original position`을 입력했다고 과거 pose를 기억·복원할 수 있다고 가정하지 않는다. 그 능력이 필요한 확장은 양쪽에 같은 reference observation을 제공하는 별도 정보 조건으로 다뤄야 한다.

문장 tokenization·200-token cap에서 목표/제약 보존 여부는 실제 tokenizer를 Docker에서 확인한다. Silent truncation이 일어난 사례를 정책 의미 실패로 집계하지 않는다. 위치·회전 tolerance는 dev의 정지 drift와 측정 단위를 확인한 뒤 policy 비교 결과를 보기 전에 고정한다. 지금 임의 수치를 “검증된 임계값”으로 채우지 않는다.

### 5. 분모·오류·예상 결과표

주 평가 단위는 **원본 초기 상태 + 공통 실행 prefix + 수정 이벤트**다. 같은 prefix의 여러 문장/seed는 반복 관측이며 독립 장면 수가 아니다. Prefix는 비교할 updater 결과를 보기 전에 공통 정책·고정 지시로 생성한다. 각 arm의 별도 rollout을 같은 상태라고 부르지 않는다.

- 전체 임무 결과는 모든 시도와 수정 전 위반을 포함한다. 수정 전 이미 제약이 깨진 사례를 조용히 버리지 않는다.
- 수정 이후 방법 비교에는 **수정 전 정보로만 정의한 적격 prefix**의 결과를 별도로 보고한다. 적격 수·탈락 이유·전체 임무 결과를 함께 공개한다. 이후 성공 여부에 따른 필터링은 금지한다.
- 의미 parse 실패는 end-to-end 실패, 정책 budget 내 미달은 행동 실패로 기록한다. 인프라 예외는 기술 오류로 별도 표기하고 완료된 표본만의 성공률을 전체 성공률처럼 쓰지 않는다.
- R8의 upstream first-hit와 복합 제약의 평가 종료는 다르다. 후속 비교는 공통 종료/중단 규칙과 종료 후 제약 평가 범위를 정한 후 시행한다.

결과표 열은 `조건 / 시도 수 / prefix 적격 수 / 의미 exact match / 제약 누락·잔존 / 목표 성공 / 시간별 위반 / joint success / 기술 오류 / 상위 호출·token·지연`으로 고정한다. 현재 값은 모두 미측정이다. Semantic exact match는 문자열 일치가 아니라 대상·관계·기준·유효 구간 일치다.

| 앞으로 나올 수 있는 관측 | 다음 판단 |
|---|---|
| 단일 작업부터 실패 | 상태 접근 가능성·정책 능력부터 진단. Memory/RL 투자 근거 없음 |
| 단일 작업은 가능, oracle 복합 지시는 실패 | 제약 실행·입력 표현·문체를 점검. 자동 의미 갱신 탓으로 단정하지 않음 |
| Oracle은 가능, 자동 재명시와 상태 갱신이 비슷함 | 추가 상태 관리 필요성은 미확인. 차이 없음도 범위를 정해 보존 |
| 규칙 parser 또는 전체 재명시로 충분 | 단순 interface를 기준으로 삼고 새 방법 주장을 축소 |
| 상태 갱신의 의미 정확도만 개선 | 언어 단계 결과. 행동 차이가 없으면 VLA 효과로 확대하지 않음 |
| 의미·행동 개선이 함께 관측 | 동일 정보·비용·표현 조건과 새 사례에서 확인할 후속 질문을 선택 |

### 6. GPU 전 완료와 남은 것

| 가이드 단계 | 이번 재점검 결과 |
|---|---|
| 0–1 공백·중요성 | 부분 수정 이후 재명시만으로 충분한가라는 질문 유지; 일반 switching 신규성 주장은 제외 |
| 2–3 문헌·가정 비교 | 직접 선행 지정 구간, 상태 접근 가능성·문장 표현의 경쟁 설명 보완 |
| 4–5 질문·closest work | 좁은 평가 질문 유지; 같은 조건의 신규성은 잠정이며 전 분야 부재 주장 안 함 |
| 6 주장–증거 | 공통 입력/출력·규칙 대안·분모·결과별 해석 계약 추가 |
| 7 저비용 검사 | 시간 의미의 수작업 반례 검수 완료. 실제 정책 비교는 미실행 |
| 8 외부 비판·결정 | 검토 질문 준비; 외부 피드백 미수신. 탐색 유지·효과 미확인 |

이번에 보완한 것은 가까운 선행의 경계, 단순 규칙 대안, renderer/입력 계약, 시간 의미 검수, 분모·오류 분류와 결과별 판단이다. GPU가 없어 못 하는 모든 일을 문서 작업으로 대체한 것은 아니다. 현재 후보는 **탐색 유지 / 효과·독립 논문 가치 미확인**이다.

다음 native 단계는 기존 R8 IO 확인이다. 그 후에만 같은 상태 복원·시간별 observer·원자/복합 지시 능력을 검증한다. H/S model revision·parser·실제 tolerance·후속 trial/split은 해당 비교 실행 전에 정할 항목이며 R8의 선행 필수 조건으로 소급하지 않는다.

외부 연구자에게 전달할 질문은 (1) 이 비교가 Hi Robot·SIMPLER-IN에 무엇을 더 알려주는가, (2) 제약을 무시해도 통과하는 사례를 어떻게 해석해야 하는가, (3) 원자 작업/oracle 대조가 구별하지 못하는 설명은 무엇인가다. **질문 작성만 완료했고 실제 독립 피드백은 미수신**이다. 이는 작은 IO 확인의 blocker가 아니며 본격 기여 판단 때 보완한다.

문서 검증: generator 구문·재생성, `git diff --check`, repository audit 통과(errors 0 / warnings 0). Registry·tier·active/history tracker를 포함한 canonical 파일 8개의 SHA-256을 보존했다. 이 검사는 정책·의미 updater의 실행 검증이 아니다.

<a id="mobile-policy-transfer"></a>

## 모바일 조작 정책 교체: GPU 확보 전 buildup 보완

- 작성: 2026-10-31 KST / 비실험 검토 완료, **1개 dev 실행 탐색 유지·후속 분할 설계 수정**.
- 대상: [연구 개요](../research_topics/mobile_policy_transfer/내용/README.md#overview), [기존 H3 비교 초안](../research_topics/mobile_policy_transfer/내용/README.md#design-history), [실행 준비](../research_topics/mobile_policy_transfer/재현%20방법/README.md#execution).
- 문헌 지정 구간·공개 JSON의 identity/annotation을 검토했다. Scene JSON은 메모리에서 읽어 metadata와 hash만 요약했고 원본을 저장·렌더링·복원하지 않았다. Simulator/model/Docker probe·패키지 설치·PDF 다운로드는 없었다. [출처와 10개 레코드](../sources/pre_gpu_buildup_review_2026-10-31.json).

### 1. 선행 대비 주장과 baseline 범위

[Mobi-π §3.1–4](https://arxiv.org/html/2505.23692v1)는 base pose에 따른 정책 성능과 policy-aware 위치 선택을 이미 다루며, 초기 시연 영상·scene map·camera geometry 등의 정보 조건을 둔다. [MoTo, CoRL 2025](https://proceedings.mlr.press/v305/wu25c.html)는 조작을 고려한 docking을 다룬다. [Semantic Handoff §IV-D, V-B/C](https://arxiv.org/html/2607.06256v1)는 이동 후 다음 skill 준비 실패와 readiness 검사까지 논의한다. 따라서 **도착 성공이 조작 성공을 보장하지 않는다는 관찰 자체**나 새로운 readiness predicate만으로 신규성을 주장하지 않는다.

남길 질문은 **동일 navigator·유한 종료 조건 집합에서 정책 묶음을 교체할 때, 기존 선택을 재사용하는 손실과 제한된 재선택의 가치를 어떻게 판단하는가**다. 기존 3개 거리의 고정 기준선은 이 작은 진단의 대안이며 최강의 geometry/IK/navigation baseline을 대표하지 않는다. 새로운 docking 방법을 제안하거나 SOTA 효용을 주장하려면 Mobi-π/MoTo와 정보·행동·예산 조건을 맞춘 추가 비교가 필요하다. 이를 현재 1개 dev IO에 요구하지 않는다.

### 2. GPU 없이 새로 확인한 데이터 제약

고정 dataset revision `0be968d3b61406ec366e1bcf7f50a9aa36bbc56f`의 radio 평가 목록과 **10개 state manifest + 10개 skill-0 scene JSON**을 읽었다. [평가 목록](https://huggingface.co/datasets/mafangniu/Behavior-Skill/blob/0be968d3b61406ec366e1bcf7f50a9aa36bbc56f/eval_episodes.json), [첫 manifest](https://huggingface.co/datasets/mafangniu/Behavior-Skill/blob/0be968d3b61406ec366e1bcf7f50a9aa36bbc56f/skill_init_states/task-0000/episode_00000010/state_manifest.json), [첫 scene](https://huggingface.co/datasets/mafangniu/Behavior-Skill/blob/0be968d3b61406ec366e1bcf7f50a9aa36bbc56f/skill_init_states/task-0000/episode_00000010/skill_00_scene.json). 전체 URL/hash는 source ledger에 있다.

| 확인 항목 | 실제 metadata 결과 | 설계에 반영 |
|---|---|---|
| Source trajectory | `input_hdf5` 경로 10개는 서로 다름 | stable key는 release + task + source path. 파일 내부 `episode_id`만 쓰지 않음 |
| Local episode ID | 10개 모두 `episode_id=0` | 이를 global identity로 사용하면 서로 다른 source가 잘못 합쳐짐 |
| Scene model | 10개 모두 `house_double_floor_lower` | 10개 독립 scene이라고 세지 않음 |
| Scene instance | 10개 모두 `house_double_floor_lower_task_turning_on_radio_0_0_template` | 기존 2/4/4는 scene-instance-disjoint holdout이 될 수 없음 |
| Object binding | 모두 `radio_89`와 `coffee_table_koagbh_0` | 같은 의미 대상/배치 template 수준의 진단으로 제한 |
| Scene file hash | 10개 모두 서로 다름 | 서로 다른 파일이지 독립 scene 또는 물리적으로 다른 초기 상태라는 증거는 아님 |
| Outer version | OmniGibson 3.7.2 / BDDL 3.7.0 | 이전 runtime 계획과 metadata 연결. 실제 로딩 호환성은 미검증 |

**기존 2 dev / 4 calibration / 4 test를 독립 instance 평가로 쓰는 계획은 수정해야 한다.** 서로 다른 HDF5 경로와 서로 다른 scene-file hash만으로 이를 해결했다고 표시하지 않는다. 물리 상태의 중복·독립성·공개 checkpoint의 학습 포함 여부까지 확인한 것은 아니다.

우선 `00000010`의 1개 dev는 IO·실제 도착·정지·상태 복원 확인에 그대로 사용한다. **그 다음 최초 비교의 범위는 동일 scene template 안의 탐색적 episode 비교로 선택한다.** 아래 source 배분은 현재 metadata로 작성한 역할 명세이며 독립 instance holdout이 아니다. 새로운 scene/instance로의 일반화는 추가 group 확보 뒤 별도 평가로 다룬다. 자원 없이 동일 목록을 재집계할 TODO는 만들지 않는다.

| 역할 | Source episode | 허용 해석 |
|---|---|---|
| 개발·실행 확인 | 00000010, 00000250 | 관측/제어·candidate 도달·복원 점검 |
| 조건 선택 | 00000470, 00000700, 00000940, 00001250 | 같은 template에서 A/B별 설정 선택; B pickup 최대 12회 |
| 선택 후 기술적 평가 | 00001590, 00001960, 00002600, 00003000 | 선택에 쓰지 않은 source 경로의 결과. 새로운 scene/instance·미학습 상태 일반화 아님 |

기존 2/4/4의 ID 배분은 유지하되 **주장의 모집단과 평가 역할을 수정**했다. Native에서 초기 물리 상태 중복과 RNG/복원 조건을 확인해 같은 초기 상태가 반복된 경우 반복 수로 표시한다. 완전히 겹치는 상태만 남으면 상태 일반화 비교를 하지 않고 해당 상태의 반복 실행 진단으로 더 좁힌다. 성공 결과를 보고 새로운 ID를 골라 넣지 않는다. 이 계획은 P0 통과 뒤 검토할 연구 설계이며 110 phase의 자동 실행 승인이 아니다.

Navigation annotation 종료와 pickup annotation 시작의 차이는 다음과 같다.

| Episode | Navigation end frame | Pickup start frame | 차이 |
|---|---:|---:|---:|
| 00000010 | 265 | 265 | 0 |
| 00000250 | 848 | 848 | 0 |
| 00000470 | 996 | 997 | 1 |
| 00000700 | 449 | 832 | 383 |
| 00000940 | 927 | 1532 | 605 |
| 00001250 | 634 | 635 | 1 |
| 00001590 | 340 | 340 | 0 |
| 00001960 | 574 | 588 | 14 |
| 00002600 | 402 | 402 | 0 |
| 00003000 | 460 | 461 | 1 |

6/10에 비영 차이가 있고 최대는 605 frame이다. 이는 **annotation 경계 차이**이며 누락 구간의 실제 행동·시간·데이터 오류를 확정하지 않는다. Frame endpoint convention도 추가 확인 대상이다. Demo pickup snapshot이 navigation 직후 상태와 같다고 가정하면 안 된다는 근거다. 실제 navigator가 만든 상태에서 공통 정지를 수행하는 기존 설계를 유지한다. Dataset frame을 현재 제어 tick이나 wall time으로 바꿔 계산하지 않는다.

### 3. 일반적인 정책 성능 차이와 종료 조건 효과를 분리

정책 A/B와 종료 조건 3개를 교차한 결과를 모두 남긴다. 최종 선택된 설정의 평균만 보고하면 B의 기본 능력 저하와 설정 전이 손실을 구별하기 어렵다. 기존 pilot 초안은 이미 A/B×3을 포함하므로 새로운 rollout을 추가하지 않고 분석 계약을 보완할 수 있다. P0는 여전히 한 dev의 최소 실행뿐이다.

`Y_p,i(k)`는 원본 사례 i에서 고정 navigator가 조건 k에 도달하고 정책 p가 시간 내 집기에 성공했는지다. 도달 실패는 0, 인프라 오류는 별도 결측/기술 오류로 기록한다. `k_A`, `k_B`는 각 정책의 calibration으로 선택한 설정이며 test에서 고르지 않는다. 주 비교는 같은 B의 `Y_B(k_B)−Y_B(k_A)`이고 고정 거리와의 차이도 함께 보고한다. **다른 정책끼리의 평균 차이 자체는 전이 손실의 추정량이 아니다.**

설정 k₁/k₂에 대한 `(Y_B(k₁)−Y_B(k₂))−(Y_A(k₁)−Y_A(k₂))`는 설정 민감도가 정책별로 다른지 보는 기술적 요약이다. 새로운 이론·순수한 geometry 인과 효과로 주장하지 않는다. 표본이 작고 같은 template이므로 하나의 대비나 순위 교차만으로 강한 일반화를 하지 않는다.

| 관측될 수 있는 결과 | 해석·다음 판단 |
|---|---|
| B가 모든 거리와 reference에서 실패 | 우선 B의 능력/loader/controller를 점검. 종료 조건 전이 실패로 단정하지 않음 |
| A/B 모두 같은 설정이 좋고 B 재선택의 이득이 작음 | 공통 조건 재사용 가능성을 이 범위에서 보고. 무차이를 동등성으로 바꾸지 않음 |
| Calibration 선택은 다르지만 평가에서 재선택 이득이 없음 | 적은 calibration의 선택 잡음 가능성. 새로운 정책 의존성의 증거로 삼지 않음 |
| B 재선택보다 고정 0.9 m가 충분 | 단순 설정의 효용을 보고하고 selector/RL 필요성을 낮춤 |
| B 재선택의 이득과 정책별 민감도 차이가 보임 | 새 사례/group에서 확인할 후속 질문. 한 template 결과로 보편적 전이 법칙을 주장하지 않음 |

### 4. 후보·예산·오류의 보완 계약

거리 0.6/0.9/1.2 m는 **같은 navigator의 정지 시점 조건**이다. 모든 설정에서 이미 가까운 상태이거나 실제 도착 pose가 거의 같으면 세 개의 다른 개입이 아니다. 도달 tick, base–target 거리/yaw, `zero_travel`, 공통 정지 전후 state를 기록하고 dev에서 설정의 구별 가능성을 확인한다. Test 결과를 보고 후보 거리를 새로 고르지 않는다. 정지 동작이 바꾸는 접촉·arm 자세도 개입에 포함되므로 시야·거리만의 효과라고 주장하지 않는다.

모든 정책 branch는 같은 초기 state와 공통 navigator 결과를 사용한다. 동일 seed라는 문구로 controller/grasp/physics/queue 상태 복원 검증을 대체하지 않는다. A/B checkpoint와 각 normalizer를 함께 바꾸므로 이는 배포 묶음의 비교이며 데이터 규모·architecture 단독 효과가 아니다. Navigator도 A라는 사실을 기록하며 다른 navigator로의 전이를 주장하지 않는다.

`B-select ≤12회`는 B의 추가 calibration pickup 상한이다. A의 사전 선택, nav 생성, 정지, reference, 평가, 실패 실행, setup/복원·추론 비용은 별도로 기록한다. 같은 run을 재사용했으면 실제 계산 비용과 배포 시 물리 비용을 구분한다. 제한된 평가로 setting을 고르는 것이므로 validation은 무료가 아니다. 동일 예산의 강한 geometry 최적화보다 낫다는 주장은 현재 범위에 없다.

결과표 열은 `source key / scene-template key / 정책·normalizer / 조건 / 도달 여부·tick / 실제 정지 pose / pickup 성공 / 오른손 준수 / 기술 오류 / 물리 tick / 추론 횟수·wall time`으로 정한다. Summary에는 정책×조건별 raw count, 선택 설정, B 재사용/고정/재선택의 paired 차이와 비용을 넣는다. 오른손 지시와 BDDL의 일반 grasp predicate는 따로 보고한다.

원래 4개 test episode를 네 독립 scene이라고 하거나, 동일 scene의 seed·frame을 표본 수로 늘리지 않는다. 현재 metadata에는 scene-template group이 1개이므로 scene-level bootstrap 신뢰구간을 만들 근거가 없다. 첫 탐색은 raw paired 결과와 범위를 보고하고, 확증에 필요한 독립 group·반복·불확실성 설계는 그 다음에 정한다. 기술 오류를 제외한 성공률을 전체 시도 성공률로 표기하지 않는다.

### 5. GPU 전 완료와 남은 것

| 가이드 단계 | 이번 재점검 결과 |
|---|---|
| 0–1 공백·중요성 | 정책 교체 뒤 설정 재사용/재검증의 의사결정 질문 유지 |
| 2–3 문헌·가정 비교 | Policy mobilization·readiness 선행과 정보 조건 대조, 10개 source identity 확인 |
| 4–5 질문·closest work | 일반 handoff 실패를 신규성으로 세지 않음; 비용을 포함한 좁은 비교로 한정 |
| 6 주장–증거 | 같은 B의 설정 비교·정책×조건 표·선택 잡음·비용·기술 오류 계약 보완 |
| 7 저비용 검사 | 실제 공개 metadata로 단일 template·annotation 경계 차이 확인, split 해석 수정 |
| 8 외부 비판·결정 | 질문 준비·피드백 미수신. 한 dev 탐색 유지, 후속 비교를 동일-template 탐색으로 수정 |

이번에 선행 대비 질문, 공정 비교의 estimand, 비용·오류·단순 대안, 데이터 identity/분할의 문제를 보완했다. **기존 “split/instance 미확인” 중 metadata 수준은 확인했으며, 결과는 한 template이므로 설계 수정이다.** 같은 metadata 검사를 다음 TODO로 반복하지 않는다. Scene state의 실제 복원·물리적 중복, 두 정책의 능력과 native 효과는 남아 있다.

1개 dev의 최소 IO는 계속할 가치가 있다. 이미지·transport·상태 복원 adapter와 자원이 갖춰지면 기존 범위로 검증한다. 후속 110-phase 초안은 자동 실행하지 않으며, 위 동일-template 역할 명세에 실제 state/seed 검증을 더한 뒤 판단한다. 이 결과는 주제 NO-GO도, GPU만 남았다는 뜻도 아니다.

외부 연구자 검토 질문은 (1) 기존 policy mobilization 지식에 재검증 비용이 무엇을 추가하는가, (2) 같은 template·같은 계열 두 정책에서 얻는 결과가 어떤 결정을 바꾸는가, (3) calibration 잡음과 정책 의존성을 무엇으로 구별할 것인가다. 질문만 준비했으며 독립 피드백은 미수신이다. 외부 메시지는 보내지 않았다.

문서 검증: source 요약의 10개 경로·단일 template·6개 비영 frame 차이·역할 배분의 정합성과 기존 P0 실행 예산 보존을 확인했다. Generator 구문·재생성, `git diff --check`, repository audit 통과(errors 0 / warnings 0). Registry·tier·읽기 기록은 변경하지 않았다. Scene 렌더링·복원·정책 실행 검사는 아니다.

<a id="remaining-work-review"></a>

## 후속 검토: 실험 없이 남은 작업의 완료 범위

- 작업: `PRE-GPU-FOLLOWUP` / 2026-10-31.
- 결론: 추가 비실험 작업이 있었다. **정답/자동 지시의 표현 불일치, 수정 경계 채점, 선택 불능·결측 처리**를 보완했다. 이 확인만으로 후보를 새 주제로 교체하지 않는다.
- 범위: 기존 문헌·설계 감사, 지정 HTML 구간 재확인, 영문 발화·의미 정답 작성, 분석 규칙 명세. Model·simulator·parser 실행, Docker probe, dependency 설치, PDF 저장은 하지 않았다. 기존 10개 scene metadata도 다시 수집하지 않았다.

### 1. 잔여 항목 감사와 문헌 확인의 종료점

| 항목 | 확인 결과 | 이번 처리 |
|---|---|---|
| 가까운 선행·단순 baseline | 두 후보 모두 이미 비교가 있음 | 실제 미확정 주장과 비교 계약만 다시 대조 |
| 지시 수정의 영문 입력 | 기존에는 완성된 현재 지시만 영어였고 최초/수정 발화는 미고정 | 8개 사례의 영문 발화·수정 전후 정답을 [SEMANTIC_CASES.json](../research_topics/instruction_revision/재현%20방법/SEMANTIC_CASES.json)으로 작성 |
| 정답 지시와 자동 renderer | R4/R5 정답에는 취소·허용 문구가 있지만 자동 renderer는 활성 조건만 사용 | 양쪽 모두 활성 목표·제약만 출력하도록 정답 후보 수정; 취소 이력은 감사 필드로 분리 |
| 시간 경계·평가 종료 | 철회 전 위반 보존 원칙은 있으나 같은 tick의 action/post-state 소유가 모호 | 아래 action별 제약 귀속과 공통 종료 정의 명세 |
| 모바일 선택 불능·기술적 결측 | 기존 동률 규칙은 있지만 all-zero/불완전 calibration의 해석은 미정 | 아래 선택 보류·고정 기준선 fallback·결측 규칙 추가 |
| 모바일 작은 표본과 비용 | 한 template·작은 표본 한계는 확인됨 | 4개 평가의 25%p 해상도, 반복 배포 규모별 비용 판단 한계 명시 |
| 물리 능력·복원·허용 오차·runtime | 정적 문헌으로 확인 불가 | Native 검증 대상으로 유지. 임의 수치/성공을 채우지 않음 |
| 외부 연구자 피드백 | 질문 초안은 이미 있음 | 실제 수신은 미완료. 사용자 지시 없이 메시지를 보내지 않음 |

이번 문헌 재확인은 [ExecVLA v2 §3–4](https://arxiv.org/html/2603.17524v2)의 고정 목표 아래 수행 제약과 goal/kinematics 평가, [SwitchVLA v1 §3–4·Limitations](https://arxiv.org/html/2506.03574v1)의 접촉 단계별 전환·rollback을 구별하는 데 사용했다. 이들은 이미 registry에 있으며 일반 제약 준수·전환·중간 상태 평가를 새 공백으로 만들 근거가 아니다. 검토 구간에서 선택적 제약 수정과 동일 renderer의 전체 재명시 비교 결과까지 확인한 것은 아니므로 좁은 질문은 잠정 유지한다. ExecVLA HTML에는 KineVLA라는 본문 명칭도 남아 있어 수치·버전 간 동일성을 새로 확정하지 않았다.

모바일 조작은 [Mobi-π](https://proceedings.mlr.press/v305/yang25b.html)와 [MoTo](https://proceedings.mlr.press/v305/wu25c.html)의 CoRL 2025 공식 범위를 재확인했다. [Look Before You Act / ActiveAlign v1 §IV-B·V](https://arxiv.org/html/2610.23378v1)는 앞선 관측 행동과 이후 정책의 학습 분포를 맞추는 연구이며, 여러 backbone·matched-state/data 대조도 이미 있다. **이 논문은 H1에서 이미 검토했으므로 새로 발견한 공백으로 세지 않는다.** 성공 replay로 학습 endpoint를 선별한 adaptation과 frozen checkpoint 교체 후 기존 종료 설정의 재사용 비용은 다른 비교다. 이름이 같은 `arXiv:2610.36859`의 calibration 연구와 혼동하지 않는다.

CounterAlign·RoboFollow의 공식 OpenReview 재접근은 이번 도구에서 실패했다. 기존 registry의 확인 이력은 유지하되 이번에 새 본문 검토를 완료했다고 표시하지 않는다. 이 제한과 검색 범위는 [공유 source ledger의 followup](../sources/pre_gpu_buildup_review_2026-10-31.json)에 남긴다. 전수 문헌 조사·신규성 보장은 아니다. 이미 검토한 선행을 반복 집계할 후속 TODO는 만들지 않는다.

### 2. 지시 수정: 의미 입력과 공정한 출력

[8개 영문 사례 명세](../research_topics/instruction_revision/재현%20방법/SEMANTIC_CASES.json)는 `initial_utterance`, `revision_utterance`, 수정 직전/직후의 활성 목표·제약, 취소·철회 이력, 정답 prompt를 담는다. 수작업 정답이며 실제 모델/정책의 실패 사례가 아니다. R6의 수정 직전 정답은 병→랙이 실제 달성된 prefix를 전제로 하며 최초 발화 직후 상태와 구별한다. 실제 object binding과 물리적 충족 여부는 native에서 확인한다.

R4의 현재 정답은 `Put the wine bottle on the rack.`, R5는 `Put the bowl on the plate.`로 정리했다. “그릇 작업 취소”나 “병 이동 허용”을 저수준 prompt에 다시 붙이지 않는다. 상위 의미 정답에서는 취소·철회를 계속 채점하므로 해당 정보가 사라진 것은 아니다. Renderer는 정답·자동 재명시·예측 상태 갱신·규칙 대안에 동일하게 적용한다. 자유 문장 덧붙이기는 별도 표현 조건이지 기본 비교가 아니다. 이 변경은 기존 자동 renderer 계약과 oracle 후보를 맞춘 것이며 renderer 구현/검증 완료는 아니다.

현재 전체 이력 재명시와 상태 갱신 양쪽에 같은 대화 이력을 허용하므로, 상태 갱신의 이득이 관찰돼도 곧바로 **문맥 압축이나 token 절약 효과**라고 부르지 않는다. 후자는 같은 정보·실제 token 비용을 따로 맞춰 검증할 다른 질문이다. 상태 갱신에는 자신이 예측한 이전 상태만 제공하고, 정답 상태와 case ID는 evaluator 전용으로 남긴다.

`original position` 같은 과거 기준은 evaluator가 보유한 pose와 다르다. 현 VLA가 그 수치나 최초 영상을 추가로 받는 것은 아니며, 과거 위치 복원 능력을 전제하지 않는다. 최초 비교에서는 수정 전 제약이 충족된 prefix와 별도 전체 임무 결과를 함께 보고한다. 과거 reference observation을 추가하는 확장은 양쪽에 같은 입력을 주는 별도 조건이다. 영문 문자열의 tokenizer 길이·잘림 여부는 Docker에서 실제 tokenizer를 사용할 때 확인한다.

### 3. 지시 수정: action 경계와 종료를 구체화

한 기록 단위는 `(t, s_t, a_t, s_{t+1}, a_t에 적용된 제약)`이다. 수정 이벤트 `τ`는 이전 action의 post-state `s_τ`를 기록·채점한 뒤, 새 action `a_τ` 직전에 적용한다. `[t0,τ)`에 유효한 제약은 그 구간의 **action 및 각 post-state**를 검사한다. 따라서 `a_{τ−1}`이 물체를 움직였으면 `s_τ`의 이동은 철회 전 위반이다. 새 금지의 기준 pose는 `s_τ`이며 과거 action에는 소급하지 않는다.

수작업 논리 대조에서 다음 정답을 명시했다. 마지막 이전 action의 이동 후 즉시 철회해도 과거 위반은 남는다. 수정 직전 이미 이동한 물체에 새 금지를 추가하면 새 제약만으로는 과거 위반이 아니다. 한때 움직였다가 돌아와도 누적 위반은 남는다. R5에서 병을 움직이지 않아도 의미 실패가 아니다. 이러한 논리 대조는 구현된 observer의 테스트가 아니다.

후속 R1/R4 비교는 모든 arm에서 같은 수정 후 horizon `H`를 사용하고, goal first-hit로 조기 종료하지 않는 계약으로 둔다. Primary goal은 공통 끝 상태, 제약은 해당 action 구간의 누적 위반이다. First-hit 시각은 secondary로 보존한다. 실패한 native step·관측 결손을 “위반 없음”으로 채우지 않는다. Parse 오류는 의미/임무 실패, simulator/transport 예외는 기술적 결측으로 구별한다. Pose norm·quaternion 부호 동치·단위·관측 주기·허용 오차는 observer 구현 명세에 포함해야 하며, 샘플링한 상태만으로 연속 시간 전체의 안전을 주장하지 않는다.

`H`와 물리적 tolerance의 숫자는 dev의 기본 능력·정지 drift·실제 단위를 확인한 뒤 **비교 결과를 보기 전에** 고정한다. 지금 임의 숫자를 채우는 것은 보완이 아니다. R8의 기존 최대 7 policy action·2 inference·17 control step IO는 이 평가 계약과 별개이며 변경하지 않는다.

### 4. 모바일 조작: 선택이 불가능한 경우와 비용 해석

기존 H3의 정상 선택 규칙(성공률 최대 → 총 물리 tick 최소 → `0.9, 0.6, 1.2` 순서)은 유지한다. 다음 규칙은 **후속 pilot 설계 보완**이며 현재 한 dev P0를 확대하지 않는다.

| Calibration 결과 | 선택·보고 규칙 |
|---|---|
| 모든 예정 사례/설정의 유효 결과가 있고 성공이 1건 이상 | 기존 선택 규칙 사용. 작은 표본의 선택 잡음 가능성은 유지 |
| 모든 유효 결과가 0 | `NO_OBSERVED_SUCCESS`로 선택 근거 부족을 표시. 운용 fallback은 사전 고정 0.9 m. 정책의 절대 불능으로 단정하지 않음 |
| Simulator/transport 등 기술적 결측이 하나라도 남음 | `INCOMPLETE_CALIBRATION`. 누락된 arm을 빼고 성공률을 비교하지 않으며 data-driven 최적 설정을 확정하지 않음. 필요시 같은 고정 0.9 m fallback을 별도 표시 |
| Navigation 미도달/timeout | 기술 결측과 달리 원래 primary 정의의 실패 0. Pickup 미실행을 성공 분모에서 제거하지 않음 |
| A가 선택 불능 | fallback과 B 조건 비교는 가능하지만 **A에 맞춰 선택한 조건의 전이 손실**로 해석하지 않음 |
| B가 선택 불능 또는 `k_A=k_B` | 재선택 효과를 만들어내지 않음. 전체 정책×조건 결과·고정 대안·비용을 보존 |

이 규칙은 test 성공을 보고 재선택하거나 calibration 사례를 교체하는 것을 허용하지 않는다. 기술적 재실행을 허용하려면 같은 case/seed·횟수 상한·첫 실패 보존 규칙을 실행 전에 정한다. 현재 준비에는 자동 retry/sweep를 추가하지 않았다.

기존 조건 선택 4개·선택 후 평가 4개에서 각 episode당 이진 결과 한 개를 사용하면, 성공률 및 paired 평균 차이의 최소 간격은 **1/4=25%p**다. 따라서 작은 개선·동등성·실용적 차이 없음의 확증에는 부족하다. 이것은 기존 설계의 산술적 해상도이며 실험 결과·power 계산이 아니다. 같은 template의 seed/frame을 늘려 독립 scene 수를 부풀리지 않는다. 이 작은 비교는 큰 실패 양상과 다음 실험의 필요성을 판단하는 단계로 둔다.

재선택의 실용 가치는 이득뿐 아니라 이후 반복 사용 횟수에도 의존한다. 가정한 향후 작업 수 `M`과 성공확률 차이 `Δp`라면 추가 성공 기대량의 표현은 `M·Δp`지만, 현재 `Δp`는 미측정이고 같은 환경 반복이라는 가정도 필요하다. Calibration의 robot time·실패 비용·추론 시간을 별도 축으로 보고하며, 12회라는 상한만으로 비용이 작다고 결론짓지 않는다. Task 성공의 가치를 임의의 GPU 시간으로 환산하거나 작은 pilot의 점추정으로 손익분기점을 확정하지 않는다.

### 5. 이번 종료 판단과 남은 작업

**이번에 식별한 독립적인 비실험 보완은 완료했다.** 두 주제는 작은 native 검증을 이어갈 탐색 후보로 유지한다. 추가 문헌 반복·수작업 사례 수 증가만으로 효과나 논문 가치를 확정할 수 없어 새 문서 queue를 늘리지 않는다. 이번에 추가 작업이 있었으므로 사용자의 조건에 따라 새 주제 탐색으로 전환하지 않았다.

| 남은 항목 | 필요한 조건 |
|---|---|
| 지시 수정 R8 IO | 호환 로컬 Docker에서 image·asset·CUDA/EGL·두 query·queue 전환 확인 |
| 지시 수정 R1/R4 | 실제 prefix/정답 지시 능력, 시간별 observer·복원, dev에서 horizon/tolerance 고정. 이후에만 상위 updater/parser 구현·비교 |
| 모바일 조작 P0 | Sim/server image·transport·state adapter 구현과 native 확인. 그 뒤 같은 상태에서 A/B IO 및 실제 도착·정지·분기 |
| 모바일 후속 비교 | 실제 state 중복·RNG, policy×조건 결과·선택 불능 규칙·cost. 기존 단일-template 제한 유지 |
| 신규성·출판 수준 가치 | 관측 결과와 가까운 선행의 비교, 범위 확장 필요성·독립 피드백 검토. 현재 미확인 |

외부 피드백 수신과 native 환경에서의 구현·검증은 남아 있다. “비실험 보완 완료”는 이 항목까지 완료했다는 뜻이나 GPU만 있으면 즉시 성능 비교가 된다는 뜻이 아니다. R8 IO와 모바일 P0의 기존 범위는 유지한다. 문서 검증 결과는 공유 source ledger에 기록한다.
