# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import prove_all

prove_all(opt=["--limit-subp=p.ads:3"])
prove_all(opt=["--limit-subp=p.ads:4"])
