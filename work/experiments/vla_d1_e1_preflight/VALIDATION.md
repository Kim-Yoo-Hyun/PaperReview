# D1-E1 preflight — 검증과 보존

2026-10-22 KST. Docker infrastructure/source 검사와 repository 무결성 검사다. Native OFT 성공·연구 효과 검증을 뜻하지 않는다.

- 사전 repository audit: 990편, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242, intensive 304, history 47, 표준 note 4,950개, Markdown 5,039개·상대 링크 8,473개. 오류 0·경고 0.
- 작업 전 canonical manifest·PAPER·tier generator·tier/tracker/history·표준 note 4,956개 SHA-256 snapshot을 생성했다.
- Docker stdlib probe exit 0. GPU allocation 요청은 예상 성공으로 바꾸지 않고 **exit 125 실패** 그대로 기록했다. Policy forward/rollout/simulator step은 0이다.
- Probe image는 native dependency environment가 아니다. Docker 내부 Python 3.10.22로 public text/JSON·AST를 확인했으며 host나 container에 별도 package를 설치하지 않았다.
- 이번 전용 container/image는 정리하여 각각 0개를 확인했다. 관련 없는 `minikube` volume은 보존했다.

- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. Tier 47 / 257 / 444 / 242 유지.
- `python3 work/scripts/audit_repository.py`: exit 0. Registry 990, intensive 304, history 47, 표준 note 4,950개, Markdown 5,041개·상대 링크 8,488개. 오류 0·경고 0.
- `git diff --check`: exit 0. 신규 artifact의 별도 trailing-whitespace 검사도 오류 0.
- Artifact 검증: script/raw report SHA-256이 manifest와 일치. Public read 10개에 error record 없음, 해당 probe의 byte 합계 304,092 일치. Normalizer hash가 raw report·manifest·pilot spec·task candidate에서 일치한다.
- Normalizer 구조: action 7D/proprio 8D의 finite 값·q99≥q01·비퇴화 범위를 정적 확인. 런타임 state 변환/정책 utility 검사가 아니다.
- 상태 검증: G0는 RESOURCE_GATE_NOT_MET_NATIVE_NOT_RUN, G1–G4는 NOT_RUN, executable/runtime freeze는 false, baseline implemented는 모두 false. Large weight의 locally verified hash는 null이다. TODO의 E1 WAITING_RESOURCE와 일치한다.
- 작업 전 **4,956개 canonical/표준 note 파일 모두 hash 동일**. 기존 dirty worktree·사용자 reading status·분석 필드를 보존했다. 비교 matrix 106행·completed 5행 유지.

G0 전체와 G1은 통과하지 않았다. Normalizer metadata 확인·실행 명세 작성·일반 Docker process 실행을 policy 재현이나 REPRODUCED로 바꾸지 않는다. 기존 10-21 runtime artifact와 L1–L4의 검증 기록은 역사적 snapshot으로 유지한다.
