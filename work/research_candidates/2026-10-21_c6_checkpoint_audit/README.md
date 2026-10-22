# C6 buildup 결과: VLA RL checkpoint 선택의 평가 오류

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- 검토일: 2026-10-21 KST
- 단계: 문헌 충돌·공개 구현·데이터 식별 가능성 심사 완료. 정책 성능 실험 전.
- **판정: 현재 C6를 독립적인 신규 방법 연구로 채택하지 않는다(NO-GO). 평가 설계와 baseline은 후속 VLA+RL 연구에 재사용한다.**

사용자 요청에 따라 [C5 결과](../2026-10-21_c5_reset_audit/README.md)를 먼저 재검토했다. Reset/coverage의 일반 주장은 선행 연구와 겹치고, 남은 진단은 새로운 native VLA reset·학습 로그 수집이 필요하다. 이 전제를 바꾸는 근거가 없어 C5의 조건부 보류를 유지하고 C6로 진행했다. 이는 C5의 가능성이 영원히 없다는 판정이 아니라 **현재 추가 투자 우선순위**에 대한 결정이다.

## 왜 현재 C6를 채택하지 않는가

| 검토한 주장 | 판정 |
|---|---|
| 제한된 rollout으로 좋은 checkpoint를 선택한다 | A-OPS가 OPE와 online 평가를 결합해 policy selection을 이미 다룬다 |
| 적은 trial로 개선 여부를 검정하고 나쁜 정책을 배제한다 | STEP·N-SCORE가 sequential comparison, 오류 제어, 여러 정책 비교를 이미 다룬다 |
| World model 또는 offline score로 VLA checkpoint를 정렬한다 | dWorldEval·RACE와 직접 겹친다. 적용 대상이 RL checkpoint라는 사실만으로 부족하다 |
| RL이 학습에 쓰인 평가기의 약점을 이용한다 | 일반 원리는 reward overoptimization 연구에 있고, VLA world-model RL 사례도 World-VLA-Loop에 있다 |
| 독립 evaluator에서도 지속되는 VLA 고유의 실패 조건을 검증한다 | 경험적 질문은 가능하지만, 현재 차별화된 조건·연속 RL 로그·독립 평가가 확보되지 않았다 |

주요 근거: [A-OPS, NeurIPS 2021](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html), [STEP, RSS 2025](https://roboticsproceedings.org/rss21/p077.html), [N-SCORE, RSS 2026](https://roboticsproceedings.org/rss22/p076.html), [dWorldEval, ICML 2026](https://proceedings.mlr.press/v306/li26hi.html). RACE는 저자 페이지의 workshop 발표 표기이며 main-conference acceptance로 간주하지 않는다. 세부 범위와 반례는 [문헌 비교](./LITERATURE_REVIEW.md)에 둔다.

## 실제로 확인한 결과

- 문헌 **12편**을 대조했다. 관련 본문 구간 확인 10편, abstract/metadata 중심 2편이며 전편 정독·체계적 전수조사로 표시하지 않는다. [Source ledger](./SOURCE_AUDIT.json)
- Docker에서 **8개 공식 repository 주소**를 검사했다. 7개는 commit을 고정해 **26개 text source / 441,388 bytes**를 확보했고, `AbrarAnwar/seq-eval`은 HTTP 404였다. 패키지 설치·upstream 실행은 하지 않았다.
- RACE 공개 JSON **54,809 bytes**를 실제로 파싱했다. VLA 27행·Diffusion Policy 30행, 총 **57개의 checkpoint 집계 기록**이다. DP에는 성공 횟수/시행 수가 있으나 개별 trial의 순서·seed·초기 상태는 없다. VLA는 3 task × 9 checkpoint이며 이를 논문의 계획된 10개로 채워 넣지 않았다.
- A-OPS에는 cartpole용 sample 파일, N-SCORE에는 LBM·RL 비교 자료, SureSim에는 paired-data interface가 있다. **평가 데이터가 전혀 없는 것이 아니다.** 이번에 확인한 자료에서 C6에 필요한 **동일 VLA의 RL 이력 × 학습 reward/evaluator provenance × 독립 trial outcome**의 연결을 확보하지 못했다.

검사 범위·원본 hash·code 위치는 [DATA_AND_CODE_REVIEW.md](./DATA_AND_CODE_REVIEW.md)와 [ARTIFACT_AUDIT.json](./ARTIFACT_AUDIT.json)에 기록했다. 집계 점수로 가상 trial을 생성하거나 sequential selection의 성능을 계산하지 않았다.

## 연구적으로 남기는 것

이 검토는 C6의 policy 효과를 반증한 실험이 아니다. **신규성·증거 확보 비용을 고려한 채택 심사**다. 지금 새 selector를 만드는 것보다 기존 statistical evaluation을 다음 정책 연구의 검증 장치로 쓰는 편이 타당하다.

재개하려면 단순한 ranking 불일치를 넘어, **어떤 RL 변화가 어떤 평가기의 오차를 악화시키며, 독립 실측과 기존 검정으로도 남는 문제가 무엇인지** 보여야 한다. 학습 reward를 바꾼 controlled contrast 없이 관측된 불일치를 reward exploitation의 인과 효과로 부르지 않는다. 필요한 데이터와 기각 규칙은 [REOPEN_PROTOCOL.md](./REOPEN_PROTOCOL.md)에 남겼다. 실행 환경·checkpoint·학습 manifest는 미확정이며 구현 직전 프로젝트로 승격하지 않는다.

Registry 974편, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242 및 사용자 reading 이력은 유지한다. [검증 및 Docker 정리](./VALIDATION.md)
