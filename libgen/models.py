# Copyright (c) 2024-2025 Johnnie
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
#
# libgen/models.py
#
# This file is part of the libgen-api-modern library

from dataclasses import dataclass


@dataclass(frozen=True)
class DownloadLinks:
    get_link: str | None
    cloudflare_link: str | None
    ipfs_link: str | None
    pinata_link: str | None
    cover_link: str | None


@dataclass(frozen=True)
class BookData:
    id: str
    authors: tuple[str, ...]
    title: str
    publisher: str | None = None
    year: str | None = None
    pages: str | None = None
    language: str | None = None
    size: str | None = None
    extension: str | None = None
    isbn: str | None = None
    cover_url: str | None = None
    download_links: DownloadLinks | None = None
    mirror_url: str | None = None
