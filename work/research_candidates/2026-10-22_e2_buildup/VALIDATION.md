# E2 문서·registry 유지보수 검증

- 날짜: 2026-10-22. 연구 효과 검증과 구분한다.
- 사전 audit: errors 0 / warnings 0. Registry 990, tier 47/257/444/242, active tracker 304/history 47, 표준 note 4,950개.
- 보호 snapshot: paper notes 4,950개와 PAPER/manifest/tier/active tracker/history/generator 6개, 합계 4,956개.
- `python3 -m py_compile work/scripts/build_reading_tiers.py`: PASS.
- `python3 work/scripts/build_reading_tiers.py`: PASS, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `git diff --check`: PASS. 새 E2 Markdown의 별도 trailing-whitespace 검사도 이상 없음.
- `python3 work/scripts/audit_repository.py`: errors 0 / warnings 0. Registry 990·notes 4,950·active 304/history 47·resources 496·index 990 유지. Markdown 5,071개·내부 링크 8,798개·comparison 106행/완료 5행 검사.
- 보호 hash: **4,955개 동일 / 1개 의도한 변경 / 누락 0**. Generator의 현재 E2 navigation 문구만 변경했다. PAPER·manifest·tier CSV·active/history tracker·paper note 4,950개는 byte-identical이다. CORE/NEXT 선정 규칙·rationale은 변경하지 않았다.
- 새 JSON 2개 파싱 PASS. Review DONE, executable=false, policy_runs=0, selected execution의 모든 필드 null을 확인했다. Source ledger의 attempt/고유 URL/성공 통계와 실제 entry가 일치한다.
- Source text/API 34회·고유 URL 32개·최종 성공 31개·1,418,229 bytes. 404 한 건과 별도 web CVF 403 두 경로를 명시했다. Web 본문/검색 결과와 hash가 있는 text fetch를 합쳐 독립 검증 수로 세지 않는다.

## 변경 범위와 근거 경계

- E2의 8단계 비실험 심사, 직접 문헌 9편, 세 method family의 pinned source 경로, 해석적 반례와 비교/기각 조건, 비실행 spec과 source ledger를 작성했다.
- E1-R1 gate NOT_MET를 유지하고 사용자 최신 조건부 요청에 따라 E2로 진행했다. 과거 E1의 자동 전환 금지는 사용자 새 지시 이전 이력으로 보존한다.
- Registry admission·tier membership·사용자 reading status 변경은 없다. Generator는 현재 연구 navigation 문구만 변경한다.
- 정책 inference·simulation·학습·FK·Docker preflight·설치·weight/trajectory/video/PDF 저장·외부 연락 없음. 공개 code를 실행하지 않았다.
- Source 설정 차이는 우리 정적 관찰이며 성능 차이·논문 오류의 증거가 아니다. Native 효과와 실제 외부 피드백은 미완료다.
- 기존 dirty worktree를 되돌리지 않았다. 이번에 만든 임시 fetch helper·source ledger·보호 hash 파일만 최종 기록 후 정리한다. 사용자 paper cache와 Docker 자원은 건드리지 않았다.
