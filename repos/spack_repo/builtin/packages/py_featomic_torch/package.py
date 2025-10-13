# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyFeatomicTorch(PythonPackage):
    """Computing representations for atomistic machine learning """

    homepage = "https://docs.metatensor.org/featomic/latest/index.html"
    pypi = "featomic_torch/featomic_torch-0.7.1.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke")

    license("BSD3-Clause", checked_by="RMeli")

    version("0.7.1", sha256="b4e5871972812922f0862d2ac2cfc5e7bec791db7de8921ae88f62be68ba5699")
    version("0.7.0", sha256="e2207214f23472eccd03d374f5660d2290b7d272796caf68c54bd18eda6cccdd")

    # pyproject.toml
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging", type="build")

    # setup.py
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-metatensor-operations", type=("build", "run"))
    depends_on("py-metatensor-torch@0.7.6:0.7", type=("build", "run"), when="@0.7.0:")
    depends_on("py-metatensor-torch@0.8.0:0.8", type=("build", "run"), when="@0.7.1:")
    depends_on("py-metatomic-torch@0.1.1:0.1", type=("build", "run"), when="@0.7.0:")
    depends_on("py-metatomic-torch@0.1.4:0.1", type=("build", "run"), when="@0.7.1:")
    depends_on("py-featomic@0.6.3:0.6", type=("build", "run"))

    # CMakeLists.txt
    depends_on("cmake@3.22:", type="build")
    depends_on("rust")
