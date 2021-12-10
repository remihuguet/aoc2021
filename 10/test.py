import scoring
import pytest

input_file = "10/test_input.txt"

legals = [
    "[]",
    "([])",
    "{()()()}",
    "<([{}])>",
    "[<>({}){}[([])<>]]",
    "(((((((((())))))))))",
]

corrupteds = ["(]", "{()()()>", "(((()))}", "<([]){()}[{}])"]


@pytest.mark.parametrize("pattern", legals)
def test_valid_patterns(pattern):
    assert scoring.valid_pattern(pattern)[0]


@pytest.mark.parametrize("pattern", corrupteds)
def test_corrupted_patterns(pattern):
    assert not scoring.valid_pattern(pattern)[0]


def test_compute_syntax_error_score():
    assert scoring.compute_syntax_error_score(input_file) == 26397


completions = [
    ("{()()()}", "", 0),
    ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]", 288957),
    ("[(()[<>])]({[<{<<[]>>(", ")}>]})", 5566),
    ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))", 1480781),
    ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>", 995444),
    ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>", 294),
]


@pytest.mark.parametrize("pattern, completion, score", completions)
def test_completion(pattern, completion, score):
    assert scoring.completion(pattern)[1] == completion


@pytest.mark.parametrize("pattern, completion, score", completions)
def test_completion_score(pattern, completion, score):
    completion = scoring.completion(pattern)[1]
    assert scoring.completion_score(completion) == score


def test_get_completion_winner():
    assert scoring.get_completion_winner(input_file) == 288957
