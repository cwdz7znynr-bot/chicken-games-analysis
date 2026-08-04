import streamlit as st
import random
import time

# --- import streamlit as st
import random
import time

# --- إعدادات الصفحة الأساسية والتصميم المظلم ---
st.set_page_config(
    page_title="LARA AI INJECTOR",
    page_icon="⚡",
    layout="centered"
)

# تخصيص واجهة تشبه الواجهة الموضحة بالصورة
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .big-mult {
        font-size: 64px !important;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        margin: 10px 0;
        font-family: monospace;
    }
    .terminal-box {
        background-color: #000000;
        border: 1px solid #1a233a;
        border-radius: 8px;
        padding: 12px;
        font-family: monospace;
        color: #00ff66;
        font-size: 12px;
        height: 110px;
        overflow-y: auto;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- إدارة حالة التصفح (Session State) ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if "selected_game" not in st.session_state:
    st.session_state.selected_game = None

if "selected_difficulty" not in st.session_state:
    st.session_state.selected_difficulty = "EASY"

if "result_mult" not in st.session_state:
    st.session_state.result_mult = "0.00x"

# ==========================================
# 1. الصفحة الرئيسية (اختيار اللعبة من الـ 5)
# ==========================================
if st.session_state.current_page == "home":
    st.markdown("<h2 style='text-align: center;'>⚡ LARA AI INJECTOR</h2>", unsafe_allow_html=True)
    st.caption("اختر اللعبة لبدء عملية التحليل والأوامر")
    st.divider()

    # قائمة الألعاب الـ 5 الخاصة بك
    games = [
        {"name": "🐔 Chicken Road Core", "desc": "تحليل مسارات لعبة الدجاج الرئيسية"},
        {"name": "🐥 Chicken Cross", "desc": "تحليل مناطق العبور والتراجع"},
        {"name": "🐔 Golden Chicken", "desc": "استخراج مضاعفات الدجاجة الذهبية"},
        {"name": "🍗 Chicken Bonus", "desc": "تحليل جولات المكافآت والمضاعفات"},
        {"name": "🐣 Mini Chicken", "desc": "تحليل الجولات السريعة ذات المخاطرة"}
    ]

    for game in games:
        with st.container(border=True):
            st.markdown(f"### {game['name']}")
            st.write(game['desc'])
            if st.button(f"🚀 الدخول للعبة", key=game['name'], use_container_width=True):
                st.session_state.selected_game = game['name']
                st.session_state.current_page = "game_dashboard"
                st.session_state.result_mult = "0.00x"
                st.rerun()

# ==========================================
# 2. شاشة التحليل (مطابقة للصورة بالكامل)
# ==========================================
elif st.session_state.current_page == "game_dashboard":
    
    if st.button("⬅️ خروج / اختيار لعبة أخرى"):
        st.session_state.current_page = "home"
        st.rerun()

    st.markdown("<h3 style='text-align: center; color: #4b8bf5;'>LARA <span style='color:#00ff66;'>AI INJECTOR</span></h3>", unsafe_allow_html=True)
    st.caption(f"اللعبة الحالية: {st.session_state.selected_game}")
    
    # الإطار الموحد للتحليل (شكل الصورة)
    with st.container(border=True):
        st.markdown("<div style='text-align: center; color: #888; font-size: 12px;'>GATEWAY: ACTIVE &nbsp;&nbsp;|&nbsp;&nbsp; PING: 24ms</div>", unsafe_allow_html=True)
        
        # عرض المضاعف الرئيسي الكبيير
        st.markdown(f"<div class='big-mult'>{st.session_state.result_mult}</div>", unsafe_allow_html=True)

        # شاشة الترمينال / السجل
        current_time = time.strftime("%H:%M:%S")
        terminal_text = f"""
        [{current_time}] SYSTEM INITIALIZED...<br>
        [{current_time}] LOADING MODULES...<br>
        [{current_time}] {st.session_state.selected_game.upper()}...<br>
        [{current_time}] SELECTED LEVEL: {st.session_state.selected_difficulty}<br>
        [{current_time}] READY FOR OPERATION.
        """
        st.markdown(f"<div class='terminal-box'>{terminal_text}</div>", unsafe_allow_html=True)

        # أزرار اختيار المستوى (EASY, MEDIUM, HARD, HARDCORE)
        st.write("اختر مستوى الصعوبة:")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("EASY", use_container_width=True, type="primary" if st.session_state.selected_difficulty == "EASY" else "secondary"):
                st.session_state.selected_difficulty = "EASY"
                st.rerun()
            if st.button("HARD", use_container_width=True, type="primary" if st.session_state.selected_difficulty == "HARD" else "secondary"):
                st.session_state.selected_difficulty = "HARD"
                st.rerun()

        with col2:
            if st.button("MEDIUM", use_container_width=True, type="primary" if st.session_state.selected_difficulty == "MEDIUM" else "secondary"):
                st.session_state.selected_difficulty = "MEDIUM"
                st.rerun()
            if st.button("HARDCORE", use_container_width=True, type="primary" if st.session_state.selected_difficulty == "HARDCORE" else "secondary"):
                st.session_state.selected_difficulty = "HARDCORE"
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # زر بدء التحليل البرتقالي الكبير (ЗАПУСТИТЬ АНАЛИЗ / START ANALYSIS)
        if st.button("🔥 ЗАПУСТИТЬ АНАЛИЗ (بدء التحليل)", use_container_width=True, type="primary"):
            with st.spinner("جاري المعالجة والحساب..."):
                time.sleep(1)
                
                # توليد مضاعف بناءً على المستوى المحدد
                if st.session_state.selected_difficulty == "EASY":
                    val = round(random.uniform(1.10, 1.80), 2)
                elif st.session_state.selected_difficulty == "MEDIUM":
                    val = round(random.uniform(1.85, 3.50), 2)
                elif st.session_state.selected_difficulty == "HARD":
                    val = round(random.uniform(3.60, 7.50), 2)
                else: # HARDCORE
                    val = round(random.uniform(8.00, 25.00), 2)

                st.session_state.result_mult = f"{val}x"
                st.rerun()
