# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import prove_all, TESTDIR
import os

os.environ["SPARKLIB_OBJECT_DIR"] = TESTDIR
prove_all(steps=2000, sparklib=True)
