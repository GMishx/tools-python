# Copyright (c) 2023 spdx contributors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TextIO

from spdx3.model.bundle import Bundle
from spdx3.writer.console.console import write_value
from spdx3.writer.console.spdx_collection_writer import write_collection


def write_bundle(bundle: Bundle, text_output: TextIO, heading: bool = True):
    if heading:
        text_output.write("## Bundle\n")
    write_collection(bundle, text_output)
    write_value("context", bundle.context, text_output)