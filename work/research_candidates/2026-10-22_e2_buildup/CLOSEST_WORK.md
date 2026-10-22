# E2 직접 선행과 신규성 경계

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다.

- 확인: 2026-10-22. [결론](./README.md) · [source 감사](./SOURCE_INTERFACE_AUDIT.md)
- 공식 publication 근거와 method 본문 근거를 분리한다. 아래 9편은 외부 비교 dossier이며 신규 registry admission이 아니다. 2024–2026을 검색하되 직접 충돌 연구가 집중된 2025–2026을 상세 비교했다. Venue quota를 채우지 않는다.
- 본문 확인 범위는 지정 section 중심이다. 사용자 정독 완료, 전체 부록/코드 재현을 의미하지 않는다. 수치 결과는 저자 보고이며 이번에 정책 실행은 없다.

## 공식 proceedings가 있는 기준 4편

| ID / 정확한 title | Status와 source | Interface·가정·학습 / 확인 범위 | E2가 다시 주장할 수 없는 것 |
|---|---|---|---|
| P1 — Real-Time Execution of Action Chunking Flow Policies | **NeurIPS 2025 main**, [공식](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html); [v2](https://arxiv.org/html/2506.07339v2), [project](https://pi.website/research/real_time_chunking) | §2–4·Algorithm 1. 관측/이전 chunk/지연 추정으로 이미 실행될 prefix를 고정하고 나머지를 inpainting. 추가 학습 없는 비동기 실행. Kinetix와 실제 π0.5 실험을 구분 | 지연과 실행 horizon의 tradeoff, 연속성을 보존하는 비동기 VLA 자체. Sim Kinetix 결과를 모든 VLA 결과로 바꾸지 않음 |
| P2 — SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies | **CoRL 2025**, [PMLR](https://proceedings.mlr.press/v305/arachchige25a.html); [v2](https://arxiv.org/html/2506.11948v2), [project](https://sail-robot.github.io/) | §3–4·App. C/D. IL motion target, 추론 consistency, tracking, speed modulation, latency scheduling의 결합. 시연·카메라·고수준 command·저수준 torque 주기를 따로 설명 | faster-than-demo, controller-invariant target, multirate 설계 자체. 모든 baseline이 같은 controller 조건이라고 추정하지 않음 |
| P3 — Learning High-Frequency Continuous Action Chunks in Latent Space | **ICML 2026**, [PMLR](https://proceedings.mlr.press/v306/wang26lj.html); [v1](https://arxiv.org/html/2605.24931v1), [code](https://github.com/tars-robotics/RTR) | §3–4. 고주파 action의 VAE latent 학습과 Reuse-then-Refine. DP/OpenVLA-OFT/π0.5, xArm contact task. 저주파 interpolation 대조를 이미 포함 | 고주파 latent·chunk seam 보정·단순 보간 대조의 최초 제안. 특정 tracking regime의 설명을 모든 controller에 일반화하지 않음 |
| P4 — Adaptive Action Chunking at Inference-time for Vision-Language-Action Models | **CVPR 2026**, [공식 목록](https://openaccess.thecvf.com/CVPR2026?day=2026-06-06), [공식 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_Adaptive_Action_Chunking_at_Inference-time_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf); [v2](https://arxiv.org/html/2604.04161v2), [project](https://lance-lot.github.io/adaptive-chunking.github.io/) | §3–5·Algorithm 1. 다수 action sample의 entropy 변화와 최소 이동량을 이용해 실행 길이를 선택. GR00T 기반 공개 client/server, 추가 학습 없이 추론 시 적용 | entropy 기반 adaptive horizon. 실행 길이 변경의 관측/계산 비용을 공짜로 취급하지 않음 |

AAC의 CVF 직접 open은 403이었다. 공식 CVF day index와 PDF의 검색 색인에 title·CVPR 2026·pp.20802–20811을 확인했고 method는 arXiv v2로 읽었다. 접근 실패를 본문 정독으로 표시하지 않는다. RTC는 ICLR이 아닌 NeurIPS 공식 entry를 기준으로 정정해 사용했다.

## 최신 직접 충돌 preprint 5편

| ID / 정확한 title | Source·status | 확인 범위 / 이미 있는 내용 | E2 해석의 경계 |
|---|---|---|---|
| P5 — Leave No Observation Behind: Real-time Correction for VLA Action Chunks | [arXiv:2509.23224v1](https://arxiv.org/html/2509.23224v1), [LIBERO code](https://github.com/k1000dai/a2c2-libero), [Kinetix code](https://github.com/k1000dai/a2c2-kinetix). **공식 acceptance 미확인**, arXiv로 유지 | §2–5·App. A/Table 7. Frozen base 위 learned residual이 최신 관측·base action·chunk 정보를 사용. Delay와 execution horizon을 별도로 바꿈 | Fresh observation correction과 delay/horizon 분리 자체는 선행. 추가 head의 학습 비용과 checkpoint 공개 경계를 포함해야 함 |
| P6 — SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies | [arXiv:2606.24049v1](https://arxiv.org/html/2606.24049v1), [project](https://haeone.site/space-website/). **arXiv** | §5.3. State-delta target과 command adapter. 15→30 Hz 실행, payload·gain 변경도 다룸 | 같은 물리 시간에서의 sample 재구성이 아니라 더 빠른 실행을 포함. Frequency shift 자체가 비어 있는 주제는 아님 |
| P7 — Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization | [arXiv:2610.05230v1](https://arxiv.org/html/2610.05230v1), [project](https://clementine24.github.io/Vela/). **arXiv**, project code는 coming soon | §3–4·§4.4/App. B.2. Continuous spline action curve·adaptive horizon, post-hoc fitting과 horizon-matched 재학습 대조 | 연속 곡선/임의 sampling을 새 발명으로 주장 불가. Horizon 통제 대조가 없다는 주장도 불가. 실제 closed-loop 동치 보장은 별개 |
| P8 — PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models | [arXiv:2610.25961v2](https://arxiv.org/html/2610.25961v2), [project](https://pacevla.github.io/). **arXiv**, 2026-10-21 v2 반영 | §3.5·App. C.3. Temporal quantization/router와 controller tracking을 연결. 가속 방법들에는 task별 같은 조정 gain, base GR00T에는 default gain을 사용한다고 명시 | 적응형 시간 압축은 직접 충돌. Gain 차이가 모든 성능 이득의 원인이라고 단정할 근거도 없음 |
| P9 — Measuring the Stability Assumption Behind Action Chunking | [arXiv:2610.01626v1](https://arxiv.org/html/2610.01626v1), [저자 페이지](https://aryangoyal7.github.io/publication/2026-stability-action-chunking). **arXiv** | 방법·평가 절. 같은 상태에서 perturbation을 가한 open-loop/closed-loop branch 비교. GR00T의 manipulation task에서 finite-horizon divergence로 구간 분류 | “상태에 따라 chunk의 안정성이 다르다”는 진단도 이미 있음. 추정 slope는 전역 안정성 보증·최적 horizon이 아님. 확인한 페이지에서 실행 repo는 미식별 |

PaceVLA·SPACE의 공개 구현을 이번에 pinned 실행 경로로 확보한 것은 아니다. P5의 ICLR 표기를 보이는 비공식 결과를 공식 채택 근거로 채택하지 않았다. 공식 source를 찾지 못했다는 것이 reject의 증거는 아니다.

## Foundation과 남은 gap의 크기

기존 registry의 [FAST](https://roboticsproceedings.org/rss21/p012.html), [RDT-1B](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html)는 시간 압축/행동 interface의 출발점이다. 기존 [VLA scout](../2026-10-22_vla_rescout/LITERATURE.md)의 연결을 재사용했으며 이번에 해당 논문의 정독 상태를 올리지 않았다.

**연구자 해석:** 이 문헌 집합은 E2의 broad motivation과 대부분의 쉬운 방법 후보를 이미 포함한다. 남은 비교 조건의 차이는 진단의 동기가 될 수 있지만 그 자체가 미해결 현상이나 새 기여는 아니다. Time/control을 맞춘 뒤 유용한 설계 지식이 추가되는지 확인해야 한다. 지금 확보한 근거만으로는 새로운 대형 모델/학습법을 정당화하지 못한다.
