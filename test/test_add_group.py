# -*- coding: utf-8 -*-

from model.group import Group
import pytest

testdata = [
        Group(name="proba1", header="Prob", footer="Forever"),
        Group(name="", header="", footer="")
    ]

@pytest.mark.parametrize("group", testdata)
def test_add_group(app, group):
    pass
    #old_groups = app.group.get_group_list()
    #app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    #new_groups = app.group.get_group_list()
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





