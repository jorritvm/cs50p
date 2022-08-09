from twttr import shorten


def test_shorten():
    assert shorten("hallo") == "hll"
    assert shorten("bold") == "bld"
    assert shorten("bAld") == "bld"
    assert shorten("bAld1") == "bld1"
    assert shorten("bAld.") == "bld."
