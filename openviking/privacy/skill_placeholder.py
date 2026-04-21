# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Placeholder helpers for skill privacy values."""


def build_placeholder(skill_name: str, field_name: str) -> str:
    return f"{{{{ov_privacy:skill:{skill_name}:{field_name}}}}}"


def placeholderize_skill_content(
    content: str, skill_name: str, values: dict[str, str]
) -> str:
    sanitized = content
    replacements = sorted(values.items(), key=lambda item: len(str(item[1])), reverse=True)
    for field_name, raw_value in replacements:
        if not raw_value:
            continue
        sanitized = sanitized.replace(str(raw_value), build_placeholder(skill_name, field_name))
    return sanitized
