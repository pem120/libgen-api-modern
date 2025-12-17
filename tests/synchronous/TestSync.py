import pytest
from libgen.client import search_sync
from libgen.errors import LibgenSearchError
from libgen.models import BookData


def test_search_success():
    """Tests a successful sync search."""
    results = search_sync(" Principia Mathematica")
    assert isinstance(results, list)
    assert len(results) > 0
    book = results[0]
    assert isinstance(book, BookData)
    assert "principia" in book.title.lower()
    assert any(b.download_links and b.download_links.get_link for b in results)


def test_search_no_results():
    """Tests a sync search that returns no results."""
    with pytest.raises(LibgenSearchError) as excinfo:
        results = search_sync("nonexistentbookxyz123abc")

    # assert "nonexistentbookxyz123abc" in str(excinfo.value)
    # assert "Failed to retrieve results from Libgen sites" in str(excinfo.value)
