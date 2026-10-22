# VLA 재탐색 문서 유지보수 검증

- 날짜: 2026-10-22 KST
- 범위: [후보 탐색](./README.md), 문헌 dossier·질문 card와 작업 navigation. 정책 실험 검증이 아니다.

## 확인 상태

- 사전 `audit_repository.py`: errors 0, warnings 0. Registry 990편, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242, active tracker 304 / history 47.
- 변경 전 보호 hash: paper note 4,950개와 registry/manifest/tier/tracker/history/generator 등 총 4,956개.
- `python3 -m py_compile work/scripts/build_reading_tiers.py`: PASS.
- `python3 work/scripts/build_reading_tiers.py`: PASS. CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `git diff --check`: PASS.
- 후속 `audit_repository.py`: errors 0, warnings 0. Markdown 5,059개·상대 링크 8,685개, comparison 106행/완료 5행 검사. Registry 990편·표준 note 4,950개·resource 496개·index 990행 유지.
- 보호 hash 비교: 4,956개 중 **4,955개 동일**. 변경 1개는 의도한 `work/scripts/build_reading_tiers.py`의 연구 초점/navigation 문구다. CORE/NEXT membership·rationale 변경 없음. PAPER/manifest/tier CSV/active·history tracker 및 모든 paper note가 byte-identical이다.
- 비교 표 P1–P16의 normalized title을 manifest와 대조: 기존 5편 / 외부 11편. 이는 탐색 기록의 매칭이며 정식 registration의 public-ID 전체 admission 검사를 대체하지 않는다.

## 수정 범위

- 새 작업 문서 4개: README, LITERATURE, E1_QUESTION, 이 검증 기록.
- TODO·AGENTS·root/work README·날짜별 update log·VLA synthesis 수동 Open Questions 갱신.
- Generator의 현재 연구 초점과 낡은 D1 활성 안내를 수정한 뒤 READING_PLAN을 재생성. Tier·사용자 상태·분석은 보존했다.
- 기존 dirty worktree를 되돌리지 않았다. 검증용 임시 보호 hash 파일은 비교 완료 후 제거한다.

문헌의 저자 보고와 현재 컴퓨터의 정책 효과를 구별한다. 실험·학습·inference·Docker preflight·dependency 설치·model/trajectory/video/PDF 저장·외부 연락은 수행하지 않았다. 공식 code의 landing/README 확인은 runtime qualification이 아니다.
