{% set stream_name = 'custom_meta_core' %}

{{
  config({
    "stream_name": stream_name
  })
}}

{{
  select(
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
    "objective"
  )
}}

