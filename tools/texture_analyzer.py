#!/usr/bin/env python3
"""
纹理分析工具 - 分析纹理文件的属性和优化建议
支持跨引擎纹理格式分析
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("警告: 需要安装Pillow库: pip install pillow")

class TextureFormat(Enum):
    """纹理格式枚举"""
    PNG = "png"
    JPEG = "jpeg"
    JPG = "jpg"
    TGA = "tga"
    BMP = "bmp"
    TIFF = "tiff"
    DDS = "dds"
    EXR = "exr"
    HDR = "hdr"
    WEBP = "webp"

class EngineSupport(Enum):
    """引擎支持级别"""
    FULL = "full"  # 完全支持
    PARTIAL = "partial"  # 部分支持
    LIMITED = "limited"  # 有限支持
    NONE = "none"  # 不支持

@dataclass
class TextureInfo:
    """纹理信息"""
    path: str
    format: TextureFormat
    width: int
    height: int
    channels: int
    size_bytes: int
    mipmaps: bool
    compression: Optional[str] = None
    color_space: Optional[str] = None
    alpha_channel: bool = False
    
@dataclass
class EngineCompatibility:
    """引擎兼容性信息"""
    engine: str
    support: EngineSupport
    notes: List[str]
    recommended_format: Optional[str] = None
    conversion_needed: bool = False

@dataclass
class OptimizationSuggestion:
    """优化建议"""
    category: str  # size, format, compression, etc.
    description: str
    potential_savings: str  # e.g., "50% size reduction"
    action: str
    priority: str  # high, medium, low

class TextureAnalyzer:
    """纹理分析器"""
    
    def __init__(self):
        self.engine_compatibility = self._load_compatibility_data()
    
    def _load_compatibility_data(self) -> Dict[str, Dict[str, EngineSupport]]:
        """加载引擎兼容性数据"""
        return {
            "Unreal Engine": {
                "png": EngineSupport.FULL,
                "jpeg": EngineSupport.FULL,
                "jpg": EngineSupport.FULL,
                "tga": EngineSupport.FULL,
                "bmp": EngineSupport.FULL,
                "tiff": EngineSupport.PARTIAL,
                "dds": EngineSupport.FULL,
                "exr": EngineSupport.FULL,
                "hdr": EngineSupport.FULL,
                "webp": EngineSupport.LIMITED,
            },
            "Unity": {
                "png": EngineSupport.FULL,
                "jpeg": EngineSupport.FULL,
                "jpg": EngineSupport.FULL,
                "tga": EngineSupport.FULL,
                "bmp": EngineSupport.FULL,
                "tiff": EngineSupport.PARTIAL,
                "dds": EngineSupport.PARTIAL,
                "exr": EngineSupport.FULL,
                "hdr": EngineSupport.FULL,
                "webp": EngineSupport.FULL,
            },
            "Godot": {
                "png": EngineSupport.FULL,
                "jpeg": EngineSupport.FULL,
                "jpg": EngineSupport.FULL,
                "tga": EngineSupport.FULL,
                "bmp": EngineSupport.FULL,
                "tiff": EngineSupport.PARTIAL,
                "dds": EngineSupport.LIMITED,
                "exr": EngineSupport.PARTIAL,
                "hdr": EngineSupport.PARTIAL,
                "webp": EngineSupport.FULL,
            }
        }
    
    def analyze_texture(self, texture_path: str) -> Optional[TextureInfo]:
        """分析单个纹理文件"""
        if not HAS_PIL:
            print("错误: 需要Pillow库来解析图像")
            return None
        
        try:
            path = Path(texture_path)
            if not path.exists():
                print(f"错误: 文件不存在: {texture_path}")
                return None
            
            # 获取文件信息
            file_size = path.stat().st_size
            file_ext = path.suffix.lower()[1:]  # 去掉点号
            
            # 使用PIL打开图像
            with Image.open(texture_path) as img:
                width, height = img.size
                mode = img.mode
                format_name = img.format.lower() if img.format else file_ext
                
                # 确定通道数
                if mode == "L":
                    channels = 1  # 灰度
                elif mode == "LA":
                    channels = 2  # 灰度+alpha
                elif mode == "RGB":
                    channels = 3
                elif mode == "RGBA":
                    channels = 4
                else:
                    channels = 0  # 未知
                
                # 检查alpha通道
                has_alpha = "A" in mode or mode == "RGBA" or mode == "LA"
                
                # 检查mipmaps（简单检测）
                has_mipmaps = file_ext in ["dds"]  # DDS通常包含mipmaps
                
                # 检查颜色空间（简单检测）
                color_space = None
                if "icc_profile" in img.info:
                    color_space = "ICC Profile"
                elif img.mode in ["RGB", "RGBA"]:
                    color_space = "sRGB"  # 假设
                
                return TextureInfo(
                    path=str(texture_path),
                    format=TextureFormat(file_ext),
                    width=width,
                    height=height,
                    channels=channels,
                    size_bytes=file_size,
                    mipmaps=has_mipmaps,
                    color_space=color_space,
                    alpha_channel=has_alpha
                )
                
        except Exception as e:
            print(f"分析纹理时出错 {texture_path}: {e}")
            return None
    
    def check_engine_compatibility(self, texture_info: TextureInfo, engines: List[str] = None) -> List[EngineCompatibility]:
        """检查引擎兼容性"""
        if engines is None:
            engines = ["Unreal Engine", "Unity", "Godot"]
        
        results = []
        format_str = texture_info.format.value
        
        for engine in engines:
            if engine not in self.engine_compatibility:
                continue
            
            support = self.engine_compatibility[engine].get(format_str, EngineSupport.NONE)
            notes = []
            recommended_format = None
            conversion_needed = False
            
            if support == EngineSupport.FULL:
                notes.append("完全支持，无需转换")
            elif support == EngineSupport.PARTIAL:
                notes.append("部分支持，可能需要额外配置")
                recommended_format = "png" if texture_info.alpha_channel else "jpg"
                conversion_needed = True
            elif support == EngineSupport.LIMITED:
                notes.append("有限支持，建议转换格式")
                recommended_format = "png"
                conversion_needed = True
            else:  # NONE
                notes.append("不支持，必须转换格式")
                recommended_format = "png" if texture_info.alpha_channel else "jpg"
                conversion_needed = True
            
            # 添加特定建议
            if format_str == "tga" and engine == "Godot":
                notes.append("Godot对TGA支持较好，但PNG是更通用的选择")
            
            if format_str == "exr" and engine in ["Unity", "Godot"]:
                notes.append("HDR纹理，确保正确配置颜色空间")
            
            results.append(EngineCompatibility(
                engine=engine,
                support=support,
                notes=notes,
                recommended_format=recommended_format,
                conversion_needed=conversion_needed
            ))
        
        return results
    
    def generate_optimization_suggestions(self, texture_info: TextureInfo) -> List[OptimizationSuggestion]:
        """生成优化建议"""
        suggestions = []
        
        # 1. 尺寸检查
        max_recommended_size = 4096  # 4K
        if texture_info.width > max_recommended_size or texture_info.height > max_recommended_size:
            suggestions.append(OptimizationSuggestion(
                category="size",
                description=f"纹理尺寸过大 ({texture_info.width}x{texture_info.height})",
                potential_savings="75%+ 内存节省",
                action=f"缩小到 {max_recommended_size} 像素以内",
                priority="high"
            ))
        
        # 2. 格式优化
        current_format = texture_info.format.value
        if current_format in ["bmp", "tiff"]:
            suggestions.append(OptimizationSuggestion(
                category="format",
                description=f"格式 {current_format.upper()} 不是游戏开发的最佳选择",
                potential_savings="50%+ 文件大小",
                action=f"转换为 PNG（有alpha）或 JPEG（无alpha）",
                priority="high"
            ))
        
        # 3. 通道优化
        if texture_info.channels == 4 and not texture_info.alpha_channel:
            suggestions.append(OptimizationSuggestion(
                category="channels",
                description="RGBA格式但没有实际alpha数据",
                potential_savings="25% 内存节省",
                action="转换为RGB格式",
                priority="medium"
            ))
        
        # 4. 文件大小检查
        size_mb = texture_info.size_bytes / (1024 * 1024)
        if size_mb > 10:  # 大于10MB
            suggestions.append(OptimizationSuggestion(
                category="compression",
                description=f"文件过大 ({size_mb:.1f}MB)",
                potential_savings="50-80% 文件大小",
                action="增加压缩级别或使用更高效的格式",
                priority="high"
            ))
        
        # 5. Mipmaps建议
        if not texture_info.mipmaps and texture_info.width >= 256:
            suggestions.append(OptimizationSuggestion(
                category="mipmaps",
                description="缺少mipmaps，可能导致远处纹理闪烁",
                potential_savings="改善渲染质量",
                action="生成mipmaps链",
                priority="medium"
            ))
        
        return suggestions
    
    def analyze_directory(self, directory_path: str, recursive: bool = False) -> Dict:
        """分析目录中的所有纹理"""
        results = {
            "directory": directory_path,
            "total_files": 0,
            "textures": [],
            "summary": {
                "by_format": {},
                "by_size": {"small": 0, "medium": 0, "large": 0},
                "total_size_bytes": 0
            }
        }
        
        path = Path(directory_path)
        if not path.exists():
            print(f"错误: 目录不存在: {directory_path}")
            return results
        
        # 收集纹理文件
        texture_extensions = {fmt.value for fmt in TextureFormat}
        pattern = "**/*" if recursive else "*"
        
        for file_path in path.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower()[1:] in texture_extensions:
                texture_info = self.analyze_texture(str(file_path))
                if texture_info:
                    results["textures"].append(asdict(texture_info))
                    results["total_files"] += 1
                    results["summary"]["total_size_bytes"] += texture_info.size_bytes
                    
                    # 按格式统计
                    fmt = texture_info.format.value
                    results["summary"]["by_format"][fmt] = results["summary"]["by_format"].get(fmt, 0) + 1
                    
                    # 按尺寸分类
                    max_dim = max(texture_info.width, texture_info.height)
                    if max_dim <= 512:
                        results["summary"]["by_size"]["small"] += 1
                    elif max_dim <= 2048:
                        results["summary"]["by_size"]["medium"] += 1
                    else:
                        results["summary"]["by_size"]["large"] += 1
        
        return results
    
    def print_report(self, texture_info: TextureInfo, 
                    compatibility: List[EngineCompatibility],
                    suggestions: List[OptimizationSuggestion]):
        """打印分析报告"""
        print("\n" + "="*60)
        print("纹理分析报告")
        print("="*60)
        
        print(f"\n文件: {texture_info.path}")
        print(f"格式: {texture_info.format.value.upper()}")
        print(f"尺寸: {texture_info.width} x {texture_info.height}")
        print(f"通道: {texture_info.channels} ({'有alpha' if texture_info.alpha_channel else '无alpha'})")
        print(f"大小: {texture_info.size_bytes / 1024:.1f} KB")
        if texture_info.color_space:
            print(f"颜色空间: {texture_info.color_space}")
        print(f"Mipmaps: {'是' if texture_info.mipmaps else '否'}")
        
        print("\n" + "-"*60)
        print("引擎兼容性:")
        print("-"*60)
        
        for comp in compatibility:
            support_icon = {
                EngineSupport.FULL: "✅",
                EngineSupport.PARTIAL: "⚠️",
                EngineSupport.LIMITED: "⚠️",
                EngineSupport.NONE: "❌"
            }[comp.support]
            
            print(f"\n{comp.engine}: {support_icon} {comp.support.value}")
            for note in comp.notes:
                print(f"  • {note}")
            if comp.conversion_needed and comp.recommended_format:
                print(f"  建议转换到: {comp.recommended_format.upper()}")
        
        if suggestions:
            print("\n" + "-"*60)
            print("优化建议:")
            print("-"*60)
            
            priority_order = {"high": 1, "medium": 2, "low": 3}
            suggestions.sort(key=lambda x: priority_order[x.priority])
            
            for suggestion in suggestions:
                priority_icon = {
                    "high": "🔴",
                    "medium": "🟡",
                    "low": "🟢"
                }[suggestion.priority]
                
                print(f"\n{priority_icon} [{suggestion.priority.upper()}] {suggestion.category}")
                print(f"  问题: {suggestion.description}")
                print(f"  潜在节省: {suggestion.potential_savings}")
                print(f"  建议操作: {suggestion.action}")

def main():
    """主函数"""
    if not HAS_PIL:
        print("请先安装Pillow库: pip install pillow")
        return
    
    import argparse
    
    parser = argparse.ArgumentParser(description="纹理分析工具")
    parser.add_argument("path", help="纹理文件或目录路径")
    parser.add_argument("--engines", nargs="+", default=["Unreal Engine", "Unity", "Godot"],
                       help="要检查的引擎列表")
    parser.add_argument("--recursive", action="store_true",
                       help="递归分析目录")
    parser.add_argument("--output", help="输出JSON报告文件")
    parser.add_argument("--summary", action="store_true",
                       help="只显示摘要信息")
    
    args = parser.parse_args()
    
    analyzer = TextureAnalyzer()
    path = Path(args.path)
    
    if path.is_file():
        # 分析单个文件
        texture_info = analyzer.analyze_texture(str(path))
        if texture_info:
            compatibility = analyzer.check_engine_compatibility(texture_info, args.engines)
            suggestions = analyzer.generate_optimization_suggestions(texture_info)
            analyzer.print_report(texture_info, compatibility, suggestions)
            
            # 保存报告
            if args.output:
                report = {
                    "texture_info": asdict(texture_info),
                    "compatibility": [
                        {
                            "engine": comp.engine,
                            "support": comp.support.value,
                            "notes": comp.notes,
                            "recommended_format": comp.recommended_format,
                            "conversion_needed": comp.conversion_needed
                        }
                        for comp in compatibility
                    ],
                    "suggestions": [
                        {
                            "category": s.category,
                            "description": s.description,
                            "potential_savings": s.potential_savings,
                            "action": s.action,
                            "priority": s.priority
                        }
                        for s in suggestions
                    ]
                }
                with open(args.output, "w", encoding="utf-8") as f:
                    json.dump(report, f, indent=2, ensure_ascii=False)
                print(f"\n报告已保存到: {args.output}")
    
    elif path.is_dir():
        # 分析目录
        results = analyzer.analyze_directory(str(path), args.recursive)
        
        if args.summary:
            print(f"\n目录分析摘要: {path}")
            print(f"总纹理文件: {results['total_files']}")
            print(f"总大小: {results['summary']['total_size_bytes'] / (1024*1024):.1f} MB")
            
            print("\n按格式分布:")
            for fmt, count in sorted(results['summary']['by_format'].items()):
                print(f"  {fmt.upper()}: {count}")
            
            print("\n按尺寸分布:")
            print(f"  小 (<512): {results['summary']['by_size']['small']}")
            print(f"  中 (512-2048): {results['summary']['by_size']['medium']}")
            print(f"  大 (>2048): {results['summary']['by_size']['large']}")
        
        else:
            print(f"\n分析完成，共找到 {results['total_files']} 个纹理文件")
            print(f"详细报告已生成，使用 --output 参数保存完整报告")
        
        # 保存完整报告
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"完整报告已保存到: {args.output}")
    
    else:
        print(f"错误: 路径不存在: {args.path}")

if __name__ == "__main__":
    main()