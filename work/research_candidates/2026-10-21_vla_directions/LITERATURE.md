# VLA 신규 방향의 문헌·출처 대조

- 웹 확인: 2026-10-21 KST
- [최종 후보 비교](./README.md) · [D1 가설과 기각 기준](./D1_SENSOR_CONFLICT.md)
- 범위: 목적을 정한 표적 문헌 조사. 2024–2026 전체 top-tier 논문의 systematic review는 아니다.
- 최초 조사 30편 중 기존 16편·외부 14편이었으나, 후속 요청으로 외부 14편 전부 등록했다. GAP·G-PSMR 2편도 추가했다. 아래 표는 최초 source 범위를 보존하되 identity·주요 version 정정을 반영한다. [최신 source audit](../2026-10-21_d1_buildup/CLOSEST_WORK.md).
- 본문 절 확인 7편은 X01/X02/X03/X04/X06/X07/X08이다. 나머지는 abstract·project·명시한 공식 검색 발췌 수준이다. 모든 논문의 전체 본문 정독을 뜻하지 않는다.

## 1. 검색과 대조 방법

Registry manifest, PAPER.md, tier/status와 기존 C1–C6 결과를 먼저 확인했다. 2024년 155편, 2025년 349편, 2026년 198편의 metadata를 최근 탐색 범위로 삼아 VLA, proprioception, contact, bimanual, mobile manipulation, instruction correction 등을 검색했다. 이후 공식 RSS 2026 program과 PMLR/CVF/NeurIPS/IEEE source를 탐색하고, 가까운 최신 preprint를 역으로 대조했다.

대표 외부 query는 `vision-language-action sensor conflict`, `sensor failure`, `calibration proprioception robustness`, `instruction change interruption`, `goal switching`, `bimanual role switching contact`, `mobile manipulation base placement reachability`, `carried object navigation`이다. Search engine이 반환한 블로그·AI 요약·비공식 paper notes는 최종 claim의 근거로 사용하지 않았다. 검색에서 동일 질문을 못 찾은 사실은 신규성의 증명이 아니다.

CoRL 2024 논문은 PMLR volume 270의 publication year가 2025로 표시된다. 아래는 conference event year 2024를 유지한다. 2026년 아직 개최/출판 상태가 다른 venue를 날짜만으로 acceptance 처리하지 않았다. NeurIPS 2026·CoRL 2026을 전수검토했다고 주장하지 않는다.

## 2. 공식 학회·저널 근거 20편

아래 제목 링크가 publication 근거다. `pr-...`는 등록된 stable identity다. 공식 abstract는 저자의 요약 주장이지 우리의 재현 결과가 아니다.

| ID / registry | 논문과 검증한 venue | 확인한 내용과 후보와의 관계 |
|---|---|---|
| L01 / pr-0051 | [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html), CoRL 2024 | 공개 generalist VLA와 fine-tuning 기반. 기존 OpenVLA와 OFT 계열의 state/action interface를 같은 것으로 가정하지 않는다. 공식 abstract. |
| L02 / pr-0724 | [Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html), NeurIPS 2024 | HPT는 서로 다른 로봇의 visual/proprioceptive 입력을 공유 trunk에 연결한다. D1의 cross-embodiment 표현 선행; language-conditioned VLA 자체와는 구분. 공식 abstract. |
| L03 / pr-0054 | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://proceedings.mlr.press/v270/huang25g.html), CoRL 2024 | 언어·RGB-D에서 생성한 공간·시간 제약을 최적화. D2/D3의 필수 강한 비교군. 공식 abstract와 저자 code README 확인. |
| L04 / pr-0055 | [VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation](https://proceedings.mlr.press/v270/liu25i.html), CoRL 2024 | acting/stabilizing 역할을 학습하는 양팔 정책. 역할 분리 자체의 신규성 주장을 제외. 공식 abstract. |
| L05 / pr-0746 | [π0: A Vision-Language-Action Flow Model for General Robot Control](https://www.roboticsproceedings.org/rss21/p010.html), RSS 2025 | flow 기반 generalist control의 대표 비교 기반. Native observation/action 계약을 검증해야 함. 공식 abstract. |
| L06 / pr-0061 | [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://proceedings.mlr.press/v305/black25a.html), CoRL 2025 | open-world generalization의 비교 기반. 명칭만으로 이 로컬 환경에서 실행 가능하다고 판단하지 않음. 공식 abstract. |
| L07 / pr-0142 | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://proceedings.mlr.press/v267/shi25d.html), ICML 2025 | 복잡한 지시와 수행 중 feedback을 high-level VLM·low-level VLA로 연결. D3의 일반 feedback/계층 제어는 이미 존재. 공식 abstract. |
| L08 / pr-0880 | [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](https://www.roboticsproceedings.org/rss21/p011.html), RSS 2025 | Ego3D position encoding과 adaptive spatial action grids. 단순 3D encoding 추가의 직접 선행. 공식 abstract. |
| L09 / pr-0058 | [3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation](https://proceedings.mlr.press/v305/li25g.html), CoRL 2025 | 2D–3D alignment와 affordance keypoint의 sequential spatial constraints. D2의 새 제약 representation은 이것과 비교해야 함. 공식 abstract. |
| L10 / pr-0975 | [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.pdf), CVPR 2025 | base–arm reachability·smoothness·collision을 다루는 trajectory optimization. **공식 CVF PDF의 검색 색인 발췌만 확인**; 직접 open은 403. 전체 실험/코드는 추가 확인 필요. |
| L11 / pr-0060 | [MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation](https://proceedings.mlr.press/v305/wu25c.html), CoRL 2025 | VLM interaction keypoint와 물리 제약으로 조작할 docking point 생성. D2에서 docking을 새 기여로 주장하지 않음. 공식 abstract; PDF direct fetch는 content-type 오류. |
| L12 / pr-0884 | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://www.roboticsproceedings.org/rss21/p018.html), RSS 2025 | VLA navigation과 locomotion skill을 계층적으로 연결. D2의 navigation 기반 비교. 공식 abstract. |
| L13 / pr-0691 | [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html), CVPR 2026 | force-aware concept와 실시간 힘 신호를 hybrid force-position control로 연결. 단순 force 융합은 제외. 공식 abstract와 supplemental의 indexed hardware discussion 발췌. |
| L14 / pr-0690 | [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html), CVPR 2026 | adaptive tactile injection과 slow visual / fast tactile stream. D1이 modality gate·반응 속도 개선만으로 끝나면 가까운 선행과 충돌. 공식 abstract와 code README. |
| L15 / pr-0272 | [PointVLA: Injecting the 3D World Into Vision-Language-Action Models](https://ieeexplore.ieee.org/document/11346992/), RA-L 2026 | frozen action expert에 3D feature를 주입. Publisher indexed abstract와 volume 11(3), DOI **10.1109/LRA.2026.3653303** 확인. Direct open은 browser challenge; full text 재확인 아님. |
| L16 / pr-0168 | [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](https://proceedings.mlr.press/v306/fan26b.html), ICML 2026 | simulator·sensor·model-estimated point cloud를 함께 사용하여 domain/depth-scale 차이를 다룸. 단순 noisy depth/다양한 point cloud 훈련은 신규 주장에서 제외. 공식 abstract. |
| L17 / pr-0151 | [TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments](https://proceedings.mlr.press/v306/huang26cd.html), ICML 2026 | delayed semantic state와 latency metadata, delay-consistent training. 일반 asynchronous VLA 제안은 제외. 공식 abstract. |
| L18 / pr-0976 | [Semantic Contact Fields for Category-Level Generalizable Tool Manipulation](https://www.roboticsproceedings.org/rss22/p004.html), RSS 2026 | visual semantics와 dense contact를 3D field로 표현하고 diffusion policy에 사용. VLA의 일반적인 한계를 동기로 쓰지만 이 방법 자체를 end-to-end VLA로 동일시하지 않음. 공식 abstract. |
| L19 / pr-0977 | [DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation](https://www.roboticsproceedings.org/rss22/p147.html), RSS 2026 | instruction으로 task policy parameter를 생성하여 scene shortcut을 다룸. 언어가 무시되는 현상을 새로 발견했다고 주장하지 않음. 공식 abstract의 구조적 주장을 본문 증명 검증으로 승격하지 않음. |
| L20 / pr-0978 | [Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models](https://www.roboticsproceedings.org/rss22/p141.html), RSS 2026 | 언어 대신 contact points를 쓰는 utility policy. VLA를 반드시 비교해야 할 task에서 contact-conditioned 작은 정책도 강한 대안이 될 수 있음. 공식 abstract; release 약속을 실제 release 확인으로 간주하지 않음. |

## 3. 최신 직접 충돌 10편 — 공식 acceptance와 분리

| ID / registry | 정확한 논문·source / 상태 | 확인 범위와 판단에 미친 영향 |
|---|---|---|
| X01 / pr-0979 | [How Should Vision-Language-Action Models Use Proprioceptive State?](https://arxiv.org/abs/2608.03052), arXiv 2026 | HTML §4–5.1과 결과 논의: 입력 위치·history 비교가 이미 존재. 16D state에 world-frame base localization이 포함되므로 pure proprioception 효과라고 단정할 수 없음. |
| X02 / pr-0980 | [Self-Adaptive VLA for Robust Robot Deployment](https://arxiv.org/abs/2609.30092), arXiv 2026 | HTML Introduction, §III-A, IV와 project. Actuation bias/encoder offset을 나누고 같은 failure의 원인 ambiguity도 논의. 고정 offset을 이전 rollout으로 보상. D1을 episode 중 unknown source 변화로 좁힘. |
| X03 / pr-0981 | [ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance](https://arxiv.org/abs/2601.16667), arXiv 2026 | 최초 v1 확인 후 v3·최신 project 대조. VLM task-stage cue로 modality imbalance와 drop/swap/relayout에 대응. 최신 project의 attention rebalance·Flash까지 고려하며 vision 강화만으로 D1의 방법을 구성하지 않음. |
| X04 / pr-0982 | [CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts](https://arxiv.org/abs/2607.03693), arXiv 2026; CoRL은 저자 표기 | **v2 §4.3 Table6 재확인:** availability mask 외에 mid-rollout outage·noise·delay·misalignment를 평가한다. Missingness만 다뤘다는 해석은 철회. |
| X05 / pr-0983 | [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](https://arxiv.org/abs/2609.37150), arXiv 2026 | Primary abstract. Point cloud에서 training view를 복원하여 cross-view coordination 대응. X04와 **다른 논문**이며 acronym으로 dedup하지 않음. |
| X06 / pr-0984 | [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843), arXiv 2026 | HTML §2–4와 Appendix G 관련 설명. 한 embodiment·episode당 한 fault axis. Policy input과 controller state corruption을 분리한다. D1에서 corruption sensitivity 자체를 신규 발견으로 주장하지 않음. |
| X07 / pr-0985 | [SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models](https://arxiv.org/abs/2506.03574), arXiv 2025; venue 미확정 | HTML §3.1–3.4, §4.1. Contact state와 forward/rollback/advance mode를 학습. Rollback은 이전 action 역방향을 사용. D3 일반 formulation을 제외한 결정적 근거. |
| X08 / pr-0986 | [VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting](https://arxiv.org/abs/2510.21817), arXiv 2025; ICLR acceptance 미확인 | HTML related work/§3와 공식 repo README. Active/Standby 및 명령 token을 통한 interruption/concurrency. OpenReview direct access는 challenge였으므로 submission PDF만으로 accept 처리하지 않음. |
| X09 / pr-0987 | [WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html), **ICLR 2026 공식 확인** | 후속 admission에서 proceedings 확인. arXiv 2025와 중복 등록하지 않는다. Repo의 codebase 공개 일정 미정과 native 실행 미검증은 유지. |
| X10 / pr-0988 | [DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts](https://jjjenghi.github.io/dialogvla/), **저자 IROS 2026 표기 / 공식 status 미확인 / Unverified로 등록** | 저자 project만 확인. Per-arm subtask와 arm/skill expert를 다루며 code는 SOON. 양팔 role assignment가 미개척이라는 주장 제외. 본문 추가 확인 필요. |

## 4. 비교에서 얻은 핵심 해석

**D1의 전제는 “proprioception을 더 쓰면 좋다”가 아니다.** X01은 state/history의 이득을 보고하지만 world-frame localization과 interface 차이가 포함된다. X06은 시험한 설정에서 policy의 reported state noise가 거의 해롭지 않고, controller에 넣은 오류는 해롭다고 보고한다. 이는 동일한 실험의 상반된 결과가 아니다. 입력의 의미·실제 사용·controller에 미치는 영향이 다르므로 비교 조건을 맞춰야 한다. 이 분리가 D1의 첫 진단이다. [X01 §4.2–5.1](https://arxiv.org/html/2608.03052v1), [X06 §3, Appendix G](https://arxiv.org/html/2610.18843v1)

X02는 encoder offset을 시각으로만 식별해야 하는 조건까지 이미 다룬다. 따라서 “vision/proprioception으로 고장의 원인을 찾는다”도 넓게는 선행 기여다. D1은 고정 offset 적응을 baseline으로 두고 **알려주지 않은 관측 오류·실제 상태 변화·원인 전환을 같은 정보로 구별할 필요가 있는지** 확인한다. 이 조건에서의 기여 여부는 아직 실험적으로 모른다. [X02 §III-A](https://arxiv.org/html/2609.30092v1)

D2의 물체 운반도 새로운 motion-planning problem은 아니다. L03/L09/L10/L11의 제약·spatial representation·reachability를 비교하고, geometry를 알려주면 풀리는 문제와 geometry/constraint를 추정해야 하는 문제를 구분해야 한다. D3는 X07의 binary contact와 역방향 trajectory를 넘어서는 task가 있어야 남는다. **논문의 제한 조건을 확장한다는 것과 가치 있는 연구 gap을 검증했다는 것은 다르다.**

## 5. 공개 artifact 확인 경계

| Source | 실제 확인한 공개 범위 | 이번에 하지 않은 것 |
|---|---|---|
| [OpenVLA 공식 repo](https://github.com/openvla/openvla), [HPT project](https://liruiw.github.io/hpt/) | Publication이 가리키는 공개 구현·자료 경로 | 현재 task/robot에서의 native 실행·성능 검증 |
| [ReKep 공식 repo](https://github.com/huangwl18/ReKep) | README는 simulation demo가 실제 perception pipeline을 포함하지 않고 simulator 정보를 사용한다고 명시 | Real-world perception을 확보한 것으로 간주하지 않음; 설치·실행 안 함 |
| [AT-VLA 공식 repo](https://github.com/clorislili/AT-VLA) | README: GO-1 계열 기반. 코드의 pi0 이름은 legacy naming이며 PI π0와 동일시하면 안 됨 | Dependency·weight·sensor interface 재현 검증 |
| [Self-Adaptive VLA project](https://icefoxzhx.github.io/self-adaptive-vla/) | Paper/video/project 확인. 확인한 페이지에서 공개 code 링크를 식별하지 못함 | 전 세계에 code가 없다고 단정하지 않음 |
| [VITA 공식 repo](https://github.com/Tencent/VITA) | VITA-E README·훈련/실행 안내 확인 | 배포 모델·task 성능 재현 |
| [WholeBodyVLA 공식 repo](https://github.com/OpenDriveLab/WholebodyVLA) | README는 현재 resource/reference 중심이며 codebase 공개의 구체적 일정이 없다고 명시 | 실행 가능한 전체 system이라고 간주하지 않음 |
| X01/X03/X04/X06 | 논문 본문의 입력·평가 설정을 확인 | 사용할 수 있는 weights/data와 pinned code의 존재·호환성은 후속 gate |

## 6. 남은 문헌 검토

우선순위는 D1의 classical fault isolation / robust visual–kinematic state estimation과 직접 충돌 paper의 공개 interface다. Hidden corruption과 fault transition을 이미 다룬 더 가까운 방법이 발견되면 D1을 수정하거나 중단한다. D2의 attached-object transport planning과 D3의 비가역 task replanning은 후보를 실제 선택할 때 본문을 확대 확인한다. 이 문서의 source 목록을 사용자 정독 완료나 READING-SUPPORTED 연구 가설로 자동 승격하지 않는다.
