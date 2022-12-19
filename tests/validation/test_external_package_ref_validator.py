#  Copyright (c) 2022 spdx contributors
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import List

import pytest

from src.model.package import ExternalPackageRef, ExternalPackageRefCategory
from src.validation.external_package_ref_validator import validate_external_package_ref
from src.validation.validation_message import ValidationMessage, ValidationContext, SpdxElementType
from tests.valid_defaults import get_external_package_ref


def test_valid_external_package_ref():

    external_package_ref = ExternalPackageRef(ExternalPackageRefCategory.OTHER, "swh",
                                              "swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2", "comment")
    validation_messages: List[ValidationMessage] = validate_external_package_ref(external_package_ref, "parent_id")

    assert validation_messages == []


@pytest.mark.parametrize("external_package_ref, expected_message",
                         [(get_external_package_ref(),
                           "TBD"),
                          ])
@pytest.mark.skip("add tests once external package ref validation is implemented: https://github.com/spdx/tools-python/issues/373")
def test_invalid_external_package_ref(external_package_ref, expected_message):
    parent_id = "SPDXRef-Package"
    validation_messages: List[ValidationMessage] = validate_external_package_ref(external_package_ref, parent_id)

    expected = ValidationMessage(expected_message,
                                 ValidationContext(parent_id=parent_id,
                                                   element_type=SpdxElementType.EXTERNAL_PACKAGE_REF,
                                                   full_element=external_package_ref))

    assert validation_messages == [expected]