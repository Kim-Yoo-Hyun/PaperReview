# 원문 감사

2026-11-26 KST 기준. 11월 전수 감사 대상 **1,252편**의 판정과 교정 결과다. 이후 등록분을 포함한 현재 편수는 [레지스트리 통계](./REGISTRY_STATS.md)에서 확인한다. [논문별 판정과 직접 근거](../work/sources/batches/source_audit_2026_11.jsonl)

## 오류율과 검증 범위

| 측정 | 분자 / 분모 | 의미 |
|---|---:|---|
| 11월 20일 교정 전 추가 확인 오류 | 37 / 1,252 (2.96%) | 당시 점검에서 사실 오류가 입증된 논문. 같은 논문은 한 번만 센다. |
| 이번 반영 후 확인 오류 | 0 / 1,252 (0.00%) | 10개 필드의 최신 판정 중 ‘수정 필요’가 남은 논문 |
| 현재 전 항목 통과 | 118 / 1,252 (9.42%) | 서지·링크, 기여·태그, 공개 자료 세 종류가 모두 통과 |
| 현재 미확인 필드 보유 | 1,134 / 1,252 (90.58%) | 하나 이상에 판정 근거가 부족한 논문 |

11월 20일 논문 기록과 자동 검색 분류에서 오류를 고친 논문은 중복을 제외해 141/1,252편(11.26%)이다. 자동 분류에서 잘못 붙은 검색 단서와 논문 내용 자체의 오류는 위 표에서 구별했다.

**[해석]** 미확인 필드에서 추가 오류가 나올 수 있어 전체의 실제 잔여 오류율은 점으로 추정할 수 없다. 기존 통과 판정을 전제로, 미확인만 해소될 때 가능한 논문 단위 범위는 0.00%–90.58%다. 필드별 미확인 건수와 당시 무작위 표본의 결과는 아래에 따로 제시했다.

## 항목별 결과

| 항목 | 11월 20일에 확인한 오류 | 현재 통과 | 존재 불확실 | 수정 필요 |
|---|---:|---:|---:|---:|
| 링크 | 0 | 1,226 | 26 | 0 |
| 제목 | 0 | 1,252 | 0 | 0 |
| 저자 | 6 | 1,252 | 0 | 0 |
| 연도 | 0 | 1,252 | 0 | 0 |
| 발표처·게재 | 0 | 1,182 | 70 | 0 |
| 요약·기여 | 30 | 1,252 | 0 | 0 |
| 코드 | 0 | 528 | 724 | 0 |
| 가중치 | 0 | 203 | 1,049 | 0 |
| 데이터 | 0 | 244 | 1,008 | 0 |
| 태그 | 1 | 1,252 | 0 | 0 |

링크는 주소의 역할별로, 공개 자료는 저자 표명과 배포 파일별로 판정한다. 이전 요약 판정 70편은 정규화 배치 문장이 대상이었다. 논문별 `scope`에서 대조한 문장을 확인할 수 있다.

## 읽기 등급별 확인 범위

| 등급 | 논문 | 전 항목 통과 | 요약·기여 미확인 | 태그 미확인 | 공개 여부 중 한 가지 이상 미확인 |
|---|---:|---:|---:|---:|---:|
| CORE | 50 | 18 | 0 | 0 | 31 |
| NEXT | 450 | 95 | 0 | 0 | 348 |
| REFERENCE | 510 | 5 | 0 | 0 | 504 |
| ARCHIVE | 242 | 0 | 0 | 0 | 242 |

## 배치별 결과

| 배치 | 논문별 원장 행 | 편수 | 전 항목 통과 | 미확인 | 수정 필요 |
|---:|---|---:|---:|---:|---:|
| <a id="batch-01"></a>1 | [pr-0001–pr-0100](../work/sources/batches/source_audit_2026_11.jsonl#L1-L100) | 100 | 15 | 85 | 0 |
| <a id="batch-02"></a>2 | [pr-0101–pr-0200](../work/sources/batches/source_audit_2026_11.jsonl#L101-L200) | 100 | 1 | 99 | 0 |
| <a id="batch-03"></a>3 | [pr-0201–pr-0300](../work/sources/batches/source_audit_2026_11.jsonl#L201-L300) | 100 | 2 | 98 | 0 |
| <a id="batch-04"></a>4 | [pr-0301–pr-0400](../work/sources/batches/source_audit_2026_11.jsonl#L301-L400) | 100 | 0 | 100 | 0 |
| <a id="batch-05"></a>5 | [pr-0401–pr-0500](../work/sources/batches/source_audit_2026_11.jsonl#L401-L500) | 100 | 2 | 98 | 0 |
| <a id="batch-06"></a>6 | [pr-0501–pr-0600](../work/sources/batches/source_audit_2026_11.jsonl#L501-L600) | 100 | 3 | 97 | 0 |
| <a id="batch-07"></a>7 | [pr-0601–pr-0700](../work/sources/batches/source_audit_2026_11.jsonl#L601-L700) | 100 | 11 | 89 | 0 |
| <a id="batch-08"></a>8 | [pr-0701–pr-0800](../work/sources/batches/source_audit_2026_11.jsonl#L701-L800) | 100 | 10 | 90 | 0 |
| <a id="batch-09"></a>9 | [pr-0801–pr-0900](../work/sources/batches/source_audit_2026_11.jsonl#L801-L900) | 100 | 19 | 81 | 0 |
| <a id="batch-10"></a>10 | [pr-0901–pr-1000](../work/sources/batches/source_audit_2026_11.jsonl#L901-L1000) | 100 | 18 | 82 | 0 |
| <a id="batch-11"></a>11 | [pr-1001–pr-1100](../work/sources/batches/source_audit_2026_11.jsonl#L1001-L1100) | 100 | 16 | 84 | 0 |
| <a id="batch-12"></a>12 | [pr-1101–pr-1200](../work/sources/batches/source_audit_2026_11.jsonl#L1101-L1200) | 100 | 15 | 85 | 0 |
| <a id="batch-13"></a>13 | [pr-1201–pr-1252](../work/sources/batches/source_audit_2026_11.jsonl#L1201-L1252) | 52 | 6 | 46 | 0 |

<a id="요약기여-원문-대조"></a>

## 요약과 기여의 원문 대조

대상 1,252편 중 1,252편(100.00%)의 요약·기여에 원문 근거가 있다. 순차 검토한 999편은 PDF 997편과 공식 웹 원문 2편이며 이 중 18편의 문자 전사를 교정했다. 원장에 문장별 쪽·절과 판본 해시를, 배치 메타데이터에 검토일·대상 등급·기준 커밋을 기록했다. [논문별 근거](../work/sources/batches/source_audit_2026_11.jsonl) · [배치 이력](../work/sources/registry_meta.json)

### 노트의 수식과 도식

10편의 표준 노트 31개에서 91줄의 글꼴 전용 문자 258개를 인쇄된 수식·그림과 대조해 복원했다. 원장에는 대조한 PDF의 SHA-256, 근거 쪽과 절, 교정 전 노트의 줄 번호를 기록했다. [논문별 근거](../work/sources/batches/source_audit_2026_11.jsonl) · [교정 내용](../work/update/REGISTRY.md#note-review)

### 원문과 판본 교정

| 논문 | 게재본과 대조한 결과 |
|---|---|
| LE-Object | 기존 arXiv 식별자는 Deng 등의 OpenObj로 연결된다. LE-Object 게재본 표 I과 참고문헌 [31]은 이 연구를 독립 비교법으로 명시한다. [기존에 연결된 PDF](https://arxiv.org/pdf/2406.08009v1) · [게재본](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304) |
| Context Graph-based Visual-Language Place Recognition | ICRA 게재본의 III-C절과 그림 4가 문맥 그래프의 계산·결합을 명시한다. 기존 PDF는 같은 저자의 2024년 저자판이며 게재본과 표제 및 평가 내용이 다르다. [기존에 연결된 PDF](https://arxiv.org/pdf/2410.19341v1) · [게재본](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699) |

**DeXtreme 저자 명단.** ICRA 게재본 인쇄 5977쪽 표제면의 저자 14명과 순서가 원장·학회 목차·저자판과 일치한다. IEEE 웹 서지에는 11명이 표시된다. [게재본 표제면](https://ieeexplore.ieee.org/ielx7/10160211/10160212/10160216.pdf#page=1) · [출판사 웹 서지](https://ieeexplore.ieee.org/abstract/document/10160216) · [학회 목차](https://www.proceedings.com/content/069/069566webtoc.pdf#page=103)

요약·서지 검토 중 20편의 저자 표기 또는 순서를 고쳤다. 교정 전후 명단과 표제면 출처는 감사 원장의 `byline_correction`에 있다. [논문별 조회](#논문별-조회)

### 평가 조건과 지표

74편의 평가 조건·지표를 보완했다. 각 논문의 `04_evaluation.md`와 감사 원장의 `summary_review.scope_clarification`에서 측정 조건과 원문 위치를 확인할 수 있다. [논문별 조회](#논문별-조회) · [감사 원장](../work/sources/batches/source_audit_2026_11.jsonl)

## 다축 태그와 공개 자료

코드·가중치·데이터의 배포 범위를 항목별로 집계했다. 기존 검색 태그 판정은 원문의 방법·평가와 대조한 논문에만 반영했다. [배치별 분류와 미확인 범위](../work/update/REGISTRY.md#taxonomy-batches)

| 배치 | 공개 근거를 갱신한 논문 | 배포 파일 | 저자의 미공개·공개 예정 안내 | 배포 미확인으로 교정 | 기존 검색 태그 대조 |
|---|---:|---:|---:|---:|---:|
| core_next_02 | 22 | 34 | 5 | 1 | 19 |
| core_next_03 | 43 | 67 | 2 | 6 | 50 |
| core_next_04 | 43 | 88 | 5 | 0 | 50 |
| core_next_05 | 42 | 78 | 3 | 7 | 50 |
| core_next_06 | 43 | 86 | 1 | 0 | 50 |
| core_next_07 | 38 | 65 | 5 | 0 | 50 |
| core_next_08 | 35 | 71 | 3 | 0 | 50 |
| core_next_09 | 38 | 75 | 2 | 0 | 50 |
| core_next_10 | 17 | 28 | 0 | 0 | 27 |

### REFERENCE 검색 태그

방법·평가 절에서 각 태그의 역할을 확인했다. 표시 태그와 검색 필터를 함께 고친 논문은 두 열에 모두 센다. [논문별 원문 위치와 교정 전 값](../work/sources/batches/source_audit_2026_11.jsonl)

| 배치 | 대조 | 표시 태그 변경 | 기존 필터 교정 | 필터 첫 등록 | 모두 유지 |
|---|---:|---:|---:|---:|---:|
| reference_tags_01 | 50 | 16 | 38 | 0 | 12 |
| reference_tags_02 | 50 | 38 | 45 | 0 | 2 |
| reference_tags_03 | 50 | 19 | 38 | 0 | 9 |
| reference_tags_04 | 50 | 23 | 50 | 0 | 0 |
| reference_tags_05 | 50 | 24 | 50 | 0 | 0 |
| reference_tags_06 | 50 | 27 | 46 | 0 | 2 |
| reference_tags_07 | 50 | 34 | 3 | 47 | 0 |
| reference_tags_08 | 16 | 11 | 0 | 16 | 0 |

### ARCHIVE 검색 태그

방법·평가 절에서 각 태그의 역할을 확인했다. 표시 태그와 검색 필터를 함께 고친 논문은 두 열에 모두 센다. [논문별 원문 위치와 교정 전 값](../work/sources/batches/source_audit_2026_11.jsonl)

| 배치 | 대조 | 표시 태그 변경 | 기존 필터 교정 | 필터 첫 등록 | 모두 유지 |
|---|---:|---:|---:|---:|---:|
| archive_tags_01 | 50 | 43 | 38 | 0 | 5 |
| archive_tags_02 | 50 | 43 | 44 | 0 | 2 |
| archive_tags_03 | 31 | 22 | 30 | 0 | 0 |

다축 정규화에서 85편의 저자 표기·순서를 교정했다. 논문별 원문과 이전 명단은 `byline_correction`에 보존했다. [감사 원장](../work/sources/batches/source_audit_2026_11.jsonl)

## CORE 공개 자료

첫 감사에서 CORE 43편의 공개 자료를 대조했다. 파일을 확인한 과제와 구성요소에만 공개 판정을 적용했다.

이후 남은 36편 68개 항목을 모두 재검토했다. 7개 항목의 배포 파일을 확인했고, 6개는 자체 학습 가중치나 실험 데이터가 연구 산출물에 해당하지 않음을 원문에서 확인했다. 현재 31편 55개 항목은 배포 여부를 판단할 근거가 부족하다. [각 항목의 판정·근거·대조 주소](../work/sources/batches/source_audit_2026_11.jsonl)

| 자료 | 첫 감사 대상 | 첫 감사 파일 확인 | 재검토 대상 | 추가 파일 확인 | 해당 없음 | 현재 미확인 |
|---|---:|---:|---:|---:|---:|---:|
| 코드 | 16 | 6 | 10 | 1 | 0 | 9 |
| 가중치 | 38 | 7 | 31 | 5 | 4 | 22 |
| 데이터 | 34 | 7 | 27 | 1 | 2 | 24 |

실험 데이터를 사용했지만 배포 파일을 확인하지 못한 7편의 기존 ‘해당 없음’ 판정을 ‘미확인’으로 고쳤다. [pr-0008](../work/sources/batches/source_audit_2026_11.jsonl#L8) · [pr-0522](../work/sources/batches/source_audit_2026_11.jsonl#L522) · [pr-0524](../work/sources/batches/source_audit_2026_11.jsonl#L524) · [pr-0620](../work/sources/batches/source_audit_2026_11.jsonl#L620) · [pr-0745](../work/sources/batches/source_audit_2026_11.jsonl#L745) · [pr-0821](../work/sources/batches/source_audit_2026_11.jsonl#L821) · [pr-0835](../work/sources/batches/source_audit_2026_11.jsonl#L835)

## 교정 재검증

2026-11-20 당시 점검 범위와 방법이다. [점검 시작 판본](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/work/sources/papers.json)

- 서지 출처에서 표제 1,252편(대표 URL에서 1,240편), 저자 순서 1,165편, 연도 1,126편, 게재 근거 1,098편을 다시 확인했다. 서지가 엇갈리면 게재본 표제면을 대조했다.
- 공개로 기록된 코드 395건·가중치 82건·데이터 94건 중 570/571건에서 파일·목록 또는 웹페이지가 응답했다. 인증이 필요한 자료는 저자 배포 목록과 판본을 확인했다. [AgiBot World Alpha 배포 목록](https://huggingface.co/api/datasets/agibot-world/AgiBotWorld-Alpha)
- 안정 ID를 정렬해 `random.Random(20261120).sample(ids, 100)`로 추출한 100편의 폐루프 행동 주장을 확인했다. 문구 없음 24편, 행동 근거 확인 39편, 범위 오류 30편, 유보 7편이다. 이 표본의 분모는 해당 문구를 검사한 논문이다.
- 자동 서식 934편·1,753곳을 정리하고 정규화 배치 33편을 개요와 연결했다. 잘못 매칭된 105편에서 힘·토크 단서 105건과 접촉 단서 99건을 제거했다.

## 이전 감사

- 11월 19일의 파일 진단은 당시 1,227편의 태그 표기, 중복 의심, 발표일 해상도를 점검했다. 비슷한 제목으로 잡힌 GR00T N1.5와 N1.6은 별도 판본으로 유지했다. 정식 발표일이 연도 단위인 항목에서 최근 6개월 비중을 확정할 수 없다. [당시 분모·검사 기준](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/REGISTRY_AUDIT.md) · [현행 통계](./REGISTRY_STATS.md)
- 같은 날 집중 읽기 477편 중 CORE 30편·NEXT 20편의 층화표본에서는 10/50편에서 11개 오류를 고쳤다. 당시 두 등급 모집단의 가중 추정은 11.7%였다. [50편의 원문·추출법·판정](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/SAMPLE_AUDIT.md)
- 11월 20일 첫 전수 감사의 **교정 전** 발견률은 109/1,252편(8.71%), 132개 필드였다. 그 뒤 280편에서 392개 필드의 증거를 보강하며 43편의 오류 45건을 교정했다. 각 시점의 오류는 같은 논문에서 겹칠 수 있다. [당시 13개 배치와 논문별 표](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/SOURCE_AUDIT.md)

## 논문별 조회

한 논문의 현재 10개 판정, 최초 판정, 교정 전후 값과 원문 출처를 안정 ID로 조회한다. 전체 보고서는 같은 원장에서 생성된다.

```bash
python3 work/scripts/render_source_audit.py --paper pr-0027
python3 work/scripts/render_source_audit.py --verify-corrections
```
