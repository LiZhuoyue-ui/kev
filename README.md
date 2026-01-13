# 🐑 自动投喂小羊 (Auto Feed Sheep)

这是一个基于 Python 的自动化脚本，旨在每天定时（早、中、晚）通过 Google Gemini AI 生成温柔的情话与用餐提醒，并通过飞书机器人（Feishu Bot）发送给女朋友。

## 📂 文件说明

- **`feed_sheep.py`**: 项目的主程序代码。包含了调用 Google Gemini API 和发送飞书 Webhook 的所有逻辑。
- **`.gitignore`**: 用于告诉 Git 忽略不需要上传的系统文件或敏感配置。

## 🚀 如何使用

### 1. 环境准备
确保你的电脑安装了 Python 3，并安装以下依赖库：
```bash
pip install requests google-genai
