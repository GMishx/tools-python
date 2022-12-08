from unittest import mock

import pytest

from src.model.document import Document


@mock.patch('src.model.document.CreationInfo', autospec=True)
@mock.patch('src.model.package.Package', autospec=True)
@mock.patch('src.model.file.File', autospec=True)
@mock.patch('src.model.snippet.Snippet', autospec=True)
@mock.patch('src.model.annotation.Annotation', autospec=True)
@mock.patch('src.model.relationship.Relationship', autospec=True)
@mock.patch('src.model.extracted_licensing_info.ExtractedLicensingInfo', autospec=True)
def test_correct_initialization(creation_info, package, file, snippet, annotation, relationship,
                                extracted_lic):
    document = Document(creation_info, [package, package], [file, file], [snippet, snippet], [annotation, annotation],
                        [relationship, relationship], [extracted_lic, extracted_lic])
    assert document.creation_info == creation_info
    assert document.packages == [package, package]
    assert document.files == [file, file]
    assert document.snippets == [snippet, snippet]
    assert document.annotations == [annotation, annotation]
    assert document.relationships == [relationship, relationship]
    assert document.extracted_licensing_info == [extracted_lic, extracted_lic]


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_correct_initialization_with_default_values(creation_info):
    document = Document(creation_info)
    assert document.creation_info == creation_info
    assert document.packages == []
    assert document.files == []
    assert document.snippets == []
    assert document.annotations == []
    assert document.relationships == []
    assert document.extracted_licensing_info == []


def test_wrong_type_in_creation_info():
    with pytest.raises(TypeError):
        Document("string")


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_wrong_type_in_packages(creation_info):
    with pytest.raises(TypeError):
        Document(creation_info, packages=["string"])


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_wrong_type_in_files(creation_info):
    with pytest.raises(TypeError):
        Document(creation_info, files={})


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_wrong_type_in_snippets(creation_info):
    with pytest.raises(TypeError):
        Document(creation_info, snippets=())


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_wrong_type_in_annotations(creation_info):
    with pytest.raises(TypeError):
        Document(creation_info, annotations=["string"])


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_wrong_type_in_relationships(creation_info):
    with pytest.raises(TypeError):
        Document(creation_info, relationships="string")


@mock.patch('src.model.document.CreationInfo', autospec=True)
def test_wrong_type_in_extracted_licensing_info(creation_info):
    with pytest.raises(TypeError):
        Document(creation_info, extracted_licensing_info=42)