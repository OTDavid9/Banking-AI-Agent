tools_listing = [    

        {
            "type": "function",
            "function": {
                "name": "search_cognitive_service",
                "description": "Get response from the context in search_cognitive_service, if the user ask about information from document",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cognitive_query": {
                            "type": "string",
                            "description": "User question about information in cognitive service ",
                        },
                        
                    },
                    "required": ["cognitive_query"],
                },
            }
        },
        
        {
            "type": "function",
            "function": {
                "name": "complaints",
                "description": "Get response from the function 'complaints' when the user have complaints.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "complaints_query": {
                            "type": "string",
                            "description": "User question information in relating to complaints e.g 'I have issuess with my accounts', 'I want to lodge a complaint' "
                        },
                        
                    },
                    "required": ["complaints_query"],
                },
            }
        },

        

         {
        "type": "function",
        "function": {
            "name": "handle_unknown_query",
            "description": "Always response with the phrase 'I CAN'T ANSWER'",
            "parameters": {
                "type": "object",
                "properties": {
                    "unknown_query": {
                        "type": "string",
                        "description": "Users' questions that are not related to ALAT and Cognitive search information in relating to  e.g what is today's date,",
                    },
                },
                "required": ["unknown_query"],
            },
        }
    },

 {
        "type": "function",
        "function": {
            "name": "top_up_airtime",
            "description": "This tool should be used to purchase airtime",
            "parameters": {
                "type": "object",
                "properties": {
                    "service_provider": {
                        "type": "string",
                        "description": "This parameter takes in the service provider you would like to buy airtime from, it returns an error if the service provider is not available",
                    },

                    "amount": {
                        "type": "string",
                        "description": "This parameter takes in the amount of airtime the user would like to buy",
                    },

                },
                "required": ["service_provider","amount"],
            },
        }
 }
    
    ]










