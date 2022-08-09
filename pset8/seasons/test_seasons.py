from seasons import convert


def test_convert():
    assert convert("qdsfqf") == False
    assert (
        convert("1987-04-01")
        == "Eighteen million, five hundred ninety-six thousand, one hundred sixty minutes"
    )
