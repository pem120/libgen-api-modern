import pytest
from libgen.client import search_async
from libgen.errors import LibgenSearchError
from libgen.models import BookData


@pytest.mark.asyncio
async def test_search_success():
    """Tests a successful async search."""
    results = await search_async("python data science")
    assert isinstance(results, list)
    assert len(results) > 0
    book = results[0]
    assert isinstance(book, BookData)
    assert book.title is not None
    assert book.id is not None
    # Check if at least some download links were resolved
    assert any(b.download_links and b.download_links.get_link for b in results)


@pytest.mark.asyncio
async def test_search_no_results():
    """Tests an async search that returns no results."""
    # The test PASSES if a LibgenSearchError is raised within this block
    with pytest.raises(LibgenSearchError) as excinfo:
        await search_async("nonexistentbookxyz123abc")

    # assert "nonexistentbookxyz123abc" in str(excinfo.value)
    # assert "Failed to retrieve results from Libgen sites" in str(excinfo.value)
