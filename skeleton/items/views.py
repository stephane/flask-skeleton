from flask import Blueprint, render_template

from .models import Item

items = Blueprint('items', __name__, template_folder='templates')

@items.route('/', methods=['GET'])
def item_list():
    items = Item.query.order_by(Item.name).all()
    return render_template('item_list.html', items=items)
