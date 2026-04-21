# Copyright (c) Magnon Compute Corporation. All rights reserved.
import os


def mkdir_allow_exists(dirname):
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
