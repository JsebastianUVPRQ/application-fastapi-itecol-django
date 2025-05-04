from unittest.mock import AsyncMock
import pytest

@pytest.mark.asyncio
async def test_classroom_caching(mocker):
    mock_redis = AsyncMock()
    mocker.patch("services.classroom_service.get_redis", return_value=mock_redis)
    
    # Test cache miss
    classroom = await get_classroom_with_cache(db, 1)
    assert mock_redis.setex.called
    
    # Test cache hit
    mock_redis.get.return_value = json.dumps({"id": 1, "name": "Test"})
    cached_classroom = await get_classroom_with_cache(db, 1)
    assert cached_classroom.name == "Test"