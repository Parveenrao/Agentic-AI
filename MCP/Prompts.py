"""    => What Prompts Are in MCP

            -> A prompt is a reusable instruction template that helps guide the AI.

            -> Instead of writing the same instructions every time, you define them once.

T            -> hink of prompts like predefined AI tasks.


       -> Example prompts:

          summarize_document
          analyze_logs
          generate_report

       -> Why MCP Has Prompts

               -> Without prompts, the AI must receive long instructions every time.

                 Example without prompt:

                 "Please read this document carefully and produce a short summary highlighting the key points."

                  With MCP prompt:

                  summarize_document

                  The server already knows the instructions.

       -> Prompt Template Example

         Example prompt template:

         Summarize the following document:

         {{document}}

         When used:

         document = company_report.txt

         AI produces the summary.

     -> Prompt Discovery

         Just like tools and resources, prompts can be discovered.

               Client request:

               list_prompts

               Server response:

               summarize_document
               analyze_logs
               generate_report


              Now the AI knows what prompt templates exist.
         
           -> Prompt Usage Flow

             Typical flow:

             Client
               ↓
         Discover prompts
              ↓
          Choose prompt
              ↓
         Provide input
              ↓
        AI executes prompt

          Example:

           Prompt → summarize_document
           Input → report.txt

         Output:

         Short summary of the report




"""