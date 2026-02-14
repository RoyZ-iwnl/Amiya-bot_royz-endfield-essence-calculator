# -*- coding: utf-8 -*-
"""
终末地基质计算器 AmiyaBot 插件
支持武器名称查询刷取方案和属性反查武器
"""

import os
import re
from typing import Optional

from core import Message, Chain, AmiyaBotPluginInstance

curr_dir = os.path.dirname(__file__)

# HTML模板路径
RESULT_TEMPLATE_PATH = os.path.join(curr_dir, 'template', 'result.html')

from .data import (
    ALL_ATTRIBUTE_STATS,
    ALL_SECONDARY_STATS,
    ALL_SKILL_STATS,
)
from .weapons import WEAPONS
from .calculator import (
    EssenceStat,
    get_best_choices,
    find_weapon_by_name,
    find_weapons_by_stats,
)


# 插件实例
bot = AmiyaBotPluginInstance(
    name='终末地基质计算器',
    version='1.1',
    plugin_id='royz-endfield-essence-calculator',
    plugin_type='',
    description='终末地基质刷取方案计算器',
    document=f'{curr_dir}/README.md',
)


def parse_attribute(text: str) -> Optional[str]:
    """解析基础属性关键词"""
    mapping = {
        '敏捷': '敏捷提升', '力量': '力量提升',
        '意志': '意志提升', '智识': '智识提升',
        '主能力': '主能力提升',
    }
    for key, value in mapping.items():
        if key in text:
            return value
    return None


def parse_secondary(text: str) -> Optional[str]:
    """解析附加属性关键词"""
    mapping = {
        '攻击': '攻击提升', '生命': '生命提升',
        '物理伤害': '物理伤害提升', '灼热伤害': '灼热伤害提升',
        '电磁伤害': '电磁伤害提升', '寒冷伤害': '寒冷伤害提升',
        '自然伤害': '自然伤害提升', '暴击率': '暴击率提升',
        '源石技艺': '源石技艺提升', '终结技效率': '终结技效率提升',
        '法术伤害': '法术伤害提升', '治疗效率': '治疗效率提升',
    }
    for key, value in mapping.items():
        if key in text:
            return value
    return None


def parse_skill(text: str) -> Optional[str]:
    """解析技能属性关键词"""
    for skill in ALL_SKILL_STATS:
        if skill in text:
            return skill
    return None


@bot.on_message(keywords=['基质武器'], level=5)
async def weapon_query(data: Message):
    """武器查询命令"""
    text = data.text.replace('兔兔基质武器', '').strip()

    if not text:
        return Chain(data).text(
            '【兔兔基质武器查询】\n'
            '用法：兔兔基质武器+武器名\n'
            '示例：兔兔基质武器 典范\n'
            '多武器查询：兔兔基质武器 熔铸火焰 热熔切割器'
        )

    # 解析多个武器名称(用空格或逗号分隔)
    weapon_names = re.split(r'[,，\s]+', text)
    weapon_names = [name.strip() for name in weapon_names if name.strip()]

    if len(weapon_names) == 1:
        # 单武器查询
        weapon_result = find_weapon_by_name(weapon_names[0])
        if weapon_result:
            return await handle_weapon_query(data, weapon_result)
        return Chain(data).text(f'未找到武器【{weapon_names[0]}】')

    # 多武器查询
    return await handle_multi_weapon_query(data, weapon_names)


@bot.on_message(keywords=['基质'], level=5)
async def essence_calculator(data: Message):
    """基质计算器主命令 - 属性反查"""
    text = data.text.replace('兔兔基质', '').strip()

    if not text:
        return Chain(data).text(
            '【终末地基质计算器】\n'
            '用法：\n'
            '1. 兔兔基质武器+武器名 - 查询武器刷取方案\n'
            '2. 兔兔基质+属性 - 反查适合的武器\n'
            '示例：兔兔基质武器 典范\n'
            '示例：兔兔基质 智识 攻击 夜幕\n'
            '多武器查询：兔兔基质武器 熔铸火焰 热熔切割器'
        )

    # 属性反查
    return await handle_stat_query(data, text)


async def handle_weapon_query(data: Message, weapon_result):
    """处理武器查询"""
    weapon_id, weapon = weapon_result
    stats = weapon.stats

    # 创建需求
    required_stat = EssenceStat(
        is_custom=False,
        weapon_id=weapon_id,
        attribute=stats.attribute,
        secondary=stats.secondary,
        skill=stats.skill,
    )

    # 计算方案
    choices = get_best_choices([required_stat], limit=5)

    if not choices:
        return Chain(data).text(
            f'未找到适合【{weapon.weapon_name}】的刷取方案'
        )

    # 构建结果
    render_data = {
        'title': f'【{weapon.weapon_name}】刷取方案',
        'weapon_id': weapon_id,
        'weapon_name': weapon.weapon_name,
        'weapon_type': weapon.weapon_type,
        'rarity': weapon.rarity,
        'rarity_class': f'rarity-{weapon.rarity}',  # 添加稀有度CSS类
        'attribute': stats.attribute or '-',
        'secondary': stats.secondary or '-',
        'skill': stats.skill or '-',
        'choices': [],
    }

    for i, choice in enumerate(choices):
        # 获取匹配的武器详细信息,排除用户查询的武器
        matched_weapons = []
        for wid in choice.matched_weapon_ids:
            if wid in WEAPONS and wid != weapon_id:  # 排除用户查询的武器
                w = WEAPONS[wid]
                matched_weapons.append({
                    'id': wid,
                    'name': w.weapon_name,
                    'type': w.weapon_type,
                    'rarity': w.rarity,
                    'attribute': w.stats.attribute or '-',
                    'secondary': w.stats.secondary or '-',
                    'skill': w.stats.skill or '-',
                })

        choice_data = {
            'index': i + 1,
            'battle_name': choice.battle_name,
            'attributes': '、'.join(choice.selected_attribute),
            'secondary': choice.selected_secondary or '-',
            'skill': choice.selected_skill or '-',
            'matched_count': len(choice.matched_weapon_ids) - 1,  # 减去用户查询的武器
            'matched_weapons': matched_weapons,
        }
        render_data['choices'].append(choice_data)

    # 使用HTML模板渲染
    return Chain(data).html(
        RESULT_TEMPLATE_PATH,
        render_data,
        width=600,
        height=1,
    )


async def handle_multi_weapon_query(data: Message, weapon_names: list):
    """处理多武器查询"""
    # 查找所有武器
    weapons_found = []
    weapons_not_found = []

    for name in weapon_names:
        weapon_result = find_weapon_by_name(name)
        if weapon_result:
            weapons_found.append(weapon_result)
        else:
            weapons_not_found.append(name)

    if not weapons_found:
        return Chain(data).text(f'未找到任何武器: {", ".join(weapons_not_found)}')

    if weapons_not_found:
        return Chain(data).text(
            f'部分武器未找到: {", ".join(weapons_not_found)}\n'
            f'已找到: {", ".join([w[1].weapon_name for w in weapons_found])}'
        )

    # 创建所有武器的需求
    required_stats = []
    for weapon_id, weapon in weapons_found:
        stats = weapon.stats
        required_stat = EssenceStat(
            is_custom=False,
            weapon_id=weapon_id,
            attribute=stats.attribute,
            secondary=stats.secondary,
            skill=stats.skill,
        )
        required_stats.append(required_stat)

    # 计算能同时刷取所有武器的方案
    choices = get_best_choices(required_stats, limit=5)

    # 过滤出能同时刷取所有武器的方案
    weapon_ids = [w[0] for w in weapons_found]
    simultaneous_choices = [
        c for c in choices
        if all(wid in c.matched_weapon_ids for wid in weapon_ids)
    ]

    if simultaneous_choices:
        # 有同时刷取方案
        return await render_multi_weapon_result(
            data, weapons_found, simultaneous_choices, is_simultaneous=True
        )
    else:
        # 没有同时刷取方案,分别给出每个武器的方案
        return await render_separate_weapon_results(data, weapons_found)


async def render_multi_weapon_result(
    data: Message,
    weapons_found: list,
    choices: list,
    is_simultaneous: bool
):
    """渲染多武器查询结果"""
    weapon_ids = [w[0] for w in weapons_found]

    # 构建结果
    weapon_names = [w[1].weapon_name for w in weapons_found]
    title = f'【{" + ".join(weapon_names)}】同时刷取方案' if is_simultaneous else f'【{" + ".join(weapon_names)}】刷取方案'

    render_data = {
        'title': title,
        'is_multi_weapon': True,
        'query_weapons': [
            {
                'id': wid,
                'name': w.weapon_name,
                'type': w.weapon_type,
                'rarity': w.rarity,
                'rarity_class': f'rarity-{w.rarity}',
                'attribute': w.stats.attribute or '-',
                'secondary': w.stats.secondary or '-',
                'skill': w.stats.skill or '-',
            }
            for wid, w in weapons_found
        ],
        'choices': [],
    }

    for i, choice in enumerate(choices):
        # 获取匹配的武器详细信息,排除用户查询的武器
        matched_weapons = []
        for wid in choice.matched_weapon_ids:
            if wid in WEAPONS and wid not in weapon_ids:
                w = WEAPONS[wid]
                matched_weapons.append({
                    'id': wid,
                    'name': w.weapon_name,
                    'type': w.weapon_type,
                    'rarity': w.rarity,
                    'attribute': w.stats.attribute or '-',
                    'secondary': w.stats.secondary or '-',
                    'skill': w.stats.skill or '-',
                })

        choice_data = {
            'index': i + 1,
            'battle_name': choice.battle_name,
            'attributes': '、'.join(choice.selected_attribute),
            'secondary': choice.selected_secondary or '-',
            'skill': choice.selected_skill or '-',
            'matched_count': len(choice.matched_weapon_ids) - len(weapon_ids),
            'matched_weapons': matched_weapons,
        }
        render_data['choices'].append(choice_data)

    # 使用HTML模板渲染
    return Chain(data).html(
        RESULT_TEMPLATE_PATH,
        render_data,
        width=600,
        height=1,
    )


async def render_separate_weapon_results(data: Message, weapons_found: list):
    """渲染分开的武器方案"""
    weapon_names = [w[1].weapon_name for w in weapons_found]

    # 为每个武器计算方案
    all_weapon_choices = []
    for weapon_id, weapon in weapons_found:
        stats = weapon.stats
        required_stat = EssenceStat(
            is_custom=False,
            weapon_id=weapon_id,
            attribute=stats.attribute,
            secondary=stats.secondary,
            skill=stats.skill,
        )
        choices = get_best_choices([required_stat], limit=3)
        all_weapon_choices.append({
            'weapon_id': weapon_id,
            'weapon': weapon,
            'choices': choices,
        })

    # 构建结果
    render_data = {
        'title': f'【{" + ".join(weapon_names)}】分开刷取方案',
        'is_separate': True,
        'separate_weapons': [],
    }

    for item in all_weapon_choices:
        weapon_id = item['weapon_id']
        weapon = item['weapon']
        choices = item['choices']

        weapon_data = {
            'id': weapon_id,
            'name': weapon.weapon_name,
            'type': weapon.weapon_type,
            'rarity': weapon.rarity,
            'rarity_class': f'rarity-{weapon.rarity}',
            'attribute': weapon.stats.attribute or '-',
            'secondary': weapon.stats.secondary or '-',
            'skill': weapon.stats.skill or '-',
            'choices': [],
        }

        for i, choice in enumerate(choices):
            # 获取匹配的武器详细信息,排除用户查询的武器
            matched_weapons = []
            for wid in choice.matched_weapon_ids:
                if wid in WEAPONS and wid != weapon_id:
                    w = WEAPONS[wid]
                    matched_weapons.append({
                        'id': wid,
                        'name': w.weapon_name,
                        'type': w.weapon_type,
                        'rarity': w.rarity,
                        'attribute': w.stats.attribute or '-',
                        'secondary': w.stats.secondary or '-',
                        'skill': w.stats.skill or '-',
                    })

            choice_data = {
                'index': i + 1,
                'battle_name': choice.battle_name,
                'attributes': '、'.join(choice.selected_attribute),
                'secondary': choice.selected_secondary or '-',
                'skill': choice.selected_skill or '-',
                'matched_count': len(choice.matched_weapon_ids) - 1,
                'matched_weapons': matched_weapons,
            }
            weapon_data['choices'].append(choice_data)

        render_data['separate_weapons'].append(weapon_data)

    # 使用HTML模板渲染
    return Chain(data).html(
        RESULT_TEMPLATE_PATH,
        render_data,
        width=600,
        height=1,
    )


async def handle_stat_query(data: Message, text: str):
    """处理属性反查"""
    attribute = parse_attribute(text)
    secondary = parse_secondary(text)
    skill = parse_skill(text)

    if not attribute and not secondary and not skill:
        return Chain(data).text(
            '【终末地基质计算器】\n'
            '用法：\n'
            '1. 兔兔基质武器+武器名 - 查询武器刷取方案\n'
            '2. 兔兔基质+属性 - 反查适合的武器\n'
            '示例：兔兔基质武器 典范\n'
            '示例：兔兔基质 智识 攻击 夜幕'
        )

    # 查找匹配的武器
    weapons = find_weapons_by_stats(attribute, secondary, skill)

    if not weapons:
        return Chain(data).text('未找到匹配的武器')

    # 构建查询条件描述
    conditions = []
    if attribute:
        conditions.append(f'基础:{attribute}')
    if secondary:
        conditions.append(f'附加:{secondary}')
    if skill:
        conditions.append(f'技能:{skill}')

    # 构建结果
    render_data = {
        'title': '属性反查结果',
        'conditions': ' | '.join(conditions),
        'weapons': [],
    }

    for weapon_id, weapon in weapons[:10]:
        weapon_data = {
            'id': weapon_id,
            'name': weapon.weapon_name,
            'type': weapon.weapon_type,
            'rarity': weapon.rarity,
            'attribute': weapon.stats.attribute or '-',
            'secondary': weapon.stats.secondary or '-',
            'skill': weapon.stats.skill or '-',
        }
        render_data['weapons'].append(weapon_data)

    # 使用HTML模板渲染
    return Chain(data).html(
        RESULT_TEMPLATE_PATH,
        render_data,
        width=600,
        height=1,
    )
