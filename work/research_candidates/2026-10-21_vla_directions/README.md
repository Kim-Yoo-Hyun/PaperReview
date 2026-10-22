# VLA 기반 신규 연구 방향: 2024–2026 문헌 대조

> 이 문서는 최초 제안 기록이다. D1의 현재 판정은 [N1–N4 후속 심사](../2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md)의 신규 방법 NO-GO / 진단 HOLD다. 이후 [D2 비실험 buildup](../2026-10-22_d2_buildup/README.md)도 넓은 방법 NO-GO / 조건부 진단 HOLD로 판단했다. 사용자의 후속 조건부 지시에 따른 [D3 buildup](../2026-10-22_d3_buildup/README.md)은 목표 가능성 진단으로 REVISE하고 추가 비실험 task 자격 검토를 추천했다. 아래 후보 순서·미실행 계획은 당시 기록으로 보존한다. 외부 16편의 registry 등록과 version 정정은 [D1 closest-work](../2026-10-21_d1_buildup/CLOSEST_WORK.md)를 따른다.

- 조사일: 2026-10-21 KST
- 판정: **D1을 다음 buildup의 조건부 1순위로 추천**. D2는 manipulation–navigation 연결 후보, D3는 직접 충돌이 커 낮은 우선순위다.
- 단계: 문헌 기반 방향 제안. 신규 방법 채택, native 실행 가능성, 정책 성능은 검증하지 않았다.
- 근거: [30편의 source·registry 대조](./LITERATURE.md), [D1 검증 설계](./D1_SENSOR_CONFLICT.md), [문서 검증](./VALIDATION.md).

## 1. 이번 조사에서 바꾼 출발점

VLA가 실제 로봇의 상태를 해석하고 행동을 바꾸는 문제에서 출발한다. RL은 필요성이 드러날 때 비교할 방법이며 연구 방향의 필수 조건으로 두지 않는다. 기존 C1–C6의 보류·NO-GO를 해제하지 않는다.

Registry 974편의 metadata를 검색하고, 그중 2024–2026년 702편을 최근 문헌의 탐색 범위로 삼았다. 아래 비교에 직접 사용한 것은 **30편: 공식 학회·저널 근거 20편, preprint 또는 저자 발표 상태만 확인한 10편**이다. 16편은 기존 registry, 14편은 외부 문헌이다. 주요 충돌 7편은 관련 method/evaluation 본문 절을 읽었다. 702편 또는 30편 전체를 정독했다는 뜻은 아니다. 학회별 전수조사·venue quota도 아니다.

주요 출처는 CoRL/PMLR, NeurIPS proceedings, RSS proceedings, CVF, ICML/PMLR, IEEE RA-L이다. 2026년에는 공식 확인한 출판물만 해당 venue로 기록했다. WholeBodyVLA와 DialogVLA의 저자 표기는 공식 acceptance 확인과 분리했다. 신규 논문 등록과 tier 재분류는 이번 방향 제안에 포함하지 않았다.

## 2. 문헌에서 확인한 흐름과 그 의미

| 흐름 | 대표 근거 | 이번 연구 선택에 주는 의미 — 연구자 해석 |
|---|---|---|
| 다양한 로봇의 입력·행동을 공유하는 정책 | OpenVLA, HPT, π0, π0.5 — L01/L02/L05/L06 | 다른 로봇을 학습하거나 action head를 공유한다는 사실만으로 새로운 기여가 되기 어렵다. 어떤 물리적 변화에 무엇이 전이되는지 좁혀야 한다. |
| 3D 정보를 행동 공간에 연결 | SpatialVLA, 3DS-VLA, PointVLA, Any3D-VLA — L08/L09/L15/L16 | 단순 point cloud 추가보다 잘못된 공간 정보가 어떤 행동 오류를 만드는지가 남길 질문이다. |
| 실제 접촉과 고속 feedback | ForceVLA2, AT-VLA, SCFields, CAP — L13/L14/L18/L20 | force/tactile 융합, slow–fast 제어, contact conditioning 자체는 이미 강한 선행연구가 있다. |
| 언어 의도와 제어의 연결 | Hi Robot, DISC, SwitchVLA — L07/L19/X07 | 지시를 더 잘 따르거나 중간에 바꾸는 넓은 질문은 혼잡하다. 전환 시 보존할 물리적 상태까지 비교해야 한다. |
| navigation과 manipulation의 통합 | MoManipVLA, MoTo, NaVILA, TIC-VLA — L10/L11/L12/L17 | 단순 docking·reachability·latency 대응을 넘어, 조작으로 바뀐 robot–object 상태가 다음 이동을 바꾸는지 볼 수 있다. |

논문별 직접 링크와 확인 범위는 [LITERATURE.md](./LITERATURE.md)에 있다. 위 해석은 각 논문의 저자 주장이나 합의된 field-wide 결론이 아니다.

## 3. 후보 비교와 추천

| 순서 | 후보와 핵심 질문 | 발전할 수 있는 기여 | 가장 강한 기각 위험 | 현재 판단 |
|---|---|---|---|---|
| 1 | **D1. 시각–proprioception 불일치의 원인에 따라 행동을 바꾸는 VLA**. 센서는 값을 보내지만 일부가 틀렸고 작업 중 원인이 바뀔 때, 실제 상태 변화와 관측 오류를 구별할 수 있는가? | 식별 가능한 조건·불가능한 조건을 구분하고, 그 구분이 task-conditioned 행동에 필요한지를 설명하는 상태 추정·정책 interface | 단순 기하학 보정, 한 모달리티 무시, history augmentation 또는 기존 adaptation으로 충분할 수 있음 | **후속 buildup 추천**. 비교 설계의 명확성과 첫 진단 비용을 기준으로 1순위; 논문 채택 가능성의 확률 평가는 아님 |
| 2 | **D2. 잡은 물체까지 포함해 이동 가능성을 판단하는 VLA**. 같은 로봇·목적지라도 grasp pose와 물체 형상이 바뀌면 운반 자세·통로 선택을 바꾸는가? | grasp → transport → place를 연결하는 행동 표현이 새로운 물체·공간 조합에서 갖는 이점 | attached-object collision planning과 ReKep/TAMP로 해결되는 고전 문제를 재포장할 위험 | **예비 후보**. 연구 적합성은 높지만 native mobile system과 물리 검증 비용이 더 큼 |
| 3 | **D3. 되돌릴 수 없는 상태 변화 뒤의 지시 수정**. 이미 수행한 행동을 단순 역재생할 수 없을 때 어떤 부분을 유지하고 새 목표로 이어가는가? | 성공한 전환 경험을 재사용하는 VLA continuation representation | SwitchVLA의 contact-aware switching·rollback, Hi Robot, symbolic replanning과 가까움 | **낮은 우선순위**. 일반 interruption 방법은 제안하지 않음 |

### D1을 먼저 권하는 이유

기존 연구들은 서로 다른 조건을 다룬다. [CoRE-VLA](https://arxiv.org/html/2607.03693v2)는 auxiliary sensor의 availability indicator를 사용하며 v2는 noise·delay·misalignment도 평가한다. [Self-Adaptive VLA](https://arxiv.org/html/2609.30092v1)는 시행 간 고정된 hardware offset을 이전 rollout으로 보상한다. [LIBERO-RIG](https://arxiv.org/html/2610.18843v1)는 한 embodiment에서 episode당 한 fault axis를 시험한다. **값이 존재하지만 틀렸으며, 원인이 작업 중 바뀌는 조건**을 이들 방법이 같은 정보·비용으로 얼마나 해결하는지 비교할 여지가 있다.

다만 “여러 fault를 합쳤다”거나 “신뢰도 gate를 붙였다”만으로는 충분하지 않다. 센서 불일치가 실제 성능 병목인지, 가용 관측으로 원인을 알아낼 수 있는지, 기존 state estimator로 설명하고 해결할 수 있는지를 먼저 확인한다. [D1 설계](./D1_SENSOR_CONFLICT.md)에 대안 설명과 중단 기준을 고정했다.

### D2를 남기는 범위

예시: 긴 물체를 잡은 뒤 좁은 통로를 지나려면 손목 방향·grasp 위치·base 경로를 함께 바꿔야 한다. 빈 gripper일 때 가능한 경로가 물체를 들면 불가능해진다. 처음에는 rigid object만 사용하고 액체·변형·humanoid balance는 제외한다.

[MoTo, CoRL 2025](https://proceedings.mlr.press/v305/wu25c.html)는 조작을 위한 docking과 interaction keypoint를 다룬다. [ReKep, CoRL 2024](https://proceedings.mlr.press/v270/huang25g.html)는 이미 여러 단계의 공간·경로 제약을 최적화한다. 따라서 새로운 질문은 “충돌을 피하는가”보다 **관측과 지시에서 추정한 grasp-dependent 운반 제약을 VLA가 재사용하며, 새로운 object × passage × goal 조합에서 단순한 modular baseline을 넘어서는가**다. 이 비교가 선행연구 전체에서 미해결이라고 확정한 것은 아니다.

첫 비교는 nominal VLA, attached-object collision planner를 붙인 VLA, 추정 geometry를 쓰는 ReKep/TAMP 계열, oracle geometry comparator다. 모두 같은 관측·grasp 후보·경로 예산을 사용한다. 성공률과 함께 물체 충돌, 최소 clearance, 재파지 수, 이동거리, 최종 배치 정확도를 보고한다. Oracle mesh 사용과 추정 geometry 사용은 별도 결과로 구분한다. 주어진 geometry로 기존 planner가 문제를 해결하면 새로운 planning 방법 주장은 중단한다. 새로운 표현의 이득도 없다면 D2를 보류한다.

### D3를 낮춘 근거

[SwitchVLA §3.4](https://arxiv.org/html/2506.03574v1)는 contact 중 rollback을 이전 action의 역방향으로 구성하고, contact가 없을 때 새 작업의 시작 자세로 전환한다. 따라서 contact-aware task switching을 새 기여로 주장하지 않는다. 남길 수 있는 좁은 질문은 seal 개봉·일방향 latch처럼 역재생으로 원상 복귀할 수 없는 상태에서의 재계획이다. 이는 **우리의 확장 해석**이며 해당 논문의 실패가 실증된 것이 아니다. State-aware task planner가 충분하면 learned VLA 방법은 불필요하다. 별도의 비가역 task·outcome 정의가 확보되기 전에는 활성 pilot으로 승격하지 않는다.

## 4. 이번에 채택하지 않은 넓은 방향

| 방향 | 제외·축소 이유 |
|---|---|
| VLA + RL의 로봇 간 전이 | 이전 검토의 qualification 문제를 해결하지 않은 채 반복하지 않는다. D1의 두 번째 embodiment 평가는 RL gain transfer와 다른 질문이다. |
| point cloud·촉각·force 추가 | L08/L09/L13–L16/L18/L20이 이미 직접적인 비교 대상이다. 센서 추가만을 기여로 삼지 않는다. |
| history를 넣어 calibration shift 적응 | X01/X02가 직접 충돌한다. D1에서도 반드시 baseline으로 취급한다. |
| sensor dropout 또는 MoE routing | X04와 충돌한다. D1은 hidden corruption의 식별 가능성을 별도로 요구한다. |
| 양팔의 acting/stabilizing 역할 분리 | VoxAct-B와 DialogVLA가 이미 역할 문제를 다룬다. 단순 역할 token으로 새 후보를 만들지 않는다. |
| 지시 변경·contact-aware rollback | X07/X08 때문에 D3의 넓은 formulation은 제외한다. |
| reward audit·reset·checkpoint selection | C4–C6 결론을 유지한다. 후속 정책 연구의 평가 protocol으로만 재사용한다. |

## 5. 바로 다음 단계와 자원 경계

다음 작업은 D1의 **본문·공개 artifact 비교와 관측 가능성 표 확정**이다. 여러 센서가 있어도 식별 불가능한 상황에서 모델만 키우지 않도록, 어떤 보정 행동을 정당화할 정보가 존재하는지 먼저 정한다. 연구 질문은 후보 수준이며 현재 존재하는 failure의 크기와 제안 효과는 아직 모른다.

- [x] 기존 후보의 중단 이유를 보존하고 최신 2024–2026 문헌과 대조.
- [x] D1의 direct collision·가설·대안 설명·최소 비교·중단 기준 작성.
- [ ] D1 direct collision의 공개 code/weights/data release와 입력 계약을 commit 단위로 확인.
- [ ] 두 candidate checkpoint의 clean-task competence와 시각·state 입력 사용을 실제로 확인.
- [ ] Fault intervention·관측 가능성·원인 label·policy-visible input manifest 생성 및 검증.
- [ ] Native Docker pilot 후 방법 구현 여부 결정.

현재 Mac/ARM64 Docker 환경의 과거 runtime 제약은 그대로다. 문헌 검토와 repository maintenance만 수행했으며 Docker 실험·모델 실행·host 패키지 설치는 하지 않았다. 이후 실험과 의존성은 Docker 안에서만 처리한다. 정적 분석 가능성과 GPU 학습 가능성을 같은 것으로 취급하지 않는다. 실행 환경·checkpoint·데이터가 확보되지 않으면 큰 학습을 시작하지 않는다.

## 6. 저장소 반영

이 폴더는 날짜별 후보 검토 결과이며 paper registry나 새로운 tier source가 아니다. PAPER.md, manifest, tier membership, 사용자 reading status, 4,870개 paper note는 유지했다. 최신 navigation은 이 문서를 가리키며, [C6 결과](../2026-10-21_c6_checkpoint_audit/README.md)를 포함한 기존 기록은 보존한다.
