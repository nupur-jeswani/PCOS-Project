create database monamie;

use monamie;

create table users (
	userID varchar(255) not null, 
    primary key(userID)
);

show tables;

insert into users values("2019nupur.jeswani@ves.ac.in");

select * from users;

create table pcos_records (
	recordID int auto_increment,
    userID varchar(255) not null,
	yearentry double not null,
    monthentry varchar(40) not null,
    age double not null,
    weight double not null,
    height double not null, 
    bmi double not null,
    bloodgroup varchar(255) not null,
    pulse_rate double not null,
    rr_breaths double not null,
    haemoglobin double not null,
    cycle_r_i double not null,
    cycle_length double not null,
    marriage_status double not null,
    pregnancy_status double not null,
    abortions_count double not null,
    betaHCGI double not null,
    betaHCGII double not null,
    FSH double not null,
    LH double not null,
    FSH_LH double not null,
    hip_size double not null,
    waist_size double not null,
    waist_hip_ratio double not null,
    TSH double not null,
    AMH double not null,
    PRL double not null,
    Vit_D3 double not null,
    PRG double not null,
    RBS double not null,
    weight_gain double not null,
    hair_growth double not null,
    skin_darkening double not null,
    hair_loss double not null,
    pimples double not null,
    fast_food double not null,
    regular_exercise double not null,
    BP_systolic double not null,
    BP_diastolic double not null,
    left_follicle_count double not null,
    right_follicle_count double not null,
    left_follicle_avg_size double not null,
    right_follicle_avg_size double not null,
    endometrium_size double not null,
    doctor_remarks varchar(455) not null,
    primary key(recordID)
);

drop table pcos_records;

show tables;

select * from pcos_records;