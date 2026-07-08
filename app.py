import streamlit as st
from PIL import Image

# ============================================================
#  WORKED SOLUTION - app.py with all 6 modifications applied
#  Building Web Apps with Python and Streamlit
#
#  This is a FACILITATOR ANSWER KEY. It shows one correct way
#  to apply every modification challenge. Teachers will normally
#  apply only 2-3 modifications, not all six.
#
#  Each modification is marked with a banner comment so you can
#  quickly locate it while circulating.
# ============================================================


# ------------------------------------------------------------
#  MODIFICATION 4 (Functions) - Step 1
#  Functions are defined at the top, before they are called.
#  Syllabus: 2.3.13 (Functions), 2.3.14 (Local/Global Variables)
# ------------------------------------------------------------
def generate_greeting(name, gender):
    """Return a personalised greeting based on name and gender."""
    title = "Mr." if gender == "Male" else "Ms."   # 'title' is LOCAL to this function
    greeting = f"Welcome {title} {name.title()}!"
    return greeting


def get_level_description(level):
    """Return a word description for the numeric level."""
    descriptions = {
        1: "Beginner",
        2: "Elementary",
        3: "Intermediate",
        4: "Advanced",
        5: "Expert"
    }
    return descriptions[level]


# App title
st.title("Simple Streamlit Demo")

# Header and subheader
st.header("Welcome to My App")
st.subheader("An interactive Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is bold markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
# NOTE: requires a dog.jpg file in the same folder.
# If the file is missing, comment out the next two lines.
img = Image.open("dog.jpg")
st.image(img, width=200)


# ============================================================
#  MODIFICATION 6 (Dynamic UI with Loops) - Stretch
#  Replaces the original single checkbox (lines 25-27).
#  Creates multiple checkboxes from a list using a for loop.
#  Syllabus: 2.3.9 (Lists), 2.3.12 (Iteration)
# ============================================================
st.subheader("Select your skills")

skills = ["Python", "HTML", "Data Analysis", "AI", "Robotics"]
selected_skills = []  # empty list to collect selected skills

# Loop through the list to create one checkbox per skill
for skill in skills:
    if st.checkbox(skill):                 # creates a checkbox with the skill name
        selected_skills.append(skill)      # add to selected list if ticked

# Display results based on what was selected
if len(selected_skills) > 0:
    st.success(f"You selected {len(selected_skills)} skill(s):")
    for s in selected_skills:
        st.write(f"  - {s}")

    # Calculate and display a percentage
    percentage = round(len(selected_skills) / len(skills) * 100)
    st.metric("Skills coverage", f"{percentage}%")
else:
    st.warning("Please select at least one skill.")


# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])
# ------------------------------------------------------------
#  MODIFICATION 4 (Functions) - Step 2
#  The original if/else that printed the gender has been
#  replaced. The greeting is now produced by
#  generate_greeting() and displayed with the text input below.
# ------------------------------------------------------------


# ============================================================
#  MODIFICATION 1 (Lists and Loops) - Starter
#  MODIFICATION 2 (Dictionaries and Selection) - Starter
#
#  These two modifications both target the selectbox.
#  This solution COMBINES them: the hobby list comes from a
#  dictionary's keys, and selecting a hobby looks up a fun fact.
#  A multiselect + for loop is added below (Modification 1).
#  Syllabus: 2.3.9, 2.3.10, 2.3.11, 2.3.12
# ============================================================

# Dictionary mapping each hobby to a fun fact (Modification 2)
hobby_facts = {
    "Dancing": "Dancing burns about 300 calories per hour.",
    "Reading": "The average person reads 12 books a year.",
    "Sports": "Regular exercise improves memory by 20%.",
    "Gaming": "The global gaming industry is worth $180 billion.",
    "Cooking": "The world's oldest recipe is over 4,000 years old.",
    "Music": "Learning an instrument boosts memory and coordination.",
}

# Build the list of hobbies from the dictionary keys (Modification 1)
hobbies = list(hobby_facts.keys())

# Selectbox using the list of hobbies
hobby = st.selectbox("Select your main hobby:", hobbies)

# Look up the fun fact from the dictionary (Modification 2)
if hobby in hobby_facts:
    st.info(hobby_facts[hobby])
else:
    st.warning("No fun fact available for this hobby yet.")

# Multiselect + for loop to display multiple hobbies (Modification 1)
selected = st.multiselect("Pick all your hobbies:", hobbies)
if selected:
    st.write(f"You selected {len(selected)} hobbies:")
    for h in selected:
        st.write(f"  - {h}")
else:
    st.info("No extra hobbies selected yet.")


# Slider
level = st.slider("Choose a level", 1, 5)
# ------------------------------------------------------------
#  MODIFICATION 4 (Functions) - Step 3
#  The original st.write is replaced by a call to
#  get_level_description(), which returns a word for the number.
# ------------------------------------------------------------
st.write(f"Your level: {get_level_description(level)}")


# ============================================================
#  MODIFICATION 5 (Numeric Operations) - Intermediate
#  Adds a second slider and performs calculations with
#  conditional feedback.
#  Syllabus: 2.3.7 (Numeric Operations), 2.3.11 (Selection)
# ============================================================
hours = st.slider("Hours of practice per week", 1, 20, 5)

# Calculate totals using arithmetic operators
monthly = hours * 4           # multiplication
yearly = hours * 52           # multiplication
daily = round(hours / 7, 1)   # division and rounding
remaining = 500 - yearly      # subtraction

# Display the yearly total as a prominent metric
st.metric("Yearly Practice Hours", yearly)
st.write(f"That is about {daily} hours per day")
st.write(f"And about {monthly} hours per month")

# Conditional feedback based on the calculation
if yearly > 500:
    st.success(f"You are on track to mastery with {yearly} hours per year!")
elif yearly > 250:
    st.info(f"Good progress! {remaining} more hours to reach 500.")
else:
    st.warning(f"Keep going! You need {remaining} more hours to reach 500.")


# ============================================================
#  MODIFICATION 3 (String Methods) - Starter
#  MODIFICATION 4 (Functions) - Step 4
#
#  The text input now:
#   - validates the name (Modification 3)
#   - applies several string methods (Modification 3)
#   - uses generate_greeting() for the greeting (Modification 4)
#  Syllabus: 2.3.8 (Strings), 2.3.13 (Functions)
# ============================================================
name = st.text_input("Enter your name", "Type here...")

if st.button("Submit"):
    # Check if the user has typed a real name
    if name == "Type here..." or name == "":
        st.warning("Please enter your name first.")
    else:
        # Validate: check if name contains only letters and spaces (Modification 3)
        name_letters = name.replace(" ", "")
        if not name_letters.isalpha():
            st.error("Name should contain letters only!")
        else:
            # Greeting produced by the function (Modification 4)
            st.success(generate_greeting(name, gender))

            # String method results (Modification 3)
            st.write(f"Uppercase: {name.upper()}")
            st.write(f"Lowercase: {name.lower()}")
            st.write(f"Number of characters: {len(name)}")
            st.write(f"Your name reversed: {name[::-1]}")
            st.write(f"Starts with 'A': {name.upper().startswith('A')}")
