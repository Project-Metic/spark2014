# Copyright (c) Magnon Compute Corporation. All rights reserved.
from e3.os.process import Run

process = Run(["gnatprove"])
print(process.out)
