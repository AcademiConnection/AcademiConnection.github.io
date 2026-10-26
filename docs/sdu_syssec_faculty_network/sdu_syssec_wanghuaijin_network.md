# 山东大学 王怀瑾 教授

> 报告生成时间：2026年10月  
> 个人主页：[whj0401.github.io](https://whj0401.github.io/)  
> 所属团队：山东大学计算机科学与技术学院（系统安全 / 软件安全方向，独立课题组）  
> 学院师资页：[cs.sdu.edu.cn 教授名录](https://www.cs.sdu.edu.cn/szdw1/js.htm)  

---

## 一、学者基本信息

| 项目 | 信息 |
|---|---|
| 姓名 | 王怀瑾（Huaijin Wang） |
| 现任职务 | 山东大学计算机科学与技术学院教授（学院师资名录在列，2026年入职）；博士生导师资格虽有课题组主页与部分人才计划材料侧面印证，但学院名录未标注“博导”、faculty.sdu.edu.cn 亦无其独立主页，本报告以“教授”为首选表述 |
| 校区 | 山东大学青岛校区（学院主体所在校区；香港科技大学校友页将其单位标注为"Shandong University, Jinan"，与学院实际驻地存在口径差异） |
| 学科与研究领域 | 计算机科学与技术 / 网络空间安全；二进制代码分析、二进制代码相似性分析（BCSA）、反编译与二进制翻译、恶意代码（病毒）分析、漏洞检测、软件成分分析与软件供应链安全、AI Agent 安全 |
| 人才称号 | 国家级青年人才（学院"杰出人才"页"国家级青年人才"名单在列；其博士生导师 Shuai Wang 课题组主页将其标注为"国家级高层次青年人才计划"） |
| 学历 | 香港科技大学计算机科学与工程系 博士（2019—2023）；南京大学 工学学士 |
| 博士后 | 香港科技大学计算机科学与工程系 博士后（2024—2026，Shuai Wang 课题组） |
| 海外研修 | 美国俄亥俄州立大学（The Ohio State University）Zhiqiang Lin 教授课题组（据 NDSS 2026 论文 vSim 的王怀瑾署名单位为该校） |
| 学术谱系 | 博士导师：[Shuai Wang（王帅）](https://cse.hkust.edu.hk/~shuaiw/)，香港科技大学计算机科学与工程系副教授（终身教职），Penn State 博士、ETH Zurich 博士后 |
| 博士论文 | *Advanced Binary Similarity Analysis and Its Downstream Applications*（2023，HKUST CSE） |
| 代表性发表载体 | CCS、NDSS、EuroSys、ICSE、ISSTA、ASE、OOPSLA、IEEE EuroS&P、TSE、TOSEM、TDSC |
| 代表性开源产出 | sem2vec、BinUSE、SafeSCA、InsnAlign、vSim（OSUSecLab）、BSA2BSCA Artifact |
| 科研资源 | 入选国家级青年人才计划并获相应科研启动支持；2025 年获 Google Cloud Research Credits Program 支持；公开渠道未见其在山东大学主持国家自然科学基金面上/青年项目的立项记录 |

王怀瑾是一位"港科大培养—港科大博士后—回国独立建组"的典型纯学术谱系学者，其全部高影响力论文几乎都围绕"二进制代码的语义表示与相似性判定"这一条技术主线展开，并以该主线向软件成分分析（供应链安全）、反编译与二进制翻译（LLM 赋能）、AI Agent 权限安全三个下游方向延伸。其学术网络的重心当前完全在**校外**——以香港科技大学 Shuai Wang 课题组为绝对核心节点，向南京大学、中山大学、俄亥俄州立大学、浙江工业大学、岭南大学以及腾讯安全科恩实验室扩散，而与山东大学校内同事的共著关系尚未形成。

## 二、教育背景与职业履历

**本科阶段（南京大学）。** 王怀瑾本科就读于南京大学，获工学学士学位（B.Eng.）。其本科阶段即参与程序分析与程序优化方向的科研工作：ICSE 2019 论文 *Global Optimization of Numerical Programs via Prioritized Stochastic Algebraic Transformations* 的作者列表为 Xie Wang、**Huaijin Wang**、Zhendong Su、Enyi Tang、Xin Chen、Weijun Shen、Zhenyu Chen、Linzhang Wang、Xianpei Zhang、Xuandong Li，除 Zhendong Su（苏黎世联邦理工学院）外，其余作者均来自南京大学计算机软件新技术国家重点实验室，其中 Xuandong Li（李宣东）、Linzhang Wang（王林章）为南大软件分析与验证方向的代表性学者。该论文是王怀瑾学术生涯最早的可查公开成果，也确立了他"以程序分析为方法、以工具系统为载体"的研究趣味。其确切本科专业、毕业年月未在任何公开渠道逐项披露；结合其 ICSE 2019 论文的参与时间与其 2019 年秋季进入香港科技大学攻读博士的事实，可合理推断其本科毕业时间为 2019 年前后。

**博士阶段（香港科技大学，2019—2023）。** 王怀瑾进入香港科技大学计算机科学与工程系攻读博士学位，导师为 Shuai Wang 副教授。据 Shuai Wang 课题组主页的毕业生名录，王怀瑾是其实验室的 **Ph.D. #2（2019—2023）**，博士论文题目为 *Advanced Binary Similarity Analysis and Its Downstream Applications*（《面向高级二进制相似性分析及其下游应用》）。博士期间他完成了从"程序优化"到"二进制安全"的重心转移，并以第一作者身份产出 TSE 2022（BinUSE）、TOSEM 2023（sem2vec）、IEEE EuroS&P 2024（BSA2BSCA）三篇标志性成果，系统解决了"神经网络二进制函数检索的误报抑制"与"汇编级语义表示学习"两个核心问题。香港科技大学 CSE 的"Selected PhD Graduates"页面亦单列其条目，标注为"Faculty Member, Shandong University，PhD 2023，Supervised by Shuai WANG"，这是其博士毕业年份（2023）与最终去向最权威的公开记录。

**博士后阶段（香港科技大学，2024—2026）。** 博士毕业后王怀瑾留于 Shuai Wang 课题组从事博士后研究（2024—2026），这一阶段的产出呈现明显的"向外扩张"特征：一方面继续深化二进制方向（NDSS 2026 的 vSim、EuroSys 2026 的 LLM 静态二进制翻译、ISSTA 2026 的 BinRAG 与编译器优化差分分析、ASE 2026 的指令对齐表示学习）；另一方面开始切入 AI 安全（CCS 2026 的 Agent Skill 最小权限执行框架 SkillScope）与密码学系统安全（CCS 2026 的零知识机器学习电路去冗余校验）。博士后期间他还赴美国俄亥俄州立大学 Zhiqiang Lin 教授课题组开展研究，NDSS 2026 论文 vSim 的两位作者署名单位均为俄亥俄州立大学，且代码仓库托管在 OSU SecLab 组织下（github.com/OSUSecLab/vSim），这是其唯一的海外驻留式合作证据。

**独立建组（山东大学，2026— ）。** 2026年，王怀瑾以教授身份加入山东大学计算机科学与技术学院（具体入职月份未公开披露），并入选国家级青年人才计划。其个人主页开篇写明"I am joining the Department of Computer Science and Technology, Shandong University"，同时仍保留香港科技大学的助教记录（COMP2011、COMP3632、CSIT5730、ARIN5303，直至 Fall 2026），说明其属于"港科大博士后期满回国、直接获聘教授"的引进路径，而非"助理教授—副教授—教授"的校内晋升路径。值得注意的是，他在山东大学教师主页系统（faculty.sdu.edu.cn）下尚无独立主页，学院层面仅以指向其 GitHub Pages 的方式列名，这与其入职时间尚短的状态一致。

**研究方向演进可概括为三个阶段：**

1. **2019—2022，方法筑基期**：以强化学习生成软件混淆序列（TDSC 2020）、编译器中间表示增强神经程序嵌入（ICSE 2022）、对抗样本欺骗二进制代码匹配（ICSME 2022）为代表，重点在"如何让机器学习模型理解程序"。
2. **2022—2024，体系成型期**：以 TSE 2022（BinUSE）、TOSEM 2023（sem2vec）、ICSE 2024（BinAug）、EuroS&P 2024（BSA2BSCA）为代表，形成"表示学习 + 等价性校验 + 输入修复"的完整二进制相似性分析技术栈，并首次把二进制相似性推向软件成分分析这一真实产业需求。
3. **2025—2026，外延扩张期**：以 ICSE 2025（隐私保护 SCA）、ISSTA 2025（DecLLM 可重编译反编译）、EuroSys 2026（LLM 静态二进制翻译）、NDSS 2026（vSim 值语义提取）、CCS 2026（Agent Skill 最小权限）为代表，将 LLM 与 AI Agent 引入二进制分析全链条，同时把研究边界扩展到 AI 系统自身的安全。

## 三、学生培养情况

王怀瑾 2026 年方以教授身份入职山东大学，**目前在公开渠道尚无其作为山东大学导师直接指导的研究生记录**——既无署名为"Shandong University"的学生论文，也无学院/课题组层面的学生名册公开。其个人主页明确表示正在招募"self-motivated students (Post-doc, PhD, Master, and Undergraduate)"，说明其独立课题组处于组建初期。其培养经历需严格区分以下几类：

| 类别 | 人员 | 依据与说明 |
|---|---|---|
| **直接指导（山东大学）** | 公开资料未披露 | 入职时间尚短，尚无公开可查的在读研究生、已毕业研究生或本科毕业设计学生名单。 |
| **论文层面的实质指导（港科大期间）** | Wai Kin Wong | ICSE 2024 论文 BinAug 的作者署名为"WONG Wai Kin, **Huaijin Wang\***, Li Zongjie, Shuai Wang"，主页注明"Dr. Shuai Wang and I are joint corresponding authors"。王怀瑾作为共同通讯作者实际承担了对这位低年级博士生（Ph.D. #7，2021—2025）的选题与论文指导，是其最接近"导师角色"的一段经历。 |
| **同组协作型合作（港科大期间）** | Zhibo Liu、Zhaoyu Wang、Zhantong Xue、Zongjie Li、Yuanyuan Yuan、Pingchuan Ma、Daoyuan Wu、Jiangrong Wu、Yixi Lin、Yuming Xiao | 均为 Shuai Wang 课题组的博士生/博士后/研究助理教授，与王怀瑾在 2024—2026 年间的多篇论文中共著（如 OOPSLA 2024、CCS 2026、ISSTA 2026、EuroSys 2026），属于"同门协作"而非"师生指导"。其中：Zhibo Liu 为 Shuai Wang 的 Ph.D. #1（2019—2023），现为南京大学副教授、国家级高层次青年人才，是与王怀瑾共著频次最高的同门（EuroSys 2026、ISSTA 2026、ISSTA 2025、ICSE 2025 等）；Pingchuan Ma 现为浙江工业大学教授；Daoyuan Wu 现为岭南大学助理教授。 |
| **团队培养（山东大学学院层面）** | 公开资料未披露 | 学院层面的研究生集体培养安排（如实验室轮转、团队组会）未在本报告的信息范围内。 |
| **本科科研训练** | 公开资料未披露 | 其主页明确欢迎本科生加入，但尚无成规模的本科生科研产出记录（港科大期间的本科生研究者名单属于 Shuai Wang 课题组，无法归因于其个人）。 |

培养模式上值得记录的一点是：王怀瑾的论文中"学生第一作者 + 本人通讯作者"的组合（BinAug）与"本人第一作者 + 导师通讯"的组合（TSE 2022、TOSEM 2023、EuroS&P 2024、ICSE 2025、NDSS 2026、ASE 2026）并存，反映出他在港科大体系中同时承担"独立执行者"与"小型课题负责人"的双重角色。这一履历为其在山大独立建组提供了较好的学生指导经验基础，但"从零开始招收并培养第一批研究生"仍是他当前面临的实际任务。

## 四、学术合作网络

### 4.1 校内合作

**现状判断：截至本报告检索，未发现王怀瑾与山东大学校内任何教师共著论文、共同承担项目或共同指导学生的公开证据。** 其 2020—2026 年的全部论文作者列表中，除其本人外无任何山东大学署名的合作者；学院官网亦未发布其加入某个建制实验室或研究中心的公告。

这一状态需要放在山东大学计算机科学与技术学院的组织结构中理解。学院现有的建制化团队主要包括：

- **智能计算研究所（IIC）**：成秀珍教授领衔，聚焦边缘智能、区块链、系统安全，官网团队页现列 16 人（成秀珍、于东晓、李峰、肖梦白、张广辉、胡鹏飞、郑艳伟、章宦乐、潘润宇、张啸、徐明辉、Riccardo Spolaor、王芯蕊、杨燕妮、邹逸飞、张国明）。该所是学院内系统安全方向最集中的建制平台，但 IIC 官网团队名册中并无王怀瑾。
- **交叉研究中心（IRC）**：屠长河、吕琳、辛士庆、曾琼等，以计算机图形学、可视化、几何计算为主，与二进制安全方向无方法交集。

因此，王怀瑾属于**学院内"系统安全 / 软件安全"方向上以个人 PI 形式独立建组的教师**，与 IIC 的"系统安全"方向（侧重于网络与系统侧信道、移动安全、AI 安全）在研究问题上相邻但并不重合：IIC 的系统安全更偏"运行时系统与网络层"，而王怀瑾的工作位于"二进制制品与软件供应链层"。

从潜在合作接口看，学院内与其研究距离最近的三位教师是：

| 教师 | 研究方向 | 与王怀瑾的潜在接口 |
|---|---|---|
| 张悦（教授） | 大模型在安全上的应用、大模型安全、移动手机安全、物联网安全、程序分析 | "程序分析 + 大模型"是与王怀瑾 LLM4Binary 路线重叠度最高的方向，是学院内最自然的潜在合作者。 |
| 胡鹏飞（教授，国家优青） | 网络安全与隐私、机器学习安全、无线智能感知 | 机器学习安全（对抗日样本、模型鲁棒性）与王怀瑾 ICSME 2022 的"对抗程序欺骗二进制匹配"存在方法交叉。 |
| 成秀珍（教授，IEEE Fellow）、徐明辉（教授） | 安全与隐私保护、区块链理论与应用、物联网与边缘计算 | 王怀瑾 CCS 2026 的零知识机器学习电路去冗余工作已进入密码学系统安全边界，与该方向存在接口。 |

以上仅为**基于研究方向的潜在接口推断，不构成已存在的合作关系**。学院可承载其后续项目的平台包括数链融合技术教育部工程研究中心、山东省算网融合理论与技术重点实验室、山东省数链融合技术创新中心等。

### 4.2 跨机构合作

王怀瑾的跨机构合作网络呈现"一条主轴 + 三条支线"的结构。

**（1）主轴：香港科技大学 Shuai Wang 课题组（不可替代的核心节点）。** 这是其全部学术网络的母体。2020—2026 年，他参与的 19 篇公开论文中，Shuai Wang 出现在绝大多数作者列表里，且两人在 ASE 2026 的 *Instruction Alignment for Binary Code Representation Learning* 中构成"仅两位作者"的最小合作单元。该课题组为其提供的不只是导师关系，而是一整套协作生态：同门的 Zhibo Liu、Wai Kin Wong、Zongjie Li、Pingchuan Ma、Zhaoyu Wang、Zhantong Xue、Yuanyuan Yuan、Daoyuan Wu，以及作为通讯/合作作者的 Shuai Wang 本人。

**（2）支线一：南京大学。** 双重连接：一是其本科母校与 ICSE 2019 论文的合作方（李宣东、王林章课题组的程序分析传统）；二是同门 Zhibo Liu 于 2023 年博士毕业后任南京大学副教授，两人在 EuroSys 2026、ISSTA 2026、ISSTA 2025、ICSE 2025 连续共著。这条支线使王怀瑾与国内软件工程/程序分析重镇南京大学保持稳定的学术通道。

**（3）支线二：中山大学（AI Agent 安全方向的新通道）。** CCS 2026 论文 *SkillScope: Toward Fine-Grained Least-Privilege Enforcement for Agent Skills* 的作者为 Jiangrong Wu、**Yuhong Nan（南雨宏）**、Yixi Lin、Huaijin Wang、Yuming Xiao、Shuai Wang、**Zibin Zheng（郑子彬）**，其中南雨宏与郑子彬均为中山大学计算机学院教授/副教授，郑子彬是区块链与软件安全方向的知名学者。该论文是王怀瑾首次以非二进制分析主题（LLM Agent 技能的最小权限执行）进入 AI 安全赛道的标志，也是其合作网络向华南地区扩展的第一个节点。论文的实证规模（在 68,312 个真实 Agent Skill 上验证出 6,590 个存在越权行为）显示该合作具备工程化数据能力。

**（4）支线三：俄亥俄州立大学（唯一的海外驻留节点）。** NDSS 2026 论文 *vSim: Semantics-Aware Value Extraction for Efficient Binary Code Similarity Analysis* 由王怀瑾与 **Zhiqiang Lin（林志强）** 两人署名，署名单位均为俄亥俄州立大学。Zhiqiang Lin 是系统安全领域知名学者（二进制分析、固件安全、移动安全），其实验室（OSU SecLab）为该论文提供了代码托管与工件（Zenodo artifact）支持。这是王怀瑾从"港科大团队成员"成长为"具备独立国际合作能力的 PI"过程中的关键一步。

此外，浙江工业大学（Pingchuan Ma，CCS 2026 零知识电路工作）与岭南大学（Daoyuan Wu，EuroSys 2026、ISSTA 2026 等）作为同门毕业生的新单位，构成其网络的"校友扩散层"。

### 4.3 国际合作

王怀瑾的国际合作目前集中在**两个地理节点**，且都以"个人学术纽带"而非"机构协议"为载体：

- **中国香港（香港科技大学）**：既是其博士与博士后培养单位，也是其论文产出的主要单位。港科大 CSE 在系统安全与软件工程方向拥有 Shing-Chi Cheung、Charles Zhang、Shuai Wang 等学者，王怀瑾通过 Shuai Wang 组间接接入这一生态。
- **美国（俄亥俄州立大学）**：以 Zhiqiang Lin 为唯一节点，产出 NDSS 2026 一篇顶会论文。

与其导师 Shuai Wang（Penn State 博士、ETH Zurich 博士后，与香港金管局、证监会、警务处有合作）相比，王怀瑾的国际网络显著更"窄"：**未见与欧洲（如 ETH、CISPA、IMDEA）、新加坡（SMU、NTU）或北美其他机构（Purdue、ASU 等二进制安全重镇）的共著记录**。其论文的合作者构成几乎全部为华人学者，国际合作的"机构多样性"尚待建立。这一特征与其 2026 年刚回国、独立建组时间尚短的状态相匹配，短期内其国际合作仍将主要依赖港科大与 OSU 两条既有通道。

## 五、业界合作关系深度分析

王怀瑾的产业合作呈现出**"单一深度通道 + 明确产品化指向"**的特征，在同期回国的青年学者中属于产业耦合度较高的一类。

### 5.1 核心通道：腾讯安全科恩实验室（Tencent Security Keen Lab）

这是其唯一可追踪的、跨越博士与博士后两个阶段的持续性产业合作通道。腾讯安全科恩实验室的三位研究者——**Sen Nie、Shi Wu、Qiyi Tang**——系统性地出现在王怀瑾自 2022 年起连续七篇论文的作者列表中：

| 年份 | 论文 | 产业作者 | 承载的技术方向 |
|---|---|---|---|
| 2022 | TSE：*Enhancing DNN-Based Binary Code Function Search With Low-Cost Equivalence Checking*（BinUSE） | Qiyi Tang、Sen Nie、Shi Wu | 二进制函数检索 |
| 2022 | ICSME：*Deceiving DNN-Based Binary Code Matching with Adversarial Programs* | Qiyi Tang、Sen Nie、Shi Wu | 二进制匹配的对抗鲁棒性 |
| 2022 | ICSE：*Unleashing the Power of Compiler Intermediate Representation...* | Qiyi Tang、Sen Nie、Shi Wu | 神经程序嵌入 |
| 2023 | TOSEM：*sem2vec: Semantics-Aware Assembly Tracelet Embedding* | Qiyi Tang、Sen Nie、Shi Wu | 汇编语义嵌入 |
| 2024 | IEEE EuroS&P：*Are We There Yet? Filling the Gap Between ML-Based Binary Similarity Analysis and Binary Software Composition Analysis* | Qiyi Tang、Sen Nie、Shi Wu | 二进制软件成分分析 |
| 2025 | ICSE：*Preserving Privacy in Software Composition Analysis*（SafeSCA） | Qiyi Tang、Sen Nie、Shi Wu | 隐私保护 SCA |
| 2025 | ISSTA：*DecLLM — LLM-Augmented Recompilable Decompilation* | Qiyi Tang、Sen Nie、Shi Wu | LLM 驱动反编译 |

这一序列的技术指向非常清晰：从"二进制相似性判定的准确性"逐步走向"软件成分分析（SCA）的可用性与合规性"，正对应软件供应链安全治理的产品需求（识别二进制制品中的开源组件、许可证与漏洞）。其中 ICSE 2025 的 SafeSCA 与 EuroS&P 2024 的 BSA2BSCA 两篇，是"学术方法—产业数据集—真实场景"结合最紧密的成果，且均开源了工具与工件（github.com/whj0401/SafeSCA、sites.google.com/view/bsa2bsca）。

值得单独指出的是，王怀瑾 2021—2022 年度获得 **CCF-腾讯犀牛鸟精英人才奖**（CCF-Tencent Rhino-Bird Elite Award），这一由 CCF 与腾讯联合设立的人才计划本身就是"高校学生/青年学者进入腾讯真实业务场景开展研究"的制度化通道，与其科恩实验室的持续共著构成相互印证的证据链。

### 5.2 其他产业接口

- **Google Cloud Research Credits Program（2025）**：获得谷歌云研究资源支持，通常用于大规模数据集的构建与模型训练。结合其 2026 年 Agent Skill 生态测量（68,312 个 Skill）与二进制码大规模语料训练的需求，这一资源支持的指向较为明确。
- **华为、字节跳动、阿里巴巴**：截至本报告检索，**未发现**王怀瑾与上述企业存在共著论文、专利、联合实验室或公开项目合作的证据。
- **国内安全厂商（奇安信、深信服、360 等）**：同样未检索到公开合作记录。

### 5.3 产业化能力评价

从三个维度评估其产业转化潜力：

- **技术深度**：其技术栈（二进制相似性、反编译、软件成分分析、二进制翻译）恰好位于"软件供应链安全治理"这一政策强需求领域的技术底座位置。SBOM（软件物料清单）在二进制制品层面的落地长期受困于"无源码如何识别组件"的问题，而 BSA2BSCA 与 SafeSCA 正是针对该痛点。
- **工程化程度**：五件以上开源工具（sem2vec、BinUSE、SafeSCA、InsnAlign、vSim），且多篇论文配有 Zenodo 可复现工件（DOI 10.5281/zenodo.17751555、10.5281/zenodo.21696749），说明其研究习惯偏向"可复现、可交付"，这与产业合作方的评估标准高度契合。
- **转化路径**：目前其转化路径主要依附于腾讯科恩实验室这一单一通道，尚无自主创办企业、技术入股或校级联合实验室的公开记录。相较于山东大学校内已有"造就 2 家科创板上市企业"传统的成果转化生态，他尚处于"接入期"而非"主导期"。

## 六、重要奖项与学术兼职

### 6.1 重要奖项与荣誉

| 年份 | 奖项/荣誉 | 关系网络意义 |
|---|---|---|
| 2026年前后 | 国家级青年人才计划入选 | 与同门的 Zhibo Liu（南京大学）、Yuanyuan Yuan（清华大学）、Pingchuan Ma（浙江工业大学）、Wenxuan Wang（中国人民大学）同属 Shuai Wang 课题组输出的"国家级高层次青年人才"序列，是该课题组人才产出链的一环，也是其获聘山东大学教授的直接依据。 |
| 2025 | Google Cloud Research Credits Program | 云算力资源支持，服务于大规模二进制语料训练与 Agent Skill 生态测量。 |
| 2021—2022 | CCF-腾讯犀牛鸟精英人才奖 | CCF 与腾讯联合设立的产学合作人才计划，是其与腾讯安全科恩实验室长期共著的制度化注脚。 |
| 2023 | 香港科技大学 CSE 博士毕业生名录入选 | 被列入 HKUST CSE "Selected PhD Graduates"（去向标注为 Shandong University），属院系层面认可。 |
| 2026 | NDSS 2026 论文录用 | 安全"四大"顶会（S&P / CCS / USENIX Security / NDSS）之一，且为其首篇以俄亥俄州立大学为署名单位、独立于导师的两人合作成果。 |
| 2026 | CCS 2026 两篇论文录用 | 安全"四大"顶会之一；两篇分别指向 AI Agent 安全（SkillScope）与密码学系统安全（零知识机器学习电路去冗余），标志其研究边界向 AI 系统自身安全的扩展。 |

注：未见其获得最佳论文奖（Best Paper / Distinguished Paper）的公开记录；其同门 Zhibo Liu 曾获 2023 年港科大 CSE 最佳博士论文荣誉提名，王怀瑾本人未见同类别记录。

### 6.2 学术兼职与服务

| 类别 | 具体内容 |
|---|---|
| 期刊审稿人 | IEEE TIFS、IEEE TDSC、IEEE TSE、Computers & Security（均标注为 2026 年） |
| 工件评审委员会 | ICSE 2024 Artifact Review Committee |
| 外部审稿人（会议） | ICSE（2024、2025）、IEEE S&P（2023、2024）、USENIX Security（2023、2024）、ESEC/FSE（2023、2024）、ISSTA（2023、2024）、CCS（2022、2023）、ASE（2022）、NDSS BAR（2022） |
| 外部审稿人（期刊） | TOSEM（2023、2024）、IEEE TIFS（2022）、DTRAP（2022） |
| 其他 | ICICS（2019、2020）、ICSE SEIP（2020） |

其服务范围覆盖**安全四大顶会中的三个（S&P、USENIX Security、CCS）与软件工程三大顶会（ICSE、FSE、ISSTA）**，形成了"安全 + 软件工程"双栖的审稿身份。这一身份结构与其研究定位高度一致——他的工作本质上就是用软件工程（程序分析、表示学习、测试）的方法解决安全问题。不过，其目前的服务层级仍停留在"审稿人/外部评审"层面：根据其个人主页公开的服务列表，**尚未见担任会议程序委员会委员（PC Member）、领域主席（Area Chair）或期刊编委（AE）的记录**，这是其学术共同体嵌入度尚待提升的部分（对比其导师 Shuai Wang 已担任 IEEE S&P、ICSE、CCS、FSE、ISSTA、ASE 的 PC 及 Journal of Computer Security 的 AE）。

### 6.3 教学经历

公开可见的教学经历全部为香港科技大学的助教工作，且集中于"网络安全原理"一门课程：

- COMP2011: Programming with C++（Spring 2020）
- CSIT5730 / COMP3632: Principles of Cybersecurity（2022 Spring、2022 Fall、2025 Fall）
- ARIN5303: Principles of Cybersecurity（2026 Fall）

其个人主页未列出任何在山东大学的授课记录，说明其教学任务尚在安排之中，或新开课程信息尚未公开。

## 七、Connection圈层总结

王怀瑾的学术关系网络是一个"**单核心、高密度、正在重排**"的结构，可概括为五个圈层：

1. **第一圈层：港科大 Shuai Wang 课题组（绝对核心）。** 这是其学术身份的来源与当前论文产出的主体。导师 Shuai Wang 既是学术谱系源头，也是最高频合作者；同门的 Zhibo Liu、Wai Kin Wong、Zongjie Li、Pingchuan Ma、Zhaoyu Wang、Zhantong Xue、Yuanyuan Yuan、Daoyuan Wu 构成协作密度最高的"同门层"。该圈层的特征是"共著频次极高、机构高度单一"——2020—2026 年的 19 篇公开论文中，绝大多数出自这一个实验室的内部协作，这也意味着其网络的"抗风险能力"尚未经过独立建组的检验。

2. **第二圈层：腾讯安全科恩实验室（唯一持久产业通道）。** Sen Nie、Shi Wu、Qiyi Tang 三人自 2022 年起连续出现在其七篇论文中，叠加 2021—2022 年度 CCF-腾讯犀牛鸟精英人才奖，构成一条贯穿博士与博士后阶段的产学合作链。该圈层的功能是为其学术方法提供真实工业数据集、真实二进制样本与产品化场景（二进制软件成分分析），也使其研究成果与"软件供应链安全治理"这一国家需求直接对齐。

3. **第三圈层：海外驻留节点（俄亥俄州立大学 Zhiqiang Lin）。** 这是其从"团队成员"走向"独立 PI"的转折性节点。vSim 以两人署名、OSU 单位发表，为其建立了独立于港科大的国际合作信用，也为未来学生交换、联合培养预留了通道。

4. **第四圈层：同门扩散的国内高校网络（南京大学、浙江工业大学、岭南大学、中山大学）。** Zhibo Liu（南大副教授）、Pingchuan Ma（浙工大教授）、Daoyuan Wu（岭南大学助理教授）作为同门毕业生在不同机构落地，形成"人散网不散"的校友型合作层；中山大学南雨宏、郑子彬的加入，则代表其合作网络向"AI Agent 安全"这一新赛道与华南地区的双重扩展，也是其未来最有可能形成新增长点的方向。

5. **第五圈层：山东大学校内网络（尚未形成）。** 这是当前最显著的结构性缺口。王怀瑾在学院内是**独立 PI**，既不属于 IIC（成秀珍领衔的智能计算研究所），也不属于 IRC（交叉研究中心），与其研究距离最近的张悦、胡鹏飞、成秀珍、徐明辉等尚未产生任何共著或项目层面的公开连接；其个人主页在 faculty.sdu.edu.cn 下亦无独立页面，学院仅以链接方式列名。这一状态是"新入职、独立建组、校内合作尚在形成中"的客观反映，而非其学术网络本身的缺陷——他 2019 年才离开本科母校、2023 年才博士毕业、2026 年才回国，其网络的"国内化"与"山大化"必然滞后于"港科大化"。

**综合评价。** 王怀瑾属于"技术主线高度聚焦、网络密度高但半径小"的青年学者类型：其学术资本几乎全部沉淀在"二进制代码语义表示与相似性判定"这一条极窄但极深的技术线上，并已通过 TSE、TOSEM、CCS、NDSS、EuroSys、ICSE、ISSTA、ASE 等顶会顶刊建立了稳固的学术信用；其产业资本则集中于腾讯科恩实验室一条通道，耦合深但分散度低。他当前面临的三项关键任务是：**其一，把港科大时期的同门协作转化为山大的独立课题组产出**，即在未来 2—3 年内产出以山东大学为第一署名单位、由其指导的学生为第一作者的顶会论文；**其二，与学院内系统安全与程序分析方向的同事（张悦、胡鹏飞、成秀珍、徐明辉等）建立实质合作**，从而嵌入学院的"网络空间安全与智能计算"双一流建设学科体系；**其三，把腾讯通道的经验复制到第二个产业伙伴**，避免产业合作的高度单点依赖。若三项任务顺利推进，其网络有望在"二进制安全 + AI Agent 安全"的交叉地带形成国内领先的辨识度；反之，则可能长期停留在"港科大团队的延伸"这一角色定位上。

---

### 参考公开资料

1. [王怀瑾个人主页（Huaijin Wang）](https://whj0401.github.io/)：个人简介、研究方向、完整论文列表（含 Preprint/Code/Artifact 链接）、审稿服务、助教经历、获奖记录、招生说明。
2. [Shuai Wang 个人主页（HKUST CSE）](https://cse.hkust.edu.hk/~shuaiw/)：课题组 Current Team 与 Alumni 名单，明确记载"Huaijin Wang (Ph.D.#2, 2019-2023) (Postdoc 2024-2026)，Currently: Professor @ Shandong University，国家级高层次青年人才计划"，并给出博士论文题目 *Advanced Binary Similarity Analysis and Its Downstream Applications*。
3. [HKUST CSE: Selected PhD Graduates](https://cse.hkust.edu.hk/pg/ourgraduates/)：官方博士毕业生去向名录，记载"Huaijin WANG, Faculty Member, Shandong University, Jinan, China, PhD 2023, Supervised by Shuai WANG"。
4. [山东大学计算机科学与技术学院：教授名录](https://www.cs.sdu.edu.cn/szdw1/js.htm)：收录王怀瑾，职称"教授"，研究方向"二进制代码分析、病毒分析、软件供应链安全"，个人链接指向 whj0401.github.io。
5. [山东大学计算机科学与技术学院：杰出人才](https://www.cs.sdu.edu.cn/szdw1/jcrc.htm)：学院人才梯队名单，"国家级青年人才"栏含王怀瑾，同列者为于东晓、甘甜、任鹏杰、张兆榕、张悦、罗琦、胡鹏飞、胡琴、赵海森、贾振格。
6. [NDSS Symposium 2026: vSim — Semantics-Aware Value Extraction for Efficient Binary Code Similarity Analysis](https://www.ndss-symposium.org/ndss-paper/vsim-semantics-aware-value-extraction-for-efficient-binary-code-similarity-analysis/)：论文作者署名单位（The Ohio State University）、摘要、论文与幻灯片下载、视频链接。
7. [arXiv:2608.11766 — Instruction Alignment for Binary Code Representation Learning](https://arxiv.org/abs/2608.11766)：ASE 2026 论文，作者为 Huaijin Wang 与 Shuai Wang 两人，用于确认其与导师的最小合作单元及其指令级对齐研究方向。
8. [arXiv:2605.05868 — SkillScope: Toward Fine-Grained Least-Privilege Enforcement for Agent Skills](https://arxiv.org/abs/2605.05868)：CCS 2026 论文，作者含 Yuhong Nan、Zibin Zheng（中山大学）等，用于确认其 AI Agent 安全方向与中山大学合作通道。
9. [arXiv:2609.10149 — Sound Debloating of Redundant Checks in Zero-Knowledge Machine-Learning Circuits](https://arxiv.org/abs/2609.10149)：CCS 2026 论文，作者含 Pingchuan Ma（浙江工业大学）、Zhaoyu Wang、Zhantong Xue 等同门，用于确认其密码学系统安全方向的协作结构。
10. [ACM DL: No More Translation at Runtime: LLM-Empowered Static Binary Translation](https://dl.acm.org/doi/10.1145/3767295.3803600)：EuroSys 2026 论文页面，作者 Zhibo Liu、Huaijin Wang、Wai Kin Wong、Daoyuan Wu、Shuai Wang。
11. [ACM DL: DecLLM — LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code](https://dl.acm.org/doi/pdf/10.1145/3728958)：ISSTA 2025 论文，作者含 Qiyi Tang、Sen Nie、Shi Wu（腾讯安全科恩实验室），用于确认其与腾讯的持续产业共著关系。
12. [DOI: Preserving Privacy in Software Composition Analysis（ICSE 2025）](https://doi.org/10.1109/ICSE55347.2025.00055)：作者为 Huaijin Wang、Zhibo Liu、Shuai Wang、Qiyi Tang、Sen Nie、Shi Wu；配套开源工具 [SafeSCA](https://github.com/whj0401/SafeSCA)。
13. [IEEE Xplore: Are We There Yet? Filling the Gap Between ML-Based Binary Similarity Analysis and Binary Software Composition Analysis（IEEE EuroS&P 2024）](https://ieeexplore.ieee.org/abstract/document/10629030)：配套工件页 [BSA2BSCA Artifact](https://sites.google.com/view/bsa2bsca/home/artifact)。
14. [ACM DL: sem2vec — Semantics-Aware Assembly Tracelet Embedding（TOSEM 2023）](https://dl.acm.org/doi/abs/10.1145/3569933)：其博士阶段代表作，代码托管于 [github.com/sem2vec](https://github.com/sem2vec)。
15. [IEEE Xplore: Global Optimization of Numerical Programs via Prioritized Stochastic Algebraic Transformations（ICSE 2019）](https://ieeexplore.ieee.org/abstract/document/8812093/)：其本科阶段（南京大学计算机软件新技术国家重点实验室）参与的最早公开论文，作者含李宣东（Xuandong Li）、王林章（Linzhang Wang）、Zhendong Su 等，用于确认其南京大学本科背景与程序分析学术起点。
