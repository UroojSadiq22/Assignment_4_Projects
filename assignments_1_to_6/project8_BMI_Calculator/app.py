import streamlit as st


st.title("BMI Calculator")
st.subheader("Calculate your Body Mass Index (BMI)")
st.markdown("This tool calculates your BMI based on the height and weight you enter.")

st.write("\t")

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI."""
    return weight / (height ** 2)


def get_bmi_category(bmi: float) -> str:
    """Determine BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Create a form for user input
with st.form(key='bmi_form'):
    st.write("Enter your details:")
    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (m)", min_value=0.0, format="%.2f")
    submit_button = st.form_submit_button(label='Calculate BMI')


# If the form is submitted, calculate and display the BMI
if submit_button:
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        st.success(f"Your BMI is: {bmi:.2f}")

        st.write("BMI Categories:")
        st.write("- Underweight: BMI < 18.5")
        st.write("- Normal weight: 18.5 <= BMI < 24.9")
        st.write("- Overweight: 25 <= BMI < 29.9")
        st.write("- Obesity: BMI >= 30")

        st.info(f"You are categorized as: {category}")
    else:
        st.error("Please enter valid weight and height values.")


# Add a footer to the app
st.write("\t")
st.markdown("---")
st.markdown("Created with ❤️ by Urooj Sadiq - [Connect on LinkedIn](https://www.linkedin.com/in/urooj-sadiq-a91031212/)")