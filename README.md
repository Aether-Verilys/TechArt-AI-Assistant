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
