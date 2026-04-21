# Copyright (c) Magnon Compute Corporation. All rights reserved.
from test_support import prove_all
import os.path

prove_all(project=os.path.join("test", "src", "demo_missions.gpr"))
