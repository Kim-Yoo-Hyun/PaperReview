# E1 직접 선행과 적용 경계

- 확인: 2026-10-22. 문헌 저자 보고와 아래 연구자 판단을 구분한다.
- P 번호는 [기존 dossier](../2026-10-22_vla_rescout/LITERATURE.md)와 같다. Registry 신규 등록·사용자 정독 상태 승격은 하지 않았다.
- 후속 X-VLA·RoboInter·Table30 V2·TrAct 비교와 pinned release 경계는 [E1-R1](./R1_REVIEW.md)에 추가했다. 아래 직접 replay/정렬 선행의 판정은 유지한다.

## 비교표

| 역할·정확한 식별 | 논문이 다루는 조건·interface | E1에 대한 판단 / 남는 질문 |
|---|---|---|
| P4 **Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning**, ICML 2026 [공식](https://proceedings.mlr.press/v306/liu26bu.html), [본문 v2](https://arxiv.org/html/2603.03818v2) | Pretrained VLA 순차 task 학습·ER, backbone/head 및 recovery 분석 | 단순 ER과 encoder/head 대조가 필수다. 다른 조건의 논문과 상충하는 보편 결론으로 만들지 않는다 |
| P10 **Memory Anchors for Continual Robot Learning**, arXiv:2608.26545v1 [§4, §5.5, App. B](https://arxiv.org/html/2608.26545v1) | 관측 overlap → 현재 정책의 새 action noise–denoise 잔차 → 과거 latent 검색. MIR/GSS 대조도 포함 | 서로 다른 로봇의 raw 명령을 직접 빼는 baseline이 아니다. 원 estimator 이후 잔여 질문이어야 한다. 공식 CoRL proceedings는 이번 확인 범위에서 미확인 |
| P12 **Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?**, arXiv:2605.26820v3 [§V-C, VI, App. B](https://arxiv.org/html/2605.26820v3) | 단일 팔·양팔 10-task stream, 일관된 normalization과 비대칭 replay. 표준화된 task progress 평가 | 이질적 kinematic stream 자체는 새롭지 않다. 첫 task 통계의 미래 coverage를 가정하지 않고 실제 다른 하드웨어·task 효과를 분리한다 |
| P15 **SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies**, arXiv:2606.24049v1 [§4, App. A/B.1](https://arxiv.org/html/2606.24049v1) | RGB/proprio → Cartesian state delta → 선형 Action Adapter → command. 기록 pose delta와 command로 보정하며 online LMS 사용 | 물리적 action 의미 통일은 직접 선행이다. Δpose→command의 inverse adapter를 command→실제 결과의 forward oracle로 간주할 수 없다 |
| P13 **HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies**, arXiv:2512.05693v2 [§3, App. C](https://arxiv.org/html/2512.05693v2) | 언어·RGB·proprio, 통합 vector·valid mask, action-space boundary experts·공유 중간층, flow matching | 이질성 분리/공유 자체도 직접 선행. Co-training 효과가 곧 continual retention의 답은 아니다. 공식 acceptance 재확인 전 arXiv로 취급 |
| P11 **Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization**, arXiv:2602.09722v1 [본문](https://arxiv.org/html/2602.09722v1) | EEF-relative 정렬, data mixture·regularization | 정렬 recipe를 약하게 만든 비교를 피한다. 공개 transform은 정렬 경로이며 실제 controller의 동일성을 입증하지 않음 |
| P6 **LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer**, RSS 2026 [공식](https://www.roboticsproceedings.org/rss22/p203.html) | Language-action 표현·cross-embodiment interface | 공개 frame transform에 dataset별 부호/축 규칙이 있다. 동일 7D vector만으로 의미가 같다고 가정하지 않는다. 제목·status는 공식 페이지 기준 |
| **Online Continual Learning with Maximally Interfered Retrieval**, NeurIPS 2019 [공식 본문](https://proceedings.neurips.cc/paper_files/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf), [공식 abstract](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) | 새 batch의 가상 업데이트 전후 old-sample loss 차이로 replay 검색. 원 구현은 classification | Gradient/손실 간섭 대안의 foundation. VLA용 loss·optimizer 변경은 별도 adaptation이며 원 연구의 robot 성능으로 취급하지 않음 |
| **RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation**, RSS 2025 [공식](https://www.roboticsproceedings.org/rss21/p152.html) | 다중 robot demonstration·RGB·proprio·language | Registry에 이미 존재. E1에는 schema 존재보다 EE 품질·command 의미·같은 goal의 qualification이 중요 |
| **RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot**, ICRA 2024 [DOI](https://doi.org/10.1109/ICRA57147.2024.10611615), [저자 공개 자산](https://rh20t.github.io/) | 여러 robot configuration, 시각·force·pose·task 설명 | Registry에 이미 존재. 시간/pose 조회 API는 유용하지만 공통 task coverage와 arm command field를 자동 보장하지 않음 |

P9 CLARE의 adapter 분리 대안은 기존 dossier에서 유지한다. 이번에는 repo revision/tree까지만 추가 확인했으며 전체 구현·RA-L publisher를 재심사했다고 표시하지 않는다.

RH20T의 ICRA metadata는 기존 registry를 유지했다. 이번 DOI 조회는 IEEE 페이지로 연결되지만 browser verification 화면이어서 publisher 본문 재확인은 못 했다. Dataset/API 근거는 저자 공개 source에서 별도로 확인했다.

## Memory Anchors의 재현 경계

App. B.1의 diffusion 설정은 DDIM 100-step schedule 중 20에서 noise를 주고 old validation의 μ+2σ를 사용한다. 그러나 **VLA App. B.6은 prefix-before-LLM latent와 top-10% threshold, flow에 맞춘 변경을 사용한다.** 따라서 diffusion 세부를 π0.5에 그대로 옮기면 원 VLA baseline이 아니다. Flow의 정확한 noise/timestep·normalizer·mask 처리는 공개 구현 확인이 남았다. [본문](https://arxiv.org/html/2608.26545v1#A2.S6).

[Project](https://robot-adaptation.github.io/MemoryAnchors/)의 Code 버튼은 repo 링크가 아니라 미공개 안내 dialog다. 예정 날짜가 지났다는 이유로 release를 가정하지 않는다. SPACE 역시 [공식 project](https://haeone.site/space-website/)에서 Code coming soon 상태다. 둘은 `WAITING_SOURCE`; 미공개 사실만으로 연구 가치가 없다고 판정하지 않는다.

## 검색 범위와 남은 불확실성

`cross-embodiment continual replay conflict/effect`, `action disagreement gradient robot continual`, `Memory Anchors code`, 물리 action 정렬·다중 robot dataset을 검색하고 공식 원문/저자 repo로 확인했다. 기존 P1–P16의 broad discovery 이후 직접 선행의 가정과 구현을 좁혔다. 전수 조사나 미발표 연구 부재의 증명은 아니다.

MIR의 proceedings abstract는 **Maximal**로, 연결 PDF는 **Maximally**로 표기한다. Abstract의 밑줄 없는 GitHub URL은 404였으나 PDF의 [공식 repo](https://github.com/optimass/Maximally_Interfered_Retrieval)는 확인했다. 표기/링크 차이를 별도 연구로 중복 등록하지 않는다.

**현재 신규성 판단:** 단순 정렬+AnchorER, effect-space 가중 잔차, MIR 적용은 독립 신규 방법의 근거가 아니다. 정상 native interface에서 실제 retention을 설명하는 조건과 비용 경계가 남는지는 아직 미검증이다. [주장 계약](./CLAIM_CONTRACT.md).
