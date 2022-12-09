import os
import pytest


@pytest.fixture
def test_tmpfile():
    # 一時ファイルを作成
    tmp_file_path = os.path.join('test','sample.txt')
    with open(tmp_file_path, 'w') as f:
        # 作成したファイルパスを渡す
        return tmp_file_path


def test_file_exist(test_tmpfile):
    # このテストメソッドが実行される前に
    # test_file() が実行され戻り値が引数で渡される
    assert os.path.isfile(test_tmpfile)