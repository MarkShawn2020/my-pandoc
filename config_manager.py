#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path

class ConfigManager:
    """配置管理器"""
    
    def __init__(self):
        self.global_config_path = Path.home() / '.config' / 'pandoc-enhanced' / 'config.yaml'
        self.project_config_name = '.pandoc-enhanced.yaml'
        
    def get_default_config(self):
        """获取默认配置"""
        return {
            'output': {
                'directory': str(Path.home() / 'Documents'),
                'format': 'pdf'
            },
            'document': {
                'author': '南川',
                'subtitle': 'V0.1',
                'language': 'zh-CN'
            },
            'pdf': {
                'template': 'eisvogel',
                'theme': 'purple',
                'toc': True,
                'emoji': True,
                'fonts': {
                    'main': 'Songti SC',
                    'cjk': 'Songti SC',
                    'mono': 'Noto Sans Mono CJK SC',
                    'sans': 'Noto Sans CJK SC'
                }
            },
            'themes': {
                'blue': '1E88E5',
                'red': 'E53935',
                'green': '43A047',
                'purple': '5D1EB1',
                'orange': 'FB8C00',
                'teal': '00ACC1'
            }
        }
    
    def load_config(self, project_dir=None):
        """加载配置文件"""
        config = self.get_default_config()
        
        # 加载全局配置
        if self.global_config_path.exists():
            with open(self.global_config_path, 'r', encoding='utf-8') as f:
                global_config = yaml.safe_load(f)
                if global_config:
                    self._merge_config(config, global_config)
        
        # 加载项目配置
        if project_dir:
            project_config_path = Path(project_dir) / self.project_config_name
            if project_config_path.exists():
                with open(project_config_path, 'r', encoding='utf-8') as f:
                    project_config = yaml.safe_load(f)
                    if project_config:
                        self._merge_config(config, project_config)
        
        return config
    
    def save_global_config(self, config):
        """保存全局配置"""
        self.global_config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.global_config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
    
    def create_project_config(self, project_dir, config=None):
        """创建项目配置文件"""
        if config is None:
            config = {
                'document': {
                    'title': '',
                    'author': '南川',
                    'subtitle': 'V0.1'
                },
                'pdf': {
                    'theme': 'purple',
                    'toc': True
                }
            }
        
        project_config_path = Path(project_dir) / self.project_config_name
        with open(project_config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
        
        return project_config_path
    
    def _merge_config(self, base_config, override_config):
        """递归合并配置"""
        for key, value in override_config.items():
            if key in base_config and isinstance(base_config[key], dict) and isinstance(value, dict):
                self._merge_config(base_config[key], value)
            else:
                base_config[key] = value

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 config_manager.py <command> [args]")
        print("Commands:")
        print("  init [directory]     - 在指定目录创建项目配置")
        print("  show [directory]     - 显示当前配置")
        print("  set <key> <value>    - 设置全局配置")
        sys.exit(1)
    
    manager = ConfigManager()
    command = sys.argv[1]
    
    if command == 'init':
        directory = sys.argv[2] if len(sys.argv) > 2 else '.'
        config_path = manager.create_project_config(directory)
        print(f"已创建项目配置文件: {config_path}")
        
    elif command == 'show':
        directory = sys.argv[2] if len(sys.argv) > 2 else '.'
        config = manager.load_config(directory)
        print(yaml.dump(config, default_flow_style=False, allow_unicode=True))
        
    elif command == 'set':
        if len(sys.argv) < 4:
            print("Usage: config_manager.py set <key> <value>")
            sys.exit(1)
        # 这里可以实现设置配置的逻辑
        print("设置配置功能待实现")
        
    else:
        print(f"未知命令: {command}")