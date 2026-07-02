# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- 출발 문제 단서: Traditional methods for solving these problems employ handcrafted features to capture geometric properties of point clouds [Lu et al.
- 주장된 효과 단서: Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Object, relation, room/scene hierarchy를 graph로 구조화해 3D perception 결과를 robot planning과 language reasoning에 넘기는 중간 표현으로 사용할 수 있다.
- 관계 중심 표현은 단일 object detection보다 task-relevant affordance, spatial relation, commonsense reasoning을 붙이기 쉽다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
- 저자가 남긴 확장 방향: While our architectures easily can be incorporated as-is into existing pipelines for point cloud-based graphics, learning, and vision, our experiments also indicate several avenues for future research and ...
- static scene graph 품질을 보인 뒤에도 dynamic updates, uncertainty, open-vocabulary relation grounding, robot action coupling은 별도 문제로 남는다.

## 다음 연구 질문
- 3D scene graph의 node/edge uncertainty를 planning cost나 action selection에 어떻게 반영할 수 있는가?
- language query에 필요한 relation만 선택적으로 구성하면 dense graph보다 효율과 성능이 개선되는가?
- dynamic manipulation/navigation 중 graph를 어떻게 갱신해야 consistency가 유지되는가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: S3DIS, ModelNet40, ShapeNet, ShapeNetPart / accuracy, mIoU, IoU, mAP
- 내 연구 확장 benchmark 후보: ScanNet, 3RScan, Matterport3D
- 내 연구 확장 metric 후보: mIoU, Recall@K, relation accuracy, task success
- 검증 초점: relation prediction, open-vocabulary grounding, downstream planning utility를 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: Traditional methods for solving these problems employ handcrafted features to capture geometric properties of point clouds [Lu et al.
- Method cue: To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- Result cue: Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
