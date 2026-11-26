# VLA의 행동 공간과 접촉 제어

2026-11-25 기준. 이 조사의 질문은 시각·언어 정책이 **어디로 움직일지, 얼마나 세게 상호작용할지, 언제 다음 단계로 넘어갈지** 가운데 무엇을 직접 결정하는가이다. 이전에 비교한 28편에서 출발해 기반 모델의 원문, 후속 논문의 초기화·배포 방식, 같은 장비에서 비교한 결과를 다시 확인했다. [기존 28편의 행동 공간과 실행 제어기](../synthesis/04_vla.md#vla-action-interfaces)

**현재 판단.** 접촉 조작에서는 목표 힘·강성을 행동에 넣는 연구와 촉각으로 실행 중인 운동을 고치는 연구가 뚜렷하다. Tactile-VLA처럼 한 정책이 두 가지를 모두 수행하는 사례도 있다. π0와 π0.5는 이 연구들이 재사용한 기반이고, 가변 강성을 시연에서 배우는 접근은 π0가 공개되기 전에도 있었다. [Tactile-VLA](https://arxiv.org/html/2507.09160#S2) · [Adaptive Compliance Policy](https://arxiv.org/abs/2410.09309)

## π0와 π0.5의 역할

**π0와 π0.5는 이 주제의 핵심 기반 논문이다.** π0는 시각·언어 표현에 연속 행동을 생성하는 전문가를 붙이는 설계를 제공했다. π0.5는 같은 모델이 하위 지시를 정하고, 그 지시에 맞춰 실물 로봇의 양팔과 베이스를 함께 움직이는 사례를 제공했다. 후속 접촉 연구에서는 두 모델의 가중치를 실제로 가져다 쓴 사례까지 확인된다. [π0 · RSS 2025](https://www.roboticsproceedings.org/rss21/p010.html) · [π0.5 · CoRL 2025](https://proceedings.mlr.press/v305/black25a.html) · [CompVLA 부록 A](https://arxiv.org/html/2609.23614#A1) · [FTP-1 부록 D](https://arxiv.org/html/2606.13102#A4)

| 기반 | 원문에서 확인한 설계 | 후속 연구에서 무엇을 이어받았나 |
|---|---|---|
| **π0** · 2024년 10월 첫 공개, RSS 2025 | 다중 RGB·언어·관절 상태를 받아 PaliGemma와 조건부 플로 매칭 행동 전문가가 50스텝의 연속 행동 청크를 생성한다. 청크 길이는 한 번에 예측하는 스텝 수다. | **CompVLA**는 공개 `pi0_base`로 초기화하고 행동 전문가의 가중치를 복사해 강성을 내는 전문가를 만든다. **Tactile-VLA**도 공통 부품을 π0 가중치로 초기화하고 촉각·힘 출력을 붙인다. [π0 §IV](https://arxiv.org/html/2410.24164#S4) · [CompVLA 부록 A](https://arxiv.org/html/2609.23614#A1) · [Tactile-VLA 방법](https://arxiv.org/html/2507.09160#S2) |
| **π0.5** · 2025년 4월 첫 공개, CoRL 2025 | 표준 사전학습 VLM에서 시작해 서로 다른 로봇·의미 과제를 이산 토큰으로 공동 학습하고, 후속 학습에서 연속 플로 행동 전문가를 갖춘다. 같은 모델이 생성한 하위 지시를 조건으로 양팔·그리퍼·몸통과 3축 베이스 속도를 함께 출력한다. 기체별 18~19차원, 50 Hz 추종이다. | **FTP-1**은 시각 인코더·언어 토크나이저·시각언어 전문가·행동 전문가를 π0.5에서 초기화하고 촉각 전문가를 더한다. **N₀-VTLA**도 공개 π0.5 가중치에서 시작한다. π0.5는 이동 조작의 기준인 동시에 촉각 정책의 실제 출발점이다. [π0.5 §IV–V](https://arxiv.org/html/2504.16054#S4) · [FTP-1 부록 D](https://arxiv.org/html/2606.13102#A4) · [N₀-VTLA §5](https://arxiv.org/html/2607.23782#S5) |

두 모델 앞에는 별개의 기술 계보가 있다. **RT-2**는 웹 지식을 배운 VLM의 토큰 공간으로 로봇 행동을 예측했고 **Diffusion Policy**는 실행할 연속 행동열을 시각 조건부로 생성했다. **Octo**는 여러 기체에 전이하는 범용 정책에 확산 행동 헤드를 썼다. 힘과 운동을 나눠 제어하는 원리는 Raibert·Craig의 혼합 위치·힘 제어와 Hogan의 임피던스 제어로 거슬러 올라간다. 최근 논문에서 새로 물어야 할 것은 이런 제어량 중 **어떤 값을 언어·접촉 이력에서 학습하고, 어느 축과 시점에 바꿀 수 있는가**이다. [RT-2](https://proceedings.mlr.press/v229/zitkovich23a.html) · [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) · [Octo](https://octo-models.github.io/) · [Raibert·Craig, 1981](https://doi.org/10.1115/1.3139652) · [Hogan, 1985](https://doi.org/10.1115/1.3140702)

## 정책이 결정하는 물리량

| 갈래 | 정책에서 하드웨어까지 | 대표 사례와 확인 범위 |
|---|---|---|
| **목표 힘·강성·감쇠** | 목표 손목 힘·모멘트, 손끝 힘, 강성 또는 감쇠가 출력에 있다. 하위 제어기는 힘 오차나 위치 오차를 줄인다. | **ForceVLA2**는 자세·목표 손목 wrench·접촉 단계 진행도를 함께 낸다. 단계 목록은 주어진다. **CompVLA**는 6축 강성과 가상 변위를 출력하고 감쇠는 강성에서 계산한다. **PaCo-VLA**는 질량·감쇠·강성을 각각 제안하며 별도 수동성 필터가 최종 적용값을 정한다. [ForceVLA2 §3](https://arxiv.org/html/2603.15169#S3) · [CompVLA §4](https://arxiv.org/html/2609.23614#S4) · [PaCo-VLA §IV](https://arxiv.org/html/2606.00515#S4) |
| **촉각·힘 피드백** | 현재 접촉을 읽고 다음 운동을 고른다. 반응 주기는 센서가 값을 내는 빈도와 정책이 새 값을 읽어 행동을 바꾸는 빈도에 좌우된다. | **ForceVLA**는 측정한 손목 힘·모멘트를 행동 생성에 넣는다. **AT-VLA**는 촉각 변화에 빠른 경로를 열어 느린 시각·언어 추론 한 번당 최대 세 번 행동을 갱신하는 설정을 평가한다. 손목의 순힘과 손가락의 국소 미끄러짐은 서로 다른 정보를 준다. [ForceVLA §3](https://arxiv.org/html/2505.22159#S3) · [AT-VLA §3](https://arxiv.org/html/2605.07308#S3) |
| **관절 속도·토크와 전신 균형** | 손목의 목표 모멘트, 관절의 목표 토크, 모터가 받는 전류는 서로 다른 명령이다. 전신 정책이 관절 목표를 정하고 단순 PD가 이를 추종하는 구조도 있다. | **Bi-LAT/Bi-VLA**는 관절각·각속도·토크 참조를 예측하고 양방향 제어기가 모터 전류를 계산한다. **HumanVLA**는 시뮬레이션에서 단일 정책이 28개 관절 목표를 30 Hz로 내며 걷고 운반한다. 실물 **Opt2VLA**의 VLA는 손발 waypoint·목표 법선력을 내고 균형은 별도 RL 제어기가 맡는다. [Bi-LAT](https://arxiv.org/html/2504.01301#S3) · [Bi-VLA](https://arxiv.org/html/2509.18865#S3) · [HumanVLA](https://arxiv.org/html/2406.19972) · [Opt2VLA](https://arxiv.org/html/2609.23968#S3) |
| **이동·태스크 전환** | 상위 지시와 운동을 같은 모델에서 차례로 생성하는 것, 같은 시점에 베이스와 팔을 움직이는 것, 이산 행동 중 하나를 고르는 것은 서로 다른 능력이다. | **π0.5**는 하위 지시를 생성한 뒤 베이스·팔을 함께 명령한다. **SPOC**는 매 스텝 이동·조작·완료 중 하나를 택하며 실물 마지막 집기는 휴리스틱이 보조한다. **OneTwoVLA**는 추론/행동 시점을 선택하지만 실물 평가에서 베이스는 고정했다. [π0.5 §V](https://arxiv.org/html/2504.16054#S5) · [SPOC](https://arxiv.org/html/2312.02976) · [OneTwoVLA](https://arxiv.org/html/2505.11917) |

**힘을 예측한다는 말에는 세 가지 뜻이 있다.** 측정한 힘은 지금 무슨 일이 일어나는지 알려주는 **입력**이다. 예측한 미래 힘은 이 동작을 하면 어떤 힘이 생길지 나타내는 **예상 결과**다. 목표 힘은 추종 제어기에 보내는 **명령**이다. ForceVLA, Facet-0, ForceVLA2가 각각의 사례다. 코드에서도 플로 헤드가 출력한 수치의 물리적 단위는 배포 인터페이스가 정한다. 예를 들어 openpi의 DROID 예제는 관절 속도와 그리퍼 위치 모드로 로봇을 연다. [ForceVLA](https://arxiv.org/html/2505.22159#S3) · [Facet-0 §4.2·5.3](https://arxiv.org/html/2609.01596#S4.SS2) · [ForceVLA2](https://arxiv.org/html/2603.15169#S3) · [공식 DROID 실행 코드](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/droid/main.py#L79-L80)

**강성의 학습에는 별도의 식별 문제가 있다.** 한 축에서 천천히 누르면 힘의 크기는 대략 강성과 평형점에서 벗어난 거리의 곱이다. 팔이 실제로 멈춘 위치와 힘만 기록했다면, 같은 접촉을 높은 강성·작은 변위와 낮은 강성·큰 변위가 모두 설명할 수 있다. CompVLA는 측정 힘에 따른 규칙으로 강성 시연값을 구성한다. **Compliance for Free**는 양방향 시연에서 조작자가 움직인 쪽의 자세를 의도한 평형점으로 간주하고, 변위·힘이 충분해 강성을 식별할 수 있는 축과 시점에만 학습 손실을 준다. 두 정책 모두 강성을 내지만 그 값에 대해 시연이 주는 근거가 다르다. [CompVLA 부록 B.2](https://arxiv.org/html/2609.23614#A2.SS2) · [Compliance for Free §III-A–C](https://arxiv.org/html/2609.19976#S3.SS1)

## 추가 조사

기존 28편의 비교표에 없던 아홉 편을 대조했다. 다섯 편은 원장에 있었고, 아래 네 편은 정책 입력·출력과 실물 비교 조건을 확인해 추가했다. [ACP 노트](../2025/ICRA/2025_ICRA_Adaptive-Compliance-Policy-Learning-Approximate-Compliance/01_overview.md) · [FTP-1 노트](../2026/CoRL/2026_CoRL_FTP-1-A-Generalist-Foundation-Tactile-Policy-Across-Tactil/01_overview.md) · [HapticVLA 노트](../2026/IROS/2026_IROS_HapticVLA-Contact-Rich-Manipulation-via-Vision-Language-Ac/01_overview.md) · [N₀-VTLA 노트](../2026/arXiv/2026_arXiv_N-VTLA-Scaling-Vision-Tactile-Language-Action-Model-with-L/01_overview.md)

| 연구 | 원문에서 확인한 내용 | 이 방향에 주는 근거 |
|---|---|---|
| **Adaptive Compliance Policy (ACP)** · ICRA 2025 | RGB·말단 자세·힘 이력으로 확산 정책이 참조 행동과 강성을 생성한다. 시연에서 모든 축의 강성을 복원하기 어려워, 힘 방향에서 순응성을 근사한다. 물체 뒤집기 5조건, 방법당 총 100회에서 ACP는 96/100, 균일 강성의 compliant policy는 23/100이었다. | 가변 강성을 학습한 시각운동 정책의 직접 선행이다. 첫 공개는 **2024년 10월 12일**, π0는 **10월 31일**이다. CompVLA의 기여를 볼 때는 언어·범용 정책에 추가한 부분과 시연에서 강성을 정한 방법을 따로 봐야 한다. [ACP §III–IV](https://arxiv.org/html/2410.09309#S3) · [ACP 공개일](https://arxiv.org/abs/2410.09309) · [π0 공개일](https://arxiv.org/abs/2410.24164) |
| **Reactive Diffusion Policy (RDP)** · RSS 2025 | 느린 확산 정책이 잠재 행동 청크를 만들고, 빠른 디코더가 청크 실행 중 새 촉각을 20~30 Hz로 읽어 동작을 수정한다. | 시각·촉각 모방학습만으로 비교할 수 있는 기준이다. Fast–Slow VLA의 이득 중 얼마가 빠른 접촉 피드백에서 오는지 분리할 수 있다. [RSS 논문](https://www.roboticsproceedings.org/rss21/p052.html) · [제어 구조 §IV-B](https://arxiv.org/html/2503.02881#S4.SS2) |
| **Force Policy** · RSS 2026 | 접촉면에서 힘을 조절할 방향과 움직일 방향을 나타내는 국소 좌표계를 시연에서 추출한다. 전역 시각 정책과 빠른 국소 힘 정책이 비동기로 실행된다. 실물 Flexiv에서 연마·삽입 계열 세 과제를 평가했다. | 같은 일을 분리된 두 정책이 얼마나 잘하는지 보여주는 대조군이다. 접촉면 좌표계와 빠른 힘 제어를 제공하는 기준선을 함께 두어야 단일 모델 통합의 이득을 판단할 수 있다. [RSS 논문](https://www.roboticsproceedings.org/rss22/p128.html) · [정책과 스케줄러 §IV-B/C](https://arxiv.org/html/2602.22088#S4.SS2) |
| **FTP-1** · CoRL 2026 | π0.5에 센서별 인코더와 공통 촉각 전문가를 붙여 서로 다른 형태의 촉각 데이터를 함께 학습한다. 처음 보는 센서 조합 두 곳에서 삽입·닦기 세 과제로 미세조정했다. | 센서 한 종류의 단순 추가에서 **다른 센서로 전이하는 접촉 표현**까지 질문이 넓어졌다. 같은 구조로 대규모 촉각 사전학습의 기여를 비교한 결과가 아래에 있다. [구조 §2.3](https://arxiv.org/html/2606.13102#S2.SS3) · [전이 실험 §4.1](https://arxiv.org/html/2606.13102#S4.SS1) · [CoRL 채택 목록](https://2026.corl.org/program/accepted-papers/) |
| **N₀-VTLA** · arXiv 2026 | π0.5의 상태·행동 표현을 계승하고 미래 촉각을 예측하는 잠재 표현을 행동 전문가에 연결한다. 배포 궤적의 상대적 진행도와 물체를 떨어뜨린 사건 등으로 좋은 행동을 표시하고, 같은 정책을 오프라인에서 개선한다. | 촉각은 정책의 관측이면서 학습한 행동을 평가하는 근거가 된다. 저자 코드의 촉각 제거·교환 검사는 표현이 입력에 의존하는지 진단한다. 실물 행동 개선은 별도의 롤아웃 결과에서 확인해야 한다. [학습 §4.4](https://arxiv.org/html/2607.23782#S4.SS4) · [저자 코드의 촉각 개입 검사](https://github.com/neoteai/N0-VTLA/blob/4e3174d6a54d9618c67728d8a2973b2b9cf05ace/docs/TACTILE_CAUSAL_PROBE.md) |
| **HapticVLA** · IROS 2026 | 과도한 파지력에 불이익을 주는 촉각 보상으로 교사를 학습하고, 교사의 행동을 촉각 인코더가 없는 학생에 증류한다. 배포 시 학생은 시각·언어·로봇 상태를 사용한다. | 훈련에 촉각을 써서 익힌 조작 습관과 이번 접촉에서 관측한 미끄러짐에 즉시 반응하는 능력을 분리할 수 있다. [IEEE 게재본](https://doi.org/10.1109/IROS61738.2026.11777360) · [학생 정책 §III-B](https://arxiv.org/html/2603.15257#S3.SS2) |
| **Facet-0** · arXiv 2026 | 플로 헤드가 운동과 그 운동이 유발할 미래 손목 wrench를 공동 예측한다. 배포 후 RL에서 평가·수정하는 것은 실행 가능한 Cartesian 행동이며, 예상 wrench는 보조 출력이다. | ‘action–wrench 공동 예측’이라는 표현만으로 목표 힘 명령으로 분류하면 혼동이 생긴다. 힘을 **예측해 움직임을 평가**하는 접근과 힘을 **선택해 제어기에 전달**하는 접근을 직접 비교할 수 있다. [공동 예측 §4.2](https://arxiv.org/html/2609.01596#S4.SS2) · [실행·적응 §5.3](https://arxiv.org/html/2609.01596#S5.SS3) |
| **ContactBench 1.0** · arXiv 2026 | 생활 접촉 과제 중 여섯 개를 골라 시각 정책 DP·π0.5와 시촉각 정책 RDP·FTP-1을 평가했다. 과제당 시연 100개를 수집했고, 실제 평가한 정책·과제 조합당 30회 시행했다. | 성공률, 진행도, 최대 손목 힘, 완료 시간을 함께 보고한다. 손가락 뒷면의 충돌은 손끝 촉각 센서의 관측 영역 밖이었고, 도구가 손 안에서 미끄러지는 신호는 일부 과제에서 조기 종료를 유발했다. [평가 §V-A](https://arxiv.org/html/2610.24512#S5.SS1) · [실패 분석 §V-C](https://arxiv.org/html/2610.24512#S5.SS3) |
| **Tune to Learn** · RSS 2026 | 같은 위치 명령도 하위 제어 이득에 따라 시연자가 기록하는 행동과 배포 시 예측 오차에 대한 응답이 달라진다. 행동 복제 실험에서 수집 이득과 실행 이득의 효과를 분리했다. | 목표 강성을 추가한 모델을 비교할 때 **데이터 수집 시 이득과 평가 시 이득**을 모두 기록해야 한다. 관측한 성능차를 정책 출력과 추종 제어기 중 어디에 귀속할지 판단하는 근거다. [RSS 논문](https://www.roboticsproceedings.org/rss22/p139.html) · [행동 복제 실험 §V-A](https://arxiv.org/html/2604.02523#S5.SS1) |

## 수치로 본 효과와 한계

| 확인하려는 효과 | 같은 논문 안의 비교 | 해석 가능한 범위 |
|---|---|---|
| 정책이 강성을 선택할 때 | CompVLA의 실물 Pivot에서 예측한 가상 변위를 유지하고 강성을 고정하면 성공 **4/10**, 학습한 강성을 쓰면 **7/10**이었다. | 같은 과제에서 강성 선택이 행동을 바꾼 근거다. 10회 규모이며 독립적인 감쇠 출력은 이 비교의 변수가 아니다. [CompVLA 표 3](https://arxiv.org/html/2609.23614#S5) |
| 촉각 사전학습을 추가할 때 | FTP-1의 미관측 센서 두 설정, 세 과제에서 평균 성공률은 **46.6%**였다. 같은 촉각 구조에 FTP-1 사전학습을 생략한 비교군은 **15.0%**였다. 두 삽입 과제는 각각 100개, 닦기는 50개 시연으로 미세조정했다. | **31.6%p**는 이 미세조정 조건에서 사전학습을 추가한 차이다. 새 센서에 학습 없이 배포한 수치로 읽을 수 없다. [FTP-1 표 3](https://arxiv.org/html/2606.13102#S4.SS1) |
| 촉각이 실제 접촉을 더 잘 다루게 했는지 | 독립 연구인 ContactBench의 실물 너트 체결에서 **π0.5와 FTP-1 모두 14/30 성공**이었다. 최대 손목 힘이 40 N을 넘은 시행은 각각 **27%와 83%**였다. | 성공률만 쓰면 두 모델이 동률이다. 힘까지 보면 물체에 가한 부하가 달랐다. 40 N은 이 벤치마크에서 정한 관측 기준이다. 두 정책은 구조와 사전학습 이력도 달라, 촉각만의 효과를 알려면 같은 정책에서 센서 입력을 바꾼 비교가 필요하다. [ContactBench 표 III·실패 분석](https://arxiv.org/html/2610.24512#S5) |

## 연구 방향에 대한 판단

**두 흐름의 근거는 서로 다른 연구진의 게재 논문에서 확인된다.** 2025년 ForceVLA에서 측정 힘을 운동 생성에 넣은 뒤, 2026년에는 목표 힘과 단계를 함께 내는 ForceVLA2, 가변 강성을 생성하는 CompVLA, 촉각 반응 빈도를 조절하는 AT-VLA가 서로 다른 설계를 실험했다. 독립 감쇠 제안과 관절 토크 참조는 이번 표본에서 확인한 더 좁은 갈래다. π 계열 자체는 경험 기반 정책 개선(π⋆0.6)과 언어·시각 하위 목표를 통한 조종 가능성(π0.7)도 발전시키고 있다. 이 조사는 접촉 연구를 골라 비교했으므로 전체 VLA 분야에서 각 갈래가 차지하는 비율까지 추정할 수는 없다. [ForceVLA](https://neurips.cc/virtual/2025/poster/120169) · [ForceVLA2](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html) · [CompVLA](https://compvla.github.io/) · [AT-VLA](https://arxiv.org/html/2605.07308#S3) · [π⋆0.6](https://www.pi.website/blog/pistar06) · [π0.7](https://www.pi.website/blog/pi07)

**검증할 질문은 “촉각을 넣으면 좋은가?”보다 좁게 잡을 수 있다.** 예를 들어 같은 삽입 자세에서 접촉면의 강성이 예고 없이 바뀔 때, 정책이 목표 힘까지 갱신하면 운동만 갱신할 때보다 **삽입 성공과 작업 시간을 유지하면서 순간 최대 힘과 힘 초과 지속 시간을 줄이는가?** ForceVLA2는 목표 힘 출력을, AT-VLA는 빠른 반응을, Force Policy는 분리된 국소 힘 제어를 이미 다뤘다. 직접 비교하려면 동일한 시연·센서 위치·수집/실행 이득·갱신 주기에서 목표 힘을 단계별 고정값으로 둔 조건과 정책이 갱신하는 조건을 짝짓고, 두 조건 모두에서 접촉 피드백을 제때 주거나 지연시킨다. 단순한 고정 목표 제어도 같은 성능을 내거나 힘 감소가 단지 느린 움직임에서 나온다면, 해당 조건에서는 학습한 힘 출력의 추가 이득을 주장하기 어렵다. 이 질문은 문헌에서 도출한 가설이다. [ForceVLA2](https://arxiv.org/html/2603.15169#S3) · [AT-VLA](https://arxiv.org/html/2605.07308#S3) · [Force Policy](https://arxiv.org/html/2602.22088#S4) · [Tune to Learn](https://arxiv.org/html/2604.02523#S5.SS1)

**조사 범위.** 추가 등록 전 원장 1,262편과 기존 행동 공간 비교표를 기준으로 삼았다. 추가 검색은 2024~2026년 공개 연구에서 `adaptive compliance policy`, `tactile feedback flow matching`, `future wrench vs force reference`, `cross-sensor tactile pretraining`, `contact-rich manipulation benchmark`로 넓혔다. OpenAlex는 판본·DOI 탐색에 쓰고, 게재처·저자 원문의 방법·부록·실험표와 공개 코드에서 위 내용을 확인했다. 표의 arXiv는 확인한 공개 판본이며, 수치는 각 저자가 보고한 실험값이다. [등록 원장](../work/sources/papers.json) · [기존 비교표](../synthesis/04_vla.md#vla-action-interfaces)
