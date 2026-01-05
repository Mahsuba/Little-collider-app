import streamlit as st
import random

#Let's put some CERN fun facts 
CERN_FUN_FACTS = [
    "CERN runs the Large Hadron Collider, a 27 km circular machine.",
    "Particles in the LHC move almost as fast as light.",
    "The World Wide Web was invented at CERN.",
    "Scientists smash particles to learn how the universe works.",
    "The LHC is underground and crosses two countries!",
    "Huge detectors record what happens after particle collisions."
]


# Let's make it wide screen
st.set_page_config(page_title="Little Collider", layout="wide")


# PAGES 


def home_page():
    import streamlit as st

    # Title
    st.title("🔬 Little Collider")

    # Welcome note
    st.markdown("**Welcome, Junior Scientist!** 👋")
    st.write(
        "Have you ever wondered what the universe is made of? "
        "At CERN, scientists explore this by smashing tiny particles together."
    )

    # We need to give a disclaimer haha.
    st.caption("This is a fun learning toy — not a real CERN simulation.")

    st.write("")

    # explanation
    st.write(
        "CERN is a giant science laboratory in Europe. "
        "Inside a huge underground tunnel called the **Large Hadron Collider (LHC)**, "
        "particles zoom around almost as fast as light!"
    )
    st.write(
        "When they collide, scientists learn secrets about matter, energy, and the universe."
    )

    st.write("")

    # What kids will do
    st.subheader("✨ What You Can Explore")
    st.write("🔹 **Energy Explorer** — Change energy and see what happens.")
    st.write("🔹 **Collision Lab** — Watch particles crash in the middle.")
    st.write("🔹 **Quiz Time** — Test what you learned.")

    st.write("")

    # Start button
    if st.button("🚀 Start Exploring"):
        st.success("Open the menu on the left and begin your science adventure!")
    st.caption("Inspired by CERN outreach and open science education.")
    



def energy_explorer_page():
    import streamlit as st
    from pathlib import Path

    st.title("Energy Explorer")
    st.write(
        "Move the slider to give particles a push! ⚡ Watch what appears and learn about it."
    )

    # 3 columns: slider , info , image
    col_slider, col_info, col_img = st.columns([1.2, 1.6, 1.2], gap="small")

    # image loader
    def show_particle_image(path_str: str, caption: str):
        path = Path(path_str)
        if path.exists():
            st.image(str(path), caption=caption, width="stretch")
        else:
            st.warning(f"Image not found: `{path_str}`")
            st.caption("Tip: Check your assets folder filenames.")

   
    # Slider / Energy input
    
    with col_slider:
        st.subheader("Energy Slider")
        energy = st.slider("How much energy to give the particle?", 0, 100, 20, 1)

        st.info(
            "Think of this like a particle race! 🏎️💨\n"
            "Particles are already inside the collider. "
            "The slider shows how much energy we give them to zoom. "
            "Low energy lets tiny, common particles appear (like photons). "
            "High energy can reveal heavier or rarer particles. "
           
        )

   
    # Determine particle based on energy
    
    if energy < 20:
        particle = "Photon"
        mass_level = "Very light"
        rarity = "Very common"
        meaning = (
            "Photons are packets of light. Low energy shows only these tiny, fast particles."
        )
        img_path = "assets/photon.png.png"
        color = "gold"

    elif energy < 40:
        particle = "Electron"
        mass_level = "Light"
        rarity = "Common"
        meaning = (
            "Electrons are found in atoms. With more energy, we can see them in our toy model."
        )
        img_path = "assets/electron.png.png"
        color = "deepskyblue"

    elif energy < 60:
        particle = "Muon"
        mass_level = "Heavier than an electron"
        rarity = "Less common"
        meaning = (
            "Muons are like heavier cousins of electrons. Medium energy lets them appear."
        )
        img_path = "assets/muon.png.png"
        color = "orange"

    elif energy < 80:
        particle = "Pion"
        mass_level = "Medium"
        rarity = "Less common"
        meaning = (
            "Pions are short-lived particles. They can appear when particles collide at medium energy."

        )
        img_path = "assets/pion.png.png"
        color = "purple"

    else:
        particle = "Rare New Particle (toy)"
        mass_level = "Very heavy (toy)"
        rarity = "Very rare"
        meaning = (
            "At extreme energy, rare particles can appear. Detectors record their signals carefully!"
        )
        img_path = "assets/rare.png"
        color = "red"

    
    # Visual circle for fun
    
    with col_slider:
        st.markdown("**Particle Visual:**")
        size_px = int(40 + (energy / 100) * 110)  # 40px -> 150px

        st.markdown(
            f"""
            <div style="
                width:{size_px}px;
                height:{size_px}px;
                background:{color};
                border-radius:50%;
                margin-top:10px;
                margin-bottom:6px;
            "></div>
            """,
            unsafe_allow_html=True
        )
        st.caption(
            "Energy is like a push. The circle shows which particle appears — bigger = rarer!"
        )

    # Info column
    
    with col_info:
        st.subheader("Particle Info")
        st.markdown(f"**Energy level:** {energy}/100")
        st.markdown(f"**Particle:** {particle}")
        st.markdown(f"**Mass level:** {mass_level}")
        st.markdown(f"**Rarity:** {rarity}")
        st.info(meaning)


    # Image column
    
    with col_img:
        st.subheader("Particle Image")
        show_particle_image(img_path, particle)



def collider_run_page():
    import streamlit as st
    import matplotlib.pyplot as plt
    import time

    
    # Title & intro
    
    st.title("🚀 Collider Run")
    st.write(
        "Watch a particle zoom along a collider beam! "
        "In this toy model, higher energy makes the particle move faster on screen. "
        "In real colliders, energy is also used to create heavier particles."
    )
    st.caption("This is a toy model for learning about particle motion.")

    
    # Controls
    
    energy = st.slider(
        "⚡ Beam Energy",
        min_value=0,
        max_value=100,
        value=30,
        step=1
    )

    st.markdown(f"**Beam Speed (toy):** `{0.005 + (energy / 100) * 0.03:.3f}`")

    col1, col2, col3 = st.columns([1, 1, 2], gap="small")

    
    # Session state initialization
    
    st.session_state.setdefault("running", False)
    st.session_state.setdefault("x_pos", 0.05)
    st.session_state.setdefault("completed", False)

    
    # Buttons
    
    if col1.button("▶ Start"):
        st.session_state.running = True
        st.session_state.completed = False

    if col2.button("⏹ Stop"):
        st.session_state.running = False

    if col3.button("↩ Reset"):
        st.session_state.x_pos = 0.05
        st.session_state.running = False
        st.session_state.completed = False

    
    # Speed calculation
    
    speed = 0.005 + (energy / 100) * 0.03

    
    # Update position
    
    if st.session_state.running:
        st.session_state.x_pos += speed
        if st.session_state.x_pos >= 0.95:
            st.session_state.x_pos = 0.95
            st.session_state.running = False
            st.session_state.completed = True

    
    # Draw particle + beam
    
    fig, ax = plt.subplots(figsize=(7, 1.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Beam line
    ax.plot([0.02, 0.98], [0.5, 0.5], linewidth=5, color="gray", alpha=0.5)

    # Particle
    ax.add_patch(plt.Circle((st.session_state.x_pos, 0.5), 0.05, color="deepskyblue"))

    
    if st.session_state.completed:
        ax.add_patch(plt.Circle((0.95, 0.5), 0.07, color="gold", alpha=0.8))

    st.pyplot(fig, width="stretch")

    
    # Result 
    
    if st.session_state.completed:
        st.success("🎉 Particle reached the end! Well done!")
        st.balloons()
    else:
        st.info("Press **Start** to see the particle zoom across the beam!")

    
    # Smooth animation loop
    
    if st.session_state.running:
        time.sleep(0.03)
        st.rerun()




def collision_lab_page():
    import streamlit as st
    import matplotlib.pyplot as plt
    import time

    
    # Title & intro
    
    st.title("💥 Collision Lab")
    st.write("Two particle beams race toward each other and collide at the center.")
    st.caption(
    "In this toy model, higher energy makes the particles move faster on screen. "
    "In real colliders, energy is also used to create heavier particles."
)

    st.write(
    "In this lab, you control how much energy the particles have when they crash. "
    "Watch what happens when they collide — sometimes they bounce, sometimes they create new particles! "
    "It’s a safe way to explore how tiny particles behave in a collider."
)

    st.write("🎯 Try different energies and see what happens when particles collide!")

    
    # Controls
    
    energy = st.slider(
        "⚡ Collision Energy",
        min_value=0,
        max_value=100,
        value=40,
        step=1
    )

    st.caption("Higher energy → faster motion and more exciting outcomes (toy logic).")

    col1, col2, col3 = st.columns(3)

    
    # Session state initialization
    
    st.session_state.setdefault("running", False)
    st.session_state.setdefault("x_left", 0.1)
    st.session_state.setdefault("x_right", 0.9)
    st.session_state.setdefault("collided", False)
    st.session_state.setdefault("celebrated", False)

    
    # Buttons
    
    if col1.button("▶ Start"):
        st.session_state.running = True

    if col2.button("⏸ Stop"):
        st.session_state.running = False

    if col3.button("↩ Reset"):
        st.session_state.running = False
        st.session_state.x_left = 0.1
        st.session_state.x_right = 0.9
        st.session_state.collided = False
        st.session_state.celebrated = False

    
    # Speed calculation 
    
    speed = 0.002 + (energy / 100) * 0.015
    st.markdown(f"**🚀 Beam Speed (toy):** `{speed:.4f}`")

    
    # Motion update
    
    if st.session_state.running and not st.session_state.collided:
        st.session_state.x_left += speed
        st.session_state.x_right -= speed

    
    # Collision detection
    
    if (
        not st.session_state.collided
        and st.session_state.x_left >= 0.47
        and st.session_state.x_right <= 0.53
    ):
        st.session_state.collided = True
        st.session_state.running = False

    
    # Drawing area
    
    fig, ax = plt.subplots(figsize=(7.5, 2.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Beam line
    ax.plot([0.05, 0.95], [0.5, 0.5], linewidth=4)

    # Particles
    ax.add_patch(plt.Circle((st.session_state.x_left, 0.5), 0.04, color="deepskyblue"))
    ax.add_patch(plt.Circle((st.session_state.x_right, 0.5), 0.04, color="orange"))

    # Collision flash
    if st.session_state.collided:
        ax.add_patch(plt.Circle((0.5, 0.5), 0.065, color="gold", alpha=0.9))

    st.pyplot(fig, width="stretch")

    
    # Collision result
    
    st.markdown("---")
    st.subheader("🧪 Collision Result")

    if st.session_state.collided:
        if not st.session_state.celebrated:
            st.balloons()
            st.session_state.celebrated = True

        if energy < 40:
            st.info("🟦 Scatter Event")
            st.write(
                "At low energy, particles usually bounce away from each other "
                "without creating new particles."
            )

        elif energy < 75:
            st.success("🟣 New Particle Created: Pion (toy)")
            st.write(
                "With medium energy, collisions can create short-lived particles "
                "like pions."
            )

        else:
            st.warning("⭐ Rare Event Detected")
            st.write(
                "At very high energy, rare events can happen. "
                "Scientists search carefully for these special signals at CERN."
            )
    else:
        st.write("Press **Start** to begin the collision.")

    
    # Smooth animation loop
    
    if st.session_state.running:
        time.sleep(0.025)
        st.rerun()


def quiz_page():
    import streamlit as st

    st.title("🧠 Quiz: Junior Collider Scientist")
    st.caption("7 questions • No time limit • Just for learning")

    st.write("Answer the questions below and see how much you’ve learned!")
    st.info("Tip: Read carefully. Some questions test honesty in science outreach.")

    
    # Questions (MCQ)
    
    q1 = st.radio(
        "1) If beam energy increases, what usually becomes possible?",
        [
            "Only lighter particles can be created",
            "Heavier and rarer particles can become possible",
            "Energy has no effect on collisions",
            "Particles disappear"
        ],
        index=None
    )

    q2 = st.radio(
        "2) Which particle is heavier?",
        [
            "Electron",
            "Muon"
        ],
        index=None
    )

    q3 = st.radio(
        "3) What do detectors do in a collider experiment?",
        [
            "They make particles move faster",
            "They record signals so scientists can understand what happened",
            "They paint particles different colors",
            "They stop time"
        ],
        index=None
    )

    q4 = st.radio(
        "4) In the Collision Lab toy outcomes, what can happen at medium energy?",
        [
            "Nothing ever changes",
            "A new particle such as a pion (toy example)",
            "The Earth’s gravity turns off",
            "All particles become photons"
        ],
        index=None
    )

    q5 = st.radio(
        "5) Is this app a real CERN-level physics simulation?",
        [
            "Yes, it is fully accurate and identical to CERN software",
            "No, it is a simplified educational toy model"
        ],
        index=None
    )

    q6 = st.radio(
        "6) Why do scientists care about rare events?",
        [
            "Rare events are always mistakes",
            "Rare events can help discover new or special particles",
            "Rare events are banned at CERN",
            "Rare events are the same as common events"
        ],
        index=None
    )

    q7 = st.radio(
        "7) If energy is low, what is the most likely toy outcome after a collision?",
        [
            "Scatter (particles bounce away)",
            "Rare Higgs-like event every time",
            "Instant black hole",
            "Time travel"
        ],
        index=None
    )

    
    # Scoring
    
    answer_key = {
        "q1": "Heavier and rarer particles can become possible",
        "q2": "Muon",
        "q3": "They record signals so scientists can understand what happened",
        "q4": "A new particle such as a pion (toy example)",
        "q5": "No, it is a simplified educational toy model",
        "q6": "Rare events can help discover new or special particles",
        "q7": "Scatter (particles bounce away)"
    }

    user_answers = {
        "q1": q1, "q2": q2, "q3": q3,
        "q4": q4, "q5": q5, "q6": q6, "q7": q7
    }

    st.markdown("---")

    if st.button("✅ Submit Quiz"):
        # Check unanswered questions
        unanswered = [k for k, v in user_answers.items() if v is None]
        if unanswered:
            st.warning("Please answer all questions before submitting 😊")
            return

        score = 0
        total = len(answer_key)

        for k in answer_key:
            if user_answers[k] == answer_key[k]:
                score += 1

        st.subheader("🎉 Your Score")
        st.write(f"**{score} / {total}**")

        if score == total:
            st.success("Excellent! You really think like a young scientist 👏")
            st.balloons()
        elif score >= total - 2:
            st.success("Great job! Just a little review and you’re perfect 👍")
        else:
            st.info("Nice try! Review the app and try again — learning takes practice 💪")

        # Reinforcement
        st.markdown("### 🔍 Why these answers are correct")
        st.write("• Higher energy can allow heavier or rarer particles to appear.")
        st.write("• A Muon is much heavier than an electron.")
        st.write("• Detectors help scientists understand what happened during a collision.")
        st.write("• This app is a learning toy, not a real CERN simulation.")
        st.write("• Rare events matter because they can reveal special particles or new ideas.")



def about_cern_page():
    import streamlit as st

    st.title("🧪 About CERN (For Curious Kids!)")

    st.write(
        "CERN is one of the coolest science places on Earth 🌍. "
        "Scientists from many different countries work together at CERN "
        "to understand what everything in the universe is made of."
    )

    st.markdown("## ⚛️ What happens at CERN?")

    st.write(
        "At CERN, scientists use a giant machine called the **Large Hadron Collider (LHC)**."
    )

    st.write("• It is a huge circular tunnel under the ground.")
    st.write("• Inside it, tiny particles are sent zooming almost as fast as light ⚡.")
    st.write(
        "• When these particles crash into each other, scientists learn new secrets "
        "about the universe 🌌."
    )

    st.write(
        "It’s like smashing LEGO pieces to see what’s inside — "
        "but much, much smaller!"
    )

    st.markdown("## 🔍 Why do scientists do this?")

    st.write("By studying these tiny crashes, scientists can:")
    st.write("• Learn how matter is made")
    st.write("• Understand how the universe began")
    st.write("• Discover new particles")
    st.write("• Build better technology for the future")

    st.write(
        "Some inventions inspired by CERN research even help doctors "
        "and computers today 💡."
    )

    st.markdown("## 🧠 Big experiments at CERN")

    st.write(
        "CERN has famous experiments with fun names. "
        "These experiments use huge detectors to watch and record particle collisions:"
    )

    st.markdown(
       "- **ATLAS** 🧲 — A giant camera that watches the biggest particle crashes\n"
       "- **CMS** 🔬 — A super detector that checks if new particles appear\n"
       "- **ALICE** 🌈 — Studies super-hot matter, like the early universe\n"
       "- **LHCb** 🧪 — Looks for tiny differences to understand why matter exists"
    )

    st.markdown("## 🎮 About this app")

    st.info(
        "This app is **not a real collider**. "
        "It is a toy educational app made to help kids:"
    )

    st.write("• Learn what energy is")
    st.write("• Understand particles")
    st.write("• Imagine how collisions work")

    st.write(
        "Just like a flight simulator helps pilots learn, "
        "this app helps kids explore science safely and simply."
    )

    st.markdown("## ❤️ Why this app was made")

    st.success(
        "This app was built to show that big science ideas can be fun and easy to understand, "
        "especially for young learners."
    )

    st.write(
        "Science starts with curiosity — and curiosity starts with questions 😊."
    )

def lhc_page():
    import streamlit as st
    from pathlib import Path

    st.title("🌀 The Large Hadron Collider (LHC)")
    st.caption("Big machine • Tiny particles • Huge discoveries")

    st.write(
        "The **Large Hadron Collider**, or **LHC**, is the biggest science machine on Earth. "
        "It helps scientists learn what the universe is made of — by smashing very tiny particles together."
    )

    st.write("")

    
    # What is the LHC?
    
    st.subheader("🔍 What is the LHC?")
    st.write(
        "The LHC is a **giant circular tunnel underground**. "
        "Inside it, particles race around and crash into each other."
    )
    st.write(
        "These particles are so small that we cannot see them, "
        "but special detectors act like super cameras."
    )

    
    # Map Image
    
    st.markdown("### 🗺️ Where is it?")
    st.write(
        "The LHC is buried underground near Geneva, Switzerland. "
        "It even goes under **two countries**!"
    )

    map_path = Path("assets/lhs1.png")
    if map_path.exists():
        st.image(str(map_path), caption="Map of the LHC tunnel (not to scale)", width="stretch")
    else:
        st.warning("LHC map image not found (lhs1).")

    
    # Why was it made?
    
    st.subheader("❓ Why was the LHC built?")
    st.write("Scientists built the LHC to answer big questions like:")
    st.write("• What is everything made of?")
    st.write("• Why does matter exist?")
    st.write("• What happened just after the universe began?")

    st.write(
        "By studying tiny particle crashes, scientists can understand "
        "very big ideas about the universe."
    )

    
    # What can it do?
    
    st.subheader("⚡ What can the LHC do?")
    st.write(
        "The LHC can push particles to **almost the speed of light**."
    )
    st.write("When particles collide, the LHC can:")
    st.write("• Create new particles")
    st.write("• Study energy and matter")
    st.write("• Help test ideas in physics")

    st.info(
        "Important: Scientists do not control the universe here — "
        "they carefully measure tiny signals using detectors."
    )

    
    # Real LHC Photos
    
    st.subheader("📸 Inside the LHC")

    col1, col2, col3 = st.columns(3)

    with col1:
        img = Path("assets/lhs2.png")
        if img.exists():
            st.image(str(img), caption="Taking a closer look at LHC", width="stretch")
        else:
            st.warning("Image lhs2 not found.")

    with col2:
        img = Path("assets/lhs3.png")
        if img.exists():
            st.image(str(img), caption="LHC tunnel underground", width="stretch")
        else:
            st.warning("Image lhs3 not found.")

    with col3:
        img = Path("assets/lhs5.png")
        if img.exists():
            st.image(str(img), caption="Scientists working at the LHC",width="stretch")
        else:
            st.warning("Image lhs5 not found.")

    
    # wrap-up
    
    st.markdown("## 🌟 Why the LHC is amazing")
    st.success(
        "The LHC shows that humans can work together to explore the universe — "
        "using curiosity, teamwork, and science."
    )

    st.write(
        "Big machines help us answer big questions — "
        "and every scientist starts as a curious kid 😊."
    )
   



# SIDEBAR MENU (navigation)


st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Go to:",
    [
        "Home",
        "Energy Explorer",
        "Collider Run",
        "Collision Lab",
        "Quiz",
        "About CERN",
        "About the LHC"

    ]
)



# CERN Fun Fact (Sidebar)


st.sidebar.markdown("---")
st.sidebar.subheader("CERN Fun Fact")

# Create memory if it doesn't exist
if "cern_fact" not in st.session_state:
    st.session_state.cern_fact = "Click the button to learn something cool about CERN!"

# Button
if st.sidebar.button("🔄 New CERN Fun Fact"):
    st.session_state.cern_fact = random.choice(CERN_FUN_FACTS)

# Show the fact
st.sidebar.info(st.session_state.cern_fact)




# PAGE SWITCHING (magic isnt it?)


if page == "Home":
    home_page()

elif page == "Energy Explorer":
    energy_explorer_page()

elif page == "Collider Run":
    collider_run_page()

elif page == "Collision Lab":
    collision_lab_page()

elif page == "Quiz":
    quiz_page()

elif page == "About CERN":
    about_cern_page()
elif page == "About the LHC":
    lhc_page()


     
