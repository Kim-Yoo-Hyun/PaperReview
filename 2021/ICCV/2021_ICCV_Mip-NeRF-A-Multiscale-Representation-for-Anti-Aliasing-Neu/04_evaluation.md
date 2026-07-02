# Evaluation

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, geometry
- Paper link: ./2021/ICCV/2021_ICCV_Mip-NeRF-A-Multiscale-Representation-for-Anti-Aliasing-Neu/paper.pdf
- Code/Project: https://jonbarron.info/mipnerf/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- Although NeRF and its variants have demonstrated impressive results across a range of view synthesis tasks, NeRF’s rendering model is flawed in a manner that can cause excessive ...
- By efficiently rendering anti-aliased conical frustums instead of rays, mip-NeRF reduces objectionable aliasing artifacts and significantly improves NeRF’s ability to represent fine details, while also being 7% faster ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
