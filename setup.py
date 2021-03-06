#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def take_package_name(name):
    if name.startswith("-e"):
        return name[name.find("=")+1:name.rfind("-")]
    else:
        return name.strip()


def load_requires_from_file(file_path):
    with open(file_path) as fp:
        return [take_package_name(pkg_name) for pkg_name in fp.readlines()]


def load_links_from_file(file_path):
    res = []
    with open(file_path) as fp:
        for pkg_name in fp.readlines():
            if pkg_name.startswith("-e"):
                res.append(pkg_name.split(" ")[1])
    return res


setup(
    install_requires=load_requires_from_file("requirements.txt"),
    dependency_links=load_links_from_file("requirements.txt"),
)
