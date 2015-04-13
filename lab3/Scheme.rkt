#lang racket
; type in (f '(3 1 4 1 5 9))
(define (f lst)
  (display lst)
  (newline)
  ; (a) ;
  (if (null? lst)
      ; (b) ;
      '()
  ; (c) ;
  (cons (+ 1 (car lst)) (f (cdr lst)))))

; type in (member? 4 '(3 1 4 1 5 9))
(define (member? e lst)
  ; This is basically an else if statement ;
  (cond
    ; if the list is null, return false ;
    ((null? lst) #f)
    ; if e is equal to the first element in the list, return true;
    ((eq? e (car lst)) #t)
    ; if e is not equal to the first element in the list, return the recursive call of
    ; everything after the first element of the lsit ;
    (else (member? e (cdr lst))))
)
; type in (set? '(3 1 4 1 5 9))
(define (set? lst)
 (if #t "Fill this in" #t)
)