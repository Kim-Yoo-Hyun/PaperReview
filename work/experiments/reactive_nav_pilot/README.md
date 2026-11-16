# GAP-P4 — 반응형 navigation bounded pilot

- Updated: 2026-10-24 KST
- **완료:** 개발12·calibration24·held-out12 scene, 384개 branch 비교. 판정은 **주 가설 미지지 / 현재 진단 HOLD / 일반 방법 NO-GO / native VLA HOLD**다. [결과와 한계](./RESULTS.md).
- 로컬 Linux ARM64 Docker CPU에서 실행했다. Host 설치·GPU·학습·모델/데이터/PDF 다운로드는 없었다.
- P3의 [adapter](../reactive_nav_contract/adapter.py)와 runtime을 그대로 재사용했다. P4는 경로 유지/변경의 의미와 split·calibration·분모를 별도로 동결했다.

| Artifact | 역할 |
|---|---|
| [PROTOCOL.json](./PROTOCOL.json) | 결과 확인 전 동결한 질문·split 생성법·baseline·metric·진행/기각 규칙과 코드 hash |
| [pilot.py](./pilot.py), [analyse.py](./analyse.py) | Docker 전용 실행/분석; 무관한 P3 artifact를 덮어쓰지 않음 |
| [FROZEN_RUN](./results/verified/FROZEN_RUN.json), [TEST_FREEZE](./results/verified/TEST_FREEZE.json) | 실제 split/code/image hash, calibration 완료 후 held-out 실행 전 hash |
| [split](./results/verified/split.json), [calibration](./results/verified/calibration.json) | 48개 고유 instance, 24개 episode의 residual과 horizon별 추정 반경 |
| [episodes](./results/verified/episodes.json), [compressed trace](./results/verified/compact_traces.jsonl.gz) | 384개 branch의 결과, 시각별 관측 위치·위험·coverage 요약 |
| [analysis](./results/verified/analysis.json), [execution](./results/verified/execution.json) | 조건별 분모, scene별 paired interaction, descriptive interval, shadow·단순 대안 비교 |
| [replay.sh](./replay.sh), [replay_analysis.py](./replay_analysis.py) | 저장 결과만 재분석; 새 rollout 0, 원본과 byte 일치 검사 |

## 다른 컴퓨터에서 저장 결과 재분석

저장소를 clone한 뒤 로컬 Docker만 사용한다. Python/RVO를 host에 설치하지 않는다.

```bash
cd work/experiments/reactive_nav_contract
bash run.sh build
bash run.sh check
cd ../reactive_nav_pilot
bash replay.sh
```

새 결과는 `results/reanalysis/`에 저장하고 기존 파일이 있으면 중단한다. 다른 폴더를 지정하려면 `bash replay.sh results/reanalysis-02`를 사용한다. 재분석은 원본 trace의 분모·pair·risk/progress 집계와 분석 JSON byte 일치를 확인한다. Simulator 재실행·native VLA 효과 재현은 아니다. P3 build의 apt snapshot은 고정하지 않았으므로 다른 build의 image ID가 달라질 수 있다. 새 물리 컴퓨터/AMD64 실행은 아직 미검증이다.

## 동결한 pilot 재실행

```bash
bash run.sh run
```

이 경로는 **원래 검증한 정확한 image ID**가 로컬에 있을 때만 실행하며 `results/replay/`에 쓴다. 없으면 중단한다. 다른 image/architecture에서 새 rollout을 하려면 P3 계약 검사를 통과하고 **별도 protocol revision**에 실제 image ID·runtime·code hash를 동결해야 한다. 기존 `PROTOCOL.json`·`results/verified/`를 고쳐 이전 근거로 위장하지 않는다. 현재 연구 gate가 HOLD이므로 GPU 확보나 clone만으로 추가 scene/학습 sweep을 시작하지 않는다.

컨테이너는 `--rm`으로 제거한다. 기존 P3 image는 재분석/계약 검사에도 쓰므로 보존한다. 새 전용 image·build cache·외부 payload는 만들지 않았다.
