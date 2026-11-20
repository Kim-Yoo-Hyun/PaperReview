# 논문 표본 감사

2026-11-19 KST 기준. 집중 읽기 대상 477편에서 CORE 30편과 NEXT 20편을 무작위로 뽑아 원장의 서지·공개 상태, overview의 한 줄 요약·핵심 기여, 태그를 대조했다. 50편 모두 원문을 식별했다. 41편은 PDF 앞부분 최대 네 쪽, 9편은 저자 HTML 원문에서 문제·방법·기여를 확인했다. 각 표의 논문명은 대조한 로컬 노트로 연결된다. [원장](../work/sources/papers.json) · [등급표](./READING_TIERS.csv) · [파일 기반 진단](./REGISTRY_AUDIT.md)

공개 여부 후속 점검에서 JALA의 구현은 공식 저장소에서 식별할 수 없었고, Ctrl-World의 새 환경 예제는 실제 디렉토리를 확인했다. 아래 원표는 최초 표본 감사 시점의 결과다. [최신 공개 판정과 수정 이력](../work/update/REGISTRY.md#외부-목록-대조와-core-심화-감사)

## 확정 오류 수정 결과

2026-11-19에 최초 판정 ‘오’ **11건을 10편에서 수정했다**. 아래 오류율과 논문별 판정표는 수정 전 표본을 보존한 기록이다. 수정 뒤 동일한 11개 항목을 다시 대조했다.

| 논문 · ID | 판정 항목 | 수정 후 확인한 내용 |
|---|---|---|
| CLIP · 0005 | 요약·데이터 | 이미지와 텍스트의 대조학습, zero-shot 분류를 원 기여로 기록했다. 저자 모델 카드의 Data 절에 따라 WIT를 미공개로 분류했다. [논문](https://proceedings.mlr.press/v139/radford21a.html) · [모델 카드](https://github.com/openai/CLIP/blob/main/model-card.md#data) |
| DDPM · 0008 | 요약 | 예측 대상은 추가한 가우시안 잡음이며 역확산 결과는 이미지다. 행동 생성은 후속 로봇 정책과의 연결로 설명했다. [논문](https://arxiv.org/html/2006.11239) |
| LIBERO · 0042 | 제목 | 공식 제목 **LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning**을 원장·노트·읽기 목록에 반영했다. [게재본](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) |
| Octo · 0052 | 요약 | 저자 각주 대신 여러 로봇의 시연으로 사전학습한 정책과 새 관측·행동 공간으로의 전이를 설명했다. [게재본](https://www.roboticsproceedings.org/rss20/p090.html) |
| ACT / ALOHA · 0566 | 데이터 | 저자 배포 폴더에서 시뮬레이션 시연을 확인해 공개로 기록했다. 공개 범위를 데이터 설명에 명시했고 구현 링크도 연결했다. [저장소](https://github.com/tonyzhaozh/act) · [시연 폴더](https://drive.google.com/drive/folders/1gPR03v05S1xiInoVJn7G7VJ9pDCnxq9O?usp=share_link) |
| PhysicsGen · 0651 | 링크 | 학회 원문 주소를 논문 필드에 유지하고 프로젝트 필드를 저자 사이트로 교체했다. 저자가 코드에 표시한 상태는 ‘Coming Soon’이다. [프로젝트](https://lujieyang.github.io/physicsgen/) |
| π₀ · 0746 | 요약 | 모델명과 행동 모듈을 바로잡고, 저자의 세탁물 접기 실험과 서론의 선행 연구 사례를 구분했다. [논문](https://arxiv.org/html/2410.24164) |
| FAST · 0749 | 요약 | 손상된 방법명을 복원하고 DCT·양자화·BPE 기반 행동 토크나이저와 이를 사용한 π₀-FAST 정책을 구분했다. [논문](https://arxiv.org/html/2501.09747) |
| TDQC · 0816 | 링크 | 404를 반환한 루트 주소를 논문별 프로젝트 주소로 교체하고 저자 구현을 연결했다. [프로젝트](https://shellytechnion.github.io/TDQC.github.io/) · [저장소](https://github.com/shellytechnion/TDQC) |
| Policy Gradient Methods · 0838 | 요약 | 타 연구에 대한 언급을 기여 위치에서 걷어내고, 정책 경사 정리와 호환 함수 근사의 조건을 기록했다. [게재본](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html) |

## 수정 전 오류율

| 논문당 한 번 집계 | CORE | NEXT | 표본 전체 | CORE/NEXT 477편 가중 추정 |
|---|---:|---:|---:|---:|
| 등록 내용·대상에서 오류 확인 | 8/30 | 2/20 | **10/50 (20.0%)** | **11.7%** |
| 오류 또는 근거가 확인된 보완 필요 | 23/30 | 14/20 | **37/50 (74.0%)** | **70.7%** |

가중 추정의 보수적 95% 구간은 **확인된 오류 2.9–34.8%**, **오류·보완 합계 45.5–88.9%**다. NEXT 427편 중 20편만 뽑았기 때문에 추정 폭이 크다. 각 층의 오류 편수에 대해 초기하분포 양측 97.5% 구간을 역산하고 두 층의 하한·상한을 각각 합했다. 이 구간은 표본 추출의 불확실성만 반영한다.

‘오류’는 원문과 충돌하는 기재, 손상된 제목·요약, 주소·링크 대상 오류다. ‘보완’은 공식 배포를 확인했으나 원장에 미기록·미식별·프로젝트만으로 남은 경우와 과업을 오해하게 하는 태그다. 미확정 판정은 분모 50에 남기고 오류 분자에서 제외했다. 따라서 위 수치는 이번 검사에서 발견한 비율이다. 저자란을 필수 완성도로 평가하면 50편 모두 보완 대상이 된다.

**해석.** CORE/NEXT의 코드·가중치·데이터 기록과 저자 필드는 **전수 검증이 필요하다**. 저자명은 표제면과 학회 서지의 순서가 다른 사례까지 있어 판본·출처를 함께 적어야 한다. 자동 추출 요약에서는 저자 각주나 다른 연구에 대한 언급이 기여 문장을 대체했다. 같은 형식의 노트를 우선 대조할 근거가 있다. 표본 밖 REFERENCE·ARCHIVE 750편의 오류율까지 추정하려면 두 등급에서도 독립적으로 표본을 뽑아야 한다.

## 수정 전 항목별 판정

각 칸은 논문 수다. ‘오’와 ‘보’는 모두 **수정 필요**, ‘통’은 **통과**, ‘?’는 **존재 불확실**이다. ‘?’에는 비교할 등록값 부재, 접근 제한, 배포 범위 미확정이 포함된다. 공개 여부의 대표 판정은 코드·가중치·데이터에서 오 → 보 → ? → 통 순으로 골랐다. 유형마다 같은 논문이 다시 집계될 수 있다.

| 점검 항목 | 통과 | 수정 필요 · 오류 | 수정 필요 · 보완 | 존재 불확실 |
|---|---:|---:|---:|---:|
| 링크 | 43 | 2 | 0 | 5 |
| 제목 | 49 | 1 | 0 | 0 |
| 저자 일치 | 0 | 0 | 0 | 50 |
| 연도 | 50 | 0 | 0 | 0 |
| 발표처·게재 상태 | 50 | 0 | 0 | 0 |
| 한 줄 요약·기여 | 44 | 6 | 0 | 0 |
| 공개 여부 · 논문 단위 | 1 | 2 | 32 | 15 |
| ↳ 코드 | 19 | 0 | 26 | 5 |
| ↳ 가중치 | 1 | 0 | 19 | 30 |
| ↳ 데이터 | 6 | 2 | 19 | 23 |
| 태그 | 48 | 0 | 2 | 0 |

- **저자.** 원장에 대조할 정규 저자 목록이 없다. overview에는 40편이 미기재 안내 문구를 두고, 10편은 저자 항목 자체가 없다. 표에는 출처의 저자 한 명을 식별자로 제시했다. SayCan의 PMLR 서지는 Brian Ichter, 표제면은 Michael Ahn부터 시작한다. Octo는 팀 이름과 개별 저자 표기를 병용한다. Mobility VLA도 PMLR 서지와 PDF의 선두 저자가 다르다. 이 차이를 로컬 저자 오기로 세지 않았다.
- **서지·링크.** 등록 주 URL과 기재된 프로젝트·코드 주소가 해당 대상으로 열리는지를 확인했다. 리디렉션 뒤 내용이 맞으면 통과다. 브라우저 확인 화면, 202 빈 응답, 403·429는 접근 보류다. 저자 저장소 안의 외부 파일 링크 장애는 해당 가중치·데이터 판정에 반영했다. 연도는 해당 판본의 학회 개최연도 또는 논문집 발행연도와 대조했고, 서로 다른 경우 행에 둘 다 적었다. arXiv 판본은 확인한 공개 상태로 평가했다.
- **요약·태그.** overview의 첫 설명과 핵심 기여를 함께 읽고 원문의 적용 대상, 방법명, 기여 주체를 대조했다. 검색에 쓰이는 넓은 연관 태그는 인정했고, 정책 출력이나 실기 전이 여부를 혼동시키는 두 건은 보완으로 셌다.
- **공개 범위.** 방법 코드, 사전학습 모델이나 배포한 구성요소, 논문용으로 수집·가공·배포한 데이터와 자산을 각각 확인했다. 모의 환경, 특정 태스크, 일부 체크포인트에 한정되면 행에 명시했다. 저자 설명과 배포 트리·파일 목록·다운로드 안내를 근거로 삼았다. 소프트웨어 실행이나 대용량 파일 내용 검증은 감사 범위 밖이다. 외부 기반 모델·벤치마크 인용만으로는 해당 저작물의 공개 여부를 결정할 수 없다.

## 수정 전 논문별 결과

서지 다섯 칸과 공개 여부 세 칸은 머리글 순서로 읽는다. 공개 상태 **통/보/?**는 코드 기록 일치, 가중치 기록 보완, 자체 데이터 공개 미확정이다. 태그 열은 불일치만 표시하며 나머지는 통과다.

### CORE

| 논문 · ID | 확인한 서지 · 대표 저자 | 링크/제목/저자/연도/발표처 | 요약 | 코드/가중치/데이터 | 태그 | 확인 내용과 원문 근거 |
|---|---|---|---|---|---|---|
| [CLIP](../2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/01_overview.md) · 0005 | ICML 2021 · Alec Radford | 통/통/?/통/통 | 오 | 통/보/오 | — | 이미지·텍스트 대조학습과 zero-shot 분류가 원 기여다. 로봇 행동 폐루프 변경으로 적은 요약과 자체 WIT 학습 데이터를 해당 없음으로 둔 기록을 수정해야 한다. 모델 로더가 공식 가중치를 제공한다. [원문·서지](https://proceedings.mlr.press/v139/radford21a.html) · [프로젝트](https://github.com/openai/CLIP) · [모델 카드](https://github.com/openai/CLIP/blob/main/model-card.md) |
| [DDPM](../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) · 0008 | NeurIPS 2020 · Jonathan Ho | 통/통/?/통/통 | 오 | 통/?/통 | — | 자연영상 생성·노이즈 제거 학습을 로봇 행동 폐루프 변경으로 요약했다. 저자 모델·샘플 Dropbox는 오류 화면을 반환해 현재 가중치 배포를 확인할 수 없다. [원문·서지](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) · [본문](https://arxiv.org/html/2006.11239) · [프로젝트](https://github.com/hojonathanho/diffusion) · [가중치](https://www.dropbox.com/sh/pm6tn31da21yrx4/AABWKZnBzIROmDjGxpB6vn6Ja) |
| [SayCan](../2022/CoRL/2022_CoRL_Do-As-I-Can-Not-As-I-Say-Grounding-Language-in-Robotic-Aff/01_overview.md) · 0020 | CoRL 2022 · Brian Ichter | 통/통/?/통/통 | 통 | 보/?/보 | — | 언어 계획에 기술 수행 가능성을 반영한다. 저자 공개 범위는 모의 탁상 구현과 지시–해법 매핑 v0다. 전체 실기 시스템 가중치 공개는 미확인. CoRL 2022, 논문집 2023. [원문·서지](https://proceedings.mlr.press/v205/ichter23a.html) · [저장소](https://github.com/google-research/google-research/tree/master/saycan) · [자료](https://github.com/say-can/say-can.github.io/tree/main/data) |
| [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md) · 0030 | RSS 2023 · Krishna Murthy Jatavallabhula | 통/통/?/통/통 | 통 | 보/?/? | — | 개방어휘 시각 특징을 3D 지도에 융합하는 구현이 있다. 저장소의 UnCoCo 배포 항목은 TODO다. 외부 특징 추출기 가중치는 구별했다. [원문·서지](https://www.roboticsproceedings.org/rss19/p066.html) · [저장소](https://github.com/concept-fusion/concept-fusion) |
| [RVT](../2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/01_overview.md) · 0037 | CoRL 2023 · Ankit Goyal | 통/통/?/통/통 | 통 | 보/보/보 | — | 가상 다중 시점으로 3D 조작 행동을 예측한다. 원 RVT 가중치와 저자가 재배포한 태스크별 replay가 있으며 RVT-2와 경로가 구분된다. [원문·서지](https://proceedings.mlr.press/v229/goyal23a.html) · [저장소](https://github.com/NVlabs/RVT) · [가중치](https://huggingface.co/ankgoyal/rvt/tree/main/rvt) · [자료](https://huggingface.co/datasets/ankgoyal/rvt/tree/main/replay) |
| [LIBERO](../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) · 0042 | NeurIPS 2023 · Bo Liu | 통/오/?/통/통 | 통 | 보/?/보 | — | 공식 제목의 첫 단어 LIBERO가 등록 제목에서 빠졌다. 평생 로봇 학습 벤치마크의 코드와 시연 다운로드 스크립트가 공개돼 있다. [원문·서지](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) · [저장소](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| [Octo](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md) · 0052 | RSS 2024 · Dibya Ghosh | 통/통/?/통/통 | 오 | 보/보/? | — | 저자 알파벳순 표기 각주가 핵심 아이디어 첫 문장에 들어갔다. 원 기여는 여러 로봇 데이터로 학습하고 적응시킬 수 있는 범용 정책이다. 공개 코드와 Octo 모델 카드를 확인했다. [원문·서지](https://www.roboticsproceedings.org/rss20/p090.html) · [저장소](https://github.com/octo-models/octo) · [모델](https://huggingface.co/rail-berkeley/octo-base-1.5) |
| [Habitat](../2019/ICCV/2019_ICCV_Habitat-A-Platform-for-Embodied-AI-Research/01_overview.md) · 0500 | ICCV 2019 · Manolis Savva | 통/통/?/통/통 | 통 | 보/?/보 | — | 플랫폼의 시뮬레이터·학습 라이브러리와 PointNav 에피소드를 배포한다. 기반 장면의 라이선스는 각 데이터셋을 따른다. [원문·서지](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) · [저장소](https://github.com/facebookresearch/habitat-lab) · [자료](https://github.com/facebookresearch/habitat-lab/blob/main/DATASETS.md) |
| [PPO](../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) · 0524 | arXiv 2017 · John Schulman | 통/통/?/통/통 | 통 | 통/?/통 | — | 대리 목적함수로 여러 번 정책을 갱신한다. OpenAI Baselines에 구현이 있다. 등록된 2017년 arXiv 판본을 확인했다. [원문·서지](https://arxiv.org/abs/1707.06347) · [프로젝트](https://github.com/openai/baselines) |
| [VLFM](../2024/ICRA/2024_ICRA_VLFM-Vision-Language-Frontier-Maps-for-Zero-Shot-Semantic/01_overview.md) · 0540 | ICRA 2024 · Naoki Yokoyama | 통/통/?/통/통 | 통 | 통/보/? | — | 객체 범주를 목표로 frontier를 고르는 ObjectNav다. 리포지토리가 PointNav 하위 정책 가중치를 포함한다. VLFM 전체의 학습 가중치로 해석할 수 없다. [원문·서지](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610712) · [프로젝트](https://github.com/bdaiinstitute/vlfm) · [가중치](https://api.github.com/repos/rai-opensource/vlfm/git/trees/main?recursive=1) |
| [VLN-CE](../2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/01_overview.md) · 0541 | ECCV 2020 · Jacob Krantz | 통/통/?/통/통 | 통 | 보/보/보 | — | 연속 공간 지시 내비게이션 환경, R2R-VLNCE 에피소드와 CMA baseline 배포를 확인했다. [원문·서지](https://api.crossref.org/works/10.1007/978-3-030-58604-1_7) · [저장소](https://github.com/jacobkrantz/VLN-CE) · [프로젝트](https://jacobkrantz.github.io/vlnce/) |
| [ACT / ALOHA](../2023/RSS/2023_RSS_Learning-Fine-Grained-Bimanual-Manipulation-with-Low-Cost/01_overview.md) · 0566 | RSS 2023 · Tony Z. Zhao | 통/통/?/통/통 | 통 | 보/?/오 | — | 액션 청크 모방학습과 저비용 양팔 시스템을 제안한다. 시뮬레이션 시연 폴더가 공개돼 있어 데이터 해당 없음 표기는 틀렸다. [원문·서지](https://www.roboticsproceedings.org/rss19/p016.html) · [저장소](https://github.com/tonyzhaozh/act) · [시연 폴더](https://drive.google.com/drive/folders/1gPR03v05S1xiInoVJn7G7VJ9pDCnxq9O?usp=share_link) |
| [SAC](../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) · 0620 | ICML 2018 · Tuomas Haarnoja | 통/통/?/통/통 | 통 | 통/?/통 | — | 최대 엔트로피 off-policy actor–critic을 제안한다. 저자 구현은 원 ICML 판본을 명시한다. [원문·서지](https://proceedings.mlr.press/v80/haarnoja18b.html) · [프로젝트](https://github.com/haarnoja/sac) |
| [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md) · 0624 | ICLR 2022 · Ilya Kostrikov | ?/통/?/통/통 | 통 | 통/?/? | — | 등록 OpenReview는 브라우저 확인 화면이었다. ICLR 프로그램과 arXiv에서 동일 논문을 대조했다. D4RL은 재사용 평가 데이터다. [원문·서지](https://iclr.cc/virtual/2022/poster/5941) · [저자 원고](https://arxiv.org/abs/2110.06169) · [프로젝트](https://github.com/ikostrikov/implicit_q_learning) |
| [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md) · 0684 | ICLR 2024 · Nicklas Hansen | 통/통/?/통/통 | 통 | 보/보/보 | — | 잠재 세계 모델로 연속 제어를 수행한다. 저자는 단일·다중 태스크 체크포인트와 30·80태스크 데이터를 배포한다. [원문·서지](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) · [저장소](https://github.com/nicklashansen/tdmpc2) |
| [π₀](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) · 0746 | RSS 2025 · Kevin Black | ?/통/?/통/통 | 오 | 보/보/? | — | flow matching 행동 정책이다. 요약에 선행 과제 예시가 잘린 채 들어가고 모델명이 zo로 추출됐다. openpi에 원 π₀ 코드·체크포인트가 있다. released로 적힌 데이터의 범위와 원 학습 혼합물의 공개 여부는 미확인이다. [원문·서지](https://www.roboticsproceedings.org/rss21/p010.html) · [본문](https://arxiv.org/html/2410.24164) · [저장소](https://github.com/Physical-Intelligence/openpi) |
| [robomimic](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md) · 0747 | CoRL 2021 · Ajay Mandlekar | 통/통/?/통/통 | 통 | 보/보/보 | — | 오프라인 사람 시연 학습을 통제 비교한다. 원 연구의 v0.1 모델과 시연 데이터가 있다. CoRL 2021, 논문집 2022. [원문·서지](https://proceedings.mlr.press/v164/mandlekar22a.html) · [저장소](https://github.com/ARISE-Initiative/robomimic) · [가중치](https://robomimic.github.io/docs/model_zoo/robomimic_v0.1.html) |
| [FAST](../2025/RSS/2025_RSS_FAST-Efficient-Action-Tokenization-for-Vision-Language-Act/01_overview.md) · 0749 | RSS 2025 · Karl Pertsch | ?/통/?/통/통 | 오 | 보/보/? | — | 시계열 압축 기반 행동 토크나이저다. 요약에서 방법명이 FAS nple로 손상됐다. FAST 토크나이저와 π₀-FAST 배포가 구분된다. [원문·서지](https://www.roboticsproceedings.org/rss21/p012.html) · [본문](https://arxiv.org/html/2501.09747) · [저장소](https://github.com/Physical-Intelligence/openpi) · [모델](https://huggingface.co/physical-intelligence/fast) |
| [OpenVLA-OFT](../2025/RSS/2025_RSS_Fine-Tuning-Vision-Language-Action-Models-Optimizing-Speed/01_overview.md) · 0750 | RSS 2025 · Moo Jin Kim | 통/통/?/통/통 | 통 | 보/보/? | — | 병렬 행동 청크 예측을 포함한 미세조정이다. 저자 코드와 LIBERO-Spatial용 OFT 체크포인트가 있다. [원문·서지](https://www.roboticsproceedings.org/rss21/p017.html) · [본문](https://arxiv.org/html/2502.19645) · [저장소](https://github.com/moojink/openvla-oft) · [모델](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial) |
| [Impedance Control I](../1985/Journal-of-Dynamic-Syste/1985_Journal-of-Dynamic-Syste_Impedance-Control-An-Approach-to-Manipulation-Part-ITheory/01_overview.md) · 0825 | ASME JDSMC 1985 · Neville Hogan | ?/통/?/통/통 | 통 | ?/?/통 | — | 접촉에서 운동·힘의 동적 관계를 다룬 이론편이다. ASME 등록 주소는 접근 확인 화면이었다. MIT의 저자 원고와 출판사 기탁 DOI 메타데이터가 일치한다. [원문·서지](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/5/1384/files/2025/02/1985-impedance-control-an-approach-to-manipulation-part-I-theory.pdf) · [DOI 기록](https://api.crossref.org/works/10.1115/1.3140702) |
| [Policy Gradient Theorem](../1999/NeurIPS/1999_NeurIPS_Policy-Gradient-Methods-for-Reinforcement-Learning-with-Fu/01_overview.md) · 0838 | NeurIPS 1999 · Richard S. Sutton | 통/통/?/통/통 | 오 | ?/?/통 | — | 한 줄 요약과 핵심 아이디어 첫머리가 Konda·Tsitsiklis의 독립 결과를 가리킨다. 이 논문의 기여는 함수 근사와 결합한 정책 경사 정리다. 원장의 별도 method 필드는 이를 올바르게 설명한다. [원문·서지](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html) |
| [SERL](../2024/ICRA/2024_ICRA_SERL-A-Software-Suite-for-Sample-Efficient-Robotic-Reinfor/01_overview.md) · 0874 | ICRA 2024 · Jianlan Luo | ?/통/?/통/통 | 통 | 통/?/? | — | 실제 조작용 표본 효율적 RL 소프트웨어다. IEEE 등록 주소의 응답에는 본문이 없었다. DOI와 저자 arXiv가 일치한다. 로봇별 자체 수집 안내는 데이터 배포 증거에서 제외했다. [원문·서지](https://arxiv.org/abs/2401.16013) · [프로젝트](https://github.com/rail-berkeley/serl) · [DOI 기록](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610040) |
| [NaVILA](../2025/RSS/2025_RSS_NaVILA-Legged-Robot-Vision-Language-Action-Model-for-Navig/01_overview.md) · 0884 | RSS 2025 · An-Chieh Cheng | 통/통/?/통/통 | 통 | 통/보/보 | — | 중간 수준 내비게이션 행동과 보행 제어를 결합한다. 저자 모델·데이터 카드가 있다. 일부 영상은 ID·주석만 공개한다. [원문·서지](https://www.roboticsproceedings.org/rss21/p018.html) · [본문](https://arxiv.org/html/2412.04453) · [프로젝트](https://github.com/AnjieCheng/NaVILA) · [가중치](https://huggingface.co/a8cheng/navila-llama3-8b-8f) · [자료](https://huggingface.co/datasets/a8cheng/NaVILA-Dataset) |
| [ConRFT](../2025/RSS/2025_RSS_ConRFT-A-Reinforced-Fine-tuning-Method-for-VLA-Models-via/01_overview.md) · 0885 | RSS 2025 · Yuhui Chen | 통/통/?/통/통 | 통 | 보/?/? | — | 오프라인·온라인 단계와 사람 개입을 결합한 VLA 미세조정이다. 저자 구현을 확인했다. [원문·서지](https://www.roboticsproceedings.org/rss21/p019.html) · [본문](https://arxiv.org/html/2502.05450) · [저장소](https://github.com/cccedric/conrft) |
| [RLDG](../2025/RSS/2025_RSS_RLDG-Robotic-Generalist-Policy-Distillation-via-Reinforcem/01_overview.md) · 0886 | RSS 2025 · Charles Xu | 통/통/?/통/통 | 통 | 통/?/보 | — | 전문 RL 정책의 궤적으로 범용 정책을 학습한다. 저자 궤적이 공개돼 있다. 프로젝트의 데이터 수집·미세조정 지침 일부는 공개 예고 상태다. [원문·서지](https://www.roboticsproceedings.org/rss21/p028.html) · [본문](https://arxiv.org/html/2412.09858) · [자료](https://huggingface.co/datasets/charlesxu0124/RLDG) · [배포 안내](https://generalist-distillation.github.io/RLDG/) |
| [3D Diffusion Policy](../2024/RSS/2024_RSS_3D-Diffusion-Policy-Generalizable-Visuomotor-Policy-Learni/01_overview.md) · 0926 | RSS 2024 · Yanjie Ze | 통/통/?/통/통 | 통 | 보/?/보 | — | 점군 기반 확산 정책이다. 구현, 저자 시뮬레이션·실기 데이터 링크가 있다. 별도 RL expert 체크포인트는 DP3 정책과 구별했다. [원문·서지](https://www.roboticsproceedings.org/rss20/p067.html) · [저장소](https://github.com/YanjieZe/3D-Diffusion-Policy) · [프로젝트](https://3d-diffusion-policy.github.io/) |
| [DPPO](../2025/ICLR/2025_ICLR_Diffusion-Policy-Policy-Optimization/01_overview.md) · 0951 | ICLR 2025 · Allen Z. Ren | 통/통/?/통/통 | 통 | 통/보/보 | — | 확산 정책의 denoising을 정책 경사로 미세조정한다. 저자 저장소가 사전학습 모델과 전처리 데이터를 제공한다. [원문·서지](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html) · [저장소](https://github.com/irom-lab/dppo) |
| [Flow Q-Learning](../2025/ICML/2025_ICML_Flow-Q-Learning/01_overview.md) · 0952 | ICML 2025 · Seohong Park | 통/통/?/통/통 | 통 | 통/?/? | — | flow 행동 모델과 한 단계 actor 증류로 Q-learning을 구현한다. OGBench·D4RL 재사용과 원 저자의 별도 데이터 배포를 구별했다. [원문·서지](https://proceedings.mlr.press/v267/park25f.html) · [저장소](https://github.com/seohongpark/fql) |
| [GAE](../2016/ICLR/2016_ICLR_High-Dimensional-Continuous-Control-Using-Generalized-Adva/01_overview.md) · 1180 | ICLR 2016 · John Schulman | 통/통/?/통/통 | 통 | 보/?/? | — | 가치함수를 이용해 advantage의 편향·분산을 조절한다. 첫 저자 modular_rl에 GAE를 사용하는 TRPO·PPO 구현이 있다. arXiv 2015, ICLR 2016. [원문·서지](https://www.iclr.cc/archive/www/2016.html) · [등록 원문](https://arxiv.org/abs/1506.02438) · [저장소](https://github.com/joschu/modular_rl) |
| [Potential-based reward shaping](../1999/ICML/1999_ICML_Policy-invariance-under-reward-transformations-Theory-and/01_overview.md) · 1181 | ICML 1999 · Andrew Y. Ng | 통/통/?/통/통 | 통 | ?/?/? | — | potential 차이를 이용한 보상 변환의 정책 보존 조건을 제시한다. 저자 소장 원문과 공동 저자 출판 목록으로 ICML 1999를 대조했다. [원문·서지](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf) · [게재 근거](https://people.eecs.berkeley.edu/~russell/publications) |

### NEXT

| 논문 · ID | 확인한 서지 · 대표 저자 | 링크/제목/저자/연도/발표처 | 요약 | 코드/가중치/데이터 | 태그 | 확인 내용과 원문 근거 |
|---|---|---|---|---|---|---|
| [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md) · 0017 | NeurIPS 2021 · Zachary Teed | 통/통/?/통/통 | 통 | 통/보/? | — | 카메라 자세와 깊이를 반복 갱신한다. 저자 저장소가 droid.pth를 제공한다. [원문·서지](https://proceedings.neurips.cc/paper_files/paper/2021/hash/89fcd07f20b6785b92134bd6c1d0fa42-Abstract.html) · [저장소](https://github.com/princeton-vl/DROID-SLAM) |
| [ManiGaussian](../2024/ECCV/2024_ECCV_ManiGaussian-Dynamic-Gaussian-Splatting-for-Multi-task-Rob/01_overview.md) · 0208 | ECCV 2024 · Guanxing Lu | 통/통/?/통/통 | 통 | 보/?/? | — | 미래 장면 재구성으로 조작 표현을 학습한다. 공식 구현은 공개됐다. README의 체크포인트 링크는 파일이 없다는 응답이어서 가중치 판정을 보류했다. [원문·서지](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php) · [저장소](https://github.com/GuanxingLu/ManiGaussian) · [가중치](https://cloud.tsinghua.edu.cn/d/b09de0a8d23f41b9b4ee/) |
| [Room-to-Room](../2018/CVPR/2018_CVPR_Vision-and-Language-Navigation-Interpreting-Visually-Groun/01_overview.md) · 0539 | CVPR 2018 · Peter Anderson | 통/통/?/통/통 | 통 | 보/?/보 | — | Matterport3D 기반 경로 지시 데이터와 시뮬레이터를 공개했다. 원 장면 접근 조건과 R2R 지시 데이터 배포는 별개다. [원문·서지](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) · [저장소](https://github.com/peteanderson80/Matterport3DSimulator) · [프로젝트](https://bringmeaspoon.org/) |
| [PhysicsGen](../2025/RSS/2025_RSS_Physics-Driven-Data-Generation-for-Contact-Rich-Manipulati/01_overview.md) · 0651 | RSS 2025 · Lujie Yang | 오/통/?/통/통 | 통 | 통/?/? | — | 소수 시연을 접촉 제약에 맞춰 최적화해 궤적을 확장한다. 등록 프로젝트 링크가 학회 논문 자체를 반복한다. 저자 사이트의 코드는 Coming Soon이다. 동명 타 연구의 저장소는 제외했다. [원문·서지](https://www.roboticsproceedings.org/rss21/p053.html) · [본문](https://arxiv.org/html/2502.20382) · [저자 사이트](https://lujieyang.github.io/physicsgen/) |
| [Ctrl-World](../2026/ICLR/2026_ICLR_Ctrl-World-A-Controllable-Generative-World-Model-for-Robot/01_overview.md) · 0687 | ICLR 2026 · Yanjiang Guo | 통/통/?/통/통 | 통 | 보/보/? | — | 다중 시점 행동 조건부 세계 모델이다. 저자 구현과 모델 카드가 있다. 공개 DROID를 전체 자체 학습 자료로 간주하지 않았다. [원문·서지](https://iclr.cc/virtual/2026/poster/10011332) · [저장소](https://github.com/Robert-gyj/Ctrl-World) · [모델](https://huggingface.co/yjguo/Ctrl-World) |
| [UMPNet](../2022/RA-L/2022_RA-L_UMPNet-Universal-Manipulation-Policy-Network-for-Articulat/01_overview.md) · 0716 | RA-L 2022 · Zhenjia Xu | 통/통/?/통/통 | 통 | 보/보/보 | — | 관절 물체에 대한 상호작용 정책이다. 저자 코드·pretrained 모델·가공한 mobility URDF 배포처가 있다. 저자 서지에서 RA-L 2022를 대조했다. [저자 서지](https://ump-net.cs.columbia.edu/) · [등록 원문](https://arxiv.org/abs/2109.05668) · [저장소](https://github.com/columbia-ai-robotics/umpnet) |
| [SayPlan](../2023/CoRL/2023_CoRL_SayPlan-Grounding-Large-Language-Models-using-3D-Scene-Gra/01_overview.md) · 0720 | CoRL 2023 · Krishan Rana | 통/통/?/통/통 | 통 | ?/?/? | — | 3D 장면 그래프 검색·재계획으로 언어 계획을 확장한다. 저자 사이트에서 논문과 영상은 확인했다. 방법 구현, 가중치, 데이터 배포는 미확인이다. [원문·서지](https://proceedings.mlr.press/v229/rana23a.html) · [프로젝트](https://sayplan.github.io/) |
| [Factory](../2022/RSS/2022_RSS_Factory-Fast-Contact-for-Robotic-Assembly/01_overview.md) · 0736 | RSS 2022 · Yashraj Narang | 통/통/?/통/통 | 통 | 통/?/보 | 보 | 시뮬레이션의 접촉력과 문헌 실측치를 비교했다. sim-to-real 태그는 학습 정책의 실기 전이를 검색할 때 오분류를 만든다. 배포한 CAD·URDF 자산을 데이터로 셌다. [원문·서지](https://www.roboticsproceedings.org/rss18/p035.html) · [저장소](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs) · [자산 목록](https://api.github.com/repos/isaac-sim/IsaacGymEnvs/contents/assets/factory) |
| [TDQC](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) · 0816 | ICML 2026 · Shelly Francis-Meretzki | 오/통/?/통/통 | 통 | 보/?/? | — | 성공 확률의 순차 보정을 다룬다. 등록 프로젝트 루트는 404였다. 올바른 프로젝트와 저자 구현을 확인했다. README가 안내하는 SAFE 자료는 재사용 데이터다. [원문·서지](https://proceedings.mlr.press/v306/francis-meretzki26a.html) · [저자 사이트](https://shellytechnion.github.io/TDQC.github.io/) · [저장소](https://github.com/shellytechnion/TDQC) |
| [DreamDojo](../2026/ICML/2026_ICML_DreamDojo-A-Generalist-Robot-World-Model-from-Large-Scale/01_overview.md) · 0871 | ICML 2026 · Shenyuan Gao | 통/통/?/통/통 | 통 | 보/보/보 | 보 | 행동을 조건으로 미래 영상을 생성한다. generalist policy 태그는 행동을 출력하는 정책과 혼동시킨다. 코드·모델과 저자 안내 GR-1 배포분을 확인했다. 44k시간 전체 배포는 미확인이다. [원문·서지](https://proceedings.mlr.press/v306/gao26q.html) · [저장소](https://github.com/NVIDIA/DreamDojo) · [모델](https://huggingface.co/nvidia/DreamDojo) |
| [UMI](../2024/RSS/2024_RSS_Universal-Manipulation-Interface-In-The-Wild-Robot-Teachin/01_overview.md) · 0873 | RSS 2024 · Cheng Chi | 통/통/?/통/통 | 통 | 보/보/보 | — | 휴대형 그리퍼 시연을 로봇 정책 학습에 사용한다. Stanford 배포 목록에 Zarr 데이터와 cup 정책 체크포인트가 있다. [원문·서지](https://www.roboticsproceedings.org/rss20/p045.html) · [저장소](https://github.com/real-stanford/universal_manipulation_interface) · [가중치](https://real.stanford.edu/umi/data/pretrained_models/) · [자료](https://real.stanford.edu/umi/data/zarr_datasets/) |
| [SmolVLA](../2025/arXiv/2025_arXiv_SmolVLA-A-Vision-Language-Action-Model-for-Affordable-and/01_overview.md) · 0915 | arXiv 2025 · Mustafa Shukor | 통/통/?/통/통 | 통 | 통/보/보 | — | 경량 VLA의 공개 모델과 SO100 stacking 데이터가 있다. 원 arXiv 기록과 저자 공개 자료를 확인했다. 별도 정식 게재를 확정할 원전은 찾지 못했다. [원문·서지](https://arxiv.org/abs/2506.01844) · [모델](https://huggingface.co/lerobot/smolvla_base) · [자료](https://huggingface.co/datasets/lerobot/svla_so100_stacking) · [저자 사이트](https://huggingface.co/blog/smolvla) |
| [3D-VLA](../2024/ICML/2024_ICML_3D-VLA-A-3D-Vision-Language-Action-Generative-World-Model/01_overview.md) · 0939 | ICML 2024 · Haoyu Zhen | 통/통/?/통/통 | 통 | 보/보/? | — | 3D 언어·행동 모델에 목표 생성기를 결합한다. 학습 코드와 목표 영상·점군 생성 가중치가 있다. 모든 행동 모듈 가중치 공개로 확대할 수 없다. [원문·서지](https://icml.cc/virtual/2024/poster/34575) · [본문](https://arxiv.org/html/2403.09631) · [저장소](https://github.com/UMass-Embodied-AGI/3D-VLA) · [모델 카드](https://github.com/UMass-Embodied-AGI/3D-VLA/blob/main/docs/model_card.md) |
| [Habitat 2.0](../2021/NeurIPS/2021_NeurIPS_Habitat-2.0-Training-Home-Assistants-to-Rearrange-their-Ha/01_overview.md) · 0948 | NeurIPS 2021 · Andrew Szot | 통/통/?/통/통 | 통 | 보/?/보 | — | 물체 재배치 환경·벤치마크·ReplicaCAD를 제시한다. 코드와 공개 장면 84개를 확인했다. 저자는 21개를 평가용으로 유보한다. [원문·서지](https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html) · [저장소](https://github.com/facebookresearch/habitat-lab) · [자료](https://aihabitat.org/datasets/replica_cad/) |
| [Beyond Binary Success](../2026/RSS/2026_RSS_Beyond-Binary-Success-Sample-Efficient-and-Statistically-R/01_overview.md) · 1028 | RSS 2026 · David Snyder | 통/통/?/통/통 | 통 | 보/?/보 | — | 로봇 정책을 순차적으로 비교한다. NSCORE 패키지와 평가용 수치 배열이 있다. 배열을 로봇 원시 시연 영상으로 분류하면 안 된다. [원문·서지](https://roboticsproceedings.org/rss22/p076.html) · [저장소](https://github.com/dasnyder5/nscore) · [배포 파일](https://api.github.com/repos/dasnyder5/nscore/git/trees/main?recursive=1) |
| [Mobility VLA](../2025/CoRL/2025_CoRL_Mobility-VLA-Multimodal-Instruction-Navigation-with-Long-C/01_overview.md) · 1063 | CoRL 2025 · Zhuo Xu | 통/통/?/통/통 | 통 | ?/?/? | — | 시연 투어에서 목표 프레임을 선택하고 위상 그래프로 이동한다. 학회 2024·PMLR 2025가 원장의 두 연도와 맞는다. 표의 저자는 게재본 순서다. [원문·서지](https://proceedings.mlr.press/v270/xu25b.html) · [저자 원고](https://arxiv.org/abs/2407.07775) |
| [Legato](../2026/RSS/2026_RSS_Learning-Native-Continuation-for-Action-Chunking-Flow-Poli/01_overview.md) · 1086 | RSS 2026 · Yufeng Liu | 통/통/?/통/통 | 통 | 통/?/? | — | flow 정책이 액션 청크를 이어서 생성하도록 학습한다. 공개 Kinetix 구현이 사용하는 기존 RTC 체크포인트·데이터와 논문에서 학습한 최종 실기 정책을 구별했다. [원문·서지](https://roboticsproceedings.org/rss22/p058.html) · [저장소](https://github.com/lyfeng001/Legato-kinetix) · [자산 목록](https://storage.googleapis.com/storage/v1/b/rtc-assets/o?prefix=bc%2F&maxResults=5) |
| [JALA](../2026/CVPR/2026_CVPR_Joint-Aligned-Latent-Action-Towards-Scalable-VLA-Pretraini/01_overview.md) · 1134 | CVPR 2026 · Hao Luo | 통/통/?/통/통 | 통 | 통/?/? | — | 실제 행동과 역동역학에 잠재 행동을 정렬한다. 공식 저장소 트리에는 README와 문서용 이미지가 있다. 이 범위에서 실행 구현 미공개 표기는 맞는다. [원문·서지](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html) · [저장소](https://github.com/BeingBeyond/JALA) · [파일 목록](https://api.github.com/repos/BeingBeyond/JALA/git/trees/main?recursive=1) |
| [Ψ₀](../2026/RSS/2026_RSS_An-Open-Foundation-Model-Towards-Universal-Humanoid-Loco-M/01_overview.md) · 1204 | RSS 2026 · Songlin Wei | 통/통/?/통/통 | 통 | 통/통/통 | — | 휴머노이드 이동 조작 모델이다. 원장이 코드·모델·데이터 공개를 이미 기록했다. 저자 코드와 모델·데이터 파일 목록을 대조했다. [원문·서지](https://www.roboticsproceedings.org/rss22/p021.html) · [저장소](https://github.com/physical-superintelligence-lab/Psi0) · [모델](https://huggingface.co/usc-psi-lab/psi-model) · [자료](https://huggingface.co/datasets/usc-psi-lab/psi-data) |
| [RFMPose](../2025/NeurIPS/2025_NeurIPS_RFMPose-Generative-Category-level-Object-Pose-Estimation-v/01_overview.md) · 1211 | NeurIPS 2025 · Wenzhe Ouyang | 통/통/?/통/통 | 통 | 통/?/? | — | 회전 다양체 위의 flow로 물체 자세 분포를 모델링한다. 저자 구현에 학습·추론 스크립트가 있다. Omni6DPose를 재사용하며 자체 체크포인트 배포는 미확인이다. [원문·서지](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) · [저장소](https://github.com/shabiouyang/RMFPose) |

## 표본 재현과 추정 범위

추출 단위는 논문 `paper_id`다. 등급표의 ID를 각 층에서 오름차순 정렬한 뒤 Python 표준 라이브러리의 동일한 `Random(20261119)` 인스턴스로 CORE 30편, 이어서 NEXT 20편을 비복원 추출했다. 표는 층 안에서 ID순으로 정렬했다. 접근 실패로 교체한 논문은 없다.

```python
import csv
import random

with open("research/READING_TIERS.csv", encoding="utf-8", newline="") as source:
    rows = list(csv.DictReader(source))

rng = random.Random(20261119)
for tier, count in [("CORE", 30), ("NEXT", 20)]:
    population = sorted(row["paper_id"] for row in rows if row["tier"] == tier)
    print(tier, sorted(rng.sample(population, count)))
```

CORE는 50편 중 30편, NEXT는 427편 중 20편을 뽑았다. 집중 읽기 대상의 추정 비율은 `(50 × CORE 표본 비율 + 427 × NEXT 표본 비율) / 477`이다. 표본 추출이 보장하는 대표성은 이 두 층에 한정되며, 자료 공개 상태와 외부 링크는 확인일 이후 달라질 수 있다.
