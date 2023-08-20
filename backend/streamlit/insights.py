import streamlit as st
import random

# Function to display company insights
def display_company_insights(name):
    year_founded = 1990
    industry = "Technology"
    country = "USA"
    employee_count = 1000
    description = """Twitter is a widely-used social media platform that allows users to share short messages, or "tweets," consisting of up to 280 characters. It serves as a real-time communication tool, enabling individuals, organizations, and celebrities to share thoughts, news, links, and multimedia content with their followers. Users can engage through retweets, likes, and replies, fostering rapid information dissemination and conversation on a wide range of topics."""
    funding_round = "Series A"

    st.write(f"**Company Name:** {name}")
    st.write(f"**Year Founded:** {year_founded}")
    st.write(f"**Industry:** {industry}")
    st.write(f"**Country:** {country}")
    st.write(f"**Employee Count:** {employee_count}")
    st.write(f"**Description:** {description}")
    st.write(f"**Funding Round:** {funding_round}")
    st.write("GPT Generated Insights:")
    st.write(f"Twitter's funding prospects appear promising, supported by its enduring user base and strategic importance. The platform's real-time communication capabilities have solidified its position in the digital realm, increasing its appeal to potential investors. Furthermore, Twitter's growth potential remains robust as it continues to diversify its offerings with features like Spaces and ventures into e-commerce integration. These endeavors align with evolving user trends and could contribute to its sustained expansion in the dynamic social media landscape.")
    st.button('Fund this company')
    st.button('Contact company')
    st.button('Chat with this company or view advanced insights')

# Function to display line graphs
def display_line_graphs():
    st.write("**Projected MAV Growth**")
    data = [random.randint(1, 100) for _ in range(10)]
    st.line_chart(data)

# Function to display news widget
def display_news_widget():
    st.write("**News**")
    
    news_sources = ["Twitter", "Reddit", "News"]
    for source in news_sources:
        st.subheader(source)
        st.image("avif.png", width=300)
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget.")
        st.image("avif.png", width=300)
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget.")

# Main Streamlit app
def main():
    st.title("Company Insights App")

    # Get query parameters
    query_params = st.experimental_get_query_params()
    company_name = query_params.get("name", ["Twitter"])[0]

    # Display company insights
    display_company_insights(company_name)

    # Display description and funding round
    st.write("---")
    display_line_graphs()

    # Display line graphs
    st.write("---")
    display_news_widget()

    st.write('')

if __name__ == "__main__":
    main()
