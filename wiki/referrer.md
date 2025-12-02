`Referer`（注意拼写是 **Referer**，不是 "Referrer"——这是 HTTP 协议早期的一个拼写错误，后来被保留下来）是 HTTP 请求头（Request Header）中的一个字段，用于**指示当前请求是从哪个页面（URL）跳转或发起的**。

---

### ✅ 含义
> **`Referer` 告诉服务器：“我是从哪个网页链接过来的。”**

例如：
- 用户在页面 `https://example.com/home` 上点击了一个链接，跳转到 `https://api.example.com/data`，
- 那么浏览器在请求 `https://api.example.com/data` 时，会自动带上：
  ```
  Referer: https://example.com/home
  ```

---

### 🔍 主要用途

1. **流量来源分析（Analytics）**  
   网站可以通过 `Referer` 知道用户是从 Google 搜索、其他网站、还是自家页面跳转来的，用于统计营销效果或用户行为。

2. **防盗链（Anti-leeching）**  
   比如图片服务器检查 `Referer`：
   - 如果请求来自自家域名（如 `https://your-site.com`）→ 允许访问；
   - 如果来自其他网站（如 `https://evil-site.com`）→ 拒绝返回图片（返回 403 或默认图）。

3. **安全防护（CSRF 防御辅助）**  
   虽然不推荐单独依赖 `Referer` 做 CSRF 防护（因为它可能被浏览器禁用或缺失），但可作为辅助判断：  
   - 如果 POST 请求的 `Referer` 不是自家域名，可能可疑。

4. **API 调用上下文（调试/日志）**  
   后端可记录 `Referer`，帮助排查“这个请求到底是从哪个前端页面发起的”。

---

### 🌐 示例

假设你在 `https://www.reese-blog.com/article/123` 页面中用 JavaScript 发起一个 API 请求：

```javascript
fetch("https://api.myservice.com/healthreport", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ user: "Reese" })
});
```

浏览器会自动在请求头中加上：
```
Referer: https://www.reese-blog.com/article/123
```

---

### ⚠️ 注意事项

| 问题 | 说明 |
|------|------|
| **隐私问题** | 出于隐私保护，浏览器在某些情况下会**不发送**或**截断** `Referer`（如从 HTTPS 跳转到 HTTP 时）。 |
| **可被伪造** | `Referer` 是客户端发送的，**不可信**！不能用于关键安全判断（如身份认证）。 |
| **拼写错误** | 协议中写的是 `Referer`，不是 `Referrer`，代码里也要写对。 |
| **可被禁用** | 用户可通过浏览器设置、插件或 `meta` 标签禁止发送 `Referer`：<br>`<meta name="referrer" content="no-referrer">` |

---

### 🛠 在 `requests` 中手动设置 Referer

虽然 `requests` 默认**不会自动设置 `Referer`**（因为它是程序发起的请求，不是浏览器跳转），但你可以手动添加：

```python
headers = {
    "Referer": "https://www.your-frontend.com/dashboard",
    "User-Agent": "Mozilla/5.0 ..."
}
response = requests.post(url, headers=headers, json=data)
```

> 💡 在爬虫或调用某些 API 时，如果服务端做了 Referer 校验，你就必须手动设置它，否则会被拒绝。

---

### 总结
`Referer` 是一个**表示请求来源页面 URL 的 HTTP 头**，主要用于：
- 统计分析
- 防盗链
- 辅助调试

但它**不可靠、可伪造、可能缺失**，切勿用于核心安全逻辑。

你提到的 **`referrer`**（注意拼写带两个 `r`）其实是日常用语或编程中对“引荐来源”的**正确英文拼写**，但在 **HTTP 协议中，对应的请求头字段名却是 `Referer`（少一个 `r`）**——这是一个历史遗留的拼写错误。

下面我们从几个角度帮你彻底理清：

---

### 📌 1. 术语 vs 字段名

| 概念 | 正确拼写 | HTTP 字段名 | 说明 |
|------|--------|-------------|------|
| 通用英文单词 | **referrer**（n. 引荐人 / 来源页） | — | 日常用语、代码变量名常用 |
| HTTP 请求头字段 | — | **`Referer`** | 协议标准中写错了，但沿用至今 |

✅ 所以：
- 当你**写代码、读文档、配置服务器**时，要写的是：`Referer`
- 当你**口头或文章中描述这个概念**时，可以说 “the referrer of the request”

> 📚 RFC 1945（最早的 HTTP/1.0 规范）就写成了 `Referer`，后来想改但为兼容性保留。

---

### 📥 2. `Referer` 字段的作用（再强化）

它表示：**“当前请求是从哪个 URL 页面发起的”**，即“来源页”。

#### 举例 🌰
你在浏览器中：
1. 打开 `https://www.google.com/search?q=health+report`
2. 点击一个搜索结果，跳转到 `https://homesignsvcuat.100jed.com/prov/healthreport/listPage`
3. 浏览器自动在请求头中加上：
   ```
   Referer: https://www.google.com/search?q=health+report
   ```

后端看到这个 `Referer`，就知道：用户是从 Google 搜索过来的。

---

### 🛠 3. 在 Python `requests` 中如何使用

**`requests` 不会自动设置 `Referer`**（因为它不是浏览器，没有“上一个页面”的概念），但你可以手动加：

```python
import requests

url = "https://homesignsvcuat.100jed.com/prov/healthreport/listPage"
headers = {
    "Referer": "https://www.your-portal.com/dashboard",  # 注意拼写！
    "User-Agent": "Mozilla/5.0 ..."
}

response = requests.post(url, headers=headers, params={"current": 1, "pageSize": 15})
```

> 💡 如果目标服务器校验 `Referer`（比如防止跨站调用），你必须显式设置，否则可能返回 403。

---

### ⚠️ 4. 常见误区

| 误区 | 正确理解 |
|------|--------|
| “应该写成 `Referrer`” | ❌ HTTP 头必须写 `Referer`，写 `Referrer` 服务器收不到 |
| “`Referer` 能防止 CSRF” | ❌ 它可被伪造或缺失，不能作为安全依据 |
| “所有请求都有 `Referer`” | ❌ 以下情况可能没有：<br>• 直接在地址栏输入 URL<br>• HTTPS → HTTP 跳转（出于隐私）<br>• 页面设置了 `<meta name="referrer" content="no-referrer">` |

---

### 🔒 5. 隐私与现代控制

现代浏览器允许页面控制 `Referer` 的发送策略，通过：
```html
<meta name="referrer" content="no-referrer|origin|same-origin|strict-origin|...">
```

例如：
- `no-referrer`：完全不发 `Referer`
- `origin`：只发协议+域名+端口（如 `https://example.com`），不带路径

这进一步说明：**不能依赖 `Referer` 一定存在或完整**。

---

### ✅ 总结一句话

> **`Referer`（拼写如此）是 HTTP 请求头，表示“请求从哪个页面来”；而 `referrer` 是这个概念的正确英文拼写，但 HTTP 协议里不用它。**

在开发中，记住：
- 写代码时用 **`Referer`**
- 理解其作用但**不信任它**
- 必要时手动设置它（尤其在模拟浏览器行为时）

如果你在调测接口时被服务器因缺少 `Referer` 拒绝，现在就知道该怎么做了 😊