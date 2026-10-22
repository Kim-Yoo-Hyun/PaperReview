# VLA 재탐색 문헌과 근거 경계

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다. Memory Anchors·CounterAlign·RoboFollow의 CoRL 2026 Poster를 공식 metadata로 추가 확인했다.

- 확인일: 2026-10-22 KST. [선별 결과](./README.md) · [E1 질문](./E1_QUESTION.md)
- 공식 proceedings로 확인한 논문 8편과 직접 충돌/버전 확인에 필요한 8편을 비교 표에 남겼다. 아래 16편 중 기존 registry 연결은 5편이며, 나머지는 이 dossier의 외부 비교 문헌이다. 신규 registry 등록·tier 변경은 하지 않았다.
- `본문 일부`는 표시한 section의 직접 확인을 뜻한다. 부록·공개 구현 전체 정독이나 사용자 reading status `READ`를 뜻하지 않는다. 원문 성능은 저자 보고이며 우리 재현 결과가 아니다.
- Publication status는 확인한 출처의 수준으로 표시한다. 저자 표기만 있는 venue를 공식 채택으로 승격하지 않는다.

## 1. 공식 proceedings를 확인한 비교 기준

| ID | 정확한 title / 공식 출처 | Year·venue | 이번 확인 범위와 역할 | Registry |
|---|---|---|---|---|
| P1 | [Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation](https://roboticsproceedings.org/rss20/p093.html) | 2024 RSS | 공식 abstract. Manipulation/navigation 공동 학습의 가능성을 보여주는 출발점. Goal-conditioned policy 결과를 모든 VLA의 전이 보장으로 확대하지 않음 | pr-0934 |
| P2 | [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html) | 2025 ICLR | 공식 abstract. 물리 의미를 유지하는 통일 action space의 직접 선행 | pr-0083 |
| P3 | [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://roboticsproceedings.org/rss21/p012.html) | 2025 RSS | 공식 abstract. 고주파 action의 압축/tokenization 기준. Temporal representation 자체가 미개척이라는 주장 배제 | pr-0749 |
| P4 | [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](https://proceedings.mlr.press/v306/liu26bu.html) | 2026 ICML | [arXiv v2](https://arxiv.org/html/2603.03818v2) §3–5의 관련 부분. 강한 ER·pretraining·모듈 교환/recovery가 비교 기준 | 외부 |
| P5 | [Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html) | 2026 ICLR | 공식 abstract. VLM2VLA의 자연어 action·LoRA·semantic retention. VQA 보존과 순차 robot-skill retention은 별도 항목 | 외부 |
| P6 | [LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer](https://www.roboticsproceedings.org/rss22/p203.html) | 2026 RSS | 공식 abstract·[project](https://lap-vla.github.io/)·repo landing. 자연어 action과 새로운 로봇 전이의 직접 비교. 본문/adapter 세부는 후속 | 외부 |
| P7 | [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](https://roboticsproceedings.org/rss22/p010.html) | 2026 RSS | 공식 abstract. HALO의 task-relevant QA supervision, spurious retrieval/model drift를 확인. 일반 메모리 관련성 주장의 충돌 | pr-0819 |
| P8 | [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_Adaptive_Action_Chunking_at_Inference-time_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf) | 2026 CVPR main | CVF 공식 본문 abstract/도입부. Entropy 기반 chunk 길이 선택; consistency/reactivity 균형을 이미 다룸. 로컬 PDF 저장 없음 | 외부 |

P4의 v1을 처음 조회한 뒤 [최신 abstract/version history](https://arxiv.org/abs/2603.03818)를 확인하고 v2 관련 본문으로 재확인했다. 본문의 replay/recovery 조건은 특정 benchmark와 model에 한정된다. 빠른 재학습을 “이미 능력을 완전히 보존한다”는 뜻으로 사용하지 않는다. PMLR 공식판과 arXiv v2의 모든 줄이 동일하다는 검증은 하지 않았다.

## 2. 직접 충돌과 최신 버전 확인

| ID | 정확한 title / 원문 | 확인한 status·version | 확인 내용과 E1/E2에 주는 제한 | Registry |
|---|---|---|---|---|
| P9 | [CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion](https://arxiv.org/abs/2601.09512) | 2026; 기존 registry RA-L, 공식 repo도 RA-L 표기. 이번 publisher 재확인 미완료 | Abstract·[project](https://tum-lsy.github.io/clare/)·[공식 repo](https://github.com/learnsyslab/clare). Exemplar-free adapter 확장/routing이 기존 대안. 전체 implementation audit 미완료 | pr-0274 |
| P10 | [Memory Anchors for Continual Robot Learning](https://arxiv.org/html/2608.26545v1) | arXiv 2026 v1; [저자 project](https://robot-adaptation.github.io/MemoryAnchors/)는 CoRL 2026 표기, 공식 proceedings 미확인 | §3–5 관련 본문. Latent overlap→noise–denoise action disagreement→과거 경험 선택이 이미 제안됨. E1의 최우선 직접 baseline | 외부 |
| P11 | [Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization](https://arxiv.org/html/2602.09722v1) | arXiv 2026 v1; 공식 conference/journal 채택 미확인 | §III–V 관련 부분·[공식 repo](https://github.com/BeingBeyond/Rethink_VLA). EEF-relative 정렬과 heterogeneous mixture의 간섭을 이미 연구. “로봇 데이터를 섞으면 손해일 수 있다”는 새 질문이 아님 | 외부 |
| P12 | [Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/html/2605.26820v3) | arXiv 2026 **v3, 2026-08-08**; 공식 채택 미확인 | §V–VII 관련 본문. 10-task single-arm/bimanual stream, normalization 일관성, 비대칭 replay를 확인. v1의 4-task 설명을 최신 범위로 사용하지 않음 | 외부 |
| P13 | [HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies](https://arxiv.org/html/2512.05693v2) | arXiv 2025→2026 v2, 2026-07-08; ICLR 표기는 공식 확인 보류 | 도입부·abstract·[repo](https://github.com/ZhiyingDu/HiMoE-VLA). Action-space 경계와 잔여 이질성을 분리하는 MoE. E1의 분리 모델 대조이며 method/appendix 전체 비교 미완료 | 외부 |
| P14 | [Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization](https://arxiv.org/html/2610.05230v1) | arXiv 2026 v1, 2026-10-04 | Abstract·§1–2. Spline 기반 trajectory와 motion-dependent horizon, 서로 다른 sampling grid를 이미 제안. E2의 continuous-time/spline 신규 방법 주장과 직접 충돌 | 외부 |
| P15 | [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](https://arxiv.org/abs/2606.24049) | arXiv 2026 v1 | Abstract. Cartesian state delta→robot-specific command adapter, control frequency·weight·gain shift 평가를 명시. E1의 물리 정렬 대조, E2의 직접 충돌. 본문·code 대조는 E1-L1 | 외부 |
| P16 | [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models](https://arxiv.org/abs/2610.25961) | arXiv 2026 **v2, 2026-10-21** | 최신 abstract. 여러 temporal granularity/horizon decoder와 router를 결합. E2의 adaptive execution을 넓은 새 기여로 주장할 수 없음 | 외부 |

P12는 fixed physical-platform setup을 한계로 명시하지만, 이미 single-arm/bimanual의 kinematic transition을 다룬다. 그 한계 문장을 “cross-embodiment만 붙이면 신규성이 생긴다”는 근거로 사용하지 않는다. E1은 **정렬 후에도 남는 충돌 추정·replay 선택의 차이**를 따로 입증해야 한다. 이 문장은 연구자 해석이다.

## 3. 공개 자산의 실제 확인 수준

| 자산 | 이번에 확인한 것 | 아직 확보하지 않은 것 |
|---|---|---|
| P4 [Continual-VLAs](https://github.com/Continual-VLAs) | PMLR Software 링크의 목적지가 organization임 | 특정 revision·훈련 entrypoint·checkpoint/data qualification |
| P9 [CLARE](https://github.com/learnsyslab/clare) | 저자 project에서 연결된 공식 repo와 RA-L 자기표기; 이전 utiasDSL URL이 redirect됨 | replay baseline과 adapter routing의 실제 입력·자원·동등 예산 |
| P10 [Memory Anchors project](https://robot-adaptation.github.io/MemoryAnchors/) | 원문과 결과 설명; 조회한 페이지의 `Code`는 클릭 가능한 repo 링크로 확인되지 않음 | 공식 구현 release 식별. “코드가 영구히 없다”는 판단은 아님 |
| P11 [Rethink_VLA](https://github.com/BeingBeyond/Rethink_VLA) | README의 pretraining/post-training 경로 및 checkpoint 링크, configs/src 디렉토리 | checkpoint tensor·두 로봇 공통 task coverage·정확한 label mapping·native 실행 |
| P13 [HiMoE-VLA](https://github.com/ZhiyingDu/HiMoE-VLA) | 저자 arXiv에서 연결된 공식 repo | 본문/implementation 일치·순차 적응 지원·실행 비용 |
| P6 [LAP](https://github.com/lihzha/lap) | 공식 project의 Code/Checkpoints 링크와 repo landing | release별 action frame·normalization·기존 로봇 능력·현재 머신 실행 자격 |

URL이나 README 존재만으로 “baseline 확보 완료” 또는 “현재 컴퓨터에서 실험 가능”으로 표시하지 않는다. 이 표는 다음 정적 검토의 출발점이다. E1-L1은 공개 code text와 metadata로 먼저 진행할 수 있다.

## 4. 검색 범위와 한계

- Registry에서는 `continual`, `forgetting`, `Memory Anchors`, `HiMoE`, `Rethinking Visual`, `LAP`, `Actions as Language`, `RDT-1B`, `FAST`, `Adaptive Action Chunking`, `SPACE`, `Vela` 등의 title/identity를 대조했다. `Grounding Actions in Camera Space`를 새 SPACE 논문과 혼동하지 않았다.
- 외부에서는 continual forgetting/replay, heterogeneous negative transfer, action-space alignment, memory retrieval, action chunk consistency, control frequency/temporal representation을 검색하고 공식/저자 원문으로 좁혔다.
- Awesome list·자동 요약·AI review 페이지는 발견 경로로만 취급했다. 논문 method와 status의 최종 근거로 인용하지 않는다.
- OpenReview 일부 forum은 browser verification 화면이 나와 내용을 확인하지 못했다. CAPTCHA 우회 없이 공식 proceedings 또는 arXiv로 확인 범위를 제한했다. HiMoE의 acceptance는 이 때문에 확정하지 않았다.
- CVF P8 HTML은 403이었지만 공식 CVF proceedings index와 공식 paper의 웹 텍스트에서 title·CVPR main status를 확인했다. PDF를 로컬에 저장하지 않았다.
- Robotics의 모든 2024–2026 논문과 citation graph를 전수 심사한 결과가 아니다. 특히 E1과 정확히 같은 effect-based cross-embodiment replay의 부재는 아직 입증되지 않았다.

## 5. Registry admission과 구분

이번 요청은 새 주제 탐색이므로 외부 11편을 이 비교 dossier에 남겼다. P4/P6/P8과 E1 직접 비교 P10–P13/P15는 후속 registration 검토 가치가 있지만, 이를 자동 CORE/NEXT 승격으로 해석하지 않는다. 정식 추가 시 public ID/normalized title의 전체 dedup, 공식 status, 5개 표준 note, generator/audit 절차를 적용한다. 이 파일은 별도 읽기 우선순위 source가 아니다.
