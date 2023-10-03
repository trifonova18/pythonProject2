import pytest

@pytest.fixture
def set_up():
    print('ход в систему выполнен')
def test_sending_mail_1():
    print('Письмо отправлено')

def test_sending_mail_2():
    print('Письмо отправлено')


