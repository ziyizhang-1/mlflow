# Copyright 2018 Databricks, Inc.
import re


VERSION = "1.25.2.WiE"


def is_release_version():
    return bool(re.match(r"^\d+\.\d+\.\d+\.WiE$", VERSION))