# 시연 재수집 검증

공개 배포본의 고정 버전에서 실제 시행을 읽고, 시연자 요청과 적용 명령을 각각 복원하거나 확인한다. 2026-11-20 로컬 Docker 28.3.3의 Linux/arm64에서 다섯 자료 검사를 실행했다. CPU 1개와 메모리 640 MiB로 충분했다. 필요한 외부 자원은 공개 파일에 접근하는 인터넷 연결이다. 모델·로봇·NVIDIA GPU는 필요하지 않다. [연구 판정](../내용/README.md)

## 재실행

저장소 루트에서 실행한다. 컨테이너가 표본을 메모리로 읽고 SHA-256을 대조한다. 호스트에 데이터나 패키지를 설치할 단계는 없다.

```bash
docker build -t registry-demo-audit:local 'work/research_topics/demonstration_recollection/재현 방법'
docker run --rm --read-only --cpus 1 --memory 640m --tmpfs /tmp registry-demo-audit:local
```

전체 실행은 자료별 JSON 다섯 줄을 출력하고 종료 코드 0을 반환한다. 한 자료만 다시 보려면 마지막 명령 끝에 `droid`, `shared`, `harmonic`, `copilot`, `geometry` 중 하나를 붙인다. 다운로드·해시·시각 짝짓기 검증에 실패하면 해당 검사에서 중단한다. 입력 URL·세대 번호·해시는 한 파일에서 관리한다. [검산 코드](./audit_samples.py) · [고정 환경](./Dockerfile)

<details>
<summary>2026-11-20 Docker 실행 출력</summary>

```jsonl
{"droid": {"IPRL": {"frames": 459, "enabled": 372, "saturated_translation": 37, "max_abs_error": 1.3877787807814457e-16}, "CLVR": {"frames": 173, "enabled": 125, "saturated_translation": 0, "max_abs_error": 2.7755575615628914e-16}, "TRI": {"frames": 149, "enabled": 143, "saturated_translation": 0, "max_abs_error": 1.3877787807814457e-16}}}
{"shared": {"paired_joint_rows": 98, "direct_demo_shape": [57, 14], "learned_assistance": {"rows": 98, "nonzero_user": 82, "median_interval_s": 0.10104990005493164, "weight_range": [0.34582871198654175, 0.43941229581832886]}, "policy_blending": {"rows": 174, "nonzero_user": 93, "median_interval_s": 0.1011650562286377, "weight_range": [0.5000087194125751, 0.6051342505890182]}}}
{"harmonic": {"control_mode.txt": 1, "ada_joy.csv": 3417, "joint_positions.csv": 7181, "robot_position.csv": 7181, "input_info.csv": 3124, "assistance_info.csv": 3124, "paired_by_timestamp": 3124, "nonzero_user_twist": 1479, "different_twist": 3124}}
{"copilot": {"export_fields": ["action", "observation.state", "observation.images.front", "next.done", "timestamp", "frame_index", "episode_index", "index", "task_index"], "episode": 0, "rows": 836, "action_shape": [836, 8], "state_shape": [836, 8], "last_time_s": 55.66666793823242}}
{"geometry": {"source_x": [13682, 6], "x": [1283, 6], "tool_z": [1283, 3], "target_tool_z": [1283, 3], "monotonic_time_ns": [1283]}}
```

</details>

## 표본과 검산 기준

| 검사 | 고정 표본 | 검산 대상 |
|---|---|---|
| `droid` | 원시 1.0.1의 IPRL 성공 2024-01-01, CLVR 성공 2023-05-09, TRI 실패 2023-08-10 각 한 시행 | `skip_action`과 로봇 이동 허용 여부를 대조한다. 허용된 행에서 원하는 병진 위치와 현재 위치 차이에 이득 5와 단위 크기 상한을 적용하고 저장된 3축 속도와 성분별 절대 오차 10⁻¹² 이내인지 확인한다. 이동이 생략된 행은 별도로 속도 0을 검사한다. [원시 명세](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/docs/the-droid-dataset.md) |
| `shared` | IROS 2021 저장소의 `user1/demos/final_n_1`, `runs/final_n_1`, `policy_blending/n_1`, `demos/n1` | 첫 두 파일의 7개 현재 관절각을 모든 행에서 대조하고, 각 상세 파일에서 사용자 요청 벡터의 크기가 10⁻¹²보다 큰 행을 센다. 파일별 해시와 숫자·목록 직렬화 명령만 허용한다. [시행 파일](https://github.com/VT-Collab/repeated-shared-autonomy/tree/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/user/user1) · [별도 정책 혼합 수집기](https://github.com/VT-Collab/repeated-shared-autonomy/blob/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/anca.py#L225-L271) |
| `harmonic` | HARMONIC 공식 1.0.0 텍스트 아카이브 내부 경로 `harmonic_0.5.0/p100/run/005/text_data` | 4.57 GB 파일의 앞 160 MiB에 범위 요청을 보내고 지정한 여섯 파일을 찾는 즉시 중단한다. 조건 코드 1, 요청·적용 속도 시각 3,124개의 일대일 대응을 확인했다. 센서·조이스틱은 각각의 시각을 갖는다. [배포 안내](https://harplab.github.io/harmonic/) · [해당 텍스트 아카이브](https://drive.google.com/file/d/1G4_fGdH0fB_8JCHj4vCEfcaej-oXs7M4/view) |
| `copilot` | `0128_gearmesh_res_nn_same_trial`의 첫 Parquet 조각 안 시행 0 | 89,400,743바이트 조각의 실제 열 이름을 확인하고 영상 디코딩 없이 낮은 차원의 필드만 읽는다. 0~835프레임과 시각 0~55.6667초가 15 Hz 간격에 맞는다. 배포 메타데이터의 43시행·14,062프레임과 여기서 읽은 1시행을 구별한다. [학습본 메타데이터](https://huggingface.co/datasets/shashuo0104/0128_gearmesh_res_nn_same_trial/blob/4a8310fdbd932bf721c458c2408d064bef9a7843/meta/info.json) |
| `geometry` | RealKuka의 `human_demo_paper_toolz_arc3mm_cropped_v001.npz` | 가공 전후 좌표 표현, 측정 공구 축, 표면에서 계산한 목표 축과 단조 시각의 배열 크기를 확인한다. 공개 NPZ가 인용한 원시 CSV는 조사한 버전의 저장소에 없었다. [배포 범위](https://github.com/epfl-lasa/Learn_Equality_Constraints_from_Demonstrations/blob/3e12fc5d2475b67bf8fc32c790085a2e7bcd1708/DATASETS.md) |

과거 시행에 배포된 바이너리와 현재 공개 수집 코드의 정확한 버전 대응은 미확인이다. DROID에서는 명령의 수치 일치로, Panda 상세 파일에서는 같은 시행의 관절각 일치로 해석을 검산했다. 특히 Panda의 공개 `play.py`는 두 버퍼를 채우지만 종료 시 파일 저장 줄이 주석 처리되어 있다. Residual Copilot의 학습본 시각과 수집기의 캡처 시각 역시 서로 바꿔 쓸 수 없다. 시뮬레이션·새 시연·정책 학습은 이번 검사의 범위 밖이다. [Panda 버퍼·파일 경로](https://github.com/VT-Collab/repeated-shared-autonomy/blob/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/play.py#L213-L255) · [기어 조립 수집기](https://github.com/shuosha/Residual_Copilot_Deployment/blob/b2e5a6a7821a9b7dc175c210c265a8adf7c42823/src/robot_control/utils/data_storage.py#L32-L57)
