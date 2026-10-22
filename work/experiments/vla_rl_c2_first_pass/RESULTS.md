# C2 1차 검증 결과 — 데이터·실행 전제에서 종료

- 검증일: **2026-10-21 KST**
- 상태: **1차 채택 심사 완료 / 현재 설계 NO-GO.** 정책 효과 검증 완료를 뜻하지 않는다.
- [사전 범위·중단 기준](./PREFLIGHT.md) · [연구 가치 최종 판단](../../research_candidates/2026-10-20_vla_rl/C2_BUILDUP_RESULT.md)
- 실행: 현재 컴퓨터의 ARM64 Docker 안에서 실제 데이터 검사·경유 판정 재계산·의존성 resolver 확인. 모델 추론·학습·simulator rollout은 **0회**.

## 1. 실제로 검사한 범위

| 검사 | 실제 범위 / 결과 |
|---|---|
| Dataset revision | `bbb1e266ed585f1557773de5a3f1e3b4cd944f97` |
| Task·episode 목록과 metadata | Right-arm task 8개 × 50개 = **400 episode**. Metadata/파일 존재 확인이며 400개 성공 시연 검증이 아님 |
| Training instruction payload | **200 JSON**, task별 3개 paraphrase, 서로 다른 텍스트 12개. `unseen` 항목 0개 |
| HDF5 및 planner payload | 학습 4개 task의 episode **0·24·49**, 총 **12개 HDF5 + 12개 pickle**. Pickle은 opcode만 읽고 역직렬화하지 않음 |
| 시계열 기본 검사 | 총 **2,992 frame**, episode당 **204–304 frame**. 12/12 frame 길이 일치·14D joint vector finite |
| 이미지 확인 | 4 camera × 3 frame × 12 episode = **144개 JPEG decode 통과**, 320×240. Native actor에는 기존 3 view만 허용 |
| 데이터 이동 | Docker 내부 cache 약 **188 MB**. Host에는 source/model/data payload를 설치하지 않고 작성한 검사 코드와 작은 evidence report만 보존 |

선택한 12개는 내용을 보기 전에 고정했다. Holdout의 HDF5·planner·instruction payload는 읽지 않았고, holdout metadata는 목록·seed·필드 존재 검사에만 사용했다. Policy 성능에 대한 test set은 소진하지 않았다. 전체 200 training HDF5의 품질을 검사했다고 주장하지 않는다. [실행 기록](./evidence/audit_execution.json), [파일 hash](./evidence/download_manifest.json), [12개 payload 결과](./evidence/payload_audit.json).

## 2. G0: 쓸 수 있는 증거와 부족한 증거

### 부분적으로 통과한 경유 판정

8개 task 가운데 `r_pick3_via4_to6_short_front`와 `r_pick3_via4_to6_long_front`만 각각 50개의 `route_samples`·`route_check` 및 collection metadata를 제공했다. 이 중 C2 training에 속하는 것은 **long_front 한 task, 50개**다. 나머지 training 150개에는 해당 경로 증거가 없다.

학습 50개에 공개 [경유 검사 함수](https://github.com/AutoLab-SAI-SJTU/RoboFollow/blob/f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8/routes.py)를 적용했다. 원래 경유 조건은 **50/50 통과**하며 기록된 판정과 일치했다. Correct/wrong waypoint를 교환하여 다른 **training task** `r_pick3_via5_to6_short_front`의 경유 조건을 검사하면 **50/50 위반**이었다. 이는 **경유 조건에 한정된 counterfactual supervision이 존재한다**는 긍정적인 발견이다. Holdout 지시로 negative를 만들지 않았다.

단, 원 코드의 `_route_initial_z`는 별도로 저장되지 않아 첫 route sample의 source 높이를 사용했다. 저장 판정과의 일치는 확인했지만 첫 sample 이전의 물리 상태를 복원한 것은 아니다. 대체 지시는 orientation도 달라지므로 이 결과를 orientation-only 개입으로 해석하지 않는다. [재계산 결과와 조건](./evidence/first_pass_analysis.json).

### 완전한 보상 비교에는 불충분

- 12개 HDF5의 모든 dataset key를 읽었다. Joint/EEF pose·camera calibration/RGB는 있으나 **조작 물체의 position/quaternion 시계열은 없다**. Point cloud는 모두 `N×0`이다. Planner pickle에서 확인한 필드는 joint position/velocity 경로이며 물체 pose 기록이 아니다.
- Route metadata는 source와 두 waypoint의 position을 제공하지만 **destination의 실제 pose와 source의 quaternion을 제공하지 않는다**. 따라서 계획한 독립 `G` 및 `Cr`, 최종 `G∧Cw∧Cr`을 이 경로로 재계산하지 못했다. RGB의 별도 annotation/perception 또는 native replay를 추가하면 해결할 수 있을지는 이번 결과 밖이다.
- 최신 형식의 metadata도 `upstream_commit=null`, `data_format=if-bench-raw-v1`이며 code digest만 있다. 현재 pinned repository와 동일한 수집 환경이라고 확정할 수 없다. 다른 task의 `{stage}: done`도 완전한 제약 만족 label을 대신하지 않는다.
- 표본 HDF5 12개 중 identity attribute로 task·episode·seed를 확인한 것은 **3개**다. 나머지 9개는 ordered `seed.txt` 매핑을 독립 확인할 attribute가 없다. Attribute 부재를 곧바로 불량 시연으로 해석하지 않는다.
- 유효한 route trace가 있는 training task 하나만 남기면 object·waypoint·orientation의 atomic/pair coverage가 사라진다. 50개의 route negative가 원래 4/4 조합 실험의 성립을 보장하지 않는다.

**G0 판정:** 경유 판정 일부는 검증했으나, 원래 C2의 완전한 reward·coverage·state grouping 계약은 **미충족**이다. Goal-only/complete reward의 실제 차이와 RL의 독립 효과를 측정했다고 보고하지 않는다.

## 3. 분할에서 확인한 위험

Task-level 4/4 parity split의 atomic/pair coverage는 그대로 유효하다. 그러나 task 분리만으로 새로운 scene이 되는 것은 아니다.

- Training의 서로 다른 seed는 85개, holdout은 78개이며 **66개 seed ID가 겹친다**.
- Holdout 200개 중 **188개**의 선언된 seed가 training에도 있다. 실제 full physics state가 동일하다는 증명은 아니며, C2의 새 scene 평가 계약을 그대로 만족한다고 간주할 수 없다는 뜻이다.
- 검사한 training task 세 개의 episode 0은 4개 camera 모두 첫 이미지 hash가 같다. 초기 장면을 공유하는 지시 비교 자체는 의도된 설계다. 이 공통 장면이 train/test 경계를 넘지 않도록 episode group을 따로 고정해야 한다.

실제 evaluation rollout에는 새로운 scene seeds와 전체 상태 hash가 필요하다. 이번 [400행 episode manifest](./evidence/episode_manifest.json)는 inventory/provenance 기록이며, 실행 가능한 split freeze가 아니다. 원 benchmark의 L0 평가를 오류라고 주장하지 않는다. C2가 별도로 요구한 generalization 계약의 문제다.

## 4. G1: 현재 컴퓨터의 reference runtime 검사

Docker daemon은 정상이고 Linux `aarch64`, VM memory 약 7.65 GiB다. 검사 container는 4 CPU·4 GiB로 제한했다. Data reader는 실제 설치·실행에 성공했다. 최초 h5py 3.11.0 설치는 ARM wheel 부재로 source build 단계에서 실패해, 이 데이터 검사에는 wheel이 있는 3.15.1을 사용했다. 이는 simulator package version을 바꿔 실행한 것이 아니다.

| 실제 검사 | 결과 |
|---|---|
| Pinned `sapien==3.0.0b1`, binary-only pip dry-run | **exit 1**, ARM64 matching distribution 없음 |
| Pinned `mplib==0.2.1`, binary-only pip dry-run | **exit 1**, ARM64 matching distribution 없음. PyPI에는 source archive가 있으므로 source build 불가능을 뜻하지 않음 |
| Docker `--gpus all` 실행 요청 | **exit 125**, GPU capability를 제공할 device driver 선택 실패 |
| Container device/driver | `/dev/nvidia0`, `/dev/nvidiactl`, `/dev/dri` 없음, `libcuda.so.1` load 실패 |
| Compatible trained checkpoint 발견 | 공식 README/π0.5 안내는 직접 fine-tuning 경로를 제공. HF의 RoboFollow 검색·저자 모델 목록 및 GitHub releases에서 해당 checkpoint를 식별하지 못함 |

[공식 RoboTwin 설치 안내](https://robotwin-platform.github.io/doc/usage/robotwin-install.html)와 [pinned requirements](https://github.com/RoboTwin-Platform/RoboTwin/blob/6dde57155eafa3e4ebf6ad1f93a7cf7d5d41a755/scripts/requirements.txt)를 기준으로 확인했다. **배포된 reference 경로는 현재 환경에서 성립하지 않았다.** x86 emulation이나 별도 CPU renderer/port를 모두 시험한 것은 아니지만, emulation만으로 CUDA planner와 GPU가 생기지는 않는다. 자산·weights를 먼저 내려받거나 host MPS로 우회하지 않았다. [의존성·checkpoint discovery 원기록](./evidence/runtime_probe.json), [Docker 실행 manifest](./runtime_manifest.json).

## 5. 1차 검증 종료 기준

| Gate | 종료 상태 |
|---|---|
| G0 데이터·predicate | **일부 경유 판정 검증 / 본래 계약 미충족** |
| G1 native runtime·checkpoint | **Reference 경로 미충족** |
| G2 native competence·양쪽 지시 feasibility | **미측정**. 입력 파싱이나 시연의 existence를 대체 증거로 사용하지 않음 |
| G3 SFT/RWI/RL 비교 | **미실행**. 사전 gate에 따라 진입하지 않음 |
| G4 다른 조건·embodiment 일반화 | **미실행** |

현재 설계의 1차 판단을 **NO-GO**로 종료한다. 이는 RL의 이득이 없다는 실험 결과가 아니다. 데이터 계약을 복구하고 native 실행을 새로 확보하는 비용을 들이기 전에, [연구적 차별성에 대한 판단](../../research_candidates/2026-10-20_vla_rl/C2_BUILDUP_RESULT.md)을 우선한다.

## 6. 재검토 가능한 기록

검사 구현은 [prepare_audit.py](./prepare_audit.py), [audit_payloads.py](./audit_payloads.py), [analyze_evidence.py](./analyze_evidence.py), [probe_runtime.py](./probe_runtime.py)다. 순서대로 Docker 내부에서 실행한다. `analyze_evidence.py`는 앞 단계의 raw metadata report를 provenance summary로 축약하므로 단독 반복 실행용이 아니다. 원 payload는 Docker scratch에서만 유지했다.

Image digest·dependency version·script/report hash·GPU 요청 실패·정리 확인은 [runtime_manifest.json](./runtime_manifest.json)에 남겼다. 전용 container와 image, 그 안의 data/source/package cache를 결과 보존 후 삭제했다. 최종 조회에서 container·image·build cache는 0이며 기존 `minikube` volume만 보존했다. [Evidence 무결성 검사](./evidence/validation_report.json)도 통과했다.
