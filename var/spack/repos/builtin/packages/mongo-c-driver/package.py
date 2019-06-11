# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class MongoCDriver(CMakePackage):
    """A Cross Platform MongoDB Client Library for C."""

    homepage = "http://mongoc.org/"
    url      = "https://github.com/mongodb/mongo-c-driver/releases/download/1.14.0/mongo-c-driver-1.14.0.tar.gz"

    maintainers = ['andreanegri']

    version('1.14.0', sha256='ebe9694f7fa6477e594f19507877bbaa0b72747682541cf0cf9a6c29187e97e8')
    version('1.10.0', sha256='65bec96b37333046679252d607a6bde7629854356f9a314666392a1d809abf12')
   
    #TODO: manage dependencies (openssl, snappy, zlib) 
    #depends_on('openssl')

    #force to use vendored libbson
    def cmake_args(self):
        args = [
            '-DENABLE_AUTOMATIC_INIT_AND_CLEANUP=OFF',
            '-DENABLE_BSON=ON',
        ]
        return args
