## 方法：将 Anaconda 的 `Scripts` 目录添加到系统 `PATH`（推荐）
这样你就可以在任意终端中直接使用 `frida`、`frida-ps` 等命令。

**步骤如下（Windows）：**

1. 按下 `Win + R`，输入 `sysdm.cpl`，回车 → 打开“系统属性”。
2. 点击 “高级” 选项卡 → 点击 “环境变量”。
3. 在 “系统变量” 或 “用户变量” 中找到 `Path`，点击 “编辑”。
4. 点击 “新建”，然后添加路径：
   ```
   E:\Programs\Anaconda\Scripts
   ```
5. 确认所有窗口，**重启终端（如 CMD、PowerShell 或 VS Code）**，使 PATH 生效。
6. 验证：在新终端中运行
   ```bash
   frida --version
   ```
   如果能输出版本号，说明成功！

> 📝 注意：如果你使用的是 Anaconda Prompt，通常它已经自动配置了 PATH，所以在这个终端里可以直接用。但如果你习惯用系统自带 CMD 或 PowerShell，就需要手动加 PATH。

---
