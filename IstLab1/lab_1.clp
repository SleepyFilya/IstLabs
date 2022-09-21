; ask the user a question with answer options
(deffunction ask-question (?question $?allowed-values)
    (print ?question)
    (bind ?answer (read))
    (if (lexemep ?answer) 
        then (bind ?answer (lowcase ?answer))
	    )
    (while (not (member$ ?answer ?allowed-values)) do
        (print ?question)
        (bind ?answer (read))
        (if (lexemep ?answer) 
            then (bind ?answer (lowcase ?answer))
		    )
	    )
    ?answer
    )

; ask the user a question with the answer options "Yes" or "No"
(deffunction yes-or-no (?question)
    (bind ?response (ask-question ?question yes no y n))
    (if (or (eq ?response yes) (eq ?response y))
        then yes 
        else no
	    )
    )

; rules for determining all the facts necessary for the conclusion

(defrule determenite-design
	(not (solution ?))
	(not (design ?))
	=>
	(assert (design (yes-or-no "Is laptop design important?: ")))
	)

(defrule determenite-unusual-color
	(not (solution ?))
	(design yes)
	(not (unusual-color ?))
	=>
	(assert (unusual-color (yes-or-no "Do you want a laptop with an unusual color?: ")))
	)

(defrule determenite-keyboard-backlight
	(not (solution ?))
	(design yes)
	(not (keyboard-backlight ?))
	=>
	(assert (keyboard-backlight (yes-or-no "Do you want a keyboard backlight?: ")))
	)

(defrule determenite-budget
	(not (solution ?))
	(not (budget ?))
	=>
	(assert (budget (yes-or-no "Do you need a more budget laptop option?: ")))
	)

(defrule determenite-for-work
	(not (solution ?))
	(design no)
	(not (for-work ?))
	=>
	(assert (for-work (yes-or-no "Do you need a laptop for work?: ")))
	)

(defrule determenite-display-size
	(not (solution ?))
	(design no)
	(for-work no)
	(not (display-size ?))
	=>
	(assert (display-size (ask-question "Choose the display size (13.3 / 15.6 / 17.3): " 13.3 15.6 17.3)))
	)

(defrule determenite-touchscreen
	(not (solution ?))
	(design no)
	(for-work yes)
	(not (touchscreen ?))
	=>
	(assert (touchscreen (yes-or-no "Need a touchscreen display?: ")))
	)

; rules for the general conclusion of the expert system

(defrule determenite-answer_type_1
	(not (solution ?))
	(and
		(budget yes)
		(keyboard-backlight yes)
		(design yes)
		(unusual-color yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you HP Pavilion 15-eh 1159ur 601D7EA" crlf)
	)

(defrule determenite-answer_type_2
	(not (solution ?))
	(and
		(budget no)
		(keyboard-backlight yes)
		(design yes)
		(unusual-color yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Swift 3 SF314-42-R7EN" crlf)
	)

(defrule determenite-answer_type_3
	(not (solution ?))
	(and
		(budget yes)
		(keyboard-backlight no)
		(design yes)
		(unusual-color yes)		
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Aspire 1 A115-32-P7AU" crlf)
	)

(defrule determenite-answer_type_4
	(not (solution ?))
	(and
		(budget no)
		(keyboard-backlight no)
		(design yes)
		(unusual-color yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Aspire 3 A315-56-33Z3" crlf)
	)

(defrule determenite-answer_type_5
	(not (solution ?))
	(and
		(unusual-color no)
		(keyboard-backlight yes)
		(design yes)
		(budget yes)	
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you HP Pavilion Aero 13-be0069ur" crlf)
	)

(defrule determenite-answer_type_6
	(not (solution ?))
	(and
		(budget no)
		(keyboard-backlight yes)
		(design yes)
		(unusual-color no)		
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Swift 3 SF314-43" crlf)
	)

(defrule determenite-answer_type_7
	(not (solution ?))
	(and
		(budget yes)
		(keyboard-backlight no)
		(design yes)
		(unusual-color no)		
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Aspire 3 A315-34-C9WH" crlf)
	)

(defrule determenite-answer_type_8
	(not (solution ?))
	(and
		(budget no)
		(keyboard-backlight no)
		(design yes)
		(unusual-color no)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Aspire 3 A315-34" crlf)
	)

(defrule determenite-answer_type_9
	(not (solution ?))
	(and
		(design no)
		(for-work no)
		(display-size 13.3)
		(budget yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Lenovo ThinkBook 13s G2 ITL" crlf)
	)

(defrule determenite-answer_type_10
	(not (solution ?))
	(and
		(design no)
		(for-work no)
		(display-size 13.3)
		(budget no)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you ASUS ZenBook Flip 13 UX363EA-HP785W" crlf)
	)

(defrule determenite-answer_type_11
	(not (solution ?))
	(and
		(design no)
		(for-work no)
		(display-size 15.6)
		(budget yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you ASUS R522MA-BQ862W" crlf)
	)

(defrule determenite-answer_type_12
	(not (solution ?))
	(and
		(design no)
		(for-work no)
		(display-size 15.6)
		(budget no)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you HUAWEI MateBook D 15" crlf)
	)

(defrule determenite-answer_type_13
	(not (solution ?))
	(and
		(design no)
		(for-work no)
		(display-size 17.3)
		(budget yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you HP 17-cp0125ur" crlf)
	)

(defrule determenite-answer_type_14
	(not (solution ?))
	(and
		(design no)
		(for-work no)
		(display-size 17.3)
		(budget no)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you HP 17-CP0138UR" crlf)
	)

(defrule determenite-answer_type_15
	(not (solution ?))
	(and
		(design no)
		(for-work yes)
		(touchscreen yes)
		(budget yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Lenovo IdeaPad Flex 5 14ITL05" crlf)
	)

(defrule determenite-answer_type_16
	(not (solution ?))
	(and
		(design no)
		(for-work yes)
		(touchscreen yes)
		(budget no)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you MSI Summit E16 Flip Evo A11MT-204RU" crlf)
	)

(defrule determenite-answer_type_17
	(not (solution ?))
	(and
		(design no)
		(for-work yes)
		(touchscreen no)
		(budget yes)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Aspire 3 A315-56" crlf)
	)

(defrule determenite-answer_type_18
	(not (solution ?))
	(and
		(design no)
		(for-work yes)
		(touchscreen no)
		(budget no)			
		)
	=>
	(assert (solution yes))
		(print "A laptop will do for you Acer Aspire 3 A315-23-R384" crlf)
	)