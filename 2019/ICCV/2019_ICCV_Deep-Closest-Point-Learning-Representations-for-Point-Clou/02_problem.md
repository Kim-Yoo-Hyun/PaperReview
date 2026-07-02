# Problem

- Year/Venue: 2019 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D Vision, registration, point cloud, alignment
- Paper link: ./2019/ICCV/2019_ICCV_Deep-Closest-Point-Learning-Representations-for-Point-Clou/paper.pdf
- Code/Project: https://github.com/WangYueFt/dcp
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Point cloud registration is a key problem for computer vision applied to robotics, medical imaging, and other applications.
- This problem involves finding a rigid transformation from one point cloud into another so that they align.
- Many modeling and computational challenges hamper the design of a stable and efficient registration method.

## 해결하려는 문제
- Our model consists of three parts: a point cloud embedding network, an attention-based module combined with a pointer generation layer, to approximate combinatorial matching, and a differentiable singular ...
- However, only our method achieve satisfying alignment for objects with sharp features and large transformation.
- To address local optima and other difficulties in the ICP pipeline, we propose a learning-based method, titled Deep Closest Point (DCP), inspired by recent techniques in computer vision ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
