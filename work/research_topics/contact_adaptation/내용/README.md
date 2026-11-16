# 접촉 조작에서 VLA 강화학습과 가변 임피던스 제어

Updated: 2026-11-09 KST. **N2 내부 설계·P0 실행 자료 작성 완료 / native 검증 대기 / 좁은 탐색 유지·독립 방법 기여 미확립.** 이 문서는 [Robotics 중심 공백 탐색](../../../update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md#robotics-reorientation)의 접촉 후보를 구체화한다. [입출력·제어·환경 계약](../재현%20방법/README.md#n2-interface), [단일 source 원장 `contact_n1`·`contact_n2`](../../../sources/vla_rl_additional_gaps_2026-11-09.json), [다음 TODO](../../../../TODO.md)를 함께 본다. 계약의 수치는 앞으로 검증할 설계값이며 실행 결과가 아니다.

<a id="registry-sync"></a>

**11/09 registry 연결:** 직접 선행 10편을 [REG-R13 등록 표](../../../update/REGISTRY_MAINTENANCE_2026-11-09.md#admissions)에 연결했다. 새 paper별 5-note는 ABSTRACT_CHECKED이고, 아래 지정 절·버전의 본문 대조를 대신하지 않는다. 특히 [CompVLA v2](https://arxiv.org/abs/2609.23614v2)와 [TORL-VLA v3](https://arxiv.org/abs/2606.09337v3)의 최신 초록을 확인했지만 N1 표는 v1 본문 근거다. P1/신규성 주장 전 버전 간 방법·평가 변경을 확인한다. FORGE는 같은 preprint의 RA-L 2025판으로 등록했고 TacCoRL/CompVLA의 저자 CoRL 표기는 공식 채택으로 승격하지 않았다.

## 현재 판단

**로봇이 물체에 닿은 뒤 어떻게 움직이고 힘을 전달할지를 학습하는 Robotics 문제다.** 다만 ‘접촉 이력 + 단일 VLA + RL + 강성 출력’을 조합한 것만으로 새 연구 방법을 주장할 근거는 부족하다. 촉각 VLA 자체의 RL, 동작·강성 공동 생성, action–wrench 가치 학습, 동작·강성 공동 RL이 각각 가까운 선행에 있다. 코드 부족이나 GPU 부재 때문에만 기여가 불명확한 것이 아니다.

작은 비교를 시작할 가치는 남는다. **같은 RGB·로봇 상태·손가락 접촉력 이력에서, 단일 π₀의 동작과 관절 강성 배율을 함께 RL로 학습하면 동작만 학습하는 경우보다 삽입 저항 변화에 잘 대응하는가?** N2에서는 공개 제어 경로에 맞춰 **관절 구동 강성의 한 개 배율**로 한정했다. Cartesian 방향별 impedance·6D wrist wrench를 사용하는 실험으로 표현하지 않는다. 유용한 차이가 있으면 언어·물체·작업 간 공유로 확장한다. 이는 **연구자 가설(CURATION-HYPOTHESIS)**이며 선행이 답하지 못한 것으로 확정한 공백이나 출판 가능성 보장이 아니다.

선택한 범위는 하나의 학습된 VLA 행동 정책이다. 고정 servo·좌표 변환·안전 제한은 실행 계층으로 허용한다. 별도 학습된 planner/skill/residual 연결은 강한 비교군이며 제안의 필수 구조로 삼지 않는다. 기존 [GAP-CONTACT 센서 필요성 진단 HOLD](../../../../synthesis/03_manipulation_contact.md#gap-contact-2026)를 재개하지 않는다.

<a id="prior-comparison"></a>
## 직접 선행 비교

8편의 지정 HTML 본문/부록, 추가 1편의 초록을 확인했다. 전체 논문의 정독이나 모든 구현의 재현은 아니다. 아래 수치·입력은 논문별 조건이며 서로 다른 성공률을 합산하거나 순위로 쓰지 않는다.

| 선행·확인 구간 | Actor 입력·이력 | 학습 대상·출력 | 실행·시간 | 이미 다룬 변화·필수 대조 |
|---|---|---|---|---|
| [TacCoRL](https://arxiv.org/html/2606.11743v1), §3–4·App. A–E | RGB·언어·proprio·10개 촉각 샘플; normal taxel | VLA 자체를 Flow-SDE/PPO와 real SFT로 학습; 14D motor chunk, H=10 | 사전 동정한 joint impedance; 학습된 gain 출력과 다름 | 마찰 DR·물체 변화, tactile IL/RL 비교. 이력·단일 VLA RL 자체는 선행 |
| [CompVLA](https://arxiv.org/html/2609.23614v1), §3–5·7·App. A | RGB·언어·TCP/gripper; 평가 actor에 force 입력 없음 | 동작·compliance experts의 flow-matching IL; twist/gripper + stiffness + virtual displacement | geometric impedance; H=25, servo Hz는 지정 구간에서 미확정 | fixed stiffness·displacement 제거 비교. 같은 힘을 만드는 stiffness–displacement 조합의 비유일성 명시 |
| [TORL-VLA](https://arxiv.org/html/2606.09337v1), §3·4.1·App. A.2–3 | 영상·상태·fingertip 12D wrench; 2초 내 10개 이력 | frozen VLA/reference·stage estimator; 단계별 actor/critic 학습, action chunk 보정 | 20Hz, H=50/K=10; 약 0.5초 재계획 | unseen friction·soft cup까지 평가. 현재 구조를 단일 actor나 항상 additive residual로 부르지 않음 |
| [ForceRFT](https://arxiv.org/html/2609.22840v1), §III–IV·구현 부록 | 상태·실측 6D wrist wrench·시간 정규화 변화·base action | frozen force-conditioned SmolVLA + bounded 6D pose residual RL | base H=50; 명목 residual 10Hz, model 시간축 30Hz와 구별 | autonomous TD / human residual imitation 분리; residual imitation도 직접 기준선 |
| [FORGE](https://arxiv.org/html/2408.04587v2), §II–III | noisy pose/velocity·추정 force·fixture pose·직전 action·force limit | 비-VLA RL; x/y/z/yaw target | impedance gains·action scale는 dynamics randomization | force ceiling·물리 불확실성·접촉 조립. 고정 controller+RL의 강한 비교군 |
| [Facet-0](https://arxiv.org/html/2609.01596v1), §4–6 지정 부분 | RGB·언어·kinematics·10개 wrist-wrench 이력 | action 7D + 예측 wrench 6D 공동 생성, value-guided post-training; 별도 local adaptation | coarse/refine 두 expert; adaptation은 frozen 표현의 bounded Cartesian actor | action/contact 가치와 contact credit도 선행. **예측 wrench는 힘 명령이 아님**, 전체 시스템은 단일 actor가 아님 |
| [CG-RL](https://arxiv.org/html/2609.13516v1), §III–V 지정 부분 | geometry/state·contact feedback·applied gain·force limit | PPO actor가 residual pose·advance rate·gain 요청 | CAD primitive + gain projection/rate limit + operational-space controller | friction/관측 변화·fixed gain·projection 영향 분석. GT fixture와 scripted phases를 쓰는 비-VLA simulation 연구 |
| [ContactBench](https://arxiv.org/html/2610.24512v2), §III-C/D·공개 task source | 정책 방법이 아니라 접촉 task/asset 자원 | 실물 접촉 benchmark와 simulation 자산 | 공개 scripted rollout을 VLA 학습 환경으로 간주할 수 없음 | 자연 저항 변화·task 성공 정의의 출발점; 아래 한 과제로 한정 |
| [CompliantVLA-adaptor](https://arxiv.org/html/2601.15541v2), N1 초록·**N2 §III/IV 지정 본문 추가** | image/language·외력; VLM phase 추정 | frozen VLM의 gain 제안 + 측정 force에 따른 gain 축소 | 약 1Hz VLM / 3Hz VLA / 1kHz VIC | 단순 force 기반 가변 gain도 빠뜨릴 수 없는 대안. 공개 code는 이번에 미검토 |

**출판 상태:** FORGE는 RA-L 2025 출판사 근거를 이전 scout에서 확인했다. CompVLA·TacCoRL의 CoRL 2026은 저자 표기이며 공식 paper별 채택은 미확인이다. 나머지 이번 상세 비교의 2026 논문은 arXiv 근거이며 verified top-tier로 승격하지 않는다. 공식 CVPR 2026 ForceVLA2·AT-VLA, RSS 2025 ConRFT 등 기존 배경은 [scout 원장](../../../sources/vla_rl_additional_gaps_2026-11-09.json)의 R02/R04/R05에 보존했다. Top-tier 배경이 있어도 최신 직접 중복을 preprint라는 이유로 제외하지 않는다.

**이번에 철회한 넓은 주장:** 이력 기반 단일 VLA RL의 부재, 물성 변화 평가의 부재, 동작·강성 공동 RL의 부재, 정책과 controller 효과를 분리하는 분석의 부재. 위 선행 이후 남는 차이는 실제 같은 조건의 비교와 VLA의 공유 능력에서 찾아야 한다.

<a id="task"></a>
## 첫 자연 과제: 충전 블록을 꽂고 손을 떼기

ContactBench의 **Plug in charger, charging block 1** 자산에서 **삽입 후 손 떼기**를 첫 과제로 정했다. 물체를 잡고 단자 가까이에서 시작하며 방 탐색·집기는 포함하지 않는다. N1에서 인용한 공식 성공 조건에는 추가 누름 시험도 있지만, N2의 첫 비교는 **완전 삽입·손 이탈·놓은 뒤 안착 유지의 부분 과제**다. 사후 scripted 누르기가 덜 꽂힌 물체를 대신 삽입하는 것을 피하기 위해 누름 시험을 빼며, 결과를 공식 ContactBench 전체 성공률로 보고하지 않는다. [공식 task 설명](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/docs/tasks.md#22-plug-in-charger)

물리적 변화는 **같은 소켓의 접촉 스프링 저항**이다. 도중에 마찰 계수를 바꾸지 않고 접촉 기구에 의해 저항이 생기게 한다. 물체 형상은 block1로 고정하며 **0.4mm 조건에서 학습·개발, 0.85mm는 학습/정책 선택에 쓰지 않는 평가 조건**으로 예약했다. 두 값은 공개 기구 모델의 측정 기반 fit이며 실제 block1 전이의 검증은 아니다. 보간/외삽된 다른 spring 값은 첫 비교에서 제외한다.

**자연 실패의 후보와 반론:** 강한 저항에서는 pinch가 미끄러져 삽입이 멈출 수 있다. 그러나 공개 `ChargerBlockVariant`는 이를 감지하면 손을 열고 위로 옮긴 뒤 블록 상단을 누르는 scripted 해결책을 이미 사용한다. 따라서 실패를 ‘VLA가 강성을 학습하지 못해서’라고 단정하지 않는다. 실제 원인은 grasp 한계·행동 방식 변경·자세 오차일 수 있다. 위에서 누르는 행동을 제안에만 허용하고 비교군에는 금지하면 불공정하다. [해당 source의 `ending`·`_press`](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/appendix_tasks/plug_in_charger_blocks.py)

이 과제는 단일 VLA의 이점을 입증하는 benchmark가 아니라 **현상과 구현 비용을 먼저 확인하는 작은 출발점**이다. 고정된 삽입 목표 하나의 향상만으로 언어 이해·generalist transfer·다양한 로봇 일반화를 주장하지 않는다.

<a id="comparison-plan"></a>
<a id="n2-contract"></a>
## N2: 최소 비교 계약

**선택 경로:** RLinf의 PyTorch π₀ + Flow-SDE/PPO. VLM은 고정하고 state/action projection과 action expert를 학습한다. Critic은 학습에만 쓰며 실행 시 하나의 VLA actor가 동작·gain을 함께 생성한다. 공개 [π₀ 설정](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/examples/embodiment/config/model/pi0.yaml)과 [RL 구현](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/models/embodiment/openpi/tasks/rl.py)을 고정했다. 새 알고리즘 제안이 아니라 비교에 사용할 기존 학습 경로다.

초기 weights는 `RLinf/RLinf-Pi0-LIBERO-Spatial-Object-Goal-SFT`로 선정했다. **초기화 용도**이며 charger 능력을 보장하지 않는다. 목표 과제의 시연·관측 변환·normalizer로 공통 SFT 시작점을 새로 만들어야 한다. Source/HF revision·원격 LFS hash는 확보했지만 weights·target 데이터는 미확보다. LIBERO 통계나 checkpoint 이름을 새 task의 재현 증거로 쓰지 않는다.

### 무엇을 비교하는가

N1의 2×2 전수 비교는 **공통 SFT → 두 RL 조건**으로 축소했다. 공개 시연에는 가변 강성 label이 없어 ‘공동 imitation’ 비교군을 이미 확보한 것으로 둘 수 없기 때문이다.

| 조건 | 같은 VLA가 학습/실행하는 것 | 역할 |
|---|---|---|
| S0 | 공통 task SFT, 개발 집합에서 선정한 고정 gain α₀ | 추가 상호작용 전 성능·원점 |
| M | 동작 RL, 실행 gain은 α₀ 고정 | 주 비교군 |
| J | 동일 RL 경로, 동작 + arm gain 배율 실행 | 제안할 가치가 있는지 보는 조건 |
| R — J에 이득이 있을 때 필수 후속 | 동작 RL + 동일 fingertip force에서 정한 규칙 gain; 별도 학습 actor 없음 | 단순 순응 제어로 충분하다는 설명을 검토. 개발에서 정한 규칙을 학습/평가 모두에 적용 |

M/J는 동일한 32D 내부 head에서 같은 8개 좌표를 생성하고 같은 logprob 차원을 사용한다. M의 마지막 gain 요청은 실행에서 무시하고 기록만 한다. 이는 ‘gain을 실제로 사용할 권한’의 비교이며, M의 무시된 좌표가 shared denoising이나 gradient 분산에 전혀 영향을 주지 않는다는 뜻은 아니다. **J가 이기면 7D scoring을 쓰는 motion-only 대안과 R을 추가 확인한 뒤 기여를 판단**한다. 이 단계 없이 인과적인 gain 학습 우월성을 주장하지 않는다. 재현 문서에 logprob 합산·단일 denoising-step surrogate의 한계를 명시했다.

R의 출발 규칙은 `α_request = clip(α₀ / (1 + max(0,F_tip−10)/20), 0.25, 1)`로 두고, `F_tip`은 actor와 같은 causal mean의 두 fingertip force norm 중 큰 값(N)이다. J와 같은 gain rate limit을 적용한다. 10N/20N은 **미교정 설계값**이며 개발 조건에서만 바꾸고 평가 전에 동결한다. 손가락 pinch force를 환경 접촉력과 혼동하지 않는다. 이 한 규칙이 모든 고전 순응 제어를 대표한다는 주장은 하지 않는다.

첫 추정 대상은 **동일한 simulation 상호작용 예산에서 M/J 학습 절차의 최종 성능 차이**다. 정책별 방문 상태가 달라지므로 같은 데이터에서 objective만 바꾼 효과가 아니다. 후자의 확인이 필요해지면 양쪽의 train-only 자료 합집합을 고정해 성공 시연 선택·return-weighted imitation을 추가한다. 성공만 골라 쓰더라도 실패·reset·필터링 비용은 삭제하지 않는다. 추가 시연만으로 J의 이득이 설명되면 RL 방법 주장을 축소한다.

### 관측·행동 권한

Actor/critic은 RGB 한 뷰, 고정 언어 지시, 실제 robot q/qd, 두 손가락의 접촉 합력과 직전 이력, 적용 gain만 본다. 물체 pose·삽입 깊이·spring label·expert phase·성공 flag는 **evaluator/reward 전용**이다. 접촉력은 시뮬레이터의 이상적 fingertip 합력이며 실제 wrist F/T나 GelSight 압력 영상이 아니다. 원 데이터 배열의 `observations[:,18:]`에는 정답 물체 pose가 들어 있어 그대로 model에 넘기지 않는다. [공개 수집 schema](https://github.com/Michaelwyx/contactbench-sim/blob/ccd864501275112e369a71c91880adf2da28b536/packages/force-bench/src/force_bench/data/collection.py)

모두에게 TCP 이동·회전, gripper 열기/닫기를 허용한다. 잡기를 풀고 위에서 누르는 행동도 같은 권한 안에서 가능하며, J에만 허용하지 않는다. 기존 source의 expert phase·정답 depth feedback·자동 `ending`은 정책 실행에서 제거한다. Source의 stabilizer는 **기본값부터 꺼져 있음**을 본문보다 코드에서 확인했다. 비교에서는 `TB_STABILIZER=0`·추가 weld 없음·effort override 없음으로 고정한다.

### 분할·비용·평가 — 실행 전 설계값

| 항목 | N2 선택 |
|---|---|
| Task | FR3·block1·삽입 후 release; train/dev spring0.4mm, evaluation ID0.4mm/OOD0.85mm |
| Reset | 단자를 소켓 위에서 잡은 상태. Fixture xy 각각 ±0.5mm, yaw ±1°의 동일 분포. 유효 collision-free reset 구현/확인은 미완료 |
| Seed 예약 | 시연/train 0–63, controller 개발 1000–1031, 정책 평가 2000–2031. 이 번호 자체는 실제 state 독립성 증거가 아니며 생성 후 state/asset hash로 중복 검사 |
| 공통 SFT | 최대 64회 train 시연 시도에서 성공 자료를 사용하고 실패도 비용/기록 보존. 가변 gain 라벨을 역산하지 않고 실제 고정 α₀를 기록. 실제 데이터 0 |
| 개발·controller 선택 | α₀ 후보 {0.25,0.5,1}을 **0.4mm 개발 조건에서만** 고르고 SFT 수집 전에 동결. 이후 M의 gain/속도 재튜닝이 J와 동등하면 공동 학습 기여 축소 |
| RL pilot 계획 | 같은 SFT에서 seed {11,22,33}; M/J 각각 seed당 총 simulation 960초 상한, reset·pre-roll·실패·후처리 포함. 성공 횟수나 완료 episode 수를 예산으로 맞추지 않음 |
| 학습 기본값 | Flow-SDE 4 denoising steps, noise0.5, PPO clip0.2, GAE γ0.99/λ0.95, actor LR5e-6 / critic LR1e-4. 기존 예제에서 출발하는 **미교정 설계값**, 실행 승인 아님 |
| 평가 | S0/M/J별 32개 초기 조건 × 두 spring. RL 3 seed 결과를 따로 보고 paired 초기 조건을 맞춤. 공통 SFT의 랜덤성까지 평가한 실험은 아님 |
| 시간 | policy 10Hz·한 action만 실행, 최대15초 + release 뒤0.5초 수동 제어 없는 관측. 고정 deadline에서 종료하지 못하면 실패 |
| 주 결과 | 제한시간 내 완전 삽입·손 이탈·안착 유지와 최대 환경 접촉력40N 이하의 성공률 차이 J−M. 40N은 simulation 비교용 설계 한도이며 실물 안전값 아님 |
| 함께 보고 | 제한 없는 성공률, force budget {20,40,60}N별 성공, peak·초과력 적분, 완료시간, slip·위에서 누르기 빈도, actuator saturation, invalid/reset/retry 수, 실제 GPU/벽시계 시간 |

기하 성공은 seat gap≤0.5mm, 손의 접촉 해제·4cm 이상 이탈, 뒤0.5초 동안 depth 변화≤0.5mm로 정의한다. 원 `criteria`의 scripted phase window는 사용하지 않는다. **환경 접촉력**은 object/fixture 접촉쌍의 합력 벡터의 norm이며 gripper pinch force와 분리한다. 반대 방향 힘의 상쇄를 놓치지 않도록 접촉별 normal force와 penetration도 함께 보고한다. 이 지표는 손상·안전 보증이 아니다. 60Hz 로그를 무조건 연속 시간 peak로 부르지 않는다. Physics substep에서 힘을 읽는 경로를 P0에서 확인하고 불가능하면 sample rate와 누락 위험을 반영해 지표/계약을 **학습 전에** 개정한다.

보상 초안은 연속 depth 진전의 potential difference와 terminal success를 쓰되, 초과력·시간·물리 guard 실패를 함께 벌점으로 둔다. 구체식은 source 원장의 `contact_n2.contract.reward`에 고정한다. Terminal success 보상은 기하 성공에 주며 힘 제약 성공률은 별도로 평가한다. 유한 horizon 종료의 potential은0으로 두고, 예산 중단은 성공/실패 terminal과 구별한다. Depth를 reward/평가에 쓰는 것은 허용하지만 actor/critic 입력으로 전달하지 않는다. 잘못된 접촉 수치나 성공 판정 오류를 policy 효과로 셈하지 않는다. Workspace·joint/effort limit과 접촉 buffer integrity의 수치/flag 연결은 P0에서 정할 구현 조건으로 남는다.

추정은 seed별 paired 성공률 차이와 force/time 분포를 우선한다. Seed가 3개인 pilot에서 작은 p-value나 정밀한 일반화 확률을 주장하지 않는다. **사전 관심 효과는 OOD 성공 +10%p**이고 ID 성공 −5%p보다 큰 악화나 force/time 증가가 있으면 다음 단계 근거가 약해진다. 이는 power를 보장한 판정선이 아니다. 효과가 작거나 불확실하면 축소/추가 관측을 선택하며 연구가 거짓이라고 단정하지 않는다.

### 결과에 따른 다음 판단

- M 또는 R의 gain/속도·힘 반사 조정으로 충분하면 공동 action head의 필요성 주장을 축소한다.
- 차이가 grasp slip→top press 전환에서만 생기면 impedance 학습과 동작 전략 선택을 분리한다. 강성 조절이 더 높은 pinch force를 허용한 결과인지도 확인한다.
- J가 같은 비용·권한에서 개선되더라도 한 삽입 task만으로 VLA나 언어의 필요성은 입증되지 않는다. 후속에 다른 물체/지시와 기존 비접촉 능력 유지가 필요하다.
- Native gain 변경·관측 시간 정렬·기본 SFT competence가 확인되지 않으면 학습 sweep으로 넘어가지 않는다. 이는 실행/비교 전제의 실패이며 연구 가설 반증이 아니다.

## 석사 연구로서의 가능성과 부담

로봇의 실제 접촉 성능과 직접 연결된다는 점은 강점이다. 반면 가까운 방법이 많고 force/controller 공정 비교와 실물 검증 부담이 커서 **현재 독립 방법 논문 후보로 확정할 수준은 아니다**. 실험 전부터 개선을 입증할 필요는 없지만, 작은 비교가 기존 설명과 무엇을 구별하는지는 분명해야 한다.

현 단계에서 과도한 새 네트워크보다 한 task의 관측·행동·controller 계약을 만드는 것이 타당하다. 실물 확장에는 힘 또는 촉각 센서만이 아니라 로봇의 실행 interface, 시간 정렬·보정, 동일 fixture와 접촉 조건, 자율 trial/reset 비용이 필요하다. 실제 하드웨어 접근권·일정·비용은 확보하지 않았다. GPU 확보만으로 이 부담이 해결되지 않는다.

<a id="buildup-status"></a>
## 비실험 buildup 상태와 다음 행동

[저장소 7단계 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 적용했다. N2는 내부의 문제·문헌·비교·실행 요구를 구체화한 단계다. 실제 외부 피드백과 native feasibility·연구 효과는 미확인이다.

| 단계 | 이번 완료 범위 | 남은 것 |
|---|---|---|
| 1. 문제·독자·의미 | 접촉 삽입의 동작/impedance 학습, robot learning 독자 | VLA 공유 능력까지 필요한 자연 확장 |
| 2. 가장 가까운 선행 | N1 8편 지정 본문·1편 초록 + N2 CompliantVLA 방법, RLinf/ContactBench/Newton 선택 source | 전체 정독·모든 baseline 재현은 미완료 |
| 3. 질문·대안·반례 | 조합 신규성 제외, grasp/controller/data 설명 구분, 동일 권한의 M/J·조건부 R 계약 | 실제 현상·단순 대안 이후 효과 |
| 4. 예상 기여·paper story | 조건 분석 후 필요한 경우 방법 확장 | 차별적 현상·효과는 미관찰 |
| 5. 최소 비교·판단 | 한 task 부분 과제·M/J·split·cost·metric·pilot 기본값과 축소 규칙 | source를 실제로 연결한 calibration·표본/효과 확인 |
| 6. 실행 부담 | source/weight metadata pin·P0-A 상한, physics recipe·bounded probe/launcher 작성·Docker stdlib16검사 | native image/payload·sensor/gain 검증·전체 collector/task adapter·실물 |
| 7. 외부 비판 | 검토 질문 준비 | 실제 독립 피드백 0; 외부 발송 없음 |

**P0-PREP 완료·다음 GAP-CONTACT-RL-P0-A는 자원/native 검증 대기다.** [실제 확인](../재현%20방법/README.md#preparation-history)에서 Mac ARM64 local Docker의 NVIDIA allocation이 exit125로 실패했다. Physics recipe·제한된 sensor/controller probe·launcher를 작성하고 Docker stdlib16검사를 통과했다. [재개 경로](../재현%20방법/README.md#resume)는 호환 local NVIDIA에서 `check → build → prepare → p0`다. Native build·force/RGB/gain과 정책 효과는 미검증이다. P0-A의 joint target hold/gain ramp는 N2의 동작·강성 학습 실험이 아니며, 전체 task adapter·시연/SFT·VLA IO는 이후 별도다. 새 방법 기여 미확립·좁은 탐색 유지 판정은 그대로다.

외부 검토 질문은 “비-VLA variable-impedance RL 이후 VLA에 남는 의미 있는 이득은 무엇인가?”, “고정 gain/속도 조정과 위에서 누르기가 이미 충분하지 않은가?”, “이 비교가 실제 로봇의 controller 선택을 바꿀 수 있는가?”다. 답을 미리 확보해야 작은 탐색을 허용하는 gate로 쓰지는 않는다.
