# GAP-P3 — Docker 계약 검사 결과

- 실행·검토: 2026-10-23 KST
- **작업 DONE / 계약 13개 PASS / 연구 가설 REVISE·미검증 / native VLA HOLD**.
- 결과 source: [검사 JSON](./results/verified/contract_report.json), [runtime provenance](./results/verified/runtime_provenance.json), [image 정보](./results/verified/docker_image.json), [저장 trace](./results/verified/smoke_trace.jsonl.gz).

## 1. 결론

**GPU 없이 작은 상태 기반 비교 pilot을 이어갈 실행 기반을 확보했다.** 로컬 Docker CPU 안에서 실제 ORCA를 호출하고 관측→예측→성숙 score→행동→상대 반응→평가 경로를 검사했다. Host에는 package를 설치하지 않았으며 모델·dataset·PDF 다운로드, 학습, native VLA 실행은 없었다.

이번 증거는 새 adapter의 제한된 계약을 지지한다. 일반 adaptive safety/replanning 방법의 NO-GO와 상태 기반 진단의 REVISE는 유지한다. 전환×반응의 추가 위험, calibration의 인과적 역할, 실제 사람/VLA의 효과는 **아직 측정하지 않았다**. 계약 통과를 연구 기여나 논문 채택 가능성의 증거로 바꾸지 않는다.

## 2. 실행한 구성

- Docker Desktop의 Linux ARM64, CPython 3.11.14, CPU 2개 제한·512 MiB·network none·read-only source. 모든 C++/Cython 설치와 Python 실행은 container/image 내부였다.
- Image ID: `sha256:ec14bd72a90f89cb6f3c4b263bb35a81de7977dffb2e5a2cb7e96946f1545ebb`.
- [Python-RVO2](https://github.com/sybrenstuvel/Python-RVO2/tree/c2c46ba8d59556aa10faf03479293236efea154d) commit `c2c46ba8d59556aa10faf03479293236efea154d`. Build에는 Cython 0.29.37/setuptools 75.8.0/wheel 0.45.1을 사용했다. [공식 RVO2 실행 순서](https://gamma-web.iacs.umd.edu/RVO2/documentation/2.0/using.html)를 참고했다. RVO 코드의 보장을 이 adapter 전체의 보장으로 이전하지 않는다.
- Human마다 현재 관측으로 ORCA를 구성하는 새 adapter다. GenSafeNav의 ego visibility·pre-integration state convention을 참고했지만 원 정책·GST·학습·평가 전체를 재현한 것은 아니다.
- 0.25 s tick·5-step CV 예측·33개 action·0.5 s FIFO delay·10 s route event. Scene와 controller 값은 실행 전 [manifest](./RUN_MANIFEST.json)와 [scenes](./scenes.json)에 고정했다.

| 최종 smoke 장면 | seed | 실행 tick / 물리 시간 | forecast record / 성숙 record | 종료 |
|---|---:|---:|---:|---|
| crossing_smoke | 71001 | 50 / 12.5 s | 1,000 / 920 | probe limit |
| head_on_smoke | 71002 | 50 / 12.5 s | 1,000 / 920 | probe limit |
| oblique_smoke | 71003 | 50 / 12.5 s | 1,000 / 920 | probe limit |

첫 관측의 history 부족 record도 1,000개에 포함된다. 아직 target이 도착하지 않은 예측은 성숙 score로 세지 않는다. 세 장면은 30 s task 완료 평가 전에 계획된 probe limit에서 끝났으므로 위 표는 성공률/안전 성능 표가 아니다. Full factorial과 M0–M3 배치 비교는 미실행이다.

## 3. 계약 검사와 확인된 반례

| 검사 | 실제 확인 내용 | 결과 |
|---|---|---|
| Timestamp maturity | 발행 뒤 target time에만 score 사용, duplicate tick/발행 거절 | PASS |
| Track permutation | 입력 순서를 뒤집어도 ID별 반대 방향 속도와 forecast 보존 | PASS |
| Missing/reappearance | 결측을 0으로 채우지 않음, 재출현 속도는 실제 경과 시간 사용, 건너뛴 target은 사후 위치로 대체하지 않음 | PASS |
| Generation replacement | 같은 slot의 새 generation에 이전 history/score 전달 안 함 | PASS |
| Episode reset | 다른 episode 관측 거절, 새 episode의 pending score 비어 있음 | PASS |
| Issued/clipped radius | 발행한 적용 반경으로 coverage 판정, 나중에 바뀐 내부 반경과 분리 | PASS |
| Terminal/swept collision | 끝점 사이 충돌 검출, terminal pose/path 보존, 자동 reset jump 없음 | PASS |
| Oracle boundary | hidden human goal·future outcome·reaction flag만 바꾸면 동일 관측의 command 동일; 잘못된 issue time 거절 | PASS |
| RNG/clone | calibration RNG 추가 사용이 world stream을 바꾸지 않음, 복제 physics 동일 | PASS |
| Reactive human input | ego 입력 포함 여부가 hand-constructed ORCA 반응을 실제로 바꿈; 새 action 이전 ego 속도를 관측 | PASS |
| Actuation delay/clock | command 2 tick 대기 중에도 human/물리 시간 진행, 실제 FIFO command 적용 | PASS |
| Methods/hysteresis | 같은 33개 action interface, 서로 다른 두 physical tick 뒤 wait 해제, 중복 호출/잘못된 generation 거절 | PASS |
| Smoke/저장 trace | 3개 route event·fork, 저장한 3,000개 prediction ID와 2,760개 성숙 record 독립 재결합, 150 step FIFO/좌표 재계산 | PASS |

두 수작업 반례가 지표의 차이를 드러냈다. Raw 반경 2 m를 실제 1 m로 clip한 뒤 오차가 1.5 m이면 raw 기준은 covered지만 **적용 반경 기준은 uncovered**다. 또한 두 disc가 tick의 시작/끝에서는 떨어져 있어도 중간 교차 시 clearance는 −0.6 m일 수 있다. 이들은 의도적으로 만든 계약 fixture이며 GenSafeNav의 실측 오류율이나 연구 현상의 크기가 아니다.

초기 검사 뒤 code review에서 **동일 tick의 반복 호출이 hysteresis clear counter를 증가시킬 수 있는 점**을 발견했다. 한 episode의 증가하는 physical tick마다 한 번만 결정하게 수정하고 duplicate-call·generation 반례를 추가했다. 이어 저장 trace의 독립 재결합을 보강하고, 새 command의 예정 실행 시각과 실제 dispatch/적용 command 시각을 별도 필드로 구분해 검사했다. 최종 13개 항목이 모두 통과했다. 네 실행 합계는 600 smoke tick이며, 초기 3개의 중복 payload는 [이력과 hash](./results/run_history.json)로 통합했다. 이전 PASS는 더 좁은 검사 범위였으며 현재 결과를 대신하지 않는다.

## 4. 연구 pilot 전에 남은 일

1. **Fixed margin의 데이터 근거:** M0/M3의 현재 반경은 수작업 fixture다. Development/calibration/test scene family를 분리하고 calibration split에서 추정해야 한다.
2. **Event의 공정성:** nominal route는 대칭이지만, 임의의 fork state에서 좌우의 남은 거리까지 같다고 가정하지 않는다. 공통 prefix·event 이전 종료·경로 길이/진행 손실을 명시한다.
3. **비교 범위:** 단순 지연, fixed margin, rolling quantile, wait/hysteresis 뒤에 남는 전환×반응 변화가 있는지는 아직 모른다. 개별 frame을 독립 표본으로 세지 않는다.
4. **원인·외적 타당성:** shadow calibration과 deployment 비교를 구분한다. 단일 ORCA·정확한 state 관측·새 adapter의 결과는 실제 사람, perception errors, native VLA로 일반화할 수 없다.
5. **이동성:** 같은 컴퓨터의 ARM64 Docker만 실행했다. 다른 컴퓨터/AMD64는 재검사해야 하며 Debian 재빌드는 byte-identical이 아닐 수 있다.

**다음 GAP-P4:** local Docker의 bounded diagnostic pilot을 설계 고정 후 실행한다. 최대 development 12·calibration 24·held-out 12개 scene instance와 M0–M3 × reaction 2 × route event 2 × delay 2의 held-out 비교(최대 384 branch episodes)를 상한으로 둔다. 이는 다음 작업의 상한이며 이번에 실행한 수가 아니다. Exact scene family/seed/hash·calibration 방식·종료/분모·분석 기준을 먼저 고정하고, precondition이 실패하면 학습으로 확대하지 않는다. 새로운 learned method·VLA 학습·실제 사람 실험은 포함하지 않는다.

P2의 full research manifest는 여전히 실행 준비 완료가 아니다. P3의 `executable=true`는 이 문서의 **계약 검사만** 뜻한다. Native VLA는 연결된 task/checkpoint/controller/clock/evaluator packet 전까지 HOLD다.

## 5. 보존과 정리

재실행 안내는 [README](./README.md)를 따른다. 검사 container는 모두 자동 삭제됐고, 불필요한 이번 base-image tag는 제거했다. 재개에 쓰는 전용 runtime image는 보존했다. 최초 cache 필터 요청은 0 B였으나, 이후 이번 build의 정확한 ID 세 개를 각각 지정해 **약461.5 MB**를 회수하고 해당 ID가 사라졌음을 확인했다. 다른 작업의 cache·image·volume은 건드리지 않았다. [정리 기록](./results/cleanup.json).

Registry·tier·사용자 읽기 상태는 변경하지 않는다. 필수 generator/audit/diff 검사, 기존 dirty 파일 보존, 산출물 hash와 임시 snapshot 정리 결과는 [유지보수 검증](./results/maintenance_validation.json)에 기록한다. Git commit/push는 이번 작업에 포함하지 않는다.
