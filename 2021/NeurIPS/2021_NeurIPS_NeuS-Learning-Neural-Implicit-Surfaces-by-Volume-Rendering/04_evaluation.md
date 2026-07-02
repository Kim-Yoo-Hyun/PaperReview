# Evaluation

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: 3D Scene Representations
- Tags: 3D Vision, NeRF, surface reconstruction, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/paper.pdf
- Code/Project: https://lingjie0206.github.io/papers/NeuS/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- DTU

## Metrics
- accuracy
- mAP
- Chamfer

## Evaluation Protocol and Results
- The results show that our approach outperforms the baseline methods on the DTU dataset in both settings – w/ and w/o mask in terms of the Chamfer distance.
- COLMAP results are achieved by trim=0.
- Baselines. (1) The state-of-the-art surface rendering approach – IDR : IDR can reconstruct surface with high quality but requires foreground masks as supervision; Since IDR has demonstrated superior ...
- Regarding the w/o mask setting, we visually compare our method with NeRF and COLMAP in the setting of w/o mask in Figure 5, which shows our reconstructed surfaces ...
- Experiments on the DTU dataset and the BlendedMVS dataset show that NeuS outperforms the state-of-the-arts in high-quality surface reconstruction, especially for objects and scenes with complex structures and ...
- The results show that our approach outperforms the baseline methods on the DTU dataset in both settings – w/ and w/o mask in terms of the Chamfer distance.

## Baselines
- Baselines. (1) The state-of-the-art surface rendering approach – IDR : IDR can reconstruct surface with high quality but requires foreground masks as supervision; Since IDR has demonstrated superior ...
- Regarding the w/o mask setting, we visually compare our method with NeRF and COLMAP in the setting of w/o mask in Figure 5, which shows our reconstructed surfaces ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
