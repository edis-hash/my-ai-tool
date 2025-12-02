import streamlit as st
import google.generativeai as genai
import requests
import json
import re

st.set_page_config(page_title="AI 内容中台 (Cloud版)", page_icon="☁️")

# === 从云端密钥库获取 Key ===
# 注意：如果 Secrets 还没配好，这里会报错。请确保在 Streamlit 网页后台填了 Secrets。
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    FEISHU_APP_ID = st.secrets["FEISHU_APP_ID"]
    FEISHU_APP_SECRET = st.secrets["FEISHU_APP_SECRET"]
    FEISHU_APP_TOKEN = st.secrets["FEISHU_APP_TOKEN"]
    FEISHU_TABLE_ID = st.secrets["FEISHU_TABLE_ID"]
except FileNotFoundError:
    st.error("❌ 尚未配置 Secrets！请在 Streamlit App 设置中填写 Key。")
    st.stop()

def get_feishu_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    try:
        resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET})
        return resp.json().get("tenant_access_token")
    except:
        return None

def push_to_feishu(data):
    token = get_feishu_token()
    if not token: return False
    
    # 注意：如果你的 Base 链接里包含 view=xxx，Table ID 只要 tbl 开头那一串
    clean_table_id = FEISHU_TABLE_ID.split("&")[0]
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{FEISHU_APP_TOKEN}/tables/{clean_table_id}/records"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    # ⚠️ 确保这里的 Key 和你飞书表格列名完全一致
    fields = {
        "主题": data.get("topic"),
        "爆款标题": data.get("title"),
        "脚本正文": data.get("script")
    }
    try:
        resp = requests.post(url, headers=headers, json={"fields": fields})
        return resp.json().get("code") == 0
    except:
        return False

def generate(topic):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"""
    分析主题：【{topic}】。
    要求：只输出纯JSON。字段包含：topic, title(爆款标题), script(口播文案)。
    不要使用Markdown标记。
    """
    try:
        response = model.generate_content(prompt)
        text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except:
        return None

# === 界面 ===
st.title("☁️ AI 爆款内容生成器")
topic = st.text_input("输入主题:")
if st.button("生成并推送") and topic:
    with st.spinner("AI 正在美国机房思考..."):
        data = generate(topic)
        if data:
            st.success("创意已生成！正在推送到飞书...")
            if push_to_feishu(data):
                st.balloons()
                st.success("✅ 成功写入飞书多维表格！")
            else:
                st.error("❌ 写入飞书失败，请检查列名或权限")
