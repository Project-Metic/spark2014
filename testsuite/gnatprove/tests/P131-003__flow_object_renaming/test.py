# Copyright (c) Magnon Compute Corporation. All rights reserved.
from subprocess import call

call(["gcc", "-c", "-gnatwm", "-gnatd.F", "p.adb"])
