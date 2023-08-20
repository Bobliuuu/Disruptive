import streamlit as st

# Conversion function from USD to ETH
def usd_to_eth(usd_amount):
    eth_to_usd_rate = 1671.74 
    eth_amount = usd_amount / eth_to_usd_rate
    return eth_amount

def main():
    bounty_name = st.experimental_get_query_params().get("bounty_name", [None])[0]
    st.title(f"Fund {bounty_name}")

    st.header("Available Bounties")

    usd_bounty_amount = 100000
    usd_bounty_amount_2 = 10000
    eth_bounty_amount = usd_to_eth(usd_bounty_amount)
    st.subheader(f'{bounty_name}: Premium Bounty')
    st.write(f"Amount: {usd_bounty_amount} USD / {eth_bounty_amount:.2f} ETH")

    if st.button("Claim Bounty", key=1):
        st.success("Bounty claimed! Logging to Hedera Consensus System")
        st.info('Please enter your wallet address and Circle API key. A payment will be made through Circe\'s SDK.')
        st.text_input(label='Enter wallet address:')
        st.text_input(label='Enter Circle API key')
        if st.button('Create transaction intent and reciept.'):
            pass
    st.subheader(bounty_name)
    st.write(f"Amount: {usd_bounty_amount_2} USD / {eth_bounty_amount:.2f} ETH")

    if st.button("Claim Bounty", key=2):
        st.success("Bounty claimed! Logging to Hedera Consensus System")
        st.info('Please enter your wallet address and Circle API key. A payment will be made through Circe\'s SDK.')
        st.text_input(label='Enter wallet address:')
        st.text_input(label='Enter Circle API key')
        if st.button('Create transaction intent and reciept.'):
            pass

    st.subheader(bounty_name)
    st.write(f"Amount: {usd_bounty_amount_2} USD / {eth_bounty_amount:.2f} ETH")

    if st.button("Claim Bounty", key=3):
        st.success("Bounty claimed! Logging to Hedera Consensus System")
        st.info('Please enter your wallet address and Circle API key. A payment will be made through Circe\'s SDK.')
        st.text_input(label='Enter wallet address:')
        st.text_input(label='Enter Circle API key')
        if st.button('Create transaction intent and reciept.'):
            pass

if __name__ == "__main__":
    main()