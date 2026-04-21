# Copyright (c) Magnon Compute Corporation. All rights reserved.
from subprocess import call
from test_support import gprbuild

gprbuild(["-q", "-U", "-P", "test.gpr"])
gprbuild(["-q", "-P", "test.gpr"])
call(["./test_lemmas"])
