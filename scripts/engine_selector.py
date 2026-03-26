#!/usr/bin/env python3
"""
引擎选择助手 - 帮助技术美术师选择最适合的游戏引擎
"""

import sys
import json
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum

class Engine(Enum):
    UNREAL = "Unreal Engine"
    UNITY = "Unity"
    GODOT = "Godot"
    CUSTOM = "Custom Engine"

@dataclass
class ProjectRequirements:
    """项目需求"""
    project_type: str  # 2D, 3D, VR, AR, Mobile, Console, PC
    team_size: int
    budget: str  # low, medium, high
    timeline: str  # short, medium, long
    target_platforms: List[str]
    team_experience: Dict[str, int]  # 引擎:经验等级(1-5)
    must_have_features: List[str]
    nice_to_have_features: List[str]

@dataclass
class EngineScore:
    """引擎评分"""
    engine: Engine
    score: float
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]

class EngineSelector:
    """引擎选择器"""
    
    def __init__(self):
        self.engine_data = self._load_engine_data()
    
    def _load_engine_data(self) -> Dict[Engine, Dict[str, Any]]:
        """加载引擎数据"""
        return {
            Engine.UNREAL: {
                "name": "Unreal Engine",
                "strengths": [
                    "高级图形渲染（Nanite, Lumen）",
                    "蓝图可视化编程",
                    "AAA级游戏支持",
                    "强大的物理系统（Chaos）",
                    "影视级实时渲染"
                ],
                "weaknesses": [
                    "学习曲线陡峭",
                    "C++编程要求高",
                    "项目文件较大",
                    "移动端优化复杂",
                    "5%收入分成"
                ],
                "best_for": ["AAA游戏", "影视制作", "建筑可视化", "高端VR"],
                "not_good_for": ["2D游戏", "超轻量级项目", "快速原型"],
                "cost": "5%收入分成（收入超过100万美元）",
                "platforms": ["Windows", "Mac", "Linux", "iOS", "Android", "Console"],
                "language": "C++, Blueprint"
            },
            Engine.UNITY: {
                "name": "Unity",
                "strengths": [
                    "广泛的平台支持",
                    "丰富的Asset Store",
                    "C#脚本易于学习",
                    "强大的2D支持",
                    "庞大的社区"
                ],
                "weaknesses": [
                    "图形质量不如UE",
                    "性能优化需要更多工作",
                    "版本升级可能破坏项目",
                    "订阅费用",
                    "代码结构依赖开发者"
                ],
                "best_for": ["移动游戏", "2D/3D混合", "AR/VR", "原型开发"],
                "not_good_for": ["影视级渲染", "超大型开放世界"],
                "cost": "个人版免费，专业版$2040/年",
                "platforms": ["所有主流平台"],
                "language": "C#"
            },
            Engine.GODOT: {
                "name": "Godot",
                "strengths": [
                    "完全开源免费",
                    "轻量级，启动快速",
                    "优秀的2D支持",
                    "场景树架构清晰",
                    "MIT许可证，无版权问题"
                ],
                "weaknesses": [
                    "3D性能有限",
                    "工具链不够成熟",
                    "社区相对较小",
                    "文档不如商业引擎",
                    "缺少某些高级特性"
                ],
                "best_for": ["2D游戏", "教育项目", "开源项目", "预算有限"],
                "not_good_for": ["AAA级3D游戏", "需要高级图形特性"],
                "cost": "完全免费",
                "platforms": ["Windows", "Mac", "Linux", "Web", "Mobile"],
                "language": "GDScript, C#, C++"
            }
        }
    
    def analyze_requirements(self, requirements: ProjectRequirements) -> List[EngineScore]:
        """分析需求并评分"""
        scores = []
        
        for engine in [Engine.UNREAL, Engine.UNITY, Engine.GODOT]:
            data = self.engine_data[engine]
            score = 0.0
            strengths = []
            weaknesses = []
            recommendations = []
            
            # 1. 项目类型匹配
            if requirements.project_type in ["3D", "VR", "Console", "PC"]:
                if engine == Engine.UNREAL:
                    score += 30
                    strengths.append("优秀的3D和VR支持")
                elif engine == Engine.UNITY:
                    score += 20
                else:
                    score += 10
            
            if requirements.project_type in ["2D", "Mobile"]:
                if engine == Engine.GODOT:
                    score += 30
                    strengths.append("优秀的2D支持")
                elif engine == Engine.UNITY:
                    score += 25
                    strengths.append("强大的2D和移动支持")
                else:
                    score += 10
            
            # 2. 团队经验
            team_exp = requirements.team_experience.get(engine.value, 0)
            if team_exp >= 3:
                score += 20
                strengths.append(f"团队熟悉{engine.value}")
            elif team_exp >= 1:
                score += 10
            else:
                score -= 5
                weaknesses.append(f"团队需要学习{engine.value}")
            
            # 3. 预算考虑
            if requirements.budget == "low":
                if engine == Engine.GODOT:
                    score += 25
                    strengths.append("完全免费")
                elif engine == Engine.UNITY:
                    score += 15  # 个人版免费
                else:
                    score += 5
            elif requirements.budget == "high":
                if engine == Engine.UNREAL:
                    score += 20
                    strengths.append("适合高预算项目")
            
            # 4. 时间线
            if requirements.timeline == "short":
                if engine == Engine.UNITY:
                    score += 15
                    strengths.append("快速原型开发")
                elif engine == Engine.GODOT:
                    score += 10
                else:
                    score += 5
            
            # 5. 必须功能匹配
            for feature in requirements.must_have_features:
                if feature in ["高级图形", "实时GI", "虚拟几何体"] and engine == Engine.UNREAL:
                    score += 15
                    strengths.append(f"支持{feature}")
                elif feature in ["2D物理", "Tilemap"] and engine in [Engine.UNITY, Engine.GODOT]:
                    score += 10
                    strengths.append(f"支持{feature}")
                elif feature in ["开源", "无版权限制"] and engine == Engine.GODOT:
                    score += 20
                    strengths.append(f"支持{feature}")
            
            # 6. 平台支持
            platform_match = all(
                platform in data["platforms"] 
                for platform in requirements.target_platforms
            )
            if platform_match:
                score += 10
                strengths.append("完全支持目标平台")
            else:
                score -= 10
                weaknesses.append("部分平台支持有限")
            
            # 生成建议
            if score < 50:
                recommendations.append("可能不是最佳选择，考虑其他引擎")
            elif score < 70:
                recommendations.append("可以考虑，但需要评估特定需求")
            else:
                recommendations.append("强烈推荐")
            
            scores.append(EngineScore(
                engine=engine,
                score=score,
                strengths=strengths,
                weaknesses=weaknesses,
                recommendations=recommendations
            ))
        
        return sorted(scores, key=lambda x: x.score, reverse=True)
    
    def print_results(self, scores: List[EngineScore], requirements: ProjectRequirements):
        """打印结果"""
        print("\n" + "="*60)
        print("引擎选择分析报告")
        print("="*60)
        
        print(f"\n项目需求:")
        print(f"  项目类型: {requirements.project_type}")
        print(f"  团队规模: {requirements.team_size}人")
        print(f"  预算: {requirements.budget}")
        print(f"  时间线: {requirements.timeline}")
        print(f"  目标平台: {', '.join(requirements.target_platforms)}")
        print(f"  必须功能: {', '.join(requirements.must_have_features)}")
        
        print("\n" + "="*60)
        print("推荐引擎（按评分排序）:")
        print("="*60)
        
        for i, score in enumerate(scores, 1):
            print(f"\n{i}. {score.engine.value} - 评分: {score.score:.1f}/100")
            print(f"   优势: {', '.join(score.strengths[:3])}")
            if score.weaknesses:
                print(f"   劣势: {', '.join(score.weaknesses[:2])}")
            print(f"   建议: {', '.join(score.recommendations)}")
        
        print("\n" + "="*60)
        print("下一步行动:")
        print("="*60)
        
        best_engine = scores[0].engine
        best_data = self.engine_data[best_engine]
        
        print(f"\n1. 试用{best_engine.value}:")
        print(f"   - 下载地址: 官方网站")
        print(f"   - 学习资源: 官方文档、教程")
        
        print(f"\n2. 验证关键需求:")
        for feature in requirements.must_have_features:
            print(f"   - {feature}: {'✓ 支持' if feature in str(best_data['strengths']) else '⚠ 需要验证'}")
        
        print(f"\n3. 评估成本:")
        print(f"   - {best_data['cost']}")
        
        print(f"\n4. 制定学习计划:")
        team_exp = requirements.team_experience.get(best_engine.value, 0)
        if team_exp < 3:
            print(f"   - 团队需要{3-team_exp}个月的学习时间")
            print(f"   - 推荐学习路径: 官方教程 → 小项目实践 → 实际项目")

def main():
    """主函数"""
    print("欢迎使用引擎选择助手！")
    print("请回答以下问题来评估你的项目需求。\n")
    
    # 收集需求（简化版）
    requirements = ProjectRequirements(
        project_type=input("项目类型 (2D/3D/VR/Mobile等): "),
        team_size=int(input("团队规模: ")),
        budget=input("预算 (low/medium/high): "),
        timeline=input("时间线 (short/medium/long): "),
        target_platforms=input("目标平台 (用逗号分隔): ").split(","),
        team_experience={
            "Unreal Engine": int(input("团队对Unreal Engine的熟悉程度 (1-5): ")),
            "Unity": int(input("团队对Unity的熟悉程度 (1-5): ")),
            "Godot": int(input("团队对Godot的熟悉程度 (1-5): "))
        },
        must_have_features=input("必须有的功能 (用逗号分隔): ").split(","),
        nice_to_have_features=input("希望有的功能 (用逗号分隔): ").split(",")
    )
    
    # 分析并显示结果
    selector = EngineSelector()
    scores = selector.analyze_requirements(requirements)
    selector.print_results(scores, requirements)
    
    # 保存结果到文件
    with open("engine_selection_report.json", "w", encoding="utf-8") as f:
        report = {
            "requirements": {
                "project_type": requirements.project_type,
                "team_size": requirements.team_size,
                "budget": requirements.budget,
                "timeline": requirements.timeline,
                "target_platforms": requirements.target_platforms,
                "team_experience": requirements.team_experience,
                "must_have_features": requirements.must_have_features
            },
            "results": [
                {
                    "engine": score.engine.value,
                    "score": score.score,
                    "strengths": score.strengths,
                    "weaknesses": score.weaknesses,
                    "recommendations": score.recommendations
                }
                for score in scores
            ]
        }
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n详细报告已保存到: engine_selection_report.json")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"\n错误: {e}")
        sys.exit(1)