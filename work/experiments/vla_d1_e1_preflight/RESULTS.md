# D1-E1 — Docker G0 resource preflight 결과

- 확인: 2026-10-22 KST.
- 판단: **Resource preflight 수행 / G0 전체 미충족 / G1 미실행 / E1 WAITING_RESOURCE**.
- 설계: [D1-L4 계약](../../research_candidates/2026-10-21_d1_buildup/PRE_EXPERIMENT_CONTRACT.md). 연구 가치 판단 **REVISE**는 유지한다.
- 실제 증거: [Docker probe 결과](./preflight_result.json), [명령·image·asset·cleanup 기록](./preflight_manifest.json), [probe script](./preflight.py). 아래는 성능 실험 결과가 아니다.

## 1. 실제로 실행한 것

현재 컴퓨터의 Docker에서 작은 Python stdlib 컨테이너를 실행했다. OS/device/memory를 읽고, 고정된 OFT source와 공개 모델 metadata·config·normalizer·weight index를 메모리에서 확인했다. 별도로 `--gpus all` device allocation을 요청했으며 daemon에서 실패했다. Upstream code를 import하지 않았고 PyTorch·simulator를 설치하지 않았다.

| 항목 | 실제 확인 결과 | 해석 |
|---|---|---|
| Host | Apple M4 MacBook Pro, 표시 메모리 16 GB, Metal GPU | NVIDIA 장비가 아니며 host MPS로 실행하지 않음 |
| Docker | Desktop 28.3.3, Linux aarch64, 10 CPU, RAM 8,218,034,176 bytes = **7.65 GiB** | Daemon과 일반 컨테이너 실행은 정상 |
| Container GPU | `/dev/nvidia*`, `/dev/dri/*`, `/dev/kfd` 모두 없음 | CUDA 연산 성공을 확인하지 못함 |
| GPU allocation | exit **125**, `could not select device driver` / GPU capability 미충족 | CUDA sample이나 OFT가 실행되기 전의 daemon 실패 |
| Default model tensor storage | Index metadata **15,082,474,368 bytes = 14.05 GiB** | 현재 VM RAM보다 크며 resident native 실행 예산 미확보 |
| 별도 action/proprio sidecar | 파일 저장량 합계 369,517,838 bytes | 추가 자산이며 tensor RAM/최대 메모리 측정값은 아님 |
| Policy forward / simulator step / episode | **0 / 0 / 0** | Clean 성공률·state/goal utility는 null |

주 probe의 cgroup limit은 256 MiB였다. 이는 metadata 검사에 의도적으로 부여한 제한이며 위 **VM 전체 RAM 7.65 GiB**와 혼동하지 않는다. 모델 메모리 비교에는 weight index의 게시된 tensor 저장량을 사용했으며 실제 model loading/OOM/latency를 측정하지 않았다. Swap·paging·offload를 포함한 모든 가능한 CPU 실행이 불가능하다는 결론도 아니다.

Docker 공식 문서는 Linux container의 `--gpus` passthrough를 Windows WSL2 경로로 설명하며, 다른 플랫폼의 Docker Model Runner 가속과 구분한다. Apple GPU가 있다는 사실만으로 이 OFT PyTorch container에 CUDA가 제공되지는 않는다. [Docker 공식 GPU 문서](https://docs.docker.com/desktop/features/gpu/).

## 2. CUDA 필수라는 단정은 수정한다

OFT의 고정 source를 실제로 대조하면 `DEVICE`는 CUDA가 없을 때 CPU를 선택한다. Model load의 명시적 FlashAttention argument는 **주석**이고 BF16 load는 활성화돼 있다. 설치 안내에서 flash-attn은 training용으로 설명한다. 따라서 **“GPU가 없으니 OFT source에 CPU 경로 자체가 없다”는 주장은 틀리다.** [공식 loader](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/openvla_utils.py#L253), [SETUP](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/SETUP.md).

이번 중단 근거는 **현재 고정한 native 평가를 실행·검증할 자원이 확보되지 않았다는 것**이다. 공식 보고 경로는 Python 3.10.14/PyTorch 2.2.0/custom Transformers 4.40.1의 A100 평가이며, 현재 CUDA allocation은 실패하고 기본 tensor 저장량만으로도 현재 VM RAM을 초과한다. CPU fallback의 의존성·full model load·rollout은 검증하지 않았다. 메모리 설정만 높이면 CUDA나 native 재현성이 자동 해결된다고 안내하지 않는다. [저자 LIBERO 재현 안내](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/LIBERO.md#L87).

Docker probe의 Python 3.10.22는 stdlib 검사용이다. 이를 OFT paper 환경의 설치 성공으로 기록하지 않는다. BF16→quantized/CPU-offload 전환, 다른 checkpoint, 작은 새 정책을 사용하지 않았다.

## 3. 자산 확인에서 추가로 해결한 부분

고정 model repository revision `c2d0f9fbbd82674683b397ff923168a12f6a307b`의 파일 목록과 LFS digest를 확인했다. 4개 backbone shard와 Goal 50K action head/proprio projector의 원격 size/digest를 manifest에 남겼다. **큰 weight의 실제 byte hash는 검증하지 않았으며 다운로드하지 않았다.** [공식 model repository](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal/tree/c2d0f9fbbd82674683b397ff923168a12f6a307b).

- **Normalizer 실제 내용 확인:** `dataset_statistics.json` 2,923 bytes를 Docker 메모리에서 읽었다. SHA-256은 `22e0549a346b2ec8a109904d017a57c50f12769b91653939aefb72b119725d47`이다. `libero_goal_no_noops` key, action 7D/proprio 8D, finite 값, q01/q99 순서와 비퇴화 범위를 확인했다. 실제 policy 입력 변환이나 성능은 검사하지 않았다.
- **Config만으로는 부족:** `config.json`의 norm_stats는 base-data 25개 key이며 Goal key가 없다. 별도 statistics 파일에는 Goal key가 있다. Native loader가 외부 statistics로 `vla.norm_stats`를 바꾸므로 두 JSON의 전체 불일치는 곧 잘못된 checkpoint라는 뜻이 아니다. 다음 native gate에서 실제 로딩된 key/hash를 assert해야 한다. [Normalizer loader](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/openvla_utils.py#L352).
- **Source 사본 차이 확인:** HF의 modeling 파일과 code repo 파일은 byte/AST가 다르다. Diff는 diffusion helper에 timestep 설정 호출 하나가 추가된 것이다. 선택한 `use_l1_regression=true, use_diffusion=false`의 해당 helper 경로는 사용하지 않지만 전체 runtime 동등성까지 입증한 것은 아니다.
- **Revision pin 누락:** Native model/processor/statistics/sidecar download 호출은 이번에 기록한 HF revision을 명시적으로 전달하지 않는다. 이후 runner는 모든 자산을 같은 revision에 고정하고 실제 loaded payload/source hash를 검증해야 한다. Repo ID만 넣어 실행한 뒤 pinned 재현이라고 부르면 안 된다. 이 차이를 수정한 runner는 아직 만들지 않았다.

보존한 raw report는 성공한 마지막 probe invocation의 공개 text/작은 JSON **10개, 304,092 bytes**를 기록한다. Source diff·loader 절은 추가 Docker 메모리 읽기로 검토했다. 전체 network traffic의 합계를 304,092 bytes라고 주장하지 않는다. Normalizer/config의 실제 작은 파일 hash와 large weight의 **게시된** LFS hash를 구분했다.

## 4. G0/G1 판정과 재개 조건

| Gate 항목 | 상태 |
|---|---|
| Docker process·read-only probe | PASS |
| GPU allocation | FAIL; native CUDA 실행 아님 |
| 현재 full-precision native resource qualification | 미충족 |
| 작은 config/normalizer identity·구조 확인 | 정적 PASS |
| Weight payload integrity·dependency lock·native load | NOT_RUN |
| Frame/normalization runtime·3회 paired reset·shared-scene 검증 | NOT_RUN |
| G1 clean competence·orientation/goal utility | NOT_RUN |

**E1을 DONE으로 바꾸지 않는다.** 연구 질문이 반증된 것도 아니며, 실행 자원 gate를 통과하지 못한 상태다. 실제 사용자 reading status/REPRODUCED도 승격하지 않는다.

재개하려면 현재 컴퓨터에서 설계에 맞는 native runtime/resource 경로가 새로 확인되거나, 사용자가 실행 범위를 명시적으로 변경한 후 수정 계약을 정해야 한다. 동일 hardware·Docker memory·backend 조건에서 preflight만 반복하지 않는다. 자원이 바뀌면 fresh GPU/CPU route 검증→dependency·weight/source lock→frame/reset→G1 순서로 진행한다. G2나 본격 학습은 아직 진행 조건을 충족하지 않는다. CPU/offload 경로를 따로 검토하더라도 현재 메모리·정책 동일성·실행 비용 검증을 생략할 수 없다.

## 5. 자원 정리와 저장소 보존

이번 전용 컨테이너는 `--rm`으로 종료했고 새로 받은 Python image도 삭제했다. 종료 시 container **0개**, image **0개**를 확인했다. 새 named volume은 만들지 않았고 관련 없는 `minikube` volume은 유지했다. Docker 전체 prune이나 사용자 자원 정리는 하지 않았다.

호스트에는 작성한 probe script·작은 JSON 증거·Markdown만 남겼다. Host package 설치, model weight·dataset·PDF 다운로드, policy 학습/추론은 없다. [저장소 검증 기록](./VALIDATION.md)은 별도이며 native qualification 결과와 구분한다.
