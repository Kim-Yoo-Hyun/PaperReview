# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_SDGS-Spatial-Difference-Guided-Gaussian-Splatting-for-Simu/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× faster per-iteration pose ...
- Our SD Gaussian descriptor with DT enhances overall convergence basin and our approach is the only method that provide sparse reconstruction using SD.
- Leveraging a state-of-theart dual-channel vision sensor that generates blur-less and high-frame-rate spatial difference outputs, our method produces accurate and detailed geometric reconstructions in challenging conditions.

## 원리적 동기
- Crucially, it maintains robust tracking and reconstruction under extreme high-speed motion where existing RGB-based approaches fail.
- We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× faster per-iteration pose ...
- We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× faster per-iteration pose ...

## 핵심 방법론
- Our SD Gaussian descriptor with DT enhances overall convergence basin and our approach is the only method that provide sparse reconstruction using SD.
- 9, our method successfully restores fine structural details and sharp textures that are lost in the blurred input images.
- This result confirms that our approach can be stably generalized to standard RGB systems and enables more efficient simultaneous tracking and reconstruction.
- By applying first-order difference operators to the RGB streams, we use extracted sparse geometric features with only minimal additional computational overhead, reducing the dense photometric burden in tracking ...
- Method Gaussian-SLAM SplaTAM MonoGS–RGBD Ours fr1/desk fr2/xyz fr3/office Average 3.00 3.32 1.45 1.64 1.34 1.33 1.23 0.54 5.63 5.25 1.75 4.15 3.32 3.30 1.48 2.11 Figure 7.
