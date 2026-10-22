# D1 closest-work / source boundary

- 최신 후속: [N1–N4 재심사](./NONEXPERIMENTAL_REVIEW.md). GAP intervention·ablation 표, G-PSMR 독립 평가·손실 pair·reference 민감도, ReViP v3 ablation과 최신 project의 경계를 추가 확인했다. 현재 method 투자 NO-GO·진단 HOLD이며 아래 문헌 기록은 보존한다.
- 2026-10-21 확인; 2026-10-22 G-PSMR 지정 절·baseline 자산 보강. 논문 claim과 아래의 D1 해석은 구분한다.
- Registry admission은 [16편 입력](../../sources/frontier_admissions_2026-10-21.json), 개별 note는 `ABSTRACT_CHECKED`다. 여기서는 직접 경쟁 문헌의 지정한 본문 절·공개 interface까지 추가 확인했다. 논문 전체나 모든 code를 정독·재현했다는 뜻은 아니다.
- 10-22 후속 [방법 감사](./BASELINE_METHOD_AUDIT.md): G-PSMR gate 시점·결합 순서는 확인했다. GAP의 공식 ICLR 수식과 고정 public commit은 rule 차이·entrypoint 문법 오류가 있다. ReViP 최신 project와 v3의 버전 경계는 유지한다. [분석·기각 계약](./CLAIM_EVIDENCE_CONTRACT.md)에 D1의 함의를 반영했다.
- D1-L3 [task·native value-path 감사](./TASK_OBSERVABILITY_AUDIT.md): openpi의 packet-level state 존재와 실제 사용을 구분했다. 지정 `pi05_libero`는 state 값 경로가 꺼져 있어 비교에서 제외하고 OFT Goal variant를 후속 후보로 정했다. 이로써 과거 10-21 source audit를 정책 사용의 증거로 확대하지 않는다.

## 직접 비교

| 논문 / anchor | 조건·입력·action / 학습 신호 | 실제 증거와 가정 | D1과 겹침 / 남은 차이 |
|---|---|---|---|
| pr-0979 [State interface study v1 §4.2–5.1](https://arxiv.org/html/2608.03052v1) | π0.5 계열, state interface/history 통제, action chunk | State 16D에 world-frame base pose 포함; pure proprio 효과로 해석 불가 | History·injection site 실험은 선행. Hidden error와 실제 변화의 구별은 별도 검사 |
| pr-0980 [Self-Adaptive v1 §III-A, IV, V](https://arxiv.org/html/2609.30092v1) | 영상·state·이전 action rollout을 context로 사용; expert action pre-compensation | Offset을 episode에서 뽑아 trial 간 고정; absolute joint command, ideal tracking 가정. Encoder offset은 실제 motion과 report를 함께 바꿈 | Hardware 원인 ambiguity와 adaptation 이미 존재. 알려주지 않은 오류 전환·실제 환경 변화에 대한 적용 범위는 확인 필요 |
| pr-0981 [ReViP v3 §3–5, App.B](https://arxiv.org/html/2601.16667v3), [최신 project](https://isee-laboratory.github.io/ReViP/) | Task-stage visual cue로 action 조건 조정; false-completion perturbation | Drop/swap/relayout. Project는 attention rebalance·Flash까지 설명하므로 구버전 FiLM만 baseline으로 삼으면 부족 | Visual progress를 되살리는 기여는 선행. Vision 오류까지 동시에 허용하면 cue의 신뢰 가정 재검사 필요 |
| pr-0982 [Conditional Routing CoRE v2 §3.1, §4.3 Table6](https://arxiv.org/html/2607.03693v2) | RGB/language/state, optional depth; availability mask와 task router | **Mid-rollout outage, intermittent loss, noise, delay, misalignment도 평가**. Missingness에는 indicator 사용; noise 등에는 indicator=1 | “Present-but-corrupt는 전혀 미평가”라는 최초 해석은 철회. 다종 원인 구별이 행동상 필요한지는 해당 표로 입증되지 않음 |
| pr-0983 [Camera CoRe v1 §4.1–4.3, §5](https://arxiv.org/html/2609.37150v1) | RGB-D → target-view reprojection → R2C → VLA; async alignment | **Source/target intrinsic과 알려진 rigid transform** 사용; wrist-camera 유지 | Camera restoration 자체는 선행. Transform 미지 setting은 별도 estimator가 필요하며 그 차이만으로 novelty를 주장하지 않음 |
| pr-0984 [LIBERO-RIG v1 §2–4, App.G](https://arxiv.org/html/2610.18843v1) | Native VLA, fault metadata 미제공; 같은 task에 rig 변형 | Policy report noise와 controller에 들어가는 noise를 구분; 단일 embodiment·한 fault axis | Hardware-shift 취약성 발견은 이미 존재. 동적·복합으로 확장하는 것만으로 충분한 기여 아님 |
| pr-0989 [GAP §3–5.4, Alg.1](https://arxiv.org/html/2602.12032v1), [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) | Proprio history로 motion-transition 추정, training gradient 조정; vision/state → action | Sim/real, single/dual arm, Octo fine-tuning 비교. Cross-embodiment training은 limitation | “State 때문에 vision을 덜 쓴다”는 발견과 temporal rebalance는 선행. Corruption-cause inference와 동일하지 않음 |
| pr-0990 [G-PSMR / Entropy 2026](https://www.mdpi.com/1099-4300/28/9/975) | Stream별 gate와 visual/state restoration, frozen OpenVLA-OFT | 10-22에 publisher 색인의 §3.1–3.5·4.1·4.5 추가 확인. 세 variant·calibration·query 비용은 [baseline 계약](./BASELINE_DOSSIER.md)에 기록 | **Stream-local diagnosis와 targeted correction도 선행**. Top-tier로 집계하지 않음. 실제 초기 자세 변화도 다루므로 보정의 유해성을 일괄 가정하지 않음; code·정확한 재현 조건 미완료 |

처음 제안한 broad D1과 가장 직접적인 collision은 Self-Adaptive, GAP, G-PSMR이다. CoRE-v2의 sensor-degradation 평가와 ReViP 최신 project 때문에 “센서 고장/실제 변화 모두 시험했다” 정도의 추가 실험으로는 강한 차별화가 어렵다.

## Classical / 인접 분야 대조 — 이번 신규 registry 16편과 별도 참고

| Source와 확인 수준 | 이미 알려진 메커니즘 | D1에 반영 |
|---|---|---|
| [Ma·Yang, Simultaneous fault diagnosis, Information Sciences 2016, DOI 10.1016/j.ins.2016.05.016](https://www.sciencedirect.com/science/article/pii/S0020025516303401), publisher abstract | Nonlinear adaptive observer로 sensor/actuator fault를 동시에 추정·분리 | 고장 분류를 새 formulation으로 주장하지 않음. 모델 가정과 얻는 sensor를 맞춰야 함 |
| [Incremona·Ferrara, vision-servo fault diagnosis](https://re.public.polimi.it/retrieve/e0c31c12-efcd-4599-e053-1705fe0aef77/11311-1102054_Incremona.pdf), 저자 기관 원문 abstract·Introduction | Vision·inverse kinematics와 observer로 sensor/actuator 고장 분리 및 feedback 대체 | Visual–kinematic consistency는 기존 강한 baseline. Camera도 틀릴 때는 별도 관측 가능성 필요 |
| [Baioumy et al., Unbiased Active Inference FTC](https://www.robots.ox.ac.uk/~nickh/papers/baioumy2021ecc.pdf), 저자 공개 원문의 abstract 확인 | Sensory fault에 대한 state-estimation/control 접근 | Precision/reliability 조절을 새 개념으로 주장하지 않음. 본문 전체 수동 검토는 남음 |
| [Han et al., Counterfactual FDI v1 §II–III](https://arxiv.org/html/2509.18460v1) | Reliability test·counterfactual hypothesis·information-based active control; 한 시점 한 fault 가정 | Active probing 역시 이미 존재. Source-specific dynamics/observation 모델과 비용이 필요 |
| [ProTracer v1 §III](https://arxiv.org/html/2609.21369v1) | 전체 episode의 proprioception으로 keyframe 선택, VLM post-hoc failure 설명 | 미래 관측을 쓰는 retrospective diagnosis는 online D1 baseline과 정보가 다르다. Prefix-only 대조 필수 |

Classical paper의 특수 observer를 그대로 구현해야 한다는 뜻은 아니다. 그보다 약한 residual baseline도 이기지 못하면 learned module로 갈 이유가 없다. 위 원문 일부만 확인한 항목, G-PSMR의 code·좌표/calibration 구현, GAP의 공개 rule 차이 해소, ReViP 최신 manuscript는 본격 구현 전 남은 literature gate다. 따라서 문헌 검색이 완전히 포화됐다고 선언하지 않는다.

## 공개 interface audit

2026-10-22 추가 확보: [baseline dossier](./BASELINE_DOSSIER.md)와 [4개 repository / 9개 source·metadata 감사](./baseline_sources_2026-10-22.json). 이번에는 공개 자료를 읽기만 했으며 Docker·정책 실행은 없다. 아래는 10-21의 별도 실행 이력이다.

Docker에서 두 official repository의 commit을 고정하여 **19개 source/config/README 파일**의 hash와 필요한 line cue를 확인했다. [원자료](./artifact_audit.json).

| Repository | 실제 확인 | 경계 |
|---|---|---|
| [GAP @ 2f605436](https://github.com/GeWu-Lab/GAP/tree/2f605436c68eedf328c05520d52877604af730d3) | 27개 blob 목록; 13개 파일. `gap/dataset.py`의 eef position/quaternion/gripper state와 CUDA phase predictor, `gap/policies/visual_encoder.py`의 proprio encoder, config의 `device: cuda` | 공개 트리에서 Octo-specific recipe/checkpoint를 식별하지 못했다. 논문에 Octo 실험이 없다는 뜻은 아님. Code 실행·학습 미수행 |
| [openpi @ 215abfb2](https://github.com/Physical-Intelligence/openpi/tree/215abfb217dbac7d5f1273282331b9b1866c0479) | 6개 파일. LIBERO native state 입력·policy adapter, pi05_libero config 안내, GPU requirements와 CUDA dependency | Native interface 존재와 정책이 그 입력을 행동에 사용하는 것은 다름. Checkpoint 다운로드·추론·성공률 측정 미수행 |
| [Self-Adaptive project](https://icefoxzhx.github.io/self-adaptive-vla/), [ReViP project](https://isee-laboratory.github.io/ReViP/) | 전자는 확인 페이지에서 code link 미식별; 후자는 Code coming soon | 실제 runnable baseline으로 확보됐다고 하지 않음 |
| State study / CoRE / camera CoRe / LIBERO-RIG | Primary paper의 지정 절 확인 | 이번 확인 source에서 paper-specific pinned code·weights·trial ledger의 완전한 조합을 확보하지 못함 |

## Admission status 수정

- 기존 외부 14편 + GAP(ICLR 2026) + G-PSMR(Entropy 2026) = 16편, stable ID `pr-0975`–`pr-0990`.
- [WholeBodyVLA 공식 ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) 확인: arXiv 2025 별도 entry를 만들지 않고 ICLR version 하나로 등록.
- ReViP의 이전 **Reducing** title은 alias로 보존. SCFields는 RSS 공식 title을 사용하고 arXiv identifier로 title variant를 연결.
- CoRE-v2 저자의 CoRL 2026 표기는 공식 acceptance 근거를 찾기 전까지 `arXiv / preprint` 유지.
- DialogVLA는 저자 project의 title/author/method cue를 확인했지만 IROS 공식 발표는 미확인. **`Unverified / publication.status=unverified`**로 등록하며 arXiv entry를 만들어내지 않음.
- CVPR 1편·RSS 3편·ICLR 2편은 공식 proceedings로 확인. Entropy 1편은 publisher 확인. arXiv 8편과 status 미확인 1편을 peer-reviewed top-tier로 합산하지 않는다.
