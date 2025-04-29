import modules.data_analysis
import modules.load_data
import json

def main():
    data = modules.load_data.get_data()
    data_analysis = modules.data_analysis.DataAnalysis(data)

    # all_users= data_analysis.get_property_for_all_data("nome")
    # print(f"total: {len(all_users)}\n{all_users}")

    # superusers, total = data_analysis.get_superuser_list()
    # superusers_names = [user.get("nome") for user in superusers]
    # print(f"total: {total}\n{superusers_names}")

    # top_countries = data_analysis.get_top_countries()
    # print(f"top_countries:\n{top_countries}")
    
    team_insights = data_analysis.get_team_insights()
    print(json.dumps(team_insights, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()