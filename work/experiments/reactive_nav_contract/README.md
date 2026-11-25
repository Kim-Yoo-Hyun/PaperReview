# 반응형 주행 계약

관측·예측·제어 명령이 같은 로봇과 물리 시각에 연결되는지 확인하는 ORCA 기반 검사다. 아래 결과는 상태 관측을 쓰는 어댑터에 해당한다. 후속 안전성 비교와 연구 판정은 별도 파일럿에 있다. [파일럿 결과](../reactive_nav_pilot/RESULTS.md)

## 다른 컴퓨터에서 실행

저장소를 clone한 컴퓨터의 로컬 Docker에서 실행한다. 첫 빌드에는 네트워크가 필요하다.

```bash
cd work/experiments/reactive_nav_contract
bash run.sh build
bash run.sh check
```

기본 출력은 `results/replay/`다. 기존 결과가 있으면 `bash run.sh check results/replay-02`처럼 새 경로를 지정한다. 검사 컨테이너는 네트워크 없이 CPU 2개·512 MiB로 실행한다. 검증된 환경은 Linux ARM64와 CPython 3.11.14다. 베이스 이미지와 Python-RVO2 커밋은 고정했고 Debian 패키지 저장소는 빌드 시점에 따라 달라진다. [실행기](./run.sh) · [이미지 정의](./Dockerfile) · [구현](./adapter.py) · [의존성·실행 환경](./results/verified/runtime_provenance.json)

<a id="results"></a>

## 검증 결과

2026년 10월 23일 시간 정렬, 트랙 ID·세대 교체, 결측·재등장, 에피소드 초기화, 지연 명령 큐, 보정 반경, 틱 사이 충돌·종료 상태 등 **13개 검사**를 통과했다. 같은 물리 틱에서 제어기를 두 번 호출해도 대기 해제 카운터가 증가하지 않는지 검증했다. [동결한 실행 조건](./RUN_MANIFEST.json) · [검사 구현](./check_contract.py) · [13개 판정과 관측값](./results/verified/contract_report.json)

| 측정 | 범위 |
|---|---|
| 장면 | 교차·정면 접근·사선 접근, 시드 71001–71003. 장면당 50틱 × 0.25초로 12.5초 |
| 제어 | 5스텝 정속 예측, 행동 후보 33개, 구동 지연 0.5초, 10초에 경로 변경. 고정 반경은 수작업으로 정한 값 |
| 저장 기록 | 총 150틱, 발행 예측 3,000개 중 목표 시각에 도달한 2,760개. 트랙·시각별로 재결합해 적용 명령과 반경을 대조 |

원래 반경이 2 m여도 제어기가 1 m로 제한하면 1.5 m 오차는 보정 범위를 벗어난다. 두 물체가 틱 양 끝에서 떨어져 있어도 중간에서 교차할 수 있다. 장면은 30초 과제의 성공 여부를 판정하기 전 종료했다. [장면과 제어값](./scenes.json) · [저장 궤적](./results/verified/smoke_trace.jsonl.gz) · [실행 이미지](./results/verified/docker_image.json)

후속 파일럿은 같은 접두 궤적에서 분기한 384개 조건을 비교했다. 사전에 정한 위험·보정 공동 기준을 통과하지 못해 해당 설계의 추가 학습을 보류했다. 실제 사람의 반응과 영상·언어 정책의 효과는 미측정이다. [파일럿 해석과 재개 조건](../reactive_nav_pilot/RESULTS.md) · [초기 실행 기록](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/6aa75b27be4ab2e88ab56cd54df5818317e7a2fb/work/experiments/reactive_nav_contract/results/run_history.json)
