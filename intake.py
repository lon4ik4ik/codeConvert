# -*- coding: utf-8 -*-

#@title <-- fill in intake parameters then click play button to left { run: "auto", display-mode: "form" }

product_scope <- commandArgs(trailingOnly = TRUE)[1]

cat("Product Scopt Value:", product_scope, "\n")

cc_platform <- commandArgs(trailingOnly = TRUE)[2]

total_level_1_call_drivers <- commandArgs(trailingOnly = TRUE)[3]

total_level_2_call_drivers = '61-80' #@param ["1-20", "21-40", "41-60", "61-80", "81-100"]

crm_integration_requirement_1 = 'Salesforce' #@param ["Salesforce", "ServiceNOW", "Hubspot", "Pega", "EPIC", "Zendesk", "Oracle Service Cloud", "Other ->", "None"] {allow-input: true}

crm_integration_requirement_2 = 'Other ->' #@param ["Salesforce", "ServiceNOW", "Hubspot", "Pega", "EPIC", "Zendesk", "Oracle Service Cloud", "Other ->", "None"] {allow-input: true}

u_analyze_conversation_packs = 'None' #@param ["None", "VOC", "Agent Performance", "Customer Loyalty", "VOC + Customer Loyalty","VOC + Agent Performance", "VOC + Agent Performance + Customer Loyalty", "Agent Performance + Customer Loyalty"] 

u_analyze_custom_dashboard_counts = 'None' #@param ["None", "1-5", "6-10"] 

u_selfserve_channels = 'None' #@param ["None", "Voice", "Mobile Chat", "Web Chat", "Voice + Mobile Chat", "Voice + Web Chat", "Mobile Chat + Web Chat", "Voice + Mobile Chat + Web Chat"] 

u_selfserve_selfservice_intents = 'None' #@param ["None", "1-5", "6-10"] 

u_selfserve_faq_intents = 'None' #@param ["None", "1-25", "26-100"] 

u_selfserve_fulfillmentapi_calls = 'None' #@param ["None", "1-10", "11-25", "26-40"] 

u_selfserve_fulfillmentapi_integrations = 'None' #@param ["None", "1-3", "4-5", "6-7"]

language_requirements = 'US English' #@param ["US English", "US English + Spanish","Japanese", "Other ->"]

client_industry = 'Financial Services' #@param ["Telco", "Healthcare - Payor", "Healthcare - Provider", "Financial Services", "Retail", "Manufacturing", "Other ->"] {allow-input: true}

client_region = 'North America' #@param ["North America", "Europe", "Asia-Pac", "Japan"] 

resource_model = 'Uniphore FTE + Contractors (any region)' #@param ["Uniphore FTE (client region)", "Uniphore FTE (any region)", "Uniphore FTE + Contractors (client region)", "Uniphore FTE + Contractors (any region)"]

base_line_ba <-1
base_line_u_assist_ba <-2
base_line_u_analyze_ba <-1
base_line_u_self_serve_ba <-1
base_line_lead_ba <-.5
base_line_tpm <-.5
base_line_sc <-.25
base_line_ie <-.5
base_line_sa <-.25
base_line_app_dev <-.25
base_line_conv_ai <-1
base_line_man_hours <- 0
base_line_cost <- 0


us_blended_cost_rate <- 70
us_contractor_blended_cost_rate <- 75
india_blended_cost_rate <- 15
india_contractor_blended_cost_rate <- 30
japan_blended_cost_rate <- 85
japan_contractor_blended_cost_rate <- 105
europe_blended_cost_rate <- 65
europe_contractor_blended_cost_rate <- 80
blended_cost_rate <- 50

scope <- product_scope
baseline <- 0
baseline_2 <-0

switch(scope,
       "Cloud - U-Assist" = {baseline <- 10} & {base_line_conv_ai <-0} & {base_line_u_analyze_ba <-0} & {base_line_u_self_serve_ba <-0},
       "Cloud - U-Analyze" = {baseline <- 7}& {base_line_conv_ai <-0} & {base_line_u_assist_ba <-0} & {base_line_u_self_serve_ba <-0},
       "Cloud - U-SelfServe" = {baseline <- 5} & {base_line_u_assist_ba <-0} & {base_line_u_analyze_ba <-0},
       "Cloud - U-Assist + U-Analyze" = {baseline <- 11}& {base_line_conv_ai <-0} & {base_line_u_self_serve_ba <-0},
       "Cloud - U-Assist + U-SelfServe" = {baseline <- 11} & {base_line_u_analyze_ba <-0},
       "Cloud - U-Assist + U-SelfServe + U-Analyze" = {baseline <- 13},
       "Cloud - U-Analyze + U-SelfServe" = {baseline <- 8} & {base_line_u_assist_ba <-0},
       "Prem - U-Assist" = {baseline <- 11}& {base_line_conv_ai <-0} & {base_line_u_analyze_ba <-0} & {base_line_u_self_serve_ba <-0},
       "Prem - U-Analyze" = {baseline <- 9}& {base_line_conv_ai <-0} & {base_line_u_assist_ba <-0} & {base_line_u_self_serve_ba <-0},
       "Prem - U-SelfServe" = {baseline <- 7} & {base_line_u_assist_ba <-0} & {base_line_u_analyze_ba <-0},
       "Prem - U-Assist + U-Analyze" = {baseline <- 13}& {base_line_conv_ai <-0} & {base_line_u_self_serve_ba <-0},
       "Prem - U-Assist + U-SelfServe" = {baseline <- 13} & {base_line_u_analyze_ba <-0},
       "Prem - U-Assist + U-SelfServe + U-Analyze" = {baseline <- 15},
       "Prem - U-Analyze + U-SelfServe" = {baseline <- 11} & {base_line_u_assist_ba <-0})

platform <- cc_platform
switch(platform,
       "Cisco" = {baseline_2 <- baseline_2} & {base_line_sa + .25},
       "Avaya" = {baseline_2 <- baseline_2} & {base_line_sa + .25},
       "Genesys Cloud" = {baseline_2 <- baseline_2 + 2},
       "Genesys PureEngage" = {baseline_2 <- baseline_2 + 2} & {base_line_sa + .25},
       "Five9" = {baseline_2 <- baseline_2},
       "inContact" = {baseline_2 <- baseline_2 + 3},
       "RingCentral" = {baseline_2 <- baseline_2 + 3},
       "Twilio" = {baseline_2 <- baseline_2},
       "Talkdesk" = {baseline_2 <- baseline_2 + 3},
       "Amazon Connect" = {baseline_2 <- baseline_2 + 2},
       "Other->" = {baseline_2 <- baseline_2 + 4}
       )  


lang <- language_requirements
switch(lang,
       "US English" = {baseline_2 <- baseline_2},
       "US English + Spanish" = {baseline_2 <- baseline_2 + 2} & {base_line_ba <- base_line_ba +2},
       "Japanese" = {baseline_2 <- baseline_2 + 2},
       "Other ->" = {baseline_2 <- baseline_2 + 2}
       )  

crm_1 <- crm_integration_requirement_1
switch(crm_1,
       "None" = {baseline_2 <- baseline_2},
       "Salesforce" = {baseline_2 <- baseline_2},
       "ServiceNOW" = {baseline_2 <- baseline_2},
       "Hubspot" = {baseline_2 <- baseline_2},
       "EPIC" = {baseline_2 <- baseline_2+1} & {base_line_app_dev <- base_line_app_dev +.5},
       "Zendesk" = {baseline_2 <- baseline_2},
       "Oracle Service Cloud" = {baseline_2 <- baseline_2},
       "Other ->" = {baseline_2 <- baseline_2+2} & {base_line_app_dev <- base_line_app_dev +.5}
       )

crm_2 <- crm_integration_requirement_2
switch(crm_2,
       "None" = {baseline_2 <- baseline_2},
       "Salesforce" = {baseline_2 <- baseline_2+1} & {base_line_app_dev <- base_line_app_dev +.25},
       "ServiceNOW" = {baseline_2 <- baseline_2+1}  & {base_line_app_dev <- base_line_app_dev +.25},
       "Hubspot" = {baseline_2 <- baseline_2+1}  & {base_line_app_dev <- base_line_app_dev +.25},
       "EPIC" = {baseline_2 <- baseline_2+2} & {base_line_app_dev <- base_line_app_dev +.5},
       "Zendesk" = {baseline_2 <- baseline_2+1}  & {base_line_app_dev <- base_line_app_dev +.25},
       "Oracle Service Cloud" = {baseline_2 <- baseline_2+1}  & {base_line_app_dev <- base_line_app_dev +.25},
       "Other ->" = {baseline_2 <- baseline_2+2} & {base_line_app_dev <- base_line_app_dev +.5}
       )

if (scope == "Cloud - U-Assist" || 
      scope == "Prem - U-Assist"){

level_1 <- total_level_1_call_drivers
switch(level_1,
       "6-9" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + 2},
       "10-20" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 3},
       "21-30" = {baseline_2 <- baseline_2 + 3} & {base_line_u_assist_ba <- base_line_u_assist_ba + 4},
       "31-40" = {baseline_2 <- baseline_2 + 4} & {base_line_u_assist_ba <- base_line_u_assist_ba + 5} & {base_line_tpm <- base_line_tpm + .5},
       "41-50" = {baseline_2 <- baseline_2 + 5} & {base_line_u_assist_ba <- base_line_u_assist_ba + 6} & {base_line_tpm <- base_line_tpm + 5}
       )

level_2 <- total_level_2_call_drivers
switch(level_2,
       "1-20" = {baseline_2 <- baseline_2},
       "21-40" = {baseline_2 <- baseline_2} & {base_line_u_assist_ba <- base_line_u_assist_ba},
       "41-60" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + .5},
       "61-80" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1},
       "81-100" = {baseline_2 <- baseline_2 + 3} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1.5}
       )
}

if (scope == "Cloud - U-Analyze" || 
      scope == "Prem - U-Analyze"){

conversation_packs <- u_analyze_conversation_packs
switch(conversation_packs,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba},
       "VOC" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Agent Performance" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "VOC + Customer Loyalty" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1.5},
       "VOC + Agent Performance" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1.5},
       "VOC + Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 3} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2} & {base_line_tpm <- base_line_tpm + .5},
       "Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1.5}
       )

dashboard <- u_analyze_custom_dashboard_counts
switch(dashboard,
       "None" = {baseline_2 <- baseline_2},
       "1-5" = {baseline_2 <- baseline_2 + .5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba},
       "6-10" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + .5}
       )
}

if (scope == "Cloud - U-SelfServe" || 
      scope == "Prem - U-SelfServe"){

ss_intents <- u_selfserve_selfservice_intents
switch(ss_intents,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "1-5" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "6-10" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25} & {base_line_tpm <- base_line_tpm + .5}
       )

faq_intents <- u_selfserve_faq_intents
switch(faq_intents,
       "None" = {baseline_2 <- baseline_2},
       "1-25" = {baseline_2 <- baseline_2 + 1} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "26-100" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

api_calls <- u_selfserve_fulfillmentapi_calls
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-10" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "11-25" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + .25},
       "26-40" = {baseline_2 <- baseline_2 + 1.5} & {base_line_app_dev <- base_line_app_dev + .50}
       )

api_integrations <- u_selfserve_fulfillmentapi_integrations
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-3" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "4-5" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + .25},
       "6-7" = {baseline_2 <- baseline_2 + 1.5} & {base_line_app_dev <- base_line_app_dev + .50}
       )      

channels <- u_selfserve_channels
switch(api_calls,
       "Voice" = {baseline_2 <- baseline_2},
       "Mobile Chat" = {baseline_2 <- baseline_2},
       "Web Chat" = {baseline_2 <- baseline_2},
       "Voice + Mobile Chat" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "Voice + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Mobile Chat + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Voice + Mobile Chat + Web Chat" = {baseline_2 <- baseline_2 + 1.5} & {base_line_app_dev <- base_line_app_dev + 1}

       )  

}

if (scope == "Cloud - U-Assist + U-Analyze" || 
      scope == "Prem - U-Assist + U-Analyze"){

base_line_tpm <- base_line_tpm + .5        

level_1 <- total_level_1_call_drivers
switch(level_1,
       "6-9" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + 2},
       "10-20" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 2.5},
       "21-30" = {baseline_2 <- baseline_2 + 3} & {base_line_u_assist_ba <- base_line_u_assist_ba + 3},
       "31-40" = {baseline_2 <- baseline_2 + 4} & {base_line_u_assist_ba <- base_line_u_assist_ba + 3.5},
       "41-50" = {baseline_2 <- baseline_2 + 5} & {base_line_u_assist_ba <- base_line_u_assist_ba + 4}
       )

level_2 <- total_level_2_call_drivers
switch(level_2,
       "1-20" = {baseline_2 <- baseline_2},
       "21-40" = {baseline_2 <- baseline_2 + .5} & {base_line_u_assist_ba <- base_line_u_assist_ba + .25},
       "41-60" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + .5},
       "61-80" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1},
       "81-100" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1.5}
       )


conversation_packs <- u_analyze_conversation_packs
switch(conversation_packs,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba},
       "VOC" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba - 1},
       "Agent Performance" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba },
       "Customer Loyalty" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + .5},
       "VOC + Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "VOC + Agent Performance" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "VOC + Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1}
       )

dashboard <- u_analyze_custom_dashboard_counts
switch(dashboard,
       "None" = {baseline_2 <- baseline_2},
       "1-5" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba},
       "6-10" = {baseline_2 <- baseline_2 + .5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + .5} 
       )

}
if (scope == "Cloud - U-Assist + U-SelfServe" || 
      scope == "Prem - U-Assist + U-SelfServe"){

base_line_tpm <- base_line_tpm + .5        

level_1 <- total_level_1_call_drivers
switch(level_1,
       "6-9" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + 2},
       "10-20" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 3},
       "21-30" = {baseline_2 <- baseline_2 + 3} & {base_line_u_assist_ba <- base_line_u_assist_ba + 4},
       "31-40" = {baseline_2 <- baseline_2 + 4} & {base_line_u_assist_ba <- base_line_u_assist_ba + 5},
       "41-50" = {baseline_2 <- baseline_2 + 5} & {base_line_u_assist_ba <- base_line_u_assist_ba + 6}
       )

level_2 <- total_level_2_call_drivers
switch(level_2,
       "1-20" = {baseline_2 <- baseline_2},
       "21-40" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + .5},
       "41-60" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "61-80" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1.5},
       "81-100" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2}
       )

ss_intents <- u_selfserve_selfservice_intents
switch(ss_intents,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "1-5" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "6-10" = {baseline_2 <- baseline_2 + 1} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

faq_intents <- u_selfserve_faq_intents
switch(faq_intents,
       "None" = {baseline_2 <- baseline_2},
       "1-25" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "26-100" = {baseline_2 <- baseline_2 + 1} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

api_calls <- u_selfserve_fulfillmentapi_calls
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-10" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "11-25" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + .25},
       "26-40" = {baseline_2 <- baseline_2 + 1.5} & {base_line_app_dev <- base_line_app_dev + .50}
       )

api_integrations <- u_selfserve_fulfillmentapi_integrations
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-3" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "4-5" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + .25},
       "6-7" = {baseline_2 <- baseline_2 + 1.5} & {base_line_app_dev <- base_line_app_dev + .50}
       )      

channels <- u_selfserve_channels
switch(api_calls,
       "Voice" = {baseline_2 <- baseline_2},
       "Mobile Chat" = {baseline_2 <- baseline_2},
       "Web Chat" = {baseline_2 <- baseline_2},
       "Voice + Mobile Chat" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "Voice + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Mobile Chat + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Voice + Mobile Chat + Web Chat" = {baseline_2 <- baseline_2 + 1.5} & {base_line_app_dev <- base_line_app_dev + 1}

       ) 


}

if (scope == "Cloud - U-Assist + U-SelfServe + U-Analyze" || 
      scope == "Prem - U-Assist + U-SelfServe + U-Analyze"){

base_line_tpm <- base_line_tpm + .75        

level_1 <- total_level_1_call_drivers
switch(level_1,
       "6-9" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + 2},
       "10-20" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 3},
       "21-30" = {baseline_2 <- baseline_2 + 3} & {base_line_u_assist_ba <- base_line_u_assist_ba + 4},
       "31-40" = {baseline_2 <- baseline_2 + 4} & {base_line_u_assist_ba <- base_line_u_assist_ba + 5},
       "41-50" = {baseline_2 <- baseline_2 + 5} & {base_line_u_assist_ba <- base_line_u_assist_ba + 6}
       )

level_2 <- total_level_2_call_drivers
switch(level_2,
       "1-20" = {baseline_2 <- baseline_2},
       "21-40" = {baseline_2 <- baseline_2 + .5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + .5},
       "41-60" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "61-80" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1.5},
       "81-100" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2}
       )


conversation_packs <- u_analyze_conversation_packs
switch(conversation_packs,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba},
       "VOC" = {baseline_2 <- baseline_2 + .5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Agent Performance" = {baseline_2 <- baseline_2 + .5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Customer Loyalty" = {baseline_2 <- baseline_2 + .5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "VOC + Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2},
       "VOC + Agent Performance" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2},
       "VOC + Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 1.5} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 3},
       "Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2}
       )

dashboard <- u_analyze_custom_dashboard_counts
switch(dashboard,
       "None" = {baseline_2 <- baseline_2},
       "1-5" = {baseline_2 <- baseline_2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1},
       "6-10" = {baseline_2 <- baseline_2 + .5} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1} 
       )

ss_intents <- u_selfserve_selfservice_intents
switch(ss_intents,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "1-5" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "6-10" = {baseline_2 <- baseline_2 + 1} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

faq_intents <- u_selfserve_faq_intents
switch(faq_intents,
       "None" = {baseline_2 <- baseline_2},
       "1-25" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "26-100" = {baseline_2 <- baseline_2 + .5} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

api_calls <- u_selfserve_fulfillmentapi_calls
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-10" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "11-25" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev + .25},
       "26-40" = {baseline_2 <- baseline_2 + .5} & {base_line_app_dev <- base_line_app_dev + .50}
       )

api_integrations <- u_selfserve_fulfillmentapi_integrations
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-3" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "4-5" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev + .25},
       "6-7" = {baseline_2 <- baseline_2 + .5} & {base_line_app_dev <- base_line_app_dev + .50}
       )      

channels <- u_selfserve_channels
switch(api_calls,
       "Voice" = {baseline_2 <- baseline_2},
       "Mobile Chat" = {baseline_2 <- baseline_2},
       "Web Chat" = {baseline_2 <- baseline_2},
       "Voice + Mobile Chat" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "Voice + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Mobile Chat + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Voice + Mobile Chat + Web Chat" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + 1}

       ) 
      }

if (scope == "Cloud - U-Analyze + U-SelfServe" || 
      scope == "Prem - U-Analyze + U-SelfServe"){

conversation_packs <- u_analyze_conversation_packs
switch(conversation_packs,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba},
       "VOC" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Agent Performance" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "Customer Loyalty" = {baseline_2 <- baseline_2 + 1} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 1},
       "VOC + Customer Loyalty" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2},
       "VOC + Agent Performance" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2},
       "VOC + Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 3} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 3},
       "Agent Performance + Customer Loyalty" = {baseline_2 <- baseline_2 + 2} & {base_line_u_analyze_ba <- base_line_u_analyze_ba + 2}
       )

dashboard <- u_analyze_custom_dashboard_counts
switch(dashboard,
       "None" = {baseline_2 <- baseline_2},
       "1-5" = {baseline_2 <- baseline_2 + 1} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1},
       "6-10" = {baseline_2 <- baseline_2 + 2} & {base_line_u_assist_ba <- base_line_u_assist_ba + 1} 
       )

ss_intents <- u_selfserve_selfservice_intents
switch(ss_intents,
       "None" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "1-5" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "6-10" = {baseline_2 <- baseline_2 + 1} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

faq_intents <- u_selfserve_faq_intents
switch(faq_intents,
       "None" = {baseline_2 <- baseline_2},
       "1-25" = {baseline_2 <- baseline_2 + .5} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "26-100" = {baseline_2 <- baseline_2 + 1} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba + 1} & {base_line_conv_ai <- base_line_conv_ai + .5} & {base_line_app_dev <- base_line_app_dev + .25}
       )

api_calls <- u_selfserve_fulfillmentapi_calls
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-10" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "11-25" = {baseline_2 <- baseline_2 + .5} & {base_line_app_dev <- base_line_app_dev + .25},
       "26-40" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + .50}
       )

api_integrations <- u_selfserve_fulfillmentapi_integrations
switch(api_calls,
       "None" = {baseline_2 <- baseline_2},
       "1-3" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "4-5" = {baseline_2 <- baseline_2 + .5} & {base_line_app_dev <- base_line_app_dev + .25},
       "6-7" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + .50}
       )      

channels <- u_selfserve_channels
switch(api_calls,
       "Voice" = {baseline_2 <- baseline_2},
       "Mobile Chat" = {baseline_2 <- baseline_2},
       "Web Chat" = {baseline_2 <- baseline_2},
       "Voice + Mobile Chat" = {baseline_2 <- baseline_2} & {base_line_u_self_serve_ba <- base_line_u_self_serve_ba},
       "Voice + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Mobile Chat + Web Chat" = {baseline_2 <- baseline_2} & {base_line_app_dev <- base_line_app_dev},
       "Voice + Mobile Chat + Web Chat" = {baseline_2 <- baseline_2 + 1} & {base_line_app_dev <- base_line_app_dev + 1}

       ) 


}

baseline <- baseline + baseline_2

total_fte_equiv <- (base_line_u_assist_ba + 
                    base_line_u_analyze_ba +
                    base_line_u_self_serve_ba +
                    base_line_lead_ba +
                    base_line_tpm +
                    base_line_sc +
                    base_line_ie +
                    base_line_sa +
                    base_line_app_dev +
                    base_line_conv_ai)

base_line_man_hours <- (total_fte_equiv * baseline * 40)

if (client_region == "North America"){

switch(resource_model,
       "Uniphore FTE + Contractors (any region)" = 
       {base_line_cost <- 
          ((base_line_man_hours * .2)*((us_blended_cost_rate + us_contractor_blended_cost_rate)/2)) +
          ((base_line_man_hours * .8)*((india_blended_cost_rate + india_contractor_blended_cost_rate)/2))
            },

       "Uniphore FTE (client region)" = 
       {base_line_cost <- (base_line_man_hours * us_blended_cost_rate)
            },            

       "Uniphore FTE (any region)" = 
         {base_line_cost <- 
          ((base_line_man_hours * .2)*(us_blended_cost_rate)) +
          ((base_line_man_hours * .8)*(india_blended_cost_rate))
            },            

       "Uniphore FTE + Contractors (client region)" = 
         {base_line_cost <- 
          ((base_line_man_hours)*((us_blended_cost_rate + us_contractor_blended_cost_rate)/2))            
          }            



       )
      }


if (client_region == "Europe"){

switch(resource_model,
       "Uniphore FTE + Contractors (any region)" = 
       {base_line_cost <- 
          ((base_line_man_hours * .2)*((europe_blended_cost_rate + europe_contractor_blended_cost_rate)/2)) +
          ((base_line_man_hours * .8)*((india_blended_cost_rate + india_contractor_blended_cost_rate)/2))
            },

       "Uniphore FTE (client region)" = 
       {base_line_cost <- (base_line_man_hours * europe_blended_cost_rate)
            },            

       "Uniphore FTE (any region)" = 
         {base_line_cost <- 
          ((base_line_man_hours * .2)*(europe_blended_cost_rate)) +
          ((base_line_man_hours * .8)*(india_blended_cost_rate))
            },            

       "Uniphore FTE + Contractors (client region)" = 
         {base_line_cost <- 
          ((base_line_man_hours)*((europe_blended_cost_rate + europe_contractor_blended_cost_rate)/2))            
          }            



       )
      }


if (client_region == "Asia-Pac"){

switch(resource_model,
       "Uniphore FTE + Contractors (any region)" = 
       {base_line_cost <- 
          ((base_line_man_hours)*((india_blended_cost_rate + india_contractor_blended_cost_rate)/2))
            },

       "Uniphore FTE (client region)" = 
       {base_line_cost <- (base_line_man_hours * india_blended_cost_rate)
            },            

       "Uniphore FTE (any region)" = 
         {base_line_cost <- 
          ((base_line_man_hours)*(india_blended_cost_rate))
            },            

       "Uniphore FTE + Contractors (client region)" = 
         {base_line_cost <- 
          ((base_line_man_hours)*((india_blended_cost_rate + india_contractor_blended_cost_rate)/2))
          }            



       )
      }


if (client_region == "Japan"){

switch(resource_model,
       "Uniphore FTE + Contractors (any region)" = 
       {base_line_cost <- 
          ((base_line_man_hours * .2)*((japan_blended_cost_rate + japan_contractor_blended_cost_rate)/2)) +
          ((base_line_man_hours * .8)*((india_blended_cost_rate + india_contractor_blended_cost_rate)/2))
            },

       "Uniphore FTE (client region)" = 
       {base_line_cost <- (base_line_man_hours * japan_blended_cost_rate)
            },            

       "Uniphore FTE (any region)" = 
         {base_line_cost <- 
          ((base_line_man_hours * .2)*(japan_blended_cost_rate)) +
          ((base_line_man_hours * .8)*(india_blended_cost_rate))
            },            

       "Uniphore FTE + Contractors (client region)" = 
         {base_line_cost <- 
          ((base_line_man_hours)*((japan_blended_cost_rate + japan_contractor_blended_cost_rate)/2))            
          }            



       )
      }

#@title <--- click play button for staffing requirements & duration estimate { run: "auto", display-mode: "form" }



paste("Total estimated weeks: ", baseline)
paste("Total FTE equiv:", total_fte_equiv)
paste("Total estimated man hours: ", base_line_man_hours)
paste("Total estimated cost: $",base_line_cost)

"Staffing Requirements:"
paste("U-Assist BA: ",base_line_u_assist_ba)
paste("U-Analyze BA: ", base_line_u_analyze_ba)
paste("U-SelfServe BA: ",base_line_u_self_serve_ba)
paste("Lead BA: ", base_line_lead_ba)
paste("TPM: ", base_line_tpm)
paste("Solution Consultant: ", base_line_sc)
paste("Implementation Engineer: ", base_line_ie)
paste("Solution Architect: ", base_line_sa)
paste("Full Stack Developer: ", base_line_app_dev)
paste("Conversational AI Designer: ", base_line_conv_ai)
