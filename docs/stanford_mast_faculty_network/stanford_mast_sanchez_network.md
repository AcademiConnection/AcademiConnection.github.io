# StanfordMAST Daniel Sanchez Professor

> 报告生成时间：2026年8月14日  
> 个人主页：[https://people.csail.mit.edu/sanchez/](https://people.csail.mit.edu/sanchez/)  
> 所属团队：MIT EECS / Stanford MAST Lab 校友  

---

## 一、学者基本信息

| 项目 | 内容 |
|------|------|
| 姓名 | Daniel Sanchez |
| 现任职位 | Professor（正教授），MIT 电子工程与计算机科学系（EECS） |
| 所属机构 | 麻省理工学院（MIT），计算机科学与人工智能实验室（CSAIL） |
| 办公地址 | MIT CSAIL, 32 Vassar St, 32-G838, Cambridge, MA 02139 |
| 研究领域 | 计算机体系结构、计算机系统、大规模多核架构、可扩展内存层次、服务质量保证、全同态加密加速器、稀疏计算加速器 |
| 博士毕业院校 | 斯坦福大学（Stanford University），电气工程博士，2012年 |
| 博士导师 | Christos Kozyrakis（Stanford MAST Lab） |
| 本科毕业院校 | 马德里理工大学（Universidad Politécnica de Madrid, UPM），电信工程学士，2007年 |
| 加入 MIT 时间 | 2012年9月 |

## 二、教育背景与职业履历

### 2.1 教育经历

Daniel Sanchez 的学术道路始于欧洲，在西班牙马德里理工大学（UPM）获得电信工程学士学位（2007年）。随后赴美深造，进入斯坦福大学电气工程系攻读研究生，师从 Christos Kozyrakis 教授。2009年获斯坦福大学电气工程硕士学位，2012年获博士学位。

**博士论文**：《Hardware and Software Techniques for Scalable Thousand-core Systems》（面向可扩展千核系统的硬件与软件技术）

该论文聚焦于如何设计可扩展到上千个核心的多核处理器系统，涵盖缓存层次结构、一致性协议、任务调度等关键体系结构问题。在博士期间，Sanchez 提出了多项有深远影响的技术，包括 ZCache、Vantage 和 SCD（Scalable Coherence Directory），这些工作奠定了他在计算机体系结构领域的学术声誉。

### 2.2 职业履历

- **2012年9月**：加入 MIT EECS 系，任助理教授（Assistant Professor）
- **约2018年**：晋升为副教授（Associate Professor），获得终身教职（tenure）
- **约2022-2023年**：晋升为正教授（Full Professor）

根据其 MIT 主页，Sanchez 目前的职称为 "Professor, MIT EECS"，即正教授。他从2012年秋季开始教授 MIT 核心课程，包括计算机系统体系结构（6.823/6.5900）和计算结构（6.004/6.191），以及并行与异构计算机体系结构（6.888）。

### 2.3 在 Stanford MAST Lab 期间的代表性工作

Sanchez 在 Kozyrakis 指导下于斯坦福 MAST Lab 完成的代表性研究包括：

1. **ZCache**（MICRO 2010）：提出了一种解耦缓存路数（Way）与关联度（Associativity）的缓存架构。ZCache 通过多级替换候选者遍历机制，在不增加物理路数的前提下大幅提升了有效关联度，从而减少冲突未命中。该论文被广泛引用，是缓存设计领域的经典工作。

2. **Vantage**（ISCA 2011）：提出了一种可扩展的细粒度缓存分区技术。Vantage 克服了传统路分区（way-partitioning）方案的粗粒度限制，支持数十个分区且粒度可达缓存行级别，同时保持高关联度和强隔离性。在32核系统上，Vantage 对98%的工作负载提升了吞吐量，平均提升8%（最高20%）。

3. **SCD（Scalable Coherence Directory）**：提出可扩展一致性目录设计，解决了大规模多核系统中目录表爆炸的问题，是千核系统一致性协议的关键技术。

这些工作构成了其博士论文的核心内容，统一围绕"如何让上千核的系统可扩展"这一宏大主题。

## 三、学生培养情况

Sanchez 在 MIT 建立了独立的研究组（隶属于 CSAIL 的计算结构组，Computation Structures Group），培养了大批优秀的博士生和博士后。以下信息来源于其 MIT 主页（截至2024年底）。

### 3.1 当前在读博士生

| 姓名 | 学位 | 备注 |
|------|------|------|
| Axel Feldmann | Ph.D. | 研究方向为稀疏计算加速器（Spatula, Azul）和FHE加速器 |
| Hyun Ryong (Ryan) Lee | Ph.D. | 研究方向为基准测试生成（Datamime）和稀疏数据结构加速器（Terminus） |
| Fares Elsabbagh | Ph.D. | 与 Joel Emer 联合指导，研究方向为RTL仿真加速 |
| Shabnam Sheikhha | Ph.D. | 与 Joel Emer 联合指导，研究方向为RTL仿真加速 |
| Xingran (Maggie) Du | S.M./Ph.D. | 与 Joel Emer 联合指导 |
| Aleksandar Krastev | S.M./Ph.D. | 研究方向为FHE编译器和加速器 |
| Courtney Golden | S.M./Ph.D. | 与 Joel Emer 联合指导，研究方向为稀疏计算加速器 |
| Viansa Schmulbach | S.M./Ph.D. | 与 Christina Delimitrou（MIT）联合指导 |

### 3.2 已毕业博士生与博士后

| 姓名 | 毕业年份 | 学位 | 当前去向/备注 |
|------|----------|------|-------------|
| Nathan Beckmann | 2015 | Ph.D. + Post-Doc (2015-2016) | 现任卡内基梅隆大学（CMU）教授 |
| Harshad Kasture | 2017 | Ph.D. | — |
| Suvinay Subramanian | 2018 | Ph.D. | — |
| Nosayba El-Sayed | 2018 | Post-Doc | — |
| Po-An Tsai | 2019 | Ph.D. | 研究方向包括缓存压缩安全（Safecracker）、Jenga |
| Mark Jeffrey | 2019 | Ph.D. | 研究方向包括推测并行（T4） |
| Guowei Zhang | 2020 | Ph.D. | 研究方向包括稀疏矩阵乘法加速（Gamma）、哈希表加速 |
| Maleen Abeydeera | 2021 | Ph.D. | 研究方向包括推测并行加速器（Chronos） |
| Quan M. Nguyen | 2022 | Ph.D. + Post-Doc (2022-2023) | 研究方向包括不规则应用加速（Pipette, Fifer, Phloem） |
| Victor Ying | 2023 | Ph.D. | 研究方向包括推测并行编译（T4） |
| Nikola Samardzic | 2024 | Ph.D. | 研究方向为FHE加速器（F1, CraterLake, BitPacker） |
| Yifan Yang | 2024 | Ph.D. | 研究方向为稀疏CNN加速（ISOSceles, SpZip, Trapezoid） |

### 3.3 已毕业硕士生（M.Eng./S.M.）

包括 Cong Yan (S.M. 2015)、Anurag Mukkara (S.M. 2016)、Webb Horn (M.Eng. 2015)、Virginia Chiu (M.Eng. 2016)、Yee Ling Gan (M.Eng. 2018)、Domenic Nutile (M.Eng. 2020)、Robert Durfee (M.Eng. 2022)、Nithya Attaluri (M.Eng. 2023)、Alan Y. Zhu (M.Eng. 2024) 等。

### 3.4 培养特点分析

Sanchez 的学生培养呈现以下显著特点：

1. **联合指导模式**：多名学生与 Joel Emer（MIT 资深体系结构教授、NVIDIA 首席研究科学家）联合指导，形成稳固的双导师合作模式。此外与 Christina Delimitrou（原 Cornell，现 MIT）也有联合指导。

2. **研究主题从系统向加速器演进**：早期学生（2015-2019）主要研究缓存层次、QoS、推测并行等传统体系结构课题；后期学生（2020年至今）逐步转向专用加速器设计，特别是全同态加密（FHE）加速器、稀疏计算加速器和零知识证明加速器。

3. **高毕业率与高质量产出**：几乎所有博士生都在 ISCA、MICRO、HPCA、ASPLOS 等顶级会议上发表多篇论文，多名学生的论文入选 IEEE Micro Top Picks。

## 四、学术合作网络

### 4.1 Kozyrakis 师承关系及持续合作

**师承关系**：Sanchez 是 Kozyrakis 在斯坦福 MAST Lab 培养的嫡系博士生。Kozyrakis 现为斯坦福大学 Leonard Bosack and Sandy K. Lerner 工程讲席教授，研究方向为计算机体系结构与系统，近期聚焦云计算、机器学习系统和系统-机器学习协同设计。Kozyrakis 本人师从 UC Berkeley 的 David Patterson（图灵奖得主），因此 Sanchez 的学术谱系可追溯至 Patterson-Berkeley 体系结构学派。

**Stanford 期间的合作论文**：
- ZCache: Decoupling Way and Associativity in Caches（MICRO 2010）— Sanchez & Kozyrakis
- Vantage: Scalable and Efficient Fine-Grain Cache Partitioning（ISCA 2011）— Sanchez & Kozyrakis
- 以及博士论文中涉及的 SCD 等其他工作

**MIT 阶段的持续联系**：虽然 Sanchez 在2012年加入 MIT 后建立了独立研究组，但其研究风格——强调软硬件协同设计、全系统原型验证、面向大规模可扩展性——明显继承了 Kozyrakis 和 Patterson 的学术传统。两人在学术理念上保持一致性，尽管公开的联合署名论文主要集中在 Stanford 时期。

### 4.2 MIT 内部合作

Sanchez 在 MIT 内部形成了多维度的合作网络：

**（1）Joel S. Emer（MIT EECS / NVIDIA）**
Emer 是 Sanchez 最核心的 MIT 合作伙伴。两人联合指导多名博士生（Fares Elsabbagh、Shabnam Sheikhha、Xingran Du、Courtney Golden），并共同发表大量论文，涵盖 RTL 仿真加速、稀疏计算加速器（ISOSceles, Trapezoid, SpZip, Gamma）等方向。Emer 同时是 NVIDIA 首席研究科学家，这一联系为学术界与工业界之间架起了桥梁。

**（2）Srinivas Devadas（MIT EECS）**
Devadas 是 MIT 密码学与安全领域的权威教授。Sanchez 与 Devadas 在全同态加密（FHE）加速器方向展开了深度合作，共同发表了 F1（MICRO 2021）、CraterLake（ISCA 2022）、Fhelipe FHE 编译器（PLDI 2024）、零知识证明加速器（MICRO 2024）等重量级论文。这一合作将 Sanchez 的体系结构专长与 Devadas 的密码学专长完美结合，开辟了"密码学-硬件协同设计"的新方向。

**（3）Charles E. Leiserson（MIT CSAIL）**
Sanchez 与 Leiserson（著名算法与并行计算学者）合作在 *Science* 期刊上发表了论文"There's plenty of room at the Top: What will drive computer performance after Moore's law?"（2020年），探讨后摩尔定律时代计算机性能提升的驱动力。该论文合作者还包括 Butler Lampson（图灵奖得主，Microsoft）等业界重量级人物。

**（4）Saman Amarasinghe（MIT CSAIL）**
与 Amarasinghe（编译器与程序优化专家）合作发表"Taming the Zoo: A Unified Graph Compiler Framework for Novel Architectures"（ISCA 2021），将编译器技术与新型体系结构结合。

**（5）Julian Shun（MIT EECS）**
在上述 Taming the Zoo 工作中亦有合作，Shun 是 MIT 并行算法专家。

### 4.3 跨机构/国际合作

**（1）Nathan Beckmann（CMU，Sanchez 前博士生）**
Beckmann 是 Sanchez 培养的第一位博士生（Ph.D. 2015），现为卡内基梅隆大学（CMU）教授。毕业后两人持续合作，共同发表了 Talus（HPCA 2015）、Cache Calculus（CAL 2016）、Jenga（ISCA 2017）、Whirlpool（ASPLOS 2016）、PHI（MICRO 2019）、Livia（ASPLOS 2020）等多篇论文。这一师生合作延续了十余年，是体系结构领域最持久的师承合作之一。

**（2）Ronald Dreslinski（University of Michigan）**
Dreslinski 是密歇根大学体系结构教授，参与合作了 F1 FHE 加速器（MICRO 2021）及其扩展版本。

**（3）Christopher Peikert**
密码学家，参与合作了 F1、CraterLake 等 FHE 加速器工作，为硬件设计提供密码学理论基础。

**（4）Karim Eldefrawy**
来自 HRL Laboratories（原 Hughes Research Laboratories），参与合作了 F1 和 CraterLake 项目，代表了对 FHE 加速器的国防/政府研究兴趣。

**（5）Michael Taylor / Mark Oskin（University of Washington）**
Taylor（现 UW）和 Oskin（UW）参与了 Taming the Zoo（ISCA 2021）的工作，Taylor 在可重构计算和异构架构方面有深厚积累。

**（6）Christopher W. Fletcher**
Fletcher 参与了 Safecracker（ASPLOS 2020）的工作，研究方向为计算机安全与隐私。

**（7）Christina Delimitrou（MIT）**
Delimitrou 原为 Cornell 教授，2022年9月转入 MIT EECS，与 Sanchez 联合指导学生 Viansa Schmulbach，代表了在系统 QoS 和可扩展架构方向的持续合作。

## 五、业界合作关系深度分析

### 5.1 与 Google 的关联

Sanchez 的直接公开合作中未发现与 Google 研究人员的联合署名论文。然而，存在以下间接联系：
- 其博士导师 Kozyrakis 获得过 Google Faculty Award，且 Kozyrakis 近期研究聚焦云计算和机器学习系统，与 Google Cloud 有研究关联。
- Sanchez 参与的 Science 论文（2020年）讨论了后摩尔定律时代的性能驱动力，其合作者包括业界知名人士，该论文的观点对 Google TPU 等专用加速器的发展战略具有理论支撑意义。
- MIT CSAIL 整体与 Google 有多项研究合作和资助关系，Sanchez 作为 CSAIL 核心成员间接受益。

### 5.2 与 Microsoft 的关联

- Sanchez 参与的 Science 论文合作者之一 Butler W. Lampson 是图灵奖得主，曾长期在 Microsoft Research 担任首席软件架构师。这一合作关系将 Sanchez 与 Microsoft 研究体系建立了联系。
- MIT CSAIL 与 Microsoft Research 之间有长期的合作传统，Sanchez 作为 CSAIL 核心教员，可能通过该渠道有间接合作。
- 其博士导师 Kozyrakis 也获得过 Microsoft Faculty Award。

### 5.3 与 Intel 的关联

Sanchez 的公开论文中未发现直接与 Intel 研究人员的联合署名。但其研究对 Intel 有间接影响：
- ZCache 和 Vantage 的缓存设计理念对工业界缓存层次设计有参考价值。
- 其前同事 Joel Emer 与 Intel 有长期合作关系（Emer 曾长期在 DEC/Compaq 和后来在 NVIDIA 工作，也与 Intel 有学术互动）。
- MIT CSAIL 与 Intel 有多项联合研究项目（如 MIT-INTEL 实验室），Sanchez 作为 CSAIL 教员可能在项目中有所参与。

### 5.4 与 NVIDIA 的关联

NVIDIA 是与 Sanchez 关联最紧密的科技公司之一，主要通过 Joel Emer 建立联系：
- Joel Emer 同时担任 NVIDIA 首席研究科学家（Principal Research Scientist），两人联合指导多名博士生并发表大量论文。
- Sanchez 团队近年来在加速器设计（FHE、稀疏计算、零知识证明）方面的研究，与 NVIDIA 在 GPU/AI 加速器领域的技术方向高度互补。
- Sanchez 团队的多篇论文涉及可重构架构和专用加速器，这些工作对 NVIDIA 在异构计算领域的战略有参考价值。

### 5.5 与 DARPA / 政府机构的关联

Sanchez 的研究体现出明显的国防/安全研究关联：

**（1）全同态加密（FHE）加速器项目**
F1（MICRO 2021）和 CraterLake（ISCA 2022）的合著者 Karim Eldefrawy 来自 HRL Laboratories，这是一家由 Boeing 和 GM 共同拥有的著名国防研究实验室。FHE 技术本身具有极高的军事和情报价值，DARPA 在该领域有大量投资（如 DPRIVE 项目）。Sanchez 团队在 FHE 加速器方向的工作几乎可以确定受到 DARPA 或相关政府机构的资助。

**（2）零知识证明加速器**
2024年的零知识证明硬件加速工作进一步强化了其在密码学硬件方向的研究，这与 DARPA 和 IARPA（情报高级研究计划局）在隐私保护计算方面的关注点高度一致。

**（3）MIT CSAIL 的 DARPA 传统**
MIT CSAIL（及其前身 MIT Laboratory for Computer Science）自1980年代起就是 DARPA 在计算机体系结构领域的重要资助对象。Sanchez 作为 CSAIL 核心教员，继承了这一传统。

### 5.6 学术-产业转化模式

Sanchez 的研究呈现出从"纯学术体系结构研究"向"具有强烈产业应用价值的加速器设计"的演进趋势：

- **早期（2012-2018）**：聚焦传统多核体系结构（缓存分区、QoS、一致性），研究更偏向基础理论
- **中期（2018-2020）**：转向稀疏计算和推测并行，与工业界对不规则应用加速的需求对接
- **近期（2020-至今）**：全面投入 FHE 加速器、零知识证明加速器、稀疏矩阵加速器，这些方向与云计算安全、隐私计算、AI 基础设施等产业热点紧密相关

这一演进轨迹表明 Sanchez 敏锐地捕捉到了体系结构领域从通用处理器向专用加速器转变的大趋势，并在关键方向上建立了领先地位。

## 六、重要奖项与学术兼职

### 6.1 IEEE Micro Top Picks 入选

Sanchez 团队多次获得 IEEE Micro Top Picks 奖项，该奖项每年从全球计算机体系结构会议论文中选出最具影响力和新颖性的论文：

- **F1: A Fast and Programmable Accelerator for Fully Homomorphic Encryption**（MICRO 2021）— 入选2021年 IEEE Micro Top Picks
- **An Architecture to Accelerate Computation on Encrypted Data**（F1 扩展版）— 入选2022年 IEEE Micro Top Picks
- **Safecracker: Leaking Secrets Through Compressed Caches**（ASPLOS 2020）— 入选2020年 IEEE Micro Top Picks（后以"Leaking Secrets Through Compressed Caches"发表）

三次 Top Picks 入选反映了其研究在创新性和长期影响力方面的高质量。

### 6.2 Science 期刊发表

2020年在 *Science* 期刊发表论文"There's plenty of room at the Top: What will drive computer performance after Moore's law?"，该论文由 MIT 多位重量级学者（Leiserson, Emer, Lampson 等）联合撰写，对后摩尔定律时代的计算性能发展提出了前瞻性分析。能在 *Science* 这样的综合性顶级期刊发表，在体系结构领域极为罕见。

### 6.3 Kozyrakis 的奖项传承

虽然 Sanchez 本人未在其主页明确列出个人奖项（CV 为 PDF 格式，无法在线获取），但其导师 Kozyrakis 获得过多项重要奖项，包括：
- ACM SIGARCH Maurice Wilkes Award
- ISCA Influential Paper Award
- NSF Career Award
- Okawa Foundation Research Grant
- IBM、Microsoft、Google Faculty Awards

Sanchez 作为 Kozyrakis 的嫡系弟子，继承了这一学术传统，其研究质量和影响力与导师一脉相承。

### 6.4 学术服务

根据公开信息推断，Sanchez 作为计算机体系结构领域活跃的正教授，担任以下类型的学术服务：
- ISCA、MICRO、HPCA、ASPLOS 等顶级会议的程序委员会成员
- IEEE Micro Top Picks 评选委员会参与
- NSF 等研究基金的项目评审专家
- MIT 核心课程（6.5900 计算机系统体系结构、6.191 计算结构）的主讲教授

## 七、Connection 圈层总结

### 核心圈层（第一层）

| 关系类型 | 人物 | 机构 | 关系描述 |
|----------|------|------|----------|
| 博士导师 | Christos Kozyrakis | Stanford | MAST Lab 嫡系师承，ZCache/Vantage/SCD 的共同作者 |
| 核心合作者 | Joel S. Emer | MIT / NVIDIA | 联合指导多名博士生，大量合著论文 |
| 核心合作者 | Srinivas Devadas | MIT | FHE 加速器方向的核心合作伙伴 |
| 第一代弟子 | Nathan Beckmann | CMU | Sanchez 的首位博士生，现为 CMU 教授，持续合作十余年 |

### 紧密圈层（第二层）

| 关系类型 | 人物 | 机构 | 关系描述 |
|----------|------|------|----------|
| 合作者 | Ronald Dreslinski | UMichigan | F1 加速器合作者 |
| 合作者 | Christopher Peikert | — | 密码学理论合作者 |
| 合作者 | Karim Eldefrawy | HRL Laboratories | FHE 加速器合作者，国防研究关联 |
| 合作者 | Charles E. Leiserson | MIT | Science 论文合作者 |
| 合作者 | Saman Amarasinghe | MIT | 编译器-体系结构协同设计 |
| 联合指导 | Christina Delimitrou | MIT | 联合指导博士生 |
| 合作者 | Michael Taylor | UW | 可重构计算合作者 |
| 合作者 | Mark Oskin | UW | 体系结构合作者 |

### 学术家族谱系

```
David Patterson (UC Berkeley, 图灵奖)
    └── Christos Kozyrakis (Stanford, MAST Lab)
            └── Daniel Sanchez (MIT, CSAIL) [博士2012]
                    ├── Nathan Beckmann (CMU) [博士2015]
                    ├── Harshad Kasture [博士2017]
                    ├── Suvinay Subramanian [博士2018]
                    ├── Po-An Tsai [博士2019]
                    ├── Mark Jeffrey [博士2019]
                    ├── Guowei Zhang [博士2020]
                    ├── Maleen Abeydeera [博士2021]
                    ├── Quan M. Nguyen [博士2022]
                    ├── Victor Ying [博士2023]
                    ├── Nikola Samardzic [博士2024]
                    └── Yifan Yang [博士2024]
```

### 产业圈层映射

| 产业方 | 关联强度 | 关联路径 |
|--------|----------|----------|
| NVIDIA | 强 | 通过 Joel Emer（NVIDIA 首席研究科学家）的直接合作 |
| DARPA / 国防机构 | 强 | FHE 加速器研究（与 HRL Laboratories 的 Eldefrawy 合作） |
| Microsoft | 中 | 通过 Butler Lampson（Science 论文合作者）和 Kozyrakis 的 Faculty Award |
| Google | 中-弱 | 通过 Kozyrakis 的 Google Faculty Award 和 MIT CSAIL 的整体合作 |
| Intel | 弱-中 | MIT CSAIL-Intel 传统合作关系，无直接论文合作 |

### 圈层特征总结

1. **强师承链**：Sanchez 处于 Patterson → Kozyrakis → Sanchez 的三代体系结构学派传承链，这一谱系在计算机体系结构领域具有标杆地位。

2. **MIT 内部协作网**：Sanchez 在 MIT 内部构建了以 Emer（加速器/体系结构）、Devadas（密码学）、Leiserson（算法/并行计算）、Amarasinghe（编译器）为核心的多学科协作网络，覆盖了从硬件到软件、从体系结构到密码学的完整技术栈。

3. **师生持续合作模式**：与 Beckmann 的十余年持续合作树立了师生合作的典范，这种模式正在与新毕业学生（Samardzic, Yang 等）延续。

4. **研究方向的产业前瞻性**：从传统多核体系结构到 FHE 加速器、零知识证明硬件的演进，精准对齐了云计算安全、隐私计算等产业热点，体现了敏锐的技术洞察力。

5. **国防与产业双线布局**：通过与 HRL Laboratories 的合作（FHE 方向）建立国防研究联系，同时通过 Emer 与 NVIDIA 保持产业前沿对接，形成了学术-国防-产业的三维合作网络。
