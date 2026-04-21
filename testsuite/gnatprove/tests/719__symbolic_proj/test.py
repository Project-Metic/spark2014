# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import prove_all
import os

os.symlink("mytest.gpr", "link.gpr")
prove_all(project="link.gpr")
