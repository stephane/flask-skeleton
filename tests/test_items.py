from flask import url_for

from skeleton.items import models as items_models

def test_item_list(session, client):
    item_1 = items_models.Item(code='FOO', name='Foo')
    item_2 = items_models.Item(code='BAR', name='Bar')
    session.add_all([item_1, item_2])

    assert items_models.Item.query.count() == 2
    url = url_for('items.item_list')
    response = client.get(url)
    assert response.status_code == 200
    assert item_1.name in response
    assert item_2.name in response
    assert item_1.code not in response
