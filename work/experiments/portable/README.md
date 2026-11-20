# C3 로그잇 재분석

한 checkpoint의 관측 16개에서 얻은 저장 로그잇과 head-score 지표를 로컬 Docker에서 재계산한다. [당시 연구 결과](../../research_topics/RESULTS.md#c3)

## 실행

Docker Engine/Desktop과 POSIX 셸이 필요하다. Windows는 WSL을 사용한다. 이 저장소를 clone한 뒤 루트에서 실행한다.

```sh
sh work/experiments/portable/run.sh check
sh work/experiments/portable/run.sh build
sh work/experiments/portable/run.sh test
sh work/experiments/portable/run.sh replay-c3
```

`build`에서 고정 Python image와 NumPy wheel을 가져온다. 입력은 read-only로 마운트되고 `replay-c3`는 네트워크 없이 결과 JSON을 stdout으로 출력한다. `PAPER_REPLAY_PLATFORM=linux/arm64` 또는 `linux/amd64`를 앞에 붙여 플랫폼을 지정할 수 있다. 실행 이미지 제거는 `sh work/experiments/portable/run.sh clean`을 사용한다.

## 입력

| 파일 | 용도 |
|---|---|
| [native_logits.npz](../vla_rl_c3_logits/evidence/native_logits.npz) | 고정 관측의 logits와 hidden state |
| [logits_analysis.json](../vla_rl_c3_logits/evidence/logits_analysis.json) | 기준 score·alias 집계 |
| [tail_audit.json](../vla_rl_c3_logits/evidence/tail_audit.json) | 마지막 slot 집중도와 alias threshold |

세 입력의 SHA256은 [재현 원장](./resume_catalog.json)에 있다. 재생기는 배열·확률과 T=1.0/1.6의 14개 지표를 검사한다. Token index 0–64/65–255의 class mapping은 해당 checkpoint 전용이다. [원 decoder 감사](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/experiments/vla_rl_c3_logits/audit_tail.py)

<a id="validation-2026-10-23"></a>

## 이전 검증

2026-10-23에 ARM64와 AMD64 에뮬레이션에서 build·unit test 4개·기준 지표 14개를 검증했다. 공백이 있는 clone 경로, 입력 변조 거부와 원격 daemon 차단도 확인했다. T=1.6의 전체 trace 감소는 약 0.4962%였고 감소량의 약 99.6224%는 마지막 slot에 집중됐다. 검증 범위는 저장 지표이며 새 모델 추론·정책 학습·실기 rollout은 0회다. [상세 결과](./validation_result.json)
