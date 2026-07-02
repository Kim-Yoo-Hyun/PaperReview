# Method

- Year/Venue: 2026 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: Gaussian Splatting, semantic mapping, open-vocabulary
- Paper link: ./2026/CVPR/2026_CVPR_OnlinePG-Online-Open-Vocabulary-Panoptic-Mapping-with-3D-G/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online setting.
- While a performance gap remains compared to offline methods that use ground truth point clouds and capture global multi-view information, our method substantially narrows this gap.
- For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ms for clustering ...

## 원리적 동기
- However, existing methods are predominantly offline or lack instance-level understanding, limiting their applicability to real-world robotic tasks.
- Despite previous approaches that combine VLMs with 3DGS having yielded satisfactory performance, two critical limitations remain: 1) offline reconstruction and perception settings.
- In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online setting.

## 핵심 방법론
- While a performance gap remains compared to offline methods that use ground truth point clouds and capture global multi-view information, our method substantially narrows this gap.
- For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ms for clustering ...
- Benefiting from our local-to-global 3D instance modeling approach and fine-grained language feature fusion based on the spatial feature grid, our method can obtain more complete 3D instance information ...
- Compared with the offline SOTA PanoGS , our approach still exists a small performance gap. mentation approach (trained on ScanNetV2 ) to obtain 3D instances for them.
- We use different colors to distinguish different instances found in the query.
