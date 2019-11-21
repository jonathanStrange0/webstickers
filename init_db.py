from app.models import Collection, CollectionItem
from app import db
import pandas as pd
import os
dir = os.path.abspath(os.path.dirname(__file__))

def main():
    for collection in Collection.query.all():
        db.session.delete(collection)
    db.session.commit()
    products_df = pd.read_csv(os.path.join(dir, 'app/rw_product_data.csv'))
    # pair down collection_df into two df's:
    # one with Collection Table info:
    #   one unique field: collection_name
    # One table with the info for CollectionItems
    # item_name
    # species
    # width
    # durability
    # length
    # iw_name
    # collection (relationship to Collection Table)
    for collection in products_df["Collection"].unique():
        c = Collection(collection_name=collection)
        db.session.add(c)
        print(c)
    db.session.commit()

    for collection_item in CollectionItem.query.all():
        db.session.delete(collection_item)
    db.session.commit()

    item_df = products_df[['Product Name', \
                            'Species', 'Width', \
                            'Durability','Length',\
                            'PO Description', 'Collection']]
    item_df.columns = ['item_name', 'species', 'width',\
                        'durability', 'length', 'iw_name', 'collection_id']

    item_df.collection_id = \
            item_df.collection_id.apply(lambda x:\
                Collection.query.filter_by(collection_name=x).first().id)
    # print(item_df.head())
    item_df.drop_duplicates(subset='item_name',
                            keep='first',
                            inplace=True)


    item_df.to_sql('collection_item',
                    db.session.bind,
                    if_exists='append',
                    index=False)


if __name__ == '__main__':
    main()
