import pandas as pd


class Retriever:
    def __init__(self, catalog_path):
        self._catalog_df = pd.read_excel("models/catalog.xlsx")

    def retrieve_cost(self, products_idx):
        min_costs = [(product_idx, self._catalog_df.loc[product_idx, "Цена"]) for product_idx in products_idx]
        return sorted(min_costs, key=lambda x: x[1])[:3]

    def retrieve_tags(self, tags):
        gender_products_idx = self._catalog_df.loc[self._catalog_df["Пол"].str.contains(tags.sex, na=True)].index
        gender_tags_df = self._catalog_df.iloc[gender_products_idx]

        hair_type_products_idx = gender_tags_df.loc[
            (
                gender_tags_df["Тип волос"].str.contains(tags.hair_type, na=True)
                | (gender_tags_df["Тип волос"].str == "все типы волос")
            )
        ].index
        hair_type_tags_df = self._catalog_df.iloc[hair_type_products_idx]

        if len(hair_type_tags_df) > 3:
            effect_products_idx = hair_type_tags_df.loc[
                hair_type_tags_df["Действие"].str.contains(tags.action, na=False)
            ].index
            effect_tags_df = self._catalog_df.iloc[effect_products_idx]

            if len(effect_tags_df) > 3:
                product_type_products_idx = effect_tags_df.loc[
                    effect_tags_df["Тип товара"].str.contains(tags.product_type, na=False)
                ].index
                return product_type_products_idx

            else:
                return effect_products_idx

        else:
            return hair_type_products_idx

    def get_products(self, tags):
        products_idx = self.retrieve_tags(tags)
        if len(products_idx) > 3 and tags.is_cheap:
            products_idx = self.retrieve_cost(products_idx)
        else:
            products_idx = products_idx[:3]
        return products_idx

    def get_products_descriptions(self, tags):
        products_idx = self.get_products(tags)
        descriptions = self._catalog_df.loc[products_idx, "О продукте"].to_list()
        names = self._catalog_df.loc[products_idx, "Название"].to_list()
        links = self._catalog_df.loc[products_idx, "Ссылка"].to_list()

        names_with_links_and_descriptions = [{"name": None, "link": None, "description": None} for _ in range(3)]

        for i in range(len(names)):
            names_with_links_and_descriptions[i] = {"name": names[i], "link": links[i], "description": descriptions[i]}

        return names_with_links_and_descriptions
