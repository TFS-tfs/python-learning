# dream_interview.py - AI梦想访谈官 v0.1
import random

print("【筑梦坞】AI家访开始...\n")
print("你好，我是你的筑梦助理。我将通过几个问题，帮你找到最治愈你的空间感觉。")

# 问题库 - 用你的心理学洞察来设计
questions = [
    "当你需要绝对放松时，你脑海中最先浮现的画面是什么？（比如：雨中咖啡馆、被书包围、星空下）",
    "如果用一个比喻，你理想的家更像什么？（一个安全的巢穴？一个探险的基地台？一个藏满宝藏的阁楼？）",
    "闭上眼睛，感受一下：这个空间的空气是什么温度？光线是明亮还是昏暗？",
    "在这个家里，你最常做的一件事会是什么？（发呆、阅读、和朋友聊天、创作）",
    "如果这个家有一种气味，你希望它闻起来像什么？（旧书、雨后泥土、晒过的被子、松木）"
]

answers = []
for q in questions:
    print(f"\n{q}")
    ans = input("> ")
    answers.append(ans)

print("\n=== 基于你的回答，AI生成了一份《造梦简报》 ===")
print("【核心感觉】融合了" + answers[0] + "的" + answers[1] + "。")
print("【氛围】" + answers[2] + "，空气中弥漫着" + answers[4] + "的味道。")
print("【主要活动】这里最适合" + answers[3] + "。")
print("\n这份简报将发送给我们的筑梦师，为您量身打造。")
# 在原有脚本末尾添加
import json
import os
from datetime import datetime 
# 构建订单数据
order_data = {
    "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "answers": answers,
    "brief": {
        "核心感觉": f"融合了{answers[0]}的{answers[1]}",
        "氛围": f"{answers[2]}，空气中弥漫着{answers[4]}的味道",
        "主要活动": f"这里最适合{answers[3]}"
    },
    "ai_prompt": prompt  # 前面生成的提示词
}

# 确保orders文件夹存在
if not os.path.exists("orders"):
    os.makedirs("orders")

# 保存为JSON文件（用时间戳作为文件名）
filename = f"orders/order_{order_data['timestamp'].replace(':', '-')}.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(order_data, f, ensure_ascii=False, indent=2)

print(f"\n订单已保存至：{filename}")
print("这是我们收到的第{}份梦想订单！".format(len(os.listdir("orders"))))