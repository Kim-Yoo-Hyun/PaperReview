# C6 검증 및 정리 기록

- Date: 2026-10-21 KST
- 완료 범위: 공개 문헌·source·데이터 전제 심사. 정책 선택 성능이나 VLA RL 재현이 아니다.

## Docker 실행과 정리

- Container `c6-artifact-audit`, Python 3.11 slim, Linux ARM64, memory 1GiB, CPU 2.
- Image digest `sha256:0a236bf8f0b6013383df04d1cd02cb0abe5fbfa1a7012141d7ff9202b7cb30a6`.
- 표준 라이브러리만 사용했다. Host/container 추가 dependency 설치 0, upstream 실행·model inference·RL update·robot rollout 0.
- 8개 repository 주소 중 7개를 commit 고정으로 읽었다. Text source 26개·441,388 bytes. 나머지 주소의 HTTP 404를 접근 상태로 기록했으며 재현 실패와 혼동하지 않았다.
- RACE JSON 54,809 bytes를 파싱하고 57개 checkpoint 집계의 schema를 확인했다. DP와 VLA의 시간 index가 달라 첫 summary 확장에서 한 번 exit 1이 발생했다. 확인한 `epoch`/`step` schema로 수정한 최종 audit와 integrity/syntax 검사는 모두 exit 0이다.
- Container의 원본 text 26개·git tree 7개·JSON payload 1개의 hash를 전부 대조했다. 새로운 selector의 알고리즘 테스트를 실행한 것은 아니다.
- 전용 container를 정상 종료(exit 0, OOM false) 후 삭제했다. 이번 image도 삭제했다. 최종 container 0·image 0, 기존 `minikube` volume 보존.

[RUNTIME_AUDIT.json](./RUNTIME_AUDIT.json)에 실제 image identity, exit/OOM, source와 artifact hash, 정리를 기록했다. 원 source/payload는 container 삭제와 함께 정리했다.

## 재검사

저장소 루트에서 필요할 때만 실행하며 기존 report를 덮지 않는 출력 경로를 사용한다.

```bash
docker run --rm --memory=1g --cpus=2 \
  -v "$PWD/work/research_candidates/2026-10-21_c6_checkpoint_audit:/audit:ro" \
  python@sha256:0a236bf8f0b6013383df04d1cd02cb0abe5fbfa1a7012141d7ff9202b7cb30a6 \
  python /audit/audit_public_artifacts.py --sources /audit/CODE_SOURCES.json \
  > /tmp/c6_artifact_recheck.json
```

Source는 commit에 고정되어 있다. RACE URL은 mutable하므로 재검사 hash가 달라지면 새 evidence로 다룬다. 404 주소는 당시의 접근 결과이며 영구적 부재를 뜻하지 않는다. 예시 `--rm`은 container만 정리하므로 재검사 후 불필요해진 전용 image도 정리한다.

## 저장소 검증

Registry 974편, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242 유지. 후보의 bibliography는 신규 paper admission과 구분한다. Reading status/history와 표준 notes는 승격·수정하지 않았다.

```bash
python3 -m py_compile work/scripts/build_reading_tiers.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/audit_repository.py
git diff --check
```

위 네 명령 모두 실행·통과했다. Repository audit는 Markdown 4,939개·내부 링크 8,115개를 검사했고 오류 0·경고 0이다. 생성기는 후보 현황 문구를 갱신했으며 tier membership을 유지했다.

변경 전 보호한 registry/manifest·notes·tier·tracker/history **4,876개 파일의 SHA256가 모두 동일**했다. Runtime에 기록한 evidence/script hash 4개와 실제 파일이 일치했고, 7개 성공 repository의 commit은 고정 source specification과 일치했다. Source ledger 12개의 ID는 고유하며 본문 관련 구간 확인 10편 / abstract·metadata 중심 2편이다. Exact/distinctive title 검색과 normalized-title 대조에서 기존 registry entry와의 일치를 찾지 못했으며, 이번에는 신규 등록하지 않았다.

## 남은 실질적 불확실성

- S06의 ICRA, S07의 workshop acceptance는 저자 표기와 공식 venue 검증을 구분했다. S08은 proceedings/preprint metadata 차이가 있다.
- Repository text/interface 검사와 payload 전수 검사는 다르다. RACE 외 데이터 payload의 전체를 읽었다고 하지 않는다.
- Native VLA RL 이력·reward/evaluator provenance·independent trial join, selection regret와 나빠진 정책 승인율, 현재 컴퓨터의 native learner 실행은 미검증이다.
- C6 NO-GO는 현재 설계의 채택 판단이며 실험으로 가설을 반증한 결과가 아니다.
