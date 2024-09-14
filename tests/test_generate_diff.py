from gendiff.generate_diff.generate_diff import gen_diff


def test_gen_diff():
    one = 'tests/fixtures/one.json'
    two = 'tests/fixtures/two.json'
    with_links_path = 'tests/fixtures/result.txt'
    with open(with_links_path, encoding='utf8') as f:
        result = f.read()
    assert gen_diff(one, two) == result
