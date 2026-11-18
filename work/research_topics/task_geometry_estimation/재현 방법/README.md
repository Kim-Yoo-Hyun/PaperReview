# TASK-GEOMETRY — 공개 자원과 실행 전 확인 사항

Updated: 2026-11-17 KST. **SCOUT + PARTIAL_SOURCE_CHECK / NOT_IMPLEMENTED / NOT_EXECUTED.** POSE-ACTIVE-N1의 SpatialVLA 확인만 교차 반영했으며 TASK-GEOMETRY-N1 전체 완료는 아니다. [질문·선행·검증 초안](../내용/README.md) · [공통 원장](../../../sources/new_field_scout_2026-11-17.json).

## 현재 자원 확인 수준

| 후보 | 이번에 확인한 범위 | 다음 확인 |
|---|---|---|
| [Robo3R 공식 project](https://yangsizhe.github.io/robo3r/) | RGB/robot state→metric robot-frame geometry와 downstream 설명 | 페이지에서 실행 code/weight release를 식별하지 못함. 공개되지 않았다고 단정하지 않으며 확보 전 필수 dependency로 고정하지 않음 |
| [SpatialVLA 고정 source 감사](../../pose_active_perception/재현%20방법/README.md#n1-source-audit) | POSE-ACTIVE-N1에서 `get_image_features`의 depth→K 기반 camera XYZ→3D embedding 경로, processor의 intrinsic/normalizer 선택을 확인 | Frozen depth 개입의 실제 지점은 있으나 공개 override API·adapter는 없음. 기존 depth 추론은 `no_grad`여서 geometry 공동 학습에는 별도 변경이 필요. Scale/좌표·task evaluator·native 호환 미검증 |
| [GeoPredict 공식 repo](https://github.com/jingjingqian75/GeoPredict) | README상 inference/checkpoint 안내; training release 확인 필요 | training geometry target·loss·depth render·비교 가능한 학습 코드. Runtime 미확인 |
| [PRISM](https://arxiv.org/html/2610.14704v1) | 정밀도 proxy와 flow supervision의 지정 본문 | code/weight 공개 여부, 동일 VLA에 적용 가능한 baseline 경로 |
| 기존 registry의 DUSt3R·MASt3R·VGGT | 기존 등록·project 링크 보존 | 필요한 모델 하나만 선택해 license·revision·camera/depth/point output 확인. 이번에 payload 받지 않음 |

## 실행 계약을 만들기 전에

1. VLA의 실제 geometry 소비 경로와 언어 조건을 확인한다. DP3 등 language가 없는 정책만 확보했다면 Robotics 진단으로 명시하고 VLA 효과라고 쓰지 않는다.
2. Object/robot/camera frame, m/mm 단위, global scale, shape deformation과 pose perturbation을 분리한다. 관측 noise와 collision geometry 변경을 별도로 명세한다.
3. 동일 checkpoint/관측에서 geometry 개입만 바꾸는 경로, RGB와 geometry가 일치하는 follow-up 경로를 각각 확인한다. 정답 pose·tolerance·mesh는 evaluator/명시한 oracle 외 정책에 노출하지 않는다.
4. Object mesh·fixture clearance·task 성공/접촉 evaluator·훈련/검증 분할·정답 calibration 확보 여부를 기록한다. 비교군의 추가 데이터/시간·세부 학습 예산을 맞춘다.
5. 선택한 code/weight/asset/normalizer revision·hash와 OS/GPU/driver·Docker·CUDA/graphics·RAM/VRAM을 실제 source 요구에 맞춰 고정한다. 지금은 기반 모델과 simulator가 선정되지 않아 정확한 용량·버전·실행 명령을 제시하지 않는다.

이후 최소 P0는 geometry→policy 입출력·좌표 정합·언어 조건·oracle 기본 능력 검증부터다. 아직 recipe/adapter/launcher가 없으며 **현재 clone 후 바로 실행할 수 있는 상태가 아니다.** 구현 단계에서 로컬 Docker 조건이 충족하면 정한 P0까지 실행하고, 미충족이면 portable 준비 자료를 작성한다. 설치·추론·simulation·측정은 Docker 안에서만 수행한다. Host 설치·PDF/weights/assets 다운로드·이번 신규 실험 결과는 없다.
