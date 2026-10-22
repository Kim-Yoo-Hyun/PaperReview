# D1 buildup: 센서 불일치에서 원인 구별이 행동에 필요한 조건

- 검토일: 2026-10-21 KST; baseline 문헌 보강: 2026-10-22 KST
- 절차: [기존 buildup 가이드의 8단계](../../../research/IDEA_BUILDUP_GUIDE.md#5-문헌에서-아이디어로-넘어가는-8단계)
- 출발점: [D1 최초 제안](../2026-10-21_vla_directions/D1_SENSOR_CONFLICT.md)
- 현재 판단: **신규 VLA+RL 방법 채택 NO-GO / 조건부 진단 HOLD.** [우선순위 1–4 재심사](./NONEXPERIMENTAL_REVIEW.md)가 아래 1차 REVISE 판단을 대체한다. Native 효과 미검증이며 GPU 확보만으로 재개하지 않는다.
- Evidence: 문헌에서 확인한 overlap·가정은 `READING-SUPPORTED`. 실행한 것은 합성 반례와 공개 source audit이며, **VLA 정책 효과는 CURATION-HYPOTHESIS**다. 사용자 reading tracker는 올리지 않았다.

**2026-10-22 작업 전환:** R1/R2/F1의 판단을 바꿀 새 근거를 확보하지 못해 D1 HOLD를 유지하고, 사용자의 조건부 요청에 따라 [D2 비실험 buildup](../2026-10-22_d2_buildup/README.md)을 진행했다. 아래 D1 재개 조건은 보존하며 현재 활성 작업의 인계는 [TODO](../../../TODO.md)를 따른다.

문제 자체는 가치가 있다. 그러나 고장 원인 분류, modality rebalance, history adaptation, 입력별 보정은 이미 존재한다. 남길 질문은 **“같은 정책 입력 예산에서, 식별 가능한 오류에 대해 원인에 맞는 보정이 단순 baseline보다 실제로 필요한가?”**다. 이 조건을 만족하는 현상을 아직 실제 VLA에서 확인하지 못했다.

**최신 N1–N4 완료:** [직접 충돌·필요 조건·task 반박·RL 심사](./NONEXPERIMENTAL_REVIEW.md)를 수행했다. 현재 task의 차별적 보정 필요성, 단순 대안 이후 gap, RL의 순차 이득이 미확보여서 현재 method 투자 NO-GO다. 문헌·수식 분석은 완료했지만 실험적 반증은 아니다. 다음은 [TODO D1-R2](../../../TODO.md)의 재개 근거 심사이며 E1/E2는 HOLD_RESEARCH다. 아래 단계별 내용과 L1–L4/E1은 판단의 이력으로 보존한다.

**2026-10-22 후속:** 실험 제약은 buildup 전체의 중단을 뜻하지 않는다. [Baseline dossier](./BASELINE_DOSSIER.md)에 핵심 6편, 공개 구현·checkpoint 위치, native interface와 비교 계약을 확보했다. 비실험 문헌 준비는 진행했고 native 정책 효과 검증은 HOLD다. G-PSMR의 지정 본문 절을 추가 확인하여 “실제 물리 변화는 항상 보정하면 안 된다”는 가정을 배제했다. 판단 기준은 목표 수행에 필요한 정보와 행동을 보존하는지다.

**D1-L1/L2 완료:** [방법 감사](./BASELINE_METHOD_AUDIT.md)에서 G-PSMR gate의 시점·결합 순서, GAP 공식판과 공개 코드의 차이, ReViP 버전 경계를 확인했다. [주장·증거 계약](./CLAIM_EVIDENCE_CONTRACT.md)은 고정 orientation bias가 원인 분류 없이 제거되는 특수 경우를 도출하고 causal 재보정·task별 reference를 강한 대조로 추가했다. 이는 정책 실험 결과가 아니다.

**D1-L3 결과:** [Task·native dataflow 감사](./TASK_OBSERVABILITY_AUDIT.md)를 완료했다. `pi05_libero`는 지정 native config에서 state 값이 action에 연결되지 않아 state 보정 primary에서 제외했다. OFT의 proprio-enabled Goal variant로 후보를 변경했다. 40개 task의 goal 구조에서 strict absolute-EEF-orientation 대조는 확보하지 못했으며, Goal 0/8과 contrast 1·보조 7을 조건부 후보로 정했다. [후보 명세](./TASK_CANDIDATES.json)는 실행 불가능한 source artifact다.

**현재 D1-L4 완료:** [비실험 계약](./PRE_EXPERIMENT_CONTRACT.md)과 [PILOT_SPEC.json](./PILOT_SPEC.json)에 report-only orientation 오류·정상 controller를 통한 초기 자세 변화, shared reset replay, split·예산·기각 기준을 고정했다. Flat state만으로 fixture/controller까지 복원되지 않는 위험을 source에서 확인했다. 생성한 spec은 executable=false이며 runtime/payload·실제 split·물리 validity는 미검증이다. 계획한 L1–L4는 완료했고 다음 [TODO D1-E1](../../../TODO.md)은 자원 조건을 충족한 뒤 G0→G1이다.

**D1-E1 착수 결과:** [현재 컴퓨터 Docker preflight](../../experiments/vla_d1_e1_preflight/RESULTS.md)는 실행했다. GPU allocation은 exit 125였고 VM RAM 7.65 GiB 대비 기본 model tensor 저장량은 14.05 GiB다. OFT source에는 CPU fallback이 있으며 FlashAttention 인수는 주석이므로 코드상 CUDA 필수라고 단정하지 않는다. 현재 native 실행 자원은 qualified하지 않아 G0 전체 미충족·G1 미실행이다. Goal normalizer 실제 hash와 native downloader의 revision 미고정도 확인했다. E1은 WAITING_RESOURCE이며 동일 조건의 preflight를 반복하지 않는다.

## 단계 1. 문제와 해결 가치

배포 중 영상과 robot state가 어긋났을 때 잘못된 입력을 보정하면 조작을 회복할 수 있지만, 실제 물체·로봇 이동을 센서 오류로 오인하여 지우면 목표 수행을 망칠 수 있다. **오류에 반응하는 것과 필요한 물리적 변화를 보존하는 것의 양립**이 목표다.

문헌은 VLA의 hardware-shift 실패, false completion, modality dominance를 뒷받침한다. 이들이 모두 하나의 hidden-cause 문제라는 주장, 복합 고장의 실제 빈도, 현재 checkpoint에서의 효과 크기는 미확인이다. [LIBERO-RIG §2–4](https://arxiv.org/html/2610.18843v1), [ReViP v3 §3](https://arxiv.org/html/2601.16667v3), [GAP §3–5](https://arxiv.org/html/2602.12032v1).

## 단계 2. 필요한 문헌 집합

[비교표](./CLOSEST_WORK.md)에 다음 역할을 채웠다.

- Foundation/강한 대안: 기존 registry의 Kalman·POMDP·HPT, 시각 기반 fault isolation과 bias 추정.
- 직접 방법: Self-Adaptive VLA, ReViP 최신 원문·project, CoRE-VLA v2, camera-restoration CoRe-VLA, GAP, G-PSMR.
- 평가: LIBERO-RIG와 proprioceptive-interface controlled study.
- 다른 설명: state를 거의 쓰지 않는 정책, state에 포함된 외부 localization, 학습 불균형, 단순 기하 보정.
- 인접 충돌: active fault diagnosis와 post-hoc VLM diagnosis. 능동 probing이나 원인 설명을 더하는 것만으로는 novelty가 되지 않는다.

최신 버전 재확인으로 최초 제안의 문헌 경계를 수정했다. CoRE-VLA v2는 missing sensor 외에 noise·delay·misalignment도 평가한다. WholeBodyVLA의 ICLR 2026 status는 공식 proceedings에서 확인했다. ReViP는 최신 title이 **Mitigating**이며 project의 새 모듈·Flash 설명은 arXiv v3와 구분했다.

## 단계 3. 가정·interface·증거 비교

비교에서 성능 숫자를 한 줄로 순위화하지 않았다. Self-Adaptive의 고정 hardware offset, CoRE의 optional depth, ReViP의 task-progress mismatch, GAP의 학습 gradient 문제는 같은 조건이 아니다. Camera CoRe의 알려진 camera transform이나 외부 localization을 쓰는 state는 D1의 배포 입력보다 정보가 많을 수 있다. [비교표와 공개 구현 확인](./CLOSEST_WORK.md).

## 단계 4. 빈칸을 경쟁 가설로 전환

| 가설 | 구별할 검사 | 이번 판단 |
|---|---|---|
| H0: 정책이 state를 사용하지 않아 개선 대상이 없다 | Value path 감사 → native input intervention·clean competence | `pi05_libero`의 state-value 경로 부재를 source로 확인하여 제외. OFT 경로는 있으나 utility는 미검증 |
| H1: 원인 구별이 관측으로 불가능하다 | 동일 history·다른 필요 행동의 반례 | 특정 무기준점 설정에서 확인 |
| H2: 구별 가능하면 단순 residual/calibration으로 충분하다 | 동일 관측의 residual baseline | 합성 single-fault 조건에서는 충분; 실제 정책은 미확인 |
| H3: 진단 없이 relative-goal control로 충분하다 | 원인 ambiguity와 task-action ambiguity를 분리 | 합성 반례에서 확인 |
| H4: GAP·history·augmentation·기존 restoration으로 충분하다 | 같은 data/history/compute의 강한 비교 | 직접 선행이 있어 우선 배제해야 함 |
| H5: 위 조건을 넘어 cause-conditioned correction이 필요하다 | 식별 가능 + 행동 차이 + baseline 잔여 gap + diagnostic headroom | **아직 지지하지 못함** |

H1이 성립하지 않는다고 H5가 참이 되는 것도, H0를 통과한다고 연구 가치가 입증되는 것도 아니다.

## 단계 5. Closest-work와 novelty 심사

다음 문장은 기여로 쓰지 않는다: “vision과 proprioception을 결합한다”, “고장 원인을 구분한다”, “history로 hardware shift에 적응한다”, “sensor stream마다 보정한다”, “episode 중 센서 문제가 생겨도 견딘다”. 각각 기존 연구가 상당 부분 다룬다.

남길 잠정 문장: **“실제 task-state 변화와 관측 오류의 보정이 충돌하는 조건에서, 관측의 식별 가능성과 task에 따른 보정 필요성을 통제하여 기존 VLA robustness 결론의 적용 범위를 검사한다.”** 아직 새로운 algorithm이나 미개척 benchmark라는 주장은 아니다. 특히 G-PSMR과 classical FDI에 간단한 변경만 해도 해결될 가능성이 크다.

## 단계 6. 주장–증거 연결과 최소 비교

| 잠정 주장 | 필요한 증거 | 가장 강한 대안 | 현재 |
|---|---|---|---|
| D1 setting에 물리적으로 타당한 보정 충돌이 있다 | 같은 task·초기 상태·goal에서 sensor 오류와 실제 변화의 paired rollout | 인위적인 observation 조작 artifact | 합성 논리만 확인 |
| 올바른 정보가 있을 때 개선 여지가 있다 | Fault-aware diagnostic comparator와 clean/fault 차이 | Base policy 능력 부족 | 미실행 |
| 일반 복원보다 task-aware correction이 필요하다 | Residual estimator, history/augmentation, GAP 계열과 matched 비교 | 기존 기법 조합·추가 정보 효과 | 미실행 |
| 다른 연구자가 재사용할 결과가 남는다 | 여러 task·seed·holdout에서 경계 재현 | 특정 checkpoint tuning | 미실행 |

정책 pilot의 입력·예산·baseline·reject 조건은 [검증 계약](./PILOT_CONTRACT.md)에 분리했다. 실행 전 필수 항목이 미확정인 상태를 표시했으며 구현 준비 완료로 취급하지 않는다.

## 단계 7. 가장 취약한 연결의 저비용 검사

Docker에서 [합성 식별 가능성 검사](./diagnostic.py)와 [공개 source audit](./artifact_audit.py)를 실행했다. 결과와 한계는 [RESULTS.md](./RESULTS.md)에 있다.

1. 기준점·초기 참값이 없을 때 같은 관측/명령 history가 서로 다른 absolute-goal correction을 요구하는 반례를 구성했다.
2. 같은 좌표계의 알려진 고정 기준점을 추가하면 단순 식으로 반례가 해소됐다. 이는 추가 정보의 효과다.
3. Relative goal에서는 원인이 불명확해도 필요한 행동이 같을 수 있었다.
4. 깨끗한 직전 상태와 single-fault 가정에서는 단순 innovation residual이 세 오류를 분리했다. 복합 오류 및 실제 외력 이동까지 포함하면 다시 alias가 생겼다.
5. Native openpi state 경로와 GAP code는 확인했지만 현재 Docker에서 공식 GPU 실행 조건을 충족하지 않는다. CPU 이식이나 새로운 작은 policy 학습으로 문제를 바꾸지 않았다.

이 결과는 “더 복잡한 VLA를 만들면 해결된다”는 출발점을 지지하지 않는다. 동시에 모든 실제 장면이 식별 불가능하다는 결론도 아니다.

## 단계 8. 반박·결정·외부 피드백

외부 연구자에게 연락하거나 피드백을 받은 적은 없다. 이 단계의 **실제 동료/지도교수 검토는 미완료**다. 대신 위 근거를 이용한 내부 반박과 결정은 완료했다.

| 예상 반박 | 반영한 수정 |
|---|---|
| 기존 state estimation을 VLA라는 이름으로 포장했다 | 새로운 fault-isolation 방법 주장 삭제; classical residual을 필수 baseline으로 고정 |
| 정답을 알 수 없는 입력에 원인 label을 강요한다 | Identifiable/ambiguous stratum 분리; ambiguous에서 정확한 원인 분류를 요구하지 않음 |
| 원인 분류가 task 수행과 무관하다 | Relative-goal 대조군 및 language-goal contrast 필수화 |
| 강한 VLA가 state를 쓰지 않으면 현상 자체가 없다 | Input-use와 clean competence를 첫 중단 gate로 이동 |
| 최신 선행을 약하게 읽었다 | CoRE v2와 ReViP 최신 project 범위 수정; GAP·G-PSMR 추가 |

**연구 가치 판단:** broad D1을 새 학습 방법으로 바로 발전시킬 근거는 부족하다. 축소한 조건부 진단은 검토 가치가 있지만, 실제 VLA에서 **식별 가능·행동 관련·단순 baseline으로 미해결**인 사례가 함께 나와야 본격 연구 후보가 된다. 현재 top-tier 기여 가능성이 검증됐다고 말할 수 없다.

N1–N4 이전의 다음 정책 실험은 후보 OFT의 G0/G1이었다. 현재는 [재심사 결과와 재개 조건](./NONEXPERIMENTAL_REVIEW.md#43-다음-행동과-재개-조건)을 먼저 충족해야 한다. Native runtime·payload·split/reset과 정책 효과는 여전히 미검증이다. G1 screening 통과만으로 유용한 proprioception의 필요성을 입증하지 않으며 C1–C6의 기존 NO-GO/HOLD도 유지한다.
