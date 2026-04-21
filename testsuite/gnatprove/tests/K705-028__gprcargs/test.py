# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import gnatprove

gnatprove(opt=["-P", "test.gpr", "--mode=check", "-q", "-cargs", "-gnat2012"])
