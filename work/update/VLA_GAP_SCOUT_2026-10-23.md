# VLA 중심 공백 탐색과 buildup 갱신 — GAP-R1

- 조사 종료일: **2026-10-23 KST**. 대상 기간: 2024–2026.
- 결과: **공백 탐색 완료, 독립 연구 주제의 GO 판정은 아직 없음.** 접촉 센싱의 정보 가치와 controller 효과를 구별하는 질문을 우선 심화하고, 데이터 보완 선택은 직접 충돌이 강해 보류한다.
- 이 문서는 날짜별 조사 기록이다. 질문의 canonical 내용은 [manipulation Open Questions](../../synthesis/03_manipulation_contact.md#gap-contact-2026), [VLA Open Questions](../../synthesis/04_vla_generalist.md#gap-data-2026)에 둔다. 활성 작업은 [TODO](../../TODO.md), 읽기 순서는 [READING_PLAN](../../research/READING_PLAN.md)만 따른다.
- [기계 판독 source ledger](../sources/vla_gap_scout_2026-10-23.json): 정확한 제목·URL·확인 깊이·발표 상태 경계·registry ID 연결. 아래 판정은 논문 보고와 구분한 연구자 해석이다.

## 1. 무엇을 조사했는가

현재 registry **1,037편의 metadata를 검색·분류**하고 그중 2024–2026의 **757편**, 기존 synthesis와 16개 후보 요약을 기준으로 외부 문헌을 교차 조사했다. 1,037편 또는 757편을 이번에 모두 정독한 것은 아니다. 외부에서는 **논문 자료 46건**을 근거 목록에 남겼다. 그중 13건은 제목/공개 ID 기준 기존 registry와 연결됐고, 33건은 아직 연결되지 않았다. 미연결은 정식 중복 심사 전 상태이며 33편을 자동 신규 등록했다는 뜻이 아니다. OpenViTac은 논문 status를 확인하지 못해 별도 resource 1건으로 둔다.

검색은 instruction grounding·conditional action support·data repair/selection, contact sensing·force distillation·feedback/controller, composition·mobile manipulation, world-model evaluation·safety, action-relevant vision을 포함했다. Survey·연구자 reading list·검색 index는 후보 발견에만 사용했고 주장에는 원 논문·공식 program·저자 자료를 연결했다. 핵심 직접 충돌은 HTML 본문과 부록의 지정 구간을 확인했으며, 모든 논문의 전체 수식·실험·코드를 정독한 조사는 아니다.

| 범위 | 확인한 대표 자료 | 이번 확인의 한계 |
|---|---|---|
| CVPR 2024–2026 | Registry의 ManipLLM 등 과거 축, 2025 MoManipVLA, 2026 ForceVLA2·AT-VLA·LIBERO-Plus | CVF 일부 개별 페이지 403. ForceVLA2 공식 페이지, AT-VLA 본문, LIBERO-Plus 공식 목록은 확인 깊이가 다름 |
| NeurIPS 2024–2026 | 기존 foundation/benchmark 축, 2025 ForceVLA·RL generalization, 2026 CIG·CofactVLA·RoboCombine 등 공식 poster 7건 | 2026은 공개 program/abstract. 앞으로 열리는 학회의 proceedings 출판까지 확인한 것으로 쓰지 않음 |
| ICCV 2025 | VLABench 및 기존 long-horizon/spatial VLA 축 | VLABench는 공식 PDF 검색 excerpt 수준. ICCV를 2024/2026에도 열리는 annual venue로 취급하지 않음 |
| ECCV 2024·2026 | Robo-ABC 공식 proceedings, LIBERO-Safety 기존 기록·저자 release | LIBERO-Safety의 2026 채택 표기는 기존 감사·저자 공지에 의존하며 이번 공식 목록 독립 확인은 미완료 |
| ICRA 2024–2026 | 기존 OXE 축, FuSe, FD-VLA 공식 ICRA 2026 program | FuSe는 저자 자료 중심. 모든 ICRA 본문을 검토하지 않음 |
| IROS 2025–2026 | 기존 registry의 navigation/3D 축, LangGap·open-world VLA 외부 검색 | LangGap 저자 repo의 IROS 표기는 확인했으나 공식 program을 찾지 못함. 임의 채택 승격 없음 |
| CoRL 2024–2026 | OpenVLA, masked sensor training, MoTo, CounterAlign | PMLR publication year와 conference year 구분. CounterAlign venue는 기존 registry 근거, 새 본문 비교는 별도 |
| ICLR 2024–2026 | 기존 policy 축, LAPA, DataMIL 공식 proceedings | 최신 data selection을 언어 보완 선택의 완성된 답으로 과장하지 않음 |
| RSS·ICML | RSS 2024 compositional collection·DROID·Colosseum; dWorldEval 저자 자료와 registry ICML 축 | dWorldEval의 ICML 표시는 저자 보고이며 공식 채택 재확인 미완료 |
| RA-L·IJRR·T-RO·Science Robotics | RA-L action-mask paper의 publisher-indexed abstract, STAR-Gen 저자 자료, IJRR survey | 저널 검색은 학회보다 얕다. T-RO·Science Robotics에서 새 결정적 원논문을 확보하지 못했으며 해당 분야에 공백이 있다는 의미가 아님 |
| 최신 preprint | ContactBench 1.0, ECT, CAST, ForceDelta-VLA 등 | Top-tier 채택 논문과 구분하면서도 직접 신규성 충돌을 배제하지 않음 |

검색 종료일 이후 논문, 접근하지 못한 원문, synonym/version alias, 비공개 data·code는 남은 불확실성이다. 빈 검색 결과나 keyword 부재를 미해결 증거로 쓰지 않았다. 검색 범위는 넓지만 systematic review나 citation saturation을 주장하지 않는다.

## 2. Buildup 절차에서 바꾼 부분

[IDEA_BUILDUP_GUIDE](../../research/IDEA_BUILDUP_GUIDE.md)에 **단계 0: 공백 탐색**을 추가하고 기존 1–8단계는 유지했다. 순서는 `관심 행동/조건 → 알려진 답 → 남은 질문 → 직접 충돌 → 경쟁 설명 → 필요한 증거 → 작은 파일럿`이다. 방법·모듈·RL 결합 여부는 그 뒤에 결정한다.

- MIT 교재의 가정 검사, DARPA의 중요성·비용·검증 질문, ICLR 2026의 구체적 문제·새 지식 기준을 재확인했다. 연구 조언은 실무 참고이지 성공을 보장하는 인과 법칙이 아니다. [MIT](https://visionbook.mit.edu/how_to_do_research.html), [DARPA](https://www.darpa.mil/about/heilmeier-catechism), [ICLR](https://iclr.cc/Conferences/2026/ReviewerGuide).
- 기여 유형에 맞는 증거를 요구하도록 ECCV 2026과 NeurIPS E&D 기준을 보강했다. 진단·시스템·평가 연구를 모두 새 architecture로 포장할 필요는 없으며, 반대로 단순 실패 사례 수집도 충분하지 않다. [ECCV](https://eccv.ecva.net/Conferences/2026/ReviewerContributionTypes), [NeurIPS E&D](https://neurips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines).
- 주장 범위, 변동·관측 단위, 예산과 재현 정보를 검토 양식에 연결했다. 문헌 gate 통과는 작은 검증에 투자할 근거이며 효과의 사전 입증 요구가 아니다. [NeurIPS checklist](https://neurips.cc/public/guides/PaperChecklist).
- 서로 다른 sensor/controller/train support를 가진 논문의 수치를 모순처럼 비교하지 않는다. `논문 보고 / 연구자 추론 / 미확인`과 가장 강한 반례를 필수로 남긴다.

## 3. 이미 연구된 문제와 실제로 남은 질문

| 조사한 방향 | 이미 확인된 답·직접 충돌 | 이번 판단 |
|---|---|---|
| 언어를 무시하는 VLA | LangGap, CounterAlign, CIG, CofactVLA, ECT가 서로 다른 현상·개입을 다룸 | 넓은 문제 제기는 신규성이 약함. 모든 실패를 language neglect로 묶지 않음 |
| 데이터 양보다 구성·언어 supervision | DataMIL, RSS compositional collection, CAST, ECT | 단순 data diversity·counterfactual label 추가는 기각. 보완 전 선택 규칙만 조건부 질문으로 보류 |
| Tactile/force를 추가한 VLA | ForceVLA/2, AT-VLA, FD-VLA, ForceDelta-VLA, ContactBench | 센서 추가 자체는 기각. 필요한 정보와 활용 가능한 controller를 분리한 설계 판단이 남는지 심화 |
| 센서 고장 대응 | Masked training, AT-VLA missing-modality 비교 | VLA에 modality dropout을 붙이는 것만으로 새 기여를 주장하지 않음 |
| 조합 skill과 navigation→manipulation 연결 | RoboCombine, MoTo, MoManipVLA, 기존 D2 | Handoff 상태·base placement·execution competence를 이미 다룸. 기존 후보 자동 재개 없음 |
| World model의 행동 관련 평가 | WorldEval, dWorldEval, RoboWorld, DreamTrue, decision-centric position | 일반적 action fidelity·policy ranking은 선행이 강함. 새 독립 후보로 올리지 않음 |
| Safety·reasoning faithfulness | LIBERO-Safety, open-world VLA 연구, Say the Same Act Differently, 기존 C4/C6 | 성공률 밖의 문제를 측정한다는 말만으로 차별화되지 않음 |
| 3D·affordance를 VLA에 연결 | Robo-ABC 및 registry의 spatial/3D policy 축 | 별도 3D benchmark 향상보다 실제 행동 차이가 먼저 필요. 이번에는 VLA 밖으로 강제 확장하지 않음 |

표의 논문별 원자료와 확인 수준은 아래 source index 및 JSON을 따른다. Abstract 기반 방향 제외는 큰 주장 수준의 충돌 판단이며, 모든 세부 질문이 해결됐다는 뜻은 아니다.

## 4. 현재 남길 질문과 다음 검토

| 문헌 심화 순서 | 남은 질문 | 왜 아직 GO가 아닌가 |
|---|---|---|
| 먼저 검토 | [GAP-CONTACT](../../synthesis/03_manipulation_contact.md#gap-contact-2026): 실측 접촉 정보의 필요성과 학습·controller의 병목을 구별해 개입 효과를 예측할 수 있는가? | ContactBench가 hidden mechanics·sensor coverage·통합 방식까지 이미 분석한다. 그 설명을 재현하는 것 이상이 필요하며 같은 조건 비교가 가능한지 미확인 |
| 보류 | [GAP-DATA](../../synthesis/04_vla_generalist.md#gap-data-2026): 기존 데이터 보완과 새 시연 수집 중 어디에 예산을 쓸지 사전에 판별할 수 있는가? | ECT가 기존 counterpart 활용과 새 action-valid data를 이미 비교한다. 비용을 포함한 선택의 새 예측이 남는지 불명확 |

접촉 질문의 핵심은 **VLA 입력에서 센서를 빼는 것과 전체 폐루프에서 센서를 없애는 것이 다르다**는 비교 계약이다. 하위 force controller가 센서를 쓰면 sensor-free 시스템이 아니다. 실측/증류 입력과 controller의 정보 사용을 나누어야 어떤 하드웨어·학습 투자가 필요한지 판단할 수 있다. 이는 이번 조사의 연구자 해석이며 새 발견이나 입증된 정리가 아니다.

다음 **GAP-R2는 비실험 문헌·공개 interface 감사**다. ContactBench, ForceVLA/2, AT-VLA, FD-VLA, ForceDelta-VLA의 본문·부록·공개 code에서 `학습 supervision / policy input / controller input / sensor coverage / rate / task·initialization / trial / release`를 대조한다. 최소 한 task에서 공정 비교가 가능하고 기존 연구와 다른 예측이 남는지 판정한다. 없으면 접촉 후보도 종료하거나 기존 결과의 비교 자료로만 남긴다. 외부 연구자 피드백·정책 효과·실행 가능성 검증은 아직 하지 않았다.

GPU는 학습 비용의 일부만 해결한다. Contact 데이터의 정렬·물리 calibration·실제 sensor/hardware가 필요한지 먼저 확인한다. 이번에 simulation, inference, 학습, package 설치, Docker 실행은 하지 않았다.

## 5. Registry 연결과 등록 경계

Registry identity·tier·reading tracker는 변경하지 않았다. 46건의 source 확인 결과를 기존 canonical provenance에 일괄 덮어쓰지 않았다. 새로운 정독 완료 또는 FULL_TEXT_CHECKED 승격도 없다. 부분 본문 대조와 사용자의 읽기 이력은 별개다.

후속 등록 심사의 직접 필요 후보는 ContactBench, ForceDelta-VLA, DataMIL, LangGap, CAST, ECT, CIG, RoboCombine이다. 이는 읽기 priority 목록이 아니라 이번 질문의 근거를 재사용하기 위한 **admission 검토 범위**다. 정확한 public ID·version·venue·중복 확인 후 관련성이 남는 논문만 `register_papers.py`와 표준 5개 note로 등록한다. Status 미확인 논문은 arXiv로 유지하며, 기존 등록 논문은 중복 생성하지 않는다.

## 6. Source index

각 행의 ID는 이번 source ledger 내부 식별자이며 registry paper ID가 아니다. `미연결`은 title/ID 기반 1차 결과로, 신규 논문 확정이 아니다. 본문 anchor·검토 경계·추가 project URL은 JSON에 남겼다. 아래 표는 조사 당시 snapshot이다.

<!-- SOURCE_INDEX:START -->
| Source | 논문·원자료 | 발표 상태·확인 경계 | Registry |
|---|---|---|---|
| S01 | [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://papers.nips.cc/paper_files/paper/2025/hash/8633b46e12cc5f2ee1f05a6ca2c65b38-Abstract-Conference.html) | 2025 NeurIPS; official proceedings | [pr-0128](../../2025/NeurIPS/2025_NeurIPS_ForceVLA-Enhancing-VLA-Models-with-a-Force-aware-MoE-for-C/01_overview.md) |
| S02 | [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html) | 2026 CVPR; official CVF | [pr-0691](../../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md) |
| S03 | [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://arxiv.org/html/2605.07308v1) | 2026 CVPR; registry venue retained, CVF endpoint inaccessible this pass | [pr-0690](../../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md) |
| S04 | [FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation](https://arxiv.org/html/2602.02142v1) | 2026 ICRA; official program + existing registry | [pr-0185](../../2026/ICRA/2026_ICRA_FD-VLA-Force-Distilled-Vision-Language-Action-Model-for-Co/01_overview.md) |
| S05 | [ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation](https://arxiv.org/html/2610.24512v1) | 2026 arXiv; acceptance unverified | 미연결 |
| S06 | [ForceDelta-VLA: Distilling Force-Conditioned ActionCorrections for Contact-Rich Manipulation](https://arxiv.org/abs/2609.18242) | 2026 arXiv; acceptance unverified | 미연결 |
| S07 | [Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding](https://arxiv.org/abs/2501.04693) | 2025 arXiv; ICRA author-reported, official status not reverified | 미연결 |
| S08 | [Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure](https://proceedings.mlr.press/v270/skand25a.html) | CoRL 8th conference; PMLR publication 2025 | 미연결 |
| S09 | [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) | 2026 ICLR; official proceedings | 미연결 |
| S10 | [LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models](https://arxiv.org/html/2603.00592v1) | 2026 arXiv; IROS author-reported, official program not located | 미연결 |
| S11 | [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](https://arxiv.org/html/2608.21740v1) | 2026 CoRL; existing registry verification, forum inaccessible this pass | [pr-1033](../../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) |
| S12 | [CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models](https://arxiv.org/html/2508.13446v1) | 2025 arXiv; acceptance unverified | 미연결 |
| S13 | [When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models](https://arxiv.org/html/2609.39971v1) | 2026 arXiv; acceptance unverified | 미연결 |
| S14 | [When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs](https://arxiv.org/abs/2602.17659) | 2026 arXiv; acceptance unverified | 미연결 |
| S15 | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/CVPR2026?day=2026-06-07) | 2026 CVPR; official proceedings listing | 미연결 |
| S16 | [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827) | 2025 arXiv; current acceptance unverified | 미연결 |
| S17 | [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.pdf) | 2025 ICCV; official CVF | [pr-0788](../../2025/ICCV/2025_ICCV_VLABench-A-Large-Scale-Benchmark-for-Language-Conditioned/01_overview.md) |
| S18 | [A Taxonomy for Evaluating Generalist Robot Manipulation Policies](https://arxiv.org/abs/2503.01238) | 2025 arXiv, updated 2026; RA-L author-reported, publisher not accessed | 미연결 |
| S19 | [Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs](https://arxiv.org/abs/2603.11426) | 2026 arXiv; acceptance unverified | 미연결 |
| S20 | [Efficient Data Collection for Robotic Manipulation via Compositional Generalization](https://roboticsproceedings.org/rss20/p013.html) | 2024 RSS; official proceedings | 미연결 |
| S21 | [Latent Action Pretraining from Videos](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html) | 2025 ICLR; official proceedings | [pr-0938](../../2025/ICLR/2025_ICLR_Latent-Action-Pretraining-from-Videos/01_overview.md) |
| S22 | [What Can RL Bring to VLA Generalization? An Empirical Study](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) | 2025 NeurIPS; official proceedings | [pr-0956](../../2025/NeurIPS/2025_NeurIPS_What-Can-RL-Bring-to-VLA-Generalization-An-Empirical-Study/01_overview.md) |
| S23 | [MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation](https://proceedings.mlr.press/v305/wu25c.html) | 2025 CoRL; official PMLR | [pr-0060](../../2025/CoRL/2025_CoRL_MoTo-A-Zero-shot-Plug-in-Interaction-aware-Navigation-for/01_overview.md) |
| S24 | [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](https://arxiv.org/abs/2503.13446) | 2025 CVPR; existing registry, author source rechecked | [pr-0975](../../2025/CVPR/2025_CVPR_MoManipVLA-Transferring-Vision-language-action-Models-for/01_overview.md) |
| S25 | [Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) | 2024 ECCV; official proceedings | 미연결 |
| S26 | [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://github.com/LIBERO-SAFETY/LIBERO-Safety) | 2026 ECCV; existing registry and author acceptance notice, official listing not independently resolved | [pr-0259](../../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md) |
| S27 | [How VLAs (Really) Work In Open-World Environments](https://arxiv.org/abs/2604.21192) | 2026 arXiv; IROS status unverified this pass | 미연결 |
| S28 | [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://dworldeval.github.io/) | 2026; ICML author-reported, official acceptance not located | 미연결 |
| S29 | [WorldEval: World Model as Real-World Robot Policies Evaluator](https://worldeval.github.io/) | 2025/2026 version year and venue unresolved | 미연결 |
| S30 | [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](https://arxiv.org/abs/2607.01060) | 2026 arXiv; acceptance unverified | 미연결 |
| S31 | [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](https://arxiv.org/abs/2610.12468) | 2026 arXiv; acceptance unverified | 미연결 |
| S32 | [How Should World Models Be Evaluated? A Decision-Making-Centric Position](https://arxiv.org/abs/2606.15032) | 2026 arXiv; acceptance unverified | 미연결 |
| S33 | [Language-Driven Multi-Task Manipulation With Action-Mask-Enhanced Multimodal Learning](https://doi.org/10.1109/LRA.2026.3674003) | 2026 RA-L; publisher-indexed metadata/abstract, page later challenged | 미연결 |
| S34 | [Bridging language and action: A survey of language-conditioned robot manipulation](https://journals.sagepub.com/doi/10.1177/02783649261468360) | 2026 IJRR; publisher record | 미연결 |
| S35 | [Inductive Generalization for Robotic Manipulation](https://arxiv.org/html/2606.20999v1) | 2026 arXiv; acceptance unverified | 미연결 |
| S36 | [ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver](https://ojs.aaai.org/index.php/AAAI/article/view/38921) | 2026 AAAI; official proceedings | 미연결 |
| S37 | [Exploring the Limits of Compositional Generalization in Vision-Language-Action Manipulation](https://neurips.cc/virtual/2026/poster/139255) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S38 | [Counterfactual Instruction Grounding for Vision-Language-Action Models](https://neurips.cc/virtual/2026/poster/152584) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S39 | [Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models](https://neurips.cc/virtual/2026/poster/148883) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S40 | [CofactVLA: Deconfounding Vision-Language-Action Models via Counterfactual Intervention](https://neurips.cc/virtual/2026/poster/153110) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S41 | [Say the Same, Act Differently: Text-Orthogonal Action Subspaces in Reasoning Vision-Language-Action Models](https://neurips.cc/virtual/2026/poster/154708) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S42 | [Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models](https://neurips.cc/virtual/2026/poster/155737) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S43 | [Beyond Data Scaling: Representation-Centric Pre-training for Vision-Language-Action Models](https://neurips.cc/virtual/2026/poster/155956) | 2026 NeurIPS official program/poster listed; proceedings publication not asserted | 미연결 |
| S44 | [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) | CoRL 2024; PMLR publication 2025 | [pr-0051](../../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md) |
| S45 | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) | 2024 RSS; official proceedings | [pr-0732](../../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md) |
| S46 | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://roboticsproceedings.org/rss20/p133.html) | 2024 RSS; official proceedings | 미연결 |
<!-- SOURCE_INDEX:END -->

## 7. 검증

`py_compile`, `build_reading_tiers.py`, `audit_repository.py`, `git diff --check`를 통과했다. Repository audit 오류·경고는 0이다. Registry 1,037편, CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242, active reading 322행·history 47행을 유지했다.

작업 시작 시 SHA256과 비교하여 `papers.json`, `READING_STATUS.csv`, `READING_STATUS_HISTORY.csv`, `READING_TIERS.csv`가 byte 단위로 동일함을 확인했다. Source 46건의 ID 유일성과 연결된 overview 경로도 검사했다. 기존 DOC-QA1의 미게시 note 수정과 사용자 변경을 보존했다. 이번 변경을 Git에 새로 commit/push하지 않았다. 문헌 검토를 정책 효과 검증으로 승격하지 않는다.
