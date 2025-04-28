from collections import Counter

class DataAnalysis:
    def __init__(self, data):
        """Initializes the connection to Secret Server"""
        self.data = data

    def get_property_for_all_data(self, property_name):
        return [users.get(property_name) for users in self.data]
    
    def get_user_by_id(self, user_id):
        for user in self.data:
            if user["id"] == user_id:
                return user
        return None
    
    def get_superuser_list(self):
        superusers_list = [
            user for user in self.data
            if user.get("score", 0) >= 900 and user.get("ativo", False)
        ]
        return superusers_list, len(superusers_list)
    
    def get_top_countries(self):
        superusers_list, _ = self.get_superuser_list()

        countries = [user.get("pais") for user in superusers_list]
        country_counter = Counter(countries)
        top_5_countries = country_counter.most_common(5)

        top_countries_data = [
            {"country": country, "total": total}
            for country, total in top_5_countries
        ]
        return top_countries_data