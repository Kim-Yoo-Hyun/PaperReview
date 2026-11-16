# 현재 6개 후보의 비실험 buildup 상태 보강

- Work ID: BUILDUP-6-STATE
- Updated: 2026-11-04 KST
- 요청: 기존 6개 후보를 비실험 buildup 과정에 맞게 보강.
- 기준: [7단계 비실험 절차](../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow). 기존 0–8 guide의 상세 원칙을 문제/문헌/대안/기여/비교/공수/외부 비판의 운영 단계에 대응했다.
- 검토 범위: 6개 내용 문서, source ledger, 비교·재개 계약, 기존 결과와 11/03 공통 감사. 신규 문헌 전수조사나 새 실험은 아니다.

## 반영한 상태

현행 비교 본문은 [주제 index](../research_topics/README.md#nonexperimental-process-audit), 후보별 근거와 분기는 각 내용 문서가 소유한다.

| 주제 | 보강한 내용 | 보존한 연구 판단 |
|---|---|---|
| [VLA residual 재사용](../research_topics/vla_residual_update/내용/README.md#buildup-status) | 기존 가중치 가치와 gain/critic/모방 대안, 구축 총비용과 교체 이후 추가 비용, A residual bootstrap 선행 조건 | 탐색 유지; 규칙 조합의 독립 신규성·효과 미검증 |
| [부분 지시 수정](../research_topics/instruction_revision/내용/README.md#buildup-status) | 의미 갱신·제약 이행·기본 능력의 결과 분기, 공통 renderer/observer 교정의 역할 | 좁은 평가 후보 유지; 자동 updater·native 효과 미검증 |
| [모바일 정책 교체](../research_topics/mobile_policy_transfer/내용/README.md#buildup-status) | 같은 설정의 결과 공유, 유한 재선택의 음수 이득, 실패를 포함한 시간 비용 | 조건부 평가 후보 유지; 한 template·동일 로봇 범위 |
| [물체 집합·수량](../research_topics/object_set/내용/README.md#buildup-status) | 반복의 충분성과 대상/참조/전환 효과, 전략의 중간 제약과 terminal-only 의미 구분 | 제한된 탐색 유지; 다중 물체 능력·evaluator 미검증 |
| [시연 저장소 확장](../research_topics/context_retrieval/내용/README.md#buildup-status) | H 불변성의 sanity-check 역할, 성공 donor/평가 독립성에 필요한 원 trajectory 연결, 제한된 reference 진단 경로 | 자료 경계를 둔 탐색 유지; 신규 router·광범위 scaling 근거 없음 |
| [행동 토큰화](../research_topics/action_tokenization/내용/README.md#buildup-status) | 알려진 양자화 설명과 실질적 설정 선택의 구분, 호환 codec 조건과 선택 가능한 후속의 경계 | 좁은 평가 자료 보존; 독립 방법 투자 근거 부족 |

각 문서에 7단계 상태·한 문단 기여 가설·결과에 따른 다음 판단·비용·첫 구현 점검·외부 검토 질문을 넣었다. VRL/RETRIEVAL/CODEC의 이전 단계별 표는 현행 표로 교체해 중복을 줄였다. 다른 세 후보는 기존 내용 문서 안에 같은 형식의 현행 상태 절을 추가했다. 주제별 새 파일은 만들지 않았다.

`정리됨`은 문헌/논리/설계가 작성됐다는 뜻이다. Native 실행·데이터 성공 provenance·정책 효과를 그 표기로 승격하지 않는다. 실제 독립 피드백은 6개 모두 기록상 미수신이며 질문 준비와 구별했다. 이는 작은 탐색의 자격을 박탈하는 조건이 아니다.

TODO의 기존 P0들은 `WAITING_RESOURCE_AND_IMPLEMENTATION`으로 보강했다. 과거 runtime JSON의 `WAITING_RESOURCE`는 당시 검사 결과 그대로다. VRL과 기존 세 후보의 외부 검토 인계는 6개 공통 `CANDIDATES-REVIEW`로 통합했다. 새로운 실행 예산·실험 승인·임계값을 만들지 않았으며, 현행 VLA+RL 작업과 기존 packet 간 우선순위도 유지한다.

## 검증·보존

- 변경 전후 repository audit: 오류 0·경고 0. 최종 1,098편·5,490개 표준 노트·368 active/47 history·Markdown 5,696개/링크 11,775개.
- 필수 generator compile/rebuild 및 staged/unstaged `git diff --check` 통과. Registry membership은 CORE 47 / NEXT 321 / REFERENCE 488 / ARCHIVE 242 그대로다. 생성된 읽기 계획의 날짜만 11/04로 갱신됐다.
- 6개 문서의 현행 상태 anchor와 총 42개 단계 행을 확인했고, 변경 Markdown의 fragment 링크 99개가 모두 유효했다.
- 사전 snapshot과 비교해 기존 파일 삭제 0, 의도한 기존 문서 변경 10개, 새 공통 기록 1개다. 기존 논문 노트 5,490개를 포함한 보호 파일 5,766개, source/실행 계약·원시 결과·읽기 CSV와 staged index가 byte 단위로 보존됐다. 읽기 tracker는 active/history 합계 415개이며 상태 승격은 없다.

새 Docker/정책/학습 실행, 환경 재시도, package/weight/PDF 설치·다운로드, 외부 전송, commit/push는 하지 않았다. GPU 조건을 현재 날짜의 새로운 실측으로 기록하지 않았다.
