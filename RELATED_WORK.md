# RELATED_WORK — 읽은 논문

형식: 논문마다 `무엇을 했나 / 무엇을 안 했나 / 내 연구와 차이`

| 논문 (저자, 연도, 출처) | 무엇을 했나 | 무엇을 안 했나 | 내 연구와 차이 |
|---|---|---|---|
| | | | |


## 읽을 예정 (2026-11-06 선정)

Park & Kang (2025) — Deformation-Aware Luminance Compensation using Gaussian-Weighted Kernels for Stretchable Displays
출처: SID Symposium Digest 2025, 27-4 (4쪽 학회 논문), doi:10.1002/sdtp.18165
확장판: JSID 2025 (아래 ### 항목)

무엇을 했나

문제: 스트레처블 디스플레이를 늘리면 픽셀 사이에 빈 픽셀(empty pixels)이 생겨 휘도가 떨어짐
방법: 빈 픽셀 근처에 가중치를 더 주는 Gaussian 커널로 주변 픽셀 휘도를 올림. 시청 거리(D)는 PSF 블러로 모델링 (식 7–8)
조건: 선형/비선형, 한 방향/두 방향 신장. 신장률 15·30%, D = 2·3·4
베이스라인: 보정 없음 / gamma (γ=1.2) / mean scaling
데이터·지표: Urban100 이미지 100장, SSIM·LPIPS·CIEDE2000
시뮬레이터를 만들어서 위 조건들을 비교

무엇을 안 했나 / 의심하는 점

기하 왜곡 보정 없음 (휘도만 다룸)
실제 패널 측정 없음. 시뮬레이터가 실제와 맞는지 검증도 없음
표준편차가 없어서 작은 차이가 의미 있는지 판단 불가 (예: 선형 30% Proposed CIEDE D3→D4: 12.49→12.64)
Gamma 베이스라인의 식·인용 없음 → 재현 불가. γ=1.2 "실험적 최적"(3쪽 오른쪽 단 Results), 제안 방법 BIR=1.1도 선정 근거 없음 (2쪽 왼쪽 단에 ">1"만). 둘 다 평가 데이터(Urban100)로 정했다면 같은 데이터 문제
본문은 "In all cases, the proposed method demonstrated superior numerical performance"라고 하는데 (4쪽 왼쪽 단, Results 끝), Table 1에서는 선형 30% D=3·4의 CIEDE2000에서 Gamma가 더 좋음 (12.19, 12.24 vs 12.49, 12.64)
CIEDE2000 값이 약 5~13으로, 보정 후에도 눈에 보이는 색차가 남음 (베이스라인보다 낫다 ≠ 충분히 좋다)
결론의 "상용화 가능성"은 이미지 시뮬레이션만으로는 근거가 약함
본문의 "Figure 1 shows…"는 Fig. 2 내용을 가리키는 번호 오류로 보임

내 연구와 차이

나는 기하 왜곡(1단계)과 휘도(2단계)를 같이 다룸
HW 파라미터(푸아송 비, 회로 보상, 섬·다리 강성)를 넣어 SW-HW 분담을 비교함. 이 논문은 SW만 다룸
시뮬레이터를 해석해·FEM·문헌 실측으로 검증할 계획 (이 논문엔 없음)
증명 기준에 절대 기준(ΔE 등)을 둠. 이 논문은 베이스라인 대비 상대 비교만 함
변형 시나리오를 안다고 가정함 → 내 후보 대안 "카메라로 변형 추정"이 이 빈틈을 다룸
확장판: Park & Kang (2025), JSID — Luminance compensation for stretchable displays using deep visual feature-optimized Gaussian-weighted kernels
출처: J. Soc. Inf. Display 2025, doi:10.1002/jsid.2052 (12쪽)
Digest 대비 달라진 점만 기록

1. 문제: Digest와 같음 (빈 픽셀로 인한 휘도 저하)

2. 방법

BIR(가장자리 밝기 배율, 커널 중심 1 → 가장자리 BIR)을 시나리오마다 LPIPS loss + Adam으로 미리 최적화 (Fig. 1, PDF 3쪽). Digest는 1.1로 고정, 선정 근거 없었음
실사용 시 시나리오에 맞는 BIR을 꺼내 셀별 커널 적용 → PSF
시나리오 확장: 신장률 10·20·30%, 단방향 / 같은 비율 양방향 / 다른 비율 양방향

3. 베이스라인: Gamma, Mean scaling (Digest와 같음)

Gamma는 Introduction(PDF 2쪽)에서 말로만 설명. 식·인용·γ 값 없음 (Digest는 γ=1.2라도 적혀 있었음) → 여전히 재현 불가

4. 검증 방식

Urban100을 나눠서 씀: 90장 BIR 최적화 / 10장 평가 (3.1 Datasets, PDF 7쪽) → Digest의 같은 데이터 문제는 해결
단, 평가 이미지가 10장뿐이고 표준편차 없음
여전히 시뮬레이션만. 실제 패널 측정·시뮬레이터 검증 없음

5. 의심하는 점 / 안 한 것

선형(Table 2, PDF 6쪽): CIEDE2000에서 지는 곳 많음. 10%,10% D=2(7.257, 꼴찌), 10%,20% D=2(12.288 vs Gamma 6.664). LPIPS로 최적화했는데 LPIPS에서도 지는 곳 있음 (단방향 10% D=3·4, 10%,20% D=2)
비선형(Table 3, PDF 7쪽): 단방향 30%는 D=2·3·4 전부 CIEDE 꼴찌. 10%,10%에서 D 3→4로 갈 때 CIEDE가 나빠짐 (4.268→4.422)
Table 3 CIEDE2000: 큰 쪽 비율이 같으면 조합이 달라도 값이 거의 같음 (SSIM·LPIPS는 다름). 설명 없음 → QUESTIONS
선형 vs 비선형 절대값은 비교 불가 (Gamma·Mean도 같이 좋아짐 → 문제 난이도 차이일 수 있음)
BIR 값(Table 1, PDF 5쪽): 비율·D에 따른 일관된 경향 없음 (단방향 D=2만 비율 따라 증가). 비율이 바뀌면 커널 크기도 같이 바뀌어 효과가 섞임 → 표에 없는 시나리오는 재최적화가 필요해 보임
결론(PDF 11쪽): "시나리오가 정해지면 제한 없이 적용 가능"이라는데, 실제 변형 시나리오를 알아내는 방법은 다루지 않음 (안다고 가정)
"real-time"이라고 주장하지만 처리 시간 측정 없음 ("designed to enable")
본인들도 한계로 인정한 것: BIR 최적화 데이터셋이 작고 다양하지 않음
나아진 점: 본문 표현이 "In all cases" → "across most stretching scenarios"로 표와 더 맞게 바뀜

## Jang et al. (2022) — Auxetic Meta-Display: Stretchable Display without Image Distortion
- 출처: Advanced Functional Materials 2022, 32, 2113299, doi:10.1002/adfm.202113299 (10쪽)

**무엇을 했나**
- 문제: 신축형 디스플레이 구현 시 높은 신축성, 균일한 변형, 낮은 이미지 왜곡을 동시에 달성해야 함 (보통 기판은 푸아송 효과로 가로세로 변형이 달라 이미지가 찌그러짐)
- 방법: 마이크로 LED + 키리가미 기반 오그제틱(음의 푸아송 비) 회로 기판(meta-PCB)을 설계·제작한 메타 디스플레이. 회전 사각형 + 힌지 구조로 푸아송 비 -1
- 비교 대상: PDMS 기판 (Fig. 3b 단축, Fig. 4 g–i 이축), 기존 플렉서블 디스플레이 (Fig. 5 e·f, 반구 부착)
  - Fig. 3b의 Natural rubber, Polyimide, Cork 등은 문헌값 기준선 (직접 측정 아님)
- 검증: 실제로 샘플을 만들어 당겨서 측정
  - 단축: 현미경 이미지로 변형률 측정 → 푸아송 비 계산, 24.5%까지 -1 유지 (Fig. 3, PDF 5쪽)
  - 이축(x·y 같은 비율 20%): DIC로 픽셀 위치 추적. meta-PCB는 균일, PDMS는 가장자리 변형률 최대 28%로 불균일 (Fig. 4, PDF 7쪽)
  - FEA: 힌지 부분 전극 변형률이 파괴 변형률 아래인지 확인용 (Fig. 3d)

**무엇을 안 했나 / 의심하는 점**
- SW 보정 없음 (HW로 왜곡 자체를 줄이는 접근)
- x·y를 다른 비율로 당긴 실험 없음 (단축, 같은 비율 이축만)
- 신축률 24.5%라고 내세우지만, 반복 인장 시험에서 완전 회복은 10.5%까지 (2.4절 끝, PDF 6쪽 왼쪽 단). 초록·결론엔 24.5%만 나옴
- 구면 부착 시 "이미지 왜곡 없음"은 사진(Fig. 5b)으로만 보여줌. 수치 측정 없음 (2.6절)
- 3인치판 반구 부착 시 22.6%까지 늘어남 → 탄성 한계 10.5% 초과. 떼어낸 뒤 회복 여부 안 나옴
- 반복 시험 세부(Figure S11, S12)는 보조자료에 있어 확인 못 함

**내 연구와 차이**
- 이 논문은 SW 보정 없음. HW 측면에서 왜곡이 일어나지 않는 새 기판을 설계·제작함
- 이 논문의 푸아송 비 -1을 시뮬레이터의 HW 파라미터로 넣고, 있을 때/없을 때 SW가 보정해야 할 왜곡량을 비교함
- 이 논문이 실험 안 한 불균일 변형(다른 비율 이축 등)에서 푸아송 비 -1이 왜곡을 얼마나 남기는지 시뮬레이터로 측정할 수 있음 (1단계 HW 확인 질문)
- 신장률 범위는 "한 번 늘리기 24.5% / 반복 사용 10.5%"로 나눠서 다룸


- Kio (2016), Distortion Correction for Non-Planar Deformable Projection Displays, 박사 논문
- Kang et al. (2022), AMOLED Pixel Circuit for Strain Compensation in Stretchable Display, SID Digest
- 확인 포인트: 기하 왜곡도 다뤘나? SW-HW 분담을 비교했나?