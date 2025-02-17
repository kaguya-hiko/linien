# Copyright 2018-2022 Benjamin Wiegand <benjamin.wiegand@physik.hu-berlin.de>
# Copyright 2022 Bastian Leykauf <leykauf@physik.hu-berlin.de>
#
# This file is part of Linien and based on redpid.
#
# Linien is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linien is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linien.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import find_packages, setup

version = "0.7.0"

setup(
    name="linien-client",
    version=version,
    author="Benjamin Wiegand",
    author_email="highwaychile@posteo.de",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin.de",
    description="Client components of the Linien spectroscopy lock application.",
    long_description="Have a look at the [project repository](https://github.com/linien-org/linien) for installation instructions.",  # noqa: E501
    long_description_content_type="text/markdown",
    url="https://github.com/linien-org/linien/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fabric>=2.7.0",
        "numpy>=1.22",
        "patchwork>=1.0.1",
        "rpyc>=4.0,<5.0",
        "scipy>=1.4.1",
        f"linien-common=={version}",
    ],
)
