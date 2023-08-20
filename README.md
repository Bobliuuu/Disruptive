# Disruptive: Disrupting the Business Market
Disruptive is an insight and funding DAO platform for new and veteran investors to seek out data, insights, and connections related to everything from micro acquisitions to series A portfolios. 

## Inspiration
Many investors looking to invest in startup companies are often overwhelmed by the sheer number of investment opportunities, worried that they will miss promising ventures without doing adequate due diligence. Likewise, since startups all present their data in a unique way, it is challenging for investors to directly compare companies and effectively evaluate potential investments.  On the other hand, thousands of startups with a lot of potential also lack visibility to the right investors. Thus, we came up with Disruptive as a way to bridge this gap and provide a database for investors to view important insights about startups tailored to a specific criteria.

## What it does
Disruptive scrapes information from various sources: company websites, LinkedIn, news, and social media platforms to generate the newest possible market insights. After homepage authentication, investors are prompted to indicate their interest in either Pre/Post+ seed companies to invest in. When an option is selected, the investor is directed to a database of company data with search capabilities. From the results table, a company can be selected and the investor will be able to view company insights, business analyst data (graphs), fund companies, and a Streamlit Chatbot interface. The investor also has the option of adding a company to the database, as well as a company pitch if they selected the pre-seed option.

## How we built it
The frontend was built with Next.js, TypeScript, and Tailwind CSS. Firebase authentication was used to verify users from the home page. (Company scraping and proxies for company information) Selenium was used for web scraping for database information. Figma was used for design, authentication was done using Firebase. 
The backend was built using Flask, StreamLit, and Taipy. We used the Circle API and Hedera to generate bounties using blockchain. SQL and graphQL were used to generate insights, OpenAI and QLoRa were used for semantic/similarity search, and GPT fine-tuning was used for few-shot prompting.

## Challenges we ran into
Having never worked with Selenium and web scraping, we found understanding the dynamic loading and retrieval of web content challenging. The measures some websites have against scraping were also interesting to learn and try to work around. We also worked with chat-GPT and did prompt engineering to generate business insights - a task that can sometimes yield unexpected responses from chat-GPT!

## Accomplishments that we're proud of + What we learned
We learned how to use a lot of new technology during this hackathon. As mentioned above, we learned how to use Selenium, as well as Firebase authentication and GPT fine-tuning.

## What's next for Disruptive
Disruptive can implement more scrapers for better data in terms of insight generation. This would involve scraping from other options than Golden once there is more funding. Furthermore, integration between frontend and blockchain can be improved further.
