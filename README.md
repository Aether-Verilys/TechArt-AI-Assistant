# Tech Art AI Assistant

一个为独立开发者和小型工作室优化的通用技术美术AI助手配置，支持多引擎工作流。

## 项目概述

Tech Art AI Assistant 是一个基于Claude Code的配置模板，专门为需要跨多个游戏引擎工作的技术美术师设计。它提供了统一的工具链、最佳实践和AI辅助决策系统，帮助你在Unreal Engine、Unity、Godot等不同引擎间高效工作。

## 特性亮点

### 🎯 多引擎支持
- **Unreal Engine 5+**: 完整支持Nanite、Lumen、蓝图系统
- **Unity**: 支持URP/HDRP、C#脚本、Asset Store集成
- **Godot**: 支持GDScript、开源工作流
- **引擎间资产转换**: 自动化的格式转换和兼容性检查

### 🤖 AI辅助工作流
- **智能决策系统**: 基于项目需求推荐最佳引擎和技术方案
- **自动化工具链**: Python脚本驱动的批量处理和工作流自动化
- **知识库集成**: 跨引擎的最佳实践和常见问题解决方案

### 🛠️ 专业工具集
- **着色器开发**: 跨引擎兼容的着色器编写和调试工具
- **性能分析**: 统一的性能监控和优化建议
- **资产处理**: 批量导入、优化、格式转换
- **VFX系统**: 特效创建和管理工具

## 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/yourusername/TechArt-AI-Assistant.git
cd TechArt-AI-Assistant
```

### 2. 安装依赖
```bash
# 安装Python依赖
pip install -r requirements.txt

# 安装引擎特定工具（可选）
python scripts/setup_engines.py
```

### 3. 配置环境
```bash
# 复制配置文件模板
cp .env.example .env

# 编辑环境变量
# 设置你的引擎路径和偏好
```

### 4. 启动AI助手
```bash
# 使用Claude Code
claude --config .claude

# 或使用其他兼容的AI编码助手
```

## 项目结构

```
TechArt-AI-Assistant/
├── .claude/                    # Claude配置
│   ├── agents/                # AI代理定义
│   └── skills/               # 技能和工具
├── docs/                     # 文档
│   ├── engine-comparison.md  # 引擎对比
│   ├── best-practices.md     # 最佳实践
│   └── workflows/           # 工作流程
├── examples/                 # 示例项目
│   ├── unreal-example/      # UE示例
│   ├── unity-example/       # Unity示例
│   └── godot-example/       # Godot示例
├── scripts/                  # Python工具脚本
├── tools/                   # 独立工具
├── tests/                   # 测试文件
└── config/                  # 配置文件
```

## 使用示例

### 创建跨引擎材质
```python
# 使用提供的工具创建兼容多个引擎的材质
from tools.material_converter import create_cross_engine_material

material = create_cross_engine_material(
    name="water_material",
    engines=["unreal", "unity", "godot"],
    properties={
        "base_color": "#1a6ea0",
        "roughness": 0.1,
        "metallic": 0.0,
        "normal_strength": 0.5
    }
)
```

### 性能分析
```bash
# 运行跨引擎性能测试
python scripts/performance_analyzer.py --project my_game --engines unreal unity
```

### 资产批量处理
```bash
# 批量优化纹理
python scripts/texture_optimizer.py --input assets/textures --output optimized/

# 转换模型格式
python scripts/model_converter.py --format gltf --input assets/models --output converted/
```

## 支持的引擎特性对比

| 特性 | Unreal Engine | Unity | Godot |
|------|---------------|-------|-------|
| 实时GI | Lumen | Enlighten/Baked | VoxelGI/SDFGI |
| 虚拟几何体 | Nanite | 无 | 无 |
| 脚本语言 | C++/Blueprint | C# | GDScript/C# |
| 渲染管线 | Deferred/Forward | URP/HDRP | Forward+/Mobile |
| 物理引擎 | Chaos | PhysX | Godot Physics |
| 2D支持 | Paper2D | 优秀 | 优秀 |
| 价格模型 | 5%收入分成 | 订阅制 | 完全免费 |

## 贡献指南

我们欢迎各种形式的贡献：

### 报告问题
- 使用GitHub Issues报告bug或建议新功能
- 提供详细的复现步骤和环境信息

### 提交代码
1. Fork项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建Pull Request

### 编写文档
- 改进现有文档
- 添加新的教程或示例
- 翻译到其他语言

## 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件。

## 致谢

- 基于 [歌歌gege的Tech Art for Unreal Engine](https://github.com/gege) 项目扩展
- 感谢所有贡献者和用户
- 特别感谢Claude Code团队提供的强大AI编码能力

## 联系方式

- GitHub Issues: [问题跟踪](https://github.com/yourusername/TechArt-AI-Assistant/issues)
- 电子邮件: your.email@example.com
- Discord: [加入我们的社区](https://discord.gg/your-invite-link)

---

**开始你的跨引擎技术美术之旅吧！** 🚀