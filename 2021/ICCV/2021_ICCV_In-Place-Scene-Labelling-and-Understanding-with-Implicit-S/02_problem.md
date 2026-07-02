# Problem

- Year/Venue: 2021 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: NeRF, semantic, 3D Vision, alignment
- Paper link: ./2021/ICCV/2021_ICCV_In-Place-Scene-Labelling-and-Understanding-with-Implicit-S/paper.pdf
- Code/Project: https://shuaifengzhi.com/Semantic-NeRF/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Though the issue can be mitigated by gathering costly annotated data or semi-supervised learning, it is not always feasible in open-set scenarios with various known and unknown classes.
- The intrinsic multi-view consistency and smoothness of NeRF benefit semantics by enabling sparse labels to efficiently propagate.

## 해결하려는 문제
- Recent implicit neural reconstruction techniques are appealing as they do not require prior training data, but the same fully self-supervised approach is not possible for semantics because labels ...
- Machine learning methods have proven to be valuable in both geometric and semantic prediction tasks, but the performance of these methods suffers when the distribution of the training ...
- We extend neural radiance fields (NeRF) to jointly encode semantics with appearance and geometry, so that complete and accurate 2D semantic labels can be achieved using a small ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
