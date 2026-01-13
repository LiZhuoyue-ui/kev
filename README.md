### 🐍 `feed-girlfriend` (核心脚本)

这是项目的主程序文件，包含了时间判断、AI 调用和消息发送的所有逻辑。**在使用前，你需要打开此文件进行以下配置：**

#### 1. 必填配置 (Configuration)
你需要修改代码顶部的变量，填入你自己的密钥：
- **`FEISHU_WEBHOOK`**: 必须填入你的飞书群自定义机器人的 Webhook 地址（用于把消息发到群里）。
- **`API_KEY`**: 必须填入你的 Google Gemini API Key（没有这个 Key，AI 无法工作）。

#### 2. 高级玩法：自定义 Prompt (Customization)
你可以通过修改 `get_ai_copy` 函数中的 **`prompt` (提示词)** 变量，来完全改变机器人的说话风格！

* **默认设定**：`"你是一个温柔体贴的男朋友..."`
* **你可以改成任何你想要的**，例如：
    * 改成 **“严厉的健身教练”** -> 提醒该吃蛋白粉了。
    * 改成 **“古代诗人”** -> 用七言绝句提醒吃饭。
    * 改成 **“新闻播报员”** -> 正式地播报午餐时间。
    
> **💡 提示**：只要修改了 `prompt` 里的文字，AI 生成的内容就会随之变化，你可以利用这一点向群里发送任何你想要的主题内容（不仅仅是吃饭提醒）。
### 2. ⚙️ 关键配置 (Configuration)

打开 `feed_sheep.py` 文件，你需要修改以下 4 个地方才能让它跑起来：

#### 1. 基础填空
- **`FEISHU_WEBHOOK`**: 填入飞书机器人的 Webhook 地址。
- **`API_KEY`**: 填入 Google Gemini API Key。
- **`PROXY`**: 如果在国内 Mac/Windows 上运行，记得填入代理地址（如 `http://127.0.0.1:7890`）；如果在海外服务器，请注释掉。

#### 2. 💖 专属定制 (昵称与关键词)
- **修改代码中的 `NICKNAME`**:
  找到 `NICKNAME = "小羊"` 这一行，把“小羊”改成你女朋友的专属昵称。

- **⚠️ 重要：设置飞书机器人关键词**:
  你必须去 **飞书开放平台 -> 机器人安全设置 -> 自定义关键词** 中，把上面的昵称（例如“小羊”）填进去！
  > **原理**：飞书为了防止骚扰，要求消息里必须包含你设定的关键词才会放行。如果你代码里改了昵称，飞书后台没加这个词，消息发不出去！

#### 3. 📝 进阶玩法：自定义 Prompt
你可以修改 `get_ai_copy` 函数里的 `prompt` 变量。想让它变成“霸道总裁”还是“古代诗人”，全看你怎么写提示词！
*只要修改了 Prompt，你可以用这个脚本做任何事：比如每天发英语单词、发股市行情、或者发笑话。*

---

## 🔗 常用资源与工具 (Useful Links)

这里整理了项目中用到的 API 申请地址和相关网站，方便随时查阅：

**🤖 AI 模型 API 申请**
* **Google AI Studio (本项目推荐)**: [https://aistudio.google.com/](https://aistudio.google.com/)
    * *说明：免费额度高，速度快，申请最简单。*
* **Moonshot AI (Kimi)**: [https://platform.moonshot.cn/](https://platform.moonshot.cn/)
    * *说明：国内直连，中文能力强，无需代理。*
* **OpenAI (ChatGPT)**: [https://platform.openai.com/](https://platform.openai.com/)
    * *说明：最强模型，但需要国外信用卡。*
* **xAI (Grok)**: [https://console.x.ai/](https://console.x.ai/)
    * *说明：马斯克的 AI，风格幽默。*

**📢 消息推送平台**
* **飞书开放平台 (Feishu Open Platform)**: [https://open.feishu.cn/](https://open.feishu.cn/)
    * *说明：在这里创建机器人并获取 Webhook 地址。*

**🛠️ 其他工具**
* **Crontab Guru**: [https://crontab.guru/](https://crontab.guru/)
    * *说明：如果不确定定时任务的时间格式怎么写，可以在这个网站上在线测试（比如 `30 8 * * *` 是几点）。*
