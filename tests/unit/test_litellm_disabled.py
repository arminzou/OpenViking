# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: Apache-2.0
"""Tests for temporary LiteLLM hard-disable behavior on the hotfix branch."""

import pytest

from openviking.models.vlm import VLMFactory, get_all_provider_names


def test_vlm_factory_rejects_litellm_provider():
    """VLMFactory should fail fast when LiteLLM is selected."""
    with pytest.raises(ValueError, match="temporarily disabled"):
        VLMFactory.create({"provider": "litellm", "model": "claude-3-7-sonnet"})


def test_vlm_registry_no_longer_exposes_litellm():
    """Provider registry should not advertise LiteLLM while disabled."""
    assert "litellm" not in get_all_provider_names()
