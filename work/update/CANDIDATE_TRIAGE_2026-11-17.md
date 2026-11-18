# 연구 후보 폐기·신뢰성 탐색 정리

- Date: 2026-11-17 KST / CANDIDATE-TRIAGE-R2
- 요청: 약한 기존 주제를 삭제·폐기하고 VLA + RL + Computer Vision + Robotics, 특히 신뢰성·불확실성·실패 문제에 집중.
- [현행 후보](../research_topics/README.md) · [폐기 이유·결과](../research_topics/retired/README.md) · [삭제/이동·출처·검증 원장](../sources/candidate_triage_2026-11-17.json) · [TODO](../../TODO.md)

## 판단과 실제 변경

기존 11개를 **유지 3개·예비 1개·폐기 7개**로 정리했다. 유지: 시각 피드백/실패 원인, 단일 VLA RL의 지시별 행동 보존, 접촉 적응. 예비: 부분 지시 수정. CODEC1·RETRIEVAL·SET·HANDOFF·ALLOC·HINDSIGHT·VRL은 독립 연구 주제로 폐기했다. 개별 이유는 폐기 요약에 한 번만 기록한다.

판정은 새 목표 아래 연구 기여와 구현·검증 부담을 비교한 투자 결정이다. 기존의 조건부 탐색 가능성이 실험으로 반증된 것은 아니다. 단순 기준선의 존재만으로 충분함을 입증했다고 쓰지 않았고, GPU 부재를 폐기 사유로 삼지 않았다. 특히 residual 구조나 hindsight 분야 전체를 제외하는 판단이 아니다.

명시한 7개 폴더의 기존 77파일을 활성 경로에서 제거했다. 그중 **결과·해석 계약 7파일은 동일 bytes로 이동 보존**, 나머지 **70파일은 삭제**했다. 실행 코드·Docker recipe·dependency 목록·상세 설계/중복 인계는 현 workspace에서 제거했다. 새 설치·실험·Docker container/image 작업은 없었다. 공유 문헌 원장과 과거 유지보수 이력은 남겼다.

과거 코드와 상세 기록은 삭제 전 Git commit [`5bec2cfa`](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096)에 있다. 폐기 요약과 파일별 원장에서 고정 경로·hash를 추적한다. 실제 CPU 토큰화 진단과 시연 자산 감사는 정책 효과와 구분하여 보존했다. 남은 4개 주제의 실행 파일은 변경하지 않았다.

현재 index·TODO·AGENTS·README와 실험 navigation을 갱신했다. Synthesis의 폐기 후보 실행 계획은 짧은 문헌 비교 원칙과 폐기 링크로 압축했다. 과거 작업 보고서의 링크는 현재 요약/이동 증거/고정 commit으로 연결하고 역사 기록임을 표시했다. 후보 파일의 `내용/`·`재현 방법/` 두 폴더 구조는 유지한다.

## 문헌 대조와 다음 방향

공식 proceedings와 arXiv에서 16개 source를 범위 제한 확인했다. 공식 게재 7개와 preprint 9개이며 대부분 초록, AHEAD·B2FF·SFF는 지정 본문/한계 구간까지 확인했다. 이전 dossier의 추가 4개 reference는 신규 본문 확인으로 세지 않는다. 이는 2024–2026 전체 문헌의 체계적 전수조사가 아니다. Canonical registry 신규 등록도 이번 범위에 포함하지 않았다.

[SAFE, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html)의 내부 특징 기반 탐지와 [SFF, 2026 preprint](https://arxiv.org/abs/2611.11688)의 배포 후 갱신이 있어 일반 실패 탐지·정책 변화 후 재보정은 새 공백으로 제안하지 않는다. [AHEAD §6.1](https://arxiv.org/html/2606.02486v1)의 운동 추정 한계와 [B2FF §5](https://arxiv.org/html/2606.09258v1)의 회복 가능성 가정에서 **실패 원인과 유용한 개입의 관계**를 더 대조할 이유를 찾았다. 논문들의 한계만으로 새 방법의 신규성을 확정하지 않았다.

사용자 제안의 14개 분야·동의어·검색식·survey→직접 선행→반례 비교 절차를 [기존 buildup guide](../../research/IDEA_BUILDUP_GUIDE.md#search-map-2026-11-17)에 통합했다. 다음은 [FEEDBACK 내용 문서](../research_topics/visual_feedback/내용/README.md#reliability-scout-2026)에서 가장 가까운 본문·공개 interface를 비교하는 비실험 작업이다. 새 신뢰성 방법을 기존 P0 코드로 구현 완료했다고 표시하지 않는다.

## 검증

변경 전 repository audit는 오류·경고 0이었다. 변경 후 전체 audit, 생성기, 읽기 이력·논문 노트·유지 실행 자료 보존, 삭제 허용 목록·내부 링크 검사를 완료했다. 최종 수치는 아래와 원장에 기록했다.

<!-- TRIAGE_VALIDATION:START -->
- **전체 repository audit: PASS, 오류 0·경고 0.** 1,206편·23 category·6,030 표준 노트·455 active/47 history, Markdown 6,245개·내부 파일 링크 13,224개 검사.
- **보존: PASS.** Canonical manifest/registry table·tier·active/history tracker bytes 동일. 논문 노트 6,030개와 유지/예비 후보의 실행 자료 43개 bytes 동일. Generated reading queue 동일.
- **폐기 범위: PASS.** 삭제 전 77개 경로만 제거, 결과/계약 7개 동일 hash로 이동, 실제 제거 70개. 다른 파일 삭제 없음. 이번 검증이 만든 Python cache 2개도 제거하고 기존 cache는 보존.
- **문서 연결: PASS.** 변경 문서·대상 관련 fragment 링크 362개 확인. 기존 buildup guide를 가리키던 옛 anchor 1개를 호환 alias로 복원해 과거 4개 링크도 연결.
- **필수 명령: PASS.** `py_compile`, `build_reading_tiers.py`, `test_reading_history.py` 6검사, `git diff --check`. 모델·simulator 실행이나 패키지 설치는 하지 않음.
- **증거 경계:** 신규 실험 0, native 효과·새 신뢰성 공백 확정·외부 피드백 수신 0. 이번 판단은 연구 투자 정리이며 출판 가능성 인증이 아님.
<!-- TRIAGE_VALIDATION:END -->
