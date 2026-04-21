# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read-time restore helpers for skill privacy placeholders."""

from openviking.privacy.skill_placeholder import build_placeholder


_SKILL_PREFIX = "viking://agent/skills/"
_SKILL_SUFFIX = "/SKILL.md"


def get_skill_name_from_uri(uri: str) -> str | None:
    if not uri.startswith(_SKILL_PREFIX) or not uri.endswith(_SKILL_SUFFIX):
        return None
    middle = uri[len(_SKILL_PREFIX) : -len(_SKILL_SUFFIX)]
    if not middle or "/" in middle:
        return None
    return middle


def restore_skill_content(content: str, skill_name: str, values: dict[str, str]) -> str:
    restored = content
    for field_name, raw_value in values.items():
        restored = restored.replace(build_placeholder(skill_name, field_name), str(raw_value))
    return restored
