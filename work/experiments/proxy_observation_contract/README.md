# 관측 정보 계약

VideoUnmask에서 장면 색 배치를 바꿔도 지시의 목표가 같은 물체에 연결되는지 확인한다. 2026년 10월 25일 Linux ARM64 Docker에서 소스와 합성 입력을 사용한 검사 17개가 통과했다. 시뮬레이터 장면 수집과 VLA 추론·학습은 미실행이다. [동결한 범위](./PROTOCOL.json) · [원본 버전·해시](./sources.lock.json) · [검사 결과](./results/verified/contract_report.json)

## 다른 컴퓨터에서 재실행

저장소 루트에서 다음 명령으로 로컬 Docker의 소스 검사를 실행한다. 결과는 비어 있는 새 경로에 쓴다.

```sh
sh work/experiments/proxy_observation_contract/run_contract.sh /tmp/gap-n3-check-new
```

첫 컨테이너에서 고정한 원본 세 파일을 받고 두 번째 컨테이너에서 네트워크를 끈 채 검사한다. 원본 해시가 다르면 중단한다. 실행에 성공하면 `contract_report.json`, `source_repair.patch`, `fixture_plan.json`이 생성된다. [실행기](./run_contract.sh) · [검사 코드](./test_contract.py) · [패치와 적용 해시](./results/verified/patch_application.json)

소스 검사는 세 색의 여섯 순열에서 목표 연결을 대조했다. 원시 표본 ID·시간 정렬과 메모리 마스크는 합성 입력에서 검사했다. 보조 지표는 로봇 말단이 지정된 상자 중심에서 수평 4 cm, 상대 높이 2–12 cm 구간에 연속 두 스텝 들어오는 사건이다. 실제 궤적에서 이 지표와 과제 성공의 관계는 아직 측정되지 않았다. [검사 인터페이스](./fixture_api.py) · [적용한 패치](./results/verified/source_repair.patch)

<a id="native-environment"></a>

## 시뮬레이터 재개 환경

당시 macOS ARM64의 Docker GPU 할당은 종료 코드 125로 실패했다. 다른 컴퓨터에서 재개할 대상은 Linux x86_64의 로컬 Docker, NVIDIA GPU 한 대, CUDA와 Vulkan 그래픽을 모두 제공하는 드라이버다. 실제 GPU 메모리 요구량은 미측정이다. [당시 환경 검사](./results/verified/runtime_check.json) · [전체 버전·마운트·공식 출처](./ENVIRONMENT_PROFILE.json)

| 범위 | 고정한 값 또는 재개 시 확인할 값 |
|---|---|
| 소스 | RoboMME `1babf64480e28320e0f9db7992554616ceefda0e`에 검증한 패치를 적용하고, ManiSkill 포크 `07be6fbc66350ddca200abfb0a11b692f078f7fd`와 저자의 `uv.lock`을 사용한다. [저자 Dockerfile](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/Dockerfile) |
| 이미지 | `nvidia/cuda:12.8.0-cudnn-runtime-ubuntu24.04`, Python 3.11, uv 0.8.17. 컨테이너 안에서 `uv sync --frozen --no-dev --group server --python 3.11`. SAPIEN 3.0.2, mplib 0.1.1, Torch 2.9.1. [저자 lock](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/uv.lock) |
| 그래픽·입출력 | `NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video`, `SAPIEN_RENDER_DEVICE=cuda`, `XDG_RUNTIME_DIR=/tmp/runtime-root`. 컨테이너 실행 사용자가 런타임 디렉토리를 소유하며 권한은 `0700`이다. 저자 Dockerfile의 `libvulkan1`, `vulkan-tools`, `libegl1`, `libgl1`을 확인한다. 장면 자산 `/assets`, 저장소 `/workspace/paper_registry:ro`, 결과는 새 `/runs` 경로를 사용한다. |
| 초기 운영 예산 | 호스트 RAM 32 GiB·여유 저장공간 40 GiB, 첫 컨테이너 4 CPU·8 GiB·공유 메모리 1 GiB를 제안했다. GPU 모델·드라이버·UUID, 실제 최고 RAM·VRAM·시뮬레이션 주파수는 현장에서 기록한다. |

**다음 검증**은 실제 장면 한 개의 세 가지 색 순열이다. `VideoUnmask/easy`, `panda_wristcam`, `pd_joint_pos`, 시드 21000, 고정 목표 `red`에서 시연 종료와 첫 정책 결정 시각의 RGB·고유수용감각·물체 자세를 대조한다. 장면 수집기·비교 허용오차·종료 조건과 자산 준비는 구현이 남아 있다. [계획된 장면과 순열](./results/verified/fixture_plan.json)

아래는 소스·패치로 이미지를 빌드하고 실제 이미지 ID를 확보한 뒤 확인할 명령이다. 먼저 GPU 할당과 Vulkan 장치, CUDA 연산을 검사하고 이어서 장면 초기화·렌더링으로 넘어간다.

```sh
# 사용자 선택 Linux GPU 컴퓨터에서만 실행. 값이 없으면 중단한다.
: "${N3_NATIVE_IMAGE:?Set the built native image ID or digest first}"

docker run --rm --gpus device=0 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  "$N3_NATIVE_IMAGE" nvidia-smi

docker run --rm --gpus device=0 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  "$N3_NATIVE_IMAGE" vulkaninfo --summary

docker run --rm -i --gpus device=0 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  "$N3_NATIVE_IMAGE" /app/.venv/bin/python - <<'PY'
import importlib.metadata as md
import torch
for name in ('mani-skill', 'sapien', 'mplib', 'torch', 'torchvision', 'numpy'):
    print(name, md.version(name))
print('torch_cuda_build', torch.version.cuda)
assert torch.cuda.is_available(), 'CUDA unavailable'
print('selected_gpu', torch.cuda.get_device_name(0))
x = torch.ones(1, device='cuda:0')
assert x.sum().item() == 1
PY
```

실제 표본 ID와 HDF5–행동 시각 연결, 정책 텐서·체크포인트·정규화 설정은 후속 단계다. 정책 환경은 별도 이미지로 정의하며 고정한 정책 소스는 `ac846a9a4aec841e483b1dc5d620dfe426bde853`이다. [정책 의존성](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/pyproject.toml) · [연구 판정과 재개 근거](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/PROXY_SELECTION_IDENTIFIABILITY_REVIEW_2026-10-26.md)
