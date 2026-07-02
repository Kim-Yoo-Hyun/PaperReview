# Insights

## 이 논문에서 가져갈 핵심 개념
- 핵심 방법 단서: We use the official training split for the training and select 4 scenes for the evaluation.
- 출발 문제 단서: Unlike existing openvocabulary 3DGS methods, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an online manner.
- 주장된 효과 단서: To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...

## 내 연구 방향에서 어떻게 활용할 수 있나
- 위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.
- Differentiable 3D scene representation을 semantic map, view synthesis, robot memory, planning cost field로 재사용할 수 있다.
- Geometry와 appearance를 함께 담는 표현은 language feature, object identity, dynamic state를 붙이는 기반이 된다.

## 이 논문이 끝난 지점
- 논문이 도달한 지점: To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...
- reconstruction/view synthesis 품질을 보인 뒤에도 real-time update, semantic consistency, dynamic interaction, robot-safe planning은 후속 과제로 남는다.

## 다음 연구 질문
- Gaussian/NeRF field에 language feature를 붙일 때 3D consistency와 open-vocabulary retrieval을 동시에 유지할 수 있는가?
- robot이 움직이며 갱신하는 online field에서 drift와 hallucinated semantics를 어떻게 줄일 수 있는가?
- rendering quality가 실제 navigation/manipulation success로 이어지는 조건은 무엇인가?

## 실험으로 확인할 방향
- 논문 내 evaluation 단서: ScanNet, ScanNet200, Replica / mIoU, mAP
- 내 연구 확장 benchmark 후보: Replica, ScanNet, Mip-NeRF 360, Tanks and Temples
- 내 연구 확장 metric 후보: PSNR, SSIM, LPIPS, mIoU
- 검증 초점: view synthesis 품질뿐 아니라 semantic querying, map update, robot task success를 같이 확인한다.

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
- Problem cue: Unlike existing openvocabulary 3DGS methods, our objectives are two-fold: 1) Reconstructs the semantic-embedded 3DGS of the entire scene from over 300 streaming images in an online manner.
- Method cue: We use the official training split for the training and select 4 scenes for the evaluation.
- Result cue: To achieve these objectives, we propose an Online Sparse Coefficients Field with a CLIP Global Codebook where it binds the 2D CLIP embeddings to each 3D Gaussian while ...
