# -*- coding: utf-8 -*-
"""
基质计算器核心逻辑
"""

from typing import List, Optional, Tuple
from dataclasses import dataclass
from itertools import combinations

from .data import (
    ALL_ATTRIBUTE_STATS,
    ENERGY_ALLUVIUMS,
    EnergyAlluvium,
)
from .weapons import WEAPONS


@dataclass
class EssenceStat:
    """基质属性需求"""
    is_custom: bool
    weapon_id: Optional[str]
    attribute: Optional[str]
    secondary: Optional[str]
    skill: Optional[str]


@dataclass
class BattleChoice:
    """战斗方案"""
    battle_id: str
    battle_name: str
    selected_attribute: List[str]
    selected_secondary: Optional[str]
    selected_skill: Optional[str]
    matched_indices: List[int]
    matched_weapon_ids: List[str]


def calculate_choices(required_stats: List[EssenceStat]) -> List[BattleChoice]:
    """
    计算所有可能的刷取方案
    """
    result: List[BattleChoice] = []

    for alluvium in ENERGY_ALLUVIUMS.values():
        # 枚举基础属性的3元组合
        for selected_attr in combinations(ALL_ATTRIBUTE_STATS, 3):
            selected_attribute = list(selected_attr)

            # 枚举附加属性
            for selected_secondary in alluvium.secondary_stats:
                choice = _create_choice_by_secondary(
                    alluvium, selected_attribute,
                    selected_secondary, required_stats
                )
                if choice and choice.matched_indices:
                    result.append(choice)

            # 枚举技能属性
            for selected_skill in alluvium.skill_stats:
                choice = _create_choice_by_skill(
                    alluvium, selected_attribute,
                    selected_skill, required_stats
                )
                if choice and choice.matched_indices:
                    result.append(choice)

    return result


def _create_choice_by_secondary(
    alluvium: EnergyAlluvium,
    selected_attribute: List[str],
    selected_secondary: str,
    required_stats: List[EssenceStat]
) -> Optional[BattleChoice]:
    """根据附加属性创建方案"""
    matched_indices: List[int] = []
    matched_weapon_ids: List[str] = []

    # 检查需求匹配
    for idx, stat in enumerate(required_stats):
        if _matches_secondary(stat, selected_attribute,
                              selected_secondary, alluvium.skill_stats):
            matched_indices.append(idx)

    # 检查武器匹配
    for weapon in WEAPONS.values():
        if _weapon_matches_secondary(weapon.stats, selected_attribute,
                                     selected_secondary, alluvium.skill_stats):
            matched_weapon_ids.append(weapon.weapon_id)

    return BattleChoice(
        battle_id=alluvium.battle_id,
        battle_name=alluvium.battle_name,
        selected_attribute=selected_attribute,
        selected_secondary=selected_secondary,
        selected_skill=None,
        matched_indices=matched_indices,
        matched_weapon_ids=matched_weapon_ids,
    )


def _create_choice_by_skill(
    alluvium: EnergyAlluvium,
    selected_attribute: List[str],
    selected_skill: str,
    required_stats: List[EssenceStat]
) -> Optional[BattleChoice]:
    """根据技能属性创建方案"""
    matched_indices: List[int] = []
    matched_weapon_ids: List[str] = []

    # 检查需求匹配
    for idx, stat in enumerate(required_stats):
        if _matches_skill(stat, selected_attribute,
                          alluvium.secondary_stats, selected_skill):
            matched_indices.append(idx)

    # 检查武器匹配
    for weapon in WEAPONS.values():
        if _weapon_matches_skill(weapon.stats, selected_attribute,
                                 alluvium.secondary_stats, selected_skill):
            matched_weapon_ids.append(weapon.weapon_id)

    return BattleChoice(
        battle_id=alluvium.battle_id,
        battle_name=alluvium.battle_name,
        selected_attribute=selected_attribute,
        selected_secondary=None,
        selected_skill=selected_skill,
        matched_indices=matched_indices,
        matched_weapon_ids=matched_weapon_ids,
    )


def _matches_secondary(
    stat: EssenceStat,
    selected_attribute: List[str],
    selected_secondary: str,
    skill_stats: List[str]
) -> bool:
    """检查需求是否匹配（按附加属性）"""
    if not stat.attribute or not stat.secondary or not stat.skill:
        return False
    return (
        stat.attribute in selected_attribute and
        stat.secondary == selected_secondary and
        stat.skill in skill_stats
    )


def _matches_skill(
    stat: EssenceStat,
    selected_attribute: List[str],
    secondary_stats: List[str],
    selected_skill: str
) -> bool:
    """检查需求是否匹配（按技能属性）"""
    if not stat.attribute or not stat.secondary or not stat.skill:
        return False
    return (
        stat.attribute in selected_attribute and
        stat.secondary in secondary_stats and
        stat.skill == selected_skill
    )


def _weapon_matches_secondary(
    stats, selected_attribute: List[str],
    selected_secondary: str, skill_stats: List[str]
) -> bool:
    """检查武器是否匹配（按附加属性）"""
    if not stats.attribute or not stats.secondary or not stats.skill:
        return False
    return (
        stats.attribute in selected_attribute and
        stats.secondary == selected_secondary and
        stats.skill in skill_stats
    )


def _weapon_matches_skill(
    stats, selected_attribute: List[str],
    secondary_stats: List[str], selected_skill: str
) -> bool:
    """检查武器是否匹配（按技能属性）"""
    if not stats.attribute or not stats.secondary or not stats.skill:
        return False
    return (
        stats.attribute in selected_attribute and
        stats.secondary in secondary_stats and
        stats.skill == selected_skill
    )


def get_best_choices(
    required_stats: List[EssenceStat],
    limit: int = 5
) -> List[BattleChoice]:
    """获取最佳方案"""
    choices = calculate_choices(required_stats)

    # 过滤并排序
    choices = [c for c in choices if c.matched_indices]
    choices.sort(key=lambda c: (
        -len(c.matched_indices),
        -len(c.matched_weapon_ids)
    ))

    return choices[:limit]


def find_weapon_by_name(name: str) -> Optional[Tuple[str, 'WeaponPreset']]:
    """根据武器名称查找武器"""
    from .weapons import WEAPONS
    for weapon_id, weapon in WEAPONS.items():
        if weapon.weapon_name == name:
            return (weapon_id, weapon)
    # 模糊匹配
    for weapon_id, weapon in WEAPONS.items():
        if name in weapon.weapon_name:
            return (weapon_id, weapon)
    return None


def find_weapons_by_stats(
    attribute: Optional[str] = None,
    secondary: Optional[str] = None,
    skill: Optional[str] = None
) -> List[Tuple[str, 'WeaponPreset']]:
    """根据属性反查武器"""
    from .weapons import WEAPONS
    results = []

    for weapon_id, weapon in WEAPONS.items():
        match = True
        if attribute and weapon.stats.attribute != attribute:
            match = False
        if secondary and weapon.stats.secondary != secondary:
            match = False
        if skill and weapon.stats.skill != skill:
            match = False

        if match:
            results.append((weapon_id, weapon))

    # 按稀有度降序排列
    results.sort(key=lambda x: -x[1].rarity)
    return results
