# Tech Art AI Assistant

为独立开发者和小型工作室优化的通用技术美术AI助手配置
专注于多引擎支持 + AI辅助工作流

设计者：Aether (基于歌歌gege的UE版本扩展)
license MIT | agents 12 | skills 18 | rules mp | 4 built for Claude Code | status experimental

## 简介

这是一个专为小型工作室和独立技术美术师优化的通用AI助手配置模板。当您需要跨多个引擎和工具工作时，您需要：

- ✅ 跨引擎材质与着色器开发工具
- ✅ 程序化生成与自动化
- ✅ VFX系统与特效管理
- ✅ 物理交互与性能优化
- ✅ 多引擎资产处理与转换
- ✅ Python脚本与工具开发
- ✅ AI辅助决策与工作流

这个配置提供了所有这些，专注于单人高效工作，支持Unreal Engine、Unity、Godot等多个引擎。

## 目标用户

### 适用场景
- **全能型技术美术师**：为1-30人团队或自由职业者提供全栈支持
- **跨引擎开发者**：需要在多个游戏引擎间切换工作
- **AI辅助系统设计师**：利用AI驱动的标准化工作流

### 核心痛点
- **引擎切换成本高**：不同引擎的工作流和工具差异大
- **技术栈碎片化**：需要掌握多种引擎的特定技术
- **决策复杂度高**：在多引擎环境下做出正确的技术选择
- **资源复用困难**：资产和代码在不同引擎间的迁移

## 核心特性

| 类别 | 数量 | 说明 |
|------|------|------|
| **Agents** | 12 | 通用技术美术师、性能分析师、管线TD、着色器专家、VFX艺术家、程序化生成专家、Unity专家、UE专家、Godot专家、Python开发者、资产处理专家、决策顾问 |
| **Skills** | 18 | 跨引擎材质开发、着色器转换、网格处理、资产优化、性能分析、纹理管道、Python脚本、技术文档、引擎特定工具等 |
| **Hooks** | 15 | 自动化工具，入库前置校验，资产体检测，决策自动沉淀，引擎转换检查 |
| **Rules** | 8 | 资产命名、着色器代码、材质制作、性能预算 + 项目级规则（安全、测试、代码风格、引擎兼容性） |
| **Commands** | 9 | standup、debt-add、debt-review、audit、perf-check、decision、new-skill、engine-switch、asset-convert |
| **MCP 服务** | 5 | 文件系统、Git历史、网页获取、结构化推理、引擎文档查询 |
| **文档** | 6 | 高频更新 + 决策 + 工作流程 + 引擎对比 + 最佳实践 |

## 项目结构

```
TechArt-AI-Assistant/
├── CLAUDE.md              # 主配置文件
├── SOUL.md                # 项目灵魂文件
├── MEMORY.md              # 项目记忆
├── RULES.md               # 规则文件
├── README.md              # 项目说明
├── .claude/
│   ├── agents/
│   │   ├── general-technical-artist.md
│   │   ├── performance-analyst.md
│   │   ├── pipeline-td.md
│   │   ├── shader-specialist.md
│   │   ├── vfx-artist.md
│   │   ├── procedural-generation-expert.md
│   │   ├── unity-specialist.md
│   │   ├── unreal-specialist.md
│   │   ├── godot-specialist.md
│   │   ├── python-developer.md
│   │   ├── asset-processor.md
│   │   └── decision-advisor.md
│   └── skills/
│       ├── cross-engine-shaders/
│       ├── asset-conversion/
│       ├── performance-optimization/
│       └── ... (其他技能)
├── docs/
│   ├── engine-comparison.md
│   ├── best-practices.md
│   └── workflows/
└── examples/
    ├── unreal-example/
    ├── unity-example/
    └── godot-example/
```

## 主配置：规则+工作流+Agent路由

### 决策算法
- **价值观对齐**：以项目成功和用户体验为核心
- **批判性思维**：多角度评估技术选择
- **性能直觉**：基于经验的性能预判
- **成本效益分析**：平衡技术先进性和实现成本

### 引擎选择策略
1. **需求分析**：根据项目类型、团队规模、目标平台选择引擎
2. **技术评估**：评估各引擎对特定功能的支持程度
3. **成本计算**：考虑学习成本、开发成本、维护成本
4. **未来扩展**：考虑项目的长期发展和技术演进

### 工作流优化
- **资产标准化**：创建跨引擎兼容的资产格式
- **工具链统一**：开发通用的Python工具链
- **知识沉淀**：建立跨引擎的最佳实践库
- **自动化测试**：确保多引擎兼容性

## 快速开始

1. **克隆项目**：
   ```bash
   git clone <repository-url>
   cd TechArt-AI-Assistant
   ```

2. **配置环境**：
   ```bash
   # 安装Python依赖
   pip install -r requirements.txt
   ```

3. **选择引擎**：
   ```bash
   # 查看可用引擎配置
   python scripts/engine-selector.py
   ```

4. **开始工作**：
   ```bash
   # 启动AI助手
   claude --config .claude
   ```

## 支持的引擎

| 引擎 | 支持级别 | 主要特性 |
|------|----------|----------|
| **Unreal Engine** | ⭐⭐⭐⭐⭐ | 高级图形、蓝图系统、Nanite、Lumen |
| **Unity** | ⭐⭐⭐⭐ | C#脚本、Asset Store、跨平台支持 |
| **Godot** | ⭐⭐⭐ | 开源、轻量级、GDScript |
| **自定义引擎** | ⭐⭐ | 灵活配置、深度定制 |

## 贡献指南

欢迎贡献：
1. 新的引擎支持
2. 跨引擎工具
3. 最佳实践文档
4. 性能优化技巧

## 许可证

MIT License - 详见 LICENSE 文件