# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyFeatomic(PythonPackage):
    """Computing representations for atomistic machine learning"""

    homepage = "https://docs.metatensor.org/featomic/latest/index.html"
    pypi = "featomic/featomic-0.6.3.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke")

    license("BSD-3-Clause", checked_by="RMeli")

    version("0.6.3", sha256="4692e681cf1fcff5daf138aeda0f44ce8c5b8e6c709511146acc1b3b6cf2d893")


    # pyproject.toml
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging", type="build")
    
    # pyproject.toml
    depends_on("py-metatensor-core@0.1.15:0.1")
    depends_on("py-metatensor-operations@0.3.0:0.3")
    depends_on("py-wigners")
   
    # featomic/CMakeLists.txt
    depends_on("cmake@3.22:", type="build")
    depends_on("rust")
