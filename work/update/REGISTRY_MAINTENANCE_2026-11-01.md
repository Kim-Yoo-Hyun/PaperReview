# Registry 보완·중복 정리 — 2026-11-01

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- Task: **REG-R6**
- 범위: 최근 연구 검토의 미등록 직접 선행 보완, SET 보고서 병합, 활성 인계·생성 view 정합성. 전체 1,080편의 최신 게재 상태를 전수 재조사한 작업은 아니다.
- [등록 입력](../sources/registry_admissions_2026-11-01.json) · [삭제/병합·검증 ledger](../sources/registry_maintenance_2026-11-01.json)
- 현재 세 후보의 판단·비실험 완료 경계는 [PRE-GPU-3](./THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md)를 유지한다. 이번에는 Docker/모델/실험·설치·payload 다운로드·commit/push를 하지 않았다.

## Registry 반영

| 논문 | 확인한 상태·근거 | 이번 역할 |
|---|---|---|
| [ClevrSkills](../../2024/NeurIPS/2024_NeurIPS_ClevrSkills-Compositional-Language-And-Visual-Reasoning-in/01_overview.md) / pr-1078 | [NeurIPS 2024 D&B 공식](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) · [공식 code](https://github.com/Qualcomm-AI-research/ClevrSkills) | 조합 task·언어/시각 prompt·평가 predicate의 NEXT benchmark |
| [Spa-Bench](../../2026/arXiv/2026_arXiv_Spa-Bench-A-Real-Robot-Benchmark-for-Spatial-Grounding-in/01_overview.md) / pr-1079 | [arXiv 2026](https://arxiv.org/abs/2610.12696) · [저자 project](https://justintiensmith.github.io/Spa-Bench/) | Counting·matched 직접 지시의 NEXT 비교 기준 |
| [Diagnosing Compositional Generalization](../../2026/CoRL/2026_CoRL_Diagnosing-Compositional-Generalization-in-Sequential-Robo/01_overview.md) / pr-1080 | [arXiv v2](https://arxiv.org/abs/2607.29687) · [저자 code](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot) | 데이터 coverage·단계 분해의 NEXT 선행 |

마지막 논문의 저자 표기 CoRL 2026 Spotlight는 공식 proceedings/program으로 독립 확인하지 못해 arXiv/unknown을 유지했다. Robotics Spa-Bench와 동명의 ICLR 2025 smartphone-agent benchmark를 혼동하지 않았다. ClevrSkills는 공식 title의 대소문자와 arXiv 표현 차이를 정규화해 같은 논문으로 확인했다.

제목·고유 구절·arXiv/DOI를 기존 manifest·PAPER·tiers와 대조했고 등록 dry-run은 **3편 승인·제목/identifier 충돌 0**이었다. 신규 paper folder 3개와 표준 노트 15개를 생성했다. 모두 **ABSTRACT_CHECKED / UNREAD**이며 이전 연구 단계의 부분 본문/code 검토를 사용자 정독으로 승격하지 않는다. CORE는 유지하고 NEXT만 3편 늘렸다.

- 전체 **1,077 → 1,080편**.
- CORE **47**, NEXT **302 → 305**, REFERENCE **486**, ARCHIVE **242**.
- 집중 읽기 **349 → 352**, 비활성 이력 **47**, 표준 노트 **5,385 → 5,400**.
- ClevrSkills·Robotics Spa-Bench의 검색용 benchmark vocabulary를 보완했다. 자동 연결은 여전히 `cue_only`이며 실제 split/role의 근거가 아니다.

## 병합·삭제와 보존

| 정리 대상 | 남긴 위치·판단 |
|---|---|
| SET 최초 탐색·source 심사·비실험 보완 3개 보고서 | [문헌·source·설계 통합 검토](../research_topics/retired/README.md#object_set) 1개. Code permalink·의미 사례·서로 다른 predicate·반증 규칙·과거 미선정 이유 보존 |
| SET 최초 P0 준비·재점검 2개 보고서 | [실행 준비·재점검 통합 기록](../research_topics/retired/README.md#object_set) 1개. 최초 GPU exit 125와 후속 check exit 3, source 고정/adapter 차이와 검사 범위 구분 |
| Python bytecode 2개 | 재생성 가능한 cache만 삭제. 의존성·환경 패키지 삭제는 하지 않음 |
| TODO·research 안내의 반복 완료 설명 | 최근 완료·현재 세 후보·실제 재개 조건으로 축약. 우선순위는 REVISION 우선 유지 |
| 내용이 동일한 과거 Docker version JSON 2개 | 서로 다른 실험의 증거이므로 각각 보존 |
| 논문·원시 실험 결과·source ledger·실행 packet·읽기 기록 | 삭제하지 않음. 미사용처럼 보인다는 이유만으로 역사적 근거를 제거하지 않음 |

총 **중복 보고서 3개 삭제(5→2 통합), cache 2개 삭제**다. 원래 경로·SHA-256·대체 위치는 ledger에 있다. 관련 Markdown/JSON의 현행 참조를 교체했으며 source ledger의 공개 URL·commit·hash는 바꾸지 않았다. 합쳐진 문서의 당시 통계는 역사로 표시했다.

<a id="completed-handoff"></a>

## TODO에서 줄인 완료 이력

| 작업 | 남긴 핵심 결과·근거 |
|---|---|
| REG-R5 / 10-31 | [이전 registry 정리](./REGISTRY_MAINTENANCE_2026-10-31.md): 직접 선행 3편, 이전 보고서 병합과 Linux 경로 정합성; 당시 1,077편 |
| PRE-GPU-FOLLOWUP / 10-31 | [두 후보 비실험 검토](./PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#remaining-work-review): 의미/observer·선택 불능·분모/비용, 실제 효과 미확인 |
| GAP-REVISION-P0 / 10-31 | [준비 결과](../research_topics/instruction_revision/재현%20방법/README.md#preparation-history): R8 IO packet 작성, native 0·image 미빌드 |
| GAP-NEXT-SCOUT / GAP-SET-R1 / GAP-SET-N1 / 11-01 | [통합 검토](../research_topics/retired/README.md#object_set): category-first·자유 subset·참조/종료 집합·292개 문서 집합 정합성; 정책 효과 아님 |
| GAP-SET-P0-PREP / GAP-SET-P0-R1 / 11-01 | [통합 준비 기록](../research_topics/retired/README.md#object_set): 미빌드 packet·native 0, 이후 오래된 image 거부/IK·결과 분류 등 준비 검사 10개 |
| PRE-GPU-3 / 11-01 | [세 후보 최종 비실험 보완](./THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md): 문헌·논리·설계 완료; 구현·교정·효과·독립 피드백 미완료 |

## 검증

- Registry audit **오류 0·경고 0**. Paper 1,080·표준 노트 5,400·Markdown 5,604·링크 11,331, generated index 1,080행·resource 560개를 확인했다.
- 등록 dry-run/apply, generator 임시 compile·tier 생성, priority-only reconcile, catalog/view dry-run/apply, `git diff --check`를 통과했다. Catalog는 benchmark 55·metric 29개이며 모두 기존 cue 경계를 유지한다.
- 문서 유지보수 6개·읽기 이력 보존 6개, **회귀 검사 총 12개 통과**. 표준 노트 5,400개의 C0/C1 제어문자 잔여는 0이다. 이는 의미 오류 전부의 부재를 뜻하지 않는다.
- 기존 **1,077개 manifest entry**, **5,385개 논문 노트**를 byte-equivalent/동일 SHA-256으로 보존했다. Active/history 합집합의 **396행 사용자 필드**가 모두 같고 신규 3행만 UNREAD·ABSTRACT_CHECKED로 추가했다.
- 기존 실험 파일의 변경·삭제는 없고 staged entry digest도 동일하다. 삭제는 위 3개 병합 원본과 2개 재생성 cache로 한정했다. Source ledger의 한 output 문서 경로만 현재 병합 위치로 연결했다.
- 연구 후보 3개의 판단·실행 예산·미구현 범위는 유지한다. Target image·native 효과·독립 외부 피드백을 새로 검증한 작업은 아니다.
