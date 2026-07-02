# Evaluation

- Year/Venue: 2022 / SIGGRAPH
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, efficiency
- Paper link: ./2022/SIGGRAPH/2022_SIGGRAPH_Instant-Neural-Graphics-Primitives-with-a-Multiresolution/paper.pdf
- Code/Project: https://nvlabs.github.io/instant-ngp/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- IoU
- mAP
- PSNR
- collision

## Evaluation Protocol and Results
- 2021], which achieves state-of-the-art results in both quality and speed by prefixing its small MLP with a lookup from an octree of trainable feature vectors.
- With a similar number of parameters (𝑇 = 224 ), our method achieves the same PSNR after 2.5 minutes of training, peaking at 41.9 dB after 4 min.
- 2021] have shown impressive results when fitting very large images—up to a billion pixels—with high fidelity at even the smallest scales.
- For comparison, on the Tokyo panorama from Figure 1, ACORN achieves a PSNR of 38.59 dB after 36.9 h of training.
- 2021], which achieves state-of-the-art results in both quality and speed by prefixing its small MLP with a lookup from an octree of trainable feature vectors.
- With a similar number of parameters (𝑇 = 224 ), our method achieves the same PSNR after 2.5 minutes of training, peaking at 41.9 dB after 4 min.

## Baselines
- As baseline, we compare with NGLOD [Takikawa et al.
- To highlight the versatility and high quality of the encoding, we compare it with previous encodings in four distinct computer graphics primitives that benefit from encoding spatial coordinates.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
