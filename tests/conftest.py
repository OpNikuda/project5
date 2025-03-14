@pytest.fixture
def valid_card_number():
    return "1234567890123456"


@pytest.fixture
def invalid_card_number():
    return "1234"


@pytest.fixture
def card_number_with_spaces():
    return "1234 5678 9012 3456"


@pytest.fixture
def valid_account_number():
    return "12345678901234567890"


@pytest.fixture
def invalid_account_number():
    return "123"


@pytest.fixture
def account_number_with_spaces():
    return "1234 5678 9012 3456 7890"


@pytest.fixture
def sample_data():
    return [
        {'state': 'EXECUTED', 'date': '2023-01-01', 'amount': 100},
        {'state': 'PENDING', 'date': '2023-01-02', 'amount': 200},
        {'state': 'EXECUTED', 'date': '2023-01-03', 'amount': 300},
        {'state': 'CANCELED', 'date': '2023-01-04', 'amount': 400},
    ]


@pytest.fixture
def unsorted_data():
    return [
        {'date': '2023-01-03', 'amount': 300},
        {'date': '2023-01-01', 'amount': 100},
        {'date': '2023-01-04', 'amount': 400},
        {'date': '2023-01-02', 'amount': 200},
    ]


@pytest.fixture
def card_number_for_masking():
    return "1234567890123456"


@pytest.fixture
def card_number_for_masking():
    return "1234567890123456"


@pytest.fixture
def account_number_for_masking():
    return "12345678901234567890"

@pytest.fixture
def invalid_payment_info():
    return "1234abcd5678"