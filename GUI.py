import streamlit as st
import numpy as np
import pickle
import mysql.connector as mysql

# mysql --port 3307 -u root -p ~ cmd command
# StorageDBS@root

st.set_page_config(
    page_title="PCOS Suggestion",
    page_icon=":page_facing_up:",
    layout="wide"
)

mydb = mysql.connect(
    host="localhost", user="root", passwd="StorageDBS@root", database="monamie", port=3307
)

st.sidebar.header("Project Navigation")

user = "2019nupur.jeswani@ves.ac.in"

PCOS_selectbox = st.sidebar.selectbox(
    "Run project using - ",
    ("Select any one process", "PCOS Suggestion", "PCOS Tracking")
)

with open('Ensembler.pkl', 'rb') as f:
    clf = pickle.load(f)


if PCOS_selectbox == "PCOS Suggestion":

    st.header("PCOS Suggestion using Logistic Regression")
    st.markdown("---")

    age_input = st.number_input("Enter your age")
    weight_input = st.number_input("Enter your weight")
    height_input = st.number_input("Enter your height")
    bmi_input = (weight_input/((height_input)*(height_input)))*10000
    st.write(f"Your BMI is {bmi_input}")
    pulse_rate_input = st.number_input("Enter your pulse rate")
    rr_breaths_input = st.number_input(
        "Enter your respiration rate (breaths per minute)")
    cycle_length_input = st.number_input(
        "Enter the number of days your periods last")
    marraige_status_input = st.number_input(
        "Enter your marraige status in years")
    pregnant_input = st.number_input("Are you pregnant at the moment?")
    no_of_abortions = st.number_input("Total number of abortions")
    hip_input = st.number_input("Enter your hip size in inches")
    waist_input = st.number_input("Enter your waist size in inches")
    waist_hip_ratio_input = waist_input / hip_input
    st.write("Your waist to hip ratio is " + str(waist_hip_ratio_input))
    weight_gain_input = st.number_input("Amount of weight gain")
    hair_growth_input = st.number_input(
        "Is your hair growing at a normal rate?")
    skin_darkening_input = st.number_input("Any skin darkening?")
    hair_loss_input = st.number_input(
        "Are you experiencing excessive hair loss?")
    pimples_input = st.number_input("Do you have excessive pimples?")
    fast_food_input = st.number_input("Are you having excessive fast food?")
    reg_exercise_input = st.number_input("Are you exercising regularly?")

    input = []
    input.append(age_input)
    input.append(weight_input)
    input.append(height_input)
    input.append(bmi_input)
    input.append(pulse_rate_input)
    input.append(rr_breaths_input)
    input.append(cycle_length_input)
    input.append(marraige_status_input)
    input.append(pregnant_input)
    input.append(no_of_abortions)
    input.append(hip_input)
    input.append(waist_input)
    input.append(waist_hip_ratio_input)
    input.append(weight_gain_input)
    input.append(hair_growth_input)
    input.append(skin_darkening_input)
    input.append(hair_loss_input)
    input.append(pimples_input)
    input.append(fast_food_input)
    input.append(reg_exercise_input)

    arr_input = np.array([input])

    if st.button("Start Detection"):
        ans = clf.predict(arr_input)
        st.write(f'Prediction result for the message {input}:', ans)


if PCOS_selectbox == "PCOS Tracking":
    st.header("PCOS Record keeper")
    st.markdown("---")

    st.markdown(
        "First select the month and year you are making this entry for - ")
    year = st.selectbox('Year', range(1990, 2024))
    month = st.selectbox('Month', ("January", "February", "March", "April", "May",
                         "June", "July", "August", "September", "October", "November", "December"))
    st.markdown("---")

    st.markdown(
        "Start filling out these questions according to the report given to you by your doctor - ")

    left, right = st.columns(2)

    with left:
        age_input = st.number_input("Enter your age")
        weight_input = st.number_input("Enter your weight")
        height_input = st.number_input("Enter your height")
        bmi_input = st.number_input(
            "Enter your BMI (Body Mass Index). Formula to calculate BMI - Weight in kgs divided by the square of height in meters or feet")
        blood_group_input = st.text_input("Enter your blood group")
        pulse_rate_input = st.number_input("Enter your pulse rate")
        rr_breaths_input = st.number_input(
            "Enter your respiration rate (breaths per minute)")
        hb_input = st.number_input("Enter your haemoglobin count")
        cycle_regularity_irregularity = st.number_input(
            "Tell us whether your cycles are regular or irregular (2 stands for regular and 4 stands for irregular)")
        cycle_length_input = st.number_input(
            "Enter the number of days your periods last")
        marriage_status_input = st.number_input(
            "Enter your marraige status in years")
        pregnant_input = st.number_input("Are you pregnant at the moment?")
        no_of_abortions = st.number_input("Total number of abortions")
        I_betaHCG = st.number_input("Enter your HCG count I (in (mIU/mL))")
        II_betaHCG = st.number_input("Enter your HCG count II (in (mIU/mL))")
        fsh = st.number_input(
            "Enter your FSH count (Follicle Stimulating hormone (in (mIU/mL))")
        lh = st.number_input(
            "Enter your LH count (Luteinizing hormone (in (mIU/mL))")
        fshlh = st.number_input("Enter your FSH/LH ratio")
        hip_input = st.number_input("Enter your hip size in inches")
        waist_input = st.number_input("Enter your waist size in inches")
        waist_hip_ratio_input = st.number_input(
            "Enter your waist to hip ratio. ")

    with right:
        tsh = st.number_input(
            "Enter your TSH count (Thyroid stimulating hormone (in mIU/L))")
        amh = st.number_input(
            "Enter your AMH count (anti-müllerian hormone (in ng/mL))")
        prl = st.number_input(
            "Enter your PRL levels (prolactin levels (in ng/mL))")
        vit_D3 = st.number_input("Enter your Vitamin D3 value (in ng/mL)")
        prg = st.number_input("Enter your progesterone count (in ng/mL)")
        rbs = st.number_input(
            "Enter your Random blood sugar value (in mg/dl))")
        weight_gain_input = st.number_input("Amount of weight gain")
        hair_growth_input = st.number_input(
            "Is your hair growing at a normal rate?")
        skin_darkening_input = st.number_input("Any skin darkening?")
        hair_loss_input = st.number_input(
            "Are you experiencing excessive hair loss?")
        pimples_input = st.number_input("Do you have excessive pimples?")
        fast_food_input = st.number_input(
            "Are you having excessive fast food?")
        reg_exercise_input = st.number_input("Are you exercising regularly?")
        BP_Systolic = st.number_input("Enter your Systolic BP value (in mmHg)")
        BP_Diastolic = st.number_input(
            "Enter your Diastolic BP value (in mmHg)")
        left_follicle_count = st.number_input("Enter your left follicle count")
        right_follicle_count = st.number_input(
            "Enter your right follicle count")
        left_avg_follicle_size = st.number_input(
            "Enter your average follicle size (left)(in mm)")
        right_avg_follicle_size = st.number_input(
            "Enter your average follicle size (right)(in mm)")
        endometrium_size = st.number_input(
            "Enter the size of your endometrium layer (in mm)")

    doctor_remark = st.text_area(
        "Any remarks from the doctor that you want to store - ")

    if st.button(f"Store this entry for the time {year, month}"):
        mycursor = mydb.cursor()
        sql = "INSERT INTO pcos_records(userID, yearentry, monthentry, age, weight, height, bmi,  bloodgroup,  pulse_rate,  rr_breaths, haemoglobin, cycle_r_i, cycle_length, marriage_status, pregnancy_status, abortions_count,  betaHCGI,betaHCGII,  FSH,  LH, FSH_LH, hip_size, waist_size, waist_hip_ratio, TSH, AMH, PRL, Vit_D3, PRG, RBS, weight_gain, hair_growth, skin_darkening, hair_loss, pimples, fast_food, regular_exercise, BP_systolic, BP_diastolic, left_follicle_count, right_follicle_count,  left_follicle_avg_size, right_follicle_avg_size,  endometrium_size, doctor_remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user, year, month, age_input, weight_input, height_input, bmi_input, blood_group_input, pulse_rate_input, rr_breaths_input, hb_input, cycle_regularity_irregularity, cycle_length_input, marriage_status_input, pregnant_input, no_of_abortions, I_betaHCG, II_betaHCG, fsh, lh, fshlh, hip_input, waist_input, waist_hip_ratio_input,
               tsh, amh, prl, vit_D3, prg, rbs, weight_gain_input, hair_growth_input, skin_darkening_input, hair_loss_input, pimples_input, fast_food_input, reg_exercise_input, BP_Systolic, BP_Diastolic, left_follicle_count, right_follicle_count, left_avg_follicle_size, right_avg_follicle_size, endometrium_size, doctor_remark)
        mycursor.execute(sql, val)
        mydb.commit()

    st.markdown("---")


# verified

# %s, %f, %f, %f, %f, %f, %f, %s, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %s

# code						    sql table
# 						        recordID
# 						        userID
# year						    yearentry
# month  					    monthentry
# age_input  					age
# weight_input				    weight
# height_input				    height
# bmi_input					    bmi
# blood_group_input			    bloodgroup
# pulse_rate_input				pulse_rate
# rr_breaths_input				rr_breaths
# hb_input					    haemoglobin
# cycle_regularity_irregularity	cycle_r_i
# cycle_length_input			cycle_length
# marriage_status_input			marriage_status
# pregnant_input				pregnancy_status
# no_of_abortions				abortions_count
# I_betaHCG					    betaHCGI
# II_betaHCG					betaHCGII
# fsh						    FSH
# lh						    LH
# fshlh						    FSH_LH
# hip_input					    hip_size
# waist_input					waist_size
# waist_hip_ratio_input			waist_hip_ratio
# tsh						    TSH
# amh						    AMH
# prl						    PRL
# vit_D3					    Vit_D3
# prg						    PRG
# rbs						    RBS
# weight_gain_input				weight_gain
# hair_growth_input				hair_growth
# skin_darkening_input			skin_darkening
# hair_loss_input				hair_loss
# pimples_input				    pimples
# fast_food_input				fast_food
# reg_exercise_input			regular_exercise
# BP_Systolic					BP_systolic
# BP_Diastolic				    BP_diastolic
# left_follicle_count			left_follicle_count
# right_follicle_count			right_follicle_count
# left_avg_follicle_size		left_follicle_avg_size
# right_avg_follicle_size		right_follicle_avg_size
# endometrium_size				endometrium_size
# doctor_remark				    doctor_remarks


# 2+21+20+1 = 44
