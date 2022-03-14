import smtplib
# SMTP = simple mail transfer protocol

my_email = "job.ashish28@gmail.com"
password = "Ashish_28"
# before @, identity of user
# after @, identity of service provider


# METHOD 1
connection = smtplib.SMTP("smtp.gmail.com", port= 587)    # every email provider has a different smtp server... google it
connection.starttls()   # TLS = transport layer security... way of securing email to our email server
connection.login(user= my_email, password= password)
connection.sendmail(from_addr= my_email, to_addrs= "msd.pratham@gmail.com",
                    msg="Subject:Hello\n\n This is the content of my email")
connection.close()      # can avoid this by using with open.... as...    similar to opening files




# METHOD 2 =withoput the need to close mail... similar to opening files
with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:     # every email provider has a different smtp server... google it

    connection.starttls()   # TLS = transport layer security... way of securing email to our email server
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr= my_email,
                        to_addrs= "msd.pratham@gmail.com",
                        msg="Subject:Hello\n\n This is the content of my email")