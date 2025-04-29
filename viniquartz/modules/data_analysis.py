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
        """Retorna os usuários com score >= 900 e ativos, com tempo de execução."""
        superusers_list = [
            user for user in self.data
            if user.get("score", 0) >= 900 and user.get("ativo", False)
        ]
        return superusers_list, len(superusers_list)
    
    def get_top_countries(self):
        """Agrupa os superusuários por país e retorna os 5 com mais usuários."""
        superusers_list, _ = self.get_superuser_list()

        countries = [user.get("pais") for user in superusers_list]
        country_counter = Counter(countries)
        top_5_countries = country_counter.most_common(5)

        top_countries_data = [
            {"country": country, "total": total}
            for country, total in top_5_countries
        ]
        return top_countries_data
    
    def get_team_insights(self):
        """Retorna estatísticas por equipe com base nos membros, projetos e liderança."""
        teams_list = {}
        sum_projects = 0
        for users in self.data:
            team = users.get("equipe")
            team_name = team.get("nome")

            if team_name not in teams_list:
                teams_list[team_name] = {
                    "total_members": 0,
                    "leaders": 0,
                    "completed_projects": 0,
                    "completed_projects_name": [],
                    "total_projects": 0
                }

            teams_list[team_name]["total_members"] += 1

            if team.get("lider"):
                teams_list[team_name]["leaders"] += 1
            
            for project in team.get("projetos"):
                teams_list[team_name]["total_projects"] += 1
                sum_projects += 1
                if project.get("concluido"):
                    teams_list[team_name]["completed_projects"] += 1
                    project_name = project.get("nome")
                    teams_list[team_name]["completed_projects_name"].append(project_name)
            
        result = []
        for name, stats in teams_list.items():
            total_projects = stats["total_projects"]
            total_completed_projects = stats["completed_projects"]
            result.append({
                "team": name,
                "total_members": stats["total_members"],
                "leaders": stats["leaders"],
                "completed_projects": total_completed_projects,
                #"completed_projects_name": stats["completed_projects_name"],
                "projects_percentage": round((total_completed_projects / total_projects * 100), 1) if total_projects else 0.0
            })

        return {"teams": result}

