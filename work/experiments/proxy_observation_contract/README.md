# GAP-N3 수정 packet과 Docker 계약 검사

- Updated: 2026-10-25 KST.
- **N3-A source/계약 artifact 완료, 전체 GAP-N3 재개 gate는 NOT_MET.** Docker 계약 검사 17/17 PASS. Native RoboMME·VLA inference·학습·수집은 0이다.
- [연구 판단과 남은 조건](../../update/PROXY_OBSERVATION_REPAIR_REVIEW_2026-10-25.md) · [동결 범위](./PROTOCOL.json) · [원본 revision/hash](./sources.lock.json).
- N3-B의 [환경 구성과 재개 절차](./ENVIRONMENT.md) · [구조화 설정·source 근거](./ENVIRONMENT_PROFILE.json). 설정 문서화는 완료했으며 native image build·reset/render 검증은 미완료다.
- 후속 [N4 비실험 심사](../../update/PROXY_SELECTION_IDENTIFIABILITY_REVIEW_2026-10-26.md)는 연구 비교식·selector/target 입력·baseline/통계 단위의 해석을 보정한다. 이 packet의 동결 protocol·코드·실행 결과는 그대로이며, source 계약 PASS가 연구 효과를 뜻하지 않는다.

## 실제 만든 것

| Artifact | 역할과 경계 |
|---|---|
| [fixture_api.py](./fixture_api.py) | Fixture 설정 검증, raw identity sidecar, 연속 post-step row의 다음 action 정렬, 동일 slot의 memory mask, 입력 기술서 검사, 접근 구간 observer. **HDF5/model adapter에 아직 연결되지 않은 함수도 포함** |
| [source_repair.py](./source_repair.py) | 지정 SHA256와 일치하는 원본 3파일에만 patch 생성. VideoUnmask의 독립 색 permutation·같은 목표 binding, 별도 language goal, metadata 전달을 수정 |
| [test_contract.py](./test_contract.py) | 합성·적대적 입력과 원본 source의 AST 일부를 이용한 계약 검사. Actor/predicate/planner는 stand-in이며 simulator를 실행하지 않음 |
| [run_contract.sh](./run_contract.sh) / [check_contract.py](./check_contract.py) | Docker 안에서 source fetch와 검사. 검사 container는 network none, read-only source, 512 MB/2 CPU/60초 제한. Host package 설치 없음 |
| [검사 결과](./results/verified/contract_report.json) | 17개 test 이름·상태·코드 hash·원본 hash·실행 image·시간·미충족 gate |
| [생성 patch](./results/verified/source_repair.patch) / [적용 검증](./results/verified/patch_application.json) | 원본에 실제 적용한 임시 파일 4개의 hash 일치. AST parse/compile 및 source binding 검사이며 native import/physics 검증은 아님 |
| [Fixture plan](./results/verified/fixture_plan.json) | 고정 scene seed 21000, red 목표, cyclic permutation 3개. `PLANNED_NOT_COLLECTED`, qualification_dev 전용; 기존 train/test나 실제 episode 수로 세지 않음 |
| [로컬 Docker 자원 확인](./results/verified/runtime_check.json) | ARM64 Docker에서 GPU allocation exit 125. Native image·CPU/Vulkan 대체 경로는 검증하지 않음 |

기존 benchmark 원본을 registry 안에 vendoring하거나 기존 실험을 덮어쓰지 않았다. Patch의 helper 파일은 `fixture_api.py`를 복사해 생성한다. 기존 source를 보존하며 `proxy_fixture`를 전달했을 때 easy/Panda/주입 recovery 없음 조건을 강제한다. Fixture가 없을 때 첫 bin을 사용하는 기존 binding은 유지되지만, upstream 전체 regression을 수행한 것은 아니다.

## 다른 컴퓨터에서 재실행

저장소를 clone하고 로컬 Docker daemon을 켠 뒤, 저장소 루트에서 아래 명령을 실행한다.

```sh
sh work/experiments/proxy_observation_contract/run_contract.sh /tmp/gap-n3-check-new
```

출력 directory는 비어 있어야 한다. 기존 `results/verified/`를 출력 경로로 쓰지 않는다. Python image를 digest로 고정했고 별도 pip/apt 설치가 없다. 첫 container만 지정 source 3파일을 인터넷에서 가져오며 두 번째 검사는 network 없이 수행한다. 임시 source와 container는 종료 시 삭제한다. 로컬에 새로 받은 image는 Docker cache로 남을 수 있으며 다른 작업 image를 prune하지 않는다. 이 기록의 검사가 끝난 뒤에는 이번에 추가된 Python image 참조도 제거했다.

ARM64에서 실제 실행했다. 같은 명령을 다른 Docker host에서 사용할 수 있지만 AMD64에서의 이번 packet 실행 기록은 아직 없다. 성공 시 `contract_report.json`, `source_repair.patch`, `fixture_plan.json`이 생성된다. 소스 hash가 바뀌면 중단하며 최신 upstream에 강제로 적용하지 않는다.

## 무엇을 검증했고 무엇이 남았는가

- 수정된 task dictionary의 실제 lambda·segment, language-goal branch, metadata loader/전달 지점을 분리 실행했다. 3색×6 permutation에서 같은 목표를 가리키는지 검사했다. 기존 source가 이 counterfactual fixture와 일치하지 않는 예도 대조했다. 이는 upstream의 원래 task가 잘못됐다는 뜻이 아니다.
- Raw identity/split·post-step alignment·memory/input helper는 **합성 데이터에서만** 검사했다. 실제 raw HDF5→PKL sample 연결, 학습 dataset 및 policy의 최종 tensor 검사, encoder/normalizer provenance 확인은 아직 없다. 검사 함수가 존재하는 것과 production 경로에 연결됐다는 것은 다르다.
- 접근 구간 event는 TCP가 특정 bin 중심의 XY 4 cm, 상대 Z 2–12 cm 범위에 연속 두 tick 들어오는 보조 proxy다. `physics_step`/tick은 이 계약에서 연속 관측 가능한 `env.step` 단위를 뜻하며 simulator 내부 substep과 혼용하지 않는다. 모호함·먼저 lift됨·무진입 종료는 별도 결과로 남긴다. Native trace에서 유용성이 확인되기 전에는 “첫 올바른 선택률”로 보고하지 않는다.
- Native qualification은 고정 장면 1개×permutation 3개만 대상으로 먼저 demo 종료·첫 decision·관측/pose 일치를 확인해야 한다. 실패하면 fixture를 수정/기각한다. 통과 후에만 HDF5/model integration·checkpoint/normalizer·예산을 채운다. N1의 72 episode 수집과 selector/target 학습은 계속 HOLD다.

**GAP-N3-B는 native runtime/resource 대기다.** 현재 Docker GPU allocation은 실패했다. 이는 GPU만 확보하면 연구 gate가 자동 통과한다는 뜻이 아니다. Native dependency/image qualification, 실제 관측 equality, controller/planner와 metric 검증이 남아 있다. CPU/Vulkan 우회나 원격/cloud로 전환하지 않았다.
