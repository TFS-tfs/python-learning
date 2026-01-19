#git使用：
#git config --global user.name 设置当前git用户签名
#git config --global email.name 设置当前git用户邮箱
#git init 初始化当前目录为git仓库
#git config --list 列出所有git配置，包括系统，全局，本地
#git status 查看工作区和暂存区
#git config --system --list 列出系统git配置
#git config --global --list 列出全局git配置
#git config --local --list 列出本地git配置
#git config --list --show-origin 查看所有git配置及其来源
#git config --list --scopy --show-origin 查看所有git配置的详细来源（包含覆盖关系）
#优先级：本地>全局>系统
#git add文件名 添加文件到暂存区
#git commit -m"日志信息"   保存到本地库
#git reflog 查看版本信息
#git reset --hard 版本号    版本穿梭
#git push origin 分支名  上传本地库文件到远程库