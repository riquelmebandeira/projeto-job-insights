from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    output = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    expected = {'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'}
    assert output[0] == expected
