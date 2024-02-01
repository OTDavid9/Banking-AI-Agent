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
    ]










