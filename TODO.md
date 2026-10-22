# 연구 작업 TODO / 다음 세션 인계

- Updated: 2026-10-23 KST
- 직전 완료: **PUB-R1 DONE** — 1,037편 registry·누적 연구 문서·Docker 재분석 자산을 origin/main에 게시하고 실제 원격 clone의 무결성·입력 hash를 검증했다. 앞선 ORG-R1 / DOC-R1 / REG-R1 결과를 포함한다.
- 다음 작업: 새 컴퓨터의 clone 재분석, DOC-QA1의 원문 대조, 또는 E2-R1/E1-R2/D3-R2의 새 연구 근거 확보. Native 학습 자동 재개 없음.
- 상세 과거 작업 ID·날짜·완료 근거는 [2026-10-22 인계 보존본](./work/update/TASK_HISTORY_2026-10-22.md)에 있다. 읽기 순서는 [READING_PLAN](./research/READING_PLAN.md), 후보 판단은 [단일 요약](./work/research_candidates/summaries/README.md)을 따른다.

## 다음 행동

| ID | 상태 | 해야 할 일·완료 기준 | 근거 |
|---|---|---|---|
| ORG-R1 | DONE | 7개 synthesis 보강·39개 파일 삭제/병합·cache 정리. C3 ARM64/AMD64 Docker와 local clone 검사 통과. 논문·읽기·실험 근거 보존 | [작업 report](./work/update/WORKSPACE_UPGRADE_2026-10-23.md) |
| PUB-R1 | DONE | Content commit `d5d60510`을 origin/main에 게시. 실제 원격 clone에서 registry 1,037편·입력 3개·실행 코드 hash 검증 통과 | [게시 기록](./work/update/UPDATES_2026-10-23.md) |
| PORT-R1 | READY | 게시된 revision을 새 컴퓨터에서 clone하고 `check → build → test → replay-c3` 실행 | [실행 안내](./work/experiments/portable/README.md). 현재 컴퓨터의 원격 clone 검사는 완료; 새 물리 컴퓨터의 실행/GPU qualification은 별도 |
| DOC-QA1 | QUEUED | 과거 PDF 추출 cue의 제어문자 잔여물을 원문과 대조해 수정 | [파일별 목록](./work/sources/publication_validation_2026-10-23.json). 내용 추정·일괄 문장 재생성 없이 확인 |
| E2-R1 | WAITING_EVIDENCE | 일관된 task–checkpoint–normalizer–controller–time–evaluator packet 및 기존 대안과 갈리는 예측 확보 | [현재 명세](./work/research_candidates/2026-10-22_e2_buildup/QUALIFICATION_SPEC.json) |
| E1-R2 | WAITING_EVIDENCE | Source episode join·command/time/scene·정상 정렬 이후 추가 effect 정보와 두 로봇의 native 평가 경로 확보 | [현재 요건](./work/research_candidates/2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json) |
| D3-R2 | WAITING_EVIDENCE | Event/RGB 정렬·pre/post feasible witness·continuation competence와 공정 비교 확보 | [현재 요건](./work/research_candidates/2026-10-22_d3_buildup/R1_EVIDENCE_REQUIREMENTS.json) |

GPU 확보만으로 E1/E2/D1–D3의 native 실험을 재개하지 않는다. D1·D2 및 C1–C6는 주제별 기존 HOLD/NO-GO를 유지하고, 초기 RL 전이·RP-2/RP-3는 RETIRED다. 효과를 실험 전에 입증하라는 요구가 아니라, 무엇을 비교하고 어떤 결과로 주장을 기각할지 정한 실행 가능한 packet이 필요하다는 뜻이다.

실험은 사용자 선택 컴퓨터의 로컬 Docker에서만 수행한다. Host dependency·MPS·원격/cloud로 임의 전환하지 않는다. 저장 결과 재분석, native runtime qualification, 정책 효과 검증을 따로 기록한다. 새 학습·새 rollout 없이 수행하는 C3 replay는 기존 연구 판정을 변경하지 않는다.

## 갱신 규칙

작업 시작/완료 시 상태·결과 링크·다음 행동을 갱신한다. `DONE`은 정해진 작업의 완료다. `WAITING_EVIDENCE`, `WAITING_SOURCE`, `WAITING_RESOURCE`, `HOLD_RESEARCH`를 분리하고, 읽기 status나 가설 입증으로 치환하지 않는다. 긴 이력은 날짜별 `work/update/`에 두며 여기에는 활성 항목만 남긴다.

운영 참고: [GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)의 작업/의존성 연결과 [The Turing Way](https://github.com/the-turing-way/the-turing-way/blob/main/ways_of_working.md)의 지속적인 인계 방식. 상태 이름과 연구 gate는 이 저장소의 로컬 계약이다.
