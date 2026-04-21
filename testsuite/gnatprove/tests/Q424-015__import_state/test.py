# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import prove_all, gprbuild

prove_all()
gprbuild(["-q", "-P", "test.gpr"])
