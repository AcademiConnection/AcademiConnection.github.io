报告生成时间：2026年8月14日  
实验室名称：MAST Lab（Multi-scale Architectures & Systems Team）  
依托单位：Stanford University, Department of Electrical Engineering & Computer Science  

---

## 一、实验室教师一览

Stanford MAST Lab 是一个以 Christos Kozyrakis 教授为唯一 PI 的 single-PI 实验室，与此前本系列报告中多教师并立的科研团队（如 PKU 刘譞哲团队、PKU-DAIR、中科大 GCL）在组织结构上有所不同。本报告集以 Kozyrakis 为核心，纳入他培养的4位已毕业博士生中现已成为教授的学者，构成一个"PI + 学术家族教职成员"的5人报告集，与他们之间跨越15年的师生合作网络。

| 姓名 | 职位 | 现任职机构 | 博士毕业院校/年份 | 研究方向 | 报告文件 |
|------|------|-----------|-------------------|---------|----------|
| Christos Kozyrakis | Professor | Stanford University (EE & CS) | UC Berkeley, 2002 | 计算机体系结构、云计算、AI系统 | stanford_mast_kozyrakis_network.md |
| Daniel Sanchez | Professor | MIT EECS / CSAIL | Stanford, 2012 | 计算机体系结构、大规模多核、缓存层次 | stanford_mast_sanchez_network.md |
| Adam Belay | Associate Professor | MIT EECS / CSAIL | Stanford, 2016 | 操作系统抽象、高性能网络、虚拟化 | stanford_mast_belay_network.md |
| Christina Delimitrou | Associate Professor | MIT EECS / CSAIL | Stanford, 2015 | 云计算系统、数据中心资源管理 | stanford_mast_delimitrou_network.md |
| Mingyu Gao (高鸣宇) | Associate Professor | 清华大学交叉信息研究院 (IIIS) | Stanford, 2018 | 体系结构与系统、高效内存架构、AI加速 | stanford_mast_gao_network.md |

---

## 二、教师的角色定位

**实验室负责人与学术家族始祖：** Christos Kozyrakis 是 MAST Lab 的创始人和唯一 PI，2002 年从 UC Berkeley 获得博士学位（导师为图灵奖得主 David Patterson），随后加入 Stanford 任教至今。他还是 Leonard Bosack and Sandy K. Lerner Professor of Engineering，ACM Fellow 和 IEEE Fellow。Kozyrakis 的研究领域横跨计算机体系结构、系统软件和云计算，早期工作集中在多核处理器的内存一致性协议（如 Reactive Nano-Processor、Bulk Scalability）和事务内存，近年来扩展到云计算资源管理与 AI 系统。他的学术家谱可追溯到6代以前（Royal W. Sorensen → Vincent C. Rideout → Gerald Estrin → David F. Martin → David A. Patterson → Christos Kozyrakis），是体系结构领域 Patterson 学派的核心传人。此外，Kozyrakis 与 Stanford 同事 Kunle Olukotun 保持了20余年的深度合作关系，联合指点了多名学生。Kozyrakis 共培养了20位已毕业博士和7位在读博士，其中4位已成为教授，学术后代质量极高。

**MIT 延续与体系结构三代传人：** Daniel Sanchez（2012年博士毕业，MIT Full Professor）是 Kozyrakis 最早期的博士毕业生之一，也是最早独立任教的学生。他的核心贡献包括 ZCache、Vantage 和 SCD 等缓存层次结构创新，在 MIT 指导了10余名博士生并与 Joel Emer (NVIDIA首席研究科学家) 建立了紧密合作关系。他还与同门 Delimitrou 联合指导博士生，延续了 MAST Lab 的学术纽带。值得注意的是，他的学生 Nathan Beckmann 现为 CMU 教授，使 Patterson → Kozyrakis → Sanchez → Beckmann 构成了一条清晰的四代学术传承链。

**MIT 体系结构与系统双子星：** Adam Belay（2016年博士毕业，MIT CSAIL 副教授）和 Christina Delimitrou（2015年博士毕业，MIT EECS 副教授）各自在 MIT 建立了独立的研究组。Belay 专注于操作系统底层抽象和高性能网络（如 IX、Shinjuku、Junction 等项目），他的学生 Amy Ousterhout 现为 UCSD 助理教授、Josh Fried 为 UPenn 助理教授，而已毕业博士中已在学术界形成下一代枝蔓。Delimitrou 于2022年9月从 Cornell 转入 MIT，是 Kozyrakis 弟子中业界合作最突出的成员之一（获得 Microsoft Research Faculty Fellowship、Sloan Fellowship、PECASE Award 等），其与 Kozyrakis 合著的 Paragon 论文在 ASPLOS'24 获得 Influential Paper Award。Sanchez、Belay、Delimitrou 三人现同在 MIT EECS/CSAIL，加上 Kozyrakis 的 Stanford MAST Lab，形成了 Stanford-Berkeley → MIT 的体系结构学术家族迁移路径。

**亚洲学术家族枝蔓：** Mingyu Gao（高鸣宇，2018年博士毕业，清华大学交叉信息院副教授）是 Kozyrakis 唯一回国任教的博士毕业生，也是 MAST Lab 学术家族在亚洲的代表性人物。他在 Stanford 期间的代表作 TETRIS（ASPLOS 2017，与 Kozyrakis 和 Mark Horowitz 合作）获 IEEE Micro Top Picks。回国后在清华 IIIS 建立了 IDEAL Lab，研究方向涵盖高效内存架构、AI加速器和硬件安全。他还担任西安交叉信息核心技术研究院前沿架构与智能芯片中心领衔教授，并创立了西安智芯华玺信息技术有限公司，实现了学术成果的产业化转化。与他在清华 IIIS 的同事包括图灵奖得主姚期智（Andrew Yao），形成了一个顶尖的学术环境。

---

## 三、团队关系网络的整体观察

**1. Patterson → Kozyrakis → 四位教授弟子的学术家族树是本网络最核心的结构特征。** Kozyrakis 作为图灵奖得主 Patterson 的嫡系博士生，继承了体系结构学派的学术传统，并将其拓展到云计算和 AI 系统方向。他培养的20位已毕业博士中，4位已成为教授（Sanchez at MIT、Belay at MIT、Delimitrou at MIT、Gao at 清华），其中3人现同在 MIT EECS/CSAIL，形成了一个高密度的校友集群。这种"一师四教授"的学术家族树在体系结构领域并不多见，体现了 Kozyrakis 在导师和人才培养方面的卓越能力。

**2. "Stanford → MIT"的学术家族迁移路径非常显著。** Kozyrakis 培养的4位教授弟子中，3位（Sanchez、Belay、Delimitrou）最终都汇聚到 MIT EECS/CSAIL，加上 Kozyrakis 本人在 Stanford，形成了一个横跨两所顶尖大学的学术合作走廊。Sanchez 于2012年首先加入 MIT，此后 Belay (2016博士/2017加入MIT) 和 Delimitrou (2015博士/2022从Cornell转入MIT) 先后抵达，三人之间既有同门合作的自然纽带，也各自发展了独立的研究方向。这种同门三人同在一校的情况在计算机体系结构领域堪称独特。

**3. 业界合作网络贯穿 Intel-Google-Microsoft-NVIDIA 四大科技公司，且各成员的产业合作各有侧重。** Kozyrakis 本人获得了 Google、Microsoft、IBM 三大公司的 Faculty Award，并与 HP Labs（Partha Ranganathan）有深度联合研究，通过 Industry-Academia Partnership 与 Intel 等芯片厂商建立长期联系。Delimitrou 获得了 Microsoft Research Faculty Fellowship（2020）和 Google 多次研究奖，其系统已部署于生产云平台。Belay 曾在 Google 工作一年从事数据中心网络研发，并获 Google 和 Meta 研究奖。Sanchez 通过 Joel Emer 与 NVIDIA 建立了深度合作关系，同时与 DARPA 等国防机构有合作（FHE加速器方向）。Gao 在国内与字节跳动（HPCA 2026 Industry Track 联合论文）、华为、DeepSeek 等企业有人才输送和合作关系。总体来看，MAST Lab 学术家族的业界合作覆盖了芯片设计（Intel、NVIDIA）、云计算（Google、Microsoft、Meta）和 AI 系统（字节跳动、DeepSeek）三大产业方向，具有极强的产学研转化能力。

**4. 学术孙辈（Kozyrakis 的弟子的弟子）已经开始在学术界开枝散叶。** Sanchez 的学生 Nathan Beckmann 现为 CMU 教授，Belay 的学生 Amy Ousterhout 为 UCSD 助理教授、Seo Jin Park 为 USC 助理教授、Josh Fried 为 UPenn 助理教授。加上 Gao 在清华培养的学生已有3人毕业去往华为、字节跳动等企业，Kozyrakis 的学术家族已经进入第四代（Beckmann at CMU 等），学术影响力持续扩展。

**5. "Delimitrou 机构信息滞后"是本次交叉核查中发现的最突出问题。** Delimitrou 于2022年9月从 Cornell 转入 MIT，但由于多个独立撰写的子代理均使用了她仍任教于 Cornell 的过时信息，导致5份报告中有大量处需要修正。更严重的是 Sanchez 报告中的原始版本竟然将调动方向完全颠倒（写成"原 MIT 转 Cornell"），属于最严重的方向性事实错误。类似地，Delimitrou 报告中还一度将 Gao 现任机构误写为"Stanford EE 助理教授"（应为清华大学 IIIS 副教授），Gao 报告中则将 MAST Lab 全称误写为"Multi-core"（应为"Multi-scale"）。这些问题已在交叉核查环节全部修正，但提示我们在使用本报告集数据时，对于学者职位、机构等可能随时间变化的信息，应以最新官方页面为准。

---

## 数据来源与说明

本系列报告数据来源包括：Stanford University 官网（stanford.edu）及 Kozyrakis 个人主页（csl.stanford.edu/~christos/）、MAST Lab 官网（mast.stanford.edu）、各弟子所在机构的官方教师主页系统（MIT CSAIL、清华大学 IIIS）、DBLP 学者消歧记录、Google Scholar、ACM/IEEE 数字图书馆、《中国科学报》及 Cornell Chronicle 等媒体公开新闻、各教师个人实验室学生列表页面等。

5位教师名单的确定逻辑为：以 Kozyrakis 为 PI 核心，从他培养的20位已毕业博士生中筛选出已获得大学教授职位的4位学者（Sanchez、Delimitrou、Belay、Gao），构成"PI + 学术家族教职成员"的报告集。这一选人标准与此前本系列对 PKU-DAIR（崔斌 + 杨智，single-PI 实验室的处理方式一致。全体5份报告已经过独立的交叉事实核查环节，重点核实了 Delimitrou 的现任职机构（已从 Cornell 转入 MIT 2022年9月）、各弟子之间的同门关系和合作论文、Kozyrakis 学术家谱链的完整性以及 MAST Lab 全称的准确性，发现的错误均已直接修正于对应报告正文中。
