# C1: native VLA 실행 전제 확인

- 설계 2026-10-20 / 실행 종료 2026-10-21 / 새 후보의 prerequisite probe
- **[결과: 243 actions 후 시간 제한, task competence 미확인](./RESULTS.md).** 실행 자원은 정리했으며 큰 후속 실험·RL 학습은 보류한다.
- 연구 연결: [C1 후보](../../research_candidates/2026-10-20_vla_rl/CANDIDATES.md)
- 범위: 기존 SmolVLA LIBERO checkpoint의 load·입출력·native task 실행과 처리량 확인.
- Active-perception selector·RL 학습·카메라 변경은 구현하지 않는다. 이 결과는 C1의 효과나 신규성 검증이 아니다.

## 먼저 고정한 조건

| 항목 | 값 |
|---|---|
| Policy | `HuggingFaceVLA/smolvla_libero`, revision `6721902bc4d61e50a3bfdb11dfb4cb626f05d102` |
| VLM config/tokenizer | `HuggingFaceTB/SmolVLM2-500M-Video-Instruct`, revision `7b375e1b73b11138ff12fe22c8f2822d8fe03467`. Checkpoint의 `SmolVLM2-500M-Instruct` 주소가 이 repository로 redirect됨을 확인 |
| LeRobot | `7e241bd630a3719a56157a497ce5d08f244784f1` / v0.6.1 |
| LIBERO implementation | Hugging Face fork `8561c60eea2fb93096146f240194649df73d8b1e` |
| Simulator assets | `lerobot/libero-assets`, revision `0b3ea86be5fe169d0fd036ae63d1070ec09e90f6`; demonstration dataset은 사용하지 않음 |
| 주요 dependency | CPU index의 torch 2.11.0+cpu / torchvision 0.26.0+cpu / MuJoCo 3.3.2 / build용 CMake 3.31.10 |
| 환경 | 현재 컴퓨터의 Linux ARM64 Docker, CPU, OSMesa; host 실행·패키지 설치 없음 |
| Native tasks | `libero_spatial/0`, `libero_goal/0`, task order 0 |
| 초기 상태 | 각 task의 prescribed init-state index 0, seed 71000/72000; development 전용 |
| 입력 | native scene+wrist RGB 256×256, 8D proprio, 원래 task instruction |
| 전처리 | LeRobot의 LIBERO processor, checkpoint의 normalizer/tokenizer; image flip 1회 |
| Action | native 7D relative OSC; 20 Hz, `chunk_size=50`, `n_action_steps=1`, flow steps 10 유지 |
| 예산 | 최대 2 episodes, 각각 280/300 control steps; model load 이후 action 시작 전 전체 900초 검사. 실행 중 action 완료분은 초과 가능 |
| 평가 | environment success checker, 실행 action 수, inference 시간, wall time, memory |

Load 시 foundation weight 중복 다운로드만 생략하고 전체 policy checkpoint를 strict load한다. CPU에서 float32로 평가하며 원 CUDA/bfloat16 결과와 수치적으로 같다고 주장하지 않는다. Dataset이나 새 학습 head는 만들지 않는다.

20 Hz는 simulator control period이며 CPU의 실제 추론 처리율을 뜻하지 않는다. Native qualification은 선택한 기존 benchmark 조건의 실행 전제 확인이고 새로운 가림·시점·instruction 일반화 평가가 아니다. Training provenance가 불완전하므로 정확한 in-distribution 여부도 확정하지 않는다.

이 checkpoint의 model card에는 task별 성공률과 평가 recipe가 없어, config의 실행 길이 1을 사용한다. LeRobot 문서의 π0.5용 실행 길이 10을 SmolVLA에 적용하지 않았다. [근거와 제한](../../research_candidates/2026-10-20_vla_rl/C1_REVIEW.md).

## 판정

- 성공한 소수 episode도 native competence qualification 통과로 간주하지 않는다.
- 시간·메모리 제한에 도달한 episode는 `budget_exhausted`로 기록하며 실패 성공률의 분모에 섞지 않는다.
- Import·shape·normalization이 실패하면 오류를 남기고 중단한다. 임의 입력·random head로 대체하지 않는다.
- 후속 20개 이상 상태의 base competence와 C1 branch 비교는 별도 gate다.

패키지·외부 source·checkpoint는 전용 image/volume에만 저장한다. Host에는 이 명세·자체 probe source·작은 결과만 둔다. 종료된 cross-embodiment 자원을 복구하지 않는다.

## 실행 경로

Repository root에서 아래 경로로 실행한다. 동일 이름의 실행 중 container가 있으면 중복 실행하지 않는다. 결과는 volume의 `/artifacts/native_probe.json`에 기록된다.

```bash
docker build --label paper-project=c1-native-probe \
  -t vla-rl-c1-probe:20261020 work/experiments/vla_rl_active_handoff
docker volume create --label paper-project=c1-native-probe vla-rl-c1-artifacts
docker run --name vla-rl-c1-probe --label paper-project=c1-native-probe \
  --memory=7g --cpus=6 \
  --mount type=volume,src=vla-rl-c1-artifacts,dst=/artifacts \
  --mount "type=bind,src=$PWD/work/experiments/vla_rl_active_handoff,dst=/probe,readonly" \
  vla-rl-c1-probe:20261020
```
