import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="💌 MBTI 이상형 남자친구 국가 찾기",
    page_icon="💘",
    layout="centered"
)

# 힙하고 커스텀된 사랑스러운 CSS 스타일 적용
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff5f7 0%, #eecda3 100%);
        font-family: 'Pretendard', sans-serif;
    }
    
    .main-title {
        text-align: center;
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 24px;
        box-shadow: 0 10px 25px rgba(255, 182, 193, 0.3);
        margin-bottom: 2rem;
        border: 2px solid #ffb6c1;
    }
    .main-title h1 {
        color: #ff4757;
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .recommend-card {
        background: white;
        padding: 2rem;
        border-radius: 24px;
        box-shadow: 0 12px 30px rgba(255, 71, 87, 0.15);
        border: 2px solid #ffeaa7;
        margin-top: 1.5rem;
        text-align: center;
    }
    
    /* 카드 내부 이미지 둥글고 감성적이게 만드는 스타일 */
    .bf-img {
        width: 100%;
        max-height: 380px;
        object-fit: cover;
        border-radius: 18px;
        margin: 1.2rem 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    
    .country-title {
        color: #2f3542;
        font-size: 2rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    .tag {
        display: inline-block;
        background: #ffeaa7;
        color: #d63031;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 0.88rem;
        font-weight: 700;
        margin: 3px;
    }
    .char-box {
        background: #fff0f3;
        border-radius: 16px;
        padding: 1.2rem;
        margin-top: 1rem;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI별 이미지 URL 포함 데이터
bf_data = {
    "INTJ": {
        "country": "독일 🇩🇪",
        "concept": "지적이고 든든한 뇌섹남 훈남",
        "img": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=800&q=80",
        "tag": "#개념충만 #체계적 #은근한스윗함 #나만바라봐",
        "desc": "논리적이고 자기관리 완벽한 스타일! 겉은 차가워 보여도 너의 고충을 스마트하게 해결해주고 오직 너에게만 다정한 츤데레 매력이 가득해 💙"
    },
    "INTP": {
        "country": "일본 🇯🇵",
        "concept": "고즈넉한 감성의 칠(Chill)한 미소년",
        "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80",
        "tag": "#자유로운영혼 #개성파 #취향존중 #아기자기",
        "desc": "너만의 엉뚱하고 깊은 생각들을 온전히 이해해주는 매력남! 함께 조용한 LP 바나 감성 카페를 찾아다니며 소소하고 깊은 대화를 나누기 딱이야 💙"
    },
    "ENTJ": {
        "country": "미국 🇺🇸",
        "concept": "당당하고 에너제틱한 야망 직진남",
        "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=800&q=80",
        "tag": "#자신감폭발 #파워풀 #솔직담백 #서포터",
        "desc": "너의 꿈과 목표를 누구보다 강력하게 응원해주는 리더십형 댕댕이! 함께 멋진 미래를 설계하며 힙하고 활기찬 데이트를 즐길 수 있어 💙"
    },
    "ENTP": {
        "country": "스페인 🇪🇸",
        "concept": "위트 넘치고 정열적인 티키타카 장인",
        "img": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=800&q=80",
        "tag": "#장난기가득 #도파민자극 #흥부자 #매력폭발",
        "desc": "지루할 틈이 전혀 없는 인싸남! 너의 엉뚱한 아이디어에 찰떡같이 장단을 맞춰주고 매일 밤 새로운 모험으로 이끌어줄 거야 💙"
    },
    "INFJ": {
        "country": "영국 🇬🇧",
        "concept": "세심하고 클래식한 젠틀맨",
        "img": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=800&q=80",
        "tag": "#다정한매너 #깊은감성 #어른스러운 #로맨틱",
        "desc": "너의 섬세한 감정 선을 먼저 알아채주는 따뜻한 젠틀맨! 조용한 미술관 데이트와 따뜻한 차 한 잔 나누며 평생 다정한 편이 되어줄 사람이야 💙"
    },
    "INFP": {
        "country": "프랑스 🇫🇷",
        "concept": "낭만과 예술을 사랑하는 몽상가 남친",
        "img": "https://images.unsplash.com/photo-1480429370139-e0132c086e2a?auto=format&fit=crop&w=800&q=80",
        "tag": "#시인감성 #소울메이트 #사랑꾼 #예술가풍",
        "desc": "너의 말 한마디에도 시적인 의미를 부여해주는 낭만파! 에펠탑 아래서 널 위한 노래를 들려줄 것 같은 달콤하고 사랑스러운 매력덩어리 💙"
    },
    "ENFJ": {
        "country": "이탈리아 🇮🇹",
        "concept": "스윗함 한도초과 사랑 표현 장인",
        "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80",
        "tag": "#칭찬폭격기 #햇살남친 #아낌없는사랑 #인생샷전문가",
        "desc": "눈만 마주치면 예쁘다고 해주는 인간 비타민! 너를 세계 최고의 주인공으로 만들어주고 모든 친구들에게 널 자랑하고 싶어 하는 직진꾼이야 💙"
    },
    "ENFP": {
        "country": "브라질 🇧🇷",
        "concept": "해피 바이러스 뿜뿜 텐션짱 남친",
        "img": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=800&q=80",
        "tag": "#긍정왕 #사랑스러운댕댕이 #어디서나핫플 #텐션업",
        "desc": "너와 함께라면 언제 어디든 축제로 만드는 열정남! 너의 톡톡 튀는 발랄함을 그대로 사랑해주고 매일 색다른 재미를 선사할 거야 💙"
    },
    "ISTJ": {
        "country": "스위스 🇨🇭",
        "concept": "바위처럼 든든하고 신뢰감 100% 남친",
        "img": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=800&q=80",
        "tag": "#약속신봉자 #안정감 #진국인남자 #따스한휴식",
        "desc": "변함없는 마음으로 널 지켜주는 든든한 소나무 같은 사람! 세심한 계획과 아늑한 자연 속 힐링으로 네 마음에 완벽한 평온을 줄 거야 💙"
    },
    "ISFJ": {
        "country": "캐나다 🇨🇦",
        "concept": "다정함이 배어있는 인간 핫팩",
        "img": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=800&q=80",
        "tag": "#배려심끝판왕 #무한한공감 #세심함 #힐링포옹",
        "desc": "네가 말하지 않아도 필요한 걸 챙겨주는 세심함의 대명사! 따뜻한 코코아처럼 너의 지친 하루를 감싸주는 쏘스윗한 휴식처 같은 사람 💙"
    },
    "ESTJ": {
        "country": "싱가포르 🇸🇬",
        "concept": "세련되고 능숙한 스마트 도시남",
        "img": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=800&q=80",
        "tag": "#갓생러 #세련된감각 #효율성갑 #확실한클래스",
        "desc": "자기 일도 연애도 스마트하게 잘해내는 뇌섹 매력남! 완벽한 데이트 코스와 힙한 루프탑 바에서 널 스마트하게 케어해줄 거야 💙"
    },
    "ESFJ": {
        "country": "호주 🇦🇺",
        "concept": "친근하고 스포티한 대형견 남친",
        "img": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=800&q=80",
        "tag": "#볼매 #친화력갑 #댕댕미 #다정다감",
        "desc": "너의 친구들과도 금방 친해지는 밝고 친근한 인싸! 주말마다 예쁜 야외로 피크닉을 떠나서 널 웃게 만들어줄 건강하고 다정한 남친이야 💙"
    },
    "ISTP": {
        "country": "핀란드 🇫🇮",
        "concept": "무심한 듯 다정한 쿨내 나는 츤데레",
        "img": "https://images.unsplash.com/photo-1513956589380-bad6acb9b9d4?auto=format&fit=crop&w=800&q=80",
        "tag": "#개인영역존중 #은근한챙김 #손재주꾼 #쿨가이",
        "desc": "불필요한 잔소리 없이 너의 자유를 100% 존중해주는 쿨남! 말보다는 묵묵히 행동으로 고장 난 걸 고쳐주거나 필요한 걸 딱 건네주는 반전 매력 💙"
    },
    "ISFP": {
        "country": "태국 🇹🇭",
        "concept": "평화롭고 아기자기한 힐링 감성남",
        "img": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=800&q=80",
        "tag": "#느림의미학 #소소한행복 #예쁜감성 #편안함",
        "desc": "너의 여유로운 속도에 맞춰주는 세상 순한 힐링남! 맛있는 거 먹고 예쁜 소품숍 구경하면서 소소하지만 가장 행복한 순간들을 선물해 줄 거야 💙"
    },
    "ESTP": {
        "country": "미국 (하와이) 🌺",
        "concept": "스릴과 낭만을 즐기는 만능 액티비티남",
        "img": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=800&q=80",
        "tag": "#도파민파티 #쿨하고솔직 #순발력갑 #해양스포츠",
        "desc": "고민은 짧게, 즐거움은 길게! 드라이브나 서핑처럼 액티브한 데이트로 너의 스트레스를 단번에 날려줄 스트리트 힙스터 남친 💙"
    },
    "ESFP": {
        "country": "멕시코 🇲🇽",
        "concept": "흥과 사랑이 넘치는 로맨틱 핫가이",
        "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80",
        "tag": "#사랑에올인 #매일이파티 #비주얼킹 #표현력만점",
        "desc": "너와 함께 있는 순간순간을 인생의 황금기로 만들어주는 열정 가득 남친! 신나는 음악과 눈부신 바다에서 널 안고 춤춰줄 직진 연하남 스타일 💙"
    }
}

# 헤더 영역
st.markdown("""
    <div class="main-title">
        <h1>💘 MBTI 감성 이상형 남친 국가 파인더</h1>
        <p style="color: #ff6b81; font-size: 0.98rem; font-weight: 600;">너의 성향과 찰떡궁합인 힙하고 사랑스러운 남자친구는 어느 나라 사람일까? 💙</p>
    </div>
""", unsafe_allow_html=True)

# MBTI 선택 박스
mbti_list = list(bf_data.keys())
selected_mbti = st.selectbox(
    "✨ 너의 MBTI를 선택해줘!",
    options=mbti_list,
    index=None,
    placeholder="여기 눌러서 MBTI 선택하기..."
)

# 선택 시 결과 출력 (사진 포함)
if selected_mbti:
    info = bf_data[selected_mbti]
    tags = "".join([f'<span class="tag">{t}</span>' for t in info["tag"].split()])
    
    st.balloons()
    
    # 1. 상단 카드 정보
    st.markdown(f"""
        <div class="recommend-card">
            <p style="color: #ff4757; font-weight: 800; font-size: 1.1rem; margin-bottom: 0px;">💖 {selected_mbti}만을 위한 운명의 이상형</p>
            <div class="country-title">{info['country']}</div>
            <p style="color: #57606f; font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">"{info['concept']}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. 이미지 표시 (Streamlit 순정 함수 - 이 부분이 핵심!)
    st.image(info['img'], use_container_width=True)
    
    # 3. 하단 태그 및 설명
    st.markdown(f"""
        <div class="recommend-card" style="margin-top: 0.5rem;">
            <div style="margin-bottom: 1rem;">{tags}</div>
            <div class="char-box">
                <p style="color: #2f3542; line-height: 1.65; margin: 0; font-size: 0.98rem;">
                    {info['desc']}
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
