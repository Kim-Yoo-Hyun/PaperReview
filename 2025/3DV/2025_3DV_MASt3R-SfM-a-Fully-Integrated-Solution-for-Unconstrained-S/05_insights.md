# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: We note that 14 scenes of T&T are part of MegaDepth , which is used for training the MASt3R checkpoint we used.
- 출발 문제 단서: The presence of outliers, e.g. wrong pixel matches, poses additional challenges and compels existing methods to resort to hypothesis formulation and verification at multiple occasions in the pipeline, ...
- 주장된 효과 단서: We show here a reconstruction from 6 views sharing the same optical center. tive function with many local minima .

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- SE(3)/rotation/translation structure를 representation이나 policy에 넣어 viewpoint, pose, sensor-frame 변화에 강한 3D reasoning을 만들 수 있다.
- Registration/calibration 관점은 multi-view, LiDAR-camera, robot-camera alignment 문제의 공통 기반으로 사용할 수 있다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: We show here a reconstruction from 6 views sharing the same optical center. tive function with many local minima .
- symmetry-aware representation이 특정 task에서 성능을 보인 뒤에도 large-scale scene, language grounding, real robot noise에서의 이득은 별도 검증이 필요하다.

## 다음 연구 질문
- SE(3)-equivariant feature가 open-vocabulary 3D grounding이나 manipulation policy에서도 실제 sample efficiency를 높이는가?
- learned alignment와 classical calibration/registration을 결합하면 sensor drift와 domain shift를 줄일 수 있는가?
- equivariance constraint가 language-conditioned tasks에서 오히려 semantic flexibility를 제한하지 않는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: ETH3D / accuracy, mAP, ATE
- 내 연구 확장 benchmark 후보: ModelNet40, ScanNet, KITTI, nuScenes
- 내 연구 확장 metric 후보: rotation error, translation error, mIoU, success rate
- 검증 초점: pose robustness, calibration/registration accuracy, downstream perception/action 성능을 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: The presence of outliers, e.g. wrong pixel matches, poses additional challenges and compels existing methods to resort to hypothesis formulation and verification at multiple occasions in the pipeline, ...
- Method cue: We note that 14 scenes of T&T are part of MegaDepth , which is used for training the MASt3R checkpoint we used.
- Result cue: We show here a reconstruction from 6 views sharing the same optical center. tive function with many local minima .
