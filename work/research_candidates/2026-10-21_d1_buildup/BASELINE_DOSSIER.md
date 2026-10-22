# D1 baseline 논문·공개 자산·비교 계약

- 확인일: **2026-10-22 KST**. `thesis`는 baseline으로 활용할 논문·방법으로 해석했다.
- 상태: **비실험 buildup 진행 가능 / native VLA 효과 검증 HOLD / 신규 방법 채택 REVISE**.
- 범위: 공식 publication, 지정한 본문 절, 저자 project, 공개 source와 checkpoint 목록을 확인했다. 학습·추론·simulator 실행은 하지 않았다.
- 소스 식별 기록: [baseline_sources_2026-10-22.json](./baseline_sources_2026-10-22.json). 소스 commit과 model repository revision은 재현성의 일부이며 실행 검증이나 weight payload hash를 대신하지 않는다.
- 후속 정밀 검토: [method/release audit](./BASELINE_METHOD_AUDIT.md), [추가 source 기록](./baseline_method_sources_2026-10-22.json), [주장·증거·기각 계약](./CLAIM_EVIDENCE_CONTRACT.md). 같은 날의 최초 자산 확인과 후속 검토를 구분한다.
- **D1-L3 수정:** [task·value-path 감사](./TASK_OBSERVABILITY_AUDIT.md)에서 `pi05_libero`가 state 값을 action에 사용하지 않는 설정임을 확인했다. State 보정 primary를 OFT의 Goal variant 후보로 변경했다. 초기 선정 이력과 현재 결정을 구분한다.
- 전체 우선순위·tier는 [READING_PLAN.md](../../../research/READING_PLAN.md)가 canonical이다. 이 문서는 D1의 **비교 역할**을 정하며 별도 읽기 순위를 만들지 않는다.

## 1. 지금 확보한 것과 현재 판단

실험이 막혔다고 buildup 전체가 막힌 것은 아니다. 문헌 기반으로 baseline의 목적, 관측·행동 조건, 필요한 학습, 공개 자산, 비교의 허점을 고정할 수 있다. 다만 장비가 갖춰져도 D1의 신규성이 자동으로 성립하지는 않는다. 기존 방법을 넘어서는 현상의 존재는 아직 미확인이다.

**현재 기본 정책 후보는 proprio-enabled OpenVLA-OFT LIBERO-Goal, 학습 기반 직접 비교는 GAP, frozen-policy 복원 비교는 G-PSMR으로 정한다.** 초기 선정한 π0.5 LIBERO variant는 state-value 보정 비교에서 제외하고 별도 vision-language reference로만 남긴다. Octo는 GAP 원논문과의 연결을 확인하는 보조 backbone이고, ReViP는 task-progress 보정에 대한 필수 문헌 비교다. 새 모듈을 설계하기 전에 이 비교군과 단순 대조군이 설명하는 범위를 배제한다.

여기서 “확보”한 것은 논문 식별자·원문 링크·선정 근거·공개 구현 위치·interface 명세다. 실제 실행 가능한 설치본을 확보했다는 뜻은 아니다. 모든 핵심 논문이 기존 registry에 있어 중복 등록하지 않았다. PDF·weight·dataset·package를 내려받지 않았다.

## 2. 핵심 논문 집합

| 논문 / registry | 검증한 발표 상태 | D1에서 맡길 역할 | 확보 수준과 제한 |
|---|---|---|---|
| π0.5: a Vision-Language-Action Model with Open-World Generalization · pr-0061 | [CoRL 2025 / PMLR](https://proceedings.mlr.press/v305/black25a.html) | 별도 vision-language reference. 해당 LIBERO variant의 state 보정 비교 제외 | Packet state는 있으나 지정 config의 value path가 꺼짐. 모든 π0.5의 특성으로 일반화하지 않음 |
| Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · pr-0750 | [RSS 2025](https://www.roboticsproceedings.org/rss21/p017.html) | 현재 primary 후보. State 입력과 frozen-policy 복원 비교 기반 | Official eval·proprio token→action 경로·Goal asset revision 확인. State utility·실행 미검증 |
| When would Vision-Proprioception Policies Fail in Robotic Manipulation? · pr-0989 | [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) | GAP. 원인 분류 없이 학습 불균형만 교정해도 충분한지 비교 | 공식판 수식/Algorithm 1과 공개 rule 차이, entrypoint 정적 문법 오류 확인. [후속 감사](./BASELINE_METHOD_AUDIT.md). Octo recipe/weights 미확보 |
| Octo: An Open-Source Generalist Robot Policy · pr-0052 | [RSS 2024](https://www.roboticsproceedings.org/rss20/p090.html) | GAP의 VLA 실험을 이해할 보조 backbone, 새로운 state interface의 대조 | [Official repo](https://github.com/octo-models/octo)와 generic pretrained checkpoint 안내 확인. D1 task-finetuned GAP checkpoint를 의미하지 않음 |
| Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies · pr-0990 | [Entropy 2026](https://www.mdpi.com/1099-4300/28/9/975) | G-PSMR. 단순한 stream별 restoration으로 충분한지 직접 비교 | Publisher 색인의 §3.1–3.5·4.1·4.5 확인. Official implementation 미식별; paper-backed 재구현 후보. Top-tier 선정 논문으로 집계하지 않음 |
| ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance · pr-0981 | [arXiv v3](https://arxiv.org/html/2601.16667v3); accepted venue 미확인 | 물리적 task 변화 뒤 visual progress를 회복하는 강한 대안 | [현재 project](https://isee-laboratory.github.io/ReViP/)는 추가 attention 모듈·Flash를 설명하나 Code coming soon. 구버전 재현을 최신 ReViP라고 부르지 않음 |

Top-tier 기반은 앞의 네 편이다. 직접 충돌하는 journal/preprint도 novelty 검토에는 포함한다. “논문이 좋은 baseline”과 “이 환경에서 바로 재현 가능”을 별개로 판정한다.

기존 note: [π0.5](../../../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md), [OFT](../../../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md), [GAP](../../../2026/ICLR/2026_ICLR_When-would-Vision-Proprioception-Policies-Fail-in-Robotic/01_overview.md), [Octo](../../../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md), [G-PSMR](../../../2026/Entropy/2026_Entropy_Restoring-the-Right-Stream-Training-Free-OOD-Robustness-fo/01_overview.md), [ReViP](../../../2026/arXiv/2026_arXiv_ReViP-Mitigating-False-Completion-in-Vision-Language-Actio/01_overview.md).

## 3. 기본 정책의 구체적인 자산

### π0.5 / openpi

- Official source commit: `215abfb217dbac7d5f1273282331b9b1866c0479`.
- Checkpoint locator: `gs://openpi-assets/checkpoints/pi05_libero`. Base pretrained `pi05_base`와 task expert를 혼동하지 않는다.
- [README checkpoint 표](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/README.md)와 이전 [native LIBERO adapter audit](./artifact_audit.json)을 연결했다. 이번에는 README와 commit 동일성을 재확인했다.
- Native packet에는 RGB·language·state가 있으나 **`pi05_libero`는 state 값의 token/continuous 경로와 output delta 변환이 꺼져 있다.** [전체 연결 확인](./TASK_OBSERVABILITY_AUDIT.md). State-only correction의 primary에서 제외한다. 논문의 모든 π0.5 variant에 같은 결론을 적용하지 않는다.
- Weight payload·normalizer hash, 최종 환경·task manifest, native clean competence는 남아 있다. 공식 NVIDIA 실행 요구와 현재 환경의 차이는 [기존 결과](./RESULTS.md)에 기록돼 있다.

### OpenVLA-OFT / state를 쓰는 LIBERO variant

| 항목 | 이번에 고정한 문헌·source 수준 값 |
|---|---|
| Code commit | `e4287e94541f459edc4feabc4e181f537cd569a8` |
| 대표 model ID | `moojink/openvla-7b-oft-finetuned-libero-spatial` |
| Model repository revision | `6d0231af0e48c5985f1ff86908f4674b84bc049b` — 파일 목록만 확인 |
| Listed sidecars | `action_head--150000_checkpoint.pt`, `proprio_projector--150000_checkpoint.pt`, `dataset_statistics.json`, config와 model shards |
| Native input | Third-person RGB + wrist RGB + language + state 8D: eef position 3, quaternion→axis-angle 3, gripper qpos 2 |
| Default LIBERO eval | `use_proprio=True`, `num_images_in_input=2`, `use_l1_regression=True`, `use_film=False`, open-loop 8 actions |
| Model output | Action 7D × chunk 8; environment 전 gripper mapping. Physical units/frame/controller scale는 환경 config와 함께 추가 고정해야 함 |
| Normalization | LIBERO constants는 `BOUNDS_Q99`; state normalization은 q01/q99 기반 scaling 후 clipping. `libero_spatial_no_noops`와 checkpoint statistics 연결 필요 |
| 재현 조건 | 공식 LIBERO 안내는 Python 3.10.14, PyTorch 2.2.0, custom Transformers 4.40.1, NVIDIA A100 결과를 명시. 이번 설치·실행은 없음 |

근거: [공식 LIBERO recipe](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/LIBERO.md), [eval input/queue](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/libero/run_libero_eval.py#L245), [normalizer](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/experiments/robot/openvla_utils.py#L649), [constants](https://github.com/moojink/openvla-oft/blob/e4287e94541f459edc4feabc4e181f537cd569a8/prismatic/vla/constants.py#L26), [checkpoint listing](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial/tree/6d0231af0e48c5985f1ff86908f4674b84bc049b).

**해석:** OFT라는 이름만으로 state 입력 여부를 판단하지 않는다. 다른 공개 RL/world-model용 variant에는 입력이 다를 수 있다. Masking·offset·restoration은 raw state와 normalized state 중 어디에 적용하는지 명시해야 한다. Clipping이 fault 크기를 지우면 “정책이 state를 안 쓴다”는 잘못된 결론이 생길 수 있다.

위 표의 Spatial asset은 최초 확보 이력이다. **D1-L3 후 primary 후보를 OFT Goal variant로 변경했다.** Goal model ID는 `moojink/openvla-7b-oft-finetuned-libero-goal`, revision은 `c2d0f9fbbd82674683b397ff923168a12f6a307b`이며 50,000-step sidecar 목록을 확인했다. [선정 근거·정확한 task/source](./TASK_OBSERVABILITY_AUDIT.md), [후보 명세](./TASK_CANDIDATES.json). Weight hash·native qualification은 미확보다. 서로 다른 backbone의 성공률을 state 유무의 ablation으로 쓰지 않는다.

**E1 후속 자산 검토:** [Docker preflight](../../experiments/vla_d1_e1_preflight/RESULTS.md)에서 Goal normalizer의 실제 작은 JSON/hash와 action 7D·proprio 8D를 확인했다. Base config에는 Goal normalization key가 없어 별도 statistics를 적용하는 native 경로가 필요하다. Model/sidecar 다운로드의 revision 전달 누락과 HF/repo modeling 사본의 diffusion helper 차이도 기록했다. OFT에는 CPU fallback이 있고 명시적 FlashAttention 인수는 주석이므로 A100 보고 환경을 코드상 절대 GPU 요건과 혼동하지 않는다. 현재 자원은 native qualification을 통과하지 못했으며 CPU/정책 실행 결과는 없다.

## 4. 직접 방법을 baseline으로 옮길 때의 계약

### GAP: training-time 대안

**Paper-supported:** Proprio motion을 CPD로 구간화하고 temporal network로 transition 정도를 추정하여 proprioception branch의 BC gradient를 조절한다. Hidden fault label 분류기가 아니다. 원문 §5.4는 Octo fine-tuning을 평가한다. [ICLR 공식판 §4, Algorithm 1, §5.4](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b3bb2c95195130977a51b3bb251c40a-Paper-Conference.pdf).

**D1 계약:** 같은 demonstrations·optimizer·update 수로 일반 fine-tuning, constant gradient scaling, GAP-style phase scaling을 비교한다. Phase 추정용 preprocessing·학습 비용도 포함한다. 추론 중 미래 expert trajectory나 정답 fault onset을 주입하지 않는다. 공개 [GAP commit](https://github.com/GeWu-Lab/GAP/tree/2f605436c68eedf328c05520d52877604af730d3)은 확보했으나, OFT/π0.5에 옮긴 구현은 **GAP-style port**이며 논문 재현이라고 부르지 않는다. Branch가 분리되지 않는 architecture에서는 gradient 적용 위치부터 정해야 한다.

**후속 감사 반영:** 고정 commit의 training 파일은 정적 Python 파싱에 실패했고 공식 수식·batch aggregation과 공개 코드가 다르다. [차이와 처리 규칙](./BASELINE_METHOD_AUDIT.md)을 해소하기 전 즉시 실행 가능한 baseline으로 표시하지 않는다. 논문 결과 자체를 반증한 것은 아니다.

### G-PSMR: frozen-policy 복원 대안

**Paper-supported:** M1은 third-person 영상의 augmentation disagreement로 gate를 열고 action consensus를 취한다. 닫힌 gate도 2회, 열린 경우 8회 policy query를 쓴다. M2는 초기 자세 `R0`, 현재 자세 `Rt`, clean reference `Rc`로 `R̃t = Rc R0⁻¹ Rt`를 사용한다. Suite별 clean 25개 상태로 reference를 만들며 policy state만 바꾼다. M3는 둘의 결합이다. [Publisher §3.4–3.5·4.1·4.5](https://www.mdpi.com/1099-4300/28/9/975). 직접 HTML 접근은 제한되어 publisher 검색 색인의 지정 절을 확인했다.

**D1 계약:** M1/M2/M3를 분리한다. Clean calibration을 모든 비교군에 동일 제공하고 test 성공 여부로 reference를 고르지 않는다. M2의 1-query 조건과 M1/M3의 다중 query를 별도 예산으로 비교한다. [후속 감사](./BASELINE_METHOD_AUDIT.md)에서 초기 1회 state gate와 state-first 결합 순서를 확인했다. 코드·실제 calibration manifest·좌표 convention과 수식의 구현 일치는 여전히 미확인이다.

**중요한 해석 수정:** 원논문은 실제 초기 자세 변화도 다룬다. “실제 변화는 항상 보정하면 안 된다”를 가정하지 않는다. 보정이 task에 필요한 정보를 지우는지는 별도 결과로 판단한다. Mid-episode fault에서 정답 onset으로 reference를 재설정하면 정보 누출이다. 기존 operator를 유지하거나 prefix-only reset 규칙을 추가한 변형임을 밝혀야 한다.

### ReViP와 Self-Adaptive: 조건부 비교

ReViP 최신 project는 visual stage grounding, action attention rebalance, in-policy cue distillation인 Flash를 설명한다. 외부 observer의 입력·latency·학습 신호가 추가되면 동일 예산으로 기록한다. Project manuscript는 이번 도구의 문서 크기 제한으로 열지 못했고, 최신 code는 coming soon이다. **현재는 novelty 비교와 재구현 준비 대상이며 runnable baseline 확보 완료가 아니다.** [저자 project](https://isee-laboratory.github.io/ReViP/).

Self-Adaptive VLA(pr-0980)는 trial 간 고정 hardware offset과 이전 rollout context를 다루므로, D1의 episode 내 변화와 바로 같은 조건으로 취급하지 않는다. 이전 trial 접근·expert pre-compensation·adaptation 비용을 동일하게 허용할 때 비교한다. 현재 확보 범위는 [기존 본문 비교](./CLOSEST_WORK.md)의 §III-A·IV·V이며 native 구현은 미확보다.

## 5. 반드시 포함할 단순 대조군

아래는 연구자 설계다. 논문에 이미 같은 구현이 존재한다고 주장하지 않는다. 이들을 이기지 못하면 복잡한 cause-conditioned 학습의 이유가 약해진다.

| ID | 비교군 | 분리할 설명 | 정보·학습·비용 제약 |
|---|---|---|---|
| B0 | Native frozen policy | 원래 정책으로 충분 | 해당 checkpoint의 원래 전처리·action queue 유지 |
| B1a | State mask / fixed-current input 진단 | 입력 사용 여부·state shortcut | Inference intervention일 뿐 vision-only policy가 아님. Mask OOD 여부 기록 |
| B1b | Matched vision-only 및 modality-dropout training | State 없이도 충분, 단순 augmentation 효과 | 같은 robot data·update budget. 공개 다른 모델을 무조건 이 대조군으로 대체하지 않음 |
| B2 | Fixed history / repeated-current history | 과거 정보 이득인가, token 수·capacity 효과인가 | 같은 token 수·timestamps·train budget. Native가 history를 지원하지 않으면 새로운 matched port로 표기 |
| B3 | Residual/state estimator + conservative correction; causal 재보정·task별 reference 대조 | 단순 filtering/calibration 또는 평균 reference mismatch로 충분 | Vision-derived pose·kinematics·anchor를 실제 관측으로 얻어야 함. GT pose는 privileged. [추가 대조의 정보 제한](./CLAIM_EVIDENCE_CONTRACT.md) 준수 |
| B4 | GAP-style / constant gradient scaling / standard fine-tune | 원인 분류 없이 optimization으로 충분 | 위 GAP 계약. 기존 정책이 frozen인 비교와 training 비용 구별 |
| B5 | G-PSMR M1, M2, M3 | Stream restoration으로 충분 | 위 세 variant 및 clean calibration/query 비용 유지 |
| B6 | Matched corruption augmentation | 노출된 오류 분포를 학습한 효과 | Onset·크기·조합·task holdout; cause labels 없이 동일 training data |
| D0 | Fault-aware 또는 true-state diagnostic comparator | 개선 여지가 원천적으로 있는가 | Evaluator-private 정보 사용. 공정 배포 baseline이나 수학적 upper bound로 취급하지 않음 |

B3의 기반은 기존 registry [Kalman filtering, pr-0823](../../../1960/Journal-of-Basic-Enginee/1960_Journal-of-Basic-Enginee_A-New-Approach-to-Linear-Filtering-and-Prediction-Problems/01_overview.md)과 [classical FDI 비교](./CLOSEST_WORK.md)다. Kalman filter 자체를 sensor/actuator fault 원인 식별기로 부르지 않는다. 실제 pose observation model, bias state와 그 observability, process noise, contact에서의 model mismatch를 먼저 명시해야 한다. 알려진 물체 기준점을 추가하는 경우 다른 방법에도 동일 정보를 준다.

최초 비교 묶음은 B0·B1a·B3·B5·D0이다. Native qualification 이후 training이 필요해질 때 B1b·B2·B4·B6를 추가한다. 이는 **실행 순서의 설계**이며 어느 baseline도 이번에 구현·실행하지 않았다. 이 묶음만으로 최신 ReViP/Self-Adaptive보다 우월하다고 주장할 수 없다.

## 6. 문헌에서 고정할 수 있는 공정성 기준

1. **입력:** 같은 RGB views, language, native state, history prefix. Calibration·task identity·이전 trial을 쓰면 모든 comparable arm에 제공한다. Fault type·magnitude·onset·simulator true state는 D0 외에 금지한다.
2. **행동:** 같은 action representation, frame, gripper mapping, chunk 실행 길이와 decision timing. 더 자주 관측/재계획한 이득을 correction 효과로 해석하지 않는다.
3. **비용:** Policy forward 수와 end-to-end latency를 함께 센다. 동일 query 수와 동일 wall-clock 조건을 모두 만족하기 어렵다면 두 비교를 분리하고 예산 차이를 명시한다. 외부 VLM·vision estimator·phase training·calibration도 비용이다.
4. **데이터:** 같은 pretrained checkpoint에서 같은 demonstrations로 만든 variants를 먼저 비교한다. 다른 backbone의 원 논문 수치는 참고값이다. Task/초기 상태와 corruption family를 development·holdout으로 분리한다.
5. **진단:** Sensor report 오류, controller feedback 오류, 실제 물리 변화, 정상 변화와 ambiguous 조건을 구별한다. 원인을 맞혀도 필요한 action이 같으면 diagnosis의 task 이득으로 세지 않는다.
6. **평가:** Paired task success, recovered/lost pairs, clean 유지, harmful correction, contact/충돌, latency. Oracle도 실패하면 cause 학습 이전에 base competence·solvability를 재검토한다.

평가 기반은 기존 [LIBERO, pr-0042](../../../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md)이며 [LIBERO-RIG, pr-0984](../../../2026/arXiv/2026_arXiv_LIBERO-RIG-A-Hardware-Setup-Robustness-Benchmark-for-Visio/01_overview.md)는 hardware-shift 조건을 대조하는 문헌이다. Benchmark는 algorithm baseline이 아니다. G-PSMR의 LIBERO-Plus 조건을 다른 LIBERO variant로 바꾸면 원논문 재현과 D1 확장 평가를 분리한다.

## 7. 기존 8단계 buildup에서 이번에 진전한 부분

| 가이드 단계 | 이번 비실험 산출물 | 남은 경계 |
|---|---|---|
| 1 문제와 가치 | 실제 변화의 보정도 유익할 수 있음을 반영 | D1 현상의 빈도·중요도 미측정 |
| 2 필요한 문헌 | 6편 핵심 baseline, classical·history·adaptation 연결 | 모든 인접 문헌 검색 포화 주장 없음 |
| 3 가정·interface 비교 | Policy/state/normalization/decision budget 명세 | Native 성능과 input-use 미검증 |
| 4 경쟁 가설 | 단순 filtering·optimization·restoration·data 효과를 B0–B6에 연결 | 어떤 설명이 충분한지는 실험 필요 |
| 5 novelty 심사 | 원인 분류·복원 자체를 기여에서 제외 | 잔여 gap 확정 불가 |
| 6 주장–증거 | 비교군·정보 경계·비용·기각 조건 구체화 | Run manifest·최종 sample budget 미생성 |
| 7 최소 검사 | 공개 자료와 자산 목록의 정적 감사만 추가 | 새로운 정책/물리 실험 없음 |
| 8 반박·결정 | REVISE / empirical HOLD 유지 | 실제 외부 연구자 피드백 미완료 |

**완료:** 기본 baseline 논문 선정, 공식 publication 확인, 공개 자산 식별, native interface 비교, baseline fairness·재구현 경계 작성. Code/source는 4개 repo의 9개 파일을 메모리에서 읽고 hash만 보존했다.

**후속 비실험 완료:** [D1-L1 방법 감사](./BASELINE_METHOD_AUDIT.md)와 [D1-L2 주장·증거 계약](./CLAIM_EVIDENCE_CONTRACT.md)을 작성했다. Gate 시점, 공개 rule 차이, 단순 대안과 기각 기준을 보강했다.

**D1-L3 완료:** [40개 task·관측 경로 감사](./TASK_OBSERVABILITY_AUDIT.md)와 실행 불가능한 후보 명세를 작성했다. Strict absolute-EEF-orientation 대조는 확보하지 못했고 primary 정책의 state-value 전제를 수정했다.

**D1-L4 완료:** [최초 pilot 계약](./PRE_EXPERIMENT_CONTRACT.md)에서 OFT/선정 task의 perturbation·shared reset·정보/예산·qualification을 고정했다. M2-style port의 calibration budget 차이와 query tier를 구분했다. 실제 구현·runtime·효과는 미검증이며 다음은 자원 조건을 충족한 D1-E1 G0/G1이다. G-PSMR 공식 구현·calibration manifest, ReViP 최신 버전, GAP Octo recipe와 코드 차이 해소는 별도 D1-R1 의존성이다. 공개되지 않은 세부를 추측해 채우지 않는다.

**실험이 있어야만 답할 항목:** Native clean competence와 useful state/goal use, fault의 task solvability, 강한 baseline 이후 남는 개선 여지, 실제 로봇·다른 embodiment 일반화. 따라서 현재 결론은 **baseline 문헌 준비 완료, D1의 연구 기여 검증은 미완료**다.
