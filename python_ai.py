
import random
import time
"""
    游戏名：教室迷雾
    基于文件内容生成的 Python 核心逻辑演示代码
    """
# --- 基础配置类 ---


class GameConfig:
    GAME_NAME = "教室迷雾"
    TOTAL_TIME = 10  # 模拟天亮所需的回合数
    INITIAL_COINS = 100  # 各种族初始元币
# --- 角色基类 ---


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # '学生', '怪物', '中立'
        self.coins = GameConfig.INITIAL_COINS
        self.is_alive = True
        self.neutral_transform_count = 2  # 中立阵营变换机会
        self.current_identity = role  # 中立玩家当前的实际阵营

    def earn_coins(self, amount):
        self.coins += amount
        print(
            f"  --> [{self.role}] {self.name} 获得 {amount} 元币，当前总额: {self.coins}")
# --- 环境类：教室门窗 ---


class ClassroomEnvironment:
    def __init__(self, player_count):
        # 文件提及：每局开局通过固定算式得出门窗数量
        # 假设算式：门窗数 = 玩家数 / 2 + 随机波动
        self.total_doors_windows = int(
            player_count / 2) + random.randint(1, 3)
        self.durability = self.total_doors_windows * 100  # 总耐久度
        self.max_durability = self.durability
        print(
            f"[环境初始化] 本局门窗数量: {self.total_doors_windows}，总耐久度: {self.durability}")

    def is_broken(self):
        return self.durability <= 0

    def attack(self, damage):
        self.durability -= damage
        if self.durability < 0:
            self.durability = 0
        return damage

    def reinforce(self, amount):
        # 加固不能超过上限
        repair = min(amount, self.max_durability - self.durability)
        self.durability += repair
        return repair
# --- 游戏核心引擎 ---


class ClassroomMistGame:
    def __init__(self):
        self.players = []
        self.environment = None
        self.current_round = 0

    def add_player(self, name, role):
        self.players.append(Player(name, role))

    def start_game(self):
        print(f"======= 游戏《{GameConfig.GAME_NAME}》开始 =======")
        # 初始化环境
        self.environment = ClassroomEnvironment(len(self.players))
        # 游戏主循环
        while self.current_round < GameConfig.TOTAL_TIME and not self.environment.is_broken():
            self.current_round += 1
            print(
                f"\n--- 第 {self.current_round} 回合 (剩余 {GameConfig.TOTAL_TIME - self.current_round} 回合天亮) ---")
            self.process_round()
            time.sleep(0.5)  # 仅仅是演示效果
        self.end_game()

    def process_round(self):
        for player in self.players:
            if not player.is_alive:
                continue
            # 1. 怪物逻辑
            if player.role == "怪物":
                damage = random.randint(15, 30)
                actual_damage = self.environment.attack(damage)
                print(
                    f"[怪物] {player.name} 攻击门窗，造成 {actual_damage} 点伤害 (剩余耐久: {self.environment.durability})")
                # 文件规则：怪物通过攻击铁门获得元币
                player.earn_coins(actual_damage // 2)
            # 2. 学生逻辑
            elif player.role == "学生":
                reinforce_amount = random.randint(10, 20)
                actual_repair = self.environment.reinforce(
                    reinforce_amount)
                print(f"[学生] {player.name} 加固门窗，恢复了 {actual_repair} 点耐久")
                # 文件规则：学生通过坚守一定时间获得元币
                player.earn_coins(10)
            # 3. 中立逻辑
            elif player.role == "中立":
                # 文件规则：中立可以选择变换身份或看风景
                # 模拟：前几回合可能变换，否则挂机
                if player.neutral_transform_count > 0 and random.random() < 0.3:
                    new_role = random.choice(["学生", "怪物"])  # 简化逻辑，变身为学生或怪物
                    print(f"[中立] {player.name} 使用变身能力，变为了 [{new_role}]！")
                    player.role = new_role
                    player.current_identity = new_role
                    player.neutral_transform_count -= 1
                    # 变身后立即执行一次行动
                    if new_role == "学生":
                        player.earn_coins(10)
                    else:
                        self.environment.attack(20)
                else:
                    # 文件规则：挂机看风景
                    print(f"[中立] {player.name} 正在看风景聊天...")
                    # 中立也可以交易(此处省略复杂交易逻辑)
                    if random.random() < 0.2:
                        print(f"  --> {player.name} 进行了元币交易。")
                        player.earn_coins(5)

    def end_game(self):
        print("\n======= 游戏结束 =======")
        if self.environment.is_broken():
            print("【结果】门窗已被破坏，怪物入侵成功！")
            winners = [p for p in self.players if p.role == "怪物"]
            # 处理中立胜利条件
            neutral_winners = [
                p for p in self.players if p.role == "中立" and p.current_identity == "怪物"]
            self.announce_winners(winners + neutral_winners)
        else:
            print("【结果】天亮了，学生成功坚守！")
            winners = [p for p in self.players if p.role == "学生"]
            neutral_winners = [
                p for p in self.players if p.role == "中立" and p.current_identity == "学生"]
            self.announce_winners(winners + neutral_winners)
        # 未变身的中立玩家
        pure_neutral = [p for p in self.players if p.role == "中立"]
        for p in pure_neutral:
            print(f"  [中立-看风景] {p.name} 存活，得分最低。")

    def announce_winners(self, winners):
        if not winners:
            return
        print("胜利者列表：")
        for p in winners:
            # 文件规则：中立变换后按变换阵容结算
            print(f"  - {p.name} (最终身份: {p.role}) | 总资产: {p.coins}")


# --- 运行示例 ---
if __name__ == "__main__":
    game = ClassroomMistGame()
    # 添加玩家
    game.add_player("玩家A", "学生")
    game.add_player("玩家B", "学生")
    game.add_player("玩家C", "怪物")
    game.add_player("玩家D", "怪物")
    game.add_player("路人甲", "中立")
    game.start_game()
