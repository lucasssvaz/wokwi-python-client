# SPDX-FileCopyrightText: 2025-present CodeMagic LTD
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel, Field


class UploadParams(BaseModel):
    name: str
    binary: str  # base64


class TextUploadParams(BaseModel):
    name: str
    text: str


class SimulationParams(BaseModel):
    firmware: str
    elf: str
    pause: bool = False
    chips: list[str] = Field(default_factory=list)
