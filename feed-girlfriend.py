# ================= 1. 代理设置 (必须放在最开头!) =================
import os

# 您的代理端口是 33210
# (如果将来在没有梯子的服务器上运行，请注释掉这两行)
os.environ["HTTP_PROXY"] = "http://127.0.0.1:33210"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:33210"

print("🔍 正在检查代理设置:", os.environ.get("HTTP_PROXY"))

# ================= 2. 导入依赖库 =================
import datetime
import requests
import json
from google import genai

# ================= 3. 配置区域 =================
# 飞书 Webhook (这里填入自己的飞书webhook地址)
FEISHU_WEBHOOK = ""

# Google API Key (填入的 Key)
API_KEY = ""

# 女友昵称(需要在飞书机器人的关键词里面添加这个昵称)
NICKNAME = "小羊"


# ================= 4. AI 生成逻辑 =================
def get_ai_copy(meal_type):
    """根据时间生成对应的温柔文案"""
    week_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    today_week = week_list[datetime.datetime.now().weekday()]

    # 提示词：您可以随时调整这里的语气要求
    prompt = f"你是一个温柔男朋友，给女友{NICKNAME}发微信提醒吃{meal_type}。今天是{today_week}，语气温柔宠溺，100字以内，带emoji。请直接输出文案。"

    print(f"🤖 正在请求 Google 生成{meal_type}文案...")

    try:
        # 初始化客户端
        client = genai.Client(api_key=API_KEY)

        # 调用模型 (保持您测试通过的 gemini-3-flash-preview)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",  # 如果3-preview不稳定，这里自动回退到2.0稳定版，您也可以改回 3-preview
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"❌ AI 生成失败: {e}")
        return None


# ================= 5. 飞书发送逻辑 =================
def send_to_feishu(title, content):
    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": title,
                    "content": [[{"tag": "text", "text": content}]]
                }
            }
        }
    }
    try:
        resp = requests.post(FEISHU_WEBHOOK, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        if resp.status_code == 200:
            print(f"✅ 发送成功！\n文案内容：{content}")
        else:
            print(f"❌ 飞书拒绝: {resp.text}")
    except Exception as e:
        print(f"❌ 网络异常: {e}")


# ================= 6. 主程序 (自动判断时间) =================
def main():
    # 获取当前小时 (0-23)
    hour = datetime.datetime.now().hour

    # 这里的逻辑是：
    # 早餐：6点到9点 (包含6点，不包含10点)
    # 午餐：11点到13点
    # 晚餐：17点到19点

    if 6 <= hour < 10:
        meal = "早餐"
        title = "☀️ 早安投喂"
    elif 11 <= hour < 14:
        meal = "午餐"
        title = "🍱 午餐时间到"
    elif 17 <= hour < 20:
        meal = "晚餐"
        title = "🌙 晚餐休息站"
    else:
        # 如果不是饭点，直接退出
        print(f"🕐 现在是 {hour} 点，不是饭点，不打扰{NICKNAME}。")
        return

    # 如果在饭点，才执行下面的代码
    ai_text = get_ai_copy(meal)

    if ai_text:
        send_to_feishu(title, ai_text)
    else:
        # 备用方案（防止断网）
        print("⚠️ AI 生成失败，发送备用文案...")
        send_to_feishu(title, f"{NICKNAME}，虽然AI网卡了，但还是要记得按时吃{meal}哦！😘")


if __name__ == "__main__":
    main()
