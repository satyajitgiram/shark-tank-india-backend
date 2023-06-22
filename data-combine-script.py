import json

# Read data from data_s1.json
json1= "/home/zec/personal/Tasks/by-tusharsir/shark-tank-india/shark_tank_backend/SharkTankIndia.json"
with open(json1) as file_s1:
    data_s1 = json.load(file_s1)

# Read data from data_s2.json
json2= "/home/zec/personal/Tasks/by-tusharsir/shark-tank-india/shark_tank_backend/data_s1.json"
with open(json2) as file_s2:
    data_s2 = json.load(file_s2)



# Select specific fields from data_s1
selected_data_s1 = []
for item_s1 in data_s1:
    selected_item_s1 = {
        "id":item_s1["pitch_number"],
        "episode_number": item_s1["episode_number"],
        "pitch_number": item_s1["pitch_number"],
        "brand_name": item_s1["brand_name"],
        "pitcher_ask_amount": item_s1["pitcher_ask_amount"],
        "pitcher_ask_equity": item_s1["ask_equity"], 
        "pitcher_ask_valuation": item_s1["ask_valuation"], 
        "deal_amount": item_s1["deal_amount"], 
        "deal_equity": item_s1["deal_equity"], 
        "total_sharks_invested": item_s1["total_sharks_invested"], 
        "equity_per_shark": item_s1["equity_per_shark"], 
        "sharks_present": {"ashneer": item_s1["ashneer_present"],"anupam": item_s1["anupam_present"],"aman": item_s1["aman_present"],"namita": item_s1["namita_present"],"vineeta": item_s1["vineeta_present"],"peyush": item_s1["peyush_present"],"ghazal": item_s1["ghazal_present"]}, 
        "sector": item_s1["ask_equity"], 
        "deal_or_not": item_s1["deal"],
        "deal_valuation": item_s1["deal_valuation"],
        
    }
    data = {"ashneer": item_s1["ashneer_deal"],"anupam": item_s1["anupam_deal"],"aman": item_s1["aman_deal"],"namita": item_s1["namita_deal"],"vineeta": item_s1["vineeta_deal"],"peyush": item_s1["peyush_deal"],"ghazal": item_s1["ghazal_deal"]}

    sharks_deal = {}

    for key, value in data.items():
        if value == 1:
            name = key.split("_")[0]
            sharks_deal[name] = value

    selected_item_s1["sharks_deal"] = sharks_deal

    selected_data_s1.append(selected_item_s1)

# Select specific fields from data_s2
selected_data_s2 = []
for item_s2 in data_s2:
    selected_item_s2 = {
        "product/idea": item_s2["Product"],
        "sector": item_s2["Sector"],
        "company_social_media":{"twitter": item_s2["Twitter (Company)"],
            "linkedin": item_s2["LinkedIn (Company)"],
            "instagram": item_s2["Instagram (Company)"],
            "facebook": item_s2["Facebook (Company)"],
            "youtube": item_s2["Youtube (Company)"],
        },
        "company_website": item_s2["Website (Company)"],
        "final_deal_debt": item_s2["Final Deal Debt in INR"],
        "final_deal_dept_interest": item_s2["Final Deal Debt Interest in %"],
    }
    

    founders = item_s2["Entrepreneurs/Founders"]
    founders_list = founders.split(",")
    # Remove empty elements from the list 
    founders_list = [founder.strip() for founder in founders_list if founder.strip()]
    # Join the list elements back into a string
    cleaned_founders = ", ".join(founders_list)
    selected_item_s2["entrepreneurs/founders"] = cleaned_founders
    selected_data_s2.append(selected_item_s2)
    



# Combine data from both files
combined_data = []
for item_s1, item_s2 in zip(selected_data_s1, selected_data_s2):
    combined_item = {**item_s1, **item_s2}
    combined_data.append(combined_item)


for i in combined_data:
    print(i)
    print("--------------------------------------------------")

# Write the combined data to a new JSON file
with open('combined_data.json', 'w') as combined_file:
    json.dump(combined_data, combined_file, indent=4)

print("Combined data has been written to combined_data.json.")
