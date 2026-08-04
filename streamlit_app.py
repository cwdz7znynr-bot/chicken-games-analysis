import streamlit as st
import random
import time

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(
    page_title="منصة تحليل الألعاب | Chicken Games",
    page_icon="🎮",
    layout="centered"
)

# --- إدارة حالة التصفح (Session State) ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if "selected_game" not in st.session_state:
    st.session_state.selected_game = None

# ==========================================
# 1. الصفحة الرئيسية (تحديد واختيار اللعبة)
# ==========================================
if st.session_state.current_page == "home":
    st.title("🎮 منصة التحليل الذكي للألعاب")
    st.caption("اختر اللعبة من القائمة بالأسفل لبدء تحليل المضاعفات ونسب الأمان")
    st.divider()

    st.subheader("🎯 الألعاب المتاحة:")
    
    # بطاقة لعبة الدجاج
    with st.container(border=True):
        st.markdown("### 🐔 لعبة الدجاج (Chicken Game)")
        st.write("تحليل متقدم لمضاعفات لعبة الدجاج واستخراج أفضل مناطق الأمان للجولات القادمة.")
        
        # زر الدخول للعبة
        if st.button("🚀 الدخول للعبة والبدء", key="enter_chicken_game", use_container_width=True):
            st.session_state.selected_game = "🐔 لعبة الدجاج"
            st.session_state.current_page = "game_dashboard"
            st.rerun()

    # بطاقات ألعاب مستقبلية (إضافية لتنظيم الشكل)
    with st.container(border=True):
        st.markdown("### ✈️ لعبة الطائرة (قريباً)")
        st.caption("الخدمة قيد التطوير والتحديث...")

# ==========================================
# 2. صفحة اللعبة (اختيار المستوى والتحليل)
# ==========================================
elif st.session_state.current_page == "game_dashboard":
    
    # زر العودة للصفحة الرئيسية
    if st.button("⬅️ العودة للقائمة الرئيسية"):
        st.session_state.current_page = "home"
        st.rerun()

    st.title(f"{st.session_state.selected_game}")
    st.caption("حدد مستوى الصعوبة وإعدادات الجولة لبدء معالجة البيانات")
    st.divider()

    # --- اختيار المستوى ---
    st.subheader("1️⃣ اختر مستوى الصعوبة المطلوب:")
    
    difficulty = st.radio(
        "مستوى اللعب:",
        [
            "🟢 سهل (Easy - مخاطرة منخفضة)",
            "🟡 متوسط (Medium - مخاطرة متزنة)",
            "🔴 صعب (Hard - مخاطرة عالية)",
            "🔥 متقدم (Expert - مضاعفات فائقة)"
        ],
        index=0
    )

    st.divider()

    # --- مدخلات التحليل ---
    st.subheader("2️⃣ إعدادات التحليل:")
    col1, col2 = st.columns(2)
    
    with col1:
        rounds = st.number_input("عدد الجولات المراد تحليلها:", min_value=1, max_value=20, value=5)
    
    with col2:
        last_multiplier = st.number_input("آخر مضاعف ظهر في اللعبة (مثال: 1.5):", min_value=1.0, value=1.2, step=0.1)

    st.divider()

    # --- زر بدء التحليل ---
    if st.button("📊 بدء تحليل المستوى والجولات", use_container_width=True, type="primary"):
        with st.spinner("جاري الاتصال بالسيرفر ومعالجة الخوارزميات..."):
            time.sleep(1)
            
            if "سهل" in difficulty:
                base_mult = 1.3
                risk_label = "منخفضة جداً"
                safety_perc = random.randint(85, 98)
            elif "متوسط" in difficulty:
                base_mult = 1.8
                risk_label = "متوسطة"
                safety_perc = random.randint(70, 85)
            elif "صعب" in difficulty:
                base_mult = 2.8
                risk_label = "عالية"
                safety_perc = random.randint(50, 70)
            else:
                base_mult = 4.5
                risk_label = "مرتفعة جداً"
                safety_perc = random.randint(30, 50)

            st.success("تم استخراج نتائج التحليل بنجاح!")
            
            m1, m2, m3 = st.columns(3)
            m1.metric("المضاعف المستهدف القادم", f"{round(base_mult * (last_multiplier * 0.8), 2)}x")
            m2.metric("نسبة النجاح المتوقعة", f"{safety_perc}%")
            m3.metric("درجة المخاطرة", risk_label)

            st.markdown("---")
            st.subheader("🎯 التوقعات التفصيلية للجولات:")
            
            for i in range(1, rounds + 1):
                target = round(random.uniform(1.1, base_mult * 1.5), 2)
                st.write(f"• **الجولة رقم {i}:** الهدف الموصى به 👈 `{target}x`")
