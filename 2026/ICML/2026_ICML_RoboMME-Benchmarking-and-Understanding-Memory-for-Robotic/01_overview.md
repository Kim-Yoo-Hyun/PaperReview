# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICML
- Authors: Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang, Jianing Yang, Chelsea Finn, Nima Fazeli, Joyce Chai
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, memory, long-horizon manipulation
- Aliases:
- Official paper: https://proceedings.mlr.press/v306/dai26c.html
- Venue verification: https://proceedings.mlr.press/v306/dai26c.html
- Code/Project: https://robomme.github.io/
- Code: https://github.com/RoboMME/robomme_benchmark
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RoboMME는 현재 영상만으로 결정하기 어려운 조작 과제에서 범용 로봇 정책이 과거의 어떤 정보를 써야 하는지 평가한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/dai26c/dai26c.pdf#page=1)

## Core Idea and Contribution

- 시간 순서, 공간, 물체, 절차를 기억해야 하는 조건을 구분해 16개 과제를 설계했다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/dai26c/dai26c.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/dai26c/dai26c.pdf#page=4)
- π0.5에 여러 기억 표현과 결합 방식을 적용하고 어떤 조합이 유리한지가 필요한 기억의 종류에 따라 달라짐을 비교했다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/dai26c/dai26c.pdf#page=5) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/dai26c/dai26c.pdf#page=7) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/dai26c/dai26c.pdf#page=9)

## Observation–State–Action Interface

현재 관측·history representation → π0.5 기반 VLA → manipulation action.

## Evaluation Scope and Claim Boundary

16 manipulation task와 14 memory variant를 보고하며 memory 효용은 task에 의존한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/dai26c.html) · [저자 project/code](https://robomme.github.io/) · [공식 code](https://github.com/RoboMME/robomme_benchmark). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

현재 GAP-N1–N3의 직접 benchmark이며 memory 필요성과 단순 정보 누설을 구분하는 기준이다.

## Verification Boundary

task dictionary와 goal/evaluator, history cutoff, raw ID와 split을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 초판 RoboMME 평가기 · scripts/evaluation.py [배포 파일](https://raw.githubusercontent.com/RoboMME/robomme_benchmark/45efbf21036b40af201b24a6d5d37f0d1b088c64/scripts/evaluation.py)
- 가중치 — MME-VLA 시각 기억 표본화 정책 · perceptual-framesamp-context/79999.zip [배포 파일](https://huggingface.co/Yinpei/mme_vla_suite/blob/5db4d53ddb98c7f80cab08792dd53d985d712ab1/perceptual-framesamp-context/79999.zip)
- 데이터 — BinFill 작업 기록 · record_dataset_BinFill.h5.tar.xz [배포 파일](https://huggingface.co/datasets/Yinpei/robomme_data_h5/blob/a5e4e25ffe8af34f64944f9533d06455ce5f8337/record_dataset_BinFill.h5.tar.xz)
