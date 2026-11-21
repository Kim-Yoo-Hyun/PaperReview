# 원문 감사

2026-11-22 KST 기준. 등록된 1,252편에서 **확인된 잔여 오류는 0/1,252편(0.00%)**, 10개 필드에 근거가 갖춰진 논문은 **19편**, 한 필드 이상 미확인인 논문은 **1,233편**이다. [논문별 판정과 직접 근거](../work/sources/batches/source_audit_2026_11.jsonl)

## 요약·기여 원문 대조

| 확인일 | 등급 | 대상 | 원문 대조 통과 | 같은 등급에서 남은 요약 |
|---|---|---|---:|---:|
| 2026-11-22 | NEXT | [pr-0028–pr-0768 중 당시 미확인 논문](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/f3806160de5ecd1a08dd7b18364fd63d0dac5745) | 100 | 261 |

안정 ID 순서로 미확인 논문을 뽑아 각 overview의 한 줄 요약과 핵심 기여 두 개를 원문 PDF에 대조했다. 각 문장의 링크는 실제 열어 본 판본의 PDF 쪽수로 이동한다. 원장에 판본의 SHA-256과 교정 전 노트의 해시를 보존했다. 이 배치는 요약 검증 진척을 나타낸다. 전체 오류율을 추정하는 무작위 표본으로 사용할 수 없다.

기존 노트에서 확인한 문자 전사 교정은 2편이다. 원장에 해당 문구와 근거를 기록했다. [pr-0552 원문](https://lavalle.pl/papers/Lav98c.pdf) · [pr-0751 원문](https://www.roboticsproceedings.org/rss21/p052.pdf)

## CORE 공개 자료

공개 자료가 한 종류 이상 미확인이었던 CORE 43편에서 저자 배포처·논문별 근거를 확인했다. 파일의 역할이 식별된 경우에만 공개 판정을 갱신했다. 일부 자료만 확인한 경우 원장에 그 범위를 적었다.

| 자료 | 점검한 미확인 항목 | 파일 근거 확보 | 남은 미확인 |
|---|---:|---:|---:|
| 코드 | 16 | 6 | 10 |
| 가중치 | 38 | 7 | 31 |
| 데이터 | 34 | 7 | 27 |

NoMaD(`pr-0568`)의 데이터는 기존에 `not_applicable`로 분류되어 있었다. 공유 저자 저장소가 훈련에 사용했다고 명시한 자료 중 수정 GoStanford2의 go_stanford.zip을 확인했다. 전체 훈련 혼합에서 공개된 부분이다. [저자 설명](https://raw.githubusercontent.com/PrieureDeSion/visualnav-transformer/dca79815b704e5aa9c6bdc3082351f9e3b2848c2/README.md) · [배포 파일](https://drive.google.com/file/d/1BVGA46WbvOZFyuzkzV2n_yZqcQsdIJy7/view)

**DeXtreme 저자 명단.** 출판사 서지에는 11명, 학회 목차와 저자판에는 14명이 적혀 있다. ICRA 게재본 인쇄 5977쪽 표제면은 출판사 인증 화면으로 연결되어 미확인으로 유지한다. [출판사 서지](https://ieeexplore.ieee.org/abstract/document/10160216) · [학회 목차](https://www.proceedings.com/content/069/069566webtoc.pdf#page=103) · [저자판](https://arxiv.org/abs/2210.13702)

## 오류율과 검증 범위

| 측정 | 분자 / 분모 | 의미 |
|---|---:|---|
| 11월 20일 교정 전 추가 확인 오류 | 37 / 1,252 (2.96%) | 당시 점검에서 사실 오류가 입증된 논문. 같은 논문은 한 번만 센다. |
| 이번 반영 후 확인 오류 | 0 / 1,252 (0.00%) | 10개 필드의 최신 판정 중 ‘수정 필요’가 남은 논문 |
| 현재 전 항목 통과 | 19 / 1,252 (1.52%) | 서지·링크, 기여·태그, 공개 자료 세 종류가 모두 통과 |
| 현재 미확인 필드 보유 | 1,233 / 1,252 (98.48%) | 미확인은 오류로 확정하거나 통과 처리하지 않았다. |

11월 20일 논문 기록과 자동 검색 분류에서 오류를 고친 논문은 중복을 제외해 141/1,252편(11.26%)이다. 자동 분류에서 잘못 붙은 검색 단서와 논문 내용 자체의 오류는 위 표에서 구별했다.

**[해석]** 미확인 필드에서 추가 오류가 나올 수 있어 전체의 실제 잔여 오류율은 점으로 추정할 수 없다. 기존 통과 판정을 전제로, 미확인만 해소될 때 가능한 논문 단위 범위는 0.00%–98.48%다. 이는 표본 신뢰구간이 아니다. 연구 비교에 쓸 요약과 공개 자료부터 미확인 필드를 계속 대조할 필요가 있다.

## 교정 재검증

2026-11-20에 수행한 전수 점검 기록이다. [당시 조사 시작 판본](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/work/sources/papers.json)

- 전 1,252편에서 대표 URL과 논문별 서지 출처에 다시 접근했다. 독립적으로 표제를 식별한 논문은 1,252편, 대표 URL 자체에서 표제를 확인한 논문은 1,240편이다. 새 서지에서 순서가 일치하는 저자열 1,165편, 해당 판본의 등록 연도 1,126편, 게재 근거 1,098편을 대조했다. 논문별 서지 필드·프로그램 표제·PDF 첫 쪽을 사용했다. 대소문자·구두점·공백·수식 표기를 정규화해 제목을 비교하고, 저자열은 각 이름의 성·이름 표기를 정리한 뒤 순서를 비교했다. 저자 수·순서가 다르거나 프로그램과 게재본이 다르면 표제면을 확인했다.
- 원장이 공개로 기록한 코드 395건·가중치 82건·데이터 94건의 출처를 다시 열었다. 571건 중 570건에서 파일·목록 또는 웹페이지가 응답했다. AgiBot World Alpha는 인증 없이 파일 주소를 열 수 없었고, 저자 배포 목록에서 같은 리비전의 파일과 이용 조건을 확인했다. 응답 결과는 접근성 검사다. 구현의 완전성, 가중치 호환성, 실험 재현성은 별도 검증 대상이다. [AgiBot World Alpha 배포 정보](https://huggingface.co/api/datasets/agibot-world/AgiBotWorld-Alpha)
- 안정 ID를 정렬한 직전 원장에서 `random.Random(20261120).sample(ids, 100)`로 비복원 추출했다. 교체 없이 100편의 overview에서 동일한 폐루프 행동 주장과 평가 범위를 점검했다. 해당 문구 없음 24편, 행동과 연결되는 근거 확인 39편, 원문 범위를 벗어난 귀속 30편, 판정 유보 7편이었다. 이 표본은 특정 서술 오류를 찾기 위한 검사다. 표본의 발견률을 열 가지 필드의 전체 오류율로 일반화할 수 없다.
- 같은 서식이 남아 있던 **934개 overview의 1,753곳**을 정리했다. 원문의 출력·평가가 확인된 경우 요약과 기여를 구체화했고, 나머지 자동 발췌에는 출처 수준을 표시했다. 기존 정규화 배치에서 이미 확인한 33편은 그 요약과 기여를 overview에 연결했다. 공통 문구를 지운 일만으로 요약을 통과시키지 않았다.
- 자동 검색 분류에서 ‘reinforcement’의 일부가 ‘force’로 읽혀 105편에 잘못된 단서가 붙었다. 힘·토크 단서 105건과 접촉 단서 99건을 제거하고 생성 규칙을 고쳤다. 독립적인 접촉 단어가 있는 논문은 해당 단서를 유지했다.
- 이번에 확인한 사실 오류는 저자 6건, 요약·기여 30건, 태그 1건이다. 원문에서 대상으로 삼은 출력과 실험으로 보인 효과를 구분한다. 예를 들어 3DVG-Transformer는 언어가 가리키는 3D 물체를 찾고, Masked Autoencoders는 가려진 패치를 복원해 시각 표현을 학습한다. [3DVG-Transformer 게재본](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html) · [Masked Autoencoders 게재본](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html)

## 항목별 결과

| 항목 | 11월 20일에 확인한 오류 | 현재 통과 | 존재 불확실 | 수정 필요 |
|---|---:|---:|---:|---:|
| 링크 | 0 | 1,206 | 46 | 0 |
| 제목 | 0 | 1,252 | 0 | 0 |
| 저자 | 6 | 1,251 | 1 | 0 |
| 연도 | 0 | 1,252 | 0 | 0 |
| 발표처·게재 | 0 | 1,182 | 70 | 0 |
| 요약·기여 | 30 | 353 | 899 | 0 |
| 코드 | 0 | 383 | 869 | 0 |
| 가중치 | 0 | 84 | 1,168 | 0 |
| 데이터 | 0 | 101 | 1,151 | 0 |
| 태그 | 1 | 395 | 857 | 0 |

링크는 대표 원문과 기재한 부가 주소별로 판정한다. 원문만 열리더라도 다른 링크의 판정은 유지한다. 잘못된 주소를 걷어낸 뒤 대체 주소가 확인되지 않은 경우에는 그 역할이 미확인이다. 저자의 공개 표명이나 배포 파일로 코드·가중치·데이터를 각각 판단한다. 배포 근거를 찾지 못한 상태는 ‘존재 불확실’이다. 기존 요약 판정에는 overview 대신 검증한 정규화 배치의 요약·기여를 대상으로 명시한 70편이 포함된다. 논문별 근거의 `scope`에서 대상 텍스트를 확인할 수 있다.

## 읽기 등급별 확인 범위

| 등급 | 논문 | 전 항목 통과 | 요약·기여 미확인 | 태그 미확인 | 공개 여부 중 한 가지 이상 미확인 |
|---|---:|---:|---:|---:|---:|
| CORE | 50 | 13 | 0 | 0 | 36 |
| NEXT | 450 | 6 | 261 | 360 | 433 |
| REFERENCE | 510 | 0 | 440 | 366 | 504 |
| ARCHIVE | 242 | 0 | 198 | 131 | 242 |

## 배치별 결과

| 배치 | 논문별 원장 행 | 편수 | 전 항목 통과 | 미확인 | 수정 필요 |
|---:|---|---:|---:|---:|---:|
| <a id="batch-01"></a>1 | [pr-0001–pr-0100](../work/sources/batches/source_audit_2026_11.jsonl#L1-L100) | 100 | 5 | 95 | 0 |
| <a id="batch-02"></a>2 | [pr-0101–pr-0200](../work/sources/batches/source_audit_2026_11.jsonl#L101-L200) | 100 | 0 | 100 | 0 |
| <a id="batch-03"></a>3 | [pr-0201–pr-0300](../work/sources/batches/source_audit_2026_11.jsonl#L201-L300) | 100 | 0 | 100 | 0 |
| <a id="batch-04"></a>4 | [pr-0301–pr-0400](../work/sources/batches/source_audit_2026_11.jsonl#L301-L400) | 100 | 0 | 100 | 0 |
| <a id="batch-05"></a>5 | [pr-0401–pr-0500](../work/sources/batches/source_audit_2026_11.jsonl#L401-L500) | 100 | 0 | 100 | 0 |
| <a id="batch-06"></a>6 | [pr-0501–pr-0600](../work/sources/batches/source_audit_2026_11.jsonl#L501-L600) | 100 | 2 | 98 | 0 |
| <a id="batch-07"></a>7 | [pr-0601–pr-0700](../work/sources/batches/source_audit_2026_11.jsonl#L601-L700) | 100 | 3 | 97 | 0 |
| <a id="batch-08"></a>8 | [pr-0701–pr-0800](../work/sources/batches/source_audit_2026_11.jsonl#L701-L800) | 100 | 2 | 98 | 0 |
| <a id="batch-09"></a>9 | [pr-0801–pr-0900](../work/sources/batches/source_audit_2026_11.jsonl#L801-L900) | 100 | 3 | 97 | 0 |
| <a id="batch-10"></a>10 | [pr-0901–pr-1000](../work/sources/batches/source_audit_2026_11.jsonl#L901-L1000) | 100 | 2 | 98 | 0 |
| <a id="batch-11"></a>11 | [pr-1001–pr-1100](../work/sources/batches/source_audit_2026_11.jsonl#L1001-L1100) | 100 | 0 | 100 | 0 |
| <a id="batch-12"></a>12 | [pr-1101–pr-1200](../work/sources/batches/source_audit_2026_11.jsonl#L1101-L1200) | 100 | 0 | 100 | 0 |
| <a id="batch-13"></a>13 | [pr-1201–pr-1252](../work/sources/batches/source_audit_2026_11.jsonl#L1201-L1252) | 52 | 2 | 50 | 0 |

## 이전 감사

- 11월 19일의 파일 진단은 당시 1,227편의 태그 표기, 중복 의심, 발표일 해상도를 점검했다. 비슷한 제목으로 잡힌 GR00T N1.5와 N1.6은 별도 판본으로 유지했다. 정식 발표일이 연도 단위인 항목에서 최근 6개월 비중을 확정할 수 없다. [당시 분모·검사 기준](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/REGISTRY_AUDIT.md) · [현행 통계](./REGISTRY_STATS.md)
- 같은 날 집중 읽기 477편 중 CORE 30편·NEXT 20편의 층화표본에서는 10/50편에서 11개 오류를 고쳤다. 당시 두 등급 모집단의 가중 추정은 11.7%였다. [50편의 원문·추출법·판정](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/SAMPLE_AUDIT.md)
- 11월 20일 첫 전수 감사의 **교정 전** 발견률은 109/1,252편(8.71%), 132개 필드였다. 그 뒤 272편에서 380개 필드의 증거를 보강하며 42편의 오류 44건을 교정했다. 각 시점의 오류는 같은 논문에서 겹칠 수 있다. [당시 13개 배치와 논문별 표](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/SOURCE_AUDIT.md)

## 논문별 조회

한 논문의 현재 10개 판정, 최초 판정, 교정 전후 값과 원문 출처를 안정 ID로 조회한다. 전체 보고서는 같은 원장에서 생성된다.

```bash
python3 work/scripts/render_source_audit.py --paper pr-0027
python3 work/scripts/render_source_audit.py --verify-corrections
```
