#!/usr/bin/env python3
"""
Tech Art AI Assistant 基本使用示例
展示如何利用项目中的工具进行跨引擎技术美术工作
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def demo_engine_selection():
    """演示引擎选择工具"""
    print("="*60)
    print("演示: 引擎选择助手")
    print("="*60)
    
    # 模拟项目需求
    from scripts.engine_selector import ProjectRequirements, EngineSelector
    
    requirements = ProjectRequirements(
        project_type="3D",
        team_size=5,
        budget="medium",
        timeline="medium",
        target_platforms=["Windows", "PlayStation", "Xbox"],
        team_experience={
            "Unreal Engine": 4,
            "Unity": 3,
            "Godot": 1
        },
        must_have_features=["高级图形", "物理破坏", "网络同步"],
        nice_to_have_features=["光线追踪", "AI系统"]
    )
    
    selector = EngineSelector()
    scores = selector.analyze_requirements(requirements)
    
    print("\n分析结果:")
    for score in scores[:2]:  # 只显示前两个
        print(f"\n{score.engine.value}: {score.score:.1f}/100")
        print(f"  优势: {', '.join(score.strengths[:2])}")
        if score.weaknesses:
            print(f"  劣势: {', '.join(score.weaknesses[:1])}")
    
    return scores[0].engine.value

def demo_texture_analysis():
    """演示纹理分析工具"""
    print("\n" + "="*60)
    print("演示: 纹理分析工具")
    print("="*60)
    
    # 创建一个测试纹理信息
    from tools.texture_analyzer import (
        TextureInfo, TextureFormat, 
        TextureAnalyzer, EngineCompatibility, OptimizationSuggestion
    )
    
    # 模拟纹理数据
    texture_info = TextureInfo(
        path="/example/texture.png",
        format=TextureFormat.PNG,
        width=4096,
        height=4096,
        channels=4,
        size_bytes=50 * 1024 * 1024,  # 50MB
        mipmaps=False,
        alpha_channel=True
    )
    
    analyzer = TextureAnalyzer()
    
    # 检查兼容性
    compatibility = analyzer.check_engine_compatibility(
        texture_info, 
        ["Unreal Engine", "Unity", "Godot"]
    )
    
    # 生成优化建议
    suggestions = analyzer.generate_optimization_suggestions(texture_info)
    
    print(f"\n纹理分析: {texture_info.path}")
    print(f"尺寸: {texture_info.width}x{texture_info.height}")
    print(f"格式: {texture_info.format.value.upper()}")
    print(f"大小: {texture_info.size_bytes / (1024*1024):.1f} MB")
    
    print("\n兼容性检查:")
    for comp in compatibility:
        support_symbol = {
            "full": "✅",
            "partial": "⚠️",
            "limited": "⚠️",
            "none": "❌"
        }
        print(f"  {comp.engine}: {support_symbol.get(comp.support.value, '?')}")
    
    print("\n优化建议:")
    for suggestion in suggestions[:3]:  # 只显示前三个
        print(f"  • {suggestion.description}")
        print(f"    建议: {suggestion.action}")
    
    return len(suggestions)

def demo_cross_engine_workflow():
    """演示跨引擎工作流"""
    print("\n" + "="*60)
    print("演示: 跨引擎工作流")
    print("="*60)
    
    workflows = [
        {
            "name": "材质转换工作流",
            "steps": [
                "1. 分析源引擎材质结构",
                "2. 提取着色器代码和参数",
                "3. 转换为目标引擎格式",
                "4. 验证视觉效果一致性",
                "5. 优化性能参数"
            ],
            "engines": ["Unreal Engine → Unity", "Unity → Godot"]
        },
        {
            "name": "资产优化工作流",
            "steps": [
                "1. 批量分析资产目录",
                "2. 识别性能瓶颈",
                "3. 自动优化设置",
                "4. 生成优化报告",
                "5. 验证优化效果"
            ],
            "engines": ["所有引擎通用"]
        },
        {
            "name": "性能分析工作流",
            "steps": [
                "1. 收集各引擎性能数据",
                "2. 统一分析指标",
                "3. 识别跨引擎共性问题",
                "4. 提供通用优化建议",
                "5. 监控改进效果"
            ],
            "engines": ["Unreal Engine", "Unity", "Godot"]
        }
    ]
    
    print("\n可用工作流:")
    for i, workflow in enumerate(workflows, 1):
        print(f"\n{i}. {workflow['name']}")
        print(f"   支持引擎: {', '.join(workflow['engines'])}")
        print(f"   步骤: {len(workflow['steps'])}步")
    
    return workflows

def create_project_structure():
    """创建示例项目结构"""
    print("\n" + "="*60)
    print("演示: 创建跨引擎项目结构")
    print("="*60)
    
    structure = {
        "项目根目录": [
            "README.md - 项目说明",
            "CLAUDE.md - AI助手配置",
            "requirements.txt - Python依赖"
        ],
        "assets/ - 资产目录": [
            "textures/ - 纹理文件",
            "models/ - 3D模型",
            "materials/ - 材质文件",
            "shaders/ - 着色器代码"
        ],
        "src/ - 源代码": [
            "unreal/ - UE特定代码",
            "unity/ - Unity特定代码",
            "godot/ - Godot特定代码",
            "common/ - 通用代码"
        ],
        "tools/ - 工具脚本": [
            "converter/ - 格式转换工具",
            "optimizer/ - 优化工具",
            "analyzer/ - 分析工具"
        ],
        "docs/ - 文档": [
            "engine_comparison.md - 引擎对比",
            "best_practices.md - 最佳实践",
            "workflows/ - 工作流程文档"
        ]
    }
    
    print("\n推荐的项目结构:")
    for category, items in structure.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  {item}")
    
    return structure

def main():
    """主演示函数"""
    print("Tech Art AI Assistant 演示")
    print("="*60)
    
    try:
        # 演示各个功能
        selected_engine = demo_engine_selection()
        suggestion_count = demo_texture_analysis()
        workflows = demo_cross_engine_workflow()
        structure = create_project_structure()
        
        print("\n" + "="*60)
        print("演示总结")
        print("="*60)
        
        print(f"\n1. 推荐引擎: {selected_engine}")
        print(f"2. 纹理优化建议: {suggestion_count} 条")
        print(f"3. 可用工作流: {len(workflows)} 个")
        print(f"4. 项目结构: {len(structure)} 个主要目录")
        
        print("\n" + "="*60)
        print("下一步行动建议:")
        print("="*60)
        
        print("""
1. 运行引擎选择工具详细分析你的项目:
   python scripts/engine_selector.py

2. 分析现有纹理资产:
   python tools/texture_analyzer.py <纹理目录>

3. 查看完整文档:
   - docs/engine_comparison.md (引擎对比)
   - docs/best_practices.md (最佳实践)

4. 开始你的跨引擎项目:
   - 选择合适的引擎
   - 设置项目结构
   - 使用提供的工具链
        """)
        
    except ImportError as e:
        print(f"\n导入错误: {e}")
        print("请确保已安装所有依赖: pip install -r requirements.txt")
    except Exception as e:
        print(f"\n演示过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()