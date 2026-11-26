# 문헌 검토

논문을 찾을 때는 [검색 색인](./REGISTRY_INDEX.csv)에서 제목·태그·별칭으로 찾고 `overview_path`로 개요를 연다. 색인의 `sequence`는 CORE·NEXT 각 등급 안의 읽기 순서다. 정독할 논문은 [읽기 계획](./READING_PLAN.md)에서 선행과 선정 이유를 확인한다.

| 필요한 정보 | 원본과 사용 방법 |
|---|---|
| 모든 논문의 등급 | [전체 등급표](./READING_TIERS.csv)의 `paper_id`로 색인과 연결한다. `track`은 읽기 그룹, `primary_track`은 분야별 비교 트랙이다. [일곱 트랙](../synthesis/README.md) |
| 내가 읽은 내용 | [현재 기록](./READING_STATUS.csv)에 상태·날짜·분석을 입력한다. [이전 기록](./READING_STATUS_HISTORY.csv)은 대상에서 빠진 논문의 메모를 보관하며 재편입 시 복원된다. [상태와 노트 작성법](./READING_STATUS.md) |
| 수록 범위와 근거 | [현재 원장 통계](./REGISTRY_STATS.md), [외부 목록 대조와 누락 심사](./GAPFILL.md), [원문 감사와 미확인 항목](./SOURCE_AUDIT.md)은 각각의 조사 시점과 분모를 표시한다. |
| 논문 간 비교·연구 질문 | [VLA 행동 공간과 접촉 제어](./VLA_ACTION_SPACE.md)에서 정책이 결정하는 물리량을 비교하고 [OpenVLA 인용 계보](./OPENVLA_LINEAGE.md)에서 직접 계승과 기준선 사용을 확인한다. [연구 설계](./RESEARCH_GUIDE.md) · [분야별 비교](../synthesis/README.md) · [로보틱스 공백 분석](../work/update/ROBOTICS_TRENDS.md#verified-gap-analysis) |
| 세부 분류 | [다축 태그와 공개 범위](../work/update/REGISTRY.md#taxonomy-batches)와 [VLA·휴머노이드 심화 근거](../work/sources/batches/tier1_vla_humanoid.yaml)에서 실제 실험 조건·미확인 값·원문 위치를 확인한다. |

<a id="paper-admission"></a>

## 논문 선정과 출처 확인

1. **선정 이유를 정한다.** 로봇 행동에 중요한 기반, 표준 과제·데이터·벤치마크, 새로운 센서·기체·제어 조건, 연구 질문에 직접 필요한 비교를 우선한다. 최신 동향은 최근 세 달력 연도, 기반 연구는 후속 사용으로 판단한다. 3D 인식은 조작·항법·접촉·복구에 미치는 효과를 본다. [검색 지도](./RESEARCH_GUIDE.md#search-map-2026-11-17)
2. **공식 판본을 확인한다.** CVPR·ICCV·ECCV·NeurIPS·ICLR·CoRL·RSS·ICRA·IROS 등의 공식 proceedings, OpenReview·PMLR·CVF 또는 저널 출판사에서 제목·저자·연도·채택 여부를 확인한다. 로보틱스 관련 T-RO·RA-L·IJRR·Science Robotics 등도 포함한다. 공식 게재가 확인되기 전에는 확인한 프리프린트 상태를 표시한다. 서베이·연구실 목록·큐레이션은 후보를 찾는 데 쓴다.
3. **기존 항목과 대조한다.** 원장·논문 목록·등급표에서 제목과 특징적인 구절, 별칭, DOI·arXiv·OpenReview ID를 확인한다. 부제·기호·표기 차이를 살피고 게재본은 안정 ID에 연결한다. 별도 등록하는 판본에는 차이와 관계를 기록한다.
4. **읽을 근거를 남긴다.** 대표 원문과 저자 프로젝트·코드, 연구 역할과 선행 대비 차이를 적는다. 가장 직접적인 기여와 평가에 따라 주 트랙 하나를 정하고 교차 주제는 태그로 연결한다. 휴머노이드는 보행·전신 제어·조작에 배정한다. PDF 유무·인기도·발표처별 편수는 등급 근거로 쓰지 않는다.
