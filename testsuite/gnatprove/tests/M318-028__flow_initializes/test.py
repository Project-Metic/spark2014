# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import do_flow
from glob import glob

do_flow(opt=sorted(glob("*.adb")))
