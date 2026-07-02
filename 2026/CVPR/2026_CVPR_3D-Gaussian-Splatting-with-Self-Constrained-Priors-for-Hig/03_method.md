# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_3D-Gaussian-Splatting-with-Self-Constrained-Priors-for-Hig/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To resolve this issue, we propose a self-constrained prior to constrain the learning of 3D Gaussians, aiming for more accurate depth rendering.
- Error map comparison of rendering on NeRF-Synthetic. our method extracts stable implicit priors from depth maps for more stable geometry inference.
- Compared with implicit methods, our method does not need to learn SDF or priors, which balances both accuracy and efficiency.

## 원리적 동기
- Rendering 3D surfaces has been revolutionized within the modeling of radiance fields through either 3DGS or NeRF.
- Although 3DGS has shown advantages over NeRF in terms of rendering quality or speed, there is still room for improvement in recovering high fidelity surfaces through 3DGS.
- To resolve this issue, we propose a self-constrained prior to constrain the learning of 3D Gaussians, aiming for more accurate depth rendering.

## 핵심 방법론
- Error map comparison of rendering on NeRF-Synthetic. our method extracts stable implicit priors from depth maps for more stable geometry inference.
- Compared with implicit methods, our method does not need to learn SDF or priors, which balances both accuracy and efficiency.
- Meanwhile, different from GS-Pull and GS-UDF that fit 3D Gaussians with gradients to learn implicit fields,
