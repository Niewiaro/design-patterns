def generate_banner(msg, style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')


def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def cow_style(msg):
    from cowpy import cow
    msg = cow.milk_random_cow(msg)
    return msg


def car_window_style(msg):
    # Center the message to fit the window (27 chars wide)
    window_msg = msg.center(23)
    art = [
        "                                              _____________",
        "                                  ..---:::::::-----------. ::::;;.",
        f"                               .'{window_msg} ;;   \\  \":._______,",
        "                            .''                          ;     \\   \"\\-----|;",
        "                          .'                            ;;      ;   \\\\  /|;",
        "                        .'                              ;   _____;   \\\\/|;",
        "                      .'                               :; ;\"     \\ ___:'.|",
        "                    .'--...........................    : =   ____:\"    \\ \\",
        "               ..-\"\"                               \"\"\"'  o\"\"\"     ;     ; :",
        "          .--\"\"  .----- ..----...    _.-    --.  ..-\"     ;       ;     ; ;",
        "       .\"\"_-     \"--\"\"-----'\"\"    _-\"        .-\"\"         ;        ;    .-.",
        "    .'  .'                      .\"         .\"              ;       ;   /. |",
        "   /-./'                      .\"          /           _..  ;       ;   ;;;|",
        "  :  ;-.______               /       _________==.    /_  \\ ;       ;   ;;;;",
        "  ;  / |      \"\"\"\"\"\"\"\"\"\"\".---.\"\"\"\"\"\"          :    /\" \". |;       ; _; ;;;",
        " /\"-/  |      *         /   /                  /   /     ;|;      ;-\" | ;';",
        ":-  :   \"\"\"----______  /   /              ____.   .  .\"'. ;;   .-\"..T\"   .",
        "'. \"  ___            \"\":   '\"\"\"\"\"\"\"\"\"\"\"\"    .   ; ; |  ;; ;.\" .\"   '--\"",
        " \",   __ \"\"\"  \"\"---... :- - - - - - - - - ' '  ; ;  ; | /;;\"  .\"",
        "  /. ;  \"\"\"---___                             ;  ; ; \\|/ ;|.\"\"",
        " :  \":           \"\"\"----.    .-------.       ;   ; ; /|\\ ;:",
        "  \\  '--__               \\   \\        \\     /    | ;/ | \\;;",
        "   '-..   \"\"\"\"---___      :   .______..\\ __/..-\"\"|  ; | ; ;",
        "       \"\"--..       \"\"\"--\"                      .   \".|. ;",
        "             \"\"------...                  ..--\"\"      \" :",
        "                        \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"    \\        /",
        "                                               \"------\""
    ]
    return "\n".join(art)

def main():
    styles = (dots_style, admire_style, cow_style, car_window_style)
    msg = 'happy coding'
    [generate_banner(msg, style) for style in styles]


if __name__ == '__main__':
    main()
