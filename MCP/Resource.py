""" 
     => Resource is the data That AI can read 
        
         -> It does not perform an action like tool 
         -> Think like resource as information 
         
        
        -> Example 
        
        /docs/company_policy
        /logs/server_logs
        /config/settings
        /database/schema 
         
        -> Scenarion 
        
           Imagine a real life AI customer support system 
           
            docs/refund_policy
            docs/shipping_policy
            
            -> Tools 
               
               create_order()
               track_order()
               send_email()
               
               
               
               User asks refund question
                          ↓
            AI reads refund_policy resource
                          ↓
                 AI answers user  
                 
       => Resource Discovery

            Just like tools, resources can also be discovered.

              Client asks server:

             
             list_resources 
             
             
             
             
             Client
               ↓
          Discover resources
               ↓
         Choose resource
              ↓
          Read resource
              ↓
         Return data         
"""