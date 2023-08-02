import pytest

from exept import UserAccessExeption, UserLevelExeption
from project import Project
from user import User


@pytest.fixture
def start_project():
    return Project.load_json()


@pytest.fixture
def exist_user():
    return User('User1', 1, 5)


@pytest.fixture
def not_exist_user():
    return User('User12345', 12345, 8)


@pytest.fixture
def user_level_dn():
    return User('User2', 2, 1)


def test_load_json_project(start_project):
    assert len(start_project.user_ls) > 1


def test_inter_project(start_project, exist_user):
    start_project.inter_project(exist_user.name, exist_user.id)
    assert start_project.admin == exist_user


def test_error_inter_project(start_project, not_exist_user):
    with pytest.raises(UserAccessExeption):
        start_project.inter_project(not_exist_user.name, not_exist_user.id)


def test_error_level_add_user(start_project, exist_user, user_level_dn):
    start_project.inter_project(exist_user.name, exist_user.id)
    with pytest.raises(UserLevelExeption):
        start_project.add_user(user_level_dn.name, user_level_dn.id, user_level_dn.level)


def test_add_user(start_project, exist_user, not_exist_user):
    start_project.inter_project(exist_user.name, exist_user.id)
    start_project.add_user(not_exist_user.name, not_exist_user.id, not_exist_user.level)
    assert start_project.user_ls[len(start_project.user_ls) - 1] == not_exist_user


def test_del_user(start_project, exist_user):
    start_project.inter_project(exist_user.name, exist_user.id)
    len_before = len(start_project.user_ls)
    start_project.del_user(exist_user.name, exist_user.id, exist_user.level)
    assert len(start_project.user_ls) < len_before


if __name__ == '__main__':
    pytest.main()
