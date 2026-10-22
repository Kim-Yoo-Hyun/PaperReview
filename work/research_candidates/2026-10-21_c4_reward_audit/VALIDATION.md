# C4 검증·실행 범위

- Date: 2026-10-21 KST
- 연구 효과를 검증한 실험과 문헌/데이터 전제 감사를 분리한다.

## 실제 실행

- Docker container `c4-metadata-audit`, Linux ARM64, 2GiB memory limit, 2 CPU limit.
- Python 3.11 slim 이미지 내부에 `pyarrow==19.0.1`을 설치했다. Host에는 dependency·영상·모델·외부 코드 package를 설치하지 않았다.
- [Metadata audit script](./audit_public_data.py)로 두 release의 실제 metadata payload 20개, 30,198,657 bytes를 파싱했다. 결과는 [DATA_AUDIT.json](./DATA_AUDIT.json), container exit/OOM·image 식별은 [RUNTIME_AUDIT.json](./RUNTIME_AUDIT.json)에 기록한다.
- 첫 실행은 16MiB per-file cap 때문에 RoboReward train metadata를 제외했다. 상한을 64MiB로 수정한 뒤 전체 감사를 다시 실행하여 최종 payload error 0, exit 0, OOM false를 확인했다. 일부만 읽고 54,135개 전수 검사로 보고한 것이 아니다.
- Policy/reward inference 0, RL update 0, robot rollout 0. 논문의 결과를 자체 재현 성공으로 표시하지 않는다.
- Public code는 source commit·SHA256·검토 line을 [CODE_AUDIT.json](./CODE_AUDIT.json)에 남겼다. Upstream code를 실행하지 않았다.

## 재현 명령

저장소 루트에서 실행한다. 외부 payload와 dependency는 container 내부에만 둔다. Script는 실행 당시 HEAD를 조회해 immutable revision으로 payload를 읽고 revision/hash를 결과에 기록한다. 과거 결과와 비교할 때 revision 차이를 먼저 확인한다.

```bash
docker run --name c4-metadata-audit --label research.scope=c4-20261021 --memory=2g --cpus=2 \
  -v "$PWD/work/research_candidates/2026-10-21_c4_reward_audit:/audit:ro" \
  python:3.11-slim sh -c 'pip install --no-cache-dir pyarrow==19.0.1 >&2 && python /audit/audit_public_data.py' \
  > work/research_candidates/2026-10-21_c4_reward_audit/DATA_AUDIT.json
```

이는 metadata 검사 명령이며 VLA 실험 설치 명령이 아니다. 실제 실행에서 식별된 image digest는 runtime JSON을 따른다. 새로운 실행이 기존 evidence를 덮지 않도록 별도 출력 경로를 사용하는 것이 좋다.

## 저장소 검증

현재 registry/tier: 974편, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242. Reading tracker와 notes를 승격·수정하지 않았다.

```bash
python3 -m py_compile work/scripts/build_reading_tiers.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/audit_repository.py
git diff --check
```

위 네 명령을 실행했고 통과했다. Repository audit는 Markdown 4,928개·내부 링크 8,067개에서 오류 0·경고 0이다. 추가 문헌 7편은 title 검색·정규화 비교에서 registry 일치가 없었으며 신규 등록하지 않았다.

작업 전 snapshot으로 보호한 notes·registry·manifest·tiers·사용자 tracker/history **4,876개 파일의 SHA256가 모두 동일**하다. 생성기는 현재 후보의 상태 문구만 갱신했으며 membership을 바꾸지 않았다. DATA/CODE JSON·실행 script의 runtime 기록 hash도 일치했다.

사용한 `c4-metadata-audit` container와 `python:3.11-slim` image를 제거했다. 종료 확인에서 container 0·image 0이며 기존 `minikube` volume을 보존했다. Global prune은 사용하지 않았다. 내부 dependency와 임시 payload는 container와 함께 정리했고 작은 evidence JSON·검사 script·결과 문서만 저장소에 남겼다.

남은 실질적 불확실성은 독립적인 VLA 현상·새 기여의 존재, policy/reward provenance join, native learner 실행 및 개선 여지다. 상세 조건은 [DIAGNOSTIC_PROTOCOL.md](./DIAGNOSTIC_PROTOCOL.md)를 따른다.
