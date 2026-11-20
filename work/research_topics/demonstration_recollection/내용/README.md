# 시연의 선택적 재수집

**2026-11-20 판정 · 공개 표본을 이용한 방법 개발은 보류한다.** 같은 작업에서 여러 조작 요청이 같은 실행으로 바뀌더라도, 시연자가 처음 요청한 명령이 남아 있으면 다시 시연을 받을 이유가 약하다. 네 원격조작 자료를 확인했다. 세 자료에는 요청을 복원하거나 직접 읽을 수 있는 시행이 있었다. 나머지 기어 조립 자료는 학습본에서 원래 입력이 빠졌지만 수집 코드에는 기록 경로가 있었다. 원래 요청을 되살릴 수 없고 가이드 방향만 바꿔 다시 시연할 수 있는 작업을 함께 확인한 사례는 없었다. [표본과 재현 방법](../재현%20방법/README.md)

## 실제로 무엇이 남았는가

등록된 비교 문헌에서 HARMONIC의 사용자 요청·보조 속도 필드와 Residual Copilot의 시연 수집 조건·하류 정책 평가를 확인할 수 있다. [HARMONIC](../../../../2022/IJRR/2022_IJRR_HARMONIC-A-multimodal-dataset-of-assistive-humanrobot-coll/01_overview.md) · [Residual Copilot](../../../../2026/CoRL/2026_CoRL_Efficient-and-Reliable-Teleoperation-through-Real-to-Sim-t/01_overview.md)

여기서 ‘요청’은 같은 상태에서 보조기가 개입하기 직전의 제어 입력이다. 사람이 궁극적으로 달성하려 한 작업은 별도 정보다. ‘적용 명령’은 제어기가 로봇에 지시한 값이며 실제 움직임은 센서가 측정한다. 각 자료에서 확인한 경로는 다음과 같다.

| 자료·작업 | 시연자의 요청과 제약 | 적용 명령·측정·시각 | 후보 판단 |
|---|---|---|---|
| DROID · Panda, 컵으로 알갱이 붓기 등 | VR 이동을 로봇 좌표계의 목표 자세로 변환한 뒤 병진 속도 크기를 제한한다. 제한 전 `target_cartesian_position`이 남는다. | `action/cartesian_velocity`는 정규화 명령이다. 관절 명령과 엔코더 값은 별도 필드다. 상태 읽기와 `control_start`도 구분된다. | 병진 요청의 방향과 크기 모두 복원 가능. 이 표본의 속도 포화는 방향을 바꾸는 가상 가이드와도 다르다. [제어식](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/droid/controllers/oculus_controller.py#L111-L175) · [기록 순서](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/droid/trajectory_utils/misc.py#L68-L115) |
| HARMONIC · Mico로 음식 집기 | 목표 음식 위치, 조이스틱 축, 제어 모드별 사용자 속도 `twist`를 저장한다. 로봇은 추정한 목표에 따른 보조 속도를 사용자 입력과 가중합한다. | 적용 속도 `exec_twist`, 관절 상태, 순기구학으로 계산한 링크 위치에 각각 시각이 있다. | 실제 보조 시행에서도 원래 요청을 읽을 수 있다. 연구자가 바꾼 변수는 보조 강도다. [논문 §3.3·§5](https://journals.sagepub.com/doi/10.1177/02783649211050677) · [로봇 제어 코드](https://github.com/HARPLab/ada_meal_scenario/blob/36fce84658987874eccaa5b06f9c422de683a58a/src/ada_meal_scenario/actions/assistance_policy_action.py#L22-L38) |
| 반복 상호작용의 공유 제어 · Panda로 탁상 목표에 접근 | 조이스틱 병진 요청과 보조 속도를 결합하고 작업공간 하단에서 아래 방향 속도를 제한한다. 사용자 요청을 관절 속도로 옮긴 `qdot_h`와 보조 성분 `qdot_r`를 별도로 기록한다. | 경과 시각, 측정 관절각, 두 속도 성분, 혼합 계수가 한 행이다. 전송하는 최종 관절 명령은 별도 단계에 있다. | 시연 파일에 관절각만 있어도 같은 시행의 상세 파일로 요청을 되찾는다. 방향 가이드를 외부에서 선택한 시행은 확인되지 않았다. [IROS 2021 자료](https://github.com/VT-Collab/repeated-shared-autonomy/tree/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study) · [혼합·기록·전송](https://github.com/VT-Collab/repeated-shared-autonomy/blob/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/play.py#L265-L303) |
| Residual Copilot · xArm7 기어 맞물림 | 온라인 경로에서 GELLO의 목표 위치·자세·그리퍼 입력에 보정을 적용한다. 수집기는 원래 목표 `base_action.*`와 보정 후 목표 `action.*`를 모두 쓴다. 오프라인 경로의 기본 입력은 kNN에서 온다. | 수집 시 관측과 명령은 같은 캡처 시각으로 이름을 붙인다. 배포한 학습본은 8차원 행동과 8차원 상태, 프레임 상대 시각을 담는다. | 학습본에 기본 입력 열이 없는 것은 확인했다. 해당 시행의 원본 JSON 공개 여부, 지정한 가이드 방향으로 다시 받을 수 있는지는 미확인이다. [온라인 입력](https://github.com/shuosha/Residual_Copilot_Deployment/blob/b2e5a6a7821a9b7dc175c210c265a8adf7c42823/src/robot_control/env/shared_autonomy_env.py#L246-L269) · [수집기](https://github.com/shuosha/Residual_Copilot_Deployment/blob/b2e5a6a7821a9b7dc175c210c265a8adf7c42823/src/robot_control/utils/data_storage.py#L32-L57) · [공개 학습본](https://huggingface.co/datasets/shashuo0104/0128_gearmesh_res_nn_same_trial/tree/4a8310fdbd932bf721c458c2408d064bef9a7843) |

**DROID 원시 시행 3개.** 전체 781프레임 중 로봇 이동이 허용된 640프레임을 검산했다. 컵 붓기는 372프레임 중 37개가 포화됐고, 물체 재배치가 제안된 시행은 125개 중 0개, 뚜껑 조작 실패 시행은 143개 중 0개였다. 목표와 현재 손목 위치 차이에 이득 5를 곱하고 크기를 1로 제한하면 640개 모두 기록된 병진 명령과 성분별 최대 절대 오차가 2.8×10⁻¹⁶ 이하였다. 같은 방향의 큰 요청들이 같은 속도로 줄어드는 제어식과, 같은 물리 상태에서 다른 사람이 실제로 같은 실행을 냈다는 관측은 구분해야 한다. 검산 범위는 병진 세 축이다. [DROID 원장 pr-0732](../../../../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) · [원시 데이터 명세](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/docs/the-droid-dataset.md)

**HARMONIC.** 보조 조건 `p100/run/005`에는 조이스틱 3,417행, 관절 상태 7,181행이 있었다. 요청과 적용 속도는 고유한 시각 3,124개에서 일대일로 대응했다. 저장된 두 6차원 벡터는 전 행에서 한 성분 이상이 10⁻⁸보다 크게 달랐고 사용자가 0이 아닌 입력을 보낸 행은 같은 허용 오차에서 1,479개였다. 조이스틱에는 재표집 과정에서 직전 값을 유지한 행이 포함된다. 이 결과는 보조 전후의 값을 별도로 읽을 수 있다는 증거다. [HARMONIC 배포](https://harplab.github.io/harmonic/) · [필드 정의, 원고 6쪽](https://harplab.github.io/assets/pubs/newman2021_ijrr_harmonic.pdf#page=6)

**Panda 공유 제어.** `final_n_1`은 시연과 상세 파일에서 측정 관절각이 98/98행 동일했고 사용자 요청이 82행에서 0이 아니었다. 같은 저장소에서 정책을 혼합한 또 다른 시행에도 사용자 요청이 174행 중 93행에 있었다. 직접 조작 `demos/n1.pkl`은 시작·현재 관절각만 57행이고 `runs/`에 같은 이름의 파일이 없다. 직접 조작 코드에는 이 작업의 가이드 방향을 바꾸는 처치가 없다. [Panda 공개 시행](https://github.com/VT-Collab/repeated-shared-autonomy/tree/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/user/user1) · [직접 시연 수집기](https://github.com/VT-Collab/repeated-shared-autonomy/blob/0bca58cbdcaf07f13b92a2d02deab8ea59b4c376/IROS2021/robot-experiments/user_study/record_demos.py#L198-L234)

**기어 조립은 가장 가까운 비교다.** 동일 시도 수 배치의 공개 학습본에서 시행 0의 연속 836프레임을 직접 확인했다. 원저자들은 직접 조작과 보조 조작을 번갈아 수집했다. 시도 수를 맞춘 하류 정책의 기어 삽입은 보조 시연으로 학습하면 11/20, 직접 시연이면 1/20이었다. 이는 보조 방식이 시연 품질에 영향을 준다는 선행 근거다. 공백으로 남는 것은 원래 명령을 잃은 자료에서 *어느 상태와 가이드 방향을 다시 선택할지*의 가치다. 저자도 보조가 들어오면 사람이 전략을 바꿀 수 있음을 한계로 적었다. 같은 시도 수에서 걸린 시간과 같은 상태에서의 반사실적 요청은 별도 검증 대상이다. [원문 §IV-C 표 II·§V](https://arxiv.org/html/2603.17016#S4.SS3)

## 기하학적 가이드까지 확인한 범위

- **실제 표면을 따라간 KUKA iiwa.** RealKuka의 가공 표본에는 원경로 표현 13,682점과 학습용 1,283점, 관절 위치·속도·외력 토크·시각이 있다. `target_tool_z`는 보정한 표면 법선에서 계산한 목표 축이다. 이 파일에서 조작자 요청은 확인되지 않지만, 같은 물리 표면과 작업을 유지한 채 독립적으로 소프트웨어 가이드 방향을 바꾸는 절차도 제시되지 않았다. [작업·가공 정의](https://github.com/epfl-lasa/Learn_Equality_Constraints_from_Demonstrations/blob/3e12fc5d2475b67bf8fc32c790085a2e7bcd1708/datasets/real_iiwa/tasks/RealKuka/task.json)
- **메시 기반 가상 가이드.** dVRK용 공개 코드는 메시로 가상 제약을 정의하며 직접 원격조작과 제약을 켠 원격조작을 각각 기록하는 경로를 제공한다. 확인한 저장소에는 실제 시행의 ROS bag이 없었고, README에서도 조사할 수 있는 원시 시행 링크를 확보하지 못했다. 따라서 이 시스템은 가이드 방향을 바꿀 잠재적 적용처로 남는다. 같은 작업·상태에서의 방향 변경, 요청 채널 누락, 직접 조작 비용은 미확인이다. [저자 저장소](https://github.com/mli0603/PolygonMeshVirtualFixture/tree/07a70b2f7b407213dbdcd8a3bf1c92e03a546c31) · [제약 전환과 기록](https://github.com/mli0603/PolygonMeshVirtualFixture/blob/07a70b2f7b407213dbdcd8a3bf1c92e03a546c31/scripts/study_control.py#L122-L132)

## 연구 가치와 재개 조건

Howard 등은 여러 제약에서 관측된 동작으로 원래 정책을 추정했다. ACIL은 행동 공간 제약에 맞게 전문가 시연을 정렬하고, Mulligan과 ThriftyDAgger는 시연을 요청할 상태를 선택한다. 이 후보의 독립 기여는 **작업 좌표를 유지하면서 다시 시연할 상태와 가이드 방향을 함께 선택하면, 처음 보는 가이드에서 행동 오류가 줄어드는지**에 있다. 원장 내 시연 분석·교정·폐루프 수집 비교점은 `pr-0747`, `pr-0931`, `pr-1236`이다. [Howard 등](https://homepages.inf.ed.ac.uk/svijayak/publications/howard-ICRA2009.pdf) · [ACIL](https://proceedings.mlr.press/v267/yeh25a.html) · [Mulligan](https://arxiv.org/html/2610.05882#S3) · [ThriftyDAgger](https://proceedings.mlr.press/v164/hoque22a.html)

**다시 투자할 근거**는 재사용 가치가 있는 기존 기록 한 묶음이다. 먼저 수집기와 원본·동일 시행의 보조 파일까지 대조해 요청이 복원되지 않는 사례를 찾는다. 이어 작업물·목표를 고정한 상태에서 가이드 방향을 바꿀 수 있고, 서로 다른 요청이 같은 실행을 만든다는 독립 기록을 확보한다. 직접 시연이나 원래 요청의 동시 기록으로 해결하는 비용도 시연자 시간·초기화·실패 횟수로 측정한다. 이번 공개 표본은 목적 표집이어서 현장에서의 발생률을 추정할 수 없다.

그 근거가 생기면 시뮬레이션에서 무작위 재수집, 많이 잘린 상태만 선택, 가이드 방향 다양성만 최대화, 상태·방향 공동 선택, 자유 시연을 같은 작업자 시간으로 비교한다. 남겨 둔 가이드에서의 작업 성공과 진행 방향 오류를 측정하고, 보조에 따라 같은 시연자의 요청이 달라지는지도 짝지은 소표본에서 확인한다. 현재는 원시 자료 감사까지 완료했다. 재수집의 정책 성능과 비용 효과는 미측정이다.
