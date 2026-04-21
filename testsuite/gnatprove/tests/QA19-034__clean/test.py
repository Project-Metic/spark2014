# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import cat, clean
import os.path

clean()
cat(os.path.join("obj1", "dummy.txt"))
