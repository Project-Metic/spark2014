# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import gcc
from test_support import prove_all

gcc("test.adb")
prove_all()
