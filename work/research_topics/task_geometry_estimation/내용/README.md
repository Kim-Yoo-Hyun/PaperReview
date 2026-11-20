# 조작용 3D 추정

Updated: 2026-11-18 KST. **N1 내부 비실험 검토·P0 코드 준비 완료 / 작은 진단 탐색 CONTINUE.** 독립 방법의 신규성·성능 이득은 미확립이다. 11/17 초안을 직접 충돌 문헌과 실제 입력 경로에 맞게 축소했고 [P0 준비 결과](#p0-preparation-result)를 추가했다. [재현 명세](../재현%20방법/README.md) · [공통 원장](../../../sources/new_field_scout_2026-11-17.json) · [TODO](../../../../TODO.md).

## 문제와 이번 결론

로봇이 물체를 넓은 받침대에 놓는 작업과 좁은 고정구에 맞추는 작업에서는 같은 위치 오차도 결과가 다르다. 평균 3D 정확도만으로 개선할 오류를 선택하면 행동에 중요한 정보를 놓칠 수 있다. 답을 알면 재구성 모델·센서·VLA 표현·학습 목표를 선택하는 로봇 연구자의 결정이 달라진다.

**현재 질문:** 동일한 물리 장면·VLA·학습 정보에서, geometry 입력 오차의 위치와 종류에 따른 행동 영향을 작업 허용 오차로 설명할 수 있는가? 전체/물체 영역 오차, 단순 보정, 정책 행동 변화량을 넘어서는 설명력이 있으면 그 신호로 제한된 geometry adapter 학습을 개선할 수 있는가?

처음에는 **SpatialVLA가 실제 소비하는 camera-frame depth 표현**을 대상으로 한다. 전체 3D reconstruction·SLAM·physics model을 새로 만들지 않는다. Scene·언어·행동을 한 정책에 연결하는 방향을 유지하되 첫 진단은 정책을 고정한다. RL 공동 갱신은 필수 조건이 아닌 후속 가설이다.

- 실제 로봇 행동과 연결되는 문제이므로 탐색 가치는 있다. GPU가 없다는 이유로 폐기하지 않는다.
- **행동에 중요한 추정 오차를 더 학습하는 원리와 허용 오차 가중은 이미 있다.** 일반적인 task-aware reconstruction loss를 새 방법으로 제시하던 초안은 수정한다.
- 먼저 고정 정책의 geometry 개입 진단을 만든다. 단순 상관·합성 noise에서의 logit 변화만 남으면 독립 방법 논문으로 확대하지 않는다. 현재의 약점은 실험 미실행뿐 아니라 내용상 강한 직접 선행에도 있다.

<a id="n1-literature"></a>
## 직접 선행 대조

2024–2026 검색과 registry 대조 후 가까운 formulation·source에 집중했다. 아래는 지정 절/공식 초록 확인이며 전면 정독·코드 재현이 아니다. [REG-R17](../../../update/REGISTRY.md#reg-r18)의 기존 등록과 이번 외부 출처를 구별하며 reading tracker는 유지한다.

| 선행·확인 범위 | 이미 있는 기여 | 필요한 구분 |
|---|---|---|
| [SpatialVLA — RSS2025](https://roboticsproceedings.org/rss21/p011.html), model/processor/finetune source | Depth→camera XYZ→Ego3D embedding | 임의 robot-frame point cloud 입력이 아님. 외부 reconstruction을 그대로 꽂을 수 있다고 가정하지 않음 |
| [Robo3R — RSS2026](https://roboticsproceedings.org/rss22/p056.html), [§III·IV-B](https://arxiv.org/html/2602.10101v1) | Robot-frame metric geometry·PnP와 실제 조작 평가. Imitation 비교는 주로 3D Maniflow, π₀는 별도 baseline | Reconstruction→조작 개선은 기존 연구. 같은 VLA에 대한 입력 geometry 효과와 구별 |
| [GeoPredict — CVPR2026](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html), [§3.3–3.4](https://arxiv.org/html/2512.16811v1)·공개 loss source | 궤적 주변 Gaussian refinement·workspace depth supervision, inference에서 decoder 생략 | ROI 중심 geometry 학습 자체는 신규성에서 제외. **Training 문서/entry/loss 공개를 이번에 확인**, 실행은 미검증 |
| [Lift3D Policy — CVPR2025](https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html), 공식 색인·[preprint §3.2](https://arxiv.org/html/2411.18623v1) | Affordance 영역의 masked depth reconstruction과 point cloud 정책 | 물체/접촉 영역에 집중하는 단순 대조 필수. Preprint의 긴 제목과 CVPR판은 동일 연구 |
| [PRISM: Precision Forcing — 2026 preprint](https://arxiv.org/html/2610.14704v1), §2–3 | 방향별 물리 허용 오차·action-error 전파, trajectory precision proxy에 따른 flow 학습 | 허용 오차 정규화·Jacobian 합성은 새 이론이 아님. Registry의 동명 depth 논문 pr-0458과 다름 |
| **[Estimate, Don't Imitate — 2026 preprint](https://arxiv.org/html/2609.34018v1)**, §III-C·V-C | Frozen expert를 통과하는 state/action 혼합 손실과 sensitivity 기반 추정 학습 | **추가 직접 충돌.** 정책에 민감한 오류를 더 학습한다는 원리와 VLA/depth 이식만으로는 신규성 부족 |
| **[Understanding the Impact of Geometric Foundation Models on VLA — ECCV2026](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2)**, [preprint §5.1·5.5·limitations](https://arxiv.org/html/2605.24642v1) | GR00T-N1.5/VGGT의 fusion·데이터·camera와 episode 평균 depth RMSE/성공률 관계 분석 | **진단에도 선행이 있음.** 동일 state의 입력 오류 개입·작업 조건 통제가 필요. 관측 상관을 인과 효과로 읽지 않음 |
| [GeomVLA — 저자 CoRL2026 표기](https://arxiv.org/html/2609.13812v2), §3·5·[project](https://ziyin-xiong.github.io/geomvla.io/) | Depth/calibration으로 scene·motion·action을 robot frame에 연결 | 통합 3D VLA 자체는 기존 기여. 공식 OpenReview 접근 제한으로 이번 확인은 저자 표기까지. Code 링크404로 필수 backbone에서 제외 |

기존 [pose 허용 오차 기반 성공 평가](https://www.emerald.com/ir/article-abstract/52/5/651/1254840/Robotic-task-success-evaluation-under-multi-modal?redirectedFrom=PDF)도 단순 tolerance baseline의 근거다. UA-Pose·[CNABU](https://roboticsproceedings.org/rss21/p039.html)는 미관측 geometry/불확실성 계보이며 이번 본문 재검토 대상은 아니다. [FlowVLA](https://arxiv.org/abs/2610.16160)는 training-only 3D flow의 인접 대조로 초록만 확인했다. ReconVLA의 2D 목표 영역 재구성을 metric 3D 방법과 혼동하지 않는다.

검색에서 발견하지 못한 조합을 미해결의 증명으로 쓰지 않는다. 11/18 후속 REG-R18에서 EDI·Geometry Impact·PRISM Precision Forcing을 각각 pr-1225/1226/1227로 등록했다. Geometry Impact의 ECCV2026 출판은 Springer에서 새로 확인했으며 과거 N1 source 기록은 당시 확인 범위로 보존한다. EDI 저자 dataset card의 ICRA2026 표기는 공식 acceptance 미확인으로 여기서 채택하지 않았다. Code 접근 실패는 미공개 사유나 과학적 반박의 증거가 아니다.

<a id="n1-question"></a>
## 기여 후보와 반박 가능한 예측

**먼저 검증할 기여 후보는 작업 조건별 geometry 오류의 통제된 분석이다.** 정책 입력에 실제로 남는 오류, 물체 영역 오류, 작업 방향별 오류가 실패를 얼마나 설명하는지 비교한다. 최종적으로 센서/표현/학습 선택을 바꾸는 결론이 있어야 하며 “정확한 깊이가 좋다”의 재확인만으로 충분하지 않다.

후속 방법 가설은 **물리적으로 일관된 깊이 보정 adapter에 작업 결과 기반 supervision을 주는 것**이다. 같은 작은 adapter·입력·train label·update 수에서 일반 depth loss, ROI loss, EDI에서 착안한 행동 일치 loss와 비교한다. 제안 신호는 행동 벡터 차이만이 아니라 고정 continuation의 task margin 감소다. Simulator를 미분 가능하다고 가정하지 않고 paired continuation label로 작은 surrogate를 학습하는 방안을 둔다. 추가 label/rollout 비용은 비교군에도 동일하게 제공한다. 이는 미구현 가설이며 독립 기여로 확정된 알고리즘이 아니다.

Test-time에는 실제 추정 오차·정답 mesh·성공 margin·fixture의 정답 허용 오차를 넣지 않는다. 깊이 수정이 물리적으로 틀린 상태를 만들어 정책을 우회하지 않는지 geometry 오차도 보고한다. 학습된 위험 점수를 보정된 성공 확률로 부르지 않는다.

| 논리 사례 — 실험 결과 아님 | 확인할 예측과 경계 |
|---|---|
| 동일3 mm 오차, 허용 폭8 mm와2 mm | 1D 정렬 모형에서는 결과를 구별할 수 있지만 수식의 신규성·실제 실패율은 아님 |
| 같은 영역/오차량, 슬롯 횡방향과 축방향 | ROI 이후 방향 의존성이 남는지. Scalar depth를 임의 XYZ 변위로 취급할 수는 없음 |
| `P(ΔD)=0`인 오류 | Area 축소 P 뒤에는 오류가 사라짐. 동일 RGB/K·결정적 실행에서 원 embedding도 같으므로 원해상도 오류를 정책에 전달됐다고 세면 안 됨 |
| 큰 action 변화지만 작업 성공 | Action consistency와 실제 결과 차이의 가능성. 빈도가 높다는 증거나 EDI의 일반 실패 증명은 아님 |
| 정답 깊이 입력에서 행동 악화 | 정확도와 학습 입력 분포를 분리. Oracle depth가 무조건 성능 상한인 것은 아님 |

최초 비교는 **고정 support·정책 입력에서의 camera XYZ RMS**를 기준으로 하고 원해상도 depth RMSE·물체 ROI 오차도 기록한다. 주입 변형량 `RMS(X′−X)`와 실제 추정 오차 `RMS(X′−X_GT)`를 구별한다. 전자만 맞추면 “같은 주입 크기” 비교이며, 실제 재구성 오차가 같다는 주장을 하려면 후자도 정해 둔 허용 범위로 맞춰야 한다. Background dilution·단위·pixel 수 차이로 만든 순위 역전은 기여가 아니다. [실제 입력 계약](../재현%20방법/README.md#geometry-contract)을 따른다.

<a id="n1-comparison"></a>
## 최소 비교와 결과별 결정

관측 단위는 `저장한 simulator state × instruction × geometry perturbation`이다. 같은 mesh·scene·seed에서 분기하고 controller/RNG/정책 history를 맞춘다. 첫 chunk만 바꾸는 영향과 매 timestep 오류가 지속되는 영향을 분리한다. 정책은 처음에는 고정하며 collision geometry는 유지한다.

| 비교군 | 목적·공정성 |
|---|---|
| 원래 ZoeDepth + 같은 VLA | 무개입·정상 동작 기준 |
| 항등 adapter | Hook/dtype/resize/cache 변경 효과 제거 |
| Global scale/bias 보정 | Calibration 한 번으로 충분한 문제인지 확인 |
| 전체/ROI depth·XYZ 오차, 고정 tolerance rule | 학습 없는 설명 대조. 정답 사용 군은 oracle 진단으로 구별 |
| 같은 adapter의 geometry-only·ROI 학습 | 용량·학습량·annotation 이득 통제 |
| 같은 adapter의 action-consistency 학습 | EDI 원리의 이식 대조이며 원 논문 재현은 아님 |
| 후보 task-margin supervision | 같은 train rollout/label budget에서 잔여 행동 이득 확인 |

GeoPredict/Lift3D의 개념을 좁게 이식한 ROI 대조와 전체 원 논문 재현은 구별한다. PRISM의 flow-time reweighting을 autoregressive SpatialVLA에 그대로 적용하지 않는다. 필요할 때 continuous-action backbone에서 별도 비교하며 먼저 범위를 확장하지 않는다.

주 지표는 release 이후 작업 성공, 목표 방향/위치/높이 margin, 접촉·충돌 실패, 시간이다. Logit KL·token likelihood·decoded action 변화는 진단 보조다. 실패 예측은 held-out object/fixture family의 ranking/calibration을 보되 label 단위를 밝힌다. 같은 mesh의 view를 독립 test object로 세지 않는다. Pair가 split을 넘지 않게 하고 episode/family 단위 신뢰구간을 사용한다. Pilot으로 큰 성능 주장을 하지 않으며 확증 표본 수는 pilot 분산으로 정한다.

| 관측 | 다음 결정 |
|---|---|
| Geometry 입력에 무반응 | Hook·표현 축소·token discretization·학습 능력을 분리. 모든 VLA/3D를 기각하지 않음 |
| 입력 반응은 있지만 기본 조작 능력 없음 | IO 진단까지만 보고. Task 시연/normalizer/finetuning 필요성을 평가하고 실패 귀속 보류 |
| Calibration·ROI·행동 일치 대조가 충분 | 새 방법 주장 축소. 중요한 원인 분석이 남으면 분석 기여 검토 |
| 작업별 잔여 차이가 여러 객체에서 반복 | 작은 task-margin adapter 비교로 진행 |
| 합성 depth 불일치에서만 효과 | 실제 reconstruction 오류·일관된 재렌더링에서 재검토; 배포 일반화 주장 금지 |

<a id="n1-story"></a>
## 짧은 논문 이야기와 석사 연구 부담

“3D 오차가 같아도 행동에 필요한 정확도는 다르다. 기존 geometry fusion·작업 영역 복원·정밀 action 학습을 바탕으로, 우리는 정책 입력에서 살아남는 오류를 동일 상태에서 개입한다. 단순 오차량과 행동 일치로 설명되지 않는 작업별 실패 구조가 있다면 제한된 geometry 학습에 반영한다. **결과·효과 크기·일반화는 미확인이다.**”

로보틱스·CV·VLA 연결은 명확하다. 반면 방법 신규성은 선행 때문에 초안보다 좁고, 기본 조작 능력·평가기·camera 정합의 부담이 있다. 첫 투자는 전체 재구성 모델 학습이 아니라 **한 checkpoint의 입력 hook과 하나의 강체 fixture**로 제한한다. 구현 일수·VRAM·성능은 측정 전 확정하지 않는다. 최종 논문에는 자연 오류와 추가 task/backbone 또는 설득력 있는 실제 로봇 검증이 필요할 수 있다.

1번보다 더 어렵거나 가능성이 낮다고 입증된 것은 아니다. 두 주제 모두 독립 방법 기여는 미확립이다. 이 주제의 새 내용상 위험은 EDI·geometry 영향 분석과의 중복이며, 구현 가능성과 효과는 작은 P0 정보로 비교한다.

<a id="n1-result"></a>
## 비실험 buildup 완료 범위와 다음 행동

| 가이드 단계 | 이번 완료 범위 |
|---|---|
| 문제·독자 | 정렬/배치의 geometry 오류와 로봇 모델 선택 문제 |
| 직접 선행 | 지정 절 검토, source/metadata21개 identity 대조와 선택 심볼 확인; 전체 파일 정독·실행과 구분 |
| 질문·대안·반례 | 질문 축소, ROI/보정/행동 일치 대조, 표현 nullspace·oracle-depth 반례 |
| 짧은 이야기 | 위 초안 작성; 결과 미확인 |
| 최소 비교 | 정보·오차 단위·paired 분기·측정·분할·결과별 결정 |
| 실행 부담 | [Depth hook·좌표·evaluator·환경·작은 P0 명세](../재현%20방법/README.md). N1 당시 구현 전이었고 아래 P0 준비에서 제한된 코드 작성 |
| 외부 비판 | “같은 label의 ROI/action loss로 충분한가?”, “실패 구조가 중요한가?”, “자연 오류에도 남는가?” 질문 준비. **실제 외부 피드백 미수신** |

N1에서 선택했던 TASK-GEOMETRY-P0-PREP의 작성 결과는 아래에 통합했다. Task 정상 능력과 방법 효과는 이후 별도 검증이며 새 N2 문헌 문서를 반복 생성하지 않는다. 자원 부족을 가설 반증으로 쓰지 않는다.

<a id="p0-preparation-result"></a>
## P0 준비 결과 — 2026-11-18

**준비 완료:** 실제 remote model의 depth/backprojection을 감싸는 개입 코드, 한 nut 장면·camera/ROI, 항등/ROI bias/area 평균 보존 순열 비교, strict loader와 2지시×4조건 probe, Docker recipe/launcher, 검사11개를 작성했다. [범위·재개 명령](../재현%20방법/README.md#resume). 원본 모델과 1번 주제의 frozen 준비 파일은 변경하지 않았다. 재사용한 모델·package 자료는 hash로 고정한다.

**내용상 보완:** 공개 loader의 tuple 반환 처리와 BF16 광선 좌표 반올림을 source/코드 검토에 반영했다. 주입 변화량과 GT 대비 실제 오차를 구별하고, 후속 token의 prefix 변화가 섞이지 않도록 첫 logits를 비교한다. Nullspace 음성 대조도 실제 수치 잔차를 남긴다. 이는 설계·구현 개선이며 실측 결과가 아니다.

**실제 확인:** Python 정적 컴파일, 현재 local Docker endpoint 확인, 새 launcher `run`의 daemon 실패 차단(exit3). Image build·Docker 검사·native scene/정책·학습·host dependency/weights 설치는 하지 않았다. 작은 입력 probe의 준비 완료를 학습된 geometry adapter나 task 실험 준비 완료로 표시하지 않는다.

**다음은 TASK-GEOMETRY-P0:** 호환 local NVIDIA에서 작성한 bounded IO를 확인한다. 성공 시에도 새 task normalizer·기본 조작 능력·release/contact evaluator·자연 오류/paired continuation·task-margin 학습은 미완료다. 현재 판단은 좁은 탐색 CONTINUE이며 신규성·성능·외부 연구자 피드백은 미확립이다.
