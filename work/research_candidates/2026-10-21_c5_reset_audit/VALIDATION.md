# C5 검증 및 정리 기록

- Date: 2026-10-21 KST
- 완료 범위: 문헌·공개 source·데이터 전제 심사. VLA/RL 성능 재현이 아니다.

## Docker 실행

- Container `c5-code-audit`, Python 3.11 slim, Linux ARM64, memory 1GiB, CPU 2.
- Image digest: `sha256:0a236bf8f0b6013383df04d1cd02cb0abe5fbfa1a7012141d7ff9202b7cb30a6`.
- 표준 라이브러리만 사용했다. Host 및 container의 추가 dependency 설치 0. Upstream code는 실행하지 않았다.
- Code audit: 4 repository / 22개 text source / 193,528 bytes; 고정 commit의 각 SHA256와 container 내부 원문을 22개 모두 대조했다.
- Data audit: 고정 HF revision의 전체 inventory와 metadata 24개·trajectory 2개의 payload 14,373,568 bytes를 검사했다. 첫 검사 뒤 metadata-only run count와 누락 sample path를 출력에 추가하고 같은 revision을 재검사했다. 최종 error 0, audit subprocess exit 0.
- Source scripts 2개의 syntax 검사도 Docker 내부에서 통과했다. Pickle opcode만 읽었고 pickle 실행·이미지 decode·policy inference·RL update·robot rollout은 모두 0.
- 감사 완료 후 대기용 PID 1 `sleep infinity`를 정지할 때 종료코드 137이었다. **OOM은 false**, code/data 감사 subprocess는 각각 exit 0이다. Cleanup 종료코드를 실험 crash나 성공코드로 바꿔 적지 않는다.
- 전용 container/image를 삭제하고 container 0·image 0 및 기존 `minikube` volume 보존을 확인했다. Global prune을 쓰지 않았다. Upstream source·원 데이터와 image cache는 이번 자원과 함께 정리했다.

실제 image/exit/OOM/hash 기록: [RUNTIME_AUDIT.json](./RUNTIME_AUDIT.json). Source/data 감사 결과와 짧은 재검사 script만 저장소에 남겼다.

## 재검사 방법

저장소 루트에서 필요할 때만 실행한다. 기존 evidence를 덮지 않도록 새로운 출력 파일을 지정한다. Source는 [CODE_SOURCES.json](./CODE_SOURCES.json)의 commit, data는 script의 고정 revision을 사용한다.

```bash
docker run --rm --memory=1g --cpus=2 \
  -v "$PWD/work/research_candidates/2026-10-21_c5_reset_audit:/audit:ro" \
  python@sha256:0a236bf8f0b6013383df04d1cd02cb0abe5fbfa1a7012141d7ff9202b7cb30a6 \
  python /audit/audit_public_code.py --sources /audit/CODE_SOURCES.json > /tmp/c5_code_recheck.json

docker run --rm --memory=1g --cpus=2 \
  -v "$PWD/work/research_candidates/2026-10-21_c5_reset_audit:/audit:ro" \
  python@sha256:0a236bf8f0b6013383df04d1cd02cb0abe5fbfa1a7012141d7ff9202b7cb30a6 \
  python /audit/audit_public_data.py > /tmp/c5_data_recheck.json
```

위 출력은 작은 summary JSON이며 외부 원 payload는 container 내부에서만 읽는다. 예시 `--rm`은 container만 삭제하므로 재실행 후 더 이상 필요 없는 해당 image도 정리해야 한다.

## 저장소 검증 범위

Registry 974편, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242 유지. 문헌 11편의 exact/distinctive phrase 검색과 normalized title 대조에서 기존 entry가 없었으며 candidate 검토만 진행하고 admission은 하지 않았다. Paper notes와 reading status/history를 승격·수정하지 않았다.

```bash
python3 -m py_compile work/scripts/build_reading_tiers.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/audit_repository.py
git diff --check
```

위 네 명령 모두 실행·통과했다. Audit 결과는 Markdown 4,933개·내부 링크 8,093개, 오류 0·경고 0이다. 생성기는 현재 후보 상태 문구만 갱신했으며 tier membership을 유지했다.

변경 전 보호한 registry/manifest·notes·tier·tracker/history **4,876개 파일의 SHA256가 모두 동일**했다. Runtime JSON의 evidence/script hash 6개도 실제 파일과 일치했다. Source ledger 11개의 ID가 고유하며 관련 본문 확인 6편 / abstract·metadata 중심 5편으로 구분되어 있다.

## 남은 uncertainty

Sample 검사로 전체 export의 provenance 완전성을 단정하지 않는다. Native VLA의 reset/학습 사건 join, 현재 컴퓨터에서의 native physical-reset RL 실행, 고정 target의 실제 정책 개선/손실, 여러 task·robot에 걸친 기여는 미검증이다. [다음 gate](./DIAGNOSTIC_PROTOCOL.md)를 통과하기 전에는 구현 직전 project로 승격하지 않는다.
