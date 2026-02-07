# -*- coding: utf-8 -*-
"""
武器数据库
"""

from typing import Dict
from .data import WeaponPreset, WeaponStat

# 武器预设数据库
WEAPONS: Dict[str, WeaponPreset] = {
    'wpn_claym_0003': WeaponPreset(
        weapon_id='wpn_claym_0003', weapon_name='工业零点一', weapon_type='双手剑', rarity=4,
        stats=WeaponStat(attribute='力量提升', secondary='攻击提升', skill='压制'),
    ),
    'wpn_funnel_0009': WeaponPreset(
        weapon_id='wpn_funnel_0009', weapon_name='遗忘', weapon_type='施术单元', rarity=6,
        stats=WeaponStat(attribute='智识提升', secondary='法术伤害提升', skill='夜幕'),
    ),
    'wpn_claym_0004': WeaponPreset(
        weapon_id='wpn_claym_0004', weapon_name='典范', weapon_type='双手剑', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='攻击提升', skill='压制'),
    ),
    'wpn_claym_0008': WeaponPreset(
        weapon_id='wpn_claym_0008', weapon_name='破碎君王', weapon_type='双手剑', rarity=6,
        stats=WeaponStat(attribute='力量提升', secondary='暴击率提升', skill='粉碎'),
    ),
    'wpn_claym_0006': WeaponPreset(
        weapon_id='wpn_claym_0006', weapon_name='昔日精品', weapon_type='双手剑', rarity=6,
        stats=WeaponStat(attribute='意志提升', secondary='生命提升', skill='效益'),
    ),
    'wpn_claym_0007': WeaponPreset(
        weapon_id='wpn_claym_0007', weapon_name='大雷斑', weapon_type='双手剑', rarity=6,
        stats=WeaponStat(attribute='力量提升', secondary='生命提升', skill='医疗'),
    ),
    'wpn_pistol_0006': WeaponPreset(
        weapon_id='wpn_pistol_0006', weapon_name='作品：众生', weapon_type='手铳', rarity=5,
        stats=WeaponStat(attribute='敏捷提升', secondary='法术伤害提升', skill='附术'),
    ),
    'wpn_claym_0009': WeaponPreset(
        weapon_id='wpn_claym_0009', weapon_name='淬火者', weapon_type='双手剑', rarity=4,
        stats=WeaponStat(attribute='意志提升', secondary='生命提升', skill='粉碎'),
    ),
    'wpn_funnel_0010': WeaponPreset(
        weapon_id='wpn_funnel_0010', weapon_name='骑士精神', weapon_type='施术单元', rarity=6,
        stats=WeaponStat(attribute='意志提升', secondary='生命提升', skill='医疗'),
    ),
    'wpn_claym_0010': WeaponPreset(
        weapon_id='wpn_claym_0010', weapon_name='达尔霍夫7', weapon_type='双手剑', rarity=3,
        stats=WeaponStat(attribute='主能力提升', secondary=None, skill='强攻'),
    ),
    'wpn_sword_0013': WeaponPreset(
        weapon_id='wpn_sword_0013', weapon_name='显赫声名', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='物理伤害提升', skill='残暴'),
    ),
    'wpn_claym_0011': WeaponPreset(
        weapon_id='wpn_claym_0011', weapon_name='探骊', weapon_type='双手剑', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='终结技效率提升', skill='迸发'),
    ),
    'wpn_claym_0012': WeaponPreset(
        weapon_id='wpn_claym_0012', weapon_name='终点之声', weapon_type='双手剑', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='生命提升', skill='医疗'),
    ),
    'wpn_lance_0008': WeaponPreset(
        weapon_id='wpn_lance_0008', weapon_name='天使杀手', weapon_type='长柄武器', rarity=4,
        stats=WeaponStat(attribute='意志提升', secondary='法术伤害提升', skill='压制'),
    ),
    'wpn_sword_0011': WeaponPreset(
        weapon_id='wpn_sword_0011', weapon_name='扶摇', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='暴击率提升', skill='夜幕'),
    ),
    'wpn_claym_0013': WeaponPreset(
        weapon_id='wpn_claym_0013', weapon_name='赫拉芬格', weapon_type='双手剑', rarity=6,
        stats=WeaponStat(attribute='力量提升', secondary='攻击提升', skill='迸发'),
    ),
    'wpn_funnel_0006': WeaponPreset(
        weapon_id='wpn_funnel_0006', weapon_name='作品：蚀迹', weapon_type='施术单元', rarity=6,
        stats=WeaponStat(attribute='意志提升', secondary='自然伤害提升', skill='压制'),
    ),
    'wpn_lance_0009': WeaponPreset(
        weapon_id='wpn_lance_0009', weapon_name='奥佩罗77', weapon_type='长柄武器', rarity=3,
        stats=WeaponStat(attribute='主能力提升', secondary=None, skill='强攻'),
    ),
    'wpn_sword_0010': WeaponPreset(
        weapon_id='wpn_sword_0010', weapon_name='黯色火炬', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='智识提升', secondary='灼热伤害提升', skill='附术'),
    ),
    'wpn_claym_0014': WeaponPreset(
        weapon_id='wpn_claym_0014', weapon_name='古渠', weapon_type='双手剑', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='源石技艺提升', skill='残暴'),
    ),
    'wpn_funnel_0003': WeaponPreset(
        weapon_id='wpn_funnel_0003', weapon_name='荧光雷羽', weapon_type='施术单元', rarity=4,
        stats=WeaponStat(attribute='意志提升', secondary='攻击提升', skill='压制'),
    ),
    'wpn_claym_0015': WeaponPreset(
        weapon_id='wpn_claym_0015', weapon_name='O.B.J.重荷', weapon_type='双手剑', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='生命提升', skill='效益'),
    ),
    'wpn_funnel_0001': WeaponPreset(
        weapon_id='wpn_funnel_0001', weapon_name='全自动骇新星', weapon_type='施术单元', rarity=4,
        stats=WeaponStat(attribute='智识提升', secondary='法术伤害提升', skill='昂扬'),
    ),
    'wpn_funnel_0002': WeaponPreset(
        weapon_id='wpn_funnel_0002', weapon_name='吉米尼12', weapon_type='施术单元', rarity=3,
        stats=WeaponStat(attribute='主能力提升', secondary=None, skill='强攻'),
    ),
    'wpn_sword_0007': WeaponPreset(
        weapon_id='wpn_sword_0007', weapon_name='坚城铸造者', weapon_type='单手剑', rarity=5,
        stats=WeaponStat(attribute='智识提升', secondary='终结技效率提升', skill='昂扬'),
    ),
    'wpn_funnel_0004': WeaponPreset(
        weapon_id='wpn_funnel_0004', weapon_name='迷失荒野', weapon_type='施术单元', rarity=5,
        stats=WeaponStat(attribute='智识提升', secondary='电磁伤害提升', skill='附术'),
    ),
    'wpn_sword_0018': WeaponPreset(
        weapon_id='wpn_sword_0018', weapon_name='十二问', weapon_type='单手剑', rarity=5,
        stats=WeaponStat(attribute='敏捷提升', secondary='攻击提升', skill='附术'),
    ),
    'wpn_funnel_0005': WeaponPreset(
        weapon_id='wpn_funnel_0005', weapon_name='悼亡诗', weapon_type='施术单元', rarity=5,
        stats=WeaponStat(attribute='智识提升', secondary='攻击提升', skill='夜幕'),
    ),
    'wpn_funnel_0007': WeaponPreset(
        weapon_id='wpn_funnel_0007', weapon_name='莫奈何', weapon_type='施术单元', rarity=5,
        stats=WeaponStat(attribute='意志提升', secondary='终结技效率提升', skill='昂扬'),
    ),
    'wpn_sword_0008': WeaponPreset(
        weapon_id='wpn_sword_0008', weapon_name='应急手段', weapon_type='单手剑', rarity=4,
        stats=WeaponStat(attribute='敏捷提升', secondary='物理伤害提升', skill='压制'),
    ),
    'wpn_sword_0020': WeaponPreset(
        weapon_id='wpn_sword_0020', weapon_name='逐鳞3.0', weapon_type='单手剑', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='寒冷伤害提升', skill='压制'),
    ),
    'wpn_funnel_0008': WeaponPreset(
        weapon_id='wpn_funnel_0008', weapon_name='爆破单元', weapon_type='施术单元', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='源石技艺提升', skill='迸发'),
    ),
    'wpn_funnel_0011': WeaponPreset(
        weapon_id='wpn_funnel_0011', weapon_name='使命必达', weapon_type='施术单元', rarity=6,
        stats=WeaponStat(attribute='意志提升', secondary='终结技效率提升', skill='追袭'),
    ),
    'wpn_funnel_0012': WeaponPreset(
        weapon_id='wpn_funnel_0012', weapon_name='布道自由', weapon_type='施术单元', rarity=5,
        stats=WeaponStat(attribute='意志提升', secondary='治疗效率提升', skill='医疗'),
    ),
    'wpn_lance_0006': WeaponPreset(
        weapon_id='wpn_lance_0006', weapon_name='向心之引', weapon_type='长柄武器', rarity=5,
        stats=WeaponStat(attribute='意志提升', secondary='电磁伤害提升', skill='压制'),
    ),
    'wpn_funnel_0013': WeaponPreset(
        weapon_id='wpn_funnel_0013', weapon_name='沧溟星梦', weapon_type='施术单元', rarity=6,
        stats=WeaponStat(attribute='智识提升', secondary='治疗效率提升', skill='附术'),
    ),
    'wpn_funnel_0014': WeaponPreset(
        weapon_id='wpn_funnel_0014', weapon_name='O.B.J.术识', weapon_type='施术单元', rarity=5,
        stats=WeaponStat(attribute='智识提升', secondary='源石技艺提升', skill='追袭'),
    ),
    'wpn_lance_0003': WeaponPreset(
        weapon_id='wpn_lance_0003', weapon_name='寻路者道标', weapon_type='长柄武器', rarity=4,
        stats=WeaponStat(attribute='敏捷提升', secondary='攻击提升', skill='昂扬'),
    ),
    'wpn_lance_0004': WeaponPreset(
        weapon_id='wpn_lance_0004', weapon_name='嵌合正义', weapon_type='长柄武器', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='终结技效率提升', skill='残暴'),
    ),
    'wpn_lance_0010': WeaponPreset(
        weapon_id='wpn_lance_0010', weapon_name='骁勇', weapon_type='长柄武器', rarity=6,
        stats=WeaponStat(attribute='敏捷提升', secondary='物理伤害提升', skill='巧技'),
    ),
    'wpn_lance_0011': WeaponPreset(
        weapon_id='wpn_lance_0011', weapon_name='J.E.T.', weapon_type='长柄武器', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='攻击提升', skill='压制'),
    ),
    'wpn_lance_0012': WeaponPreset(
        weapon_id='wpn_lance_0012', weapon_name='负山', weapon_type='长柄武器', rarity=6,
        stats=WeaponStat(attribute='敏捷提升', secondary='物理伤害提升', skill='效益'),
    ),
    'wpn_pistol_0010': WeaponPreset(
        weapon_id='wpn_pistol_0010', weapon_name='艺术暴君', weapon_type='手铳', rarity=6,
        stats=WeaponStat(attribute='智识提升', secondary='暴击率提升', skill='切骨'),
    ),
    'wpn_lance_0013': WeaponPreset(
        weapon_id='wpn_lance_0013', weapon_name='O.B.J.尖峰', weapon_type='长柄武器', rarity=5,
        stats=WeaponStat(attribute='意志提升', secondary='物理伤害提升', skill='附术'),
    ),
    'wpn_pistol_0001': WeaponPreset(
        weapon_id='wpn_pistol_0001', weapon_name='佩科5', weapon_type='手铳', rarity=3,
        stats=WeaponStat(attribute='主能力提升', secondary=None, skill='强攻'),
    ),
    'wpn_pistol_0002': WeaponPreset(
        weapon_id='wpn_pistol_0002', weapon_name='呼啸守卫', weapon_type='手铳', rarity=4,
        stats=WeaponStat(attribute='智识提升', secondary='攻击提升', skill='压制'),
    ),
    'wpn_pistol_0003': WeaponPreset(
        weapon_id='wpn_pistol_0003', weapon_name='长路', weapon_type='手铳', rarity=4,
        stats=WeaponStat(attribute='力量提升', secondary='法术伤害提升', skill='追袭'),
    ),
    'wpn_sword_0014': WeaponPreset(
        weapon_id='wpn_sword_0014', weapon_name='白夜新星', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='源石技艺提升', skill='附术'),
    ),
    'wpn_pistol_0004': WeaponPreset(
        weapon_id='wpn_pistol_0004', weapon_name='理性告别', weapon_type='手铳', rarity=5,
        stats=WeaponStat(attribute='力量提升', secondary='灼热伤害提升', skill='追袭'),
    ),
    'wpn_pistol_0005': WeaponPreset(
        weapon_id='wpn_pistol_0005', weapon_name='领航者', weapon_type='手铳', rarity=6,
        stats=WeaponStat(attribute='智识提升', secondary='寒冷伤害提升', skill='附术'),
    ),
    'wpn_pistol_0008': WeaponPreset(
        weapon_id='wpn_pistol_0008', weapon_name='楔子', weapon_type='手铳', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='暴击率提升', skill='附术'),
    ),
    'wpn_sword_0006': WeaponPreset(
        weapon_id='wpn_sword_0006', weapon_name='熔铸火焰', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='智识提升', secondary='攻击提升', skill='夜幕'),
    ),
    'wpn_pistol_0009': WeaponPreset(
        weapon_id='wpn_pistol_0009', weapon_name='同类相食', weapon_type='手铳', rarity=6,
        stats=WeaponStat(attribute='主能力提升', secondary='法术伤害提升', skill='附术'),
    ),
    'wpn_sword_0016': WeaponPreset(
        weapon_id='wpn_sword_0016', weapon_name='不知归', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='意志提升', secondary='攻击提升', skill='流转'),
    ),
    'wpn_pistol_0012': WeaponPreset(
        weapon_id='wpn_pistol_0012', weapon_name='O.B.J.迅极', weapon_type='手铳', rarity=5,
        stats=WeaponStat(attribute='敏捷提升', secondary='终结技效率提升', skill='迸发'),
    ),
    'wpn_sword_0003': WeaponPreset(
        weapon_id='wpn_sword_0003', weapon_name='塔尔11', weapon_type='单手剑', rarity=3,
        stats=WeaponStat(attribute='主能力提升', secondary=None, skill='强攻'),
    ),
    'wpn_sword_0005': WeaponPreset(
        weapon_id='wpn_sword_0005', weapon_name='钢铁余音', weapon_type='单手剑', rarity=5,
        stats=WeaponStat(attribute='敏捷提升', secondary='物理伤害提升', skill='巧技'),
    ),
    'wpn_sword_0009': WeaponPreset(
        weapon_id='wpn_sword_0009', weapon_name='浪潮', weapon_type='单手剑', rarity=4,
        stats=WeaponStat(attribute='智识提升', secondary='攻击提升', skill='追袭'),
    ),
    'wpn_sword_0012': WeaponPreset(
        weapon_id='wpn_sword_0012', weapon_name='热熔切割器', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='意志提升', secondary='攻击提升', skill='流转'),
    ),
    'wpn_sword_0015': WeaponPreset(
        weapon_id='wpn_sword_0015', weapon_name='仰止', weapon_type='单手剑', rarity=5,
        stats=WeaponStat(attribute='敏捷提升', secondary='物理伤害提升', skill='夜幕'),
    ),
    'wpn_sword_0019': WeaponPreset(
        weapon_id='wpn_sword_0019', weapon_name='O.B.J.轻芒', weapon_type='单手剑', rarity=5,
        stats=WeaponStat(attribute='敏捷提升', secondary='攻击提升', skill='流转'),
    ),
    'wpn_sword_0021': WeaponPreset(
        weapon_id='wpn_sword_0021', weapon_name='宏愿', weapon_type='单手剑', rarity=6,
        stats=WeaponStat(attribute='敏捷提升', secondary='攻击提升', skill='附术'),
    ),
}
