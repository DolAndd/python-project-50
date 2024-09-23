from gendiff.generate_diff.generate_diff import generate_diff


def test_gen_diff_json():
    one = 'tests/fixtures/one.json'
    two = 'tests/fixtures/two.json'
    with_links_path = 'tests/fixtures/result.txt'
    with open(with_links_path, encoding='utf8') as f:
        result = f.read()
    assert generate_diff(one, two) == result


def test_gen_diff_yaml():
    three = 'tests/fixtures/three.yaml'
    four = 'tests/fixtures/four.yaml'
    with open('tests/fixtures/result.txt', encoding='utf8') as f:
        result = f.read()
    assert generate_diff(three, four) == result


def test_gen_diff_big_yaml():
    bigfile1 = 'tests/fixtures/bigfile1.yaml'
    bigfile2 = 'tests/fixtures/bigfile2.yaml'
    with open('tests/fixtures/result2.txt', encoding='utf8') as f:
        result2 = f.read()
    assert generate_diff(bigfile1, bigfile2) == result2


def test_gen_diff_big_json():
    bigfile1 = 'tests/fixtures/bigfileone.json'
    bigfile2 = 'tests/fixtures/bigfiletwo.json'
    with open('tests/fixtures/result2.txt', encoding='utf8') as f:
        result2 = f.read()
    assert generate_diff(bigfile1, bigfile2) == result2


def test_gen_diff_plain():
    bigfile1 = 'tests/fixtures/bigfile1.yaml'
    bigfile2 = 'tests/fixtures/bigfile2.yaml'
    with open('tests/fixtures/plain_result.txt', encoding='utf8') as f:
        plain_result = f.read()
    assert generate_diff(bigfile1, bigfile2, 'plain') == plain_result
