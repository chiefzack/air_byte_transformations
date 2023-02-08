import pandas as pd

def transform(df, stream_name):
    if stream_name == "ads_insights":
        # Keep only the columns that you need for the 'ads_insights' stream
        df = df[[
                  "date_start", 
                  "actions", 
                  "action_values", 
                  "ad_id", 
                  "adset_id",
                  "campaign_id",
                  "campaign_name",
                  "adset_name",
                  "ad_name",
                  "clicks",
                  "spend", 
                  "impressions", 
                  "objective"]]
    return df
    
    result = transform(df, "ads_insights")
print(result)
