import streamlit as st

def main():
    st.title("☀️ Solar Charging Helper")

    st.subheader("1. Sunlight Detection")
    lux = st.slider("Enter sunlight level (lux)", min_value=0, max_value=120000, value=10000)
    
    if lux < 10000:
        st.warning("Not enough sunlight. Try to reposition the solar panel.")
    elif lux < 30000:
        st.info("Moderate sunlight. Charging may be slow.")
    else:
        st.success("Good sunlight! Ideal for charging.")

    st.subheader("2. Suggested Panel Tilt Angle")
    st.text("Recommended angle based on general location: 45°")

    st.subheader("3. Charging Speed (Simulated)")
    if lux < 10000:
        st.text("Charging speed: ⚡ Very slow")
    elif lux < 30000:
        st.text("Charging speed: ⚡⚡ Medium")
    else:
        st.text("Charging speed: ⚡⚡⚡ Fast")

if __name__ == "__main__":
    main()
