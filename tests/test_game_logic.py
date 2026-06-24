from logic_utils import check_guess, update_score


# ---------------------------------------------------------------------------
# check_guess — existing baseline tests (outcome only)
# ---------------------------------------------------------------------------

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# check_guess — bug: hint messages were swapped
# When guess > secret the player needs to go LOWER, not HIGHER.
# When guess < secret the player needs to go HIGHER, not LOWER.
# ---------------------------------------------------------------------------

def test_too_high_hint_says_go_lower():
    # Bug was: "Too High" returned "Go HIGHER!" (contradicts the outcome)
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Bug was: "Too Low" returned "Go LOWER!" (contradicts the outcome)
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_win_hint_says_correct():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_hints_are_not_swapped():
    # One assertion that directly contrasts both directions
    _, high_msg = check_guess(99, 1)   # way too high
    _, low_msg  = check_guess(1, 99)   # way too low
    assert "LOWER" in high_msg
    assert "HIGHER" in low_msg


# ---------------------------------------------------------------------------
# update_score — bug 1: "Too High" on even attempts awarded +5 instead of -5
# Every wrong guess should deduct 5 points regardless of attempt parity.
# ---------------------------------------------------------------------------

def test_too_high_on_even_attempt_deducts():
    # Bug was: attempt_number % 2 == 0 gave +5 for "Too High"
    score = update_score(100, "Too High", attempt_number=2)
    assert score == 95  # should deduct, not add

def test_too_high_on_odd_attempt_deducts():
    score = update_score(100, "Too High", attempt_number=3)
    assert score == 95

def test_too_high_deduction_is_consistent_across_attempts():
    # Both even and odd attempts must produce the same result
    even = update_score(100, "Too High", attempt_number=2)
    odd  = update_score(100, "Too High", attempt_number=3)
    assert even == odd

def test_too_low_deducts():
    score = update_score(100, "Too Low", attempt_number=1)
    assert score == 95


# ---------------------------------------------------------------------------
# update_score — bug 2: win points used (attempt_number + 1) causing off-by-one
# Points should be 100 - 10 * attempt_number, not 100 - 10 * (attempt_number + 1).
# ---------------------------------------------------------------------------

def test_win_on_first_attempt_score():
    # attempt_number=1 → points = 100 - 10*1 = 90
    # Bug gave: 100 - 10*(1+1) = 80
    score = update_score(0, "Win", attempt_number=1)
    assert score == 90

def test_win_on_second_attempt_score():
    # attempt_number=2 → points = 100 - 10*2 = 80
    score = update_score(0, "Win", attempt_number=2)
    assert score == 80

def test_win_score_floors_at_10():
    # Late win (attempt 10+) should never go below 10 points
    score = update_score(0, "Win", attempt_number=10)
    assert score == 10

def test_win_score_does_not_go_below_floor():
    score = update_score(0, "Win", attempt_number=50)
    assert score == 10
