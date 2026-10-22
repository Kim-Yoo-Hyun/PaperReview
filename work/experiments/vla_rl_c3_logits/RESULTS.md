# C3 실제 checkpoint logits 진단

- 작성: 2026-10-21 KST
- 상태: **실제 checkpoint 진단 완료. C3 본격 학습 주제로의 우선순위를 낮춤. 마지막 slot의 국소적 현상은 보존.**
- [후보](../../research_candidates/2026-10-21_execution_interface/README.md) · [동결 계약](../../research_candidates/2026-10-21_execution_interface/LOGITS_PROTOCOL.md) · [이전 synthetic mechanism 검사](../vla_rl_c3_interface/RESULTS.md)

## 질문과 판정 범위

같은 binary gripper 명령으로 변환되는 token들의 확률이 실제 pretrained VLA에서도 여러 token에 분산되어 있는가? 이전 synthetic 검사에서 드러난 clipping·score variance 차이가 실제 checkpoint 분포에서도 큰 영향을 줄 가능성이 있는지를 검사한다.

이 검사는 **실제 가중치의 forward와 조건부 분포 분석**이다. Rollout return, actual old/new RL update, 성공률, 학습 sample efficiency는 측정하지 않는다. Score covariance는 return을 곱한 policy-gradient covariance와 다르다.

## 결과와 연구 판단

**현상은 실제 logits에도 존재한다. 그러나 현재 checkpoint·표본에서는 대부분 마지막 gripper slot에 국한되고, 전체 chunk 기준 효과가 작아 일반적인 VLA RL 효율 개선 방법으로 확장할 근거는 약하다.** 기존 CAPG/MPG와의 신규성 문제까지 고려해 본격 학습 투자를 진행하지 않는 판단이다. 이는 모든 VLA나 실제 reward-weighted gradient에 효과가 없다는 반증은 아니다.

| 측정값 | Temperature 1.0 | 공개 recipe의 1.6 |
|---|---:|---:|
| Gripper alias mass 평균 | 0.8038% | 1.2595% |
| Gripper alias mass 중앙값, 확률 단위 | 1.43×10⁻¹² | 1.05×10⁻⁷ |
| Alias mass > 1%인 gripper slot | 4/128 | 6/128 |
| Gripper만 집계한 조건부 head score trace 감소 | 96.526% | 84.650% |
| **56개 token 전체 chunk 기준 head score trace 감소** | **0.4435%** | **0.4962%** |
| 가상 perturbation의 native PPO active clipping 확률 | 0.1863% | 0.2795% |

큰 gripper 상대 감소율만 보고 “RL gradient variance가 85–97% 줄었다”고 쓰면 안 된다. 원래 gripper가 차지하는 전체 chunk head score trace 비중은 각각 0.4594%·0.5862%다. 위 표는 fixed observation의 조건부 score metric이며, **성공률·학습 개선율의 추정치나 상한이 아니다**. [전체 수치](./evidence/logits_analysis.json).

### 사후 확인: 마지막 slot에 집중된 예외

큰 alias mass를 확인한 뒤 slot별로 분해했다. 이는 primary 분석 이후의 **exploratory audit**다.

- Temperature 1.6에서 alias mass > 1%인 6개 위치는 모두 8번째 gripper slot이었다. 제거되는 head score trace의 **99.622%**가 이 마지막 slot에서 나온다. 1.0에서는 **99.995%**다.
- 앞의 일곱 gripper 위치만 marginalize하면 전체 chunk head score trace 감소는 **0.001874%**(1.6), **0.0000214%**(1.0)다.
- 가장 큰 예외는 관측 1, episode 0의 30% frame, 마지막 gripper다. Temperature 1.6에서 “닫기” class 확률은 **99.8345%**인데 대표 token 외 alias mass는 **82.6864%**다. 물리 명령의 불확실성보다 같은 명령 내부 token의 분산이 크다.
- Native input/label extension과 rollout gather/decoder의 AST는 checkpoint에 함께 배포된 코드와 동일했다. `forward`/`generate_action_verl` 차이는 비활성화된 optional proprio projector 연결뿐이다. 별도로 실제 첫 관측의 actor/rollout token 추출도 일치했다. **이 검사가 SFT 학습 당시 label/padding 처리가 올바랐음을 입증하지는 않는다.** 원인은 미확정이다.

[Tail audit](./evidence/tail_audit.json)에 slot별 비중과 source diff를 보존했다. 다음에 재개한다면 학습보다 **마지막 slot의 SFT supervision·padding·checkpoint 계보 감사**가 먼저다. 이 원인이 일반적인 token aliasing 이외의 학습/구현 문제라면 새 method contribution으로 포장하지 않는다.

## 입력과 실행

| 항목 | 고정 내용 |
|---|---|
| Checkpoint | [Openvla-oft-SFT-libero10-trajall](https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero10-trajall/tree/97d6e58bc5fbc402e85bab382e4206bb8e5f0db0), revision `97d6e58bc5fbc402e85bab382e4206bb8e5f0db0` |
| Native code | [SimpleVLA-RL](https://github.com/PRIME-RL/SimpleVLA-RL/tree/7c51662df27b586f9e8a1ab35fcf849f2b8852f9), commit `7c51662df27b586f9e8a1ab35fcf849f2b8852f9` |
| 관측 | [lerobot/libero](https://huggingface.co/datasets/lerobot/libero/tree/a1aaacb7f6cd6ee5fb43120f673cebb0cfea7dd4), revision `a1aaacb7f6cd6ee5fb43120f673cebb0cfea7dd4` |
| 선택 | 처음 식별되는 LIBERO-10 task 2개, 각각 최초 2개 episode, 길이 10/30/60/90% 지점. 총 16개 관측·4개 episode. 선택은 logits를 보기 전에 고정 |
| 데이터 범위 | 두 task 모두 mug 배치와 관련된 LIBERO-10 manipulation. 서로 다른 task family·robot으로 세지 않는다 |
| Policy 입력 | Agent-view 1개, prompt, proprio 없음. Native action placeholder masking. 8×7개 slot의 parallel categorical prediction |
| 전처리 | 이미 회전된 video frame에 추가 회전 없음. Native JPEG encode/decode → Lanczos3 224 resize → TensorFlow center crop → checkpoint image processor |
| 저장/연산 | 원본 BF16 safetensors → exact FP32 cast. 양자화 없음. Native forward와 parameter load/release hook, CPU SDPA |
| 자원 | 로컬 Linux ARM64 Docker, 7 GiB memory·6 CPU. Host dependency 설치 없음 |

Video는 AV1로 압축되어 원본 RGB와 동일하지 않다. [공식 LeRobot 설명](https://github.com/huggingface/lerobot/blob/afbf3f14a13bdad3e5990e2bed629c6539605658/docs/source/libero.mdx)과 [rotation 설명](https://github.com/huggingface/lerobot/blob/afbf3f14a13bdad3e5990e2bed629c6539605658/docs/source/env_processor.mdx)을 확인했다. [선택 manifest](./evidence/observation_manifest.json)에 episode/frame, input token, image·video·전처리 tensor hash를 기록한다.

## 실제 실행과 수치 검증

- 원 가중치 **15,082,600,832 bytes**, 4 shard의 SHA256을 pinned Hub metadata와 대조했다. **7,541,237,184 parameters / 982 tensors**의 key·shape가 모두 일치했다. Missing/unexpected key는 0이다.
- Native checkpoint `forward` **3회, 총 16개 관측**을 계산했다. 배치는 1·7·8개이며 시간은 29.83·150.60·179.32초, 전체 추론 driver는 **360.56초**였다. Peak process RSS는 약 **6.82 GiB**, OOM/kill은 0이다. [실행 기록](./evidence/forward_runtime.json), [환경](./evidence/runtime_environment.json).
- 첫 decoder layer의 resident/streamed 실행 출력 차이는 **0**이었다. Actual LM output을 이용한 native rollout gather/argmax/decoder와 actor 추출 token ID도 일치했다. 두 경로를 별도 전체 forward로 재실행했다는 뜻은 아니다.
- 실제 checkpoint head weight와 저장된 hidden state로 logits를 독립 재계산한 최대 차이는 **5.77×10⁻⁵**였다. 네 위치의 token/class log-probability에 대해 autograd와 analytical head gradient의 최대 오차는 **5.59×10⁻¹⁵** 이하였다. [독립 수치 검사](./evidence/numerical_validation.json).
- FP32 logits에서 분석 확률은 FP64 softmax로 계산했다. Alias mass는 작은 값을 보존하도록 대표 token을 제외한 확률의 합으로 계산한다.
- [원본 logits와 hidden-state evidence](./evidence/native_logits.npz), [입력/source hash](./evidence/input_source_hashes.json), [전처리 검사](./evidence/preprocessing_audit.json), [패키지 버전 목록](./evidence/packages.txt)을 보존했다. 원본 모델·video·dependency 자체는 host에 설치하지 않았다.

## 지표 해석

실행 class `c`의 확률은 `P_c=Σ[i∈c]p_i`, 조건부 token 확률은 `q_c(i)=p_i/P_c`다.

- **Alias mass:** `1−Σ_c max[i∈c] p_i`. 각 class 대표 token 외에 남아 있는 전체 확률이다.
- **Raw score:** `s_i=e_i−p`. **Class score:** `s_c=q_c−p`. Temperature를 적용한 logit 좌표에서 fixed observation의 기대값은 모두 0이며, covariance trace를 정확한 유한합으로 계산한다. 원 model logit/weight에 대한 미분에는 아래의 `1/T²`가 추가된다.
- **최종 linear head:** 저장된 hidden state `h`에 대해 score trace에 `||h||²/T²`를 곱한다. Native model parameter의 마지막 head까지의 값이며 backbone gradient가 아니다.
- **전체 chunk에서의 비중:** 해당 구현의 56개 독립 categorical draw에 대한 조건부 head score trace를 합산한다. Gripper 8개 위치만 집계한 큰 상대 감소율을 전체 policy 효과로 오인하지 않기 위한 범위 검사다. Return을 곱하면 token 간 상관이 생길 수 있으므로 실제 RL gradient variance를 대신하지 않는다.
- **Clipping stress test:** 실제 `p`에서 class 안 token 순서별 ×0.4/×1.6 tilt 후 원래 class mass로 재정규화한다. Native loss의 `[0.8,1.28]` clip을 사용하며, advantage는 가상의 centered close-command reward다. 실제 학습 업데이트가 아니다. Token 개수 비율 대신 `p`로 가중한 clipping 빈도를 보고한다.

128개 gripper slot은 16개 관측에 종속되어 있다. 이를 128개 독립 trial로 취급하거나 통계적 유의성을 주장하지 않는다.

## 재현 경로

작성한 driver는 [가중치·source 확보](./fetch_assets.py), [입력 선택과 전처리](./prepare_observations.py), [원본 forward](./native_forward.py), [분포 분석](./analyze_logits.py)이다. 중간 전송을 재개한 [range downloader](./resume_weights.py)는 기존 연속 prefix만 대상으로 하며, 중단된 sparse range 파일을 완성된 prefix로 오인하지 않도록 guard가 있다.

모든 driver는 Docker 내부 `/tmp`에 복사하여 실행한다. `prepare_observations.py`가 입력 manifest를 먼저 기록하고, 네 shard의 SHA256 확인 후 `native_forward.py`, 이어서 `analyze_logits.py`를 실행한다. 모델·원 데이터·패키지를 repository에 설치하지 않는다.

사후 [tail/수치 감사 driver](./audit_tail.py)도 Docker에서 실행했다. 입력·forward·analysis·tail driver는 현재 파일과 실행된 파일의 hash가 일치한다. `fetch_assets.py`는 이번의 분리된 metadata/source 확보 절차를 최종 파일에 통합했고, range 재시작 guard도 실행 후 보완했다. **정리된 전체 cold-start download 경로를 다시 실행하지는 않았다.** 결과 검증은 실제 다운로드 receipt·source hash와 실행 evidence에 근거한다.

Container에서 복사한 evidence 14개와 최종 driver 5개의 hash를 대조했다. [복사 검증](./evidence/copy_verification.json). 자원 정리와 repository 검증은 [종료 manifest](./runtime_manifest.json)에 기록한다.

이번 container·image와 내부 가중치·원 데이터·package cache는 삭제했다. 종료 확인 시 container 0·image 0, 기존 `minikube` volume은 보존했다. Registry generation·audit·`git diff --check`를 통과했고, 보호한 기존 notes/registry/tier/tracker/history 4,876개 hash는 바뀌지 않았다. Registry 974편과 모든 tier membership은 유지했다.

## 아직 측정하지 않은 항목

- GPU BF16 reference와 CPU FP32 forward의 수치 비교.
- SFT `trajall` checkpoint와 demonstration 데이터의 개별 training overlap 및 마지막 slot의 학습 label/padding provenance.
- On-policy 또는 failure/transition 상태의 coverage와 실제 advantage.
- Native PPO 대 MPG/class PPO 대 binary head의 공정한 학습 비교.
- 다른 checkpoint, robot/controller, continuous-grip interface에서의 재현성.
- 실제 로봇 성공률·sample cost·안전성 개선.
