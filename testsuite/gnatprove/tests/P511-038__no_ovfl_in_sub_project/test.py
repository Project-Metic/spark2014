# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import prove_all, gprbuild
from subprocess import call

prove_all(opt=["--report=fail"])
gprbuild(["-q", "-P", "test.gpr"])
call(["./check"])
