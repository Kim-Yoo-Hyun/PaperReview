# 조작 허용 오차를 반영하는 3D 추정과 VLA 학습

2026-11-18: 직접 선행의 정식 paper-note와 publication 경계는 [REG-R17 등록](../../../update/REGISTRY_MAINTENANCE_2026-11-18.md)으로 연결했다. 아래 연구 판단·실행 준비 상태는 유지한다.

Updated: 2026-11-17 KST. **TASK-GEOMETRY / 초기 탐색 후보 2순위 / CURATION-HYPOTHESIS.** 사용자 지정 `3D reconstruction + VLA + estimation + Robotics`에 대응한다. 문헌 확인·기여 경계·작은 검증 초안을 정리했으며 방법 신규성·실험 효과는 미확립이다. [재현 준비](../재현%20방법/README.md) · [공통 원장: pose_reconstruction_scout](../../../sources/new_field_scout_2026-11-17.json) · [전체 후보](../../README.md).

## 연구 질문

**전체 3D 재구성 오차가 비슷해도 접촉 면·끼움 방향·여유 공간의 오차가 다르면 VLA의 성공은 달라지는가? 그 차이를 예측하는 표현으로 3D 추정과 정책 학습을 개선할 수 있는가?** 목표는 더 보기 좋은 reconstruction이 아니라, 작업에 허용되는 오차와 실제 추정 오차의 관계를 로봇 행동으로 검증하는 것이다.

초기 범위는 한 팔의 강체 집기→방향 정렬/삽입이다. 물체 local shape, object pose, camera extrinsic, metric scale을 구분한다. 전체 mapping·physics reconstruction·SLAM·world model을 동시에 새로 만들지 않는다. 같은 geometry에서도 넓은 tray 배치와 좁은 fixture 배치는 필요한 정확도가 다르다.

## 선행이 지지하는 사실과 신규성 경계

| 선행 | 이미 해결한 부분 | 남는 질문을 좁히는 조건 |
|---|---|---|
| [Robo3R, RSS 2026](https://roboticsproceedings.org/rss22/p056.html), [방법](https://arxiv.org/html/2602.10101v1) | RGB+robot state에서 robot frame의 metric geometry 추정. Local geometry·camera pose·global alignment와 PnP 보정. 실제 manipulation downstream 평가 포함 | **재구성을 로봇 좌표로 옮겨 조작에 쓰는 것** 자체는 기여 아님 |
| [GeoPredict, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html), [공식 코드 설명](https://github.com/jingjingqian75/GeoPredict) | 미래 robot keypoint trajectory와 3D Gaussian geometry 예측, 궤적 주변 refinement와 depth 보조 학습 | **작업/궤적 주변을 더 정밀하게 재구성**하는 것도 이미 있음. Training-only geometry 보조와 실행 중 geometry 입력을 구별 |
| [SpatialVLA, RSS 2025](https://roboticsproceedings.org/rss21/p011.html), [Pose-VLA, RSS 2026](https://roboticsproceedings.org/rss22/p145.html) | 각각 공간 표현을 VLA에 통합, pose/trajectory pretraining 후 embodiment 정렬 | 3D feature/pose token을 VLA에 추가했다는 사실로 독립 기여 주장 불가 |
| [UA-Pose, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html), [CNABU, RSS 2025](https://roboticsproceedings.org/rss21/p039.html) | 각각 부분 reference의 관측/미관측 geometry와 pose 불확실성, 조작/시점 이동 뒤 calibrated map belief 예측 | 관측된 표면과 생성된 표면의 confidence 구분도 새 발상이 아님 |
| [Naik 등, Industrial Robot 2025](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF) | pose 추정 오차와 task 허용 오차 분포로 성공 가능성 평가 | tolerance-aware uncertainty 일반론은 이미 존재 |
| [PRISM, arXiv 2026 §2–3](https://arxiv.org/html/2610.14704v1) | 물리 허용 오차와 flow error의 관계를 분석하고, 시연 운동/그리퍼에서 얻은 정밀도 요구 proxy로 VLA 학습을 재가중 | **정밀 구간 loss를 강화한다**는 제안은 직접 중복. 본 후보는 입력 geometry 오차의 위치·방향·원인을 분리해야 함 |

Registry의 DUSt3R·MASt3R·VGGT는 geometry backbone 계보이며 이번에 모두 다시 정독한 것은 아니다. [ReconVLA, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/38921)의 reconstruction은 목표 영역의 영상 재구성으로, metric 3D 재구성과 혼동하지 않는다. [ATAP](https://arxiv.org/html/2609.23504v1)는 생성 shape의 task affordance를 추가 관측으로 검증하므로 ‘생성된 geometry를 확인한다’만으로 별도 후보를 만들지 않았다.

## 연구자 해석 — 기여 후보

제안은 **작업의 방향별 허용 오차로 정규화한 geometry error/uncertainty 표현**과 그에 따른 학습이다. 예를 들어 슬롯 축 방향, 횡방향, 접촉 면 법선 방향의 오차는 같은 크기여도 결과가 다르다. 영상에 가까운 부분만 더 잘 복원하는 ROI weight와 달리, 어떤 geometry 성분을 잘못 추정했는지가 성공을 설명해야 한다.

초기에는 frozen geometry model과 VLA를 고정하고 **동일한 오차량의 원인별 개입**으로 실패 원인을 확인한다. 이 진단이 단순 object crop·depth RMSE·pose error보다 새로운 예측을 주면, task-conditioned geometric confidence/auxiliary loss를 작은 adapter에 학습시키는 방법으로 확장한다. Task tolerance의 수치·성공 판정은 simulator/CAD 평가자가 정의하고, test-time 정책에는 정답 geometry나 허용 오차 정답을 자동 제공하지 않는다. 미관측 object/fixture에서 추정해야 한다면 별도 generalization 문제다.

오차 전파 Jacobian, Mahalanobis distance, tolerance 정규화 자체는 기존 수학이다. **새로 주장할 수 있는 것은** 측정 가능한 geometry 오류가 행동 실패로 이어지는 조건과, 그 조건을 학습해 기존 모델보다 개선한다는 검증 결과다. ‘접촉 부근이 중요하다’는 자명한 관찰이나 PRISM 방식의 일반 reweighting만 남으면 독립 방법 주제로 확대하지 않는다.

## 최소 검증 초안

| 비교 | 조절하는 변수 | 반드시 확인할 해석 경계 |
|---|---|---|
| 같은 3D 오차 크기, 다른 공간 위치 | target/contact 면 vs 배경 | foreground ROI 가중만으로 설명되는지 먼저 비교 |
| 같은 물체/오차 크기, 다른 방향 | 슬롯 횡방향·축방향·표면 법선 | 방향별 tolerance 모델이 isotropic pose/point error보다 잘 예측하는지 |
| 같은 장면·비슷한 평균 오차, 다른 원인 | global scale/extrinsic vs local shape vs object pose | 변환 오류와 shape 오류를 혼합하지 않음; 단위·좌표계 정합 |
| 같은 geometry, 다른 지시/fixture | 넓게 놓기 vs 방향 정렬/좁은 끼움 | 실제 tolerance와 언어 조건의 효과, trajectory/context proxy를 분리 |
| held-out object/clearance/reconstructor | mesh·허용 오차·geometry backbone | 특정 model artifact와 같은 mesh의 view를 일반화로 포장하지 않음 |

위 사례는 구현·확보된 benchmark가 아니다. RGB와 point map의 인위적 불일치 실험은 진단으로 표시하고, 후속에는 재렌더링된 일관된 관측 또는 실제 reconstruction 오류에서 반복해야 한다. Simulator collision mesh 자체를 바꿨다면 perception-only 개입이 아니므로 분리한다.

비교군은 RGB VLA, 같은 VLA의 일반 3D 입력/보조 학습, isotropic geometry loss, object/trajectory ROI loss, 단순 tolerance rule, 가능한 경우 GeoPredict 방식의 보조 학습과 PRISM 방식의 precision weighting이다. 각 원 논문 그대로의 재현과 좁은 이식 baseline을 구별한다. 모델 크기·학습량·관측/주석 정보·추론 비용을 맞추고 pose/shape confidence head의 정보 추가 효과를 ablation한다.

주요 결과는 task 성공·정렬/접촉 실패·성공까지 걸린 시간이다. 보조 결과는 Chamfer/depth/pose error와 실패 예측의 보정·순위이며, 단순 geometry metric 개선만으로 VLA 기여를 주장하지 않는다. 최소한 여러 오차 조건에서 새 지표가 단순 지표보다 downstream 성능 순서를 설명하거나, 통제된 학습이 held-out 조건에서 행동을 개선해야 결과 주장이 생긴다. 아직 그 증거는 없다.

## 가치·부담·다음 단계

**새 후보 중 2순위**다. Computer Vision 방법과 실제 로봇 행동의 연결이 분명하고 분석→학습으로 확장할 수 있다. 다만 Robo3R·GeoPredict·PRISM 이후 남는 차이가 좁으며, geometry 입력이 실제로 정책에 반영되는지부터 확인해야 한다. Point-cloud diffusion policy의 이득을 VLA 이득으로 바꿔 부를 수 없다. Camera/robot frame 정합·형상 label·정밀 접촉 기본 능력·실물 calibration이 부담이다. 다만 POSE-ACTIVE-N1에서 SpatialVLA의 depth→3D embedding 경로를 확인했으므로 **1번보다 준비 비용이 높다는 초기 단정은 유보한다.** Frozen depth 개입 진단은 더 짧게 시작할 수도 있다. 2순위는 현재 질문 구체화 순서이며 연구 잠재력·실측 구현 비용의 열세를 뜻하지 않는다.

다음 비실험 작업은 확인된 [SpatialVLA 입력 지점](../재현%20방법/README.md)에서 개입/adapter 범위를 구체화하고, simulator의 depth/pose/mesh/evaluator와 더 강한 단순 대안까지 확인하는 것이다. 이 부분 source 확인을 TASK-GEOMETRY-N1 전체 완료로 세지 않는다. 정책의 공간 입력이 없으면 외부 3D 모델을 바꿔도 이 가설을 검증할 수 없다. 새로운 3D 모델 전체 사전학습이나 4M-frame 데이터 재수집을 시작하지 않는다. 우선순위는 [TODO](../../../../TODO.md)가 관리하며 현재 이 후보는 실행 대기가 아닌 초기 탐색이다.
