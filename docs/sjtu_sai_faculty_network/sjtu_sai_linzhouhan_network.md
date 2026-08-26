# SJTU-人工智能学院 林洲汉 副教授

> 报告生成时间：2026年8月25日  
> 个人主页：[Zhouhan Lin（hantek.github.io）](https://hantek.github.io/)  
> 所属团队：上海交通大学人工智能学院（LUMIA Lab；兼约翰·霍普克罗夫特计算机科学中心副主任）  

---

## 一、学者基本信息

| 项目 | 内容 |
|---|---|
| 姓名 | 林洲汉 |
| 当前职称 | **副教授**（[学院官网](https://sai.sjtu.edu.cn/cn/facultydetails/zzjs/linzhouhan)职称栏口径；其个人主页自述为 Professor，可能存在职称信息更新滞后，以官网为准） |
| 校内身份 | 上海交通大学人工智能学院专职教师、博士生导师；约翰·霍普克罗夫特计算机科学中心（JHC）副主任 |
| 实验室 | [LUMIA Lab](https://github.com/LUMIA-Group)（Language Understanding and Machine Intelligence Algorithms，语言理解与机器智能算法实验室）负责人 |
| 研究方向 | 机器学习与自然语言处理：自监督学习、注意机制、语言建模；近期聚焦 decoder-only Transformer 之外的新架构（多尺度表征、外部记忆、循环结构）、next-token-prediction 之外的新预训练任务、长序列建模与高效模型（高效注意力、KV 压缩） |
| 论文规模 | 学术论文 60 余篇，Google Scholar 总引用 9000 余次（2024 年公开讲者简介口径，现应更高），其中 2 篇单篇引用超 1700 次 |
| 代表荣誉 | 国家海外高层次青年人才计划、上海市浦江学者、2022 年 AI 华人青年学者榜（经典领域） |
| 邮箱 | hantek@sjtu.edu.cn |

**消歧说明（供索引）**：本报告对象为人工智能学院教师页（hantek@sjtu.edu.cn）与个人主页所对应的林洲汉，其可唯一识别的特征为"哈工大本硕 + 蒙特利尔大学 Mila 博士（导师 Yoshua Bengio）+ FAIR 访问科学家"履历组合。公开检索未见国内高校其他同名同领域学者造成混淆。需要说明，最初调研线索中"林洲汉曾在 Google 工作十年"的说法不成立——其在 Google AI Language 仅为博士期间实习，应以官方履历为准。

---

## 二、教育背景与职业履历

林洲汉本科（2012）与硕士（2014）均毕业于**哈尔滨工业大学**，随后赴加拿大，2019 年在**蒙特利尔大学（Université de Montréal）Mila 研究所**获得计算机科学博士学位，师从 2018 年图灵奖得主、深度学习奠基人 **Yoshua Bengio**。博士期间，他曾在纽约的 **Google AI Language** 团队实习，在约克敦高地的 **IBM Watson** 与 **Bowen Zhou（周伯文）**、Mo Yu 共事，并在蒙特利尔的 **Microsoft Research** 担任兼职学生研究员（与 Alessandro Sordoni、Adam Trischler 合作）[（个人主页 Bio）](https://hantek.github.io/)。

```text
深度学习蒙特利尔学派
└── Yoshua Bengio（Mila / 蒙特利尔大学，图灵奖得主）
    └── 林洲汉（PhD 2019，蒙特利尔大学 Mila）
        ├── 博士期实习圈：Google AI Language、IBM Watson（周伯文）、MSR Montreal
        └── 现职：上海交大 SAI / JHC 副教授、LUMIA Lab 负责人
```

博士毕业前后，他在 **Facebook AI Research（FAIR）** 门洛帕克总部任访问科学家，与 **Michael Auli** 从事 NLP 研究，随后加入上海交通大学约翰·霍普克罗夫特计算机科学中心（JHC），历任助理教授、副教授，并出任 JHC 副主任；上海交通大学人工智能学院设立后，列入学院专职教师序列，现领导 LUMIA Lab。其博士期间的代表作影响深远：ICLR 2016（口头报告）的低比特神经网络《Neural networks with few multiplications》、ICLR 2017 与 Bengio 等合作的《A structured self-attentive sentence embedding》（自注意力句向量，被引超 1700 次的高被引论文）、ICLR 2018 句法-词法联合语言建模、ACL 2018《Straight to the Tree》句法距离成分句法分析等。近年工作转向新架构与大模型底层技术：Ordered GNN（ICLR 2023）、Graph Parsing Networks（ICLR 2024）、Cluster-wise Graph Transformer（NeurIPS 2024 Spotlight）、LLM 人类可读指纹 HuRef（NeurIPS 2024）、外挂记忆模块 Memory Decoder（NeurIPS 2025）、连续空间"思考"预训练 PonderLM/PonderLM-2（ICLR/ICML 2026）、频域 KV 压缩 FreqKV 等，并与合作者开源了地学基础大模型 GeoGalactica（30B）与 K2（7B）。2026 年 LUMIA 实验室在 ICML 投稿录用 2 篇、ICLR 2026 录用 6 篇，处于高产期 [（News）](https://hantek.github.io/)。

---

## 三、学生培养情况

林洲汉在个人主页公开招收 2027 级硕士/博士研究生，并明确 2026 年名额已满 [（个人主页）](https://hantek.github.io/)。LUMIA Lab 成员主要依据其实验室 GitHub 组织（LUMIA-Group）与近年论文署名推定，除特别说明外，具体导师归属以实验室名单为准，以下学生身份属论文/代码署名层面的确认：

### 1. Boyi Zeng（博士生，核心学生）

PonderLM、PonderLM-2（ICLR/ICML 2026，其一作）与 HuRef（NeurIPS 2024，共同一作）的第一作者，是 LUMIA 在"新架构"主线上最主要的学生研究者，并负责 HuggingFace 模型开源发布。

### 2. Yunchong Song（博士生）

Ordered GNN（ICLR 2023）、Graph Parsing Networks（ICLR 2024）、Flow of Spans（ICLR 2026）一作或共同一作，是图结构语言建模主线的主力学生。

### 3. Siyuan Huang（博士生）

Cluster-wise Graph Transformer（NeurIPS 2024 Spotlight）、Gumbel Reranking（ACL 2025）一作，多篇 NeurIPS/EMNLP 论文核心作者。

### 4. 其他 LUMIA 成员

Jushi Kai（FreqKV、Fourier Compressor，ECCV 2026 Spotlight）、Beiya Dai（ContextLM，ICML 2026）、Yuliang Liu（ContextLM、AdaptiveStep）、Bo Xue（Flow of Spans）、Jiaqi Cao 与 Jiarui Wang（Memory Decoder，NeurIPS 2025 共同一作）、Chang Su（Anchor-Embedding，EMNLP 2025）等。其中 Ziwei He 在 FreqKV 等论文中担任共同通讯作者，推测为实验室青年研究人员或资深成员（具体身份公开资料未披露）。上述成员中已毕业者的去向公开资料未系统披露。

---

## 四、学术合作网络

**DBLP/署名消歧说明**：林洲汉英文名 Zhouhan Lin 在 DBLP 中可唯一定位（Mila/SJTU 轨迹连续），无显著同名混淆；合作者频次以 Google Scholar 与个人主页所选论文为准，未逐篇统计。

### 4.1 学院/校内合作

林洲汉横跨人工智能学院与 JHC（两单位深度重叠），与 JHC 主任郁昱（HuRef 合作者）、张拳石（JHC 副主任）、李帅（JHC 副主任）等构成上海交大机器学习理论与方法的中坚力量。校内高频合作者还包括 **Xinbing Wang**（王新兵，上海交大教授，AWM、PonderLM、ContextLM 等多篇末位作者）、傅洛伊（Luoyi Fu，Flow of Spans）、计算机系的郭守婧（Jingwen Leng）与过敏意（Minyi Guo，Gumbel Reranking）以及访问学者层面的中科院数学与系统科学研究院 Chenghu Zhou、上海交大张拳石（RASAT）等。

### 4.2 跨机构合作（境内）

- **周伯文（Bowen Zhou）**：从 IBM Watson 时期的上司转变为持续科研合作者，现清华大学教授；ContextLM（ICML 2026）、Memory Decoder（NeurIPS 2025）、模型坍缩数据合成（ICML 2025）等多篇论文的合作者，是林洲汉国内合作网络中最重要的资深学者之一。
- **上海人工智能实验室圈**：Kai Chen、Qipeng Guo（Qwen 系列参与者）在 ContextLM、Memory Decoder 中深度参与，表明其与上海 AI Lab 大模型团队存在实质性合作。
- **微软亚洲研究院**：AdaptiveStep（ICML 2025）与 MSR 的 Li Zhao、Jiang Bian 等合作，论文获微软亚洲研究院公众号专题报道。
- **地学大模型合作**：GeoGalactica/K2 系列与地学领域团队合作完成（具体机构以论文署名为准）。

### 4.3 国际合作

其国际网络核心是 **Mila/Bengio 学派**：Yoshua Bengio、Aaron Courville、Yikang Shen（Yikang Shen 后任职于 Apple/哈佛等，Straight to the Tree 等合作）、Athul Paul Jacob、Chin-Wei Huang 等。FAIR 时期的 **Michael Auli**、MSR Montreal 的 **Alessandro Sordoni** 与 **Adam Trischler**、IBM Watson 的 **Mo Yu** 等为其博士期业界导师层。Stanford/CMU 等机构学生亦有合作（如 HuRef 中的 Yuncong Hu）。整体上国际合作为论文共同体关系，无长期联合职务。

---

## 五、业界合作关系深度分析

与创业型教师不同，林洲汉的业界关系以**研究共同体与项目合作**为主：

1. **Meta/FAIR**：博士毕业后的正式职位（访问科学家），与 Michael Auli 合作 NLP 方向，是其唯一的业界全职研究经历。
2. **谷歌、IBM、微软**：均为博士期间实习/兼职（Google AI Language NYC、IBM Watson、MSR Montreal），积累了跨越硅谷大厂 NLP 团队的同行网络；近年与**微软亚洲研究院**在推理模型方向（AdaptiveStep）重启合作。
3. **开源生态**：LUMIA Lab 的 PonderLM 系列、Memory Decoder、FreqKV 等成果均在 GitHub/HuggingFace 全量开源（含 30B 级 GeoGalactica 权重），在知乎、小红书等平台有较高社区传播度，属于"开源影响力型"产业连接。
4. **应用落地**：地学大模型（GeoGalactica/K2）面向地球科学科研场景，是其最接近垂直行业落地的工作；具体企业横向项目公开资料未披露。

---

## 六、重要奖项与学术兼职

| 类别 | 内容 |
|---|---|
| 人才计划 | 国家海外高层次青年人才计划；上海市浦江学者 |
| 榜单荣誉 | 2022 年 AI 华人青年学者榜（经典领域） |
| 论文荣誉 | ICLR 2016 Oral（Neural networks with few multiplications）；NeurIPS 2024 Spotlight（Cluster-wise Graph Transformer）；RSS 相关荣誉不适用；ECCV 2026 Spotlight（Fourier Compressor，学生一作） |
| 期刊审稿 | JMLR、IEEE TASLP、IEEE TNNLS 审稿人 |
| 会议审稿 | ICLR、NeurIPS、ICML、AAAI、ACL、EMNLP、NAACL、AACL 审稿人 |
| 领域主席 | EMNLP、AAAI、AACL、COLING 领域主席（Area Chair） |
| 会议组织 | MLNLP 2025 组织主席；CCL 2025 讲习班/Workshop 主席；CIPS-LMG 2025 高效 LLM 架构论坛组织者 |
| 受邀报告 | NYU Shanghai 讲座（2025，新架构方向）、CSML 2025 主旨报告、CIPS-LMG 2024 讲习班两场报告 |
| 教学 | CS-1605 C++ 程序设计实践；CS-3602 自然语言处理 |

---

## 七、Connection圈层总结

**第一圈层：Mila/Bengio 师承圈。** Yoshua Bengio 门下的博士学位与自注意力句向量等高被引早期工作，奠定了他在深度学习 NLP 共同体中的学术身份；Aaron Courville、Yikang Shen 等同门构成其国际网络底座。

**第二圈层：硅谷大厂 NLP 研究圈。** FAIR（Michael Auli）、Google AI Language、IBM Watson（周伯文、Mo Yu）、MSR Montreal（Sordoni、Trischler）的经历，使其成为少数横跨四大 AI 研究部门的中国青年学者，并延续为与周伯文、MSRA 的持续合作。

**第三圈层：上海交大 JHC—SAI 共同体。** 作为 JHC 副主任与 SAI 专职教师，他与俞勇体系下的郁昱、张拳石、李帅、温颖等共同构成上海交大 AI 学院的方法论核心，并与 Xinbing Wang、傅洛伊、郭守婧、过敏意等校内力量形成稳定的跨系合作。

**第四圈层：LUMIA 学生网络与大模型新架构社区。** Boyi Zeng、Yunchong Song、Siyuan Huang 等学生群体在 ICLR/ICML/NeurIPS 持续产出，与上海 AI Lab（Kai Chen、Qipeng Guo）、清华（周伯文）的联合工作使 LUMIA 成为国内"超越 decoder-only 架构"研究方向的活跃节点；开源模型带来的社区影响力是其独特资产。

---

**主要参考来源**：[林洲汉个人主页](https://hantek.github.io/)（Bio、News、Selected Publications、Teaching）；[上海交通大学人工智能学院教师页（林洲汉）](https://sai.sjtu.edu.cn/cn/facultydetails/zzjs/linzhouhan)；[SAI 专职教师名录](https://soai.sjtu.edu.cn/cn/faculty/zzjs)；[CSIG 讲者简介（2024）](https://conf.csig.org.cn/6594/202407/44776.html)；[腾讯新闻·追问专访（2025-02）](https://new.qq.com/rain/a/20250228A01EGU00)；[Google Scholar 主页](https://scholar.google.com/citations?user=LNZ4efwAAAAJ&hl=en)。
