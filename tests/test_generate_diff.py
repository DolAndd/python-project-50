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


def test_gen_diff():
    bigfile1 = 'tests/fixtures/bigfileone.json'
    bigfile2 = 'tests/fixtures/bigfiletwo.json'
    with open('tests/fixtures/result2.txt', encoding='utf8') as f:
        result2 = f.read()
    assert generate_diff(bigfile1, bigfile2) == result2
