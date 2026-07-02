# Method

- Year/Venue: 2025 / 3DV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_SSRFlow-Semantic-aware-Fusion-with-Spatial-Temporal-Re-emb/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this issue, we propose a novel approach called Dual Cross Attentive (DCA) for the latent fusion and alignment between two frames based on semantic contexts.
- Conclusion 0.0171 0.0169 0.0136 0.0122 0.0109 0.0101 0.0082 0.0059 We propose the SSRFlow network to accurately and robustly estimate scene flow.
- Secondly, we test the internal and external position encoder of cross-attention in DCA Fusion.

## 원리적 동기
- However, contemporary scene flow methods face three major challenges.
- To address this issue, we propose a novel approach called Dual Cross Attentive (DCA) for the latent fusion and alignment between two frames based on semantic contexts.

## 핵심 방법론
- Conclusion 0.0171 0.0169 0.0136 0.0122 0.0109 0.0101 0.0082 0.0059 We propose the SSRFlow network to accurately and robustly estimate scene flow.
- Secondly, we test the internal and external position encoder of cross-attention in DCA Fusion.
- More visualization results are exhibited in Supplementary Material, Sec 11 GF In (a) of Table 7, we provide a detailed list of the importance of the DCA Fusion, ...
- Additionally, we replace the Method Runtime Method Runtime Method EPE3D↓ FlowStep3D PT-Flow DifFlow 292.1ms 376.2ms 231.7ms PV-RAFT MSBRN SSRFlow (Ours) 780.2ms 225.9ms 101.1ms Ours (full equip) 0.0122 (a) ...
- Moreover, the position encoder outside the DCA Fusion provides additional spatial features that are superior to internal equipment.
