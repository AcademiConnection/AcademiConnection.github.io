# 样式设置

本页面允许您自定义网站的配色方案，包括明暗模式、主色调和辅助色。

## 配色方案

根据浏览器与系统设置自动切换明暗主题，也可手动切换。

<div class="tx-switch">
<button data-md-color-scheme="default" class="tx-palette-btn"><code>Default（浅色）</code></button>
<button data-md-color-scheme="slate" class="tx-palette-btn"><code>Slate（深色）</code></button>
</div>

## 主色

点击色块可更换主题的主色。

<div class="tx-switch">
<button data-md-color-primary="red" class="tx-palette-btn"><code>Red</code></button>
<button data-md-color-primary="pink" class="tx-palette-btn"><code>Pink</code></button>
<button data-md-color-primary="purple" class="tx-palette-btn"><code>Purple</code></button>
<button data-md-color-primary="deep-purple" class="tx-palette-btn"><code>Deep Purple</code></button>
<button data-md-color-primary="indigo" class="tx-palette-btn"><code>Indigo</code></button>
<button data-md-color-primary="blue" class="tx-palette-btn"><code>Blue</code></button>
<button data-md-color-primary="light-blue" class="tx-palette-btn"><code>Light Blue</code></button>
<button data-md-color-primary="cyan" class="tx-palette-btn"><code>Cyan</code></button>
<button data-md-color-primary="teal" class="tx-palette-btn"><code>Teal</code></button>
<button data-md-color-primary="green" class="tx-palette-btn"><code>Green</code></button>
<button data-md-color-primary="light-green" class="tx-palette-btn"><code>Light Green</code></button>
<button data-md-color-primary="lime" class="tx-palette-btn"><code>Lime</code></button>
<button data-md-color-primary="yellow" class="tx-palette-btn"><code>Yellow</code></button>
<button data-md-color-primary="amber" class="tx-palette-btn"><code>Amber</code></button>
<button data-md-color-primary="orange" class="tx-palette-btn"><code>Orange</code></button>
<button data-md-color-primary="deep-orange" class="tx-palette-btn"><code>Deep Orange</code></button>
<button data-md-color-primary="brown" class="tx-palette-btn"><code>Brown</code></button>
<button data-md-color-primary="grey" class="tx-palette-btn"><code>Grey</code></button>
<button data-md-color-primary="blue-grey" class="tx-palette-btn"><code>Blue Grey</code></button>
<button data-md-color-primary="white" class="tx-palette-btn"><code>White</code></button>
</div>

## 辅助色

点击色块更换主题的辅助色。

<div class="tx-switch">
<button data-md-color-accent="red" class="tx-palette-btn"><code>Red</code></button>
<button data-md-color-accent="pink" class="tx-palette-btn"><code>Pink</code></button>
<button data-md-color-accent="purple" class="tx-palette-btn"><code>Purple</code></button>
<button data-md-color-accent="deep-purple" class="tx-palette-btn"><code>Deep Purple</code></button>
<button data-md-color-accent="indigo" class="tx-palette-btn"><code>Indigo</code></button>
<button data-md-color-accent="blue" class="tx-palette-btn"><code>Blue</code></button>
<button data-md-color-accent="light-blue" class="tx-palette-btn"><code>Light Blue</code></button>
<button data-md-color-accent="cyan" class="tx-palette-btn"><code>Cyan</code></button>
<button data-md-color-accent="teal" class="tx-palette-btn"><code>Teal</code></button>
<button data-md-color-accent="green" class="tx-palette-btn"><code>Green</code></button>
<button data-md-color-accent="light-green" class="tx-palette-btn"><code>Light Green</code></button>
<button data-md-color-accent="lime" class="tx-palette-btn"><code>Lime</code></button>
<button data-md-color-accent="yellow" class="tx-palette-btn"><code>Yellow</code></button>
<button data-md-color-accent="amber" class="tx-palette-btn"><code>Amber</code></button>
<button data-md-color-accent="orange" class="tx-palette-btn"><code>Orange</code></button>
<button data-md-color-accent="deep-orange" class="tx-palette-btn"><code>Deep Orange</code></button>
</div>

<script>
  (function () {
    var STORAGE_SCHEME  = "data-md-color-scheme";
    var STORAGE_PRIMARY = "data-md-color-primary";
    var STORAGE_ACCENT  = "data-md-color-accent";

    /* 点击按钮 → 写入 body.dataset 并持久化 */
    function bindButtons(attr, storageKey, datasetKey) {
      var buttons = document.querySelectorAll(".tx-palette-btn[" + attr + "]");
      Array.prototype.forEach.call(buttons, function (btn) {
        btn.addEventListener("click", function () {
          document.body.dataset[datasetKey] = this.getAttribute(attr);
          localStorage.setItem(storageKey, this.getAttribute(attr));
          updateActiveButtons();
        });
      });
    }

    bindButtons("data-md-color-scheme",  STORAGE_SCHEME,  "mdColorScheme");
    bindButtons("data-md-color-primary", STORAGE_PRIMARY, "mdColorPrimary");
    bindButtons("data-md-color-accent",  STORAGE_ACCENT,  "mdColorAccent");

    /* 高亮当前选中的按钮 */
    function updateActiveButtons() {
      var scheme  = document.body.dataset.mdColorScheme  || "default";
      var primary = document.body.dataset.mdColorPrimary || "indigo";
      var accent  = document.body.dataset.mdColorAccent  || "indigo";

      // 清除所有 active
      document.querySelectorAll(".tx-palette-btn").forEach(function (btn) {
        btn.classList.remove("tx-active");
      });

      // 标记当前 scheme
      var sBtn = document.querySelector('.tx-palette-btn[data-md-color-scheme="' + scheme + '"]');
      if (sBtn) sBtn.classList.add("tx-active");

      // 标记当前 primary
      var pBtn = document.querySelector('.tx-palette-btn[data-md-color-primary="' + primary + '"]');
      if (pBtn) pBtn.classList.add("tx-active");

      // 标记当前 accent
      var aBtn = document.querySelector('.tx-palette-btn[data-md-color-accent="' + accent + '"]');
      if (aBtn) aBtn.classList.add("tx-active");
    }

    /* 监听 body dataset 变化（顶栏切换也会触发） */
    var observer = new MutationObserver(updateActiveButtons);
    observer.observe(document.body, { attributes: true });

    /* 初始化 */
    updateActiveButtons();
  })();
</script>

<style>
  .tx-palette-btn {
    width: 8.4rem;
    margin-bottom: .4rem;
    padding: 2.4rem .4rem .4rem;
    transition: background-color .25s, opacity .25s;
    border-radius: .2rem;
    color: #fff;
    font-size: .8rem;
    text-align: left;
    cursor: pointer;
    position: relative;
    border: 2px solid transparent;
  }
  .tx-palette-btn > code {
    background-color: var(--md-code-bg-color);
  }

  /* 选中状态：白色边框 + 右上角打勾 */
  .tx-palette-btn.tx-active {
    border-color: #fff;
    box-shadow: 0 0 0 2px rgba(255,255,255,0.3);
  }
  .tx-palette-btn.tx-active::after {
    content: "✓";
    position: absolute;
    top: 0.3rem;
    right: 0.4rem;
    font-size: 1rem;
    font-weight: bold;
    color: #fff;
    text-shadow: 0 0 2px rgba(0,0,0,0.5);
  }

  /* 浅色按钮特殊处理 */
  button[data-md-color-scheme='default'].tx-palette-btn {
    background-color: hsla(0, 0%, 100%, 1);
    color: #333 !important;
    border-color: #ddd;
  }
  button[data-md-color-scheme='default'].tx-palette-btn > code {
    color: #333 !important;
  }
  button[data-md-color-scheme='default'].tx-palette-btn.tx-active {
    border-color: #333;
    box-shadow: 0 0 0 2px rgba(0,0,0,0.15);
  }
  button[data-md-color-scheme='default'].tx-palette-btn.tx-active::after {
    color: #333;
    text-shadow: none;
  }

  /* 白色主色特殊处理 */
  button[data-md-color-primary='white'].tx-palette-btn {
    background-color: var(--md-primary-bg-color);
    color: var(--md-primary-fg-color);
  }
  button[data-md-color-primary='white'].tx-palette-btn > code {
    color: var(--md-primary-fg-color);
  }

  /* 各类型按钮背景色 */
  button[data-md-color-accent].tx-palette-btn {
    background-color: var(--md-accent-fg-color);
  }
  button[data-md-color-accent].tx-palette-btn > code {
    color: var(--md-accent-fg-color);
  }
  button[data-md-color-primary].tx-palette-btn {
    background-color: var(--md-primary-fg-color);
  }
  button[data-md-color-primary].tx-palette-btn > code {
    color: var(--md-primary-fg-color);
  }
  button[data-md-color-scheme='slate'].tx-palette-btn {
    background-color: var(--md-default-bg-color);
  }

  /* hover */
  .tx-palette-btn:hover {
    opacity: .85;
  }
</style>
