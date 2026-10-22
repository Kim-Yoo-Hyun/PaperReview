# C2 후속 검토: 수행 제약의 조합 일반화에 RL이 필요한가

- 확인일: **2026-10-21 KST**
- 최신 판단: **1차 데이터·실행 gate 검증 후 현재 설계 NO-GO. 본격 연구로 채택하지 않는다.** [빌드업 최종 판단](./C2_BUILDUP_RESULT.md).
- 근거: 관련 본문, 공식 publication metadata, revision을 고정한 공개 코드의 정적 검토. 학습·추론·시뮬레이션 결과는 없다.
- 연결: [공개 평가·데이터 감사](./C2_DATA_AUDIT.md) · [축소한 검증 설계](./C2_PROTOCOL.md) · [source audit](./C2_SOURCE_AUDIT.json) · [Docker 1차 검증](../../experiments/vla_rl_c2_first_pass/RESULTS.md)

아래 문헌 비교와 초기 설계는 유지한다. 후속 검증에서는 실제 payload 12개와 학습 경유 trace 50개를 확인했으나 완전한 reward·coverage 계약 및 native runtime을 확보하지 못했다. 정책 효과는 미측정이다. 초기의 “다음 데이터 검사” 판단은 위 최종 결과로 대체한다.

## 1. 이번에 바뀐 판단

“같은 목표라도 수행 방식이 다르다”, “언어를 무시하는 VLA를 개선한다”, “실행 제약을 별도로 평가한다”는 문제 제기만으로는 부족하다. 초기 목록에 없던 **ExecVLA, RoboFollow, Diagnosing Compositional Generalization**까지 포함하면 문제 설정·평가·데이터 커버리지 분석에 직접적인 선행 연구가 있다.

또한 CounterAlign은 현재 **CoRL 2026 Poster**로 확인됐다. 이전 문헌표의 venue 미검증 표기를 갱신한다. 아래 publication status는 공식 OpenReview Search API의 정확한 title·forum·venueid를 대조했다. Forum 웹 렌더링과 일부 proceedings 본문 접근이 제한되어 기술 비교에는 명시한 arXiv 본문을 사용했다. 최종 학회판과 모든 개정 차이를 대조했다는 뜻은 아니다. [공식 CounterAlign forum](https://openreview.net/forum?id=AY4totylcx), [검증 metadata](./C2_SOURCE_AUDIT.json).

## 2. 직접 충돌과 평가 범위

아래 L 번호는 [문헌표](./LITERATURE.md)의 검토용 reference다. Registry admission이나 사용자 정독 완료를 뜻하지 않는다.

| 문헌 / 확인 status | 확인 범위와 paper-supported conclusion | C2에서 남겨야 할 구별 |
|---|---|---|
| **L1 LangForce — ICML 2026** | [PMLR](https://proceedings.mlr.press/v306/lian26d.html), [arXiv §3–4](https://arxiv.org/html/2601.15197). Query 위치로 vision-only와 language-conditioned branch를 구분하고, action imitation에 language LLR 목적을 결합한다. 추론에는 posterior branch를 쓴다. 공개 `LangForce.py`의 forward·loss·predict 경로도 확인했다. | Language-sensitive objective 자체는 선점됐다. 같은 backbone에서 coverage를 통제한 RL 대 SFT 효과와는 구분된다. 서로 다른 모델의 점수를 곧바로 RL 효과로 비교하지 않는다. |
| **L2 How-Level 진단 — arXiv; ACL ARR 2026 October submission, 채택 아님** | [본문 §3–6, App. B/C](https://arxiv.org/html/2610.21251), [공식 submission](https://openreview.net/forum?id=PM8XCMAwjI). Segment enrichment로 행동 반응이 늘어도 demanding/OOD 조건의 성공으로 이어지는 것은 아니다. SIMPLER-IN은 Path·Grasp·Place를 다룬다. | 반응성·성공·준수의 구별도 기존 기여다. 공개 Path의 조건 변경은 물리 환경도 바꾸므로 C2의 동일 장면 개입에 그대로 쓰지 않는다. |
| **L3 CounterAlign — CoRL 2026 Poster** | [공식 forum](https://openreview.net/forum?id=AY4totylcx), [본문 §3–4 및 relabeling 부록](https://arxiv.org/html/2608.21740). Instruction-grounded discriminator reward, nnPU, IQL 및 advantage-weighted flow matching을 결합한다. 주요 simulation 비교는 LIBERO-PRO의 Obj/Pos/Sem/Task perturbation이다. | Negative relabeling·offline RL·모호한 negative 처리는 신규성이 아니다. 확인한 평가가 고정 goal의 object×waypoint×orientation holdout을 검증한 것으로 해석되지는 않는다. 저자 [project](https://counteralign.airoa.io/)는 현재 code를 Coming Soon으로 표시한다. |
| **L4 RSS — ACL 2026 main** | [공식 본문 §3–4](https://aclanthology.org/2026.acl-long.190.pdf). Instruction 확장과 conditional/unconditional steering을 결합한다. 공개 flow-policy 구현에서는 두 velocity prediction을 guidance scale로 결합한다. | 단순 language guidance를 새 방법으로 제안하지 않는다. 언어 변형의 의미 보존과 실제 실행 제약 변경을 구분하고, 추가 추론 비용을 포함한다. |
| **L7 ExecVLA — arXiv v2; ICLR 2027 submission, 채택 아님** | [v2 본문 §3–4, App. A](https://arxiv.org/html/2603.17524v2), [공식 submission](https://openreview.net/forum?id=BCw1oqG73w). Goal과 execution 표현·reasoning을 분리하여 LIBERO 계열 및 Realman에서 수행 제약을 평가한다. 본문 일부에는 이전 이름 KineVLA가 남아 있다. | C2의 넓은 what/how 구분에 가장 직접적인 방법 충돌이다. 확인한 평가 기술에서 엄격한 factor-combination holdout을 식별하지 못했지만, 이를 논문 전체에 없다는 단정으로 쓰지 않는다. 별도 저자 구현은 이번 공식 출처 범위에서 식별하지 못했다. 인용된 MiniVLA repo를 ExecVLA code로 오인하지 않는다. |
| **L8 Diagnosing Compositional Generalization in Sequential Robot Tasks — CoRL 2026 Spotlight** | [공식 forum](https://openreview.net/forum?id=gQFYIM5dJy), [본문 §3–5, App. B](https://arxiv.org/html/2607.29687). Marginal·composition·context/action shift를 구분하고, 고정 demonstration 예산에서 pair/dependency coverage를 분석한다. DINOv2 기반 flow policy와 순차 task를 사용한다. | “모든 atom이 나왔으므로 coverage가 충분하다”는 가정을 버린다. Pair coverage와 dependency 분석도 신규성이 아니다. 이 결과만으로 pretrained VLA에서 RL이 불필요하다고 결론 내릴 수도 없다. |
| **L9 RoboFollow — CoRL 2026 Poster** | [공식 forum](https://openreview.net/forum?id=A9AQjk3dAt), [본문 §3–4, App. B](https://arxiv.org/html/2609.25636). 같은 scene의 여러 지시, trajectory/orientation 조건, intent/execution 구분, L0–L3 평가를 제공한다. 공개 task와 evaluator도 확인했다. | 같은 장면의 언어 의존성과 how-level 평가를 새 benchmark 기여로 주장하지 않는다. 특히 Scene 3 L2의 semantic rewrite를 C2의 새로운 실행 조합 holdout과 동일시하지 않는다. |
| **L6 SafeVLA — NeurIPS 2025** | [공식 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html)의 constrained learning 설정 재확인. 이번에는 안전 학습 전체 구현을 감사하지 않았다. | Constraint reward나 CMDP를 쓰는 것만으로 새 RL 알고리즘이 되지 않는다. |

**Identity 주의:** ExecVLA와 KineVLA는 arXiv `2603.17524`의 버전 관계다. 두 논문으로 세지 않는다. CoRL status는 위 세 논문에 한정한다. Submission을 acceptance로 올리지 않는다.

## 3. 남길 연구 질문과 경쟁 설명

**연구자 해석 / 미검증 가설:** 동일한 pretrained policy·관측·행동·학습 trajectory와 검증된 label을 사용하고, atomic/pairwise instruction coverage를 맞춘 뒤에도, 완전한 수행 제약 보상을 사용하는 RL이 balanced SFT와 return-weighted imitation보다 **새로운 3요소 조합의 goal∧constraint 성공**을 높이는가?

이를 확인하는 데 필요한 구별은 다음과 같다.

1. **Coverage 효과:** 추가 demonstrations가 새 의존관계나 행동을 제공했는가?
2. **Reward 효과:** 원래 빠진 constraint label을 제공한 것만으로 설명되는가?
3. **Optimization 효과:** 같은 label·trajectory를 사용하는 imitation/return weighting보다 RL의 가치 추정이 필요한가?
4. **Interaction 효과:** RL만 새 rollout을 받았기 때문에 좋아졌는가?

이 네 가지의 분리는 실험 설계 원칙이다. 그 자체를 새 이론이나 방법으로 주장하지 않는다. 표준 RL로 해결되면 새로운 RL 방법의 필요성을 기각한다. 다만 어떤 데이터 지원에서 어떤 보상이 충분한지 재현 가능한 설명이 남으면 empirical study로 재평가할 수 있다.

**첫 데이터 gate에는 reward contrast도 필요하다.** 기록된 모든 trajectory가 원 지시의 goal과 how를 만족한다면, 동일 시점에 지급하는 goal-only/complete terminal reward는 해당 데이터에서 같다. 그 데이터만으로 두 reward의 효과를 구분할 수 없다. 같은 goal의 다른 **training instruction**으로 전체 trace를 재판정한 유효한 위반 예시가 필요하다. 이는 CounterAlign의 relabeling 문제와 다시 만나는 지점이며, 새 기여가 아니다. 후속 검사에서 경유 조건의 negative 50개는 확인했지만 한 training task에만 해당하며, 독립 goal/orientation 판정과 전체 coverage는 미충족이다.

질문은 초기 object×constraint pair holdout에서 **object×waypoint×orientation triple holdout**으로 좁혔다. 모든 pair를 학습에 포함하면서 새로운 triple을 남길 수 있어 coverage 반론을 더 강하게 검사한다. 여전히 state/action support까지 보장하는 설계는 아니다. [8개 실제 task ID와 분할](./C2_SPLIT_DRAFT.json).

## 4. 실행 전제와 현재 판단

| 자산 | 정적으로 확인한 것 | 아직 성립하지 않은 것 |
|---|---|---|
| SIMPLER-IN | evaluator·client·GPU launcher | 동일 scene의 instruction-only Path 비교, 조합 holdout, 현재 Docker runtime |
| RoboFollow | 실제 Scene 3 task ID·평가 경로·3 RGB/14D 입출력; 선택한 8 task 각각 50개 HDF5 파일의 공개 목록 | trajectory 품질, episode별 support/label, scene leakage, 해당 task의 checkpoint competence |
| 조합 일반화 공개 release | training/evaluation code와 고정 simulator revision; README는 pretrained checkpoint 다운로드가 아직 없다고 명시 | 공개 release가 논문의 모든 figure/metric을 그대로 재현한다는 주장 |
| LangForce / RSS | objective 또는 guidance 구현과 공개 model 안내 | C2 데이터에서 동일 조건 학습·평가, 현재 ARM64 Docker 성능 |

RoboFollow의 reference stack은 NVIDIA CUDA와 SAPIEN/cuRobo를 사용한다. LangForce와 조합 일반화 release도 GPU 학습 recipe다. **현재 M4 Docker에서 검증된 C2 실행 경로는 없다.** 이것은 모든 CPU 이식이 불가능하다는 뜻이 아니다. 별도 이식과 native competence 검증 없이 checkpoint를 새 task에 연결하는 일을 본 실험으로 취급하지 않는다. [RoboFollow pinned README](https://github.com/AutoLab-SAI-SJTU/RoboFollow/blob/f642e3d19ddc0a3b0fb5795eef2cd17a12f286d8/README.md), [공개 release](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot/blob/e29c44474495b341d19636bbf90f3cf0fcb1d2d2/README.md).

초기 검토는 **문헌·정적 평가 감사와 실제 task 분할 초안**까지였다. 이후 요청에 따라 별도 Docker에서 실제 데이터를 검사하고 reference 의존성·GPU 경로를 확인했다. [1차 검증 결과](../../experiments/vla_rl_c2_first_pass/RESULTS.md)는 데이터 reader 실행 성공과 native runtime gate 실패를 구분한다. C1의 실행 결과를 C2의 competence 증거로 사용하지 않는다.

## 5. 채택 기준과 다음 작업

- **방법 연구 채택:** 현재 NO-GO. 직접 충돌을 넘는 효과와 설명이 없다.
- **1차 진단:** G0·G1 검사를 수행했고 원 계약 미충족으로 종료했다. G2–G4의 정책 비교는 수행하지 않았다.
- **재개:** 데이터·native 실행 계약을 복구할 새 근거가 생길 때만 최소 진단을 재개한다. [재개 조건](./C2_BUILDUP_RESULT.md)을 따른다.
- **top-tier 가능성:** 현재 근거로는 본격 투자 비추천. 단순 task 추가·성공률 상승을 넘는 설명이 있어야 재판정한다.

검색은 `execution constraints / how-level / instruction following / compositional generalization / counterfactual / VLA RL`과 저자 reference를 중심으로 수행했다. 이번 직접 충돌 검토 범위는 마쳤지만 관련 분야 전체의 부재 증명이나 신규성 확정은 아니다. 남은 핵심 uncertainty는 **RL의 독립적인 이득과 이 설계의 현재 컴퓨터 실행 가능성**이다.
