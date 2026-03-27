    import tkinter as tk
    from tkinter import ttk, messagebox, scrolledtext
    import random
    import time
    class Barrier:
        """障碍物类：代表门窗"""
        def __init__(self, name, max_hp=100):
            self.name = name
            self.max_hp = max_hp
            self.hp = max_hp
        def repair(self, amount):
            self.hp = min(self.max_hp, self.hp + amount)
            return self.hp
        def damage(self, amount):
            self.hp = max(0, self.hp - amount)
            return self.hp
    class Player:
        """玩家基类"""
        def __init__(self, name, role):
            self.name = name
            self.role = role
            self.money = 50
            self.is_alive = True
    class ClassroomDefenseGame:
        def __init__(self, root):
            self.root = root
            self.root.title("教室保卫战 - GUI版")
            self.root.geometry("900x600")
            self.root.resizable(False, False)
            # 游戏核心数据
            self.time_elapsed = 0  # 单位：分钟
            self.dawn_time = 300   # 5小时天亮 (300分钟)
            self.is_game_over = False
            self.is_paused = True
            self.barriers = []
            self.players = []
            self.log_queue = []
            # 界面构建
            self.setup_ui()
            self.init_game()
        def setup_ui(self):
            """构建界面布局"""
            # --- 顶部状态栏 ---
            top_frame = tk.Frame(self.root, bg="#2c3e50", height=50)
            top_frame.pack(fill=tk.X, side=tk.TOP)
            self.lbl_time = tk.Label(top_frame, text="时间: 00:00 (倒计时: 05:00)", 
                                     font=("微软雅黑", 14, "bold"), bg="#2c3e50", fg="white")
            self.lbl_time.pack(pady=10)
            # --- 左侧：教室环境 ---
            left_frame = tk.LabelFrame(self.root, text="教室结构 (门窗状态)", 
                                       font=("微软雅黑", 10), padx=10, pady=10)
            left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
            self.barrier_frame = tk.Frame(left_frame)
            self.barrier_frame.pack(fill=tk.BOTH, expand=True)
            # --- 右侧：玩家与控制 ---
            right_frame = tk.Frame(self.root, width=300)
            right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
            right_frame.pack_propagate(False)
            # 玩家信息区
            info_frame = tk.LabelFrame(right_frame, text="我的状态", font=("微软雅黑", 10))
            info_frame.pack(fill=tk.X, pady=5)
            self.lbl_role = tk.Label(info_frame, text="角色: 学生", font=("微软雅黑", 12, "bold"), fg="#3498db")
            self.lbl_role.pack(pady=2)
            self.lbl_money = tk.Label(info_frame, text="元币: 50", font=("微软雅黑", 12))
            self.lbl_money.pack(pady=2)
            # 操作区
            action_frame = tk.LabelFrame(right_frame, text="行动操作", font=("微软雅黑", 10))
            action_frame.pack(fill=tk.X, pady=10)
            btn_style = {"font": ("微软雅黑", 10), "width": 20, "height": 2}
            self.btn_repair = tk.Button(action_frame, text="加固门窗 (消耗20元币)", 
                                        command=self.action_repair, bg="#27ae60", fg="white", **btn_style)
            self.btn_repair.pack(pady=5)
            self.btn_earn = tk.Button(action_frame, text="自习赚钱 (坚守奖励)", 
                                      command=self.action_earn_money, bg="#f1c40f", **btn_style)
            self.btn_earn.pack(pady=5)
            self.btn_switch = tk.Button(action_frame, text="叛变/变身 (改变阵营)", 
                                        command=self.action_switch_role, bg="#e67e22", fg="white", **btn_style)
            self.btn_switch.pack(pady=5)
            # 中立特殊按钮（初始隐藏）
            self.btn_trade = tk.Button(action_frame, text="交易物资 (中立专属)", 
                                       command=self.action_trade, bg="#95a5a6", **btn_style)
            # 敌方状态
            enemy_frame = tk.LabelFrame(right_frame, text="战场情报", font=("微软雅黑", 10))
            enemy_frame.pack(fill=tk.X, pady=5)
            self.lbl_enemy_status = tk.Label(enemy_frame, text="怪物数量: ?\n中立数量: ?", justify=tk.LEFT)
            self.lbl_enemy_status.pack(pady=5)
            # --- 底部：日志 ---
            log_frame = tk.Frame(self.root)
            log_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
            self.log_text = scrolledtext.ScrolledText(log_frame, height=6, state='disabled', 
                                                      font=("Consolas", 9), bg="#ecf0f1")
            self.log_text.pack(fill=tk.X)
            # 开始按钮
            self.btn_start = tk.Button(right_frame, text="开始游戏", font=("微软雅黑", 12, "bold"),
                                       bg="#2980b9", fg="white", command=self.toggle_game)
            self.btn_start.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        def init_game(self):
            """初始化游戏数据"""
            self.time_elapsed = 0
            self.is_game_over = False
            self.is_paused = True
            self.btn_start.config(text="开始游戏")
            # 1. 生成环境
            self.barriers = []
            num_doors = 2
            num_windows = 3 + random.randint(0, 2)
            for widget in self.barrier_frame.winfo_children():
                widget.destroy()
            for i in range(num_doors):
                b = Barrier(f"前门_{i+1}")
                self.barriers.append(b)
                self.create_barrier_ui(b)
            for i in range(num_windows):
                b = Barrier(f"窗户_{i+1}")
                self.barriers.append(b)
                self.create_barrier_ui(b)
            # 2. 生成玩家 (玩家扮演第一个学生，其余AI)
            self.players = [Player("我(玩家)", "学生")]
            roles = ["学生", "学生", "怪物", "怪物", "中立"]
            for i in range(5):
                p = Player(f"AI_{i+1}", random.choice(roles))
                self.players.append(p)
            self.update_player_ui()
            self.add_log("系统: 游戏初始化完成。请点击'开始游戏'。")
        def create_barrier_ui(self, barrier):
            """为障碍物创建进度条UI"""
            frame = tk.Frame(self.barrier_frame)
            frame.pack(fill=tk.X, pady=5)
            lbl = tk.Label(frame, text=barrier.name, width=10, anchor="w")
            lbl.pack(side=tk.LEFT)
            progress = ttk.Progressbar(frame, length=200, mode='determinate', maximum=barrier.max_hp)
            progress['value'] = barrier.hp
            progress.pack(side=tk.LEFT, padx=5)
            lbl_hp = tk.Label(frame, text=f"{barrier.hp}/{barrier.max_hp}")
            lbl_hp.pack(side=tk.LEFT)
            # 将UI组件绑定到对象上
            barrier.ui_progress = progress
            barrier.ui_lbl_hp = lbl_hp
        def toggle_game(self):
            """开始/暂停游戏"""
            if self.is_game_over:
                self.init_game()
                return
            self.is_paused = not self.is_paused
            if not self.is_paused:
                self.btn_start.config(text="暂停游戏")
                self.game_loop()
            else:
                self.btn_start.config(text="继续游戏")
        def game_loop(self):
            """主游戏循环"""
            if self.is_paused or self.is_game_over:
                return
            # 时间流逝
            self.time_elapsed += 1
            self.update_time_display()
            # AI 行动
            self.ai_turn()
            # 检查胜利条件
            if self.check_game_over():
                return
            # 自动更新UI
            self.update_barrier_ui()
            self.update_player_ui()
            # 循环 (每200毫秒代表游戏内1分钟)
            self.root.after(200, self.game_loop)
        def action_repair(self):
            """玩家加固"""
            player = self.players[0]
            if player.role == "怪物":
                self.add_log("错误: 怪物不能加固门窗。")
                return
            if player.money >= 20:
                # 优先加固破损最严重的
                target = min([b for b in self.barriers if b.hp > 0], key=lambda x: x.hp, default=None)
                if target:
                    player.money -= 20
                    target.repair(30)
                    self.add_log(f"你消耗20元币加固了 {target.name} (+30耐久)")
                    self.update_barrier_ui()
                    self.update_player_ui()
                else:
                    self.add_log("所有门窗都已损毁，无处可修！")
            else:
                self.add_log("元币不足！需要20元币。")
        def action_earn_money(self):
            """玩家赚钱"""
            player = self.players[0]
            # 学生或中立可以赚钱
            amount = random.randint(10, 20)
            player.money += amount
            self.add_log(f"你通过努力获得了 {amount} 元币。")
            self.update_player_ui()
        def action_switch_role(self):
            """改变阵营"""
            player = self.players[0]
            if player.role == "学生":
                player.role = "怪物"
                self.add_log("你背叛了同学，变成了怪物！现在可以攻击门窗了。")
                self.btn_repair.config(state=tk.DISABLED)
            elif player.role == "怪物":
                player.role = "中立"
                self.add_log("你厌倦了杀戮，变成了中立观察者。")
                self.btn_repair.config(state=tk.NORMAL)
            else:
                # 中立变学生
                player.role = "学生"
                player.money += 50 # 转换奖励
                self.add_log("你决定挺身而出，变回学生！(奖励50元币)")
            self.update_player_ui()
        def action_trade(self):
            """中立交易"""
            player = self.players[0]
            if player.role == "中立":
                # 消耗自己的钱，给所有门窗加血（模拟卖给全体学生物资）
                if player.money >= 30:
                    player.money -= 30
                    for b in self.barriers:
                        b.repair(10)
                    self.add_log("你向学生们出售了物资，所有门窗耐久+10，赚了一笔。")
                    player.money += 50 # 交易获利
                    self.update_barrier_ui()
                    self.update_player_ui()
                else:
                    self.add_log("资金不足进行交易。")
        def ai_turn(self):
            """AI 逻辑"""
            monsters = [p for p in self.players if p.role == "怪物" and p.is_alive]
            students = [p for p in self.players if p.role == "学生" and p.is_alive]
            neutrals = [p for p in self.players if p.role == "中立" and p.is_alive]
            # 怪物攻击
            for m in monsters:
                target = random.choice([b for b in self.barriers if b.hp > 0] or [None])
                if target:
                    dmg = random.randint(5, 15)
                    target.damage(dmg)
                    m.money += 5
                    self.add_log(f"{m.name} 攻击了 {target.name} 造成 {dmg} 伤害。")
            # 学生修补
            for s in students[1:]: # 跳过玩家
                if random.random() > 0.6 and s.money >= 10:
                    target = random.choice([b for b in self.barriers if b.hp > 0] or [None])
                    if target:
                        s.money -= 10
                        target.repair(15)
                        self.add_log(f"{s.name} 加固了 {target.name}。")
            # 中立决策
            for n in neutrals:
                if random.random() > 0.9:
                    n.role = random.choice(["学生", "怪物"])
                    self.add_log(f"中立玩家 {n.name} 突然变成了 {n.role}！")
        def update_time_display(self):
            mins = self.time_elapsed
            hrs = mins // 60
            remain_mins = mins % 60
            left = max(0, self.dawn_time - mins)
            self.lbl_time.config(text=f"时间: {hrs:02d}:{remain_mins:02d} (距离天亮: {left}分钟)")
        def update_barrier_ui(self):
            for b in self.barriers:
                if hasattr(b, 'ui_progress'):
                    b.ui_progress['value'] = b.hp
                    b.ui_lbl_hp.config(text=f"{b.hp}/{b.max_hp}")
        def update_player_ui(self):
            p = self.players[0]
            self.lbl_role.config(text=f"角色: {p.role}")
            self.lbl_money.config(text=f"元币: {p.money}")
            # 按钮状态控制
            if p.role == "怪物":
                self.btn_repair.config(state=tk.DISABLED)
                # 怪物没有专门的攻击按钮，这里简化为自动攻击或通过时间流逝
                # 进阶版可以添加专门的"攻击"按钮
            elif p.role == "中立":
                self.btn_repair.config(state=tk.NORMAL)
                self.btn_trade.pack(pady=5) # 显示交易按钮
            else:
                self.btn_repair.config(state=tk.NORMAL)
                self.btn_trade.pack_forget() # 隐藏交易按钮
            # 敌方情报更新
            m_count = len([p for p in self.players if p.role == "怪物"])
            n_count = len([p for p in self.players if p.role == "中立"])
            self.lbl_enemy_status.config(text=f"怪物数量: {m_count}\n中立数量: {n_count}")
        def check_game_over(self):
            # 1. 天亮
            if self.time_elapsed >= self.dawn_time:
                self.game_over("学生阵营", "天亮了！学生成功坚守到了最后！")
                return True
            # 2. 门窗全破
            all_broken = all(b.hp <= 0 for b in self.barriers)
            if all_broken:
                self.game_over("怪物阵营", "所有门窗被破坏，怪物冲进了教室！")
                return True
            return False
        def game_over(self, winner, msg):
            self.is_game_over = True
            self.is_paused = True
            self.btn_start.config(text="重新开始")
            # 判断玩家个人胜负
            p = self.players[0]
            personal_msg = ""
            if winner == "学生阵营" and p.role == "学生":
                personal_msg = "\n恭喜！你获得了胜利！"
            elif winner == "怪物阵营" and p.role == "怪物":
                personal_msg = "\n恭喜！你作为怪物获得了胜利！"
            elif p.role == "中立":
                personal_msg = "\n作为中立，你安然无恙地看完了整场戏。"
            else:
                personal_msg = "\n你输了..."
            messagebox.showinfo("游戏结束", f"{msg}{personal_msg}")
            self.add_log(f"游戏结束: {winner} 获胜")
        def add_log(self, text):
            self.log_text.config(state='normal')
            timestamp = f"[{self.time_elapsed:03d}分] "
            self.log_text.insert(tk.END, timestamp + text + "\n")
            self.log_text.see(tk.END)
            self.log_text.config(state='disabled')
    if __name__ == "__main__":
        root = tk.Tk()
        app = ClassroomDefenseGame(root)
        root.mainloop()