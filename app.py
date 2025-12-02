import streamlit as st
import google.generativeai as genai
import requests
import json
import re

st.set_page_config(page_title="AI 内容中台 (调试版)", page_icon="🐞")
st.title("🐞 飞书内容中台 - 深度调试模式")

# ==========================================
# 1. 检查 Secrets (最常见的问题是这里没配好)
# ==========================================
st.subheader("第一步：检查环境配置")
try:
    # 尝试读取 Secrets
    GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")
    FEISHU_APP_ID = st.secrets.get("FEISHU_APP_ID")
    FEISHU_APP_SECRET = st.secrets.get("FEISHU_APP_SECRET")
    FEISHU_APP_TOKEN = st.secrets.get("FEISHU_APP_TOKEN")
    FEISHU_TABLE_ID = st.secrets.get("FEISHU_TABLE_ID")

    # 检查是否有空值
    if not all([GOOGLE_API_KEY, FEISHU_APP_ID, FEISHU_APP_SECRET, FEISHU_APP_TOKEN, FEISHU_TABLE_ID]):
        st.error("❌ 错误：Secrets 配置不完整！请检查 Streamlit 后台 Settings -> Secrets。")
        st.write("目前读取到的状态：")
        st.json({
            "GOOGLE_KEY": "✅ 有值" if GOOGLE_API_KEY else "❌ 空",
            "FEISHU_ID": "✅ 有值" if FEISHU_APP_ID else "❌ 空",
            "FEISHU_SECRET": "✅ 有值" if FEISHU_APP_SECRET else "❌ 空",
            "FEISHU_TOKEN": "✅ 有值" if FEISHU_APP_TOKEN else "❌ 空",
            "FEISHU_TABLE": "✅ 有值" if FEISHU_TABLE_ID else "❌ 空",
        })
        st.stop() # 停止运行
    else:
        st.success("✅ 环境配置读取成功！")

except Exception as e:
    st.error(f"❌ 读取 Secrets 发生严重错误: {e}")
    st.info("请确保你的 Secrets 格式是 TOML 格式（即 key = \"value\"）")
    st.stop()

# ==========================================
# 2. 定义核心函数 (带日志)
# ==========================================

def get_feishu_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    st.info("正在向飞书申请 Token...")
    try:
        resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET})
        data = resp.json()
        if data.get("code") == 0:
            st.write("✅ 飞书 Token 获取成功")
            return data.get("tenant_access_token")
        else:
            st.error(f"❌ 飞书 Token 失败: {data}")
            return None
    except Exception as e:
        st.error(f"❌ 网络请求报错: {e}")
        return None

def push_to_feishu(data):
    token = get_feishu_token()
    if not token: return

    # 清洗 Table ID (去掉 &view=xxx)
    clean_table_id = FEISHU_TABLE_ID.split("&")[0]
    
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{FEISHU_APP_TOKEN}/tables/{clean_table_id}/records"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    # 构造数据
    fields = {
        "主题": data.get("topic", "无"),
        "爆款标题": data.get("title", "无"),
        "脚本正文": data.get("script", "无")
    }
    
    st.write("📤 准备写入飞书的数据：")
    st.json(fields) # 打印出来给你看

    try:
        resp = requests.post(url, headers=headers, json={"fields": fields})
        res_json = resp.json()
        
        st.write("📥 飞书返回结果：")
        st.json(res_json) # 打印飞书的回复

        if res_json.get("code") == 0:
            st.balloons()
            st.success("🎉 写入成功！")
        else:
            st.error(f"❌ 写入失败！请检查上方返回的 msg 错误信息。通常是列名不对。")
    except Exception as e:
        st.error(f"❌ 写入请求报错: {e}")

def generate(topic):
    st.info("正在呼叫 Google Gemini (美国节点)...")
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = f"""
        分析主题：【{topic}】。
        要求：只输出纯JSON。字段包含：topic, title(爆款标题), script(口播文案)。
        不要使用Markdown标记。
        """
        
        response = model.generate_content(prompt)
        st.write("🤖 Gemini 原始回复：")
        st.code(response.text) # 打印原始回复
        
        # 清洗
        text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception as e:
        st.error(f"❌ AI 生成失败: {e}")
        return None

# ==========================================
# 3. 界面交互
# ==========================================
st.markdown("---")
st.subheader("第二步：执行操作")
topic = st.text_input("输入一个测试主题:", value="测试内容")

if st.button("🚀 点击运行调试"):
    with st.spinner("流水线运行中..."):
        # 1. AI 生成
        data = generate(topic)
        
        # 2. 飞书写入
        if data:
            st.success("✅ JSON 解析成功，开始写入...")
            push_to_feishu(data)
        else:
            st.error("🚫 流程中断：AI 没有返回有效数据")
