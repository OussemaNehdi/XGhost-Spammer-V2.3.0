# importing Modules
from tkinter import *  # for the GUI
from PIL import ImageTk, Image  # for the banner and the icon
from subprocess import call  # to call websites
from smtplib import SMTP_SSL  # to check if the gmail work and spam gmails
from validate_email import validate_email  # to check gmail of target (may cause error later cause we installed a module in order to have it (py3DNS))
from datetime import datetime  # to print the time when starting
from tkinter import messagebox  # to show errors
from threading import Thread
from time import sleep

# *_f = function / *_b = Button / *_v = Variable

# validate email Version: 1.3
# PIL version: 10.1.0
# tkinter version: 8.6
# pydns3 Version: 4.0.0

target_v_list = [""]
didwestop = False
MAX_ADDED_GMAILS = 10  # sufficient. you can change this to a higher number


# add built in gmails manually here (HARD CODE)
ghostslist = []  # manually add emails
ghostspasslist = []  # manually add app passwords (16 digit)
a = 1
gmailslist = []  # added automatically by user


win = Tk()
var_a = False  # Ghosts are running
v_run = True
sp_nu = IntVar()
sp_nu.set(0)


def start_f():  # launch ghosts,

    global didwestop
    global var_a, server
    global target_v, msg_v, on_of_v, seconds_v
    global target_v_list

    didwestop = False

    #################### Deleting output to be ready for next operation ############
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=7, column=0, columnspan=4, sticky="w")
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=8, column=0, columnspan=4, sticky="w")
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=9, column=0, columnspan=4, sticky="w")
    Label(
        win,
        text=">>>                                                                                                                   ",
        fg="white",
        bg="black",
        font=3,
    ).grid(row=10, column=0, columnspan=4, sticky="w")
    ################################################
    ping = call("ping -n 1 google.com", shell=True)
    if ping == 1:
        messagebox.showerror(
            "XGhost Spammer", "There is no Internet connection"
        )  # NO network.
    else:
        if (
            "|" not in e_target.get()
        ):  # since it's an advanced feature to multi spam we trust the user with the input
            is_valid = validate_email(e_target.get())
            if is_valid == True:  # put time and receiver

                if int(var_c1.get()) == 1:
                    try:  # isnum check (implementation after bug fix instead of isnum)
                        abs(int(e_s.get()))
                    except:
                        c_n = False
                    else:
                        c_n = True
                    if c_n == True:
                        server = SMTP_SSL("smtp.gmail.com", 465)

                        var_a = True
                        timenow = datetime.now()
                        l2 = ">>>   Started at " + str(timenow)
                        l3 = ">>>   Sending " + str(e_target.get()) + " ..."
                        Label(win, text=l2, fg="white", bg="black", font=3).grid(
                            row=7, column=0, columnspan=4, sticky="w"
                        )
                        Label(win, text=l3, fg="white", bg="black", font=3).grid(
                            row=8, column=0, columnspan=4, sticky="w"
                        )

                        stop_b.configure(
                            state=NORMAL
                        )  # ----------DISABLING FOR NO ERRORS-------

                        start_b.configure(state=DISABLED)
                        add_b.configure(state=DISABLED)
                        e_target.configure(state=DISABLED)
                        e_msg.configure(state=DISABLED)
                        e_s.configure(state=DISABLED)
                        c1.configure(state=DISABLED)
                        r_ghosts.configure(state=DISABLED)
                        r_gmails.configure(state=DISABLED)
                        o_ghosts.configure(state=DISABLED)
                        o_gmails.configure(state=DISABLED)

                        target_v = e_target.get()

                        msg_v = e_msg.get()
                        on_of_v = var_c1.get()
                        seconds_v = e_s.get()

                        # ------------------------RUNNING THREADS-----------------------

                        # make threads

                        send_f()

                    else:
                        messagebox.showerror(
                            "XGhost Spammer", "Time Delay must be a number"
                        )

                else:
                    server = SMTP_SSL("smtp.gmail.com", 465)

                    send_f()

                    var_a = True
                    timenow = datetime.now()
                    l2 = ">>>   Started at " + str(timenow)
                    l3 = ">>>   Spamming " + str(e_target.get()) + " ..."
                    Label(win, text=l2, fg="white", bg="black", font=3).grid(
                        row=7, column=0, columnspan=4, sticky="w"
                    )
                    Label(win, text=l3, fg="white", bg="black", font=3).grid(
                        row=8, column=0, columnspan=4, sticky="w"
                    )
                    stop_b.configure(
                        state=NORMAL
                    )  # ----------DISABLING FOR NO ERRORS-------

                    start_b.configure(state=DISABLED)
                    add_b.configure(state=DISABLED)
                    e_target.configure(state=DISABLED)
                    e_msg.configure(state=DISABLED)
                    e_s.configure(state=DISABLED)
                    c1.configure(state=DISABLED)
                    r_ghosts.configure(state=DISABLED)
                    r_gmails.configure(state=DISABLED)
                    o_ghosts.configure(state=DISABLED)
                    o_gmails.configure(state=DISABLED)
                    # --------------------------ALL THE WORK ON START--------------
                    target_v = e_target.get()
                    msg_v = e_msg.get()
                    on_of_v = var_c1.get()
                    seconds_v = e_s.get()

            else:
                messagebox.showerror(
                    "XGhost Spammer", "The target Gmail account doesn't exist"
                )

        else:
            if int(var_c1.get()) == 1:
                try:  # isnum check (implementation after bug fix instead of isnum)
                    abs(int(e_s.get()))
                except:
                    c_n = False
                else:
                    c_n = True
                if c_n == True:
                    server = SMTP_SSL("smtp.gmail.com", 465)

                    var_a = True
                    timenow = datetime.now()
                    l2 = ">>>   Started at " + str(timenow)
                    l3 = ">>>   Sending " + str(e_target.get()) + " ..."
                    Label(win, text=l2, fg="white", bg="black", font=3).grid(
                        row=7, column=0, columnspan=4, sticky="w"
                    )
                    Label(win, text=l3, fg="white", bg="black", font=3).grid(
                        row=8, column=0, columnspan=4, sticky="w"
                    )

                    stop_b.configure(
                        state=NORMAL
                    )  # ----------DISABLING FOR NO ERRORS-------

                    start_b.configure(state=DISABLED)
                    add_b.configure(state=DISABLED)
                    e_target.configure(state=DISABLED)
                    e_msg.configure(state=DISABLED)
                    e_s.configure(state=DISABLED)
                    c1.configure(state=DISABLED)
                    r_ghosts.configure(state=DISABLED)
                    r_gmails.configure(state=DISABLED)
                    o_ghosts.configure(state=DISABLED)
                    o_gmails.configure(state=DISABLED)

                    target_v = e_target.get()

                    target_v_list = target_v.split("|")
                    print("inside start function : ")
                    print(target_v_list)

                    msg_v = e_msg.get()
                    on_of_v = var_c1.get()
                    seconds_v = e_s.get()

                    # ------------------------RUNNING THREADS-----------------------

                    send_f()  # create threads

                else:
                    messagebox.showerror(
                        "XGhost Spammer", "Time Delay must be a number"
                    )

            else:
                server = SMTP_SSL("smtp.gmail.com", 465)

                send_f()

                var_a = True
                timenow = datetime.now()
                l2 = ">>>   Started at " + str(timenow)
                l3 = ">>>   Spamming " + str(e_target.get()) + " ..."
                Label(win, text=l2, fg="white", bg="black", font=3).grid(
                    row=7, column=0, columnspan=4, sticky="w"
                )
                Label(win, text=l3, fg="white", bg="black", font=3).grid(
                    row=8, column=0, columnspan=4, sticky="w"
                )
                stop_b.configure(
                    state=NORMAL
                )  # ----------DISABLING FOR NO ERRORS-------

                start_b.configure(state=DISABLED)
                add_b.configure(state=DISABLED)
                e_target.configure(state=DISABLED)
                e_msg.configure(state=DISABLED)
                e_s.configure(state=DISABLED)
                c1.configure(state=DISABLED)
                r_ghosts.configure(state=DISABLED)
                r_gmails.configure(state=DISABLED)
                o_ghosts.configure(state=DISABLED)
                o_gmails.configure(state=DISABLED)
                # --------------------------ALL THE WORK ON START--------------
                target_v = e_target.get()
                target_v_list = target_v.split("|")
                print("inside start function : ")
                print(target_v_list)
                msg_v = e_msg.get()
                on_of_v = var_c1.get()
                seconds_v = e_s.get()


def send_f():  # start threads (send emails)

    if r.get() == 1:
        n1 = drop_gh.get()  # built in gmails
        for i in range(n1):
            t = Thread(target=ghost, args=[ghostslist[i], ghostspasslist[i]])
            t.daemon = True
            t.start()

    if r.get() == 2:
        n2 = drop_gm.get()  # added gmails
        for i in range(n2):
            t = Thread(target=gmail, args=[gmailslist[i][0], gmailslist[i][1]])
            t.daemon = True
            t.start()


def ghost(ghost_gmail, pwd):  # thread for built in gmails
    print(ghost_gmail, pwd)
    print("in ghosts")
    print(target_v_list)
    global didwestop
    server.login(ghost_gmail, pwd)

    if on_of_v == 0:  # no delay
        if "|" in target_v:
            while True:
                for t in target_v_list:
                    server.sendmail(ghost_gmail, t, msg_v)
                    sp_nu.set(sp_nu.get() + 1)
                    l_spam = Label(
                        win,
                        text="Sent " + str(sp_nu.get()) + " Emails",
                        fg="white",
                        bg="black",
                    ).grid(row=5, column=2)

                    print(didwestop)

                    if didwestop == True:
                        return

        else:

            while True:

                server.sendmail(ghost_gmail, target_v, msg_v)
                sp_nu.set(sp_nu.get() + 1)

                l_spam = Label(
                    win,
                    text="Sent " + str(sp_nu.get()) + " Emails",
                    fg="white",
                    bg="black",
                ).grid(row=5, column=2)

                print(didwestop)

                if didwestop == True:
                    break

    else:  # with delay
        if "|" in target_v:
            while True:
                for t in target_v_list:
                    server.sendmail(ghost_gmail, t, msg_v)
                    print("sent")
                    l_spam = Label(
                        win,
                        text="Sent " + str(sp_nu.get()) + " Emails",
                        fg="white",
                        bg="black",
                    ).grid(row=5, column=2)
                    sleep(int(seconds_v))
                    # Add here also
                    sp_nu.set(sp_nu.get() + 1)
                    if didwestop == True:
                        break

        else:
            while True:
                server.sendmail(ghost_gmail, target_v, msg_v)
                print("sent")
                l_spam = Label(
                    win,
                    text="Sent " + str(sp_nu.get()) + " Emails",
                    fg="white",
                    bg="black",
                ).grid(row=5, column=2)
                sleep(int(seconds_v))
                # Add here also
                sp_nu.set(sp_nu.get() + 1)
                if didwestop == True:
                    break


def gmail(user, passwd):  # thread for user gmails
    print("inside gmails")
    print(target_v_list)

    server.login(user, passwd)
    if on_of_v == 0:  # no delay
        if "|" in target_v:
            print("|")

            while True:

                for t in target_v_list:
                    print("hey")
                    print(t)
                    server.sendmail(user, t, msg_v)
                    l_spam = Label(
                        win,
                        text="Sent " + str(sp_nu.get()) + " Emails",
                        fg="white",
                        bg="black",
                    ).grid(row=5, column=2)

                    sp_nu.set(sp_nu.get() + 1)
                    if didwestop == True:
                        return
        else:
            while True:

                server.sendmail(user, target_v, msg_v)
                l_spam = Label(
                    win,
                    text="Sent " + str(sp_nu.get()) + " Emails",
                    fg="white",
                    bg="black",
                ).grid(row=5, column=2)

                sp_nu.set(sp_nu.get() + 1)
                if didwestop == True:
                    break

    else:  # with delay
        if "|" in target_v:

            while True:
                for t in target_v_list:
                    server.sendmail(user, t, msg_v)
                    l_spam = Label(
                        win,
                        text="Sent " + str(sp_nu.get()) + " Emails",
                        fg="white",
                        bg="black",
                    ).grid(row=5, column=2)
                    sp_nu.set(sp_nu.get() + 1)
                    sleep(int(seconds_v))
                    if didwestop == True:
                        return
        else:
            while True:
                server.sendmail(user, target_v, msg_v)
                l_spam = Label(
                    win,
                    text="Sent " + str(sp_nu.get()) + " Emails",
                    fg="white",
                    bg="black",
                ).grid(row=5, column=2)

                sp_nu.set(sp_nu.get() + 1)
                sleep(int(seconds_v))
                if didwestop == True:
                    break


# -------------------------------------INFO-----------EXIT BUTTONS--------------------------------------------


def exit_b():
    closing()
    pass


def info_b():
    # Open the website
    cmd = "ws_xg\\project.html"
    call(cmd, shell=True)


def closing():
    if var_a == False:  # the user is not currently sending emails
        win.destroy()

    if var_a == True:  # the user is sending emails
        ok = messagebox.askokcancel("", "Are you sure you want to end the operation")
        if ok == 0:
            pass
        else:
            win.destroy()


# ------------------------------ start and stop ------------------------------------
def stop_f():  # stop button function
    global var_a, v_run, didwestop
    # EDIT
    didwestop = True
    # END EDIT

    var_a = False
    v_run = False

    l4 = ">>>   Stopped at " + str(datetime.now())

    l5 = ">>>   Sent " + str(sp_nu.get()) + " Message"
    Label(win, text=l4, fg="white", bg="black", font=3).grid(
        row=9, column=0, columnspan=4, sticky="w"
    )
    Label(win, text=l5, fg="white", bg="black", font=3).grid(
        row=10, column=0, columnspan=4, sticky="w"
    )

    # ----
    start_b.configure(
        state=NORMAL
    )  # give time and how much messages and kill the ghosts
    stop_b.configure(state=DISABLED)  # ---------ENABLING FOR NEXT SET-------

    add_b.configure(state=NORMAL)
    e_target.configure(state=NORMAL)
    e_msg.configure(state=NORMAL)
    e_s.configure(state=NORMAL)
    c1.configure(state=NORMAL)
    r_ghosts.configure(state=NORMAL)
    r_gmails.configure(state=NORMAL)
    o_ghosts.configure(state=NORMAL)
    o_gmails.configure(state=NORMAL)
    # --------------------------------PROGRAM---------------


def add_f():  # for adding user gmails
    global add_win, a

    ############################ FUNCTIONS (3) ###########################
    texta = "Add Gmail Number " + str(a)

    def b_a_a_f():
        global a

        gmail = e_email.get()
        password = e_pass.get()

        pair = [gmail, password]

        gmailslist.append(pair)

        # deleting the input fields
        e_email.delete(0, END)
        e_pass.delete(0, END)
        ping1 = call("ping -n 1 google.com", shell=True)  # network check
        if ping1 == 1:
            messagebox.showerror(
                "XGhost Spammer", "There is no Internet connection"
            )  # NO network.
        else:
            server = SMTP_SSL("smtp.gmail.com", 465)
            try:
                server.login(gmail, password)
            except:
                messagebox.showerror(
                    "",
                    "Couldn't connect to this Gmail account, please make sure the password entered is the app password generated by gmail (16 digits) and not the default pasword",
                )
                e_email.insert(0, gmail)
                e_pass.insert(0, password)

            else:
                server.quit()

                a += 1
                if a == int(drop_gm.get()) + 1:
                    add_win_f()
                else:
                    texta = "Add Gmail Number " + str(a)
                    l_a_a = Label(add_win, text=texta, bg="gray").grid(row=1, column=1)

    def b_a_b_f():
        global a
        if a > 1:
            # deleting first
            e_email.delete(0, END)
            e_pass.delete(0, END)

            a -= 1

            pair = t[a - 1]
            gmail = pair[0]
            password = pair[1]

            t.pop(a - 1)

            e_email.insert(0, gmail)
            e_pass.insert(0, password)

            texta = "Add Gmail Number " + str(a)
            l_a_a = Label(add_win, text=texta).grid(row=1, column=1)

    ################################ ADD GMAIL WINDOW #####################################
    # ------------------------------ DESIGN ---------------------------------------
    # window
    add_win = Toplevel()
    add_win.protocol("WM_DELETE_WINDOW", add_win_f)
    add_win.title("Add Gmails")
    add_win.geometry("300x160")
    add_win.resizable(False, False)
    add_win.iconbitmap("pictures/icon.ico")
    add_win.configure(bg="gray")
    add_b.configure(state=DISABLED)
    ##### CREATING ITEMS
    # 2 buttons
    b_a_a = Button(add_win, text="Add", bg="gray", borderwidth=4, command=b_a_a_f)
    b_a_b = Button(add_win, text="Back", bg="gray", borderwidth=4, command=b_a_b_f)
    # 2 entries
    e_email = Entry(add_win, width=30, bg="silver")
    e_pass = Entry(add_win, show="•", width=30, bg="silver")
    # 3 label
    l_a_a = Label(add_win, text=texta, bg="gray")
    # --
    l_e = Label(add_win, text="Gmail Adress", bg="gray")
    l_p = Label(add_win, text="Password", bg="gray")

    # 4 white spaces
    fws = Label(add_win, text="", fg="gray", bg="gray")
    bsws = Label(add_win, text="", fg="gray", bg="gray")
    sws = Label(add_win, text="", fg="gray", bg="gray")
    tws = Label(add_win, text="", fg="gray", bg="gray")
    ##### POISITIONS
    fws.grid(row=0, column=0)
    bsws.grid(row=1, column=0)
    l_a_a.grid(row=1, column=1)
    l_e.grid(row=2, column=0)
    e_email.grid(row=2, column=1, pady=5)
    l_p.grid(row=3, column=0)
    e_pass.grid(row=3, column=1, pady=5)
    sws.grid(row=4, column=0)
    b_a_a.grid(row=5, column=2)
    tws.grid(row=5, column=1)
    b_a_b.grid(row=5, column=0)


# ---------------------------------------DISABLES-------------------------------------------
def add_win_f():
    add_b.configure(state=NORMAL)
    start_b.configure(state=NORMAL)
    add_win.destroy()


def check_f():  # disable/enable checkbutton
    if var_c1.get() == 1:  # disabling and enabling time
        e_s.configure(state=NORMAL)
    if var_c1.get() == 0:
        e_s.delete(0, END)
        e_s.configure(state=DISABLED)


def a_o_g():
    global gmailslist
    if r.get() == 1:  # disabling and enabling ghosts and gmails
        o_gmails.configure(state=DISABLED)
        o_ghosts.configure(state=NORMAL)
        add_b.configure(state=DISABLED)
        o_gmails.configure(state=DISABLED)
        if len(ghostslist) == 0:
            o_ghosts.configure(state=DISABLED)
        else:
            o_ghosts.configure(state=NORMAL)
        start_b.configure(state=NORMAL)
        try:
            add_win.destroy()
        except:
            pass

    if r.get() == 2:
        o_gmails.configure(state=NORMAL)
        o_ghosts.configure(state=DISABLED)
        add_b.configure(state=NORMAL)
        o_ghosts.configure(state=DISABLED)
        o_gmails.configure(state=NORMAL)
        start_b.configure(state=DISABLED)

        gmailslist = []  # reset when chosing user gmails option again


# GUI setup
# win = Tk()
win.geometry("760x450")
win.title("XGhost Spammer")
win.iconbitmap("pictures/icon.ico")
win.configure(bg="black")
win.resizable(False, False)
######################################---->>> DESIGN <----########################################
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# ------------------------------------------------BANNER-------------------------------------------------
# banner buton,images,and texts
b_info = Button(
    win, text="Info", command=info_b, padx=30, pady=10, fg="black", bg="silver"
)
b_exit = Button(
    win, text="Exit", command=exit_b, padx=31, pady=10, fg="black", bg="silver"
)

my_img = ImageTk.PhotoImage(Image.open("pictures/ban.png"))
banner_l = Label(image=my_img)
my_imge = ImageTk.PhotoImage(Image.open("pictures/imgg.png"))
ghost_l = Label(image=my_imge)


# Position of banner
banner_l.grid(row=0, column=1, rowspan=2)
ghost_l.grid(row=0, column=2, rowspan=2)
b_exit.grid(row=1, column=0)
b_info.grid(row=0, column=0)

# ------------------------------------------------INFORMATION----------------------------------------------(LABEL)
# frame label for the 2 inputs, frame setup
f_i = LabelFrame(win, text="Information", padx=98.5, pady=5, background="gray")
f_i.grid(row=2, column=0, columnspan=3, pady=0)
# 2 inputs
e_target = Entry(f_i, width=30, bg="gainsboro")
e_msg = Entry(f_i, width=30, bg="gainsboro")
# 2 labels
l_target = Label(f_i, text="Target Gmail  ", background="gray")
l_msg = Label(f_i, text="              Message ", padx=10, background="gray")
# Positioning all
l_target.grid(row=0, column=0)
l_msg.grid(row=0, column=2)
e_target.grid(row=0, column=1)
e_msg.grid(row=0, column=3)
# ------------------------------------------------TIME-----------------------------------------------------
f_t = LabelFrame(win, text="Time Delay", padx=265, pady=2, background="gray")
f_t.grid(row=3, column=0, columnspan=3, pady=0)
# making the time checkbox, the label of it, the input field and duration
var_c1 = IntVar()
l_c_b = Label(f_t, text="Use Time Delay ", bg="gray")  # label of checkbutton
c1 = Checkbutton(
    f_t, variable=var_c1, command=check_f, background="gray"
)  # checkbutton
l_s = Label(f_t, text="Seconds", background="gray")
e_s = Entry(f_t, width=10, bg="gainsboro", state=DISABLED)  # the entry of seconds
# positioning
l_c_b.grid(row=0, column=0)
c1.grid(row=0, column=1)
l_s.grid(row=0, column=2)
e_s.grid(row=0, column=3)
# --------------------------------------------------SENDER OPTIONS--------------------------------------------------------
# make a label for sender options
f_a = LabelFrame(win, text="Sender Options", padx=109, bg="gray")
f_a.grid(row=4, column=0, columnspan=4, pady=0)
# 2 check buttons and 2 drop down munus


drop_gh = IntVar()
drop_gh.set(1)

drop_gm = IntVar()
drop_gm.set(1)

r = IntVar()
r.set(1)

r_ghosts = Radiobutton(
    f_a,
    text="Use Built-in Gmails                  ",
    command=a_o_g,
    variable=r,
    value=1,
    bg="gray",
)  # Radio button
r_gmails = Radiobutton(
    f_a, text="Use My Own Gmails", command=a_o_g, variable=r, value=2, bg="gray"
)  # Radio Button
try:
    o_ghosts = OptionMenu(f_a, drop_gh, *range(1, len(ghostslist) + 1))
except:
    print("came here")
    o_ghosts = OptionMenu(f_a, drop_gh, 0)
    o_ghosts.configure(state=DISABLED)


o_gmails = OptionMenu(
    f_a, drop_gm, *range(1, MAX_ADDED_GMAILS)
)  # just using OptionMenu for symetric and beatiful UI although an input field would be more optimal


o_ghosts.configure(bg="gray")  # changing the background color
o_gmails.configure(bg="gray")
l_n_g = Label(f_a, text="Number Of Gmails                       ", bg="gray")
l_n_gh = Label(f_a, text="Number Of Gmails", bg="gray")
# positioning
r_ghosts.grid(row=0, column=0)
r_gmails.grid(row=0, column=1)
o_ghosts.grid(row=1, column=1, pady=10)
o_gmails.grid(row=1, column=3, pady=10)
l_n_g.grid(row=1, column=2)
l_n_gh.grid(row=1, column=0)
# ----------------------------------------- CONTROL ------------------
# output label
f_p = LabelFrame(win, padx=0, bg="gray")
f_p.grid(row=5, column=0, columnspan=4, pady=3)

# start button, Stop Button, show emails, spam Button and add emails Button

start_b = Button(f_p, text="Start", command=start_f, padx=15, pady=5, bg="silver")
stop_b = Button(
    f_p, text="Stop", command=stop_f, padx=15, pady=5, bg="silver", state=DISABLED
)
# show_b = Button(f_p,text="Show Spam Amount",command = show_spam_f,padx=15,pady=5,bg = "silver",state=DISABLED)
add_b = Button(
    f_p, text="Add Gmails", command=add_f, padx=15, pady=5, bg="silver", state=DISABLED
)
l_space = Label(f_p, text="", padx=50, bg="gray")


l_spam = Label(
    win, text="Sent " + str(sp_nu.get()) + " Emails", fg="white", bg="black"
).grid(row=5, column=2)


a_o_g()

# Positioning
start_b.grid(row=0, column=0)
stop_b.grid(row=0, column=1)
l_space.grid(row=0, column=2)
add_b.grid(row=0, column=3)
# ----------------------------------------- CONSOLE -------------------------


l_v_o = Label(
    win,
    text=">>>   XGhost Spammer 2020 Version 2.3.0  by Oussema Nehdi",
    fg="white",
    bg="black",
    font=3,
)
l_v_o.grid(row=6, column=0, columnspan=4, sticky="w")

l_s_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_s_o.grid(row=7, column=0, columnspan=4, sticky="w")

l_w_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_w_o.grid(row=8, column=0, columnspan=4, sticky="w")


l_e_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_e_o.grid(row=9, column=0, columnspan=4, sticky="w")


l_sp_o = Label(win, text=">>>", fg="white", bg="black", font=(3))
l_sp_o.grid(row=10, column=0, columnspan=4, sticky="w")

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
######################################---->>> BACKEND PROGRAM <----##################################

win.protocol("WM_DELETE_WINDOW", closing)  # command so we make some stuff when closing


messagebox.showinfo(
    "XGhost Spammer",
    "Spamming is ILLEGAL.\nPlease use this on your own Email accounts.\nThe programm Developer is not responsible for any damage caused by the users . Click Info for more Informations ",
)


# ----------------------------------------CREATING DATABASE--------------------------------------------
# EDIT : we no longer use database (Version 2.x.x)

# -------------------------------------INSERTING INFORMATIONS TO DATABASE---------------------------------
# EDIT : we no longer use database (Version 2.x.x)


mainloop()
