# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RMagrittr(RPackage):
    """Provides a mechanism for chaining commands with a new forward-pipe
    operator, %>%. This operator will forward a value, or the result of an
    expression, into the next function call/expression. There is flexible
    support for the type of right-hand side expressions. For more information,
    see package vignette."""

    homepage = "https://cran.r-project.org/web/packages/magrittr/index.html"
    url      = "https://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/magrittr"

    version('1.5', 'e74ab7329f2b9833f0c3c1216f86d65a')
