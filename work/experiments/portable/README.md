# Clone 후 Docker 재분석·연구 재개

- Updated: 2026-10-23 KST
- 실행 가능한 범위: **C3의 저장된 logits 재분석**. 새 model forward·robot rollout·학습은 포함하지 않는다.
- 새 native 정책 실험: **HOLD_RESEARCH**. GPU 확보와 별개로 [후보별 재개 조건](../../research_candidates/summaries/README.md)을 충족해야 한다.

## 다른 컴퓨터에서 실행

이 문서·실행 recipe와 `work/experiments/vla_rl_c3_logits/evidence/`의 세 입력 파일이 함께 저장된 Git revision을 clone한다. [게시·검증 기록](../../update/UPDATES_2026-10-23.md)에서 해당 revision을 확인한다. 과거 2026-10-23 ORG-R1 검증 당시에는 uncommitted 상태였으며, 그때의 검사 JSON은 역사적 기록으로 보존한다. 저장소 경로는 고정하지 않으며 공백을 포함한 경로도 처리한다.

```sh
git clone https://github.com/Kim-Yoo-Hyun/PaperReview.git
cd PaperReview
```

로컬 Docker Engine/Desktop 및 POSIX shell이 필요하다. Windows에서는 WSL shell을 사용한다. 아래 명령은 clone한 저장소 루트에서 실행한다. Host Python·pip·NumPy 설치는 필요 없다.

```sh
sh work/experiments/portable/run.sh check
sh work/experiments/portable/run.sh build
sh work/experiments/portable/run.sh test
sh work/experiments/portable/run.sh replay-c3
```

`build`만 이미지/NumPy 다운로드에 네트워크를 사용한다. Python image digest와 NumPy 2.2.6 Linux arm64/amd64 wheel hash를 고정했다. Daemon의 architecture를 기본으로 사용하며 `PAPER_REPLAY_PLATFORM=linux/amd64` 또는 `linux/arm64`를 build/test/replay/clean 앞에 같은 방식으로 지정할 수 있다. 이미지 tag는 architecture별로 분리된다. 재분석은 네트워크 없이 read-only 입력·read-only container에서 실행되며 결과 JSON을 stdout으로 출력한다. 기존 evidence를 덮어쓰지 않는다. 다른 위치의 shell에서도 `sh /path/to/clone/work/experiments/portable/run.sh replay-c3`로 실행할 수 있다.

결과를 보관하려면 원하는 새 파일로 stdout을 리다이렉트한다. 이는 작은 결과 기록이며 패키지·모델의 host 설치가 아니다. 종료 컨테이너는 `--rm`으로 제거된다. 이 작업의 이미지가 불필요해지면 다음을 사용한다. 다른 이미지·volume·전체 build cache는 정리하지 않는다.

```sh
sh work/experiments/portable/run.sh clean
```

## 입력과 검증 계약

| 입력 | 역할 |
|---|---|
| `../vla_rl_c3_logits/evidence/native_logits.npz` | 16개 관측·56개 action token logits·hidden state. SHA256 고정 |
| `../vla_rl_c3_logits/evidence/logits_analysis.json` | 기존 primary score/alias 집계의 비교 기준 |
| `../vla_rl_c3_logits/evidence/tail_audit.json` | 마지막 slot 집중도·alias threshold의 비교 기준 |

`replay_c3.py`는 세 입력 파일의 hash·배열 shape·유한값과 두 command class의 유효 확률을 확인한다. T=1.0/1.6의 총 14개 지표가 기존 결과와 `rtol=1e-9`, `atol=1e-10` 이내에서 일치해야 PASS다. Token index 0–64/65–255의 class mapping은 [원래 decoder/autograd 감사 코드](../vla_rl_c3_logits/audit_tail.py)의 해당 checkpoint 전용 경계다. 다른 controller/checkpoint에 일반화하지 않는다.

이번 재분석은 head score trace·alias mass·slot 집중도만 확인한다. 원래의 checkpoint 다운로드/forward, PPO loss 호출, autograd, SFT label/padding 검토를 재실행하지 않는다. 원래 driver·source hash·runtime manifest는 역사적 실행 근거로 그대로 보존한다. 특히 큰 gripper trace 감소를 전체 chunk·실제 reward-weighted gradient·성공률 개선과 혼동하지 않는다. [기존 결과](../vla_rl_c3_logits/RESULTS.md).

실제 검증 플랫폼·이동 경로 테스트·제한은 [이번 검증 기록](./VALIDATION.md), 작업별 실행 가능 범위는 [resume_catalog.json](./resume_catalog.json)을 따른다. 다른 OS/물리 컴퓨터에서의 cold start를 실행했다고 주장하지 않는다.

## Native 연구 실험을 재개하려면

1. [TODO](../../../TODO.md)의 해당 연구 gate를 확인한다. RETIRED/NO-GO/HOLD는 자동 해제하지 않는다.
2. Source/episode identity, task·관측·action/시간 단위, split/reset, 단순 baseline, 독립 outcome, 기각 조건을 채운다. 과거 spec의 `executable=false`를 자원 확보만으로 true로 바꾸지 않는다.
3. 일관된 repository commit·checkpoint revision·파일 hash·normalizer·controller·evaluator와 Docker recipe를 고정한다. 기존 C3 forward driver는 `/tmp/c3_logits`와 실행 당시 확보한 자산에 의존하므로 이 replay와 같은 cold-start 보장을 하지 않는다.
4. 선택한 컴퓨터의 로컬 Docker에서 장치·메모리·native baseline의 기본 능력부터 검증한다. GPU 접근 성공은 full runtime·정책 competence 검증이 아니다. 실패하면 그 범위에서 멈춘다.
5. 최소 비교를 실행하고 실제 명령·image ID·seed·reset·trial 분모·원시 결과를 새 run 경로에 기록한다. 기존 실험 근거는 덮어쓰지 않는다.

Docker Desktop의 일반 `--gpus` Linux-container passthrough는 공식 문서상 Windows WSL2 경로다. 이 Mac의 ARM Docker에서 CUDA가 자동 제공된다고 가정하지 않는다. Linux GPU host도 해당 장치의 Docker runtime 구성이 선행되어야 한다. 현재 task에는 host driver/runtime 설치·원격/cloud 실행을 포함하지 않았다. [Docker GPU 안내](https://docs.docker.com/desktop/features/gpu/).

입력은 repository-relative 위치에서 찾아 read-only bind mount하며, Docker daemon은 선택한 컴퓨터의 로컬 endpoint만 허용한다. 이미지 digest 고정은 실행 환경의 변동을 줄이기 위한 것으로, 향후 dependency 갱신 시 별도 재검증한다. [Bind mount 공식 문서](https://docs.docker.com/engine/storage/bind-mounts/), [이미지 고정 지침](https://docs.docker.com/build/building/best-practices/#pin-base-image-versions). 참고 확인일: 2026-10-23.
