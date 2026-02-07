# -*- coding: utf-8 -*-
"""
基质计算器数据模块
包含武器、属性、能量淤积点等数据定义
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

# 全部的基础属性
ALL_ATTRIBUTE_STATS = ['敏捷提升', '力量提升', '意志提升', '智识提升', '主能力提升']

# 全部的附加属性
ALL_SECONDARY_STATS = [
    '攻击提升', '生命提升', '物理伤害提升', '灼热伤害提升',
    '电磁伤害提升', '寒冷伤害提升', '自然伤害提升', '暴击率提升',
    '源石技艺提升', '终结技效率提升', '法术伤害提升', '治疗效率提升',
]

# 全部的技能属性
ALL_SKILL_STATS = [
    '强攻', '压制', '追袭', '粉碎', '昂扬', '巧技', '残暴',
    '附术', '医疗', '切骨', '迸发', '夜幕', '流转', '效益',
]

# 武器类型
WEAPON_TYPES = ['单手剑', '双手剑', '长柄武器', '手铳', '施术单元']


@dataclass
class WeaponStat:
    """武器属性"""
    attribute: Optional[str]  # 基础属性
    secondary: Optional[str]  # 附加属性
    skill: Optional[str]      # 技能属性


@dataclass
class WeaponPreset:
    """武器预设"""
    weapon_id: str
    weapon_name: str
    weapon_type: str
    rarity: int
    stats: WeaponStat


@dataclass
class EnergyAlluvium:
    """能量淤积点"""
    battle_id: str
    battle_name: str
    secondary_stats: List[str]
    skill_stats: List[str]


# 能量淤积点配置
ENERGY_ALLUVIUMS: Dict[str, EnergyAlluvium] = {
    '重度能量淤积点·枢纽区': EnergyAlluvium(
        battle_id='重度能量淤积点·枢纽区',
        battle_name='重度能量淤积点·枢纽区',
        secondary_stats=[
            '攻击提升', '灼热伤害提升', '电磁伤害提升', '寒冷伤害提升',
            '自然伤害提升', '源石技艺提升', '终结技效率提升', '法术伤害提升',
        ],
        skill_stats=['强攻', '压制', '追袭', '粉碎', '巧技', '迸发', '流转', '效益'],
    ),
    '重度能量淤积点·源石研究园': EnergyAlluvium(
        battle_id='重度能量淤积点·源石研究园',
        battle_name='重度能量淤积点·源石研究园',
        secondary_stats=[
            '攻击提升', '物理伤害提升', '电磁伤害提升', '寒冷伤害提升',
            '自然伤害提升', '暴击率提升', '终结技效率提升', '法术伤害提升',
        ],
        skill_stats=['压制', '追袭', '昂扬', '巧技', '附术', '医疗', '切骨', '效益'],
    ),
    '重度能量淤积点·矿脉源区': EnergyAlluvium(
        battle_id='重度能量淤积点·矿脉源区',
        battle_name='重度能量淤积点·矿脉源区',
        secondary_stats=[
            '生命提升', '物理伤害提升', '灼热伤害提升', '寒冷伤害提升',
            '自然伤害提升', '暴击率提升', '源石技艺提升', '治疗效率提升',
        ],
        skill_stats=['强攻', '压制', '巧技', '残暴', '附术', '迸发', '夜幕', '效益'],
    ),
    '重度能量淤积点·供能高地': EnergyAlluvium(
        battle_id='重度能量淤积点·供能高地',
        battle_name='重度能量淤积点·供能高地',
        secondary_stats=[
            '攻击提升', '生命提升', '物理伤害提升', '灼热伤害提升',
            '自然伤害提升', '暴击率提升', '源石技艺提升', '治疗效率提升',
        ],
        skill_stats=['追袭', '粉碎', '昂扬', '残暴', '附术', '医疗', '切骨', '流转'],
    ),
    '重度能量淤积点·武陵城': EnergyAlluvium(
        battle_id='重度能量淤积点·武陵城',
        battle_name='重度能量淤积点·武陵城',
        secondary_stats=[
            '攻击提升', '生命提升', '电磁伤害提升', '寒冷伤害提升',
            '暴击率提升', '终结技效率提升', '法术伤害提升', '治疗效率提升',
        ],
        skill_stats=['强攻', '粉碎', '残暴', '医疗', '切骨', '迸发', '夜幕', '流转'],
    ),
}
