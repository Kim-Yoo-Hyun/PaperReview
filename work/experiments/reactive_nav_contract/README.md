# 반응형 주행 계약

- Updated: 2026-10-23 KST
- **상태:** 로컬 Linux ARM64 Docker CPU에서 13/13 검사·3개 smoke scene 통과. [결과](./RESULTS.md).
- 실행 범위는 새 상태 기반 adapter의 시간·identity·평가 계약이다. GenSafeNav 재현, native VLA, 연구 효과 비교·학습이 아니다.
- [P2 설계](../../sources/reactive_navigation_preexperiment_manifest_2026-10-23.json)는 당시 역사적 초안이다. 실행한 계약 범위는 [RUN_MANIFEST.json](./RUN_MANIFEST.json), 현재 결과는 [contract_report.json](./results/verified/contract_report.json)이 소유한다.

## 다른 컴퓨터에서 실행

이 저장소를 clone한 뒤 **로컬 Docker**에서 아래 명령을 실행한다. Host Python·pip·conda로 adapter를 실행하거나 의존성을 설치하지 않는다. Docker build의 compiler/Cython/RVO 설치는 모두 image 내부에서 일어난다. 첫 build에는 network가 필요하며 검사 container는 network 없이 실행한다.

```bash
cd work/experiments/reactive_nav_contract
bash run.sh build
bash run.sh check
```

새 결과는 `results/replay/`에 작성한다. 이미 결과가 있으면 덮어쓰지 않는다. 이후 실행은 `bash run.sh check results/replay-02`처럼 새 디렉토리를 지정한다. 검사 실패는 exit code 1이며 PASS/FAIL/NOT_RUN이 출력된다. 사전 hash 불일치는 실행 전에 실패한다.

검증된 환경은 **Linux ARM64 / CPython 3.11.14** 하나다. AMD64와 다른 물리 컴퓨터는 아직 미검증이며 해당 컴퓨터에서 build/check를 통과해야 한다. Base image digest와 RVO commit·Python build dependency는 고정했다. Debian apt snapshot은 고정하지 않았으므로 다른 시점에 다시 build한 바이너리까지 bit-identical하다고 보장하지 않는다. 실행 image ID·설치 목록·RVO source archive와 바이너리 hash는 각 결과 폴더에 남긴다.

## 구성과 해석

| 파일 | 역할 |
|---|---|
| [scenes.json](./scenes.json) | 3개 장면·seed·route·33개 action 규칙·clock·threshold |
| [adapter.py](./adapter.py) | ORCA human, CV predictor, timestamp/track join, 4개 calibration/control interface, FIFO와 swept-disc 평가 |
| [check_contract.py](./check_contract.py) | 수작업 반례·13개 계약·3개 smoke·저장 trace 독립 재결합 |
| [Dockerfile](./Dockerfile), [run.sh](./run.sh) | Docker 내부 build·network 없는 제한 실행·자동 container 삭제 |
| [RUN_MANIFEST.json](./RUN_MANIFEST.json) | 실행 **직전** 동결 상태와 5개 artifact hash. `NOT_RUN_AT_FREEZE`는 당시 상태이며 현재 결과를 뜻하지 않음 |
| [최종 검사](./results/verified/contract_report.json), [runtime provenance](./results/verified/runtime_provenance.json) | 실제 결과와 의존성/환경 증거 |
| [smoke trace](./results/verified/smoke_trace.jsonl.gz) | 150개 physical step의 관측·예측·성숙 score·FIFO 기록; gzip JSONL |
| [실행 이력](./results/run_history.json) | 초기 3회와 최종 실행의 관계. 대체된 중복 trace·환경 파일은 hash만 남김 |

고정 margin은 `[0.1,0.2,0.3,0.4,0.5]` m의 **수작업 fixture**다. 데이터에서 calibration한 baseline으로 부르지 않는다. Smoke는 M1·reactive·0.5 s actuator delay·10 s route switch 한 구성이다. 이 P3 smoke의 범위에는 전체 factorial·방법 성능 비교가 없다. 후속 [P4 pilot](../reactive_nav_pilot/RESULTS.md)에서 384 branch 비교를 완료했으며 주 가설 joint gate는 실패했다. 유일한 scene/seed 세 개를 train/test split으로 취급하지 않는다.

Native VLA·실제 human 효과는 HOLD다. P4 이후 현재 판단은 [GAP-PLAN](../../../synthesis/01_control.md#gap-plan-2026)의 진단 HOLD이며 추가 pilot은 자동 재개하지 않는다. Fixture PASS만으로 연구 가설의 evidence maturity를 올리지 않는다.

현재 재사용할 image `paper-gap-p3:rvo-c2c46ba`는 보존한다. 필요가 없어지면 이 **전용 tag만** `docker image rm paper-gap-p3:rvo-c2c46ba`로 제거할 수 있다. Containers는 `--rm`으로 삭제된다. 다른 image·volume·cache를 일괄 정리하지 않는다.
