# 시행 간 영향 재현

2026-11-19 KST에 현재 Mac의 로컬 CPU Docker에서 평면 로봇팔의 서랍 조작, 공개 문 기구의 복원, 공개 Panda SAC 정책 두 개의 문 열기를 실행했다. 세 검사는 NVIDIA GPU를 사용하지 않는다. [질문과 판정](../내용/README.md) · [서랍·문 기구 원자료](./results.json) · [Panda 정책 원자료](./panda_results.json)

## 다른 컴퓨터에서 실행

로컬 Docker 데몬을 시작하고 저장소 루트에서 다음 명령을 실행한다. Docker Desktop이 꺼져 있는 컴퓨터에서는 `docker desktop start`를 사용할 수 있다. 첫 빌드는 Python 이미지, 고정 버전의 휠과 공개 문 XML을 받기 위해 인터넷을 사용한다. 이후 시뮬레이션 컨테이너는 네트워크 없이 실행한다. 출력 경로는 새 파일이어야 한다.

```sh
pilot_dir='work/research_topics/reset_carryover/재현 방법'
result_dir=$(mktemp -d)
sh "$pilot_dir/run.sh" "$result_dir/results.json"
```

[실행 스크립트](./run.sh)는 로컬 Docker 소켓을 확인하고 이미지를 빌드한다. 기본 시행을 두 번 실행해 결과가 바이트 단위로 일치하는지 검사한다. 시간 간격·닫기 동작 대조와 공개 문 검사까지 통과하면 네 결과를 JSON 하나로 저장한다. 각 블록의 여덟 배정 조합, 시행 중복·누락, 유한 측정값과 집계 일치를 검사한다. 동일 실행 환경에서 저장본과 비교할 때는 다음을 사용한다. 아키텍처가 다르면 결과에 기록된 환경명과 부동소수점값도 달라질 수 있다.

```sh
docker run --rm -i --network none registry-reset-carryover:pilot-1 check < "$pilot_dir/results.json"
cmp "$pilot_dir/results.json" "$result_dir/results.json"
```

| 단계 | 필요한 자원 | 이번에 확인한 범위 |
|---|---|---|
| 서랍·문 시뮬레이션과 분석 | 로컬 Linux 컨테이너, CPU 1개 할당, 컨테이너당 메모리 상한 512 MiB. 디스플레이·CUDA·GPU 패스스루 불필요 | Docker 28.3.3, VM `linux/aarch64`, Python 3.12.16, MuJoCo 3.3.7, NumPy 2.2.6으로 실행. 호스트 ARM64/16 GiB, Docker VM 약 7.65 GiB. `linux/amd64`용 이미지·휠도 게시되어 있으며 이번 실측은 ARM64 |
| 공개 Panda 문 열기 | CPU Linux x86-64 컨테이너. ARM64 Mac에서는 Docker Desktop의 x86-64 실행 지원. 4개 worker로 실행할 때 CPU 4개·메모리 상한 5 GiB | 46차원 관측, 7차원 행동, 공개 체크포인트 2개, 장면 4개. MuJoCo 2.0·robosuite 1.0.1에서 정책 추론과 물리 실행 |
| 향후 실물 확인 | 학교 로봇팔·호환 제어 인터페이스, 독립적인 기계 상태 계측, 실험실 사용 시간 | G1·5090은 현재 물리 가설의 필수 장비가 아니다. 실물 명령·계측 0회 |
| 추후 CUDA 전용 정책이나 GPU 기반 시뮬레이터를 선택할 경우 | 해당 구현이 요구하는 NVIDIA 드라이버·CUDA·Docker GPU 패스스루와 5090 지원 빌드 | 그 구현을 선택했을 때만 학교 컴퓨터에서 컨테이너 내부 GPU 인식과 실제 모델 연산을 확인한다. 5090 호환성은 이번에 측정하지 않았다. [NVIDIA 컨테이너 검증](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html) |

[Dockerfile](./Dockerfile)에 Python 베이스의 다중 아키텍처 다이제스트와 의존성 버전을 고정했다. 공개 XML은 robosuite 커밋과 SHA-256을 고정하고 빌드 및 로드 때 내용을 확인한다. 서랍에는 외부 모델·가중치·정규화기·메시가 필요 없다. 호스트에 실험 패키지를 설치하지 않는다. [MuJoCo 3.3.7 배포](https://pypi.org/project/mujoco/3.3.7/) · [MuJoCo의 관절·텐던 정의](https://mujoco.readthedocs.io/en/3.3.7/XMLreference.html#tendon-fixed)

## 서랍 시행

1. [drawer.xml](./drawer.xml)은 길이 0.16 m인 두 링크, 이상적으로 손잡이를 잡고 있는 구속, 레일 위 서랍과 내부 마찰 슬라이더를 정의한다. 내부 슬라이더와 서랍의 상대 변위에 160 N/m 스프링이 작용한다. 카메라·손가락 접촉·걸쇠 파손·실측 재료 계수는 모델링하지 않았다.
2. [simulate.py](./simulate.py)의 기본값은 시드 `20261119`, 물성 블록 6개, 적분 간격 2 ms다. 블록별 레일 마찰력은 0.7~1.1 N, 내부 슬라이더 마찰력은 1.7~2.3 N 구간에서 표집한다. 각 블록 안에서 모든 조건에 같은 값을 쓴다. 이 범위와 아래 게이트는 이 파일럿의 설계값이다.
3. 매 쌍을 독립 초기 상태에서 시작한다. 직전 정책이 0.8초 동안 열고 1초 동안 닫는다. A는 축 방향 힘 상한 5.5 N과 닫기 목표 0 mm, B는 9 N과 −26 mm를 사용한다. 일반·기준 리셋 모두 0.6초 중앙 구속 후 해제한다. 기준 리셋에서는 내부 슬라이더도 중앙에 구속한다. 정책 ID로 숨은 상태값을 대입하지 않는다.
4. 현재 정책의 시작 좌표와 속도 허용 범위는 ±0.5 mm, ±1 mm/s다. 밖에 있는 쌍도 기록하고 집계한다. 스프링 저항은 개방을 방해하는 방향을 양수로 한 `k × (서랍 위치 − 내부 슬라이더 위치)`다. 이 값은 진단용 정답이고 정책은 팔 관절로 계산한 손 위치·속도만 쓴다.
5. 주 지표는 현재 정책이 0.8초 안에 처음으로 45 mm 이상에 도달했는지다. 보조 지표는 시작 저항 및 **시작 기준 좌표로부터 0.2초의 서랍 위치**다. 직전 B와 A의 차이를 같은 현재 정책·리셋·물성에서 비교한다. 정책 선택 지표는 직전 정책을 50:50으로 섞은 뒤의 현재 B−A 성공률 차이다. 0은 동률이다.

| 결과 키 | 실행 구성 | 해석 단위 |
|---|---|---|
| `primary` | 내부 결합 유지 48쌍, 동일 일정의 결합 제거 대조 48쌍 | 6개 물성 블록 × 8조건 × 2모델. 직전·현재가 한 쌍 |
| `half_step` | 동일 입력·시간 길이, 적분 간격만 1 ms | 수치 민감도. 새 기구·독립 표본으로 더하지 않는다 |
| `matched_close` | 어떤 정책이 열었든 직전 닫기에 A의 목표와 힘 상한을 공통 적용 | 정책별 닫기 차이가 기전에 기여했는지 검사 |
| `public_door` | 손잡이 목표 2 × 리셋 2 × 대기 시간 2의 상태 8개 | 별도 자산에서의 기구 측정. 정책 성공 시행 수에 포함하지 않는다 |

기본 시행은 JSON에 배정 순서, 두 마찰값, 준비 동작의 성공, 시작 위치·속도, 시작 저항, 진행 거리·현재 정책 성공을 보존한다. 환경·모델·코드 해시도 함께 들어 있다. 검증한 결과 묶음의 SHA-256은 `6af60b80dcba8641f1555c20d7be7a7c545b332ceb5f9b5e867b6f5f29079dce`다.

## 공개 문 기구

[door_probe.py](./door_probe.py)는 robosuite 1.5.1의 잠금 문 XML에서 렌더링 전용 재질·질감을 제거하고, 원 환경의 라디안 단위와 문 경첩 마찰·감쇠 설정을 적용한다. 문짝 고정용 구속과 기준 리셋용 손잡이 구속을 추가한다. 손잡이 목표 ±0.6 rad를 0.4초간 최대 1 N·m로 추종한 뒤 외력을 푼다. 일반 리셋은 문짝만 맞추고, 기준 리셋은 손잡이도 맞춘다. 처음 0.6초 검사에서 손잡이 각속도가 남아 있어 양 조건 모두 3.0초로 대기를 늘린 대조를 추가했다. 출력에는 실제 도달각, 해제 직후 측정한 문·손잡이 각도, 손잡이 속도·기준점의 3D 좌표가 있다. 이 실험의 `ordinary`는 직접 구성한 물리적 복원이다. robosuite가 기본 제공하는 `env.reset()`은 시뮬레이터를 재생성하거나 초기화한다. [잠금 자산](https://github.com/ARISE-Initiative/robosuite/blob/a071383d53568ab798eb315c0e95357911be922d/robosuite/models/assets/objects/door_lock.xml) · [원 환경의 기구 설정](https://github.com/ARISE-Initiative/robosuite/blob/a071383d53568ab798eb315c0e95357911be922d/robosuite/environments/manipulation/door.py#L286) · [기본 리셋](https://github.com/ARISE-Initiative/robosuite/blob/a071383d53568ab798eb315c0e95357911be922d/robosuite/environments/base.py#L270)

<a id="next-sim"></a>

## 공개 Panda 정책 재현

**실행 전 고정한 비교.** 장면 시드 1101~1104, 학습 시드 17·59, 20 Hz, 최대 500 제어 스텝을 사용한다. 성공은 공식 조건(문 경첩 각도 >0.3 rad)의 최초 도달이다. 독립 초기화에서 각 정책이 적어도 한 장면에서 목표를 달성하는지 먼저 검사한다. 준비 정책은 500스텝까지 실행해 자연스럽게 남긴 손잡이 각도·각속도를 저장한다. 후행 정책에는 같은 장면·팔 자세·닫힌 문짝을 제공한다. 0.6초와 3초의 대기에 대해 손잡이 상태 보존, 관측 가능한 손잡이 상태 정렬, 독립 복원을 비교한다. 비교의 단위는 장면이고 준비 정책에는 같은 비중을 준다. 호환성 오류를 고칠 때 장면·성공 문턱·체크포인트를 바꾸지 않는다.

공식 robosuite v1.0 벤치마크에 공개된 Panda–Door SAC 정책 중 시드 순서상 첫 두 개(17·59)를 선정했다. 두 `variant.json`에 같은 Panda, `OSC_POSE`, 20 Hz, horizon 500, 은닉층 [256, 256]이 기록돼 있다. 원본 `params.pkl`의 바이트 해시를 각각 확인했다. [시드 17 배포 경로](https://github.com/ARISE-Initiative/robosuite-benchmark/tree/b229f7442f3590dd0e0cad21dc6ae52f410a34bc/runs/Door-Panda-OSC-POSE-SEED17) · [시드 59 배포 경로](https://github.com/ARISE-Initiative/robosuite-benchmark/tree/b229f7442f3590dd0e0cad21dc6ae52f410a34bc/runs/Door-Panda-OSC-POSE-SEED59)

| 시드 | `params.pkl` SHA-256 | `variant.json` SHA-256 |
|---|---|---|
| 17 | `71c775ddb977eaf6a0d686fc3d156df5c4de12a6ba42cb67255d436acc0e0713` | `eeb0f57046a17c5af184ad84527e2fa1f5e71d0d3415f7ef1ff64258eea4a053` |
| 59 | `46931b453fab158a9bcee26291ee01b8f6f81ca651301a33785a1514b138d779` | `3f511cea79294794b0675fff657965413eeb2c75983a78f39c67e4b91c5b1b1c` |

**공개 코드의 버전 차이.** 2020년 9월 배포 당시 평가기는 기본 `GymWrapper(env)`를 호출한다. 이 래퍼는 환경이 관측 사전에 값을 넣은 순서대로 채택한 항목을 이어 붙인다. 당시 로봇 상태 키는 `robot0_robot-state`다. 이후 개정된 스크립트에 나온 `robot0_proprio-state`를 그대로 쓰면 입력이 달라진다. 체크포인트의 `evaluation/policy`는 RLkit의 결정적 SAC 정책이다. 배포 설정의 `hard_reset=false`는 저자의 독립 평가 스크립트가 `True`로 덮어쓴다. 동작 비교에서는 이 재설정을 따르고 화면과 영상 기록을 끈다. 저자 요구사항은 robosuite의 하한을 지정했으므로 이번 재현에는 공개 배포판 1.0.1을 고정했다. [2020년 평가기](https://github.com/ARISE-Initiative/robosuite-benchmark/blob/09f3d65996c057fd97ddc28ac632c066c674985d/scripts/rollout.py#L48) · [당시 GymWrapper](https://github.com/ARISE-Initiative/robosuite/blob/8fa4ec9c5faa067563af115bc3781abb3369e217/robosuite/wrappers/gym_wrapper.py#L37) · [개정된 평가기](https://github.com/ARISE-Initiative/robosuite-benchmark/blob/b229f7442f3590dd0e0cad21dc6ae52f410a34bc/scripts/rollout.py#L91) · [원 요구사항](https://github.com/ARISE-Initiative/robosuite-benchmark/blob/386afd7af7374b0c739575de89284d28a1325fa5/requirements.txt) · [성공 기준](https://github.com/ARISE-Initiative/robosuite/blob/8fa4ec9c5faa067563af115bc3781abb3369e217/robosuite/environments/door.py#L392)

Linux x86-64용 MuJoCo 2.0과 공개 activation key, `mujoco-py==2.0.2.9`, robosuite 1.0.1, CPU PyTorch 1.4.0을 사용한다. 두 학습 실행의 `git_infos.txt`에 기록된 RLkit 커밋은 `d63dab7008cf4d5b6018db8da97b714718bf8a8a`다. 동봉된 로컬 패치는 진단 출력과 환경 객체 저장에만 관련된다. 원 벤치마크의 Python은 3.7.4이고 컨테이너는 3.7.17이다. 학습 당시 robosuite의 정확한 Git 커밋은 미확인이다. [학습 실행 기록](https://github.com/ARISE-Initiative/robosuite-benchmark/blob/b229f7442f3590dd0e0cad21dc6ae52f410a34bc/runs/Door-Panda-OSC-POSE-SEED17/Door_Panda_OSC_POSE_SEED17_2020_09_13_00_26_44_0000--s-0/git_infos.txt) · [당시 정책 코드](https://github.com/rail-berkeley/rlkit/blob/d63dab7008cf4d5b6018db8da97b714718bf8a8a/rlkit/torch/sac/policies.py#L127) · [MuJoCo 배포·키](https://www.roboti.us/license.html) · [robosuite 배포판](https://pypi.org/project/robosuite/1.0.1/)

저장소 루트에서 아래 명령을 실행한다. `run.sh`는 로컬 Docker 소켓을 검사한다. 이미지는 공개 가중치와 라이브러리, 기구 자산을 포함한다. 시뮬레이션은 네트워크를 끈 컨테이너에서 수행하고 JSON 한 개를 새 경로에 남긴다. 메모리가 제한된 컴퓨터에서는 `PANDA_WORKERS=1`로 장면을 순차 실행할 수 있다. [빌드 정의](./Panda.Dockerfile) · [실행 스크립트](./run.sh) · [평가 코드](./panda_eval.py)

```sh
pilot_dir='work/research_topics/reset_carryover/재현 방법'
result_dir=$(mktemp -d)
sh "$pilot_dir/run.sh" "$result_dir/panda_results.json" panda
```

1. 장면마다 두 정책에 독립적으로 같은 시드를 준다. 문 배치, 전체 관절 위치·속도와 첫 관측의 해시가 두 정책에서 같은지 확인한다. 당시 래퍼가 이어 붙인 로봇 상태 32개와 물체 상태 14개를 원 관측 사전으로 재구성한다. 체크포인트 결정적 행동과 가중치의 NumPy 순전파를 대조한다.
2. 두 준비 정책을 각각 500스텝 실행한다. 처음 성공한 제어 스텝과 **500번째 스텝이 끝난** 손잡이 각도·각속도를 별도로 저장한다. 준비 정책이 목표에 도달한 직후의 값을 종료 상태로 쓰면 다른 조건의 실험이 된다.
3. 중간 리셋에서 장면·Panda·닫힌 문짝 및 컨트롤러를 원래 시작 상태로 되돌린다. 준비 정책의 마지막 손잡이 상태를 넣고, 팔과 문짝을 매 물리 스텝 시작에 고정하면서 원 모델의 걸쇠를 0.6초 또는 3초 움직인다. 대조용으로 준비 정책과 독립된 초기 걸쇠도 같은 시간 동안 움직인다. 아래 네 처치에서 후행 정책의 최초 성공 또는 500스텝 실패까지 기록한다.

| JSON 값 | 후행 정책 시작 시 손잡이 상태 |
|---|---|
| `panel` | 직전 정책에서 온 각도와 각속도가 대기 중 자연스럽게 변한 값을 모두 보존 |
| `angle` | 각도만 독립 복원의 값으로 덮어쓰고 직전 정책에서 온 각속도는 보존. 각도를 순간 설정하는 기전 분리용 처치 |
| `angle_speed` | 각도와 각속도를 모두 같은 시간의 독립 복원값으로 맞춤 |
| `fresh` | 직전 정책의 정보 없이 독립 복원한 뒤 같은 시간 대기 |

이 구현에서 이전 시행으로부터 옮기는 자유도는 걸쇠 하나다. 따라서 `angle_speed`와 `fresh`는 구조상 같은 상태에 도달한다. 동일 장면·현재 정책·정확히 같은 시작 상태는 궤적 한 번을 공유한다. JSON의 `reference`는 실제 준비 시행, `blocks[].trials`는 비교에 배정한 조건, `blocks[].paths`는 중복을 제거한 실제 후행 궤적이다. `summary`는 직전 정책을 균등하게 섞은 성공 수와 성공률 격차를 담는다. 이 리셋은 손잡이를 잡고 문을 닫는 사람이나 로봇의 궤적을 모사하지 않는다.

**실행 검산.** 학습 당시 RLkit으로 저장한 결과 파일의 SHA-256은 `3fac2b21dde7ce296dee70b5f2f83178d9b2b78d71690e5a819e0aec2609f675`다. 벤치마크 저장소의 재생용 RLkit 커밋 `b7f97b2463df1c5a1ecd2d293cfcc7a4971dd0ab`으로도 같은 네 장면을 실행했다. 두 실행에서 첫 관측·행동, 준비 시행 8회, 후행 고유 궤적 80개의 종점·최초 성공 스텝과 8개 조건 집계가 모두 일치했다. 이 재실행은 같은 장면의 검산이다. 공개 벤치마크는 누적 보상도 보고하며, 여기서 비교한 지표는 원 과제 성공 조건의 최초 도달이다. [저장 결과](./panda_results.json) · [벤치마크 설치 지침](https://github.com/ARISE-Initiative/robosuite-benchmark/blob/b229f7442f3590dd0e0cad21dc6ae52f410a34bc/README.md) · [저자의 보상 집계](https://github.com/ARISE-Initiative/robosuite-benchmark/blob/09f3d65996c057fd97ddc28ac632c066c674985d/util/rlkit_utils.py#L205)
