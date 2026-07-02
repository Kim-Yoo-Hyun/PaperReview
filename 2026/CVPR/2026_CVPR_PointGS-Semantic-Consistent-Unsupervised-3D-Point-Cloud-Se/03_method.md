# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, semantic, alignment, point cloud, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_PointGS-Semantic-Consistent-Unsupervised-3D-Point-Cloud-Se/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The Gaussian space is aligned with the original point cloud via two-step registration, and point semantics are assigned through nearest-neighbor search on labeled Gaussians.
- PointGS leverages 3D Gaussian Splatting as a unified intermediate representation to bridge the discretecontinuous domain gap.
- Multi-view dense images are rendered from the Gaussian space, with 2D semantic masks extracted via SAM, and semantics are distilled to 3D Gaussian primitives through contrastive learning to ...

## 원리적 동기
- To address these limitations, this paper proposes PointGS, a simple yet effective pipeline for unsupervised 3D point cloud segmentation.
- Unsupervised point cloud segmentation is critical for embodied artificial intelligence and autonomous driving, as it mitigates the prohibitive cost of dense point-level annotations required by fully supervised methods.
- The Gaussian space is aligned with the original point cloud via two-step registration, and point semantics are assigned through nearest-neighbor search on labeled Gaussians.

## 핵심 방법론
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
