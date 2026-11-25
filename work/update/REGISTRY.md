# 레지스트리 변경

논문별 출처와 판정은 원장에 남기고, 여기에는 같은 검색어를 서로 다른 뜻으로 쓰기 쉬운 사례와 등록 기준을 모았다. [논문 목록](../../PAPER.md) · [전체 통계](../../research/REGISTRY_STATS.md) · [원문 감사](../../research/SOURCE_AUDIT.md)

## 서랍 연구 브랜치의 문헌 통합

기존 원장 1,252편과 로컬 연구에서 확인한 8편의 제목·공식 식별자를 대조했다. 겹치는 논문은 없었다. 기존 원격 안정 ID를 유지하고 접촉 조작·장시간 과제·양팔·시각 피드백 연구 등 여덟 편을 `pr-1253`–`pr-1260`에 배정했다. 각 논문의 표준 노트와 기존 근거 날짜를 옮겼다. CORE 50, NEXT 454, REFERENCE 514, ARCHIVE 242편이다. 11월 원문 감사의 1,252편은 당시 표본이다. [전체 색인](../../research/REGISTRY_INDEX.csv) · [서랍 실험과 비교할 시각 피드백 연구](../../2026/arXiv/2026_arXiv_IMPACT-VLA-Interaction-aware-Multimodal-Propagation-Attrib/01_overview.md)

Tune to Learn은 11월 19일의 원문·공개 평가 자료 확인 기록과 11월 23일의 RSS 쪽수별 요약을 한 노트에 통합했다. 읽기 상태는 기존 `UNREAD`를 유지한다. [논문 개요](../../2026/RSS/2026_RSS_Tune-to-Learn-How-Controller-Gains-Shape-Robot-Policy-Lear/01_overview.md) · [평가 범위](../../2026/RSS/2026_RSS_Tune-to-Learn-How-Controller-Gains-Shape-Robot-Policy-Lear/04_evaluation.md)

<a id="taxonomy-batches"></a>

## 다축 태그와 공개 범위

연구 브랜치 통합 전 집중 읽기 500편 중 423편(84.6%)에 다축 태그가 있다. 정규화 8개 배치의 CORE 50편·NEXT 350편과 별도 등록한 NEXT 23편을 합한 수다. YAML의 `registry_id`는 원장의 안정 ID에 대응한다. `changed_from`에서 변경 전 값을 확인할 수 있다. [배치 정의](../sources/registry_meta.json) · [별도 등록 원장](../sources/batches/gapfill_2026_11.yaml) · [당시 남은 77편의 작업 순서](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/TODO.md)

| 분류할 때의 질문 | 판정 근거 |
|---|---|
| 무엇을 학습하거나 제어하는가? | 시연·교사 행동은 IL, 보상에 의한 정책·가치 갱신은 RL, 예측 동역학을 이용한 계획·학습은 모델기반으로 기록한다. 하위 제어기와 정책을 각각 확인한다. |
| 어느 로봇의 어떤 행동인가? | 조작·내비게이션·이동·전신제어·모바일매니퓰레이션은 실제 과업을 따른다. 로봇 형상은 명시된 기체나 구성에서 확인한다. |
| 실행 중 정책이 무엇을 볼 수 있는가? | 기록한 센서, 정책에 입력한 센서, 학습 시에만 사용한 상태를 구별한다. 장면 영상·센서 깊이·광학식 촉각·손목 힘/토크는 신호의 역할을 명시한다. |
| 자료를 어디에서 얻었는가? | 인간 영상, 실제 로봇 시연, 사람이 원격조작한 시뮬레이션, 합성 자료를 구분한다. 실물에서 평가했다는 사실은 학습 자료의 출처를 결정하지 않는다. |
| 전용 태그는 무엇을 설명하는가? | VLA의 백본·배포 시 행동 표현·학습 방식·평가 조건, 휴머노이드의 제어 범위·학습·기종·손을 기록한다. 기존 정책만 비교한 실험에는 평가 대상임을 표시한다. |
| 어떤 파일을 공개했는가? | 코드·가중치·데이터를 따로 판정한다. 구현 범위, 모델 버전, 훈련·평가용 여부를 저자가 배포한 파일에 연결한다. 미확인은 `unknown`, 저자가 공개하지 않았다고 명시한 경우는 `N`이다. |

<a id="첫-배치-태그-매핑"></a>
<a id="두-번째-배치-태그-매핑"></a>
<a id="세-번째-배치-태그-매핑"></a>
<a id="네-번째-배치-태그-매핑"></a>
<a id="다섯-번째-배치-태그-매핑"></a>
<a id="여섯-번째-배치-태그-매핑"></a>
<a id="일곱-번째-배치-태그-매핑"></a>
<a id="여덟-번째-배치-태그-매핑"></a>

### 배치별 근거

| 검토 범위 | 재사용할 때 주의할 사례 | 이전 값·원문 위치 |
|---|---|---|
| CLIP ~ RFMPose | OFT의 L1 직접 회귀와 계측용 휴대 그리퍼 시연은 기존 열거값으로 표현하기 어려워 설명을 보존했다. JALA와 Ctrl-World의 공개 판정에는 후속 교정이 있다. | [첫 50편](../sources/batches/core_next_01.yaml) |
| Diffusion Policy ~ GaussianGrasper | 연속 행동 회귀와 공간 복셀 선택은 다른 출력이다. 자세·형상 평가에 해당하는 논문은 로봇 과업의 실행 근거를 따로 찾는다. | [두 번째 50편](../sources/batches/core_next_02.yaml) |
| Clio ~ PIN-WM | DAPG의 시연·정책, RoboPack의 체크포인트·표본 데이터는 각각 공개 범위가 다르다. Q-Transformer의 과제 세부 수는 본문과 그림 표기가 달라 둘 다 기록했다. | [세 번째 50편](../sources/batches/core_next_03.yaml) |
| Dexterous World Models ~ Memory Retrieval in Visuomotor Policies | WMPO는 세계 모델 안에서 정책을 학습한다. PALM의 실물 평가는 여섯 하위 동작을 포함하는 과제 한 개다. | [네 번째 50편](../sources/batches/core_next_04.yaml) |
| DexterityGen ~ RoboSplat | DIGIT과 후속 센서 DIGIT 360의 배포처를 구별했다. CordViP의 실물 장치는 단일 UR5와 LEAP Hand다. | [다섯 번째 50편](../sources/batches/core_next_05.yaml) |
| PartInstruct ~ OopsieVerse | NavDP와 LoGoPlanner의 별칭, GR00T N1·N1.5·N1.6의 체크포인트는 판본별로 대조했다. RLinf-VLA 실물 서랍 닫기에서는 비교한 두 정책이 각각 8/10회 성공했다. | [여섯 번째 50편](../sources/batches/core_next_06.yaml) |
| USER ~ TidyBot++ | 카메라 시점을 복원하는 CoRe-VLA와 전문가 선택을 다루는 CoRE-VLA는 다른 연구다. TidyBot++의 배포 시연·가중치는 sim-v1 예제에 해당한다. | [일곱 번째 50편](../sources/batches/core_next_07.yaml) |
| PhysTwin ~ Force Policy | Spa-Bench는 저장한 카메라와 정책에 사용한 카메라가 다르다. Force Policy는 실물 세 과제를 평가했고, 확인된 정책·데이터는 상자 뒤집기용이다. | [여덟 번째 50편](../sources/batches/core_next_08.yaml) |

직접 회귀, 지도 구축·진단만 수행하는 방법, 계측용 휴대 그리퍼에서 온 시연은 기존 분류에 맞는지 미확정이다. 원문에서 확인한 실제 역할을 서술하고 불명확한 축은 `unknown`으로 둔다. 각 판정 시점의 기존 태그 전체 매핑, 중복 후보와 검색 기준, 배포 범위의 변경 내역은 원래의 표와 감사 원장에서 조회할 수 있다. [기존 태그 전체 매핑](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/6aa75b27be4ab2e88ab56cd54df5818317e7a2fb/work/update/REGISTRY.md#taxonomy-batches) · [항목별 공개 여부](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

<a id="reg-r18"></a>

## 등록·서지 교정

- 공유 제어 문헌 HARMONIC과 Residual Copilot을 REFERENCE에 추가했다. 두 논문은 각각 보조 전후의 명령 기록과 보조 시연으로 학습한 정책의 실물 기어 삽입 평가를 제공한다. DROID의 RSS 게재본과 저자 배포 자료도 연결했다. [HARMONIC](../../2022/IJRR/2022_IJRR_HARMONIC-A-multimodal-dataset-of-assistive-humanrobot-coll/01_overview.md) · [Residual Copilot](../../2026/CoRL/2026_CoRL_Efficient-and-Reliable-Teleoperation-through-Real-to-Sim-t/01_overview.md) · [DROID 게재본](https://www.roboticsproceedings.org/rss20/p120.html)
- 외부 목록과 대조한 36편 중 23편을 NEXT에 등록했고 9편을 보류했다. 4편은 기존 ID와 일치했다. 직접 선행 추가 18편, 3D 추정 문헌, Ψ₀를 포함한 이전 등록의 선정 근거도 조회할 수 있다. [누락 심사](../../research/GAPFILL.md) · [대조 범위](../../research/EXTERNAL_COVERAGE.md) · [직접 선행 등록](../sources/registry_maintenance_2026-11-18.json) · [Ψ₀ 교정](../sources/registry_accuracy_2026-11-16.json)
- OpenVLA의 선행·후속 관계와 DINOv2·RT-2의 게재 서지를 대조했다. TrajOpt의 잘못된 arXiv 식별자는 IJRR 게재 DOI와 저자 PDF로 교정했다. [OpenVLA 계보](../../research/OPENVLA_LINEAGE.md) · [TrajOpt 게재본](https://doi.org/10.1177/0278364914528132) · [CORE 심화 검토](../sources/batches/tier1_vla_humanoid.yaml)

<a id="note-review"></a>

## 노트 교정

원문 쪽수와 텍스트 수정을 연결해 둔 기록이다. PDF 추출 감사에서는 55편의 노트 135개에서 306개 구간을 대조·수정했다. 11월 24일 수식·도식 감사에서는 10편의 노트 31개에서 91줄을 확인했다. 숫자는 각 감사의 단위와 범위로 해석한다. [PDF 추출 교정](../sources/pdf_note_review_2026-10-23.json) · [후속 교정](../sources/pdf_note_review_followup_2026-10-23.json) · [수식·도식 감사](../../research/SOURCE_AUDIT.md#노트의-수식과-도식) · [논문별 감사 원장](../sources/batches/source_audit_2026_11.jsonl)
